#!/usr/bin/env python3
"""
falsify_problem_n.py
Analytical & Numerical Falsification Suite for Problem N (Ostrogradsky Ghosts)
Examines graviton two-point propagator poles and residue signs for higher-derivative gravity.
"""

import numpy as np

def analyze_ostrogradsky_propagator(alpha_vals, G_eff=1.0):
    """
    Analyzes the graviton propagator denominator:
    D(p^2) = p^2 * (1 - 32 * pi * G_eff * alpha * p^2)
    Locates extra spin-2 poles p_ghost^2 = 1 / (32 * pi * G_eff * alpha).
    """
    print("=== PROBLEM N: OSTROGRADSKY GHOST PROPAGATOR ANALYSIS ===")
    results = []
    
    for alpha in alpha_vals:
        if alpha == 0:
            status = "Pure GR (No extra poles)"
            p_ghost_sq = np.inf
            is_ghost = False
        else:
            p_ghost_sq = 1.0 / (32.0 * np.pi * G_eff * alpha)
            if alpha > 0:
                # Extra pole at physical p^2 > 0 with negative residue -> OSTROGRADSKY GHOST
                status = "PROPAGATING OSTROGRADSKY GHOST (Negative Residue)"
                is_ghost = True
            else:
                # Extra pole at p^2 < 0 -> TACHYON
                status = "TACHYONIC POLE (p^2 < 0)"
                is_ghost = True
                
        results.append({
            'alpha': alpha,
            'p_ghost_sq': p_ghost_sq,
            'is_ghost': is_ghost,
            'status': status
        })
    return results

def run_falsification_tests():
    # Test across a spectrum of coupling coefficients alpha (Weyl-squared coupling)
    alpha_test_range = [-1.0e-2, -1.0e-4, 0.0, 1.0e-5, 1.0e-3, 1.0e-1]
    results = analyze_ostrogradsky_propagator(alpha_test_range)
    
    print("\n[Results Summary]")
    print(f"{'Alpha':>12} | {'Ghost Pole (p^2)':>18} | {'Physical Status'}")
    print("-" * 65)
    for r in results:
        p_str = f"{r['p_ghost_sq']:.4e}" if not np.isinf(r['p_ghost_sq']) else "Infinity"
        print(f"{r['alpha']:12.2e} | {p_str:>18} | {r['status']}")
        
    print("\n[Conclusion for Problem N]")
    print("To avoid Ostrogradsky ghosts, higher-derivative operators C^2 and R^2 MUST NOT")
    print("be diagonalized as independent propagating degrees of freedom. They must be")
    print("treated strictly as EFT insertion vertices for momenta p^2 << p_ghost^2.")

if __name__ == "__main__":
    run_falsification_tests()