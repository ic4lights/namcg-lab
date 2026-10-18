"""030 script 7: identification of the s^0 tail c0 with the Maxwell (a_2) term of the charged scalar H = eta^{ab} Pi_a Pi_b with the induced gauge field a_b = eps zeta alpha_b sin(kappa.x):
prediction  K_Max(s) = (4 pi)^-3 det(B)^(-1/2) * i * (s^2/12) * G * E_s[zeta^2],  G = (kappa.kappa)(alpha.alpha) - (kappa.alpha)^2  (eta contractions),  E_s[zeta^2] = Gaussian average at proper time s.
Compared with the exact K(s) of nlo_scan at s = 1e5, and with the gauge test alpha -> kappa (G = 0)."""
import sys, numpy as np, mpmath as mp
sys.dont_write_bytecode = True
from gauss_tools import *
mp.mp.dps = 60
terms = load_terms(name='r2', k=2)
rng = np.random.default_rng(11)
def Gram(alpha, kappa):
    return (kappa * eta_a) @ kappa * ((alpha * eta_a) @ alpha) - ((alpha * eta_a) @ kappa) ** 2
for trial in range(6):
    z = rand_z_pos(rng, rng.uniform(0.6, 3)); M0 = Mfun(z)
    q = rng.normal(size=4); alpha = rng.normal(size=4)
    dat = frozen_data(M0, q)
    s_ = mp.mpf(10) ** 5
    K, g = integrand(terms, dat, alpha, s_)
    Gm = Gram(alpha, dat['kappa'])
    pred = (4 * mp.pi) ** -3 / g.sqrtdet * 1j * s_ ** 2 / 12 * Gm * g.C[4, 4]
    Kg, gg = integrand(terms, dat, dat['kappa'], s_)
    print("trial %d: K(1e5) = %s ; Maxwell prediction = %s ; ratio = %s ; G = %.4f ; K(alpha=kappa)/K(alpha) = %s" % (trial, mp.nstr(K, 8), mp.nstr(pred, 8), mp.nstr(K / pred, 8), Gm, mp.nstr(Kg / K, 5)))
