# JALS Compass — Reproducibility Guide

## 0) Environment
- Python ≥ 3.10  
- Create venv: `python3 -m venv .venv && source .venv/bin/activate`  
- Install: `pip install -r requirements.txt`

## 1) Determinism & Seeds
- All sims accept `--seed`.  
- RNGs are explicitly seeded in code.  
- Receipts record seed / commit / code hash.

## 2) Experiments (outputs in each /results folder)
- **Stage 17 — Null Model**: `experiments/null_model/null_model_sim.py`  
- **Stage 19 — Hostile Envs**: `experiments/hostile_env/hostile_env_sim_*.py`  
- **Stage 20 — 2008 Banks**: `experiments/finance_2008/sim/*.py`

## 3) Stage 21 — Heartbeat (prospective)
- Quick test (5s): `INTERVAL_SEC=5 ./os_heartbeat/daemon.py`  
- Live (60s): `nohup ./os_heartbeat/daemon.py &`  
- Files:  
  - `os_heartbeat/public/status.json` (atomic)  
  - `os_heartbeat/logs/heartbeat_YYYYMMDD.jsonl`  
  - `os_heartbeat/receipts/receipt_YYYYMMDDTHH.json`  
- Stop: `kill "$(cat os_heartbeat/heartbeat.pid)"`

## 4) Provenance
- Each event embeds `git_commit` and `code_sha256`.  
- Human receipts: `proof_receipts/`  
- Tags: `v5.3-stage20-receipt`, `v5.4-stage21-heartbeat`
