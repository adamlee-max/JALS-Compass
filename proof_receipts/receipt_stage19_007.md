# Stage19_007 — Instant vs Mixed Survival (v1)

**Goal**  
Compare survival curves between the Stage19 v1 variants:  
- **Instant (v1)** — `experiments/hostile_env/results/hostile_env_instant_v1.csv`  
- **Mixed (v1)** — `experiments/hostile_env/results/hostile_env_mixed_v1.csv`

**Method**  
Ran comparison helper:

```bash
python3 proof_receipts/hostile_env_compare_v1.pysts=$(date -u +"%Y%m%dT%H%MZ") && \
mkdir -p audits && \
git rev-parse HEAD > audits/GIT_REV.txt && \
{ 
  echo "== STAGE19 AUDIT MANIFEST =="
  echo "timestamp: $ts (UTC)"
  echo -n "git_rev: "; cat audits/GIT_REV.txt
  echo ""
  echo "== files =="
  printf "%-9s  %s\n" "BYTES" "PATH"
  find experiments/hostile_env -type f -print0 | xargs -0 stat -f "%z %N" | sort -n | awk '{printf("%-9s  ",$1); $1=""; print substr($0,2)}'
  echo ""
  echo "== sha256 =="
  find experiments/hostile_env -type f -print0 | xargs -0 shasum -a 256
} > audits/STAGE19_manifest.txt && \
zip -rq audits/STAGE19_audit_$ts.zip \
  experiments/hostile_env \
  proof_receipts/hostile_env_compare_v1.png \
  proof_receipts/receipt_stage19_007.md \
  audits/GIT_REV.txt audits/STAGE19_manifest.txt && \
echo "== WROTE: audits/STAGE19_audit_$ts.zip =="
**Outputs**
- Combined plot: `proof_receipts/hostile_env_compare_v1.png`
- Inputs: `experiments/hostile_env/results/hostile_env_instant_v1.csv`, `experiments/hostile_env/results/hostile_env_mixed_v1.csv`

**Result (v1)**
The survival curves diverge between ~200–280 steps; **Instant (total)** retains ~5–15 more survivors across the decline and reaches extinction slightly later (~290–300 steps) than **Mixed (total)**.

**Conclusion**
Under identical hostile conditions, **instant-knowledge agents survive measurably longer than mixed**. This matches the Stage-19 prediction that higher effective coherence (**C_proxy**) correlates with survival.  
**Stage19_007 is closed.**