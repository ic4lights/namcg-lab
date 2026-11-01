"""s6_regulator_deficit.py (proposal 048, round 2). Prints to stdout only; writes nothing.

Finding 8 of review-r1: the regulated static value of I(S1), rho0 = 1, approaches 1/4 as a square root of eps only for
eps >> c0^2, and linearly below that.  This compares 4*(1/4 - I_eps) with the two asymptotic forms of the review:
sqrt(eps) pi/(2 sqrt 2) for eps >> c0^2 and pi eps/(2 c0 theta) for eps << c0^2.  So the review's two forms are read here
as the deficit of 4 I, the value normalised to 1; for I itself each carries a factor 1/4.
I_eps is the quadrature of s4 G (reg_exact, src S1), restated here.
"""
import numpy as np
from scipy import integrate

s2 = 1e4
r = 1 / s2
theta = 1 + r
c0sq = r / theta
c0 = np.sqrt(c0sq)
print("s^2 = %g, c0^2 = %.6g, theta = %.6g" % (s2, c0sq, theta))


def I_eps(eps):
    d = lambda c: r * (1 - c * c) - c * c
    # at rho = 1: X v.X v = (1/4) v.v, regulated by v.v -> v.v + i eps, real part
    return 0.25 * integrate.quad(lambda c: d(c) ** 2 / (d(c) ** 2 + eps ** 2), 0, 1, points=[c0], limit=8000)[0]


print("%10s %12s %14s %14s %14s" % ("eps", "I_eps", "4(1/4-I_eps)", "sqrt form", "linear form"))
for eps in (0.02, 0.002, 0.0002, 0.00002, 0.000002, 0.0000002):
    v = I_eps(eps)
    print("%10g %12.7f %14.7f %14.7f %14.7f" % (eps, v, 4 * (0.25 - v), np.sqrt(eps) * np.pi / (2 * np.sqrt(2)), np.pi * eps / (2 * c0 * theta)))
