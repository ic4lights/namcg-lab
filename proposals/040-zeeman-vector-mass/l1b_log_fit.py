"""040 l1b: the 1/s coefficient of the vector (Zeeman-dressed) and Dirac responses as quadratic forms in alpha, fitted to F1 = y^2((k.a)^2 - k^2 a^2) and F2 = k^2 (a.y)^2.
c_X(alpha) = lim s * T2_X ; A-form of 034: A = (F1 - 2 F2)/24 (c = A/16 pi^2).  Fit c_X*16 pi^2 = g1 F1 + g2 F2 (indices raised with eta, canonical frame)."""
import sys, numpy as np, mpmath as mp
sys.dont_write_bytecode = True
from l3_fin import *
from l1_log_coefficient import spec
from engine_z import *
mp.mp.dps = 30
def c16(d, th, alpha, key, rho=mp.mpf('3e-4'), nq=6):
    cd = canonical_data(d, np.array([np.cos(th), np.sin(th)]), alpha)
    a, b = mp.mpf(cd['a']), mp.mpf(cd['b'])
    s = rho / max(a, b) * mp.expj(-mp.mpf('0.6'))
    v = k2coef_z(lambda kk: spec(key, a, b, kk, cd['alpha']), a, b, cd['kappa'], cd['alpha'], cd['y'], cd['c0'], s, nquad=nq, lam=mp.mpf('1e-6'))
    return complex(v * Theta(s, a, b) * s * 16 * mp.pi ** 2), cd
def F12(cd):
    al = cd['alpha']; k = cd['kappa']; y = cd['y']; e = etan
    y2 = y @ e @ y; k2 = k @ e @ k
    ka = k @ e @ al; a2 = al @ e @ al; ay = al @ y   # alpha lower, y upper
    return y2 * (ka ** 2 - k2 * a2), k2 * ay ** 2
if __name__ == "__main__":
    seed = int(sys.argv[1]); th = float(sys.argv[2])
    rng = np.random.default_rng(seed)
    M0 = rand_point(rng); q = rng.normal(size=4); _ = rng.normal(size=4)
    d = leaf_data(M0, q)
    rows = []; ys = {'scal': [], 'vec': [], 'dirac': []}
    r2 = np.random.default_rng(100 + seed)
    for t in range(8):
        al = r2.normal(size=4)
        for key in ys:
            v, cd = c16(d, th, al, key)
            ys[key].append(v)
        rows.append(F12(cd))
    X = np.array(rows)
    print('seed', seed, 'th', th, 'a,b', cd['a'], cd['b'], 'c0', cd['c0'])
    for key in ys:
        y_ = np.array(ys[key])
        coef, res, rk, sv = np.linalg.lstsq(X, y_, rcond=None)
        print('%-5s: fit c*16pi^2 = g1 F1 + g2 F2 : g1 = %s  g2 = %s   residual %.2e (relative)' % (key, np.round(coef[0], 6), np.round(coef[1], 6), np.linalg.norm(X @ coef - y_) / np.linalg.norm(y_)))
    print('expected scalar: g1 = 1/24 = %.6f, g2 = -2/24 = %.6f' % (1 / 24, -2 / 24))
