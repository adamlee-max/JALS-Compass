# Stage 8 — External Re-Audit Manifest (Gemini × Grok)

**Objective:** Independent replay of empirical results + confirmation of falsification and metadata integrity.

**Package:** Gemini_AuditPayload_v5.1_ready.zip  
**Trigger Receipt:** receipts/receipt_011_stage8_trigger.md  
**Timestamp:** 2025-11-09 13:45 UTC

## Checks to run
- [ ] Empirical replay — Anti-JALS collapse (C < 0.2) under identical stress  
      Data: stage7/SUBMISSION_PACKAGE/receipts/ANTI_JALS_FALSIFICATION.md
- [ ] Mathematical mapping present & consistent  
      File: stage7/SUBMISSION_PACKAGE/metadata/INVARIANT_MAPPING_v5.1.md
- [ ] Version alignment v3.3 → v5.1 verified  
      File: stage7/SUBMISSION_PACKAGE/metadata/VERSION_MAP_v3.3_to_v5.1.md
- [ ] Authorship & stewardship policy correct  
      File: stage7/SUBMISSION_PACKAGE/metadata/AUTHORSHIP_AND_STEWARDSHIP.md
- [ ] Manuscript header reflects v5.1_final (Stage 7 Closure)  
      File: stage7/SUBMISSION_PACKAGE/manuscript/MANUSCRIPT_v5.1.md

**Expected Output:** `Gemini_Revalidation_Package_v5.1_final.zip` + `.sha256`
