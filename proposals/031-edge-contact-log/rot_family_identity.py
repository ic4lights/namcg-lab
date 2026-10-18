"""Rotation-invariant SD family (random polynomial data, free functions beta(x3,x4) etc.): at points of Sigma={x1=x2=0}
 (i)  Sigma totally geodesic check: R_Sigma(4D formula) == intrinsic -rho^{-1} Lap_0 ln rho
 (ii) (3/2)X' - tau_Omega  vs 2 R_Sigma
 (iii) independence of R_Sigma and |grad ln rho|^2_Sigma."""
import sys, random
import sympy as sp
import jetlib as jl
from common import *
import sd_rot_family, base_a_side as B

use_gaussian(3)
import sd_family
x1, x2, x3, x4 = sd_family.X
for seed in range(5):
    bsol, eta, nf = sd_rot_family.rot_solution(4, seed)
    rho = sp.expand(bsol[0]**2 + bsol[1]**2 + bsol[2]**2)
    lr = sp.log(rho)
    random.seed(10 + seed)
    for t in range(2):
        p3 = sp.Rational(random.randint(-3, 3), random.randint(3, 6)); p4 = sp.Rational(random.randint(-3, 3), random.randint(3, 6))
        x0 = (0, 0, p3, p4)
        d = B.run(x0, bsol=bsol, eta=eta)
        sub = {x1: 0, x2: 0, x3: p3, x4: p4}
        rho0 = rho.subs(sub)
        lap = (sp.diff(lr, x3, 2) + sp.diff(lr, x4, 2)).subs(sub)
        grad2 = ((sp.diff(lr, x3)**2 + sp.diff(lr, x4)**2) / rho).subs(sub)
        RS_int = sp.nsimplify(-lap / rho0)
        RS_4d = d['Rsig']
        lhs = sp.Rational(3, 2) * d['Xp'] - d['T']
        print('seed', seed, 'pt', (p3, p4), 'rho', rho0)
        print('   R_Sigma 4D-formula - intrinsic =', sp.simplify(RS_4d - RS_int), ' | W=', sp.simplify(d['Rijij'] - (d['Rii'] - d['R'] / 3)))
        print('   (3/2)X-T - 2R_Sigma =', sp.simplify(lhs - 2 * RS_4d), ' ; X/R_Sigma =', sp.simplify(d['Xp'] / RS_4d), ' T/R_Sigma =', sp.simplify(d['T'] / RS_4d))
        print('   |grad ln rho|^2_Sigma / R_Sigma =', sp.simplify(grad2 / RS_4d))
        sys.stdout.flush()
