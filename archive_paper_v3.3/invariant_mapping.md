cd paper_v3.3
cat > invariant_mapping.md <<'EOF'
# Invariant ⇄ Proxy Mapping (Stage 10 / v5.1_final)

| Invariant (LSI)        | Proxy Variable | Direction | Rationale |
|------------------------|----------------|-----------|-----------|
| Boundary Symmetry (B)  | E_m            | + | Effort in ↔ value out (exchange symmetry). |
| Dynamic Centre (D)     | R              | + | Reciprocity maintains the system’s core balance. |
| Loop Continuity (L)    | Pr             | – | Breach risk breaks feedback loops. |
| Pattern Sufficiency (P)| H              | – | Opacity reduces usable pattern information. |
| Recurrence (R)         | G              | – | Goal drift erodes memory and stability. |

**Sign convention:** ‘+’ supports viability; ‘–’ reduces it.  
**Note:** This table documents the Stage-4 proxy; real domains can substitute metrics.
EOF

git add invariant_mapping.md
git commit -m "add: invariant_mapping.md (Stage 4 proxy table for Stage 5 prep)"
git push