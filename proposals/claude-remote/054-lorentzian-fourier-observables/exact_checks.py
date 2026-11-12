#!/usr/bin/env python3
"""Exact (sympy) and sampled checks of the elementary identities used in proposal 054.  Prints to stdout
(saved as exact_checks.txt).  Writes nothing else."""
import sympy as sp, numpy as np

x, k, k0, l, lam, a, u, K, r, y, t = sp.symbols('x kappa kappa0 ell lambda alpha u K r y t', real=True)

print("(1) Gaussian smearing: int exp(-(k-k0)^2/l^2) e^{i k x} dk = sqrt(pi) l exp(i k0 x - l^2 x^2/4)")
lp = sp.symbols('ellp', positive=True)
lhs = sp.integrate(sp.exp(-(k-k0)**2/lp**2)*sp.exp(sp.I*k*x), (k, -sp.oo, sp.oo))
rhs = sp.sqrt(sp.pi)*lp*sp.exp(sp.I*k0*x-lp**2*x**2/4)
print("    difference simplifies to:", sp.simplify(sp.expand(lhs-rhs)))

print("(2) On R_u, A_0 = e^{-i alpha} At_0 with eigenvalue lam of At_0 real: log|exp(i k0 A_0 - l^2 A_0^2/4)| =")
expo = sp.re(sp.I*k0*sp.exp(-sp.I*a)*lam-lp**2*sp.exp(-2*sp.I*a)*lam**2/4)
expo = sp.simplify(sp.expand_complex(expo))
print("   ", expo)
lstar = sp.solve(sp.diff(expo, lam), lam)[0]
print("    maximum over lam:", sp.simplify(expo.subs(lam, lstar)), " (= k0^2 sin^2 a/(l^2 cos 2a) for cos 2a > 0)")
print("    check:", sp.simplify(expo.subs(lam, lstar)-k0**2*sp.sin(a)**2/(lp**2*sp.cos(2*a))))

print("(3) Unitarity on R_u: kappa A_0 = K At_0 for kappa = K e^{3 pi i u/8}; kappa A_j = K At_j for kappa = K e^{-pi i u/8}")
print("   ", sp.simplify(K*sp.exp(3*sp.pi*sp.I*u/8)*sp.exp(-3*sp.pi*sp.I*u/8)), sp.simplify(K*sp.exp(-sp.pi*sp.I*u/8)*sp.exp(sp.pi*sp.I*u/8)))

print("(4) Arguments of F_E: timelike t = (kappa e^{-3 pi i/8})^2, kappa = K e^{3 pi i u/8}: arg t = 3 pi (u-1)/4;")
print("    spacelike t = (kappa e^{i pi/8})^2, kappa = K e^{-pi i u/8}: arg t = pi (1-u)/4.")
print("    u -> 0+: timelike arg t -> -3 pi/4, spacelike arg t -> pi/4; u = 1: both 0; u in (0,2): timelike |arg t| < 3 pi/4.")
for uu in (sp.Rational(0), sp.Rational(1), sp.Rational(2)):
    print(f"    u={uu}: timelike {3*sp.pi*(uu-1)/4}, spacelike {sp.pi*(1-uu)/4}")
print("    k.k = -kappa^2 (timelike, k^0 = kappa) and e^{i pi/4} k.k with k.k = |kappa|^2 e^{i(2 arg kappa - pi)}:")
ak = sp.symbols('argk', real=True)
print("    arg(e^{i pi/4} k.k) = ", sp.simplify(sp.pi/4+2*ak-sp.pi), " = arg t of the timelike case:", sp.simplify((sp.pi/4+2*ak-sp.pi)-(2*ak-3*sp.pi/4)) == 0)

print("(5) |2 cos(z r/2)| >= 2|sinh(Im z r/2)|:  |cos(p+iq)|^2 - sinh(q)^2 =",
      sp.simplify(sp.expand_complex(sp.Abs(sp.cos(x+sp.I*y))**2-sp.sinh(y)**2).rewrite(sp.exp)))

print("(6) Scaling of the dominating integral: At -> c^{-1/4} At in int d^30 At det(Gt)^4 exp(-c S_E): exponent")
print("    (30 + 24)/4 =", sp.Rational(30+24, 4), "; for SU(N): (10 + 8)(N^2-1)/4 =", sp.factor(sp.Rational(18, 4)*(sp.Symbol('N')**2-1)))

print("(7) Re i S_b on (alpha, beta) contours at N=2 in terms of Euclidean pieces:")
e2W, P = sp.symbols('e2W Pquad', positive=True)
be = sp.symbols('beta', real=True)
ReiS = sp.re(sp.I*lam*(sp.exp(4*sp.I*be)*e2W-sp.exp(2*sp.I*(be-a))*P))
print("   ", sp.simplify(sp.expand_complex(ReiS)), " ; on R_u (a=3 pi u/8, beta=pi u/8):",
      sp.simplify(sp.expand_complex(ReiS.subs({a: 3*sp.pi*u/8, be: sp.pi*u/8}))))

print("(8) Sampled Cauchy-Binet bound |det(G(u))| <= det(Gt), G(u) = e^{2 i beta} Bt^T Bt - e^{-2 i alpha} at at^T, u in (0,2)")
rng = np.random.default_rng(54)
worst = 0
for _ in range(20000):
    at = rng.normal(size=3)*rng.exponential(); Bt = rng.normal(size=(9, 3))*rng.exponential(size=(1, 3))
    uu = rng.uniform(0, 2); al, bb = 3*np.pi*uu/8, np.pi*uu/8
    Gu = np.exp(2j*bb)*Bt.T@Bt-np.exp(-2j*al)*np.outer(at, at)
    Gt = Bt.T@Bt+np.outer(at, at)
    worst = max(worst, abs(np.linalg.det(Gu))/np.linalg.det(Gt))
print("    max ratio over 20000 samples:", worst)

print("(9) Evenness at N=2: G = W - a a^T and a^T (tr W - W) a are even in a; with A_j a row of B, W = sum_i b_i b_i^T is even in b_j.")
