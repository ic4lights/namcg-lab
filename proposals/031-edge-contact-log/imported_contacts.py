"""Imported (Hodge-type) contact terms for the vector sector of the fixed-state replica, log order, on the rotation-invariant
SD family (and the 029 example).  Compare with  -sigma_fs = [R_Sigma/24 - g/16]/pi  needed for cancellation.
 C_E  = -(R + 3 tr_N E_G)/(24 pi)          (Ricci-type delta, E_delta = -2 pi P_N)
 C_Om = tr(J Omega_12)/(24 pi)            (bundle-curvature delta Omega_delta = 2 pi J)"""
import sys, random
import sympy as sp
from common import *
import sd_family, sd_rot_family, sector_data as S
x1, x2, x3, x4 = sd_family.X
rows = []
for seed in range(int(sys.argv[1]) if len(sys.argv) > 1 else 3):
    bsol, eta, nf = sd_rot_family.rot_solution(4, seed)
    rho = sp.expand(bsol[0]**2 + bsol[1]**2 + bsol[2]**2)
    random.seed(70 + seed)
    for t in range(3):
        p3 = sp.Rational(random.randint(-4, 4), random.randint(2, 6)); p4 = sp.Rational(random.randint(1, 4), random.randint(2, 6))
        sub = {x1: 0, x2: 0, x3: p3, x4: p4}
        rho0 = rho.subs(sub)
        if rho0 == 0: continue
        r3 = sp.diff(rho, x3).subs(sub); r4 = sp.diff(rho, x4).subs(sub)
        g = sp.together((r3**2 + r4**2) / rho0**3)
        d = S.run((0, 0, p3, p4), bsol, eta)
        RS = d['Rsig']
        CE = -(d['R'] + 3 * d['trN_EG']) / 24     # times 1/pi
        COm = d['trJOm_v'] / 24
        rows.append((RS, g, d['Rii'], d['R'], CE, COm, d['tau'], d['Xp']))
        print('seed', seed, 'pt', (p3, p4), 'RSig', RS, 'g', g, 'R', d['R'], 'Rii', d['Rii'], 'CE*pi', CE, 'COm*pi', COm, 'tau', d['tau'], 'check tau-RS-.75g', sp.simplify(d['tau'] - RS - sp.Rational(3,4)*g), 'X-1.5g', sp.simplify(d['Xp']-sp.Rational(3,2)*g))
        sys.stdout.flush()
# fit CE, COm  = a RSig + b g + c Rii  (exact solve on first three rows, verify on the rest)
M = sp.Matrix([[r[0], r[1], r[2]] for r in rows])
for name, idx in (('C_E*pi', 4), ('C_Omega*pi', 5), ('tau', 6)):
    y = sp.Matrix([r[idx] for r in rows])
    sol = sp.linsolve((M[:3, :], y[:3, :]))
    sol = list(sol)[0]
    resid = [sp.simplify((M[i, :] * sp.Matrix(sol))[0] - y[i]) for i in range(len(rows))]
    print(name, '= a R_Sigma + b g + c R_ii with (a,b,c) =', sol, ' residuals on all rows:', resid)
