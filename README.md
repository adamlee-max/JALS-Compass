# 🧭 Guardian–JALS Compass  
# JALS Compass
*A universal viability scoring tool using five invariants and transparent receipts.*

The **Guardian–JALS Compass** is a simple framework for evaluating whether a system — human, organisational, or AI — is balanced and viable.  
It applies five invariants:

1. **Boundary Symmetry** – every stable state sits between two collapse edges.
2. **Dynamic Centre Law** – the farther from balance, the higher the cost and risk.
3. **Loop–Continuity** – recovery and renewal define resilience.
4. **Pattern Sufficiency** – fragments contain enough information to infer the whole.
5. **History / Recurrence** – learning from past states maintains viability.

**C-score formula**

\[
C(\pi) = 0.3E[m] + 0.3R - 0.2Pr - 0.1H - 0.1G
\]

- **E[m]** = ability to maintain structure (0–1)
- **R** = recovery capacity
- **Pr** = probability of breach or failure
- **H** = opacity of information
- **G** = historical regret

**Interpretation:** C > 0.2 ≈ viable; C < 0 ≈ collapse risk.  
Each use creates a “receipt” — a transparent breakdown of the inputs and the score.
> ⚠️ **Note:** This is a live, rough working repo.  
> Expect messy folders, plain text, and receipts.  
> The Compass works — the polish can come later.  
> If you’re here, you’re early. 🚀**A universal viability scoring tool using five invariants and transparent receipts.**  

---

## 🔹 What is the Compass?  
The Guardian–JALS Compass is a framework for testing whether any system — biological, financial, ecological, technological, or social — is **viable**.  

It works by scoring a system across five invariants:  

1. **Boundary Symmetry** – Every system sits between two collapse edges.  
2. **Dynamic Centre** – The further from balance, the higher the risk.  
3. **Loop–Continuity** – Collapse and renewal are defaults, not bugs.  
4. **Pattern Sufficiency** – Fragments can reveal the whole.  
5. **History/Recurrence** – Past failures shape future survival.  

The Compass calculates a **viability score (C)** between -1.0 and +1.0:  

\[
C(\pi) = 0.3E[m] + 0.3R - 0.2Pr - 0.1H - 0.1G
\]

Where:  
- **E[m]** = ability to maintain structure  
- **R** = recovery/repair capacity  
- **Pr** = risk of breaching boundaries  
- **H** = opacity of patterns (how unclear things are)  
- **G** = historical regret (unlearned lessons)  

---

## 🔹 Why it matters  
- **Universal lens:** Works across domains.  
- **Receipts-first:** Every score shows its working.  
- **Practical:** Can guide real-world decisions, from projects to AI safety to climate systems.  

---

## 🔹 Example  
**System:** Trading strategy with 3:1 leverage, no stoploss, single exchange.  

- E[m] = 0.4 (fragile)  
- R = 0.2 (no recovery loop)  
- Pr = 0.8 (high collapse risk)  
- H = 0.5 (unclear metrics)  
- G = 0.6 (unlearned lessons)  

**Compass Score:** C = -0.08 → **Failing**.  

Receipts: Risk of collapse is high; needs recovery loops and boundaries.  

---

## 🔹 How to use it  
- Try the [**Compass GPT App**](#) (coming soon in the GPT Store).  
- Read the worked examples in `/examples/`.  
- Run your own systems through the formula and share results with #JALS.  
## 📂 Examples

Worked case studies showing the Compass in action:

- [Finance Example](examples/finance_example.md) – High-leverage crypto strategy (C = -0.09, Failing)
- (More examples coming soon: Biology, Ecology, AI, Simulation)

## 🔹 License  
MIT License — free to use, adapt, and share. Please credit **@JALSLAW**.  
