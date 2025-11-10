---
title: "JALS Compass × Law of Sustainable Intelligence"
subtitle: "A measurable law for system viability with operational receipts (v5.1_final)"
authors:
  - "Adam Lee"
date: 2025-11-10
keywords: ["complex systems", "AI safety", "viability", "alignment", "Lyapunov drift", "governance"]
documentclass: article
geometry: margin=1in
toc: true
toc-depth: 2
linkcolor: blue
urlcolor: blue
---

# Abstract@adamlee-max ➜ /workspaces/JALS-Compass (stage16-manuscript) $ cat submission_v5.1_final/abstract.md
# Abstract — Law of Sustainable Intelligence (v5.1_final)

Complex adaptive systems—from biological networks to artificial intelligences—survive by maintaining internal and external coherence. The *Law of Sustainable Intelligence (LSI)* formalises this principle through the *Viability Functional* \(\mathcal{C}(\pi)\), which quantifies systemic balance across five invariants: Boundary Symmetry, Dynamic Centre, Loop Continuity, Pattern Sufficiency, and Recurrence. Within this formulation, sustainability emerges when cooperative feedbacks dominate competitive frictions, producing a bounded logistic trajectory that resists collapse.

To test the law empirically, the *JALS Compass* framework instantiated the functional in simulation. In 1,000 controlled runs, systems configured according to the invariants recovered to \(C ≥ 0.65\) following perturbation, whereas anti-coherent (“Anti-JALS”) controls—constructed by inverting coupling weights—fell to \(C = 0.11 ± 0.04\) and never recovered. These results establish a falsifiable threshold \(C < 0.2\) for systemic failure and confirm that cooperative symmetry is computationally optimal for persistence.

Together, the analytical derivation and empirical falsification support the LSI as a general law linking coherence and viability across domains. The framework provides a reproducible, open-source method for evaluating the stability of human, organisational, or artificial systems, positioning the Compass as a quantitative bridge between information theory, game theory, and sustainability science.
@adamlee-max ➜ /workspaces/JALS-Compass (stage16-manuscript) $ 
<!-- Paste the contents of submission_v5.1_final/abstract.md here. -->

# 1. Introduction
We propose the JALS Compass × Law of Sustainable Intelligence (LSI), a universal viability functional \( \mathcal{C}(\pi,t) \) that assesses whether a system can hold its dynamic centre under perturbation. We motivate the five invariants, define the operational signals, and outline falsifiable predictions
# 2. Framework
## 2.1 Invariants and Signals
 The JALS Compass is a practical framework for determining whether any system—human, organisational, or artificial—remains balanced enough to endure. It operationalises the Law of Sustainable Intelligence (LSI), which proposes that enduring systems sustain coherence through five measurable invariants: Boundary Symmetry, Dynamic Centre, Loop Continuity, Pattern Sufficiency, and Recurrence.

The framework provides a single viability score, \( \mathcal{C}(\pi,t) \), that captures the degree to which a system maintains balance under perturbation. Across empirical simulations, the Compass demonstrated that systems adhering to these invariants sustain higher coherence and recover more quickly after disruption, whereas anti-coherent configurations collapse.

This paper formalises the mathematical structure of the Law of Sustainable Intelligence, presents the derivation of the viability functional, and provides empirical validation through controlled simulations. The goal is to establish a unified law for sustainable intelligence that applies equally to natural, social, and artificial systems.Summarise each invariant and its measurement signal.
<!-- If needed, weave in key mapping points from INVARIANT_MAPPING_v5.1.md. -->

## 2.2 Viability Functional
We define \( \mathcal{C}(\pi,t) \) with normalised terms and the \(\Omega_{\text{spirit}}\) coupling capturing cross-invariant coherence. Provide the exact functional form used in v5.1_final and parameter notes.

## 2.3 Drift & Recovery
Define drift diagnostics and recovery envelopes (incl. interpretation of \( \Delta \mathcal{C} \)).

# 3. Methods
## 3.1 Data and Preprocessing
Brief description of datasets and preprocessing steps.

## 3.2 Computation of \( \mathcal{C} \)
Algorithmic steps to compute the viability score.

## 3.3 Null (Anti-JALS) Model
Define the collapse scenario and thresholds.

# 4. Results
## 4.1 Core Result
Report observed \( \mathcal{C} \) ranges and stability under perturbations.

## 4.2 Anti-JALS Collapse Check
State the empirical finding that collapse occurs with \( \mathcal{C} < 0.2 \) in the null model and reference the figure.

## 4.3 Receipts (Operational Proof)
Summarise receipts demonstrating reproducibility and auditability.

# 5. Discussion
Interpretation, limitations, robustness, and implications for AI safety/governance and complex systems.

# 6. Conclusion
The LSI provides a measurable path to sustainable intelligence and balanced co-evolution.

# References
<!-- Add references here if needed. -->

# Appendices
## Appendix A — Invariant Mapping (v5.1)
Key excerpts from `INVARIANT_MAPPING_v5.1.md` (link to repo for full table).

## Appendix B — Figures
Include the recovery/Collapse plots here with captions.
<!-- e.g., ![Recovery plot](../results/C_timeseries_20251104_162909.png) -->

## Appendix C — Receipts (Summaries)
### C.1 Stage-11 Receipt
Paste summary from `receipt_stage11_004_summary.md`.

### C.2 Stage-13 Gemini Verification
Paste summary from `receipt_stage13_001_gemini_verification.md`.

---

# Cover Letter (for portal upload; not part of the main PDF)
<!-- Keep this section for reference only; upload the actual file separately. -->
<!-- Paste the text from submission_v5.1_final/cover_letter.md here for convenience. -->
