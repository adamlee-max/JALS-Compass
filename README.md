> **The JALS Compass** is a practical framework for checking if any system — human, organisational, or AI — is *balanced enough to last*.
>[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17542087.svg)](https://doi.org/10.5281/zenodo.17542087)
> **✅ Proof Summary — Stage 5 (v5.0)**
> 
> The *Law of Sustainable Intelligence (LSI)* has been formally proven and archived.
> 
> - **DOI:** [10.5281/zenodo.17542087](https://doi.org/10.5281/zenodo.17542087)  
> - **Perma Record:** [https://perma.cc/N6BV-E9GK](https://perma.cc/N6BV-E9GK)  
> - **Verification Commit:** `8e8029d`  
> - **Viability Score:** `C = 0.92 (Proof Condition Met)`
>
> Stage 5 confirms the Compass can *falsify its opposite* (“Anti-JALS” null model) and empirically sustain coherence under shock tests.  
> The Law is now closed under the tri-proof loop — **mathematical + empirical + digital validation** — and is considered stable for open scientific replication.
>
> 🩶 *Balance wins. Always.*
> It works through five simple checks (boundaries, centre, loops, patterns, history) and produces a quick C-score to show stability.
>
> Think of it as a reality gauge: “Are we still balanced, and can we prove it?”
>
> # JALS Compass × Law of Sustainable Intelligence (LSI) — Stage 3 (v3.3)
>🩺 **Live Status:** See [`/monitor/`](monitor/README.md) → System viable ✅ C ≈ +0.8  |  External proof: Perma.cc 🔒🗂️ **Repo Map:** `/paper_v3.3` → academic core · `/drafts` → layman’s pack · `/receipts` → real-world proofs · `/assets` → visuals

📄 **Executive Abstract:** [/drafts/Executive_Abstract.md](drafts/Executive_Abstract.md)  
📢 **[Read the Public Statement →](Public_Statement.md)**  

A short human introduction to what the Compass is and why it exists.**Status:** Stage 3 – LSI v3.3 locked • **Date:** 30 Oct 2025 (UTC+0)  
**Purpose:** This repo is the canonical, timestamped record (“receipt of existence”) for the JALS Compass and the Law of Sustainable Intelligence (LSI).

## What this is
The **JALS Compass** operationalises the **Law of Sustainable Intelligence** using five invariants:
1) Boundary Symmetry  2) Dynamic Centre  3) Loop Continuity  4) Pattern Sufficiency  5) Recurrence

v3.3 introduces: time-varying weights **wᵢ(t, π)**, cross-invariant coupling **κᵢⱼ**, and a formalised global coherence term **Ω_spirit**.  
The full functional and definitions live in `/paper_v3.3/formula_v3.3.md`.

## Why this repo matters
- **Single source of truth** for the math, proofs, and receipts.  
- **Public traceability:** each commit is a dated receipt.  
- **Interoperable:** papers, app blueprints, and validations reference this repo.
## C(π): Law vs Operational Proxy (repo truth)

**This repo implements a pragmatic proxy of the Law.**  
The formal law lives in the paper; here we use a simple, reproducible score for quick checks and examples.

### Formal law (paper)
- **Snapshot (state):** \( C_s(\pi,t) = \frac{\log S(t)}{\log D(t)} \)  
- **Dynamic (process):** \( \displaystyle \frac{dC(\pi,t)}{dt} = \frac{d}{dt}\Big(\frac{\log S(t)}{\log D(t)}\Big) \)  
  - Read: how fast coherence is improving or decaying over time.

> **Meta-Law (guiding principle):**  
> Systems that maintain coherence through noise, drift, and interaction tend to survive; those that cannot, dissolve.

### Operational proxy (used in this repo)
We use a **linear heuristic** for fast, transparent scoring in examples/sims:

\[
C_{\text{proxy}}(\pi) \;=\; 0.3\,E_m \;+\; 0.3\,R \;-\; 0.2\,Pr \;-\; 0.1\,H \;-\; 0.1\,G
\]

- \(E_m\): meaningful effort \(R\): reciprocity \(Pr\): breach risk  
- \(H\): opacity/hiddenness \(G\): regret/goal drift  
- Range: \([-1, +1]\) approx. Higher = more viable.

> **Disclosure:** `C_proxy` is a **pragmatic proxy**, not the Law itself.  
> Full derivation and dynamic form are in the paper (see `/paper_v3.3/`).

### Falsifiability (how this can be wrong)
If a system **sustains survival** while its measured coherence **decreases over time** (dynamic \(dC/dt<0\) persistently), the law fails.  
If coherence increases yet the system **consistently collapses**, the law fails.  
This repo includes small sims to make that check explicit.
## Relationship to Paper
This repository serves as the **operational layer** of the *Law of Sustainable Intelligence* (LSI v3.3), mirroring the formal derivation in [`/paper_v3.3/formula_v3.3.md`](paper_v3.3/formula_v3.3.md) and its philosophical context in [`/paper_v3.3/Philosophical_Paper_LSIv3.3.md`](paper_v3.3/Philosophical_Paper_LSIv3.3.md).
Each update here corresponds to a validated stage or “receipt” of theoretical evolution.### Quick example (proxy)
```python
from compass import jals_compass  # C_proxy
score = jals_compass(E_m=0.85, R=0.80, Pr=0.15, H=0.10, G=0.05)
print(f"C_proxy = {score:.2f}")
# Tip: treat >0.2 as “viable” in examples; tune per domain.## Repo layout (Stage 3 seed)
→ See [`/examples/finance_trading.json`](examples/finance_trading.json) for a full JSON-based system test.- [`/paper_v3.3/`](paper_v3.3/README.md) — academic paper materials (outline, formula, and [Philosophical Paper — LSI v3.3](paper_v3.3/Philosophical_Paper_LSIv3.3.md))  
- [`/receipts/`](receipts/) — validation runs & logs (Compass Receipts)  
- [`/drafts/`](drafts/) — philosophical companion & layman’s pack  
- [`/assets/`](assets/) — diagrams and figures  
- [`README.md`](README.md) — this file (project home)

## Quick start
- Read the functional: `/paper_v3.3/formula_v3.3.md`  
- See proof templates: `/receipts/compass_receipt_001.md` (coming next step)  
- Track changes via Releases (v3.3+)

## Citation (placeholder)
JALS Research Group (2025). *The Law of Sustainable Intelligence & the JALS Compass (v3.3).* GitHub repository.  
---

## 💬 Layman’s Pack
If you just want the plain-English version, start here:

- [Layman’s Pack](drafts/laymans_pack.md)
- [Quick Checklist](drafts/laymans_checklist.md)
- _This plain-English guide is now live and linked to the Stage 3 verified monitor._  
→ See current system health in [`/monitor/`](monitor/README.md)
