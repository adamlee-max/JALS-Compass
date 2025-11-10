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
The framework formalises five measurable invariants that together define sustainable intelligence:

1. **Boundary Symmetry** – how well the system maintains balanced exchange with its environment.  
2. **Dynamic Centre** – the system’s internal equilibrium point that adjusts under pressure without collapse.  
3. **Loop Continuity** – the integrity of feedback and learning cycles across time.  
4. **Pattern Sufficiency** – the richness and coherence of structural patterns that sustain function.  
5. **Recurrence** – the ability of a system to recover its state following perturbation.

Each invariant generates a signal \( I_i(t,\pi) \) normalised between 0 and 1. These signals feed into the composite viability functional \( \mathcal{C}(\pi,t) \), producing a continuous measure of systemic balance.
The framework provides a single viability score, \( \mathcal{C}(\pi,t) \), that captures the degree to which a system maintains balance under perturbation. Across empirical simulations, the Compass demonstrated that systems adhering to these invariants sustain higher coherence and recover more quickly after disruption, whereas anti-coherent configurations collapse.

This paper formalises the mathematical structure of the Law of Sustainable Intelligence, presents the derivation of the viability functional, and provides empirical validation through controlled simulations. The goal is to establish a unified law for sustainable intelligence that applies equally to natural, social, and artificial systems.Summarise each invariant and its measurement signal.
<!-- If needed, weave in key mapping points from INVARIANT_MAPPING_v5.1.md. -->

## 2.2 Viability Functional
We define a normalised viability functional \( \mathcal{C}(\pi,t) \in [0,1] \) that aggregates invariant signals with time-varying weights and cross-invariant coherence:

- **Signals:** \( I_i(t,\pi) \in [0,1] \) for \( i \in \{1,\dots,5\} \) correspond to the five invariants.  
- **Weights:** \( w_i(t,\pi) \ge 0 \) with \( \sum_i w_i = 1 \) capture context-sensitive importance.  
- **Coherence:** a global term \( \Omega_{\text{spirit}}(t,\pi) \in [0,1] \) encodes cross-invariant alignment (via coupling \( \kappa_{ij} \)).

Operationally, \( \mathcal{C}(\pi,t) \) rises as invariants strengthen and align, and falls under imbalance or breakdown. Exact parameter settings used for v5.1_final are provided in the repository configuration to ensure reproducibility.
## 2.3 Drift & Recovery
System drift is detected when the viability score \( \mathcal{C}(\pi,t) \) deviates persistently beyond a defined tolerance window. Recovery occurs when corrective feedback restores \( \mathcal{C} \) toward its equilibrium trajectory \( \mathcal{C}_0(t) \). 

For practical monitoring, drift magnitude \( \Delta \mathcal{C} = \mathcal{C} - \mathcal{C}_0 \) and recovery time \( \tau_r \) are logged as diagnostic receipts. Sustained recovery within bounded \( \tau_r \) indicates resilience; unbounded drift signals collapse.
# 3. Methods
## 3.1 Data and Preprocessing
The simulation dataset comprised 1,000 controlled system configurations generated under varying perturbation levels. Each configuration produced time-series outputs for the five invariant signals \( I_i(t,\pi) \), normalised to [0,1]. Pre-processing included smoothing transient noise, ensuring temporal alignment, and rescaling signals to a consistent resolution before computing the viability functional.
## 3.2 Computation of \( \mathcal{C} \)
The viability functional \( \mathcal{C}(\pi,t) \) was computed at each time step as a weighted mean of the invariant signals and a coherence adjustment term:

\[
\mathcal{C}(\pi,t) = \sum_{i=1}^{5} w_i(t,\pi) I_i(t,\pi) \, \Omega_{\text{spirit}}(t,\pi)
\]

Algorithmically:
1. Read invariant signals \( I_i(t,\pi) \) for the current state.
2. Apply weights \( w_i(t,\pi) \) and normalise so \( \sum_i w_i = 1 \).
3. Compute the cross-invariant coherence \( \Omega_{\text{spirit}}(t,\pi) \).
4. Multiply and record the resulting \( \mathcal{C}(\pi,t) \).
5. Log each output as a receipt for reproducibility.
## 3.3 Null (Anti-JALS) Model
The Anti-JALS null model represents a deliberately incoherent configuration in which invariant couplings are inverted to disrupt systemic balance. In this control condition, weights \( w_i(t,\pi) \) are randomised and feedback loops are broken, producing collapse dynamics that serve as a falsification baseline. 

Empirically, systems in the null model exhibit a viability score \( \mathcal{C} < 0.2 \) and fail to recover once feedback symmetry is lost. The collapse plot and associated data are archived in `/results/anti_JALS_collapse.csv` and visualised in `/results/C_timeseries_20251104_162909.png`.
# 4. Results
## 4.1 Core Result
Across all baseline simulations, systems adhering to invariant coupling maintained stable viability scores within the range \( 0.65 \leq \mathcal{C} \leq 0.92 \). Under mild perturbations, \( \mathcal{C} \) temporarily dipped but recovered within bounded \( \tau_r \), confirming the model’s resilience. 

These results validate that cooperative feedback and boundary symmetry preserve systemic balance, establishing \( \mathcal{C} \) as a measurable indicator of sustainable intelligence.
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
