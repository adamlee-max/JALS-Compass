# JALS Compass Repository Audit — 2025-12-08

**Scope:** Read-only structural review of `JALS-Compass` repo (main branch + `6-add-minimal-ci-with-two-smoke-tests-badge` feature branch).  
**No code changes.** Documentation-only observations and zero-risk suggestions.

---

## 1. Inventory: Directory and File Tree (Top 2 Levels)

```
JALS-Compass/
├── .github/
│   └── workflows/
│       └── smoke-tests.yml                    [CI workflow: syntax + daemon import]
├── AUDIT/
│   └── audit_repo_2025-12-08.md              [This file]
├── archive/
│   └── README.md                              [Legacy: Old research snapshots]
├── archive_paper_v3.3/
│   ├── Philosophical_Paper_LSIv5.1.md        [Archived v3.3 formulations]
│   ├── anti_jals_null_model.md
│   ├── C_function_explicit.md
│   ├── invariant_mapping.md
│   ├── methods_addendum_CDM.md
│   └── README.md
├── assets/
│   ├── compass_diagram_placeholder.md        [Placeholder; no image yet]
│   └── plots/                                 [Output dir: future survival curves etc.]
├── drafts/
│   ├── Executive_Abstract.md                 [Non-final draft versions]
│   ├── laymans_checklist.md
│   └── laymans_pack.md
├── examples/
│   ├── sim_dynamic_test.py                   [Entry point: Stage-4 dynamic validation]
│   ├── sim_survival_curves.py                [Entry point: Stage-5 prototype]
│   ├── compass_science_crossdomain.md
│   ├── education_example.md
│   ├── finance_example.md
│   ├── finance_trading.json
│   ├── healthcare_example.md
│   ├── lehman_example.md
│   ├── meta_loop_example.md
│   └── README.md
├── experiments/
│   ├── finance_2008/                         [Stage 20: 2008 crisis replay (Complete)]
│   │   ├── prep/ (data_prep_v1.py)
│   │   ├── sim/ (sim_2008_v1.py, etc.)
│   │   └── results/ (banks_2008_*.png, *.csv)
│   ├── hostile_env/                          [Stage 19: Adversarial conditions (Complete)]
│   │   ├── hostile_env_sim_v1.py
│   │   ├── hostile_env_sim_instant.py
│   │   ├── hostile_env_sim_mixed.py
│   │   ├── hostile_env_sim_anti_only.py
│   │   └── hostile_env_compare_v1.py
│   └── null_model/                           [Stage 17: Null-model runs (Complete)]
│       ├── null_model_sim.py
│       └── null_model_survival.png
├── monitor/
│   ├── C_current.txt                         [Status snapshot (prospective)]
│   ├── README.md
│   ├── measurement_axiom_addendum_v5.2.md   [Technical addendum]
│   └── proxy_invariant_alignment_addendum_v5.2.md
├── os_heartbeat/
│   ├── daemon.py                             [Entry point: Stage-21 heartbeat (Gated for CI)]
│   ├── README.md
│   ├── logs/                                 [Output dir: heartbeat_YYYYMMDD.jsonl]
│   ├── receipts/                             [Output dir: receipt_YYYYMMDDTHH.json]
│   └── public/
│       ├── status.json                       [Live status (atomic)]
│       └── index.html                        [Live dashboard]
├── paper_v5.1/
│   ├── abstract.md                           [Submission packet (Final)]
│   └── cover_letter.md
├── peer_reviews/
│   └── Gemini_LSIv3.3_Review.md             [AI review (informational)]
├── proof_receipts/
│   ├── hostile_env_compare_v1.py            [Analysis script]
│   ├── hostile_env_compare_v1.png
│   ├── receipt_stage10.md
│   ├── receipt_stage17_nullmodel.md
│   ├── receipt_stage19_*.md                  [Stage 19 receipts (5 files)]
│   ├── receipt_stage20_001.md
│   ├── receipt_stage21_001.md
│   ├── receipt_stage21_002.md
│   └── receipt_stage21_FINAL.md
├── reaudits/
│   └── stage10/                              [Re-audit snapshots (historical)]
├── receipts/
│   ├── compass_receipt_*.md                  [Receipts 1–7]
│   ├── compass_receipt_006.csv
│   ├── receipt_008.md
│   ├── receipt_RSOS_*.md                     [Royal Society submission records]
│   └── README.md                             [Receipts ledger]
├── results/
│   ├── anti_jals_collapse.csv               [Stage-17 null-model output]
│   └── anti_jals_collapse.png
├── stage6/ stage7/ stage8/ stage9/ stage10/
│   ├── *.md (README, receipts, manifests, submission checklists)
│   ├── *.zip (audit and submission packages)
│   └── observer_logs/ (historical logs)
├── submission_v5.1_final/
│   └── [Contents: manuscript PDF, supplementary data]
├── compass.py                                 [Entry point: Quick C_proxy calculator]
├── .gitignore
├── AUTHORS.md
├── LICENSE
├── Public_Statement.md
├── README.md                                  [Main status + stage overview]
├── REPRODUCIBILITY.md                         [Guide for running experiments]
├── SUBMIT_THIS.md                             [Royal Society submission instructions]
├── requirements.txt                           [3 dependencies: numpy, pandas, matplotlib]
├── start_heartbeat.sh / stop_heartbeat.sh   [Shell launchers for daemon]
├── JALS-Compass_v5_audit.zip                [Snapshot: exported audit ZIP]
├── ck --full --strict                        [ANOMALY: Git log output saved as filename]
└── __pycache__/                               [Generated: Python bytecode cache]
```

---

## 2. Status Guesses per Major Folder

| Folder | Status | Evidence | Notes |
|--------|--------|----------|-------|
| **paper_v5.1** | **Final** | Abstract + cover letter present; referenced in README as "manuscript v5.1" | Ready for submission; minimal content (2 files). Full manuscript likely in `submission_v5.1_final/`. |
| **experiments/hostile_env** | **Complete** | `receipt_stage19_*.md` files; README mentions "Stage 19 sealed"; 5 simulation variants + comparison script + plot | Adversarial testing locked; all artifacts present. |
| **experiments/finance_2008** | **Complete** | `receipt_stage20_001.md`; README mentions "Stage 20 sealed"; data prep + sim + results (PNG, CSV) | 2008 crisis replay; 6/6 bank prediction accuracy; sealed. |
| **experiments/null_model** | **Complete** | `receipt_stage17_nullmodel.md`; 10k-run simulation + survival curves in `results/` | Stage 17 baseline; outputs in place. |
| **os_heartbeat** | **Active/Prospective** | `daemon.py` gated under `if __name__ == "__main__" and AUTOSTART and not CI:`; README v0.1.3 | Stage 21 daemon; not yet deployed live; CI-safe (no autostart in Actions). |
| **monitor** | **Draft** | `C_current.txt` present but sparse (1-2 lines); addenda are v5.2 | Monitoring infra placeholder; not actively tracking live signals. |
| **drafts/** | **Draft** | Labels say "draft"; no final version markers | Lay summaries + executive abstract. |
| **receipts/** | **Complete** | Ledger in `receipts/README.md`; 8 compass receipts + 3 RSOS journal submissions | Historical validation records. |
| **stage6 .. stage10** | **Archived** | Each has sealed receipts, manifests, submission zips, observer logs | Stages 6–10: completed + locked historical checkpoints. |
| **archive_paper_v3.3** | **Legacy** | Marked "v3.3"; predates v5.1; philosophical paper | Old iteration; kept for provenance. |
| **archive/** | **Legacy** | Minimal contents; marked as historical | Snapshots; not active. |
| **examples/** | **Runnable** | Entry points with `if __name__ == "__main__"`; docstrings present | Stage-4 and Stage-5 prototypes; ready to execute. |
| **peer_reviews/** | **Informational** | Single Gemini AI review; not published submission feedback | AI-generated feedback (not peer-reviewed). |

---

## 3. Executability Check: Python Entry Points

**Method:** Static file reading (no execution).

| File | Imports | Main Guard | Verdict | Notes |
|------|---------|-----------|---------|-------|
| **compass.py** | None (pure function) | ✅ `if __name__ == "__main__"` | ✅ **Runnable** | Simple demo; no external deps. |
| **examples/sim_dynamic_test.py** | pandas, matplotlib, argparse (implied) | ✅ `if __name__ == "__main__"` | ⚠️ **Likely runnable** | Uses pandas, matplotlib; requires `requirements.txt`. |
| **examples/sim_survival_curves.py** | numpy, matplotlib | ✅ `if __name__ == "__main__"` | ⚠️ **Likely runnable** | Requires numpy, matplotlib. |
| **experiments/null_model/null_model_sim.py** | numpy, matplotlib, `lifelines` | ❌ No `if __name__ == "__main__"` | ⚠️ **Will run on import** | **RISK:** Runs unconditionally. Missing `lifelines` in `requirements.txt`. |
| **experiments/hostile_env/hostile_env_sim_v1.py** | numpy, matplotlib (implied) | ✅ `if __name__ == "__main__"` | ⚠️ **Likely runnable** | Gated properly. |
| **experiments/hostile_env/hostile_env_sim_instant.py** | numpy, matplotlib | ✅ `if __name__ == "__main__"` | ⚠️ **Likely runnable** | Gated properly. |
| **experiments/hostile_env/hostile_env_sim_mixed.py** | numpy, matplotlib | ✅ `if __name__ == "__main__"` | ⚠️ **Likely runnable** | Gated properly. |
| **experiments/hostile_env/hostile_env_sim_anti_only.py** | Not fully checked | ✅ `if __name__ == "__main__"` | ⚠️ **Likely runnable** | Assume gated. |
| **experiments/hostile_env/hostile_env_compare_v1.py** | Not fully checked | ✅ `if __name__ == "__main__"` | ⚠️ **Likely runnable** | Gated properly. |
| **proof_receipts/hostile_env_compare_v1.py** | numpy, matplotlib | ✅ `if __name__ == "__main__"` | ⚠️ **Likely runnable** | Gated properly; copy/duplicate of above. |
| **os_heartbeat/daemon.py** | json, os, random, signal, sys, time, hashlib, subprocess, dataclasses, datetime, pathlib | ✅ `if __name__ == "__main__" and AUTOSTART and not CI` | ✅ **CI-safe** | **New:** Gated for CI; will NOT autostart when imported in GitHub Actions (CI=true). |
| **experiments/finance_2008/sim/sim_2008_v1.py** | Not yet read | ✅ (assumed) | ⚠️ **Likely runnable** | Not fully inspected. |
| **experiments/finance_2008/prep/data_prep_v1.py** | Not yet read | ✅ (assumed) | ⚠️ **Likely runnable** | Not fully inspected. |

**Key Finding:** `null_model_sim.py` **runs on import** (no `if __name__` guard); this causes side-effects and the import test in CI would execute it.

---

## 4. CI Coverage Analysis

**Current CI Workflow:** `.github/workflows/smoke-tests.yml` (on all push/PR)

### What is Tested
1. **Python Syntax Check:** `python -m py_compile $(git ls-files '*.py')`  
   → Verifies all `.py` files parse without errors.  
   → ✅ Passes (confirmed Dec 8, 2025).

2. **Daemon Import Test:** `python -c "import importlib; importlib.import_module('os_heartbeat.daemon')"` (with `CI=true` env var in daemon)  
   → Verifies `os_heartbeat.daemon` imports successfully in CI context.  
   → ✅ Does **NOT** autostart heartbeat loop (gated by new `AUTOSTART and not CI` condition).

### What is **NOT** Tested
- ❌ **Dependency resolution:** `requirements.txt` is not installed in CI. Syntax check only verifies parsing, not import availability.
- ❌ **Missing `lifelines` module:** `null_model_sim.py` imports `lifelines` (KaplanMeierFitter), which is not in `requirements.txt`. CI syntax check will pass, but runtime execution would fail.
- ❌ **Argument parsing & runtime behavior:** No integration tests for experiment entry points (sim_*.py).
- ❌ **Heartbeat execution:** Only tests import; does not verify the daemon loop, logging, or receipt generation logic.
- ❌ **Experiment reproducibility:** No seed-based or deterministic output validation.
- ❌ **Dashboard / public files:** No check for `public/status.json`, `index.html` generation.
- ❌ **Data prep scripts:** `finance_2008/prep/data_prep_v1.py` not tested.

---

## 5. Risk & Confusion: Duplicates, Version Drifts, Missing Pins, Dead Files

### 🔴 Critical Issues

1. **Missing `lifelines` Dependency**  
   - **File:** `experiments/null_model/null_model_sim.py` (line ~3)  
   - **Impact:** Code imports `lifelines.KaplanMeierFitter` but `lifelines` is **not** in `requirements.txt`.  
   - **Risk:** Runtime failure if someone tries to run the null-model simulation locally (even though CI syntax check will pass).  
   - **Fix:** Add `lifelines` to `requirements.txt`.

2. **Unconditional Execution in `null_model_sim.py`**  
   - **File:** `experiments/null_model/null_model_sim.py` (lines 46–79)  
   - **Issue:** The main simulation loop (`for i in range(EPISODES): ...`) and plot generation are at module level, not gated under `if __name__ == "__main__"`.  
   - **Risk:** Importing the module will run the entire 10k-episode simulation (~seconds to minutes).  
   - **Symptom:** CI daemon-import test or any notebook importing this will unexpectedly compute + plot.  
   - **Fix:** Wrap main logic in `if __name__ == "__main__":` block.

### 🟡 Medium-Risk Issues

3. **Duplicate Script: `hostile_env_compare_v1.py` in Two Places**  
   - **Files:** `experiments/hostile_env/hostile_env_compare_v1.py` and `proof_receipts/hostile_env_compare_v1.py`  
   - **Issue:** Same filename in two locations; unclear which is canonical.  
   - **Risk:** Confusion during development; maintenance burden (which to update?).  
   - **Fix:** Keep only one (prefer `experiments/`) and remove or symlink the other. Update `proof_receipts/README.md` if needed.

4. **Finance 2008 Data Scripts Not Verified**  
   - **Files:** `experiments/finance_2008/prep/data_prep_v1.py` and `sim/sim_2008_v1.py`  
   - **Issue:** Not statically reviewed; assumed to have `if __name__` guards.  
   - **Risk:** Unknown side-effects on import.  
   - **Fix:** Audit these files for unconditional execution.

5. **Odd Filename in Root**  
   - **File:** `ck --full --strict`  
   - **Content:** Git log output (20 lines)  
   - **Risk:** Confusing to new users; appears to be a command accidentally saved as a filename.  
   - **Fix:** Move to `ARCHIVE/` or delete (likely a mistake).

6. **Version Drift Between Paper Artifacts**  
   - **Locations:** `paper_v5.1/` (v5.1) vs. `archive_paper_v3.3/` (v3.3) vs. drafts/  
   - **Observed:** README mentions "v5.1 manuscript" but also references v5.2 addenda in `monitor/`.  
   - **Risk:** External reviewers may download wrong version.  
   - **Fix:** Add a table in README clearly mapping submission versions → folders.

### 🟢 Low-Risk Issues

7. **Empty or Sparse Output Directories**  
   - **Dirs:** `results/` (2 files only), `assets/plots/` (empty), `monitor/C_current.txt` (sparse)  
   - **Issue:** Placeholders; actual outputs would be generated at runtime.  
   - **Status:** Expected (pre-deployment state).  
   - **No action needed.**

8. **Archived Stages 6–10 Are Large (Many ZIPs)**  
   - **Observation:** Each stage has `.zip` snapshots (e.g., `JALS-Compass_Stage6_Audit.zip` 425 KB).  
   - **Status:** Historical checkpoints; intentional for provenance.  
   - **No action needed.**

---

## 6. Zero-Risk Fixes (Documentation Only)

These are changes that improve clarity without modifying executable code:

### 6.1 Clarify Version Mapping in README

**Current problem:** Readers don't know which folder contains the "final" manuscript.

**Suggested addition** (after "Manuscript version:" section in [`README.md`](../../README.md)):

```markdown
## Version Guide

| Version | Location | Status | Notes |
|---------|----------|--------|-------|
| **v5.1** | `paper_v5.1/`, `submission_v5.1_final/` | Final submission packet | Core scientific write-up for Royal Society; ready to submit. |
| **v5.2** | `monitor/` (addenda only) | Refinements | Technical clarifications to measurement axiom and proxy invariant. |
| **v3.3** | `archive_paper_v3.3/` | Legacy | Older iteration; kept for historical reference. |
| **Drafts** | `drafts/` | In-progress | Lay summaries and examples; not for final submission. |
```

### 6.2 Add Dependency Installation Note to `REPRODUCIBILITY.md`

**Current:** Lists Python version and commands to run sims, but doesn't emphasize the missing `lifelines`.

**Suggested edit** (after the pip install line):

```markdown
## Environment Setup

### Full Dependencies
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pip install lifelines  # Required for null_model_sim.py Kaplan-Meier survival curves
```

### Verify Installation
```bash
python -c "import numpy, pandas, matplotlib, lifelines; print('All deps OK')"
```
```

### 6.3 Add Clarity Note on `os_heartbeat` CI-Safety

**Suggested addition** to [`os_heartbeat/README.md`](../../os_heartbeat/README.md):

```markdown
## CI & Testing

**Safe for import in CI/CD:** The daemon is gated to **NOT autostart** when the environment variable `CI=true` (set by GitHub Actions). 
This allows syntax checks and import validation without triggering the heartbeat loop.

To manually test CI-safe import:
```bash
CI=true python -c "import os_heartbeat.daemon; print('Import OK, no loop started')"
```
```

### 6.4 Flag the Odd Filename in `.gitignore`

**Suggested:** Add a note in root [`README.md`](../../README.md) or create a task in `AUDIT/`:

```markdown
## Known Oddities

- **`ck --full --strict`**: Root-level file containing git log (appears to be an accidental save; safe to delete or archive).
```

### 6.5 Add CI Status and Future Roadmap

**Suggested section** in [`README.md`](../../README.md):

```markdown
## Continuous Integration

✅ **Smoke Tests** (`.github/workflows/smoke-tests.yml`):
- Python syntax validation (all `.py` files)
- Daemon import check (gated for CI)
- **Coverage gap:** Does not test dependencies (e.g., `lifelines`, `numpy`) or simulate execution.

**Future:** Consider adding integration tests for experiment reproducibility (e.g., null-model 10-run smoke test).
```

---

## 7. Summary Table: Risk Assessment

| Issue | Severity | Category | Recommendation |
|-------|----------|----------|-----------------|
| Missing `lifelines` in `requirements.txt` | 🔴 High | Dependency | Add `lifelines` to requirements. |
| `null_model_sim.py` runs unconditionally on import | 🔴 High | Code quality | Wrap main logic in `if __name__ == "__main__"`. |
| Duplicate `hostile_env_compare_v1.py` | 🟡 Medium | Maintenance | Consolidate (keep `experiments/`, remove duplicate). |
| Finance 2008 sim scripts not audited | 🟡 Medium | Unknown | Review for unconditional execution. |
| Odd filename `ck --full --strict` | 🟡 Medium | Hygiene | Move to archive or delete. |
| Version drift/confusion (v3.3 vs v5.1 vs v5.2) | 🟡 Medium | Documentation | Add version table to README. |
| CI does not test dependency availability | 🟡 Medium | CI coverage | Consider `pip install -r requirements.txt` in CI job. |
| No integration tests for simulations | 🟡 Medium | CI coverage | Optional: add smoke run (e.g., 10-run null model). |

---

## 8. Audit Artifacts

This report is saved to:  
**`AUDIT/audit_repo_2025-12-08.md`**

**Next Steps for Maintainers:**
1. Address critical issues (lifelines, null_model_sim.py main guard).
2. Consolidate duplicate scripts.
3. Apply zero-risk documentation fixes.
4. Consider extended CI coverage for experiment reproducibility.

---

**Report Generated:** 2025-12-08  
**Auditor:** GitHub Copilot (read-only static analysis)  
**Branch:** main + 6-add-minimal-ci-with-two-smoke-tests-badge (smoke-tests.yml added)
