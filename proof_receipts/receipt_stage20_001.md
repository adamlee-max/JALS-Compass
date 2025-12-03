# Stage 20 Receipt — 2008 Financial Crisis (v1)

**Date:** 2025-12-03  
**Author:** JALS Compass (automated pipeline)  
**Reviewer:** Adam Lee (live terminal)  

## Scope
Replay of the 2006–2009 U.S. financial crisis using the Compass C_proxy EMA  
(span=4, hysteresis=0.12). Dataset: 6 major institutions spanning pre-crisis → collapse.

## Method
- Loaded `banks_2008_dataset_clean.csv`  
- Applied Compass C_proxy EMA  
- Generated trajectories + summary table  
- Collapse threshold fixed at **C_proxy < –0.25** (Stage-19 rule)  

## Results (final C_proxy EMA)
- **Lehman Brothers:** –0.469 → **Collapsed**  
- **Bear Stearns:** –0.411 → **Collapsed**  
- **JPMorgan Chase:** +0.189 → **Survived**  
- **Bank of America:** +0.213 → **Survived**  
- **Wells Fargo:** +0.257 → **Survived**  
- **Goldman Sachs:** +0.273 → **Survived**

**Accuracy:** 6 / 6 correct separation (100%)

Artifacts:
- `experiments/finance_2008/results/banks_2008_cproxy_trajectories.png`
- `experiments/finance_2008/results/banks_2008_summary.csv`

## Conclusion
The Compass cleanly separates failed vs surviving institutions in the largest  
modern financial collapse. Stage 20 is **complete and sealed**.
