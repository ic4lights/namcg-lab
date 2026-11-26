# s1_wick_pushforward_D2.py -- proposal 103, edge G.moments-nonproduct-measures.
# Checks for the coherence-induced non-product slot law at D=2:
#  (A) Bessel ray integral  int_0^oo tau e^{-b tau} I_0(c tau) dtau = b/(b^2-c^2)^{3/2}
#      (30-digit mpmath quadrature at several (b,c) pairs, b>c>0);
#  (B) closed form f(p) = det*b/(b^2-c^2)^{3/2}, b = g2 p + g1 (1-p), c = 2|rho| sqrt(p(1-p))
#      with g_i = sigma_i^2: rho=0 reduction to the 089 product density g1*g2/(g2 p + g1(1-p))^2
#      (30-digit grid check), exact normalization, equal-variance symbolic form
#      (1-r^2)/(1-4 r^2 p(1-p))^{3/2}, f(1/2)=1/sqrt(1-r^2);
#  (C) complex-Wick contingency-table moments E[prod |w_i|^{2 alpha_i}] at D=2 and D=3 vs Monte Carlo;
#  (D) Monte Carlo of the profile pushforward p_1 = E_1/(E_1+E_2), fixed seed 1031, against the
#      closed form (bins), phase-blindness in arg(rho), and Laplace-transform identity
#      E exp(-t.E) = det(I+T Sigma)^{-1} at D=3.
# Run from repo root: python -I proposals/103-g-moments-nonproduct-measures/s1_wick_pushforward_D2.py
import itertools

import mpmath
import numpy as np
import sympy as sp

mpmath.mp.dps = 30

print("=== (A) Bessel ray integral, 30-digit quadrature ===")
for (bv, cv) in [(3.0, 1.0), (5.0, 4.9), (2.5, 0.0)]:
    lhs = mpmath.quad(lambda t: t * mpmath.exp(-bv * t) * mpmath.besseli(0, cv * t), [0, mpmath.inf])
    rhs = bv / (bv**2 - cv**2) ** mpmath.mpf("1.5")
    print("b=%g c=%g: lhs %s rhs %s reldiff %.2e" % (bv, cv, mpmath.nstr(lhs, 20), mpmath.nstr(rhs, 20), abs(lhs - rhs) / rhs))

print()
print("=== (B) closed-form density checks ===")
p, r, g1, g2, rr = sp.symbols("p r g1 g2 rhoabs", positive=True)
det = g1 * g2 - rr**2
bb = g2 * p + g1 * (1 - p)
cc = 2 * rr * sp.sqrt(p * (1 - p))
f = sp.simplify(det * bb / (bb**2 - cc**2) ** sp.Rational(3, 2))
f0 = g1 * g2 / (g2 * p + g1 * (1 - p)) ** 2
print("rho=0 reduction: max over 41-point p-grid of |f-f0| at (g1,g2)=(3,7), 30-digit:", end=" ")
ff = sp.lambdify(p, (f - f0).subs({g1: 3, g2: 7, rr: 0}), "mpmath")
print(max(abs(ff(mpmath.mpf(k) / 40)) for k in range(1, 40)))
num = {g1: 1, g2: 2, rr: sp.Rational(1, 2)}
val = mpmath.quad(lambda x: sp.lambdify(p, f.subs(num), "mpmath")(x), [0, "0.5", 1.0])
print("normalization int_0^1 f dp at (g1,g2,|rho|)=(1,2,1/2):", mpmath.nstr(val, 25))
num2 = {g1: 1, g2: 1, rr: sp.Rational(7, 10)}
val2 = mpmath.quad(lambda x: sp.lambdify(p, f.subs(num2), "mpmath")(x), [0, "0.5", 1.0])
print("normalization at (1,1,7/10):", mpmath.nstr(val2, 25))
feq = sp.simplify(f.subs({g1: 1, g2: 1, rr: r}))
feq_target = (1 - r**2) / (1 - 4 * r**2 * p * (1 - p)) ** sp.Rational(3, 2)
print("equal-variance form (1-r^2)/(1-4r^2 p(1-p))^{3/2} exact:", sp.simplify(feq - feq_target) == 0)
print("f(1/2) at equal variance == 1/sqrt(1-r^2):", sp.simplify(feq.subs(p, sp.Rational(1, 2)) - 1 / sp.sqrt(1 - r**2)) == 0)
print("f(0) at equal variance:", sp.simplify(feq.subs(p, 0)), " f(1):", sp.simplify(feq.subs(p, 1)))

print()
print("=== (C) complex-Wick contingency-table moments ===")

def tables(rs, cs):
    """Tables of nonneg ints with row sums rs and column sums cs."""
    if not rs:
        yield []
        return
    for row in itertools.product(range(rs[0] + 1), repeat=len(cs)):
        if sum(row) != rs[0] or any(row[j] > cs[j] for j in range(len(cs))):
            continue
        for rest in tables(rs[1:], [cs[j] - row[j] for j in range(len(cs))]):
            yield [list(row)] + rest

def wick_moment(alpha, Sig):
    D = len(alpha)
    fact = 1
    for a in alpha:
        fact *= sp.factorial(a)
    tot = sp.Integer(0)
    for M in tables(list(alpha), list(alpha)):
        term = sp.Integer(1)
        den = sp.Integer(1)
        for i in range(D):
            for j in range(D):
                m = M[i][j]
                if m:
                    term *= Sig[i, j] ** m
                    den *= sp.factorial(m)
        tot += term * fact * fact / den
    return sp.simplify(tot)

rng = np.random.default_rng(1031)
n = 400_000

def sample_w(Sig_np, n, rng):
    L = np.linalg.cholesky(Sig_np)
    z = rng.standard_normal((n, Sig_np.shape[0])) + 1j * rng.standard_normal((n, Sig_np.shape[0]))
    # rows of z are iid CN(0,2I) as coded; divide by sqrt(2) so that E[w w^H] = Sigma
    return (z @ L.T) / np.sqrt(2.0)

s1x, s2x, rho = sp.symbols("sigma1 sigma2 rho", positive=True)
Sig2 = sp.Matrix([[s1x, rho], [rho, s2x]])
m11 = wick_moment([1, 1], Sig2)
m21 = wick_moment([2, 1], Sig2)
m22 = wick_moment([2, 2], Sig2)
print("E[E1 E2]      =", m11)
print("E[E1^2 E2]    =", m21)
print("E[E1^2 E2^2]  =", m22)
subs = {s1x: 1, s2x: 2, rho: sp.Rational(6, 10) * sp.sqrt(2)}
vals = [float(m.subs(subs)) for m in (m11, m21, m22)]
Sig_np = np.array([[1.0, 0.6 * np.sqrt(2.0)], [0.6 * np.sqrt(2.0), 2.0]])
W = sample_w(Sig_np, n, rng)
E = np.abs(W) ** 2
mc = [np.mean(E[:, 0] * E[:, 1]), np.mean(E[:, 0] ** 2 * E[:, 1]), np.mean(E[:, 0] ** 2 * E[:, 1] ** 2)]
for name, ex, mn in zip(["E[E1 E2]", "E[E1^2 E2]", "E[E1^2 E2^2]"], vals, mc):
    print("%s exact %.10g MC %.10g reldev %.2e" % (name, ex, mn, abs(ex - mn) / abs(ex)))

a = np.array([[1.0, 0.3 + 0.2j, 0.1], [0.3 - 0.2j, 1.5, 0.4 - 0.1j], [0.1, 0.4 + 0.1j, 0.8]])
S3 = sp.Matrix([[sp.nsimplify(x) for x in row] for row in a])
m3 = wick_moment([1, 1, 1], S3)
print("E[E1 E2 E3] at D=3 (exact data) =", sp.simplify(m3))
W3 = sample_w(a, n, rng)
E3 = np.abs(W3) ** 2
mcm = np.mean(E3[:, 0] * E3[:, 1] * E3[:, 2])
exm = complex(m3)
print("exact %.10g MC %.10g reldev %.2e" % (exm.real, mcm, abs(exm.real - mcm) / abs(exm.real)))

print()
print("=== (D) Monte Carlo pushforward vs closed form, phase-blindness, Laplace identity ===")

def pushforward_hist(Sig_np, n, bins=200):
    W = sample_w(Sig_np, n, rng)
    E = np.abs(W) ** 2
    p1 = E[:, 0] / E.sum(axis=1)
    h, edges = np.histogram(p1, bins=bins, range=(0, 1), density=True)
    return h, edges[:-1] + (edges[1] - edges[0]) / 2

fml = sp.lambdify(p, f.subs({g1: 1, g2: 2, rr: sp.Rational(1, 2)}), "numpy")
for phase, tag in [(0.0, "rho real"), (np.pi / 3, "rho e^{i pi/3}"), (np.pi * 0.37, "rho e^{i 0.37 pi}")]:
    mag = 0.5
    Sig = np.array([[1.0, mag * np.exp(1j * phase)], [mag * np.exp(-1j * phase), 2.0]])
    h, mid = pushforward_hist(Sig, n)
    exact = fml(mid)
    good = mid > 0.05
    rel = np.max(np.abs(h[good] - exact[good]) / exact[good])
    print("binwise max rel dev (%s), central 90%% bins: %.4f" % (tag, rel))

fml_eq = sp.lambdify(p, feq_target.subs(r, sp.Rational(7, 10)), "numpy")
Sig_eq = np.array([[1.0, 0.7], [0.7, 1.0]])
h, mid = pushforward_hist(Sig_eq, n)
good = mid > 0.05
print("equal-variance r=0.7 binwise max rel dev, central 90%% bins: %.4f"
      % np.max(np.abs(h[good] - fml_eq(mid)[good]) / fml_eq(mid)[good]))
Weq = np.abs(sample_w(Sig_eq, 200_000, rng)) ** 2
peq = Weq[:, 0] / Weq.sum(1)
print("MC E[p1] r=0.7 (expect 1/2): %.5f ; MC E[s2] r=0.7: %.5f"
      % (peq.mean(), np.mean(peq**2 + (1 - peq) ** 2)))
Wfl = np.abs(sample_w(np.eye(2), 200_000, rng)) ** 2
pfl = Wfl[:, 0] / Wfl.sum(1)
print("MC E[s2] r=0 equal var (expect 2/3 = 2/(D+1) of the flat-Dirichlet statistics paragraph): %.5f" % np.mean(pfl**2 + (1 - pfl) ** 2))

t = np.array([0.3, 0.7, 1.3])
W3 = sample_w(a, n, rng)
E3 = np.abs(W3) ** 2
lhs = np.mean(np.exp(-(E3 * t).sum(1)))
rhs = np.real_if_close(np.linalg.det(np.eye(3) + np.diag(t) @ a)).real
print("Laplace E exp(-t.E) MC %.8f det(I+T Sig)^{-1} %.8f reldev %.2e"
      % (lhs, 1 / rhs, abs(lhs - 1 / rhs) * rhs))
print("S1 DONE")
