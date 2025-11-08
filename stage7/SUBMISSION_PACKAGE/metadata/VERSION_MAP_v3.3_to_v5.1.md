# Version Map — Repository v5.1_clean → Submission v5.1

## Purpose
Traceability map aligning code/repo terminology (v5.1_clean lineage) with submission manuscript (v5.1), ensuring reviewers can reconcile notation, figures, and claims.

## Summary Table
| Repo/Track | Submission (v5.1) | Notes |
|---|---|---|
| C(π) functional (v5.1_clean) | Core viability functional (Sec. II) | Identical form; symbol hygiene unified. |
| Invariants I_i | Invariants I₁..I₅ (Boundaries, Centre, Loops, Patterns, History) | Normalised to [0,1]; dimensional consistency checked. |
| Dynamic weights w_i(t,π) | Time/context weights w_i | Explained with examples + bounds. |
| Cross-coupling κ_ij | Inter-invariant coupling κ_ij | Clarified symmetry/asymmetry cases. |
| Ω_spirit term | System-level coherence term Ω | Defined; empirical proxy policy described. |
| Null model (“anti-JALS”) | Falsifiability protocol (Appx. B) | Collapse demonstration: C < 0.2. |
| C(t) drift plots | Stability/Recovery figures | Lyapunov-style drift narrative. |
| Receipts folder | Transparency artifacts | Checklist, chain-of-custody, checksum. |

## Figure Mapping
- Fig. 1 — Framework Overview → repo: /docs/figures_overview (source)
- Fig. 2 — C(t) Drift under Stress → repo: /monitor/plots/C_timeseries_*.png
- Fig. 3 — Anti-JALS Collapse (C < 0.2) → repo: /sim/null_model/results.png

## Claims ↔ Evidence
- Dimensional consistency → Mapping worksheet + Section II proofs.
- Falsifiability → Anti-JALS dataset + Appendix B.
- Reproducibility → Git commit hash embedded in receipts.

*Prepared for reviewers and editors; update paths if figure filenames change.*
