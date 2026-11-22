"""S0. Operator-level check on the bundle (independent of the section-value formulas):
for the vector fields D_a = u_a^b(E_b + (u Om_b) d/du), S_cd on G x GL(4) restricted to
Lorentz u, verify [S_cd, D_a] = eta_ad D_c - eta_ac D_d, read off T(u), R(u) from
[D_a, D_b] = -T_ab^c D_c + 1/2 R_ab^{cd} S_cd and compare with the rotated section values,
and evaluate M_b = eta^{ac}[D_c,[D_a,D_b]] at random Lorentz u (numerical).
Run: python -I s0_operator_check.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import opcheck, lin, bg

cases = [('F trace-free (s=1)', lin.bg_F()), ('F tau=1 (s=1)', lin.bg_F(tau=1.0)),
         ('H (kappa=1, zeta=1, x=0.5)', lin.bg_H(1.0, 1.0, 0.5))]
rng = np.random.default_rng(3)
cases.append(('control: Heisenberg C with random W (not a solution)', (lin.bg_H()[0], bg.W_of(np.round(rng.normal(size=24), 1)))))
for name, (C, W) in cases:
    for r in opcheck.check(C, W, [-1, 1, 1, 1], seed=5, npts=2):
        print(name, {k: '%.1e' % float(v) for k, v in r.items()})
