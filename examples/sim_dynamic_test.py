"""
Stage 4 Simulation – Dynamic Validation of C_proxy (Falsifiability Receipt #006)
Author: JALS Research Group
Date: 04 Nov 2025

Runs small stochastic and skewed-input tests to ensure the Compass proxy
does not “auto-balance” under unrealistic conditions.
Outputs results as JSON to /examples/results/.
"""

import json, os, random, statistics
from compass import jals_compass

os.makedirs("examples/results", exist_ok=True)

def run_skew_test():
    results = []
    for var in ["E_m", "R", "Pr", "H", "G"]:
        values = {v: 0.1 for v in ["E_m", "R", "Pr", "H", "G"]}
        values[var] = 1.0
        c = jals_compass(**values)
        results.append({"type": "skew", "max_var": var, "C_proxy": round(c, 3)})
    return results

def run_noise_test(n=50, base=None, noise=0.15):
    if base is None:
        base = {"E_m": 0.5, "R": 0.5, "Pr": 0.5, "H": 0.5, "G": 0.5}
    results = []
    for _ in range(n):
        noisy = {k: min(max(v + random.uniform(-noise, noise), 0), 1) for k, v in base.items()}
        c = jals_compass(**noisy)
        results.append(c)
    return {
        "type": "noise",
        "mean": round(statistics.mean(results), 3),
        "stdev": round(statistics.stdev(results), 3),
        "samples": len(results),
    }

def run_naive_optimizer():
    """Compare to naive optimizer ignoring Compass weights."""
    best = 0
    for _ in range(100):
        vals = {v: random.random() for v in ["E_m", "R", "Pr", "H", "G"]}
        c = jals_compass(**vals)
        if c > best:
            best = c
    return {"type": "naive_optimizer", "best_C_proxy": round(best, 3)}

if __name__ == "__main__":
    all_results = {
        "skew_test": run_skew_test(),
        "noise_test": run_noise_test(),
        "naive_optimizer": run_naive_optimizer(),
    }
    out_file = "examples/results/sim_dynamic_test_results.json"
    with open(out_file, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"✅ Simulation complete → {out_file}")
