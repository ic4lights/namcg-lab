"""040 t1: engine_z with a scalar species (chi=1, no Zeeman) reproduces the 034 engine_e_mp kappa^2 coefficient (VV part only)."""
import sys, numpy as np, mpmath as mp
sys.dont_write_bytecode = True
from engine_z import *
import engine_e_mp as e0
mp.mp.dps = 30
rng = np.random.default_rng(3)
kappa = rng.normal(size=4)
y = rng.normal(size=4)
y = y - kappa * (y @ kappa) / (kappa @ kappa)
alpha = rng.normal(size=4); c0 = 0.8
a, b = mp.mpf('0.7'), mp.mpf('1.3')
for s in (mp.mpf('0.4'), mp.mpf('0.9') * mp.expj(-0.6)):
    r1 = e0.k2coef_e(a, b, kappa, alpha, y, c0, s, nquad=8, lam=mp.mpf('1e-8'))
    r2 = k2coef_z(lambda kk: [scalar_species()], a, b, kappa, alpha, y, c0, s, nquad=8)
    print('s=', mp.nstr(s, 6), 'engine_e_mp', mp.nstr(r1, 12), ' engine_z scalar', mp.nstr(r2, 12), ' reldiff', mp.nstr(abs(r1 - r2) / abs(r1), 3))
