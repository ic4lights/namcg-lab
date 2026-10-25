"""040 t3: (i) sum of spin blocks = k2coef_z vector; (ii) growth of each block of Theta*block along rays s = rho e^{-i theta}.
Prediction: block exponent (per |s|)  -(a cos th + b sin th) + max_u [2 a cos th m(u) - 2 b sin th n(u)] with the E/B weights of the endpoints."""
import sys, numpy as np, mpmath as mp
sys.dont_write_bytecode = True
from l3_fin import *
from blocks_z import *
from engine_z import *
mp.mp.dps = 30
seed, th0 = 12, 0.8
rng = np.random.default_rng(seed)
M0 = rand_point(rng); q = rng.normal(size=4); alpha = rng.normal(size=4)
d = leaf_data(M0, q)
cd = canonical_data(d, np.array([np.cos(th0), np.sin(th0)]), alpha)
a, b = mp.mpf(cd['a']), mp.mpf(cd['b'])
print('a,b', a, b, ' theta* = arctan(a/b) = %.4f' % float(mp.atan(a / b)))
s = mp.mpf('0.07') * mp.expj(-0.5)
blk = k2_blocks(a, b, cd['kappa'], cd['alpha'], cd['y'], cd['c0'], s, nquad=8)
tot = sum(blk.values())
ref = k2coef_z(lambda kk: [vector_species(a, b, kk, np.array([mp.mpf(x) for x in cd['alpha']], dtype=object))], a, b, cd['kappa'], cd['alpha'], cd['y'], cd['c0'], s, nquad=8)
print('sum of blocks', mp.nstr(tot, 12), ' direct', mp.nstr(ref, 12), ' reldiff', mp.nstr(abs(tot - ref) / abs(ref), 3))
rho0 = 1.0
for th in (0.0, 0.4, 0.9, 1.199, 1.4):
    print('--- ray theta = %.3f' % th)
    for rho in (0.5, 1.0, 1.5):
        s = mp.mpf(rho) * mp.expj(-th)
        blk = k2_blocks(a, b, cd['kappa'], cd['alpha'], cd['y'], cd['c0'], s, nquad=8)
        Th = Theta(s, a, b)
        line = []
        for k in sorted(blk, key=lambda z: -abs(blk[z])):
            line.append('%s %.1f' % (k, float(mp.log10(abs(blk[k] * Th) + mp.mpf('1e-300')))))
        print(' rho=%.1f  log10|Theta*block| (top):' % rho, ' | '.join(line[:8]))
