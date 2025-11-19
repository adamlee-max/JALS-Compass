# 🧩 Measurement Axiom Addendum (v5.2)
_JALS Compass · Stage 18 — Measurement Clarification_

### Purpose
This addendum formalises the Measurement Axiom for the JALS Compass and clarifies the relationship between the theoretical invariants (I_i) and their operational proxies (p_i). It closes the measurement-clarity gap identified in Stage 16 and aligns directly with the null-model experimental receipts created in Stage 17.

---

# 1. Statement of the Measurement Axiom

A measurement of an invariant must not introduce structure that is not already present in the system.

Equivalently:

> A proxy is valid if and only if it preserves the topology and sign of the underlying invariant under all admissible perturbations.

This ensures that measurement can reduce resolution but must never inject artefacts.  
It also guarantees that the viability functional C(t,π) is monotonic with respect to real system coherence, not measurement noise.

---

# 2. Mapping Invariants to Proxies

For each invariant I_i, a proxy p_i is admissible if:

1. **Local preservation:**  
   sign(p_i(Δs)) = sign(I_i(Δs)) for all small perturbations Δs.

2. **No artificial smoothness or sharpness:**  
   ∇p_i ≈ ∇I_i up to a monotone transform.

3. **Proxy degeneracy allowed:**  
   Loss of resolution (flatness) is acceptable.  
   Introduction of new gradients or discontinuities is not.

4. **Proxy-independence:**  
   The computation of C(t,π) must not depend on any specific choice of proxies.

This is exactly the condition satisfied by the Stage-17 null-model experiment, where all five invariants were replaced by simplified synthetic signals but topology and sign were preserved.

---

# 3. Measurement Pipeline (Operational)

Measurement proceeds in three steps:

### (1) System State Extraction  
Collect raw system data s(t) at time t.

### (2) Proxy Encoding  
Produce a vector of monotone-preserving proxies:  
p(t) = (p₁(t), …, p₅(t))

### (3) Viability Functional Application  
Feed proxies into the LSI viability functional C(t,π) to obtain the system’s coherence score.

This is exactly the pipeline implemented in:

experiments/null_model/null_model_sim.py

and confirmed in the empirical receipts.

---

# 4. Why This Addendum is Required

Peer-review notes (Stage 16) and AI-auditor commentary identified a consistent need:

“Clarify what counts as a valid measurement of an invariant.”

This addendum:

- Removes ambiguity between theory and proxies  
- Aligns manuscript v5.1 and codebase v5.2  
- Locks the Compass onto a single, rigorous measurement foundation  
- Demonstrates directly why the Anti-JALS null model collapses  
- Closes the final Tier-1 conceptual gap

---

# 5. Relationship to Empirical Receipts

The Stage-17 null-model experiment depends on this axiom:  
JALS preserves viability because proxies preserve the invariant topology.  
Anti-JALS collapses because it breaks the axiom.

Thus the empirical receipts do not merely demonstrate behaviour — they validate the axiom itself.

---

# 6. Versioning

Addendum Version: v5.2  
Applies to:
- Manuscript v5.1  
- Codebase v5.2.x  
- All future JALS Compass measurement specifications  

---

# End of Addendum v5.2