# Compass Example — High-Leverage Crypto Strategy

**Summary verdict:** **Failing** (C = **-0.09**) → Very high collapse risk unless boundaries and recovery loops are added.

---

## Scenario
A discretionary crypto strategy using **3:1 leverage**, **no stop-loss**, trading on a **single exchange**, with **no formal postmortems** after bad weeks and minimal observability beyond PnL.

## Invariant mapping → scores
- **E[m] (maintenance): 0.4**  
  Ad-hoc process, no runbooks, single-venue dependency.
- **R (recovery/repair): 0.2**  
  No staged rollbacks, no position caps, no weekly “kill switch” drill.
- **Pr (edge risk): 0.8**  
  High leverage + single exchange = one edge breach wipes the book.
- **H (pattern opacity): 0.5**  
  Few metrics beyond PnL; weak signal on risk drivers.
- **G (historical regret): 0.6**  
  Drawdowns recur; lessons not systematically captured.

## Compass calculation
\[
C(\pi) = 0.3E[m] + 0.3R - 0.2Pr - 0.1H - 0.1G
\]

Numbers:
- \(0.3 \times 0.4 = 0.12\)  
- \(0.3 \times 0.2 = 0.06\)  
- \(-0.2 \times 0.8 = -0.16\)  
- \(-0.1 \times 0.5 = -0.05\)  
- \(-0.1 \times 0.6 = -0.06\)

**Total C = 0.12 + 0.06 − 0.16 − 0.05 − 0.06 = -0.09 → Failing**

---

## Top risks (edges)
- Single-venue failure or liquidation cascade at 3:1 leverage.  
- No engineered boundary (no stop-loss/position cap).  
- No tested recovery loop after adverse moves.

## Levers to raise C
- **Boundary Symmetry (Pr↓):** Add hard position caps + per-trade stop-loss.  
- **Loop–Continuity (R↑):** Weekly drill: flatten risk to zero, restore from backup plan.  
- **Pattern Sufficiency (H↓):** Track drawdown, VaR, slippage, venue health as core signals.  
- **History/Recurrence (G↓):** Postmortem template + action tracker after every -5% week.  
- **Maintenance (E[m]↑):** Multi-venue routing or backup account to reduce single-point failure.

> **Band:** C < 0.00 = Failing. Target C ≥ 0.20 (Viable) after applying 2–3 levers.
>## Invariant breakdown (receipts)

**E[m] = 0.4** — fragile process, single-venue dependency  
**R = 0.2** — no rollback/stop-loss drills (weak recovery loop)  
**Pr = 0.8** — 3:1 leverage + single exchange = near the edge  
**H = 0.5** — poor observability beyond PnL  
**G = 0.6** — repeated drawdowns, lessons not embedded

### C(π) calculation
C = 0.3·E[m] + 0.3·R − 0.2·Pr − 0.1·H − 0.1·G

= (0.3×0.4) + (0.3×0.2) − (0.2×0.8) − (0.1×0.5) − (0.1×0.6)  
= 0.12 + 0.06 − 0.16 − 0.05 − 0.06  
= **−0.09 → Failing**
_Last updated: Oct 02, 2025_  

*#JALS*
