"""049 r2 s7: the first term of the factorisation in the potential of chi, fibre-constant frozen symbol. Prints only.

Own check of F1 of review-r1; closed forms are used instead of quadrature on the loop-mode sums.
Density in units a = F sqrt|g| / 32 pi^2, at equal weights:
  L(chi) = - int ds s^-3 { s0K(s) w(xi) + (vK-tauK)(s) (1 + s a1) - (1/4) sig(xi) tauK(s) },
  xi = s th / 2, a1 = 2 - 3 th/4,
  w(xi)   = <tr_V e^{-sZ}> - 2 <tr_D e^{-sZ}> + 4,   sig(xi) = <tr_D e^{-sZ}> - 4,
with the merged closed forms <tr_D> = 4(1-xi)e^{-xi/2}, <tr_V> = 2+2(1-4xi)e^{-2xi}.

(A) w and sig from the Gaussian boost; series.
(B) Y per K-mode: closed form against quadrature; limit (15/2) th^2.
(C) d/dln chi of the mixed term: closed form, against 2U_2; the large-N law -4x^2-6x+15/2 on S^2_N at 60 digits.
(D) exponent forms with Y (symbolic), with dY/dln chi retained then neglected.
(E) x0, the 10/13 bound, x >= 5/2, beta < -1.
(F) the counterexample at x = 3/10 in exact rationals; independent root solve; finite N.
(G) Tbar^{ab mu} y_mu = 0, so a perturbation along y y leaves the Gaussian average unchanged.
"""
import fractions as fr
import os
import sys

import mpmath as mp
import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
mp.mp.dps = 60

print("(A) Gaussian boost: three-vector b with variance xi per component, D eigenvalues exp(+-i|b|), V eigenvalues exp(+-2i|b|),1,1")
xi, c, r = sp.symbols("xi c r", positive=True)
mom = sp.integrate(sp.cos(c * r) * r ** 2 * sp.exp(-r ** 2 / (2 * xi)), (r, 0, sp.oo)) / sp.integrate(r ** 2 * sp.exp(-r ** 2 / (2 * xi)), (r, 0, sp.oo))
print("    <cos(c|b|)> - (1-c^2 xi) exp(-c^2 xi/2) =", sp.simplify(mom - (1 - c ** 2 * xi) * sp.exp(-c ** 2 * xi / 2)))
trD = 4 * (1 - xi) * sp.exp(-xi / 2)
trV = 2 + 2 * (1 - 4 * xi) * sp.exp(-2 * xi)
w = trV - 2 * trD + 4
sig = trD - 4
print("    w   =", sp.series(w, xi, 0, 5).removeO())
print("    sig =", sp.series(sig, xi, 0, 4).removeO())
print("    w = <(2cos|b| - 2)^2> >= 0:", sp.simplify(w - (4 * (mom.subs(c, 2) * 0 + (1 - 4 * xi) * sp.exp(-2 * xi)) / 2 + 2 - 8 * (1 - xi) * sp.exp(-xi / 2) + 4)) == 0)


def Ia(a, th):
    """I(a) = int ds s^-2 e^{-sa} w(s th/2) in closed form: Sum c p ln p - Sum d ln p."""
    def xl(p):
        return p * mp.log(p) if p > 0 else mp.mpf(0)
    def lg(p):
        return mp.log(p)
    return 6 * xl(a) + 2 * xl(a + th) - 8 * xl(a + th / 4) + 4 * th * lg(a + th) - 4 * th * lg(a + th / 4)


def wnum(x):
    if x < mp.mpf("1e-4"):
        return 15 * x ** 2 - mp.mpf(35) / 2 * x ** 3 + mp.mpf(189) / 16 * x ** 4
    return 6 + 2 * (1 - 4 * x) * mp.exp(-2 * x) - 8 * (1 - x) * mp.exp(-x / 2)


def Y_mode(a, th):
    return 2 * a * Ia(a, th) if a > 0 else mp.mpf(0)


print("(B) Y per K-mode: 2 a I(a)")
for a_, th_ in ((mp.mpf(3), mp.mpf(1)), (mp.mpf("0.05"), mp.mpf(1)), (mp.mpf(40), mp.mpf(2))):
    q = mp.quad(lambda s: mp.exp(-s * a_) * wnum(s * th_ / 2) / s ** 2, [0, mp.mpf("1e-3"), 1, 10, 100, mp.inf])
    print("    a=%s th=%s closed %s quad %s" % (a_, th_, mp.nstr(Ia(a_, th_), 15), mp.nstr(q, 15)))
aa, tt = sp.symbols("a th", positive=True)
Ib = 6 * aa * sp.log(aa) + 2 * (aa + tt) * sp.log(aa + tt) - 8 * (aa + tt / 4) * sp.log(aa + tt / 4) + 4 * tt * sp.log(aa + tt) - 4 * tt * sp.log(aa + tt / 4)
eps = sp.Symbol("e", positive=True)
ser = sp.series(sp.expand_log((2 * aa * Ib).subs(aa, 1 / eps), force=True), eps, 0, 2).removeO()
print("    large a: 2 a I(a) =", sp.simplify(ser), " (leading 15 th^2/2, next -35 th^3 /(8 a) in this expansion)")


def s2_lists(l):
    L = mp.mpf(l)
    tc = [(4 * (2 * L + 2), L * L), (4 * 2 * L, (L + 1) ** 2), (-8 * (2 * L + 1), L * (L + 1))]
    if l == 0:
        vc = [(mp.mpf(3), mp.mpf(0)), (mp.mpf(-3), mp.mpf(0))]
    else:
        vc = [(2 * L + 3, L * (L - 1)), (2 * L + 1, L * (L + 1) + 2), (2 * L - 1, (L + 1) * (L + 2)), (-3 * (2 * L + 1), L * (L + 1))]
    return tc, vc


def plog(c_, b, p):
    return c_ * b ** p * mp.log(b) if b > 0 else mp.mpf(0)


def hats(N):
    V = T = U = mp.mpf(0)
    for l in range(N):
        tc, vc = s2_lists(l)
        T += sum(plog(c_, b, 1) for c_, b in tc)
        V += sum(plog(c_, b, 1) for c_, b in vc)
        U += -(sum(plog(c_, b, 2) for c_, b in vc) - sum(plog(c_, b, 2) for c_, b in tc)) / 2
    return V, T, U


def Jm(b, th):
    return 4 * (b + th / 4) * mp.log(b + th / 4) - 4 * b * mp.log(b) + 2 * th * mp.log(b + th / 4)


def parts(N, chi2, th):
    """d/dln chi in units a: Y, mixed (full frozen), 4U4, and the a1 part of (vK-tauK)."""
    Y = M = mp.mpf(0)
    for l in range(N):
        Y += (2 * l + 1) * Y_mode(l * (l + 1) * chi2, th)
        tc, _ = s2_lists(l)
        for c_, b in tc:
            if b > 0:
                M += -c_ * (b * chi2) * Jm(b * chi2, th) / 2
    V, T, U = hats(N)
    return Y, M, -4 * U * chi2 ** 2, -2 * (V - T) * chi2 * (2 - 3 * th / 4), V, T, U


print("(C) on S^2_N. First a check of the closed spectra against klib brute force at N=4")
import klib  # noqa: E402

V4, T4, U4, ext = klib.moments(klib.K_sphere(4))
Vc, Tc, Uc = hats(4)
print("    brute V,T,U %.10f %.10f %.10f; closed %s %s %s; min vector %.2e" % (V4, T4, U4, mp.nstr(Vc, 11), mp.nstr(Tc, 11), mp.nstr(Uc, 11), ext["minV"]))
print("    columns: N, x=chi2/th, th | Y/(7.5 th^2 (N^2-1)) | mixed/2U2 | L'/(N^2 th^2) | law -4x^2-6x+7.5 | a1 part/(N^2 th^2)")
for N in (64, 256, 1024, 4096):
    for th in (mp.mpf(1), mp.mpf(2)):
        for x in ("0.1", "0.3", "0.81", "2.5", "10"):
            x_ = mp.mpf(x)
            chi2 = x_ * th
            if N == 4096 and (th != 1 or x not in ("0.3", "2.5")):
                continue
            Y, M, q4, a1p, V, T, U = parts(N, chi2, th)
            u2 = -mp.mpf(3) / 4 * th * T * chi2 * 2
            Lp = Y + M + q4
            print("    %5d %5s %s | %s | %s | %s | %s | %s" % (N, x, mp.nstr(th, 2), mp.nstr(Y / (mp.mpf(15) / 2 * th ** 2 * (N ** 2 - 1)), 8), mp.nstr(M / u2, 8), mp.nstr(Lp / (N ** 2 * th ** 2), 8), mp.nstr(-4 * x_ ** 2 - 6 * x_ + mp.mpf(15) / 2, 8), mp.nstr(a1p / (N ** 2 * th ** 2), 3)))
print("    Y/2|U2| at N=1024 th=1 x=.3 and (5/4)/x:", end=" ")
Y, M, q4, a1p, V, T, U = parts(1024, mp.mpf("0.3"), mp.mpf(1))
print(mp.nstr(Y / (2 * mp.mpf(3) / 4 * T * mp.mpf("0.3")), 6), mp.nstr(mp.mpf(5) / 4 / mp.mpf("0.3"), 6))
print("    d Y/d ln chi over Y at th=1, x=.3:", end=" ")
for N in (64, 256, 1024):
    d = mp.mpf("1e-12")
    Y1 = parts(N, mp.mpf("0.3") * mp.exp(2 * d), mp.mpf(1))[0]
    Y0 = parts(N, mp.mpf("0.3") * mp.exp(-2 * d), mp.mpf(1))[0]
    print("N=%d: %s" % (N, mp.nstr((Y1 - Y0) / (2 * d) / parts(N, mp.mpf("0.3"), mp.mpf(1))[0], 4)), end="; ")
print()

print("(D) exponent with Y. Write Lp = 4 U4 + 2 U2 + Y, Lpp = 16 U4 + 4 U2 + Yp, U_chichi = Ut'' + Lpp, beta = 2 Lp/U_chichi = -2 Ut'/U_chichi")
U4s, U2s, Ys, Yp, Ut, C3, C2 = sp.symbols("U4 U2 Y Yp Ut C3 C2", real=True)
Lp = 4 * U4s + 2 * U2s + Ys
Lpp = 16 * U4s + 4 * U2s + Yp
for name, Ut1, Ut2, coef in (("quartic alone (coefficient Ut)", 4 * Ut, 16 * Ut, Ut), ("quartic + cubic C3", 4 * Ut + 3 * C3, 16 * Ut + 9 * C3, C3), ("quartic + mass C2", 4 * Ut + 2 * C2, 16 * Ut + 4 * C2, C2)):
    sol = sp.solve(Ut1 + Lp, coef)[0]
    Uxx = (Ut2 + Lpp).subs(coef, sol)
    print("    %s: U_chichi = %s ; 2 Lp/U_chichi at Yp=0 = %s" % (name, sp.factor(sp.expand(Uxx)), sp.factor(sp.simplify(2 * Lp / Uxx.subs(Yp, 0)))))
quart = sp.solve(4 * Ut + Lp, U2s)[0]
e_ = U4s / Ut
print("    quartic alone: beta + 1/(1+eps-Y/4Ut) at Yp=0:", sp.simplify((2 * Lp / (16 * Ut + Lpp)).subs(Yp, 0).subs(U2s, quart) + 1 / (1 + e_ - Ys / (4 * Ut))))
print("    cubic at U4 = Ut - 3 U2/2, Y=Yp=0:", sp.simplify((2 * (4 * U4s + 2 * U2s) / (4 * Ut + 4 * U4s - 2 * U2s)).subs(U4s, Ut - sp.Rational(3, 2) * U2s)))
print("    cubic example Ut=1,U2=-1,U4=5/2,Y=0: beta", sp.Rational(2) * (10 - 2) / (4 + 10 + 2), " C3 =", -(sp.Integer(4) + 10 - 2) / sp.Integer(3), "U_chichi", 4 + 10 + 2)
print("    homogeneous mode, L = L(chi^2/lam): beta_hom = (1/2) Lpp/U_chichi = (8 U4 + 2 U2 + Yp/2)/U_chichi; for Ut=0 it is 1/2 at any Y")

print("(E) large-N law. Units a N^2 th^2, x = chi2/th: U4 = -x^2, 2U2 = -6x, Y = 15/2")
x = sp.Symbol("x", positive=True)
Lpx = -4 * x ** 2 - 6 * x + sp.Rational(15, 2)
print("    positive root x0 =", sp.nsimplify(sp.solve(Lpx, x)[0]), "=", sp.N(sp.solve(Lpx, x)[0], 12), "; (sqrt39-3)/4 =", sp.N((sp.sqrt(39) - 3) / 4, 12))
A, ee = sp.symbols("A e", positive=True)
stat = A * x ** 2 - 6 * x + sp.Rational(15, 2)
print("    tree quartic only: A = 4(1/|eps|-1); discriminant", sp.discriminant(stat, x), "=> A <= 6/5, 1/|eps| <= 13/10, |eps| >=", sp.Rational(10, 13))
print("    U_chichi = 2x d(stat)/dx = 2x(2Ax-6): positive only on the larger root x = (3 + sqrt(9-15A/2))/A; at A=6/5 x =", sp.Rational(3) / sp.Rational(6, 5))
for A_ in (sp.Rational(6, 5), sp.Rational(1), sp.Rational(1, 2), sp.Rational(1, 10)):
    xm = (3 + sp.sqrt(9 - sp.Rational(15, 2) * A_)) / A_
    e1 = 1 / (A_ / 4 + 1)
    Ut1 = 4 * xm ** 2 / e1
    Uxx = 2 * xm * (2 * A_ * xm - 6)
    print("    A=%s |eps|=%s x_min=%s U_chichi=%s beta=%s" % (A_, e1, sp.N(xm, 8), sp.N(Uxx, 8), sp.N(-2 * Ut1 / Uxx, 8)))
print("    A <= 0 (|eps| >= 1): one positive root with 2Ax-6 < 0, a maximum. So a minimum only for 10/13 <= |eps| < 1.")
print("    beta < -1 at the minimum <=> 1/|eps| < 2 + 3/(2x), and 1/|eps| <= 13/10 there.")

print("(F) counterexample at x = 3/10, exact rationals, units a N^2 th^2, chi0^2 = 3 th/10")
F = fr.Fraction
xr = F(3, 10)
Lp_ = -4 * xr * xr - 6 * xr + F(15, 2)
Lpp_ = 2 * xr * (-8 * xr - 6)
Utt = 2 * Lp_ - Lpp_
print("    L' =", float(Lp_), Lp_, " L'' =", float(Lpp_), Lpp_, " required Ut' =", float(-Lp_), " Ut'' =", float(Utt))
Uq = (Utt - 3 * (-Lp_)) / 4
Cc = (-Lp_ - 4 * Uq) / 3
print("    quartic + cubic: quartic", float(Uq), Uq, " cubic", float(Cc), Cc, " |eps| =", float(xr * xr / Uq), " U_chichi =", float(Utt + Lpp_), " beta =", 2 * Lp_ / (Utt + Lpp_))
Um = (Utt - 2 * (-Lp_)) / 8
Cm = (-Lp_ - 4 * Um) / 2
print("    quartic + mass : quartic", float(Um), Um, " mass ", float(Cm), Cm, " |eps| =", float(xr * xr / Um), " U_chichi =", float(Utt + Lpp_), " beta =", 2 * Lp_ / (Utt + Lpp_))


def dlnchi_dphi(Uq_, Cc_, pw, x0, h=mp.mpf("1e-18")):
    """Independent: minimise U(lnchi, phi) = tree(lnchi) + exp(-2 phi) L(lnchi); dln chi/dphi by a symmetric root solve."""
    x0 = mp.mpf(x0.numerator) / x0.denominator
    Uq_ = mp.mpf(Uq_.numerator) / Uq_.denominator
    Cc_ = mp.mpf(Cc_.numerator) / Cc_.denominator
    def g(u, phi):
        xv = x0 * mp.exp(2 * u)
        return 4 * Uq_ * mp.exp(4 * u) + pw * Cc_ * mp.exp(pw * u) + mp.exp(-2 * phi) * (-4 * xv ** 2 - 6 * xv + mp.mpf(15) / 2)
    up = mp.findroot(lambda u: g(u, h), mp.mpf(0))
    um = mp.findroot(lambda u: g(u, -h), mp.mpf(0))
    return (up - um) / (2 * h), g(mp.mpf(0), mp.mpf(0))


print("    independent root solve (u = ln chi - ln chi0): cubic d u/d phi, residual:", [mp.nstr(z, 12) for z in dlnchi_dphi(Uq, Cc, 3, xr)])
print("    independent root solve: mass d u/d phi, residual:", [mp.nstr(z, 12) for z in dlnchi_dphi(Um, Cm, 2, xr)])
print("    finite N, full frozen forms at th=1, x=.3 (units N^2): tree data for beta=1 with L', L'' from exact sums")
for N in (64, 256, 1024):
    d = mp.mpf("1e-10")
    def Lprime(xx):
        Y, M, q4, a1p, V, T, U = parts(N, xx, mp.mpf(1))
        return (Y + M + q4) / N ** 2
    L1 = Lprime(mp.mpf("0.3"))
    L2 = (Lprime(mp.mpf("0.3") * mp.exp(2 * d)) - Lprime(mp.mpf("0.3") * mp.exp(-2 * d))) / (2 * d)
    Ut2 = 2 * L1 - L2
    Uq_ = (Ut2 + 3 * L1) / 4
    Cq_ = (-L1 - 4 * Uq_) / 3
    print("      N=%d L'=%s L''=%s quartic %s cubic %s beta %s" % (N, mp.nstr(L1, 7), mp.nstr(L2, 7), mp.nstr(Uq_, 7), mp.nstr(Cq_, 7), mp.nstr(2 * L1 / (Ut2 + L2), 7)))

print("(G) Tbar^{ab mu} y_mu = eta^{a mu} y_mu y^b - eta^{b mu} y_mu y^a = y^a y^b - y^b y^a")
eta = sp.diag(-1, 1, 1, 1)
ys = sp.Matrix(sp.symbols("y0:4", real=True))
Tb = lambda a, b, mu: eta[a, mu] * ys[b] - eta[b, mu] * ys[a]
ylow = eta * ys
print("    all zero:", all(sp.simplify(sum(Tb(a, b, mu) * ylow[mu] for mu in range(4))) == 0 for a in range(4) for b in range(4)))
print("    Hence delta g_{mu nu} = - g h g with h = lapse y y leaves Tbar^{ab mu} Tbar^{cd nu} g_{mu nu} unchanged, and every moment of Z(k);")
print("    the loop density at fixed Tbar in this channel is sqrt|g| times a function of chi. Fibre-constant modes only.")
