"""On SD/ASD closed-form J=0 backgrounds the a_2 density of each sector is nonzero; find all (N_s, n_D) for which
the weighted total (N_s-2) s + v - n_D d vanishes on a set of backgrounds (least squares / exact solve)."""
import sympy as sp
import jetlib as jl
from jetlib import Jet
from common import *
import geom, sd_family
use_gaussian(3)
gm = gam_mn_domain()
rows = []
for anti in (False, True):
    for seed in (1, 2, 3, 4):
        bsol, eta = sd_family.sd_solution(deg=3, seed=seed, anti=anti, b0=(1, 2, 3))
        w = sd_family.omega_jets(bsol, eta, (0, 0, 0, 0))
        Th = theta_from_omega(w)
        out, sqrtG, base = geom.sector_all(Th, gm)
        def cv(z):
            z = sqrtG*z
            return sp.Rational(z.x.numerator, z.x.denominator) if hasattr(z, 'x') else z
        s, v, d = [cv(out[k][1]) for k in ('scalar', 'vector', 'dirac')]
        rows.append((s, v, d))
a, nD = sp.symbols('a nD')
eqs = [a*s + v - nD*d for (s, v, d) in rows]
print('solutions of all', len(eqs), 'equations (a = N_s-2):', sp.solve(eqs, [a, nD], dict=True))
# also a_1 scan for comparison: a1 densities
