import numpy as np
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter

# ==============================
#  JALS vs Anti-JALS Null Model
#  Stage 17 – Empirical Receipt
# ==============================

EPISODES = 10000
MAX_STEPS = 200

# Survival storage
jals_survival = np.zeros(EPISODES)
anti_survival = np.zeros(EPISODES)


def run_episode(is_jals: bool = True) -> int:
    """
    Simple null-model episode:
    - JALS system recovers from shocks more effectively
    - Anti-JALS accumulates imbalance and collapses earlier
    """

    balance = 1.0

    for step in range(MAX_STEPS):
        # Random environmental shock
        shock = np.random.normal(0, 0.2)

        if is_jals:
            # JALS: Stable centre, negative feedback recovery
            balance += -0.3 * balance + shock
        else:
            # Anti-JALS: No recovery, runaway imbalance
            balance += +0.3 * balance + shock

        # Collapse condition
        if abs(balance) > 3:
            # the episode length before collapse
            return int(step)

    # If it never collapsed, survived full duration
    return int(MAX_STEPS)


# ==============================
# Run full simulation
# ==============================

for i in range(EPISODES):
    jals_survival[i] = run_episode(is_jals=True)
    anti_survival[i] = run_episode(is_jals=False)

# Optional safety check
print("NaNs in JALS:", np.isnan(jals_survival).sum())
print("NaNs in Anti-JALS:", np.isnan(anti_survival).sum())

# ==============================
# Survival Curve Plot
# ==============================

kmf = KaplanMeierFitter()

plt.figure(figsize=(10, 6))

# JALS curve
kmf.fit(jals_survival, event_observed=jals_survival < MAX_STEPS, label="JALS")
kmf.plot(ci_show=False)

# Anti-JALS curve
kmf.fit(anti_survival, event_observed=anti_survival < MAX_STEPS, label="Anti-JALS")
kmf.plot(ci_show=False)

plt.title("Stage 17 Null Model – Survival Curves")
plt.xlabel("Steps Before Collapse")
plt.ylabel("Survival Probability")

# Save figure
plt.savefig("experiments/null_model/null_model_survival.png", dpi=300)
plt.close()