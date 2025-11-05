# Explicit Viability Function — C(t, π)

We define the system’s live viability score as:

\[
C(t, π) = σ [ α E_m + β R − γ ( Pr + H + G ) ]
\]

where:

| Symbol | Meaning | Role |
|---------|----------|------|
| E_m | Energy / effort exchange symmetry | Supports boundary balance |
| R | Reciprocity (centre stability) | Reinforces viability |
| Pr | Breach probability | Reduces feedback integrity |
| H | Information opacity | Reduces usable patterns |
| G | Goal drift | Reduces coherence |

**σ** = sigmoid scaling (0 → 1)  
**α, β, γ** = domain-specific weights.  
**t** = time; **π** = policy trajectory or intervention path.

### Simplified / Derived Form (S/D)

For the observed trajectory π*:
\[
C_{S/D}(t) = ΔC/Δt ≈ σ' ( α ΔE_m + β ΔR − γ ( ΔPr + ΔH + ΔG ) )
\]

Positive C or Ċ > 0 ⇒ system learning / recovery.  
Negative C or Ċ < 0 ⇒ system failure / collapse.

**Interpretation:**  
C is the real-time expression of the Law of Sustainable Intelligence:  
> Systems that balance, survive.