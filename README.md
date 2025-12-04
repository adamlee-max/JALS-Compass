[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17542087.svg)](https://doi.org/10.5281/zenodo.17542087)
JALS Compass × Law of Sustainable Intelligence (LSI)

Working hypothesis: systems that maintain coherent balance across their boundaries, centre, feedback loops, patterns, and history tend to survive; those that cannot, dissolve.

This repository hosts the JALS Compass, an operational framework for assessing whether a system — human, organisational, or artificial — is balanced enough to last, together with a candidate Law of Sustainable Intelligence (LSI) that motivates it.

The repo is under active investigation. The goal is not to declare a final law, but to make the current formulation and evidence transparent, testable, and falsifiable.

⸻

Current Status

Stage 17 – Null-model receipt:
	•	10,000-run simulation comparing a JALS-aligned system vs an Anti-JALS null model
	•	Code: /experiments/null_model/null_model_sim.py
	•	Outputs: survival curves + CSV artifacts in /results/ and /proof_receipts/
	•	In the experiments run so far, the Anti-JALS baseline consistently collapses faster than the JALS-aligned system.

Stage 18 – Repo & manuscript clean-up (in progress):
	•	Align README and repo map with the v5.1 manuscript
	•	Clarify measurement and proxy alignment
	•	Tighten reproducibility paths for external reviewers

Stage 19 — Hostile environment suite (completed):

• Stress-tested the Compass under adversarial conditions (attack, noise, opacity, imbalance rewards).
• Four v1 simulations:
    - baseline hostile: /experiments/hostile_env/hostile_env_sim_v1.py
    - instant-knowledge cohort: /experiments/hostile_env/hostile_env_sim_instant.py
    - mixed-behaviour cohort: /experiments/hostile_env/hostile_env_sim_mixed.py
    - anti-only placeholder: /experiments/hostile_env/hostile_env_sim_anti_only.py
• Outputs: comparison plot in /proof_receipts/hostile_env_compare_v1.png
• Result: Instant cohort survives ~5–15 steps longer than Mixed.
• Conclusion: Higher effective coherence (C_proxy) predicts survival even when the environment rewards imbalance.
• Status: Stage 19 sealed — tag: v5.1_stage19_receipt

Stage 20 — 2008 financial crisis replay (completed):

• Applied the Compass to the 2006–2009 U.S. financial crisis.
• Used quarterly bank-level signals (Em, R, Pr, H, G) with the Stage-19-locked C_proxy EMA (span=4, hysteresis=0.12).
• Banks tested:
    - Lehman Brothers (collapsed)
    - Bear Stearns (collapsed)
    - JPMorgan Chase (survived)
    - Bank of America (survived)
    - Wells Fargo (survived)
    - Goldman Sachs (survived)
• Result: **6/6 perfect separation** — failed banks end below the collapse threshold (–0.25), survivors remain positive.
• Artifacts:
    - Trajectories: /experiments/finance_2008/results/banks_2008_cproxy_trajectories.png
    - Summary CSV: /experiments/finance_2008/results/banks_2008_summary.csv
    - Receipt: /proof_receipts/receipt_stage20_001.md
• Status: Stage 20 sealed — tag: v5.3_stage20_receipt

Manuscript version:
	•	Core scientific write-up: /paper_v5.1/
	•	Submission packet: /submission_v5.1_final/

⸻

Canonical Records & External Proofs

These resources are intended as receipts, not as claims of finality.

Zenodo archive (Stage 5 proof packet):
DOI: 10.5281/zenodo.17542087

Perma.cc record (external timestamp):
https://perma.cc/N6BV-E9GK

Historical snapshots & audits:
	•	Stage 3 archive (v3.3): /archive_paper_v3.3/
	•	Historical proof summary: HISTORICAL_PROOF_SUMMARY.md
	•	Stage reports and receipts: /proof_receipts/

The intention is that any future critic or collaborator can trace what was claimed, when, and on the basis of which evidence.

⸻

What the JALS Compass Tries to Measure

Five invariants:
	1.	Boundary Symmetry (B)
	2.	Dynamic Centre (D)
	3.	Loop Continuity (L)
	4.	Pattern Sufficiency (P)
	5.	Recurrence (R)

The Law of Sustainable Intelligence (LSI) is a proposed relationship between a system’s coherence and its long-run viability.
The Compass is a pragmatic operationalisation of that idea.

⸻

Law vs Operational Proxy

The repo distinguishes between the theoretical law (in the paper) and the simple operational proxy (used in examples and sims).

Theoretical form (paper)

Formal definitions live in:
	•	/paper_v5.1/formula_v5.1.md
	•	/paper_v5.1/Philosophical_Paper_LSIv5.1.md

High-level test:
If coherence decreases while a system survives indefinitely, the law fails.
If coherence increases while the system repeatedly collapses, the law fails.

Operational proxy (repo)

C_proxy(pi) = 0.3 Em + 0.3 R – 0.2 Pr – 0.1 H – 0.1 G

Where:
	•	Em = meaningful effort
	•	R = reciprocity
	•	Pr = breach risk
	•	H = opacity
	•	G = regret / goal drift

Range approx [-1, 1].
Implementation: compass.py.

⸻

Reproducibility – Quick Start

Clone and run:

git clone https://github.com/adamlee-max/JALS-Compass.git
cd JALS-Compass

Run null model (Stage 17):

python experiments/null_model/null_model_sim.py

Outputs will appear in /results/, /assets/, and /proof_receipts/.

⸻

Repo Map (Stage 17+)
	•	paper_v5.1/
	•	submission_v5.1_final/
	•	experiments/null_model/
	•	results/
	•	proof_receipts/
	•	monitor/
	•	peer_reviews/
	•	archive_paper_v3.3/
	•	HISTORICAL_PROOF_SUMMARY.md

⸻

What Is Still Open?

This repo tracks open questions such as:
	•	Domain robustness of the proposed law
	•	Sufficiency of the current invariants
	•	Conditions where Anti-JALS does not collapse
	•	Adversarial counterexamples

Counterexamples and refinements are logged as first-class receipts.

⸻

Contributing / Contact

Contributions include:
	•	replications
	•	counterexamples
	•	alternative measurement schemes
	•	theoretical critiques

Contact information in AUTHORS.md.

⸻

This repo is an attempt to treat intelligence, balance, and survival as measurable and falsifiable.
The real test is what survives sustained scrutiny.
The system now runs in prospective mode.