import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Stage 20 Simulation v1 (Compass-aligned)

INPUT_PATH = "experiments/finance_2008/data/banks_2008_dataset_clean.csv"
PLOT_PATH = "experiments/finance_2008/results/banks_2008_cproxy_trajectories.png"
SUMMARY_PATH = "experiments/finance_2008/results/banks_2008_summary.csv"

# C_proxy EMA calculation (matched to your Stage 19 side-car version)
def calculate_cproxy_ema(values, span=4, hysteresis=0.12):
    raw = (
        0.30 * np.array(values['Em']) +
        0.30 * np.array(values['R']) -
        0.20 * np.array(values['Pr']) -
        0.10 * np.array(values['H']) -
        0.10 * np.array(values['G'])
    )
    ema = pd.Series(raw).ewm(span=span, adjust=False).mean()

    crossed = False
    for i in range(len(ema)):
        if not crossed and ema[i] < -0.25:
            if i == 0 or ema[i-1] >= -0.25:
                ema[i] = max(ema[i], -0.25 + hysteresis)
            else:
                crossed = True

    return ema

df = pd.read_csv(INPUT_PATH)

banks = df.bank.unique()

plt.figure(figsize=(12,7))
summary = []

for bank in banks:
    sub = df[df.bank == bank].sort_values("quarter")
    c_ema = calculate_cproxy_ema(sub)

    plt.plot(
        sub.quarter,
        c_ema,
        label=f"{bank} ({'Survived' if c_ema.iloc[-1] > -0.25 else 'Collapsed'})"
    )

    summary.append({
        "bank": bank,
        "c_min": round(float(c_ema.min()),3),
        "c_final": round(float(c_ema.iloc[-1]),3),
        "collapsed": c_ema.iloc[-1] < -0.25
    })

plt.axhline(-0.25, color="red", linestyle="--", label="Collapse threshold")
plt.title("Stage 20 — 2008 Crisis: C_proxy EMA Trajectories")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig(PLOT_PATH)

pd.DataFrame(summary).to_csv(SUMMARY_PATH, index=False)

print("Stage 20 complete — results written:")
print(" -", PLOT_PATH)
print(" -", SUMMARY_PATH)
