"""
Cone (replica) heat-kernel checks for proposal 015.

Part 1  Mellin/zeta regularisation: sum_m (1/2) int_0^inf e^{-t} I_{nu_m}(t) dt = -(1/2) sum_m nu_m  (regularised),
        reproduces Tr K_n - n Tr K_1 = (1/12)(1/n - n) for the flat 2D cone of angle 2 pi n.
Part 2  Entropy and induced Newton constant with one proper-time cutoff s_min = eps^2 (common regulator):
        S = A/(48 pi eps^2) per real component, 1/G_ind = 1/(12 pi eps^2), S = A/(4 G_ind);
        contact term for E = xi R: Delta S = -xi A/(8 pi eps^2) = -2 pi xi A <phi^2>, <phi^2> = 1/(16 pi^2 eps^2).
Part 3  Direct numerical test (no regularisation): D(n;T) = sum_m (1/2) int_0^T e^{-t} I_{nu_m}(t) dt - n * (n=1 value)
        for (I) pull-back replica [nu_m = |m|/n]  and
            (II) cone carried by the Poisson structure  [scalar: nu_m = sqrt(m^2+eps^2)/n, m=0 index -alpha/2;
                 connection component a^+ in the block class: nu_m = sqrt((m+a)^2 - 3 a^2/4)/n, m=0 index -a/(2n)].
        First-order coefficient F'(1) = dD/dn at n=1.
Part 4  Local Seeley-DeWitt check of (II): a_1 with the delta functions of R_G and of E.
"""
import numpy as np
import mpmath as mp
import sympy as sp
from scipy import integrate, special

# ---------------- Part 1 ----------------
print("PART 1: Mellin transform  int_0^inf e^{-t} I_nu(t) t^{mu-1} dt = Gamma(mu+nu)Gamma(1/2-mu)/(2^mu sqrt(pi) Gamma(1+nu-mu))")
mu_, nu_ = -0.2, 0.7
num = mp.quad(lambda t: mp.e ** (-t) * mp.besseli(nu_, t) * t ** (mu_ - 1), [0, 1, 10, 100, 1000, 10**5, mp.inf])
ana = mp.gamma(mu_ + nu_) * mp.gamma(0.5 - mu_) / (2 ** mu_ * mp.sqrt(mp.pi) * mp.gamma(1 + nu_ - mu_))
print("  numeric", mp.nstr(num, 12), " closed form", mp.nstr(ana, 12))
nu = sp.symbols('nu', positive=True)
print("  analytic continuation to mu = 1:", sp.simplify(sp.gamma(1 + nu) * sp.gamma(-sp.Rational(1, 2)) / (2 * sp.sqrt(sp.pi) * sp.gamma(nu))), "(= -nu)")
n = sp.symbols('n', positive=True)
z = sp.symbols('z')
zeta_sum_scalar = -sp.Rational(1, 2) * (2 * sp.zeta(-1) / n)  # -(1/2) sum_{m in Z} |m|/n, zeta-regularised
F = sp.simplify(zeta_sum_scalar - n * zeta_sum_scalar.subs(n, 1))
print("  Tr K_n - n Tr K_1 =", F, " expected (1/12)(1/n - n):", sp.simplify(F - (1 / n - n) / 12) == 0)
Sfac = sp.simplify((F - n * sp.diff(F, n)).subs(n, 1))
print("  (1 - n d/dn) F at n=1 =", Sfac, " (= 1/6)")

# ---------------- Part 2 ----------------
print("\nPART 2: entropy and induced EH with a common proper-time cutoff s_min = eps^2")
s, eps, A, xi, Gind = sp.symbols('s epsilon A xi G_ind', positive=True)
# ln Z_n - n ln Z_1 = (1/2) int_{eps^2}^inf ds/s * F(n) * A/(4 pi s) ; S = (1-n d_n) at n=1
S = sp.Rational(1, 2) * Sfac * A / (4 * sp.pi) * sp.integrate(1 / s ** 2, (s, eps ** 2, sp.oo))
print("  S per real component =", sp.simplify(S), " (= A/(48 pi eps^2))")
# induced: W_E = -(1/2) int ds/s (4 pi s)^-2 s (R/6) = -(R/6) /(2 (4 pi)^2 eps^2) ; W_E = -(1/16 pi G) int R
coefR = sp.Rational(1, 6) / (2 * (4 * sp.pi) ** 2) * sp.integrate(1 / s ** 2, (s, eps ** 2, sp.oo))
invG = sp.simplify(16 * sp.pi * coefR)
print("  induced 1/G_ind =", invG, " (= 1/(12 pi eps^2))")
print("  S - A/(4 G_ind) =", sp.simplify(S - A * invG / 4))
# contact term: E = xi R, R_sing = 4 pi (1-n) delta_Sigma.  Tr K contains -s*xi*R_sing*(4 pi s)^(-2) -> -(1-n) xi A/(4 pi s)
Fc = -(1 - n) * xi
Sc = sp.Rational(1, 2) * sp.simplify((Fc - n * sp.diff(Fc, n)).subs(n, 1)) * A / (4 * sp.pi) * sp.integrate(1 / s ** 2, (s, eps ** 2, sp.oo))
print("  contact term Delta S =", sp.simplify(Sc), " (= -xi A/(8 pi eps^2))")
phi2 = sp.integrate(1 / (4 * sp.pi * s) ** 2, (s, eps ** 2, sp.oo))
print("  <phi^2> =", phi2, "; Q = 2 pi xi A <phi^2> =", sp.simplify(2 * sp.pi * xi * A * phi2), "; -Delta S - Q =", sp.simplify(-Sc - 2 * sp.pi * xi * A * phi2))
invG_xi = sp.simplify(16 * sp.pi * (sp.Rational(1, 6) - xi) / (2 * (4 * sp.pi) ** 2) * sp.integrate(1 / s ** 2, (s, eps ** 2, sp.oo)))
print("  S_BH - S_cone =", sp.simplify(A * invG_xi / 4 - S), " ; S_cone - S_BH =", sp.simplify(S - A * invG_xi / 4), "= Q  (Solodukhin eqs. 322-323)")

# ---------------- Part 3 ----------------
print("\nPART 3: direct numerical test of the first-order cone coefficient (no zeta regularisation)")
T = 300.0


def half_int(v):
    f = lambda t: special.ive(v, t)
    val = 0.0
    edges = [0.0, 1e-3, 0.1, 1.0, 10.0, 50.0, T]
    for a, b in zip(edges[:-1], edges[1:]):
        r, _ = integrate.quad(f, a, b, epsabs=1e-13, epsrel=1e-13, limit=400)
        val += r
    return 0.5 * val


def Dn(nval, kind):
    M = int(9.0 * np.sqrt(T) * max(nval, 1.0)) + 5
    tot = 0.0
    for m in range(-M, M + 1):
        if kind == 'I':
            v = abs(m) / nval
        elif kind == 'IIs':
            e2 = ((nval - 1.0) / 2.0) ** 2
            v = -np.sqrt(e2) / nval if m == 0 else np.sqrt(m * m + e2) / nval
            # m = 0 regular branch: index -|alpha|/2 with alpha=(n-1)/n handled by sign convention below
            al = (nval - 1.0) / nval
            v = -al / 2.0 if m == 0 else v
        elif kind == 'IIv':
            a = nval - 1.0
            if m == 0:
                v = -a / (2.0 * nval)
            else:
                v = np.sqrt((m + a) ** 2 - 0.75 * a * a) / nval
        else:
            raise ValueError
        tot += half_int(v)
    flat = 0.0
    M1 = int(9.0 * np.sqrt(T)) + 5
    for m in range(-M1, M1 + 1):
        flat += half_int(abs(m))
    return tot - nval * flat


def d1(kind, dl):
    return (Dn(1 + dl, kind) - Dn(1 - dl, kind)) / (2 * dl)


for dl in (0.02, 0.01):
    # Richardson across dl
    pass

def fp(kind):
    a = d1(kind, 0.02)
    b = d1(kind, 0.01)
    return (4 * b - a) / 3.0, a, b

print("  checks at integer n:  D_I(2) =", Dn(2.0, 'I'), "  expected (1/12)(1/2-2) =", (0.5 - 2) / 12)
print("  D_I(3) =", Dn(3.0, 'I'), "  expected (1/12)(1/3-3) =", (1 / 3 - 3) / 12)
res = {}
for kind, label, pred in (('I', '(I)  pull-back replica       ', -1 / 6), ('IIs', '(II) scalar, Poisson-structure cone', 1 / 12),
                          ('IIv', '(II) connection component a^+ (block class)', 1 / 12)):
    r, a, b = fp(kind)
    res[kind] = r
    print(f"  F'(1) {label}: {r:.5f} (raw {a:.5f}, {b:.5f})  prediction {pred:.5f}")

# ---------------- Part 4 ----------------
print("\nPART 4: local Seeley-DeWitt a_1 with distributional R_G and E in (II)")
# G conical, angle 2 pi n.  rho ~ r^{n-1}, u = r^n/n, ln rho = alpha ln u + const, alpha = (n-1)/n.
# box_G ln u = 2 pi n delta^2_G  (flux of d_u ln u = 1/u through circle of length 2 pi n u).
al = sp.symbols('alpha')
nn = sp.symbols('n', positive=True)
E_sing = -sp.Rational(1, 2) * ((nn - 1) / nn) * 2 * sp.pi * nn           # coefficient of delta_Sigma in E = -(1/2) box ln rho
R_sing = 4 * sp.pi * (1 - nn)
a1_sing = sp.simplify(R_sing / 6 - E_sing)
print("  E_sing =", sp.simplify(E_sing), "delta ;  R_sing/6 - E_sing =", a1_sing, "delta")
kappa_II = sp.simplify(a1_sing / (4 * sp.pi * (1 - nn)) * sp.Rational(1, 1))
print("  ratio to the (I) value R_sing/6 :", sp.simplify(a1_sing / (R_sing / 6)), " -> S_II / S_I =", sp.simplify(a1_sing / (R_sing / 6)))
print("  contact coefficient c = E_sing/(4 pi (1-n) delta) =", sp.simplify(E_sing / (4 * sp.pi * (1 - nn))))
