"""Exact fit on the rotation-invariant SD family (random polynomial data), points of Sigma={x1=x2=0}:
   conjecture:  X' = (3/2) g,   tau_Omega = R_Sigma + (3/4) g,   g := |grad_Sigma ln rho|^2_{g_Sigma}  (g_Sigma = rho delta).
   hence 24 pi sigma_log = (3/2)X' - tau = (3/2) g - R_Sigma."""
import sys, random
import sympy as sp
from common import *
import sd_family, sd_rot_family, base_a_side as B
use_gaussian(3)
x1, x2, x3, x4 = sd_family.X
bad = 0; n = 0
for seed in range(int(sys.argv[1]) if len(sys.argv) > 1 else 6):
    bsol, eta, nf = sd_rot_family.rot_solution(4, seed)
    rho = sp.expand(bsol[0]**2 + bsol[1]**2 + bsol[2]**2)
    random.seed(50 + seed)
    for t in range(3):
        p3 = sp.Rational(random.randint(-4, 4), random.randint(2, 6)); p4 = sp.Rational(random.randint(1, 4), random.randint(2, 6))
        sub = {x1: 0, x2: 0, x3: p3, x4: p4}
        rho0 = rho.subs(sub)
        if rho0 == 0: continue
        r3 = sp.diff(rho, x3).subs(sub); r4 = sp.diff(rho, x4).subs(sub)
        g = sp.together((r3**2 + r4**2) / rho0**2 / rho0)
        lap = sp.diff(rho, x3, 2) + sp.diff(rho, x4, 2)
        lap_ln = (lap.subs(sub) / rho0 - (r3**2 + r4**2) / rho0**2)
        RS_int = sp.together(-lap_ln / rho0)
        d = B.run((0, 0, p3, p4), bsol=bsol, eta=eta)
        RS = sp.nsimplify(d['Rsig'])
        D0 = sp.simplify(RS - RS_int)
        D1 = sp.simplify(d['Xp'] - sp.Rational(3, 2) * g)
        D2 = sp.simplify(d['T'] - RS - sp.Rational(3, 4) * g)
        n += 1
        ok = (D0 == 0 and D1 == 0 and D2 == 0)
        bad += (not ok)
        print('seed', seed, 'pt', (p3, p4), 'R_Sigma-intrinsic:', D0, ' X-1.5g:', D1, ' T-R_Sigma-0.75g:', D2, ' g=', g, ' R_Sigma=', RS)
        sys.stdout.flush()
print('points', n, 'failures', bad)
