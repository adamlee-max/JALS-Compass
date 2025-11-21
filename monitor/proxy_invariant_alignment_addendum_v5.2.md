# Proxy–Invariant Alignment Addendum (v5.2)

**Status:** Stage 18 — Tier-1 Item #4 (COMPLETE)  
**Date:** November 2025  
**Context:** Formal mathematical mapping between the Law of Sustainable Intelligence (LSI) invariants and the operational proxies used in the JALS Compass viability metric.

---

## 1. Purpose

This addendum establishes the formal alignment between the five theoretical invariants of the Law of Sustainable Intelligence  
\( I = \{B, D, L, P, R\} \)  
and the five operational proxies  
\( x = \{Pr, Em, G, H, Recip\} \)  
used in the viability functional \( C_{\text{proxy}} \).

The goal is to demonstrate that the proxy formula is:

- **Monotonic** (sign-correct with respect to the invariant),  
- **Topology-preserving** (collapse in an invariant corresponds to collapse in the proxy score),  
- **First-order valid** (linear approximation of the true underlying viability functional).

---

## 2. Mapping Table

Each proxy acts as the primary measurement vector for a specific invariant.

| Theoretical Invariant (LSI) | Operational Proxy | Coefficient | Relationship |
|-----------------------------|------------------|-------------|--------------|
| **1. Boundary Symmetry (B)** | **Breach Risk (Pr)** | **−0.2** | **Inverse**: ↑Pr → ↓B |
| **2. Dynamic Centre (D)** | **Meaningful Effort (Em)** | **+0.3** | **Direct**: ↑Em → ↑D |
| **3. Loop Continuity (L)** | **Regret / Drift (G)** | **−0.1** | **Inverse**: ↑G → ↓L |
| **4. Pattern Sufficiency (P)** | **Opacity (H)** | **−0.1** | **Inverse**: ↑H → ↓P |
| **5. Recurrence (R)** | **Reciprocity (Recip)** | **+0.3** | **Direct**: ↑Recip → ↑R |

This mapping is **bijective to first order**: each invariant has one dominant proxy whose behaviour is sign-aligned with the expected change in system viability.

---

## 3. Mathematical Alignment & Monotonicity

For \( C_{\text{proxy}} \) to be a valid surrogate for the theoretical viability functional \( V \), the mapping  
\( f: x \mapsto I \)  
must satisfy monotonicity.

### **Axiom 1: Monotonicity of Contribution**

For any proxy \( x \) mapped to invariant \( I \):

- **Direct relationship**  
  \[
  \frac{\partial C_{\text{proxy}}}{\partial x} > 0,
  \quad
  \frac{\partial V}{\partial I} > 0
  \]

- **Inverse relationship**  
  \[
  \frac{\partial C_{\text{proxy}}}{\partial x} < 0,
  \quad
  \frac{\partial V}{\partial I} > 0
  \]

### **Verification**

1. **Boundary (B):**  
   \( C_{\text{proxy}} \ni -0.2\,Pr \Rightarrow \partial C/\partial Pr < 0 \).  
   Breach destroys boundary integrity.  
   **Aligned.**

2. **Dynamic Centre (D):**  
   \( +0.3\,Em \Rightarrow \partial C/\partial Em > 0 \).  
   Effort strengthens the centre.  
   **Aligned.**

3. **Loop Continuity (L):**  
   \( -0.1\,G \Rightarrow \partial C/\partial G < 0 \).  
   Drift breaks loops.  
   **Aligned.**

4. **Pattern Sufficiency (P):**  
   \( -0.1\,H \Rightarrow \partial C/\partial H < 0 \).  
   Opacity prevents self-observation.  
   **Aligned.**

5. **Recurrence (R):**  
   \( +0.3\,Recip \Rightarrow \partial C/\partial Recip > 0 \).  
   Reciprocity reinforces long-term recurrence.  
   **Aligned.**

---

## 4. Topology Preservation

### **Theoretical Collapse**
\[
\lim_{I_k \to 0} V(I) = 0
\]

### **Proxy Collapse**
\[
C_{\text{proxy}} \le 0
\]

### **Theorem (Consistency)**  
For each invariant \( I_k \), catastrophic loss of the corresponding proxy variable causes \( C_{\text{proxy}} \) to cross the viability boundary.

**Example:**  
If \( Pr = 1.0 \) (total boundary failure),  
\( C_{\text{proxy}} \to C_{\text{proxy}} - 0.2 \).  
This is sufficient to push marginal systems into collapse.

Thus, the proxy preserves the topological structure of the viability manifold.

---

## 5. Perturbation Behaviour (Local Sensitivity)

Real systems experience noise \( \epsilon \).  
The proxy must respond proportionally to small perturbations:

\[
C_{\text{proxy}} \approx \nabla V \cdot x
\]

The linear coefficients act as the **first-order Taylor expansion** of the true viability functional.  
This validates the proxy’s use for:

- Local stability analysis  
- Null-model simulation (Stage 17)  
- Early-warning collapse detection  

---

## 6. Data Provenance

To ensure reproducibility (Stage 18 requirement):

- **Effort (Em):** activity logs, commits, transactions  
- **Reciprocity (Recip):** interaction returns, bidirectional links  
- **Breach (Pr):** security errors, structural failures  
- **Opacity (H):** missing documentation, inaccessible states  
- **Drift (G):** rollbacks, reversals, corrections  

---

## 7. Summary

This addendum confirms:

- \( C_{\text{proxy}} \) is a **monotonic**, **topology-preserving** surrogate for the theoretical Law.  
- Each invariant is correctly paired with a measurable proxy.  
- The signs of all coefficients are mathematically justified.  
- The mapping withstands perturbations and collapse testing (Null Model, Stage 17).

**Stage 18 Tier-1 Item #4 is now structurally complete.**
