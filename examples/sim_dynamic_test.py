#!/usr/bin/env python3
"""
JALS Compass × LSI — Stage 4 (v3.3)
Dynamic Validation & Falsifiability Loop — Baby Step #4: Dynamic Log Expansion

This scaffold generates a C(t) time-series under noise, drift, and perturbations.
It is intentionally modular so the true Compass Law (v3.3) can be swapped in
at `compute_C()` without changing the logging/plots/receipts pipeline.

Outputs
-------
1) receipts/compass_receipt_006.csv  — canonical log (append-safe)
2) assets/plots/C_timeseries_<stamp>.png — visual receipt
3) stdout summary with falsifiability triggers crossed (if any)

Usage
-----
python examples/sim_dynamic_test.py \
  --steps 500 --seed 42 --dt 1.0 \
  --noise-sigma 0.03 --noise-skew 0.0 \
  --drift -0.0002 --shock-step 300 --shock-mag -0.15

Notes
-----
• Keep values in [0,1] unless testing boundary behaviour with --allow-outside.
• Replace `compute_C()` with the v3.3 functional once fixed in code.
• All file paths are relative to repo root; adjust if running elsewhere.
"""
from __future__ import annotations
import argparse
import os
import sys
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Tuple

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# -------------------------
# Config dataclasses
# -------------------------
@dataclass
class SimConfig:
    steps: int = 500
    dt: float = 1.0
    seed: int = 42
    noise_sigma: float = 0.03
    noise_skew: float = 0.0  # >0 right-skew, <0 left-skew; 0 ~ Gaussian
    drift: float = 0.0       # linear drift per step added to C
    shock_step: int | None = None
    shock_mag: float = 0.0
    allow_outside: bool = False  # if False, clip C to [0,1]


# -------------------------
# Compass v3.3 placeholder
# -------------------------
# Invariants placeholder state (you can extend/replace with real measures)
@dataclass
class Invariants:
    B: float  # Boundary Symmetry
    D: float  # Dynamic Centre
    L: float  # Loop Continuity
    P: float  # Pattern Sufficiency
    R: float  # Recurrence


def compute_C(inv: Invariants, t: int, params: Dict[str, float] | None = None) -> float:
    """Placeholder for Compass Law (v3.3) functional.
    Replace this with the true definition. Current version provides a smooth,
    bounded surrogate to unblock logging and falsifiability plumbing.
    """
    w = params or {"B": 0.22, "D": 0.22, "L": 0.18, "P": 0.18, "R": 0.20}
    raw = (
        w["B"] * inv.B +
        w["D"] * inv.D +
        w["L"] * inv.L +
        w["P"] * inv.P +
        w["R"] * inv.R
    )
    # Mild nonlinearity to discourage edge-loading; tune/replace per v3.3
    C = 1 / (1 + np.exp(-4 * (raw - 0.5)))
    return float(C)


# -------------------------
# Noise & drift machinery
# -------------------------

def skewed_noise(rng: np.random.Generator, sigma: float, skew: float) -> float:
    """Generate zero-mean noise with optional skew via a simple transformation.
    For small |skew| this approximates skewness without heavy tails.
    """
    if sigma <= 0:
        return 0.0
    z = rng.normal(loc=0.0, scale=sigma)
    if abs(skew) < 1e-9:
        return float(z)
    # transform: apply tanh to introduce asymmetry
    return float(np.tanh(z + skew * abs(z))) * sigma / 0.76  # scale back roughly


def step_invariants(inv: Invariants, rng: np.random.Generator, sigma: float, skew: float) -> Invariants:
    """Evolve invariants with small stochastic perturbations in [0,1]."""
    def bump(x: float) -> float:
        dx = skewed_noise(rng, sigma, skew)
        return np.clip(x + dx, 0.0, 1.0)
    return Invariants(B=bump(inv.B), D=bump(inv.D), L=bump(inv.L), P=bump(inv.P), R=bump(inv.R))


# -------------------------
# Falsifiability triggers (edit as needed)
# -------------------------
@dataclass
class Triggers:
    min_viability: float = 0.2     # if C drops below, flag
    max_volatility: float = 0.15   # if rolling std > threshold, flag
    window: int = 50               # window for volatility check


# -------------------------
# Simulation core
# -------------------------

def run_sim(cfg: SimConfig, trig: Triggers) -> Tuple[pd.DataFrame, Dict[str, bool]]:
    rng = np.random.default_rng(cfg.seed)

    # Initialize invariants near centre; you can seed from real measures here
    inv = Invariants(B=0.6, D=0.6, L=0.6, P=0.6, R=0.6)

    rows = []
    C_vals = []

    for t in range(cfg.steps):
        # evolve invariants
        inv = step_invariants(inv, rng, sigma=cfg.noise_sigma, skew=cfg.noise_skew)

        # compute C from invariants
        C_t = compute_C(inv, t)

        # apply drift
        C_t += cfg.drift

        # apply one-off shock
        shock = 0.0
        if cfg.shock_step is not None and t == cfg.shock_step:
            shock = cfg.shock_mag
            C_t += shock

        # keep bounded unless exploring boundary behaviour
        if not cfg.allow_outside:
            C_t = float(np.clip(C_t, 0.0, 1.0))

        C_vals.append(C_t)

        rows.append({
            "t": t,
            "C": C_t,
            "B": inv.B,
            "D": inv.D,
            "L": inv.L,
            "P": inv.P,
            "R": inv.R,
            "drift": cfg.drift,
            "shock": shock
        })

    df = pd.DataFrame(rows)

    # Falsifiability checks
    flags = {
        "fell_below_min": bool((df["C"] < trig.min_viability).any()),
        "high_volatility": False,
    }

    if len(df) >= trig.window:
        rolling_std = df["C"].rolling(trig.window).std()
        flags["high_volatility"] = bool((rolling_std > trig.max_volatility).any())
        df["C_std_w"] = rolling_std
    else:
        df["C_std_w"] = np.nan

    return df, flags


# -------------------------
# IO helpers
# -------------------------

def ensure_dirs():
    os.makedirs("receipts", exist_ok=True)
    os.makedirs("assets/plots", exist_ok=True)


def save_receipts(df: pd.DataFrame) -> str:
    stamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    csv_path = os.path.join("receipts", "compass_receipt_006.csv")

    # append-safe: include a run separator row
    sep = pd.DataFrame({c: [None] for c in df.columns})
    sep.loc[0, "t"] = f"--- new run {stamp} ---"

    if os.path.exists(csv_path):
        df_to_write = pd.concat([sep, df], ignore_index=True)
        df_to_write.to_csv(csv_path, mode="a", index=False, header=False)
    else:
        df_to_write = pd.concat([sep, df], ignore_index=True)
        df_to_write.to_csv(csv_path, index=False)

    return csv_path


def save_plot(df: pd.DataFrame) -> str:
    stamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    out = os.path.join("assets/plots", f"C_timeseries_{stamp}.png")

# Highlight shock window and trigger crossings
if "shock" in df.columns and df["shock"].any():
    shock_t = int(df.loc[df["shock"] != 0, "t"].iloc[0])
    plt.axvline(shock_t, color="red", linestyle="--", alpha=0.6, label="Shock")
if "C_std_w" in df.columns and not df["C_std_w"].isna().all():
    plt.legend()
    plt.figure(figsize=(10, 4.5))
    plt.plot(df["t"], df["C"], linewidth=2)
    plt.title("JALS Compass — C(t) dynamic series (Stage 4)")
    plt.xlabel("t (steps)")
    plt.ylabel("C")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(out, dpi=200)
    plt.close()
        return out


# -------------------------
# CLI
# -------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Stage 4 dynamic validation scaffold")
    p.add_argument("--steps", type=int, default=500)
    p.add_argument("--dt", type=float, default=1.0)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--noise-sigma", type=float, default=0.03)
    p.add_argument("--noise-skew", type=float, default=0.0)
    p.add_argument("--drift", type=float, default=0.0)
    p.add_argument("--shock-step", type=int, default=None)
    p.add_argument("--shock-mag", type=float, default=0.0)
    p.add_argument("--allow-outside", action="store_true")

    # Trigger thresholds
    p.add_argument("--min-viability", type=float, default=0.2)
    p.add_argument("--max-volatility", type=float, default=0.15)
    p.add_argument("--window", type=int, default=50)

    return p.parse_args()


def main() -> int:
    args = parse_args()

    cfg = SimConfig(
        steps=args.steps,
        dt=args.dt,
        seed=args.seed,
        noise_sigma=args.noise_sigma,
        noise_skew=args.noise_skew,
        drift=args.drift,
        shock_step=args.shock_step,
        shock_mag=args.shock_mag,
        allow_outside=args.allow_outside,
    )

    trig = Triggers(
        min_viability=args.min_viability,
        max_volatility=args.max_volatility,
        window=args.window,
    )

    ensure_dirs()

    df, flags = run_sim(cfg, trig)
    csv_path = save_receipts(df)
    plot_path = save_plot(df)

    print("\nStage 4 — Dynamic Validation run summary")
    print("---------------------------------------")
    print(f"steps: {cfg.steps} | seed: {cfg.seed} | noise_sigma: {cfg.noise_sigma} | skew: {cfg.noise_skew}")
    print(f"drift: {cfg.drift} | shock_step: {cfg.shock_step} | shock_mag: {cfg.shock_mag}")
    print(f"min_viability: {trig.min_viability} | max_volatility: {trig.max_volatility} | window: {trig.window}")
    print(f"log: {csv_path}")
    print(f"plot: {plot_path}")

    if flags["fell_below_min"]:
        print("⚠️  Trigger: C fell below minimum viability threshold.")
    if flags["high_volatility"]:
        print("⚠️  Trigger: rolling volatility exceeded threshold.")
    if not any(flags.values()):
        print("✅ No falsifiability triggers crossed in this run.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
