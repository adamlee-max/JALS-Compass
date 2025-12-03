# Stage19_008 — Capstone Summary (v1)

**Scope**  
Stage 19 stress-tested the Compass under hostile conditions (attack/noise/asymmetry).  
We ran four v1 simulations and a comparison:

- `experiments/hostile_env/hostile_env_sim_v1.py`
- `experiments/hostile_env/hostile_env_sim_instant.py`
- `experiments/hostile_env/hostile_env_sim_mixed.py`
- `experiments/hostile_env/hostile_env_sim_anti_only.py`
- Combined comparison plot: `proof_receipts/hostile_env_compare_v1.png`

**Result**  
Across runs, survival curves diverge between ~200–280 steps; **Instant (total)** retains ~5–15 more survivors at collapse than **Mixed (total)**. This matches the Stage-19 prediction that higher effective coherence (**C_proxy**) correlates with survival.

**Conclusion**  
The Law holds under hostile, mixed, and knowledge-asymmetric environments.  
Stage 19 is complete and sealed. Cleared to proceed to **Stage 20 — 2008 Financial Crisis replay**.

**Receipt Links**  
- Instant run: `proof_receipts/receipt_stage19_005_instant_run.md`  
- Mixed run:   `proof_receipts/receipt_stage19_006_mixed_run.md`  
- Comparison:  `proof_receipts/receipt_stage19_007.md`

**Tag**  
`v5.1_stage19_receipt`
