#!/usr/bin/env python3
"""
JALS-OS Stage 21 — Public Heartbeat Daemon v0.1.3
- Canonical weights (Stage-21 lock)
- PID lock (single instance)
- JSONL logs + hourly first-seen receipts
- Public status.json + tiny dashboard (atomic writes)
- Git commit + code sha256 in every event
- EMA + hysteresis; collapse threshold aligned with prior stages
"""

import json, os, random, signal, sys, time, hashlib, subprocess
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path

# CI/autostart flags
import os
CI = os.getenv("CI", "").lower() == "true"
AUTOSTART = os.getenv("HEARTBEAT_AUTOSTART", "1") == "1"

# ---- config / thresholds ----
EMA_SPAN   = 4
HYSTERESIS = 0.12
COLLAPSE   = -0.25   # consistent with prior stages

# ---- directories ----
ROOT        = Path(__file__).resolve().parent
LOG_DIR     = ROOT / "logs"
RECEIPT_DIR = ROOT / "receipts"
PUBLIC_DIR  = ROOT / "public"
PID_FILE    = ROOT / "heartbeat.pid"

for d in (LOG_DIR, RECEIPT_DIR, PUBLIC_DIR):
    d.mkdir(parents=True, exist_ok=True)

# ---- canonical weights (locked for Stage 21) ----
WEIGHTS = {"Em": 0.30, "R": 0.30, "Pr": -0.20, "H": -0.10, "G": -0.10}

# ---- dummy signal generator ----
@dataclass
class Signals:
    Em: float; R: float; Pr: float; H: float; G: float

    @staticmethod
    def random_walk(prev=None, step=0.04, revert=0.005):
        def move(x):
            x += random.uniform(-step, step)
            x -= revert * x  # light mean reversion
            return max(-1.0, min(1.0, x))
        if prev is None:
            return Signals(*[random.uniform(-0.15, 0.15) for _ in range(5)])
        return Signals(*(move(getattr(prev, k)) for k in "Em R Pr H G".split()))
        # ---- C_proxy computation ----
def c_proxy(s: Signals) -> float:
    return sum(WEIGHTS[k] * getattr(s, k) for k in WEIGHTS)

# ---- git provenance ----
def git_hash() -> str:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=ROOT,
            text=True
        )
        return out.strip()
    except Exception:
        return "no-git"

CODE_HASH = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
GIT_HASH  = git_hash()

# ---- EMA + hysteresis ----
def ema_update(prev_ema, x, span=EMA_SPAN):
    alpha = 2/(span+1)
    return x if prev_ema is None else (alpha*x + (1-alpha)*prev_ema)

def hysteresis_clip(prev_ema, ema, threshold=COLLAPSE, hysteresis=HYSTERESIS):
    # prevents single noisy dips from flipping status to red
    if prev_ema is not None and prev_ema >= threshold and ema < threshold:
        return max(ema, threshold + hysteresis)
    return ema

def status_from_c(c: float) -> str:
    if c >= 0.20:
        return "green"
    if c <= COLLAPSE:
        return "red"
    return "amber"

# ---- atomic file write ----
def atomic_write(path: Path, data: str):
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(data, encoding="utf-8")
    os.replace(tmp, path)

# ---- JSONL append ----
def append_jsonl(path: Path, obj: dict) -> None:
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")

# ---- single-instance PID lock ----
def acquire_lock():
    if PID_FILE.exists():
        try:
            old_pid = int(PID_FILE.read_text())
            os.kill(old_pid, 0)  # raises if not active
            print("Another heartbeat instance is already running. Exiting.")
            sys.exit(1)
        except (ProcessLookupError, ValueError):
            # stale PID file
            pass
    PID_FILE.write_text(str(os.getpid()))
# ---- dashboard scaffold ----
STATUS_FILE = PUBLIC_DIR / "status.json"
INDEX_FILE  = PUBLIC_DIR / "index.html"

INDEX_FILE.write_text("""<!doctype html><meta charset="utf-8"><title>JALS-OS Stage 21</title>
<h1>JALS-OS Stage 21 — Live</h1>
<pre id="out"></pre>
<script>
setInterval(()=>fetch('status.json').then(r=>r.json()).then(d=>{
  document.getElementById('out').textContent =
    `C_proxy (EMA) = ${d.C_ema.toFixed(4)} [${d.status}]\\n` +
    `C_proxy (raw) = ${d.C_proxy_raw.toFixed(4)}\\n` +
    `${new Date(d.ts)} UTC`;
}), 5000);
</script>""", encoding="utf-8")

# ---- run state ----
RUN = True

def stop(*_):
    global RUN
    RUN = False

# Trap CTRL+C and termination
for s in (signal.SIGINT, signal.SIGTERM):
    signal.signal(s, stop)

# ---- startup banner ----
prev = None
prev_ema = None
start_time = datetime.now(timezone.utc).isoformat()

print("[Stage21 v0.1.3] Public daemon started — prospective experiment live", flush=True)

# ---- core loop entrypoint (full logic added in chunk 4) ----
def loop(interval_sec: int = 60):
    global prev, prev_ema
    while RUN:
        now = datetime.now(timezone.utc)

        # update signals
        prev = Signals.random_walk(prev)
        c_raw = c_proxy(prev)

        # EMA + hysteresis
        c_ema = ema_update(prev_ema, c_raw)
        c_ema = hysteresis_clip(prev_ema, c_ema)
        prev_ema = c_ema

        # construct event dictionary (written in chunk 4)
        event = {
            "ts": now.isoformat(),
            "C_proxy_raw": round(c_raw, 6),
            "C_ema": round(c_ema, 6),
            "status": status_from_c(c_ema),
            "signals": asdict(prev),
            "weights": WEIGHTS,
            "daemon_version": "stage21_v0.1.3",
            "code_sha256": CODE_HASH,
            "git_commit": GIT_HASH,
            "stage21_start": start_time
        }

        # writing and sleeping logic in chunk 4
                # append to log
        append_jsonl(LOG_DIR / f"heartbeat_{now:%Y%m%d}.jsonl", event)

        # public status (atomic)
        atomic_write(STATUS_FILE, json.dumps(event, indent=2))

        # hourly first-seen receipt (atomic)
        hour = now.strftime("%Y%m%dT%H")
        rp = RECEIPT_DIR / f"receipt_{hour}.json"
        if not rp.exists():
            atomic_write(rp, json.dumps(event, indent=2))

        # console pulse
        print(f"{now}  C_ema = {c_ema:+.4f}  [{event['status']}]", flush=True)

        # exact-interval sleep (monotonic)
        deadline = time.monotonic() + int(os.environ.get("INTERVAL_SEC", "60"))
        while RUN and time.monotonic() < deadline:
            time.sleep(0.2)

# ---- launcher / shutdown ----
def heartbeat_loop():
    acquire_lock()
    try:
        loop()
    finally:
        try:
            PID_FILE.unlink(missing_ok=True)
        except Exception:
            pass
        print("[Stage21] Stopped. Receipts preserved.", flush=True)

if __name__ == "__main__" and AUTOSTART and not CI:
    heartbeat_loop()