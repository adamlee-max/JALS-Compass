# 🧪 Hostile-Environment Experiments (Stage 19)

This folder contains the simulations where environmental hostility is varied and stress-tested — e.g., high attack probability, visibility asymmetry, noise, drift amplification, resource decay, and other “anti-JALS” conditions.

Stage 19 currently includes **four simulation variants**, each with placeholder scripts and ready to be executed in Codespaces:

## 1. `hostile_env_sim_anti_only.py`
Pure Anti-JALS population under hostile pressure.
- Purpose: test collapse behaviour when no JALS-aligned dynamics exist  
- Expected: fast decline of C_proxy, accelerated resource failure  
- Status: placeholder only (to be executed in Codespaces)

## 2. `hostile_env_sim_instant.py`
Instant-knowledge JALS agents vs hostiles.
- Purpose: stress-test LSI under unfair advantage (omniscient Anti-JALS)  
- Expected: JALS survives only if Recurrence + Loop-Continuity mechanisms are strong  
- Status: placeholder only

## 3. `hostile_env_sim_mixed.py`
Mixed population: JALS + Anti-JALS + noise agents.
- Purpose: tests group-level dynamics, drift, and restoration  
- Expected: JALS cluster survives if Dynamic-Centre + Pattern-Sufficiency remain stable  
- Status: placeholder only

## 4. `hostile_env_sim_v1.py`
Baseline hostile-environment model.
- Purpose: first adversarial test environment  
- Expected: separation of coherent vs incoherent agents under continuous stress  
- Status: placeholder only

---

## 🗂 Results Directory

All output plots, CSVs, and summary statistics will be stored in:
