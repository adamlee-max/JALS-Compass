# 🧪 Hostile-Environment Experiments (Stage 19)

Stage 19 contains the stress-test simulations where environmental hostility is varied and increased — e.g. high attack probability, visibility asymmetry, noise, drift amplification, and other “anti-JALS” conditions.

The goal is to test whether coherence (C_proxy) still predicts survival under extreme conditions.These simulations include four modes:

- **Anti-JALS only** (`hostile_env_sim_anti_only.py`)
- **Mixed population** (`hostile_env_sim_mixed.py`)
- **Instant-knowledge agents** (`hostile_env_sim_instant.py`)
- **Baseline hostile environment** (`hostile_env_sim_v1.py`)
# 🧪 Hostile-Environment Experiments (Stage 19)

Stage 19 contains the stress-test simulations where environmental hostility is varied and increased — e.g. high attack probability, visibility asymmetry, noise, drift amplification, and other “anti-JALS” conditions.

The goal is to test whether coherence (C_proxy) still predicts survival under extreme conditions.

These simulations include four modes:

- **Anti-JALS only** (`hostile_env_sim_anti_only.py`)
- **Mixed population** (`hostile_env_sim_mixed.py`)
- **Instant-knowledge agents** (`hostile_env_sim_instant.py`)
- **Baseline hostile environment** (`hostile_env_sim_v1.py`)

---

## 📊 Stage 19 — Results Summary (v1)

This folder contains the v1 survival outputs for the Stage 19 stress-tests:

### **Instant-Knowledge Environment**
- `hostile_env_instant_v1.csv`
- `hostile_env_instant_v1.png`

### **Mixed Population Environment**
- `hostile_env_mixed_v1.csv`
- `hostile_env_mixed_v1.png`

### **Combined Comparison Plot**
Generated from both inputs using the comparison script:
- `proof_receipts/hostile_env_compare_v1.png`

---

## 🧾 Receipt Link (Stage 19-007)

The validated proof receipt for this comparison is:

`proof_receipts/receipt_stage19_007.md`

This completes Stage 19 (v1) and confirms that:

**Under hostile, mixed, and knowledge-asymmetric environments, coherence still predicts survival.**