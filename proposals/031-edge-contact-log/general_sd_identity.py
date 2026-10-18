"""Test whether (3/2)X' - tau_Omega = 2 R_Sigma^{(12)} (R_Sigma^{(12)} = R - 2R_ii + R_ijij, normal plane (1,2))
holds for GENERIC self-dual closed omega (no rotation symmetry), at random points. 029 checked it only at 3 points of one symmetric example."""
import sys, random
import sympy as sp
import jetlib as jl
import sd_family, lib
from common import *
import base_a_side as B

use_gaussian(3)
res = []
for seed in range(4):
    bsol, eta = sd_family.sd_solution(deg=3, seed=seed, b0=(1, 2, 3))
    random.seed(100 + seed)
    for t in range(2):
        x0 = tuple(sp.Rational(random.randint(-3, 3), random.randint(2, 5)) for _ in range(4))
        try:
            d = B.run(x0, bsol=bsol, eta=eta)
        except Exception as ex:
            print('seed', seed, 'x0', x0, 'ERR', ex); continue
        lhs = sp.Rational(3, 2) * d['Xp'] - d['T']
        rs = d['Rsig']
        W = d['Rijij'] - (d['Rii'] - d['R'] / 3)
        print('seed', seed, 'x0', x0, ' W(Weyl proj)=', sp.simplify(W), ' e-R/6=', sp.simplify(d['e'] - d['R'] / 6))
        print('   (3/2)X-T =', sp.nsimplify(lhs), '  2R_Sigma =', sp.nsimplify(2 * rs), '  ratio', sp.simplify(lhs / (2 * rs)) if rs != 0 else None)
        print('   X/Rsig', sp.simplify(d['Xp'] / rs), ' T/Rsig', sp.simplify(d['T'] / rs), ' Rii/R', sp.simplify(d['Rii'] / d['R']), ' Rijij/R', sp.simplify(d['Rijij'] / d['R']))
        sys.stdout.flush()
