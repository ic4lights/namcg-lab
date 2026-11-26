"""030 script 2: validation of the weight-2 resolvent symbol of nlo_symbol.build against the textbook one-dimensional heat-kernel coefficient and the 2D Maxwell coefficient.
Test: eta=(1,1), kappa=(1,0), alpha=(0,1), omega_1 = P, omega'_2 = -f sin(phi):  H = P^2 + V(phi), V = f^2 sin^2 phi  (Euclidean, one dimension after integrating nothing else).
Heat kernel (1D): Tr e^{-tH} = (4 pi t)^{-1/2} int [ ... - t^3 V'^2/12 + ... ] up to total derivatives, so with Tr (H-z)^{-1} = int_0^inf dt e^{tz} Tr e^{-tH}
the weight-2 part of  int dphi int dP/(2 pi) r_2  must equal  -(1/12) (4 pi)^{-1/2} Gamma(7/2) int dphi V'^2 (V-z)^{-7/2}   (the e^{-tV}-dressed form  e^{-tV}[-t^2 V''/6 + t^3 V'^2/12] ).
Second test: 2D Euclidean U(1): add the transverse momentum w2 = omega~_2 - f sin(phi), int d omega~_2/(2 pi): weight-2 part must equal (4 pi)^{-1} Gamma(2)... -(1/12) F_ab F^ab with F_12 = f cos(phi) (a_2 = -(1/12) F_ab F^ab)."""
import sympy as sp, numpy as np
from scipy.integrate import quad, dblquad
from math import gamma, pi
from nlo_symbol import build
B = build([1, 1])
w1, w2 = B['w']; zeta, S, C, eps, Ui = B['zeta'], B['S'], B['C'], B['eps'], B['Ui']
al1, al2 = B['al']; ka1, ka2 = B['ka']
r2 = B['r2'].subs({ka1: 1, ka2: 0, al1: 0, al2: 1, zeta: 1})
z = -1.0
r2f = sp.lambdify((w1, w2, S, C, eps, Ui), r2, 'numpy')
f = 0.7
def inner(phi):
    s_, c_ = np.sin(phi), np.cos(phi)
    g = lambda P: np.real(r2f(P, -f * s_, s_, c_, f, 1 / (P ** 2 + f ** 2 * s_ ** 2 - z)))
    return quad(g, -np.inf, np.inf, epsabs=1e-13, epsrel=1e-13)[0] / (2 * pi)
lhs = quad(inner, 0, 2 * pi, epsabs=1e-13, epsrel=1e-13)[0]
rhs = -1.0 / 12 * (4 * pi) ** -0.5 * gamma(3.5) * quad(lambda p: (2 * f ** 2 * np.sin(p) * np.cos(p)) ** 2 * (f ** 2 * np.sin(p) ** 2 - z) ** -3.5, 0, 2 * pi, epsabs=1e-13, epsrel=1e-13)[0]
print("1D test: lhs = %.12e  rhs = %.12e  ratio = %.12f" % (lhs, rhs, lhs / rhs))
def inner2(phi):
    s_, c_ = np.sin(phi), np.cos(phi)
    def gP(P, om):
        w2v = om - f * s_
        return np.real(r2f(P, w2v, s_, c_, f, 1 / (P ** 2 + w2v ** 2 - z)))
    val = dblquad(lambda P, om: gP(P, om), -np.inf, np.inf, -np.inf, np.inf, epsabs=1e-12, epsrel=1e-12)[0]
    return val / (2 * pi) ** 2
lhs2 = quad(inner2, 0, 2 * pi, epsabs=1e-11, epsrel=1e-11)[0]
rhs2 = -1.0 / 12 * (4 * pi) ** -1 * gamma(2) * (-z) ** -2 * 2 * f ** 2 * pi
print("2D Maxwell test: lhs = %.12e  rhs = %.12e  ratio = %.12f" % (lhs2, rhs2, lhs2 / rhs2))
