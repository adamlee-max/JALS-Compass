"""
Stage 19 — Hostile Environment Experiments (v1)
------------------------------------------------

Baseline simulation for the JALS Compass × Law of Sustainable Intelligence.

This script implements a simple hostile environment where:

- JALS agents are:
    * low opacity (easier to see / attack)
    * internally "balanced" (higher starting health)
- Anti-JALS agents are:
    * high opacity (harder to see / attack)
    * internally "imbalanced" (lower starting health)

Environment is hostile because:
    - Every step, agents lose health from background stress.
    - Agents randomly attack each other.
    - Attack success is weighted by target visibility (1 - opacity).

We run multiple simulations and plot:
    - Average number of JALS agents alive over time.
    - Average number of Anti-JALS agents alive over time.

This is a **baseline**:
    - No learning yet.
    - No dynamic weights yet.
    - No instant-knowledge / mixed fancy logic.
Those will be added in later versions (v2, v3, v4, v5).

Output:
    - A PNG file saved next to this script:
        hostile_env_survival_v1.png

Usage (from repo root, inside Codespaces/terminal):

    python3 experiments/hostile_env/hostile_env_sim_v1.py

"""

from __future__ import annotations

import random
from dataclasses import dataclass
from pathlib import Path
from typing import List, Literal, Tuple

import matplotlib.pyplot as plt
import numpy as np


AgentType = Literal["JALS", "ANTI"]


@dataclass
class Agent:
    """Simple agent in the hostile environment."""

    kind: AgentType
    health: float
    opacity: float  # 0 = fully visible, 1 = fully hidden
    alive: bool = True

    def is_alive(self) -> bool:
        return self.alive and self.health > 0.0


def create_initial_population(
    n_jals: int = 25,
    n_anti: int = 25,
    seed: int | None = None,
) -> List[Agent]:
    """Create a starting population of JALS and Anti-JALS agents."""
    if seed is not None:
        random.seed(seed)

    agents: List[Agent] = []

    # JALS: balanced, lower opacity (more visible), higher health
    for _ in range(n_jals):
        agents.append(
            Agent(
                kind="JALS",
                health=1.0,      # high starting coherence / resilience
                opacity=0.2,     # very visible → attacked more
            )
        )

    # Anti-JALS: imbalanced, higher opacity (more hidden), lower health
    for _ in range(n_anti):
        agents.append(
            Agent(
                kind="ANTI",
                health=0.7,      # lower internal coherence
                opacity=0.8,     # well hidden → attacked less
            )
        )

    return agents


def step_environment(
    agents: List[Agent],
    background_stress: float = 0.03,
    attack_prob: float = 0.6,
    attack_damage: float = 0.25,
) -> None:
    """
    Advance the environment by one time step.

    - All agents lose some health from background stress.
    - Each alive agent may attack one other agent.
    - Attack success probability is proportional to target visibility (1 - opacity).
    """

    # Background stress: everyone loses some health
    for a in agents:
        if a.is_alive():
            a.health -= background_stress
            if a.health <= 0:
                a.alive = False

    # Build list of indices of alive agents
    alive_indices = [i for i, a in enumerate(agents) if a.is_alive()]
    if len(alive_indices) <= 1:
        # Nothing interesting can happen with 0 or 1 survivor
        return

    # Each alive agent may attack once
    for idx in alive_indices:
        attacker = agents[idx]
        if not attacker.is_alive():
            continue

        if random.random() > attack_prob:
            # No attack this step
            continue

        # Choose a random target that is not the attacker
        possible_targets = [j for j in alive_indices if j != idx]
        if not possible_targets:
            continue

        target_idx = random.choice(possible_targets)
        target = agents[target_idx]

        if not target.is_alive():
            continue

        # Visibility-based hit chance: more visible targets get hit more often
        visibility = 1.0 - target.opacity  # e.g. 0.8 visible if opacity=0.2
        hit_prob = visibility  # simple mapping; could be tuned later

        if random.random() < hit_prob:
            target.health -= attack_damage
            if target.health <= 0:
                target.alive = False


def count_population(agents: List[Agent]) -> Tuple[int, int]:
    """Return (n_jals_alive, n_anti_alive)."""
    jals = sum(1 for a in agents if a.is_alive() and a.kind == "JALS")
    anti = sum(1 for a in agents if a.is_alive() and a.kind == "ANTI")
    return jals, anti


def run_simulation(
    steps: int = 30,
    runs: int = 10,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Run multiple hostile-environment simulations and return average survival curves.

    Returns
    -------
    avg_jals_alive : np.ndarray
        Shape (steps + 1,) – average number of JALS agents alive at each step.
    avg_anti_alive : np.ndarray
        Shape (steps + 1,) – average number of Anti-JALS agents alive at each step.
    """
    rng = random.Random(seed)

    all_jals = []
    all_anti = []

    for run in range(runs):
        run_seed = rng.randint(0, 1_000_000)
        agents = create_initial_population(seed=run_seed)

        jals_alive = []
        anti_alive = []

        # Record initial state at step 0
        j, a = count_population(agents)
        jals_alive.append(j)
        anti_alive.append(a)

        for _ in range(steps):
            step_environment(agents)
            j, a = count_population(agents)
            jals_alive.append(j)
            anti_alive.append(a)

        all_jals.append(jals_alive)
        all_anti.append(anti_alive)

    # Convert to arrays and average across runs
    jals_arr = np.array(all_jals, dtype=float)   # (runs, steps+1)
    anti_arr = np.array(all_anti, dtype=float)

    avg_jals = jals_arr.mean(axis=0)
    avg_anti = anti_arr.mean(axis=0)

    return avg_jals, avg_anti


def plot_results(
    avg_jals: np.ndarray,
    avg_anti: np.ndarray,
    steps: int,
) -> Path:
    """Plot survival curves and save PNG next to this script."""
    t = np.arange(steps + 1)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(t, avg_jals, label="JALS (balanced / visible)")
    ax.plot(t, avg_anti, label="Anti-JALS (imbalanced / hidden)")

    ax.set_xlabel("Time step")
    ax.set_ylabel("Agents alive (average over runs)")
    ax.set_title("Stage 19 — Hostile Environment Survival (v1)")
    ax.grid(True, alpha=0.3)
    ax.legend()

    out_path = Path(__file__).with_name("hostile_env_survival_v1.png")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)

    return out_path


def main() -> None:
    steps = 30
    runs = 10

    print("Running hostile environment baseline (v1)...")
    print(f"  Steps: {steps}")
    print(f"  Runs : {runs}")

    avg_jals, avg_anti = run_simulation(steps=steps, runs=runs, seed=19)

    # Simple text summary
    print("\nAverage survivors at final step:")
    print(f"  JALS     : {avg_jals[-1]:.2f}")
    print(f"  Anti-JALS: {avg_anti[-1]:.2f}")

    out_path = plot_results(avg_jals, avg_anti, steps=steps)
    print(f"\nPlot saved to: {out_path}")


if __name__ == "__main__":
    main()
