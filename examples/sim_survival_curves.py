# sim_survival_curves.py
# Stage-5 prototype: generate survival curves for JALS vs Anti-JALS

import numpy as np
import matplotlib.pyplot as plt

def simulate(model, N=500, T=300, shock_time=75):
    failures = []
    for k in range(N):
        # initialise random seed for reproducibility
        rng = np.random.default_rng(k)
        # baseline proxy states
        Em, R, Pr, H, G = 1.0, 1.0, 0.2, 0.2, 0.2
        failed_at = None
        for t in range(T):
            if t == shock_time:
                Pr += 0.3  # disturbance
            # model parameters
            if model == "JALS":
                α, β, γ = 1.0, 1.0, 1.0
            else:  # Anti-JALS
                α, β, γ = 0.0, 0.0, 2.0
                R = 0.0
                Em = max(0, rng.normal(0.3, 0.05))
                Pr += rng.normal(0.02, 0.01)
                H += rng.normal(0.02, 0.01)
                G += rng.normal(0.02, 0.01)
            # compute C
            C = 1/(1+np.exp(-(α*Em + β*R - γ*(Pr+H+G))))
            if C < 0.2 and failed_at is None:
                failed_at = t
        failures.append(failed_at if failed_at is not None else T)
    return np.array(failures)

def km_curve(fail_times, T):
    # Kaplan–Meier survival estimator
    times = np.arange(T)
    surv = np.ones(T)
    n = len(fail_times)
    for t in range(1, T):
        deaths = np.sum(fail_times == t)
        risk = np.sum(fail_times >= t)
        surv[t] = surv[t-1] * (1 - deaths / risk) if risk > 0 else surv[t-1]
    return times, surv

def main():
    N, T = 500, 300
    fail_jals = simulate("JALS", N, T)
    fail_anti = simulate("ANTI", N, T)
    t, S_jals = km_curve(fail_jals, T)
    _, S_anti = km_curve(fail_anti, T)

    plt.plot(t, S_jals, label="JALS (balanced)")
    plt.plot(t, S_anti, label="Anti-JALS (unbalanced)", linestyle="--")
    plt.axhline(0.2, color="grey", ls=":", lw=1)
    plt.xlabel("Time (t)")
    plt.ylabel("Survival S(τ)")
    plt.title("Figure 2 — Survival under disturbance")
    plt.legend()
    plt.tight_layout()
    plt.savefig("assets/plots/Figure2_survival_curves.png", dpi=300)
    print("✅ Figure 2 saved → assets/plots/Figure2_survival_curves.png")

if __name__ == "__main__":
    main()