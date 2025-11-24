import os
import pandas as pd
import matplotlib.pyplot as plt

INSTANT_PATH = "experiments/hostile_env/results/hostile_env_instant_v1.csv"
MIXED_PATH   = "experiments/hostile_env/results/hostile_env_mixed_v1.csv"

def load(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    # expected columns: t,total,jals,anti — use total as the survival proxy
    if "survival" not in df.columns:
        df["survival"] = df["total"]
    return df

def compare(out_path: str = "proof_receipts/hostile_env_compare_v1.png") -> None:
    inst = load(INSTANT_PATH)
    mix  = load(MIXED_PATH)

    plt.figure(figsize=(7.2, 4.2))
    plt.plot(inst["t"], inst["survival"], label="Instant (total)")
    plt.plot(mix["t"],  mix["survival"],  label="Mixed (total)")
    plt.xlabel("Step")
    plt.ylabel("Survivors")
    plt.title("Instant vs Mixed — Survival (Stage19 v1)")
    plt.legend()
    plt.tight_layout()
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.savefig(out_path, dpi=150)
    plt.close()
    print("[Stage19 v1 — Compare] Saved plot:", out_path)

if __name__ == "__main__":
    compare()
