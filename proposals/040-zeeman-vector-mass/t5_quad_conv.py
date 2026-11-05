"""040 t5: u-quadrature convergence of the Zeeman-dressed vector integrand at large |s| on the ray theta*, flux rescaled to a ~ 1 (centre variable zeta -> r zeta)."""
import sys, numpy as np, mpmath as mp, time
sys.dont_write_bytecode = True
from l3_fin import *
from engine_z import *
mp.mp.dps = 40
seed, th0 = 12, 0.8
rng = np.random.default_rng(seed)
M0 = rand_point(rng); q = rng.normal(size=4); alpha = rng.normal(size=4)
d = leaf_data(M0, q)
r = 0.12
cd = canonical_data(d, r * np.array([np.cos(th0), np.sin(th0)]), alpha); cd['c0'] = 0.0
a, b = mp.mpf(cd['a']), mp.mpf(cd['b'])
ths = mp.atan(a / b)
print('a,b', mp.nstr(a, 5), mp.nstr(b, 5), 'theta*', mp.nstr(ths, 5), 'c0', cd['c0'])
for rho in (20, 50, 100):
    s = rho * mp.expj(-ths)
    out = []
    for nq in (16, 24, 32, 44):
        t = time.time()
        v = k2coef_z(lambda kk: [vector_species(a, b, kk, np.array([mp.mpf(x) for x in cd['alpha']], dtype=object))], a, b, cd['kappa'], cd['alpha'], cd['y'], cd['c0'], s, nquad=nq, lam=mp.mpf('1e-12'))
        out.append((nq, mp.nstr(v * Theta(s, a, b), 10), round(time.time() - t, 1)))
    print('rho', rho, out)
