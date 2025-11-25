"""
Stage 19 — Hostile Environment Simulation (INSTANT-KNOWLEDGE v1)

This variant is identical to the baseline except for ONE rule:
JALS agents have *instant knowledge* of who is Anti-JALS and will
preferentially target Anti-JALS if any are visible. Anti-JALS still
choose targets at random. All other parameters match the baseline.

Outputs:
  - PNG: experiments/hostile_env/results/hostile_env_instant_v1.png
  - CSV: experiments/hostile_env/results/hostile_env_instant_v1.csv
"""

from __future__ import annotations
import os, random
from dataclasses import dataclass
from typing import List, Tuple
import numpy as np
import matplotlib.pyplot as plt

# Reproducible seeds (simple baseline parity)
random.seed(12345)
np.random.seed(12345)

# Paths
HERE = os.path.dirname(__file__)
RESULTS_DIR = os.path.join(HERE, "results")
os.makedirs(RESULTS_DIR, exist_ok=True)

# Match baseline parameters
PARAMS = {
    "num_agents": 200,          # total agents
    "frac_jals": 0.50,          # proportion of JALS vs Anti-JALS
    "steps": 500,               # time steps
    "base_stress": 0.003,       # background damage each step
    "attack_prob": 0.05,        # chance an agent attempts an attack each step
    "attack_damage": 0.08,      # nominal attack damage (weighted by visibility)
    # JALS vs Anti-JALS traits
    "jals_opacity": 0.25,       # lower = harder to hit (more “hidden”)
    "anti_opacity": 0.75,       # higher = easier to hit (more “visible”)
    "jals_health0": 1.00,       # starting health
    "anti_health0": 0.80,       # starting health
}

# --- Agent model ---
@dataclass
class Agent:
    kind: str          # "JALS" or "ANTI"
    health: float
    opacity: float     # 0 = fully visible, 1 = fully hidden
    alive: bool = True

    def is_alive(self) -> bool:
        return self.alive and self.health > 0.0


# --- Population factory ---
def create_population() -> List[Agent]:
    num_agents = PARAMS["num_agents"]
    n_j = int(num_agents * PARAMS["frac_jals"])
    n_a = num_agents - n_j

    agents: List[Agent] = []
    for _ in range(n_j):
        agents.append(Agent("JALS", PARAMS["jals_health0"], PARAMS["jals_opacity"]))
    for _ in range(n_a):
        agents.append(Agent("ANTI", PARAMS["anti_health0"], PARAMS["anti_opacity"]))
    random.shuffle(agents)
    return agents


# --- Core step with *instant knowledge* for JALS only ---
def step_environment_instant(agents: List[Agent]) -> None:
    base_stress = PARAMS["base_stress"]
    attack_prob = PARAMS["attack_prob"]
    attack_damage = PARAMS["attack_damage"]

    # Background stress
    for a in agents:
        if a.is_alive():
            a.health -= base_stress
            if a.health <= 0:
                a.alive = False

    # Indices of living agents
    alive_idx = [i for i, a in enumerate(agents) if a.is_alive()]
    if len(alive_idx) <= 1:
        return

    # Each alive agent may attack
    for idx in alive_idx:
        attacker = agents[idx]
        if not attacker.is_alive():
            continue
        if random.random() >= attack_prob:
            continue

        # Visible = 1 - opacity
        def visible_score(target: Agent) -> float:
            return 1.0 - target.opacity

        # Candidate targets (not self, alive)
        candidates = [j for j in alive_idx if j != idx]
        if not candidates:
            continue

        # INSTANT-KNOWLEDGE:
        # - If attacker is JALS, prefer Anti-JALS among visible candidates.
        # - Otherwise (Anti attacker), pick a random target.
        if attacker.kind == "JALS":
            anti_candidates = [j for j in candidates if agents[j].kind == "ANTI"]
            # If any Anti exist, pick the *most visible* Anti; else fall back to most visible overall.
            if anti_candidates:
                target_idx = max(anti_candidates, key=lambda j: visible_score(agents[j]))
            else:
                target_idx = max(candidates, key=lambda j: visible_score(agents[j]))
        else:
            target_idx = random.choice(candidates)

        target = agents[target_idx]
        if not target.is_alive():
            continue

        # Hit chance scales with target visibility
        hit_prob = visible_score(target)
        if random.random() < hit_prob:
            target.health -= attack_damage * hit_prob
            if target.health <= 0:
                target.alive = False


def count_population(agents: List[Agent]) -> Tuple[int, int]:
    jals = sum(1 for a in agents if a.is_alive() and a.kind == "JALS")
    anti = sum(1 for a in agents if a.is_alive() and a.kind == "ANTI")
    return jals, anti


def run_simulation() -> Tuple[List[int], List[int], List[int]]:
    steps = PARAMS["steps"]
    agents = create_population()

    total_surv, jals_surv, anti_surv = [], [], []

    for _ in range(steps):
        # record before step
        j, a = count_population(agents)
        total_surv.append(j + a)
        jals_surv.append(j)
        anti_surv.append(a)

        step_environment_instant(agents)

    return total_surv, jals_surv, anti_surv


def C_proxy_from_survival(total_surv: List[int]) -> float:
    n0 = float(PARAMS["num_agents"])
    steps = float(PARAMS["steps"])
    auc = sum(s / n0 for s in total_surv) / steps
    return float(auc)


def save_plot(total_surv: List[int], jals_surv: List[int], anti_surv: List[int], out_png: str):
    x = np.arange(len(total_surv))
    plt.figure(figsize=(7.2, 4.2))
    plt.plot(x, total_surv, label="Total")
    plt.plot(x, jals_surv, label="JALS (instant knowledge)")
    plt.plot(x, anti_surv, label="Anti-JALS")
    plt.xlabel("Step")
    plt.ylabel("Survivors")
    plt.title("Hostile Environment — Instant-Knowledge (v1)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_png, dpi=150)
    plt.close()


def save_csv(total_surv: List[int], jals_surv: List[int], anti_surv: List[int], out_csv: str):
    with open(out_csv, "w") as f:
        f.write("t,total,jals,anti\n")
        for t, (T, J, A) in enumerate(zip(total_surv, jals_surv, anti_surv)):
            f.write(f"{t},{T},{J},{A}\n")


def main():
    total_surv, jals_surv, anti_surv = run_simulation()
    c_est = C_proxy_from_survival(total_surv)

    png_path = os.path.join(RESULTS_DIR, "hostile_env_instant_v1.png")
    csv_path = os.path.join(RESULTS_DIR, "hostile_env_instant_v1.csv")

    save_plot(total_surv, jals_surv, anti_surv, png_path)
    save_csv(total_surv, jals_surv, anti_surv, csv_path)

    print(f"[Stage19 v1 — Instant] Saved plot: {png_path}")
    print(f"[Stage19 v1 — Instant] Saved data: {csv_path}")
    print(f"[Stage19 v1 — Instant] C_proxy (AUC-survival): {c_est:.3f}")


if __name__ == "__main__":
    main()