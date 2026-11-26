import numpy as np, mpmath as mp, time, sys
sys.dont_write_bytecode = True
from l3_fin import *
rng = np.random.default_rng(12)
M0 = rand_point(rng); q = rng.normal(size=4)
d = leaf_data(M0, q); alpha = rng.normal(size=4)
cd = canonical_data(d, np.array([np.cos(0.3), np.sin(0.3)]), alpha)
print("a,b =", cd['a'], cd['b'], " c0 =", cd['c0'])
a, b = mp.mpf(cd['a']), mp.mpf(cd['b'])
for rho in (0.3, 3.0, 12.0):
    s = rho * PH / max(a, b)
    vals = []
    for nq in (6, 8, 12):
        t = time.time(); v = k2coef_e(a, b, cd['kappa'], cd['alpha'], cd['y'], cd['c0'], s, nquad=nq); vals.append((nq, mp.nstr(v, 12), round(time.time() - t, 1)))
    print("rho=%.1f/max(a,b):" % rho, vals)
