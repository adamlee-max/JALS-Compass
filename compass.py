"""
JALS Compass — Operational Proxy (C_proxy)
Implements the quick, testable linear form of the Law of Sustainable Intelligence (LSI).
Full derivation: /paper_v3.3/formula_v3.3.md
"""

def jals_compass(E_m, R, Pr, H, G):
    """
    Pragmatic proxy of C(π) for simple viability checks.

    Args:
        E_m: meaningful effort (0–1)
        R: reciprocity / cooperation (0–1)
        Pr: breach or pressure risk (0–1)
        H: hiddenness / opacity (0–1)
        G: goal drift / regret (0–1)
    Returns:
        float: C_proxy score (approx. -1 → +1)
    """
    C = 0.3 * E_m + 0.3 * R - 0.2 * Pr - 0.1 * H - 0.1 * G
    return round(C, 3)


if __name__ == "__main__":
    # Example: quick self-check
    score = jals_compass(E_m=0.85, R=0.80, Pr=0.15, H=0.10, G=0.05)
    print(f"C_proxy = {score:.2f} → {'Viable' if score > 0.2 else 'Failing'}")
