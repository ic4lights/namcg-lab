"""030 script 5: consistency of the new machinery with the 028 leading-symbol Hessian.
Compute int ds K0(s) for the eps^2 coefficient of r0 (phase-averaged) along the contour s = t e^{-i theta}, theta = pi/2-0.35, and compare 4*(this) with d^2N/d eps^2 of 028 (mass_moment_hessian.derivs, phase phi = pi/2, same window kappa=3/4, alpha, q)."""
import sys, numpy as np, mpmath as mp
sys.dont_write_bytecode = True
from gauss_tools import *
import importlib.util
spec = importlib.util.spec_from_file_location('mmh', '../028-second-variation/mass_moment_hessian.py')
# avoid writing bytecode into 028: load source manually
src = open('../028-second-variation/mass_moment_hessian.py').read().split('if __name__')[0]
ns = {}
exec(compile(src, 'mmh', 'exec'), ns)
mp.mp.dps = 20
terms0 = load_terms(name='r0', k=2)
rng = np.random.default_rng(3)
theta = np.pi / 2 - 0.35
for trial in range(4):
    z = rand_z_pos(rng, rng.uniform(0.6, 3)); M0 = Mfun(z)
    q = rng.normal(size=4); alpha = rng.normal(size=4)
    dat = frozen_data(M0, q)
    Wd, Yq, Pw, wf = ns['setup'](M0, q)
    n0, d1, d2 = ns['derivs'](Wd, Yq, Pw, alpha)
    ph = mp.mpc(np.cos(theta), -np.sin(theta))
    f = lambda t: integrand(terms0, dat, alpha, t * ph)[0] * ph
    val = mp.quad(f, [0, 1, 10, 100, mp.inf])
    print("trial %d: 4*int K0 = %s ; 028 d2N = %s ; ratio = %s" % (trial, mp.nstr(4 * val, 10), np.round(d2, 8), mp.nstr(4 * val / mp.mpc(d2), 10)))
    # kappa check: W_a(phi) = s m q^a  and Y.dphi = 0
    m = M0[4, 5]
    print("   kappa =", np.round(dat['kappa'], 6), " s*m*q^a =", np.round(-1.0 * m * (np.diag([-1., 1, 1, 1]) @ q), 6), " Y.dphi =", float(dat['Y'] @ dat['dphi']))
