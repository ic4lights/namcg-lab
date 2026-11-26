#!/usr/bin/env python3
"""
symbolic_problem_c.py
Symbolic evaluation of Problem C (Conformal Mode Mass & Kinetic Sign)
Computes exact pure-trace Einstein-Hilbert + scalar potential Hessian and tests
kinetic normalization Z = 2N - 3/(4*pi*G_eff*v^2).
"""

import sympy as sp

def analyze_conformal_sector_symbolically():
    print("=== PROBLEM C: SYMBOLIC HESSIAN & KINETIC SIGN ANALYSIS ===")
    
    # Define symbolic variables
    sigma = sp.Symbol('sigma', real=True)
    v = sp.Symbol('v', positive=True, real=True)
    lam = sp.Symbol('lambda', positive=True, real=True)
    N = sp.Symbol('N', integer=True, positive=True, real=True)
    G_eff = sp.Symbol('G_eff', positive=True, real=True)
    M_P = sp.Symbol('M_P', positive=True, real=True) # Planck mass
    
    # 1. Pure-trace conformal factor Omega = 1 + sigma/v
    Omega = 1 + sigma / v
    
    # 2. Matrix Mexican-hat potential for singlet radial mode
    # V(sigma) = (lambda/4) * N * ((v + sigma)^2 - v^2)^2
    V = (lam / 4) * N * ((v + sigma)**2 - v**2)**2
    
    # Taylor expand potential up to O(sigma^3)
    V_expanded = sp.series(V, sigma, 0, 3).removeO()
    print(f"\n[1] Pure-trace Potential Expansion V(sigma):\n    V = {V_expanded}")
    
    # Second derivative V'' at vacuum (sigma = 0)
    V_pp = sp.diff(V, sigma, 2).subs(sigma, 0)
    print(f"    V''(0) = {V_pp}")
    
    # 3. Induced Einstein-Hilbert conformal kinetic term
    # sqrt(-g) R = 6 * (d Omega)^2 = 6/v^2 (d sigma)^2
    # Preloaded with 1 / (16 * pi * G_eff) = M_P^2 / 2
    # Yields induced kinetic term: + (3 * M_P^2 / v^2) * (d sigma)^2
    
    # Microscopic kinetic term: - N * (d sigma)^2
    # Combined kinetic Lagrangian density: - 1/2 * Z * (d sigma)^2
    # Z = 2*N - (3 * M_P^2) / v^2
    Z = 2 * N - (3 * M_P**2) / v**2
    print(f"\n[2] Exact Kinetic Normalization Factor Z:\n    Z = {Z}")
    
    # Critical vacuum ratio for ghost-free kinetic term (Z > 0)
    v_critical = sp.solve(Z, v)[0]
    print(f"\n[3] Critical Threshold for Ghost-Freedom (Z > 0):\n    v > {v_critical}")
    
    # Pole mass formula: m^2 = V''(0) / Z
    m_sq_pole = V_pp / Z
    print(f"\n[4] Pole Mass Squared m_psi^2:\n    m_psi^2 = {sp.simplify(m_sq_pole)}")
    
    return Z, v_critical, m_sq_pole

if __name__ == "__main__":
    analyze_conformal_sector_symbolically()