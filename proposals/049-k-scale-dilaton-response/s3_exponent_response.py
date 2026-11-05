"""049 s3: static response for a K mass with exponent beta_K. Prints only.

Setting of the 048 paragraph: q=(0,0,0,k), q.y=0, equal weights. At a fibre point with polar angle theta about qhat,
  (u.v)^2 = m^2 k^2 c^2,  v.v = k^2 (l^2 s^2 - m^2 c^2),  c = cos theta, s = sin theta.
The average over the fibre is int_0^1 dc (azimuth averaged where needed).

 (A) pointwise inverse with a general B: the form C[(v.v) a.a + b (a.v)^2] + 2m a.Xv has extremum -(m^2/C) I_n;
 (B) algebra of I for X = rho0 (uu + (beta/2) eta), and its decomposition;
 (C) closed forms of g and g2 against regulated quadrature; K(tau) of 048 in terms of them;
 (D) potentials from the solution, ratio gamma_beta and its limits;
 (E) adding a trace mass term and the vacuum shift: the three poles (algebra);
 (F) direct numerical elimination of a discretised fibre with a regulator, compared with the closed result.
"""
import numpy as np
import sympy as sp
from scipy import integrate

print("(A) pointwise elimination")
C, b, m = sp.symbols("C b m", positive=True)
vv, Xv2, vXv = sp.symbols("vv Xv2 vXv", real=True)
# In the plane spanned by v and Xv the quadratic form is C vv I + C b v v^T.  Sherman-Morrison gives
# (Q^-1) = [1/(C vv)] [I - b v v^T/(vv (1 + b))], so the extremum of a.Q.a + 2m a.Xv is -m^2 Xv.Q^-1.Xv.
ext = -m ** 2 * (Xv2 - b * vXv ** 2 / (vv * (1 + b))) / (C * vv)
rho = 1 / (1 + b)
Iform = Xv2 / vv + (rho - 1) * vXv ** 2 / vv ** 2
print("    residual of -m^2/C * I_n against the extremum:", sp.simplify(ext + m ** 2 * Iform / C))
# numerical confirmation with random 4-vectors and eta
np.random.seed(49)
eta = np.diag([-1.0, 1, 1, 1])
for _ in range(3):
    v = np.random.normal(size=4)
    Xv_ = np.random.normal(size=4)
    b_ = 0.37
    C_ = 1.3
    m_ = 2.1
    vv_ = v @ eta @ v
    Q = C_ * (vv_ * eta + b_ * np.outer(eta @ v, eta @ v))
    src = 2 * m_ * (eta @ Xv_)
    a = -np.linalg.solve(2 * Q, src)
    val = a @ Q @ a + src @ a
    Xv2_ = Xv_ @ eta @ Xv_
    vXv_ = v @ eta @ Xv_
    rho_ = 1 / (1 + b_)
    print("    numeric extremum %.10f, formula %.10f" % (val, -m_ ** 2 / C_ * (Xv2_ / vv_ + (rho_ - 1) * vXv_ ** 2 / vv_ ** 2)))

print("(B) I for X = rho0 (u u + (beta/2) eta), per rho0^2")
beta, rho_s, g, g2 = sp.symbols("beta varrho g g2", real=True)
uv2, vv = sp.symbols("uv2 vv", real=True)
# Xv = u (u.v) + (beta/2) v, with u.u = -1: Xv.Xv = -(u.v)^2 + beta (u.v)^2 + (beta^2/4) v.v
Xv2e = -uv2 + beta * uv2 + beta ** 2 / 4 * vv
vXve = uv2 + beta / 2 * vv
In = Xv2e / vv + (rho_s - 1) * vXve ** 2 / vv ** 2
In = sp.expand(In)
# <uv2/vv> = -g, <uv2^2/vv^2> = g2
I_beta = In.subs(uv2 ** 2, g2 * vv ** 2).subs(uv2, -g * vv)
I_beta = sp.simplify(I_beta)
print("    I/rho0^2 =", sp.factor(I_beta))
sig = beta / 2
dec = rho_s * (sig - g) ** 2 + (g - g2 + rho_s * (g2 - g ** 2))
print("    residual of rho (beta/2 - g)^2 + [g - g2 + rho (g2 - g^2)]:", sp.simplify(I_beta - dec))
print("    at rho=1:", sp.factor(I_beta.subs(rho_s, 1)), " S1 (beta=1):", sp.simplify(I_beta.subs({rho_s: 1, beta: 1})), " S2 (beta=0):", sp.simplify(I_beta.subs({rho_s: 1, beta: 0})))
print("    at g=g2=1:", sp.factor(I_beta.subs({g: 1, g2: 1})))

print("(C) closed forms of g, g2")


def closed(s2):
    th = 1 + 1 / s2
    c0 = 1 / np.sqrt(1 + s2)
    at = np.arctanh(c0)
    gv = (1 - c0 * at) / th
    g2v = (1 - 1.5 * c0 * at - (th - 1) / 2) / th ** 2
    return gv, g2v, c0, th


def regulated(s2, eps):
    gv, g2v, c0, th = closed(s2)
    # real parts of the prescription c^2 - c0^2 -> c^2 - c0^2 + i eps
    def den(c):
        return (c ** 2 - c0 ** 2) + 1j * eps
    f1 = lambda c: (c ** 2 / den(c)).real / th
    f2 = lambda c: (c ** 4 / den(c) ** 2).real / th ** 2
    pts = [c0]
    a = integrate.quad(f1, 0, 1, points=pts, limit=2000)[0]
    b_ = integrate.quad(f2, 0, 1, points=pts, limit=2000)[0]
    return a, b_


print("    %8s %10s %10s | eps=1e-3: %10s %10s | eps=1e-5: %10s %10s" % ("s^2", "g", "g2", "g", "g2", "g", "g2"))
for s2 in (0.5625, 1.0, 4.0, 25.0, 100.0):
    gv, g2v, c0, th = closed(s2)
    r1 = regulated(s2, 1e-3)
    r2 = regulated(s2, 1e-5)
    print("    %8.4f %10.6f %10.6f |           %10.6f %10.6f |           %10.6f %10.6f" % (s2, gv, g2v, r1[0], r1[1], r2[0], r2[1]))
print("    large s^2: 1-g ~ 2/s^2, g-g2 ~ 2/s^2, g2-g^2 = O(1/s^4):")
for s2 in (1e2, 1e3, 1e4, 1e5):
    gv, g2v, c0, th = closed(s2)
    print("      s^2=%8.0f  (1-g)s^2=%.5f  (g-g2)s^2=%.5f  (g2-g^2)s^4=%.5f  g(1-g)s^2=%.5f" % (s2, (1 - gv) * s2, (gv - g2v) * s2, (g2v - gv ** 2) * s2 ** 2, gv * (1 - gv) * s2))
print("    048 K(tau) = 4 g2 - 4 g + 1 from the S1 case of (B); values:")
for s2 in (1.0, 4.0, 100.0, 1e4):
    gv, g2v, c0, th = closed(s2)
    print("      s^2=%8.1f K=%.6f" % (s2, 4 * g2v - 4 * gv + 1))

print("(D) potentials at rho=1, per rho0, from hbar proportional to <(Xv v + v Xv)/v.v>")
h00 = (2 - beta) * g
h11 = beta * (1 - g) / 2
t = sp.simplify(-h00 + 2 * h11)
print("    hbar^00 =", h00, ", hbar^11 =", h11, ", t =", sp.factor(t))
hb00 = sp.simplify(h00 + beta / 2 * t)  # eta^00 = -1, h_beta = hbar - (beta/2) eta t
hb11 = sp.simplify(h11 - beta / 2 * t)
print("    h_beta^00 =", sp.factor(hb00), ", h_beta^11 =", sp.factor(hb11))
print("    residual of 2 h_beta^00 against I (the source couples to h_beta):", sp.simplify(2 * hb00 - 4 * (beta ** 2 / 4 + (1 - beta) * g)))
print("    sum h^00 + h^11 same in both readings, residual:", sp.simplify(hb00 + hb11 - h00 - h11))
gam = sp.simplify(hb11 / hb00)
print("    gamma_beta(g) =", sp.factor(gam))
print("    gamma_beta(g=1) =", sp.factor(gam.subs(g, 1)), "; at beta=1:", sp.simplify(gam.subs(beta, 1)), "; at beta=0:", sp.simplify(gam.subs(beta, 0)))
print("    R(beta) = 4 I at rho=1, g=1 :", sp.factor(4 * (beta ** 2 / 4 + (1 - beta))))
print("    roots of gamma=1 at general g:", sp.solve(sp.numer(sp.together(gam - 1)), beta))
hbs = beta.subs(beta, 2 * g)
print("    t = 0 at beta = 2 g: hbar^11/hbar^00 =", sp.simplify((h11 / h00).subs(beta, 2 * g)), ", I at rho=1 =", sp.factor((beta ** 2 / 4 + (1 - beta) * g).subs(beta, 2 * g)))
print("    table at g=1:  beta, kappa_m=1-beta/2, gamma=beta/(2-beta), R=(2-beta)^2")
for bv in (sp.Integer(-1), sp.Rational(-1, 2), sp.Rational(-1, 6), sp.Integer(0), sp.Rational(1, 2), sp.Integer(1)):
    print("      %6s %6s %6s %6s" % (bv, 1 - bv / 2, bv / (2 - bv), (2 - bv) ** 2))

print("(E) trace mass term and vacuum shift")
q2, qs2, qb2, L, s0, tt, ss = sp.symbols("q2 qs2 qb2 L s0 t sigma", real=True)
Y = g - g2 + rho_s * (g2 - g ** 2)
S_sigma = -(L / q2) * (rho_s * (ss - g) ** 2 + Y)  # rho0 = 1
Mass = qs2 / (2 * L)
# Legendre: S = S(sigma) - (sigma - s0) t + (1/2) Mass t^2; extremise over sigma and t
sol = sp.solve([sp.diff(S_sigma, ss) - tt, -(ss - s0) + Mass * tt], [ss, tt], dict=True)[0]
Sval = sp.simplify((S_sigma - (ss - s0) * tt + Mass * tt ** 2 / 2).subs(sol))
target = -L * rho_s * (s0 - g) ** 2 / (q2 + rho_s * qs2) - (L / q2) * Y
print("    residual of the closed response with a trace mass:", sp.simplify(Sval - target))
rv = q2 / (q2 - qb2)
target2 = sp.simplify(target.subs(rho_s, rv))
pf = -L * (s0 - g) ** 2 / (q2 - qb2 + qs2) - (L / q2) * (g - g2) - L * (g2 - g ** 2) / (q2 - qb2)
print("    residual with rho -> q^2/(q^2 - q_b^2) against the three poles:", sp.simplify(target2 - pf))

print("(F) discretised fibre with a regulator, V = T + vacuum shift, compared with the closed result")


def direct(s2, bval, rho_val, eps, Nc=200001):
    gv, g2v, c0, th = closed(s2)
    c = np.linspace(0, 1, Nc)
    # work in units m k = 1 so that (u.v)^2 = c^2 and v.v = (1/s2)(1-c^2) - c^2 + i eps
    vv_ = (1 - c ** 2) / s2 - c ** 2 + 1j * eps
    uv2_ = c ** 2
    Xv2 = (bval - 1) * uv2_ + bval ** 2 / 4 * vv_
    vXv = uv2_ + bval / 2 * vv_
    In = Xv2 / vv_ + (rho_val - 1) * vXv ** 2 / vv_ ** 2
    return np.trapezoid(In.real, c)


print("    %8s %6s %6s | %12s %12s %12s" % ("s^2", "beta", "rho", "closed", "eps=1e-3", "eps=1e-5"))
for s2 in (4.0, 25.0):
    for bv in (0.0, 1.0, -1.0, -0.5):
        for rv_ in (1.0, 0.5):
            gv, g2v, _, _ = closed(s2)
            cl = rv_ * (bv / 2 - gv) ** 2 + gv - g2v + rv_ * (g2v - gv ** 2)
            print("    %8.2f %6.2f %6.2f | %12.6f %12.6f %12.6f" % (s2, bv, rv_, cl, direct(s2, bv, rv_, 1e-3), direct(s2, bv, rv_, 1e-5, 2000001)))
