"""040 l1: coefficient of ds/s of the Zeeman-dressed species responses at order eps^2 (small-s limit of s*Theta*k2coef), leaf data.
For each (seed, centre direction, random alpha) prints c_X/c for X = scalar, vector (N sign +1 and -1), Dirac (4 copies, weight +1 here),
with c = A/(16 pi^2) the 034 coefficient (A_engine).  Also the decomposition of the quadratic form in alpha over F1, F2 (see fit_forms)."""
import sys, numpy as np, mpmath as mp
sys.dont_write_bytecode = True
from l3_fin import *          # leaf data, canonical_data, A_engine, Theta
from engine_z import *
mp.mp.dps = 30

def spec(key, a, b, kk, alpha, signN=1):
    al = np.array([mp.mpf(x) for x in alpha], dtype=object)
    if key == 'scal':
        return [scalar_species()]
    if key == 'vec':
        sp = vector_species(a, b, kk, al); sp.N = sp.N * signN; return [sp]
    if key == 'dirac':
        sp = dirac_species(a, b, kk, al); sp.w = mp.mpf(1); sp.N = sp.N * signN; return [sp]

def ratio(d, th, alpha, key, signN=1, rho=mp.mpf('3e-4'), nq=6):
    cd = canonical_data(d, np.array([np.cos(th), np.sin(th)]), alpha)
    a, b = mp.mpf(cd['a']), mp.mpf(cd['b'])
    s = rho / max(a, b) * mp.expj(-mp.mpf('0.6'))
    A = A_engine(cd['alpha'], cd['kappa'], cd['y'])
    c = mp.mpf(A) / (16 * mp.pi ** 2)
    v = k2coef_z(lambda kk: spec(key, a, b, kk, cd['alpha'], signN), a, b, cd['kappa'], cd['alpha'], cd['y'], cd['c0'], s, nquad=nq, lam=mp.mpf('1e-6'))
    return v * Theta(s, a, b) * s / c, cd

if __name__ == "__main__":
    for seed, th in ((12, 0.8), (21, 1.4), (12, 2.0)):
        rng = np.random.default_rng(seed)
        M0 = rand_point(rng); q = rng.normal(size=4); alpha = rng.normal(size=4)
        d = leaf_data(M0, q)
        for key, signN in (('scal', 1), ('vec', 1), ('vec', -1), ('dirac', 1), ('dirac', -1)):
            r, cd = ratio(d, th, alpha, key, signN)
            print('seed %d th %.1f a=%.3f b=%.3f  %-5s signN=%+d  s*T2/c = %s' % (seed, th, cd['a'], cd['b'], key, signN, mp.nstr(r, 8)))
