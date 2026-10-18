"""030 script 6: large-proper-time behaviour of the weight-2 (NLO) integrand K(s) at order eps^2 (phase-averaged), real proper time s, Gaussian window of Delta_{3/4}.
Reports K(s) at s = 1e1 ... 1e5 and the successive estimates of c0 = lim K(s), c1 = lim s (K(s)-c0).
Also K at small s (s <= 1) to show that the integrand is finite at small s."""
import sys, numpy as np, mpmath as mp
sys.dont_write_bytecode = True
from gauss_tools import *
mp.mp.dps = 60
terms = load_terms(name='r2', k=2)
rng = np.random.default_rng(11)
svals = [mp.mpf(10) ** k for k in (-1, 0, 1, 2, 3, 4, 5)]
for trial in range(3):
    z = rand_z_pos(rng, rng.uniform(0.6, 3)); M0 = Mfun(z)
    q = rng.normal(size=4); alpha = rng.normal(size=4)
    dat = frozen_data(M0, q)
    print("trial %d: alpha=%s kappa=%s" % (trial, np.round(alpha, 4), np.round(dat['kappa'], 4)))
    Ks = []
    for s_ in svals:
        K, g = integrand(terms, dat, alpha, s_)
        Ks.append(K)
        print("   s=%8.1e  K(s)=%s" % (float(s_), mp.nstr(K, 10)))
    # Richardson-type estimates
    K4, K5 = Ks[-2], Ks[-1]; s4, s5 = svals[-2], svals[-1]
    c1 = (K4 - K5) / (1 / s5 - 1 / s4) * (-1) if False else (K5 - K4) / (1 / s5 - 1 / s4)
    c0 = K5 - c1 / s5
    print("   fit K = c0 + c1/s on s=1e4,1e5:  c0 = %s   c1 = %s" % (mp.nstr(c0, 10), mp.nstr(c1, 10)))
