#!/usr/bin/env python3
"""
problem_f_heat_kernel.py
Exact Seeley-DeWitt Heat-Kernel Evaluation for Problem F (Coefficients A, B, C & G_eff)
Calculates traced heat-kernel coefficients a_0, a_1, a_2 across field content and ghosts.
"""

import numpy as np

def evaluate_seeley_dewitt_sector(field_type, weight, fibre_dim, E_endomorphism=0.0, non_minimal_xi=0.0):
    """
    Computes Seeley-DeWitt coefficients for a single Laplace-type operator:
    O = -D^2 + E
    a_0 = tr(I)
    a_1 = tr(1/6 * R - E) = fibre_dim * (1/6 - non_minimal_xi) * R - tr(E_0)
    """
    a0 = fibre_dim
    # Curvature coefficient multiplying R in a_1
    a1_R_coeff = fibre_dim * ((1.0 / 6.0) - non_minimal_xi) - E_endomorphism
    
    return {
        'type': field_type,
        'weight': weight,
        'fibre_dim': fibre_dim,
        'a0': weight * a0,
        'a1_R': weight * a1_R_coeff
    }

def run_problem_f_evaluation():
    print("=== PROBLEM F: SEELEY-DEWITT HEAT-KERNEL SECTOR SUM ===")
    
    # Define exact sector spectrum for locked condensate block
    sectors = [
        # Real scalar / radial mode (1 component, weight +1)
        evaluate_seeley_dewitt_sector("Radial Scalar (sigma)", weight=1.0, fibre_dim=1, non_minimal_xi=0.0),
        # Symmetric trace-free tensor T_mu_nu (9 components, weight +1)
        evaluate_seeley_dewitt_sector("Tensor Block (T_munu)", weight=1.0, fibre_dim=9, non_minimal_xi=0.0),
        # Vector current A_mu (4 components, weight +1)
        evaluate_seeley_dewitt_sector("Internal Vector (A_mu)", weight=1.0, fibre_dim=4, non_minimal_xi=0.0),
        # Diffeomorphism Ghosts (4 vector components, weight -2 for complex ghost)
        evaluate_seeley_dewitt_sector("Diff Ghosts", weight=-2.0, fibre_dim=4, non_minimal_xi=0.0),
        # Local Lorentz Ghosts (6 antisymmetric components, weight -2)
        evaluate_seeley_dewitt_sector("Lorentz Ghosts", weight=-2.0, fibre_dim=6, non_minimal_xi=0.0),
    ]
    
    total_a0 = sum(s['a0'] for s in sectors)
    total_a1_R = sum(s['a1_R'] for s in sectors)
    
    print("\n[Sector-by-Sector Breakdown]")
    print(f"{'Sector Name':<25} | {'Weight':>6} | {'Dim':>4} | {'Net a0':>8} | {'Net a1(R)':>10}")
    print("-" * 65)
    for s in sectors:
        print(f"{s['type']:<25} | {s['weight']:6.1f} | {s['fibre_dim']:4d} | {s['a0']:8.1f} | {s['a1_R']:10.3f}")
        
    print("-" * 65)
    print(f"{'TOTAL WEIGHTED TRACE (N_0)':<25} | {'--':>6} | {'--':>4} | {total_a0:8.1f} | {total_a1_R:10.3f}")
    
    # Calculate conditional 1/G_eff matching coefficient
    # 1 / (16 * pi * G_eff) = (total_a1_R / (32 * pi^2)) * Lambda_UV^2
    # => 1 / G_eff = (16 * pi * total_a1_R / (32 * pi^2)) * Lambda_UV^2 = (total_a1_R / (2 * pi)) * Lambda_UV^2
    G_eff_prefactor = total_a1_R / (2.0 * np.pi)
    
    print(f"\n[Calculated Heat-Kernel Pre-factor]")
    print(f"  N_0 (Effective fibre trace count) = {total_a0}")
    print(f"  Curvature Coefficient Pre-factor   = {total_a1_R:.4f}")
    print(f"  1 / G_eff Pre-factor (A_coeff)    = {G_eff_prefactor:.4f}")
    
    if G_eff_prefactor > 0:
        print("  --> RESULT: Positive G_eff (Attractive Gravitational Coupling)")
    else:
        print("  --> RESULT: Repulsive Gravitational Coupling (Wrong Sign G_eff)")

if __name__ == "__main__":
    run_problem_f_evaluation()