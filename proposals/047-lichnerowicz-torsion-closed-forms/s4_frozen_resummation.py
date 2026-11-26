"""
s4_frozen_resummation.py  (proposal 047)  --  prints to stdout only; writes nothing.

Exact Gaussian resummation of the background torsion for fibre-constant loop modes at frozen coefficients, as a statement
about the frozen integral only.  With F = Tbar.k + t dF, A = (1/2)F.F, P = (1/4) eps F F, Cbar(w) = cosh(s sqrt w):
   tr_D e^{-sZ} = 2 C(A+iP) + 2 C(A-iP),   tr_V e^{-sZ} = 4 C(A+iP) C(A-iP),   tr_V - 4 - 2(tr_D - 4) = 4 (C(A+iP)-1)(C(A-iP)-1),
and A|_{t=0} = -Lam^2, P|_{t=0} = 0, Lam = y0 |kvec| at y^i = 0.
(A) Background: <tr_D e^{-sZ}> = 4 (1-xi) e^{-xi/2}, <tr_V e^{-sZ}> = 2 + 2 (1-4xi) e^{-2xi}, xi = s coth^2 tau / 2, checked by quadrature.
(B) Second variation: closed forms for the helicities 2, 1, 0 (polynomial in xi times exponentials) compared with
    (i) the series s Q1 + s^2 Q2 of 046, (ii) a direct numerical evaluation with matrix exponentials and Gauss quadrature.
(C) K-weighted mixed form  G_h(M) = int ds s^{-1} e^{-sM} <D2>_h  and the first term; the frozen non-Einstein coefficient as
    a function of M/coth^2 tau.
(D) Completeness test at the background: the frozen s^2 coefficient against the complete a_2 index part of the Laplace-type
    operator (Gilkey), and that against the Levi-Civita curvature expression.
"""
import sys
sys.dont_write_bytecode = True
import numpy as np, sympy as sp, itertools
from scipy.linalg import expm

# ---------- symbolic radial machinery ----------
xi = sp.Symbol('xi', positive=True)
beta, sig = sp.symbols('beta sigma', positive=True)
Phi = sig * sp.sqrt(sp.pi / 2) * sp.exp(-beta ** 2 * sig ** 2 / 2)                 # int_0^inf cos(beta r) exp(-r^2/2 sig^2) dr
def I_cos(j):   # int r^{2j} cos(beta r) gaussian
    return (-1) ** j * sp.diff(Phi, beta, 2 * j)
def I_sin(j):   # int r^{2j+1} sin(beta r) gaussian
    return (-1) ** (j + 1) * sp.diff(Phi, beta, 2 * j + 1)
norm = sp.sqrt(2 / sp.pi) / sig ** 3                                                 # 3D radial measure norm: int_0^inf r^2 gaussian = sig^3 sqrt(pi/2)

s_, Y0, M_ = sp.symbols('s y0 m', positive=True)
alpha = s_ * Y0                                                                      # z = alpha r, sigma^2 = 1/(2 s m^2)
sig2 = 1 / (2 * s_ * M_ ** 2)
def avg_cos_r(l, b):      # <r^{2l} cos(b r)> in 3D
    return (norm * I_cos(l + 1)).subs(beta, b)
def avg_sin_r(l, b):      # <r^{2l-1}... > helper: <r^{2l} sin(b r)/r> = norm * int r^{2l+1} sin(b r)
    return (norm * I_sin(l)).subs(beta, b)
def finalise(e):
    e = e.subs(sig, sp.sqrt(sig2))
    return sp.simplify(e)
# radial expectation values, l >= 0 or >= 1 as stated:
def E_Cp(l):      # <C'(-Lam^2) r^{2l}> with C' = s sin z /(2 Lam) = (s/(2 y0)) sin(alpha r)/r
    return (s_ / (2 * Y0)) * avg_sin_r(l, alpha)
def E_Cpp(l):     # <C''(-Lam^2) r^{2l}>, l >= 1, C'' = (s^4/4)(sin z - z cos z)/z^3
    return (s_ ** 4 / 4) * ((1 / alpha ** 3) * (norm * I_sin(l - 1)).subs(beta, alpha) - (1 / alpha ** 2) * (norm * I_cos(l)).subs(beta, alpha))

k0, k1, k2, k3 = sp.symbols('k0 k1 k2 k3')
kup = sp.Matrix([k0, k1, k2, k3])
etaS = sp.diag(-1, 1, 1, 1)
dot = lambda u, v: (u.T * etaS * v)[0]
Q0, Q3 = sp.symbols('q0 q3', real=True)
def angular(poly_expr):
    """average over directions of kvec and Gaussian moments of k0^mu, returns polynomial in r^2 (Symbol R2) at fixed s"""
    R2 = sp.Symbol('R2', positive=True)
    P = sp.Poly(sp.expand(poly_expr), k0, k1, k2, k3)
    tot = 0; var = 1 / (2 * s_ * M_ ** 2)
    df = lambda n: sp.factorial2(n - 1) if n > 0 else 1
    for (a, b, c, d), co in P.terms():
        if a % 2 or b % 2 or c % 2 or d % 2: continue
        n = b + c + d
        ang = df(b) * df(c) * df(d) / sp.factorial2(n + 1) if n > 0 else 1
        tot += co * df(a) * (-var) ** (a // 2) * ang * R2 ** (n // 2)
    return sp.Poly(tot, R2)

def helicity_forms(q0v, q3v, y0v, m_v):
    qu = sp.Matrix([-q0v, 0, 0, q3v]); yu = sp.Matrix([sp.Symbol('y0', positive=True), 0, 0, 0])
    yu = sp.Matrix([Y0, 0, 0, 0])
    q2 = dot(qu, qu)
    e1 = sp.Matrix([0, 1, 0, 0]); e2 = sp.Matrix([0, 0, 1, 0]); e3 = sp.Matrix([q3v, 0, 0, -q0v])
    pols = {2: e1 * e1.T - e2 * e2.T, 1: e1 * e3.T + e3 * e1.T, 0: e3 * e3.T - dot(e3, e3) / 2 * (e1 * e1.T + e2 * e2.T)}
    out = {}
    for h, hh in pols.items():
        u = hh * etaS * kup
        uu = dot(u, u); ku = dot(kup, u); yuu = dot(yu, u); kk = dot(kup, kup); ky = dot(kup, yu); kq = dot(kup, qu); yq = dot(yu, qu); yy_ = dot(yu, yu)
        A2 = q2 * uu / 4; A1 = -(kq * yuu - ku * yq)
        GM = sp.Matrix([[kk, ky, kq, ku], [ky, yy_, yq, yuu], [kq, yq, q2, 0], [ku, yuu, 0, uu]])
        P12 = -GM.det(method='berkowitz')
        out[h] = dict(A2=angular(A2), A1s=angular(A1 ** 2), P1s=angular(P12), unit=None)
    return out

def closed_dirac(forms):
    """<D2> = 4 <C' A2> + 2 <C'' (A1^2 - P1^2)>"""
    tot = 0
    for (n,), co in forms['A2'].terms():
        tot += 4 * co * E_Cp(n)
    for name, sgn in (('A1s', 1), ('P1s', -1)):
        for (n,), co in forms[name].terms():
            if sp.simplify(co) == 0: continue
            assert n >= 1
            tot += 2 * sgn * co * E_Cpp(n)
    return tot

# numerical test values
q0v, q3v, y0v, m_v = sp.Rational(2, 5), sp.Rational(9, 10), sp.Integer(5), sp.Integer(3)
forms = helicity_forms(q0v, q3v, y0v, m_v)
x_val = (sp.Integer(16) * (q3v ** 2 - q0v ** 2) + (y0v * q0v) ** 2) / (-m_v ** 2 * (q3v ** 2 - q0v ** 2))
coth2 = sp.Rational(25, 9)
print("(B) closed forms at (y0,y4) = (5,3), q = (2/5,0,0,9/10), x = %s = %.5f; xi = s coth^2 tau / 2" % (x_val, float(x_val)))
closed = {}
for h in (2, 1, 0):
    e = closed_dirac(forms[h])
    e = e.subs(sig, sp.sqrt(sig2)).subs(Y0, y0v).subs(M_, m_v)
    unit = (2 * s_ ** 2 * sum(co * ((1 / (2 * s_ * m_v ** 2)) * 3 ** n if n else 1) for (n,), co in forms[h]['A2'].terms())).subs(Y0, y0v).subs(M_, m_v)
    # unit: s Q1 with Q1 = -2 unit0: compute Q1 from the leading coefficient of the series
    ser = sp.series(sp.simplify(e), s_, 0, 4).removeO()
    Q1 = ser.coeff(s_, 1); Q2 = ser.coeff(s_, 2); Q3_ = ser.coeff(s_, 3)
    unit0 = Q1 / (-2)
    phi = {2: 0, 1: sp.Rational(1, 2), 0: sp.Rational(2, 3)}[h]
    closed_Q2 = sp.Rational(3, 2) * coth2 + (x_val - 1) * phi
    res = sp.simplify(sp.simplify(e / unit0).subs(s_, 2 * xi / coth2))
    closed[h] = (sp.simplify(e / unit0), unit0)
    print("  helicity %d: <D2>/unit0 in xi: %s" % (h, sp.factor(sp.simplify(res))))
    print("      series check: Q1/unit0 = %s (expect -2); Q2/unit0 = %s (expect %s)" % (sp.nsimplify(Q1 / unit0), sp.nsimplify(Q2 / unit0), sp.nsimplify(closed_Q2)))

# ---------- direct numerical evaluation ----------
sxn = np.array([[0, 1], [1, 0]], complex); syn = np.array([[0, -1j], [1j, 0]]); szn = np.diag([1., -1.]).astype(complex); I2 = np.eye(2)
gE = [np.kron(sxn, I2), np.kron(syn, I2), np.kron(szn, sxn), np.kron(szn, syn)]
etaN = np.diag([-1., 1, 1, 1]); Gam = [1j * gE[0], gE[1], gE[2], gE[3]]
SigD = np.array([[0.25 * (Gam[a] @ Gam[b] - Gam[b] @ Gam[a]) for b in range(4)] for a in range(4)])
SigV = np.zeros((4, 4, 4, 4), complex)
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                SigV[a, b, c, d] = etaN[a, c] * (1 if b == d else 0) - etaN[b, c] * (1 if a == d else 0)
def num_eval(sv, hh, q_up, yv, m, Sig):
    """direct evaluation of the t^2 coefficient of <tr e^{-sZ}>, k^0 = i w (Gauss-Hermite), kvec = r n (Gauss quadrature)"""
    from numpy.polynomial.hermite import hermgauss
    sigma = np.sqrt(1 / (2 * sv * m ** 2))
    wn, ww = hermgauss(5); wn = wn * np.sqrt(2) * sigma; ww = ww / np.sqrt(np.pi)
    # radial: Gauss-Laguerre type through 3D Gaussian: r^2 measure -> use Gauss-Hermite on the line with r^2 weight (even integrand)
    rn, rw = hermgauss(60); rn = rn * np.sqrt(2) * sigma; rw = rw / np.sqrt(np.pi) * (rn ** 2 / sigma ** 2)
    ctn, ctw = np.polynomial.legendre.leggauss(8); phs = (np.arange(16) + 0.5) * 2 * np.pi / 16
    tot = 0
    T0 = np.zeros((4, 4, 4));
    for a in range(4):
        for b in range(4):
            for mu in range(4):
                T0[a, b, mu] = etaN[a, mu] * yv[b] - etaN[b, mu] * yv[a]
    # dT^{ab mu} = -(1/2) (q^a h^{b mu} - q^b h^{a mu})
    dT = -0.5 * (np.einsum('a,bm->abm', q_up, hh) - np.einsum('b,am->abm', q_up, hh))
    def trace_exp(Tt, k_low):
        Tl = np.einsum('ac,bd,cdm->abm', etaN, etaN, Tt)
        Z = -1j * np.einsum('abij,ab->ij', Sig, np.einsum('abm,m->ab', Tl, k_low))
        return np.trace(expm(-sv * Z))
    ts = np.array([-1., -0.5, 0.0, 0.5, 1.0]) * 0.3
    for iw, w in enumerate(wn):
        for ir, r in enumerate(rn):
            if r <= 0: continue
            for ic, ct in enumerate(ctn):
                st = np.sqrt(1 - ct ** 2)
                for ph in phs:
                    kup_ = np.array([1j * w, r * st * np.cos(ph), r * st * np.sin(ph), r * ct])
                    k_low = etaN @ kup_
                    vals = np.array([trace_exp(T0 + t * dT, k_low) for t in ts])
                    c2 = np.linalg.solve(np.vander(ts, 5, increasing=True).astype(complex), vals)[2]
                    tot += ww[iw] * 2 * rw[ir] * ctw[ic] / 2 / 16 * c2
    return tot
qupv = np.array([-float(q0v), 0, 0, float(q3v)]); yvv = np.array([float(y0v), 0, 0, 0])
e1n = np.array([0, 1., 0, 0]); e2n = np.array([0, 0, 1., 0]); e3n = np.array([float(q3v), 0, 0, -float(q0v)])
polsn = {2: np.outer(e1n, e1n) - np.outer(e2n, e2n), 1: np.outer(e1n, e3n) + np.outer(e3n, e1n),
         0: np.outer(e3n, e3n) - (e3n @ etaN @ e3n) / 2 * (np.outer(e1n, e1n) + np.outer(e2n, e2n))}
print("\n    direct numerical check of <D2> (matrix exponential, Gauss quadrature):")
for h in (2, 0):
    for sv in (0.3, 1.2):
        val = complex(closed[h][0].subs(s_, sv) * closed[h][1].subs(s_, sv))
        num = num_eval(sv, polsn[h], qupv, yvv, 3.0, SigD)
        print("      helicity %d, s = %.2f: closed %.8f, numeric %.8f%+.1ei, relative difference %.1e" % (h, sv, val.real, num.real, num.imag, abs(val - num) / abs(val)))

print("\n(A) background traces: <cos z> and <cos 2z>, closed against quadrature")
for sv in (0.2, 1.0, 3.0):
    al = sv * 5.0; sg_ = np.sqrt(1 / (2 * sv * 9.0)); xiv = sv * (25 / 9) / 2
    rn, rw = np.polynomial.hermite.hermgauss(200); rr = rn * np.sqrt(2) * sg_; ww_ = rw / np.sqrt(np.pi) * rr ** 2 / sg_ ** 2
    c1 = np.sum(ww_ * np.cos(al * np.abs(rr))); c2 = np.sum(ww_ * np.cos(2 * al * np.abs(rr)))
    print("   s=%.1f xi=%.4f: <cos z> %.10f vs (1-xi)e^{-xi/2} %.10f; <cos 2z> %.10f vs (1-4xi)e^{-2xi} %.10f" % (sv, xiv, c1, (1 - xiv) * np.exp(-xiv / 2), c2, (1 - 4 * xiv) * np.exp(-2 * xiv)))

print("\n(C) K-weighted frozen mixed form G_h(M) = int_0^inf ds s^{-1} e^{-sM} <D2>_h / unit (tau^K = tau_2 s^2 e^{-sM}),")
print("    first-order truncation: -2/M + Q2hat/M^2; at (5,3), x as above")
Mgrid = [100, 30, 10, 3, 1, 0.3, 0.1, 0.03, 0.01]
hdr = "   M   coth^2/M " + " ".join("  G_%d(M)    trunc_%d " % (h, h) for h in (2, 1, 0)) + "   G_1-G_2  G_0-G_2"
print(hdr)
fn = {}
for h in (2, 1, 0):
    # closed[h][0] is a function of s only
    fn[h] = sp.lambdify(s_, closed[h][0], 'numpy')
from scipy.integrate import quad
qhat = {2: float(sp.Rational(3, 2) * coth2), 1: float(sp.Rational(3, 2) * coth2 + (x_val - 1) / 2), 0: float(sp.Rational(3, 2) * coth2 + (x_val - 1) * 2 / 3)}
for Mv in Mgrid:
    row = {}
    for h in (2, 1, 0):
        row[h] = quad(lambda t: complex(fn[h](t)).real / t * np.exp(-t * Mv), 0, np.inf, limit=400)[0]
    print("  %6.2f %7.3f " % (Mv, float(coth2) / Mv) + " ".join("%10.5f %10.5f" % (row[h], -2 / Mv + qhat[h] / Mv ** 2) for h in (2, 1, 0)) + "  %8.4f %8.4f" % (row[1] - row[2], row[0] - row[2]))

# ---------- (D) completeness test at the background ----------
print(); print("(D) completeness at the background, exact rational points (m^2 = -y.y - l^2): frozen s^2 coefficient against the complete a_2 index part")
Y = sp.symbols('y0:4', real=True); L_ = sp.Symbol('L', positive=True)
yl_ = etaS * sp.Matrix(Y); yy2 = sum(Y[i] * yl_[i] for i in range(4)); m2s = -yy2 - L_ ** 2
Gs = etaS / m2s; Gis = etaS * m2s
Gm_ = [[[sum(Gis[l_, r_] * (sp.diff(Gs[r_, n_], Y[k_]) + sp.diff(Gs[r_, k_], Y[n_]) - sp.diff(Gs[k_, n_], Y[r_])) for r_ in range(4)) / 2 for n_ in range(4)] for k_ in range(4)] for l_ in range(4)]
def Riem(r_, s2, mu, nu):
    t = sp.diff(Gm_[r_][nu][s2], Y[mu]) - sp.diff(Gm_[r_][mu][s2], Y[nu])
    for l_ in range(4):
        t += Gm_[r_][mu][l_] * Gm_[l_][nu][s2] - Gm_[r_][nu][l_] * Gm_[l_][mu][s2]
    return t
RR = [[[[Riem(a, b, c, d) for d in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]
pts = [{Y[0]: sp.Integer(5), Y[1]: 0, Y[2]: 0, Y[3]: 0, L_: 4}, {Y[0]: sp.Integer(13), Y[1]: 3, Y[2]: -2, Y[3]: 1, L_: 5}]
gam = [sp.Matrix(np.array(g).tolist()) for g in []]
from sympy.physics.quantum import TensorProduct as TP
sxs = sp.Matrix([[0, 1], [1, 0]]); sys_ = sp.Matrix([[0, -sp.I], [sp.I, 0]]); szs = sp.Matrix([[1, 0], [0, -1]]); I2s = sp.eye(2)
gEs = [TP(sxs, I2s), TP(sys_, I2s), TP(szs, sxs), TP(szs, sys_)]
Gams = [sp.I * gEs[0], gEs[1], gEs[2], gEs[3]]
SDs = {(a, b): (Gams[a] * Gams[b] - Gams[b] * Gams[a]) / 4 for a in range(4) for b in range(4)}
Tb = [[[etaS[a, mu] * Y[b] - etaS[b, mu] * Y[a] for mu in range(4)] for b in range(4)] for a in range(4)]
def Bup(mu):                       # B^mu = kappa Sigma_ab T^{ab mu}, kappa = -1
    tot = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            if a != b: tot += -1 * SDs[(a, b)] * (etaS[a, a] * etaS[b, b] * Tb[a][b][mu])
    return tot
Bu = [Bup(mu) for mu in range(4)]
Bl = [sum((Gs[mu, nu] * Bu[nu] for nu in range(4)), sp.zeros(4, 4)) for mu in range(4)]
Om = [[-(sp.diff(Bl[nu], Y[mu]) - sp.diff(Bl[mu], Y[nu])) / 2 + (Bl[mu] * Bl[nu] - Bl[nu] * Bl[mu]) / 4 for nu in range(4)] for mu in range(4)]
for p in pts:
    Gis0 = Gis.subs(p); Gs0 = Gs.subs(p); m2v = m2s.subs(p)
    RRv = [[[[sp.nsimplify(RR[a][b][c][d].subs(p)) for d in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]
    Rl = lambda a, b, c, d: sum(Gs0[a, e_] * RRv[e_][b][c][d] for e_ in range(4))
    Ric = sp.Matrix(4, 4, lambda b, d: sum(RRv[a][b][a][d] for a in range(4)))
    Rsc = sum(Gis0[b, d] * Ric[b, d] for b in range(4) for d in range(4))
    Riem2 = sum(Rl(a, b, c, d) * Rl(a, b, c, d) * Gis0[a, a] * Gis0[b, b] * Gis0[c, c] * Gis0[d, d] for a, b, c, d in itertools.product(range(4), repeat=4))
    Ric2 = sum(Ric[a, b] ** 2 * Gis0[a, a] * Gis0[b, b] for a in range(4) for b in range(4))
    Omv = [[Om[mu][nu].subs(p).applyfunc(sp.nsimplify) for nu in range(4)] for mu in range(4)]
    trOm2 = sp.expand(sum((Omv[mu][nu] * Omv[mu][nu]).trace() * Gis0[mu, mu] * Gis0[nu, nu] for mu in range(4) for nu in range(4)))
    rho_ = 1 / sp.sqrt(m2s); sqG = 1 / m2s ** 2
    phi_ = sp.log(rho_ / sqG) / 2
    dp = [sp.diff(phi_, Y[i]) for i in range(4)]
    boxp = sum(sp.diff(sqG * Gis[i, i] * dp[i], Y[i]) for i in range(4)) / sqG
    dp2 = sum(Gis[i, i] * dp[i] ** 2 for i in range(4))
    e_ = sp.nsimplify(sp.simplify((-boxp - dp2).subs(p))) + Rsc / 6      # e = R/6 + E0
    c_ = sp.Rational(-yy2.subs(p) , 1) / m2v
    # frozen: <4 cos z> = 4 (1-xi) e^{-xi/2}; in the frame (y^i != 0 allowed): Lam = sqrt((k.y)^2 - k^2 y^2), xi = s c /2 with c = -y.y/m^2
    Q1bar = -3 * c_ ; Q2bar = sp.Rational(5, 8) * c_ ** 2
    a_ = Q1bar / 4
    complete = 4 * e_ * a_ + 2 * a_ ** 2 + trOm2 / 12
    lc = Rsc ** 2 / 72 - Riem2 / 24 - 2 * e_ ** 2
    print("   point %s: c = %s; R = %s, e = %s; Q1bar = %s; check e + a = -R/12: %s" % ({str(k): v for k, v in p.items()}, c_, sp.nsimplify(Rsc), sp.nsimplify(e_), Q1bar, sp.simplify(e_ + a_ + Rsc / 12) == 0))
    print("       tr Omega^2 (from B) = %s ; -(1/2) Riem^2 = %s" % (sp.nsimplify(trOm2), sp.nsimplify(-Riem2 / 2)))
    print("       frozen s^2 coefficient (Z^4 part) = %s ; complete index a_2 (mod total derivatives): e tr A + (1/2) tr A^2 + (1/12) tr Omega^2 = %s ; R^2/72 - Riem^2/24 - 2 e^2 = %s" % (Q2bar, sp.nsimplify(complete), sp.nsimplify(lc)))
