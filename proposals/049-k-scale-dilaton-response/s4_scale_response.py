"""049 s4: response of the K scale to the frame at one loop. Prints only.

Background (units R=1, y^i=0): gamma = m^2 eta, Tbar^{ab mu} = eta^{a mu} y^b - eta^{b mu} y^a, q.y = 0, q.alpha = q.v = 0.
 (A) Tbar . deltaT = 0 at q.y = q.v = 0; Xbar = 6 y^2/m^2 = -6 vartheta; first variation of sqrt|g| X;
 (B) the rank-one determinant, the second-order vacuum term and the fourth moment 1/15;
 (C) stationarity and exponents for each stabiliser, homogeneous mode and static late-time channel;
 (D) the sign statement at random data;
 (E) the finite-q form of the exponent and the contact term.
"""
import numpy as np
import sympy as sp

print("(A) torsion and index density")
eta = sp.diag(-1, 1, 1, 1)
y0, ell, m, k = sp.symbols("y0 ell m k", positive=True)
Y = sp.Matrix([y0, 0, 0, 0])  # upper index, y^i = 0
ylow = eta * Y
a1, a2, a3, v0, v1, v2 = sp.symbols("a0 a1 a2 v0 v1 v2", real=True)
alpha = sp.Matrix([a1, a2, a3, 0])  # q.alpha = 0 for q along 3
v = sp.Matrix([v0, v1, v2, 0])  # q.v = 0
q = sp.Matrix([0, 0, 0, k])  # upper
def Tbar(a, b, mu):
    return eta[a, mu] * Y[b] - eta[b, mu] * Y[a]
def dT(a, b, mu):
    return -m * v[mu] * (q[a] * alpha[b] - q[b] * alpha[a])
low = lambda f: lambda a, b, mu: sum(eta[a, c] * eta[b, d] * eta[mu, e] * f(c, d, e) for c in range(4) for d in range(4) for e in range(4))
Tl = low(Tbar)
contr = sum(Tl(a, b, mu) * dT(a, b, mu) for a in range(4) for b in range(4) for mu in range(4))
print("    Tbar . deltaT at q.y=q.v=0:", sp.simplify(contr))
TT = sp.Matrix(4, 4, lambda mu, nu: sum(eta[a, c] * eta[b, d] * Tbar(a, b, mu) * Tbar(c, d, nu) for a in range(4) for b in range(4) for c in range(4) for d in range(4)))
yy = (Y.T * eta * Y)[0]
print("    Tbar^{ab mu} Tbar_ab^nu - 2 (y^2 eta^{mu nu} - y^mu y^nu):", sp.simplify(TT - 2 * (yy * eta - Y * Y.T)) == sp.zeros(4, 4))
Xbar = sum((eta / m ** 2)[mu, nu] * TT[mu, nu] for mu in range(4) for nu in range(4))
print("    Xbar =", sp.simplify(Xbar), "= 6 y^2/m^2 with y^2 =", yy)
# first variation at fixed Tbar: g_mn = (gamma)^-1, delta g_mn = - g h g, sqrt|g| -> sqrt|g| (1 - t/(2 m^2))
h00, h11, h22, h33 = sp.symbols("h00 h11 h22 h33", real=True)
h = sp.diag(h00, h11, h22, h33)
t = sum(eta[i, i] * h[i, i] for i in range(4))
gamma = m ** 2 * eta + sp.Symbol("e") * h
e = sp.Symbol("e")
g = gamma.inv()
dens = 1 / sp.sqrt(-gamma.det())
Xe = sum(g[i, j] * TT[i, j] for i in range(4) for j in range(4))
F = sp.log(dens * (-Xe))
dF = sp.diff(F, e).subs(e, 0)
yhy = y0 ** 2 * h00
form = -sp.Rational(5, 6) * t / m ** 2 + yhy / (3 * yy * m ** 2)
print("    d ln(sqrt|g| X)/de - [-(5/6) t/m^2 + y.h.y/(3 y^2 m^2)]:", sp.simplify(dF - form))
print("    Omega := m^2 d ln(sqrt|g| X) with h22=h11, h33=0:", sp.simplify((m ** 2 * dF).subs({h22: h11, h33: 0})), "(t = -h00 + 2 h11)")
print("    with h11 = 0 (late-time static channel): Omega/t =", sp.simplify(((m ** 2 * dF) / t).subs({h22: h11, h33: 0}).subs(h11, 0)))
print("    isotropic h = c eta at fixed Tbar: m^2 dF/c =", sp.simplify((m ** 2 * dF).subs({h00: -sp.Symbol('c'), h11: sp.Symbol('c'), h22: sp.Symbol('c'), h33: sp.Symbol('c')}) / sp.Symbol('c')),
      "; with Tbar scaled (X^a -> sqrt(lam) X^a, c = m^2 dlam) the torsion adds +2 m^2 dlam, total -m^2 dlam")

print("(B) rank-one determinant and second-order vacuum term")
x = sp.Symbol("x", real=True)
A4 = sp.Matrix(4, 1, sp.symbols("A0:4"))
V4 = sp.Matrix(4, 1, sp.symbols("W0:4"))
print("    det(1 + A W^T) - (1 + W.A):", sp.simplify((sp.eye(4) + A4 * V4.T).det() - (1 + (V4.T * A4)[0])))
print("    1/(1+x) to second order:", sp.series(1 / (1 + x), x, 0, 3).removeO(), "; e^{-2 phi} with phi = (x - x^2/2)/2 agrees")
rng = np.random.default_rng(49)
n = rng.normal(size=(400000, 3))
n /= np.linalg.norm(n, axis=1, keepdims=True)
c_ = rng.normal(size=(3, 3))
s_ = rng.normal(size=(3, 3))
a_ = n @ c_  # alpha(n), three components as a toy inner product
vv_ = n @ s_
xx = np.sum(a_ * vv_, axis=1)
M = c_ @ s_.T
print("    <x>  MC %.4f, tr/3 %.4f ; <x^2> MC %.4f, (tr(M M)+tr(M M^T)+tr(M)^2)/15 %.4f (structure of the second-order vacuum term)" % (xx.mean(), np.trace(M) / 3, (xx ** 2).mean(), (np.trace(M @ M) + np.trace(M @ M.T) + np.trace(M) ** 2) / 15))

print("(C) exponents")
chi, phi = sp.symbols("chi phi", positive=True)
A4_, A3_, A2_, b4, y2 = sp.symbols("A4 A3 A2 b4 y2", real=True)
def exponent(Ut, w4, w2):
    """beta = dln chi / dphi from U = Ut(chi) + exp(-2 w4 phi) b4 chi^4 + exp(-2 w2 phi) y2 chi^2 at phi = 0."""
    U = Ut + sp.exp(-2 * w4 * phi) * b4 * chi ** 4 + sp.exp(-2 * w2 * phi) * y2 * chi ** 2
    Uc = sp.diff(U, chi)
    return sp.simplify((-sp.diff(Uc, phi) / (chi * sp.diff(Uc, chi))).subs(phi, 0)), sp.simplify(Uc.subs(phi, 0))
for name, w4, w2 in (("homogeneous rescaling (w4,w2)=(1,1/2)", 1, sp.Rational(1, 2)), ("static plane wave, late times (w4,w2)=(1,1)", 1, 1)):
    print("  ", name)
    for lbl, Ut in (("A4 chi^4", A4_ * chi ** 4), ("A3 chi^3", A3_ * chi ** 3), ("A2 chi^2", A2_ * chi ** 2)):
        be, stat = exponent(Ut, w4, w2)
        # eliminate the tree coefficient through stationarity
        coef = [s for s in (A4_, A3_, A2_) if Ut.has(s)][0]
        cs = sp.solve(stat, coef)[0]
        be2 = sp.simplify(be.subs(coef, cs))
        print("     V_t =", lbl, ": beta =", sp.factor(be2))
        print("        y2=0:", sp.simplify(be2.subs(y2, 0)), "; b4=0:", sp.simplify(be2.subs(b4, 0)))

print("  tree mass plus tree quartic, static channel, Y2 and b4 retained")
Ut = A2_ * chi ** 2 + A4_ * chi ** 4
be, stat = exponent(Ut, 1, 1)
cs = sp.solve(stat, A2_)[0]
print("     beta =", sp.factor(sp.simplify(be.subs(A2_, cs))), " with A4 chi^4 = tree quartic, b4 chi^4 = loop quartic, y2 chi^2 = loop quadratic")
Ut3 = A3_ * chi ** 3 + A4_ * chi ** 4
be, stat = exponent(Ut3, 1, 1)
cs = sp.solve(stat, A3_)[0]
print("     tree cubic + quartic: beta =", sp.factor(sp.simplify(be.subs(A3_, cs))))
print("     no tree stabiliser (quartic only): beta(b4, y2):", end=" ")
be, stat = exponent(A4_ * chi ** 4, 1, 1)
cs = sp.solve(stat, A4_)[0]
print(sp.factor(sp.simplify(be.subs(A4_, cs))), "; in terms of eps = b4/A4: -1/(1+eps), check residual",
      sp.simplify((sp.factor(sp.simplify(be.subs(A4_, cs)))) + 1 / (1 + b4 / cs)))

print("(D) sign statement, static channel: beta = 4 (2 B4 + Y2)/U_pp with U_pp the second derivative in ln chi")
cnt = 0
viol = 0
gen = np.random.default_rng(4904)
for _ in range(200000):
    a2, a3, a4 = gen.normal(size=3) * np.array([3, 3, 3])
    B4 = -abs(gen.normal())
    Y2 = -abs(gen.normal())
    # impose stationarity by solving for a2 at unit chi: 2 a2 + 3 a3 + 4 a4 + 4 B4 + 2 Y2 = 0
    a2 = -(3 * a3 + 4 * a4 + 4 * B4 + 2 * Y2) / 2
    Upp = 4 * a2 + 9 * a3 + 16 * a4 + 16 * B4 + 4 * Y2
    if Upp <= 0:
        continue
    cnt += 1
    be = 4 * (2 * B4 + Y2) / Upp
    if be >= 0:
        viol += 1
print("    samples with a local minimum: %d, with beta >= 0: %d" % (cnt, viol))

print("(E) exponent at finite q")
Z, Upp, Upf, J, dphi, p, q2 = sp.symbols("Z Upp Upf J dphi varrho q2", real=True)
S = sp.Rational(1, 2) * (Z * q2 + Upp) * p ** 2 + (Upf * dphi + J) * p
sol = sp.solve(sp.diff(S, p), p)[0]
Sred = sp.simplify(S.subs(p, sol))
print("    reduced:", sp.factor(Sred))
print("    terms: dphi^2:", sp.simplify(sp.diff(Sred, dphi, 2) / 2), " J dphi:", sp.simplify(sp.diff(sp.diff(Sred, dphi), J)), " J^2:", sp.simplify(sp.diff(Sred, J, 2) / 2))
print("    With J = 2 rho0 m^2 and dphi = t/(4 m^2), the term linear in t is (beta(q)/2) rho0 t with beta(q) = -Upf/(Z q2 + Upp)")
