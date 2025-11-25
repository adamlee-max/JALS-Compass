"""
Stage 19 — Hostile Environment Simulation (MIXED v1)

This variant mixes behaviours: JALS agents sometimes use *instant knowledge*
(prefer Anti-JALS if visible), and sometimes behave randomly like baseline.

Outputs:
  - PNG: experiments/hostile_env/results/hostile_env_mixed_v1.png
  - CSV: experiments/hostile_env/results/hostile_env_mixed_v1.csv
"""

from __future__ import annotations
import os, random
from dataclasses import dataclass
from typing import List, Tuple
import numpy as np
import matplotlib.pyplot as plt

# Reproducible seeds
random.seed(12345)
np.random.seed(12345)

# Paths
HERE = os.path.dirname(__file__)
RESULTS_DIR = os.path.join(HERE, "results")
os.makedirs(RESULTS_DIR, exist_ok=True)

# Parameters (match baseline scale)
PARAMS = {
    "num_agents": 200,
    "frac_jals": 0.50,
    "steps": 500,
    "base_stress": 0.003,
    "attack_prob": 0.05,
    "attack_damage": 0.08,
    # traits
    "jals_opacity": 0.25,     # lower = harder to hit
    "anti_opacity": 0.75,     # higher = easier to hit
    "jals_health0": 1.00,
    "anti_health0": 0.80,
    # mixed behaviour knob: probability JALS uses instant-knowledge targeting
    "instant_prob": 0.5,
}

@dataclass
class Agent:
    kind: str          # "JALS" or "ANTI"
    health: float
    opacity: float
    alive: bool = True

    def is_alive(self) -> bool:
        return self.alive and self.health > 0.0

def create_population() -> List[Agent]:
    n = PARAMS["num_agents"]
    n_j = int(n * PARAMS["frac_jals"])
    n_a = n - n_j
    agents: List[Agent] = (
        [Agent("JALS", PARAMS["jals_health0"], PARAMS["jals_opacity"]) for _ in range(n_j)] +
        [Agent("ANTI", PARAMS["anti_health0"], PARAMS["anti_opacity"]) for _ in range(n_a)]
    )
    random.shuffle(agents)
    return agents

def step_environment_mixed(agents: List[Agent]) -> None:
    base_stress = PARAMS["base_stress"]
    attack_prob = PARAMS["attack_prob"]
    attack_damage = PARAMS["attack_damage"]
    instant_prob = PARAMS["instant_prob"]

    # background stress
    for a in agents:
        if a.is_alive():
            a.health -= base_stress
            if a.health <= 0:
                a.alive = False

    alive_idx = [i for i, a in enumerate(agents) if a.is_alive()]
    if len(alive_idx) <= 1:
        return

    def visible_score(target: Agent) -> float:
        return 1.0 - target.opacity

    for i in alive_idx:
        atk = agents[i]
        if not atk.is_alive() or random.random() >= attack_prob:
            continue
        candidates = [j for j in alive_idx if j != i]
        if not candidates:
            continue

        if atk.kind == "JALS" and random.random() < instant_prob:
            anti_candidates = [j for j in candidates if agents[j].kind == "ANTI"]
            if anti_candidates:
                target_idx = max(anti_candidates, key=lambda j: visible_score(agents[j]))
            else:
                target_idx = max(candidates, key=lambda j: visible_score(agents[j]))
        else:
            target_idx = random.choice(candidates)

        tgt = agents[target_idx]
        if not tgt.is_alive():
            continue
        hit_prob = visible_score(tgt)
        if random.random() < hit_prob:
            tgt.health -= attack_damage * hit_prob
            if tgt.health <= 0:
                tgt.alive = False

def count_population(agents: List[Agent]) -> Tuple[int, int]:
    jals = sum(1 for a in agents if a.is_alive() and a.kind == "JALS")
    anti = sum(1 for a in agents if a.is_alive() and a.kind == "ANTI")
    return jals, anti

def run_simulation() -> Tuple[List[int], List[int], List[int]]:
    steps = PARAMS["steps"]
    agents = create_population()
    total, jals, anti = [], [], []
    for _ in range(steps):
        J, A = count_population(agents)
        total.append(J + A)
        jals.append(J)
        anti.append(A)
        step_environment_mixed(agents)
    return total, jals, anti

def C_proxy_from_survival(total_surv: List[int]) -> float:
    n0 = float(PARAMS["num_agents"])
    steps = float(PARAMS["steps"])
    auc = sum(s / n0 for s in total_surv) / steps
    return float(auc)

def save_plot(total_surv: List[int], jals_surv: List[int], anti_surv: List[int], out_png: str):
    x = np.arange(len(total_surv))
    plt.figure(figsize=(7.2, 4.2))
    plt.plot(x, total_surv, label="Total")
    plt.plot(x, jals_surv, label="JALS (mixed)")
    plt.plot(x, anti_surv, label="Anti-JALS")
    plt.xlabel("Step"); plt.ylabel("Survivors"); plt.title("Hostile Environment — Mixed (v1)")
    plt.legend(); plt.tight_layout(); plt.savefig(out_png, dpi=150); plt.close()

def save_csv(total_surv: List[int], jals_surv: List[int], anti_surv: List[int], out_csv: str):
    with open(out_csv, "w") as f:
        f.write("t,total,jals,anti\n")
        for t, (T, J, A) in enumerate(zip(total_surv, jals_surv, anti_surv)):
            f.write(f"{t},{T},{J},{A}\n")

def main():
    total, jals, anti = run_simulation()
    c_est = C_proxy_from_survival(total)
    png_path = os.path.join(RESULTS_DIR, "hostile_env_mixed_v1.png")
    csv_path = os.path.join(RESULTS_DIR, "hostile_env_mixed_v1.csv")
    save_plot(total, jals, anti, png_path)
    save_csv(total, jals, anti, csv_path)
    print(f"[Stage19 v1 — Mixed] Saved plot: {png_path}")
    print(f"[Stage19 v1 — Mixed] Saved data: {csv_path}")
    print(f"[Stage19 v1 — Mixed] C_proxy (AUC-survival): {c_est:.3f}")

if __name__ == "__main__":
    main()