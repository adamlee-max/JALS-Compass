# Stage 19 — Hostile Environment Experiments (Setup Receipt)

**Date:** November 2025  
**Author:** Adam Lee (+ Grok, GPT)

## Summary

This receipt records the creation of the Stage 19 hostile-environment
experiment scaffold.

- Folder created: `experiments/hostile_env/`
- Documentation added: `experiments/hostile_env/README.md`
- Simulation script added: `experiments/hostile_env/hostile_env_sim_v1.py`
- Script content: hostile-environment model with
  - JALS vs Anti-JALS agents
  - opacity / visibility effects
  - resource drain + attacks
  - hooks for dynamic weights, learning agents, instant-knowledge agents,
    and mixed populations.

## Status

- ✅ File + folder structure in place  
- ✅ Baseline hostile-environment simulation code added (from Grok run)  
- ⏳ Code **not yet executed** or validated in Codespaces  
- ⏳ Plots + summary stats to be generated in a later Stage 19 session

## Next Actions (Stage 19)

1. Open `hostile_env_sim_v1.py` in Codespaces and run baseline sim.  
2. Save survival / C_proxy plots into `experiments/hostile_env/`.  
3. Add a short `results` section to `hostile_env/README.md` with links
   to plots and key numbers.  
4. (Optional) Add separate scripts for:
   - dynamic weights
   - learning agents
   - instant-knowledge agents
   - mixed population runs
