import pandas as pd
import matplotlib.pyplot as plt
import os

INSTANT_PATH = "experiments/hostile_env/results/hostile_env_instant_v1.csv"
MIXED_PATH   = "experiments/hostile_env/results/hostile_env_mixed_v1.csv"

def load(path):
    df = pd.read_csv(path)
    # expected columns: t,total,jals,anti
    df["survival"] = df["total"]  # rename proxy
    return df

def main():
    inst = load(INSTANT_PATH)
    mix  = load(MIXED_PATH)

    plt.figure(figsize=(8,5))
    plt.plot(inst["t"], inst["survival"], label="Instant Only")
    plt.plot(mix["t"], mix["survival"], label="Mixed")
    plt.xlabel("t")
    plt.ylabel("survival (proxy)")
    plt.title("Hostile Environment – Instant vs Mixed")
    plt.legend()

    out = "experiments/hostile_env/results/hostile_env_compare_v1.png"
    plt.savefig(out, dpi=150, bbox_inches="tight")
    print(f"[Stage19 v1 – Compare] Saved plot: {out}")

if __name__ == "__main__":
    main()
