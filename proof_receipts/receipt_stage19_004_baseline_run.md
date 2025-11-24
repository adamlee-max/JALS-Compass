# Stage 19 — Baseline Hostile Environment Run (v1)

## Summary

This receipt verifies the baseline hostile-environment simulation using  
`hostile_env_sim_v1.py`.

This run validates:

- Correct file placement  
- Correct imports  
- Correct population initialisation  
- Correct survival-curve generation  
- Correct output of PNG + CSV  
- Correct C_proxy calculation  

## Run Outputs

- **PNG:** `experiments/hostile_env/results/hostile_env_survival_v1.png`  
- **CSV:** `experiments/hostile_env/results/hostile_env_survival_v1.csv`  
- **C_proxy (AUC-survival):** 0.365  

## Terminal Receipt

python3 hostile_env_sim_v1.py
[Stage19 v1] Saved plot: /workspaces/JALS-Compass/experiments/hostile_env/results/hostile_env_survival_v1.png
[Stage19 v1] Saved data: /workspaces/JALS-Compass/experiments/hostile_env/results/hostile_env_survival_v1.csv
[Stage19 v1] C_proxy (AUC-survival): 0.365