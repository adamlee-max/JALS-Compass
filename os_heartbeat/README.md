# Stage 21 — JALS-OS Heartbeat (v0.1.3)

Prospective heartbeat that computes `C_proxy` each minute, logs JSONL, keeps hourly receipts, and serves a tiny dashboard (`public/status.json` + `public/index.html`). Canonical weights, PID lock, EMA + hysteresis, atomic writes.

## Run
chmod +x os_heartbeat/daemon.py
nohup ./os_heartbeat/daemon.py &

## Stop (clean)
kill "$(cat os_heartbeat/heartbeat.pid)"

## Files
- daemon.py — heartbeat daemon
- logs/heartbeat_YYYYMMDD.jsonl — minute events (code SHA + git commit)
- receipts/receipt_YYYYMMDDTHH.json — hourly first-seen snapshots
- public/status.json / public/index.html — live status

## Status bands
- green: C_ema ≥ +0.20
- amber: between green and red
- red: C_ema ≤ −0.25
