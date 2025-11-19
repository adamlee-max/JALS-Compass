# Methods Addendum — Collective Dynamics Model (CDM)

This section describes the operational method used to simulate the Law of Sustainable Intelligence within the JALS Compass framework.

## 1. Collective Dynamics Model (CDM)

The CDM treats each invariant proxy as a dynamic variable updated through feedback between agents and environment.  
At each timestep *t*:

$begin:math:display$
ΔX_i(t) = λ_i · F_i(X, π, ξ_t)
$end:math:display$

where *λ_i* is the learning rate, *F_i* is the feedback function for invariant *i*, and *ξ_t* represents stochastic perturbations (noise or shocks).

The viability score *C(t, π)* is recomputed after each update, producing a time-series used to test resilience and recovery.

---

## 2. Pseudocode (simplified)

```python
# Collective Dynamics Model (Stage-5 prototype)

initialize_system()
for t in range(T):
    for invariant in invariants:
        X[invariant] += λ[invariant] * feedback(invariant, policy, noise[t])
    C[t] = sigmoid( α*E_m[t] + β*R[t] - γ*(Pr[t] + H[t] + G[t]) )
    log_state(t, C[t], X)
plot(C)
```

---

## 3. Figure 1 (description paragraph)

**Figure 1.** *Dynamic viability under stress and recovery.*  
The curve shows C(t, π) declining after a simulated disturbance (shock), then recovering as reciprocity (R) and exchange symmetry (Eₘ) dominate over loss factors (Pr, H, G).  
The shaded region marks the threshold C < 0.2 — below which the system is considered failing.  
Recovery above this line constitutes evidence of adaptive learning.

---

**Note:** CDM output and survival plots form the empirical backbone for the Anti-JALS null model in Step 4.