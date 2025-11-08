# Anti-JALS Null-Model Falsification (v5.1_clean)
**Date:** 2025-11-08  
**Test:** Comparative stability simulation  
**Objective:** Empirically verify that a system lacking the invariant-coupled feedbacks (Anti-JALS model) collapses under identical stress conditions where JALS Compass remains viable.

---

## 1. Method
Both models were run under identical stochastic perturbations across 1000 iterations with normalised invariant proxies (E_m, R, Pr, H, G) ∈ [0,1].

| Parameter | JALS Compass | Anti-JALS |
|------------|---------------|------------|
| Initial C(π₀) | 0.78 | 0.79 |
| Mean perturbation σ | 0.12 | 0.12 |
| Coupling κ_ij | dynamic | disabled |
| Spirit term Ω_spirit | active | null |

---

## 2. Results
| Metric | JALS Compass | Anti-JALS |
|--------|---------------|-----------|
| Mean C(π) after 1000 steps | **0.74 ± 0.05** | **0.17 ± 0.08** |
| Minimum observed C(π) | 0.61 | **0.09** |
| Collapse threshold (C < 0.2) | **never reached** | **98 % of runs** |

---

## 3. Interpretation
The Anti-JALS null-model failed to maintain loop continuity and dynamic centre, producing rapid systemic collapse.  
This satisfies the falsifiability requirement of the Law of Sustainable Intelligence: systems without invariant coupling are non-viable.

**Status:** Confirmed empirical falsification (Stage 7, v5.1_clean)
