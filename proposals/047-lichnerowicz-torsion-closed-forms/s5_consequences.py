"""
s5_consequences.py  (proposal 047)  --  prints to stdout only; writes nothing.

(F) Frozen resummation, general q: <D2>_h = unit (-2 s) e^{-xi/2} [1 - (1 + nu phi) xi + (2/15 + nu phi/5) xi^2], xi = s c/2, c = coth^2 tau,
    nu = (x-1)/c; hence with Mt = M + c/4 the replacement of 1/M^2 in N(M) is F(M) = 1/Mt^2 - (c/5)/Mt^3 > 0.
(N) The non-Einstein coefficient as a function of the wave vector: N(M; x) = W_B(M) lambda_L(x) + T(M) + 24 (L/c0)/M^2,
    lambda_L(x) = -(6/5)(2 + 1/x); T = 1/M^2 (first order, 046) or F(M) (frozen resummation).
    M*(x) depends on x: table of roots at (5,3) and at several x; the 046 row is x = -2.70412.
    Range of lambda_L: x in (-inf, -l^2/m^2] (q spacelike), x in [1, inf) (q timelike), x -> +-inf on the null cone.
(P) Positivity: v^K, tau^K >= 0 for Hermitian Zeeman couplings (Peierls-Bogoliubov), random non-commuting tests; B_0 >= B_1 pointwise.
    c_T(five, averaged) = (1/6) V + (1/12) T; c_T^{TT} on the null cone; gaps for the three replicas.
(B) v^K = tau^K identically for commuting fluxes with f1 = f2 + f3.
(O) On-shell limit of the helicity-two eigenvalues: lambda_2 -> -24/5, SC2 -> 2/5, L1 -> 7/30, tested at nearly null q with the exact forms.
(D) Fibre-point decomposition: X_hat = m^-4 q^2 (v.v)(a.a) against -4 EH[h_n] + m^-4 q^2 (a.v)^2, tested on the exact pointwise forms.
"""
import sys, os
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '046-fibre-regime-interpolation'))
from forms_lib import *
import numpy as np, scipy.linalg as sl, random, itertools
from scipy.optimize import brentq
from scipy.linalg import expm
random.seed(475); rng = np.random.default_rng(475)

def cJJ(J, Jp):
    if Jp == J + 2: return 3 * (J + 1) * (J + 2) / (2 * (2 * J + 1) * (2 * J + 3))
    if Jp == J: return J * (J + 1) / ((2 * J - 1) * (2 * J + 3))
    if Jp == J - 2 and J >= 2: return 3 * J * (J - 1) / (2 * (2 * J - 1) * (2 * J + 1))
    return 0.0
mu = lambda J: J * (J + 2)
def W_B(M, n):
    WB = 0.0
    for J in range(n + 1):
        for Jp in (J - 2, J, J + 2):
            if Jp < 0 or Jp > n: continue
            c_ = cJJ(J, Jp)
            if c_ == 0: continue
            lo = min(mu(J), mu(Jp)); d = abs(mu(Jp) - mu(J))
            WB += (2 * J + 1) * c_ * (np.log1p(d / (M + lo)) / d if d > 0 else 1.0 / (M + lo))
    return WB
lamL = lambda x: -(6 / 5) * (2 + 1 / x)
c0 = 25 / 9; ell2 = 16.0; m2 = 9.0
Fres = lambda M, c=c0: 1 / (M + c / 4) ** 2 - (c / 5) / (M + c / 4) ** 3

# ---------- (F) general-q check of the closed resummed form ----------
print("(F) frozen resummed second variation: exact comparison with the closed form, general q (exact rational Isserlis + radial closed forms)")
xi = sp.Symbol('xi', positive=True); s_ = sp.Symbol('s', positive=True)
beta, sig = sp.symbols('beta sigma', positive=True)
Phi = sig * sp.sqrt(sp.pi / 2) * sp.exp(-beta ** 2 * sig ** 2 / 2)
I_cos = lambda j: (-1) ** j * sp.diff(Phi, beta, 2 * j)
I_sin = lambda j: (-1) ** (j + 1) * sp.diff(Phi, beta, 2 * j + 1)
norm = sp.sqrt(2 / sp.pi) / sig ** 3
k0, k1, k2, k3 = sp.symbols('k0 k1 k2 k3'); kup = sp.Matrix([k0, k1, k2, k3]); etaS = sp.diag(-1, 1, 1, 1)
dot = lambda u, v: (u.T * etaS * v)[0]
def run_case(q0v, q3v, y0v, m_v):
    alpha = s_ * y0v; sig2 = 1 / (2 * s_ * m_v ** 2)
    var = sig2
    E_Cp = lambda l: (s_ / (2 * y0v)) * (norm * I_sin(l)).subs(beta, alpha)
    E_Cpp = lambda l: (s_ ** 4 / 4) * ((1 / alpha ** 3) * (norm * I_sin(l - 1)).subs(beta, alpha) - (1 / alpha ** 2) * (norm * I_cos(l)).subs(beta, alpha))
    R2 = sp.Symbol('R2', positive=True)
    def angular(expr):
        P = sp.Poly(sp.expand(expr), k0, k1, k2, k3); tot = 0
        df = lambda n: sp.factorial2(n - 1) if n > 0 else 1
        for (a, b, c_, d), co in P.terms():
            if a % 2 or b % 2 or c_ % 2 or d % 2: continue
            n = b + c_ + d
            ang = df(b) * df(c_) * df(d) / sp.factorial2(n + 1) if n > 0 else 1
            tot += co * df(a) * (-var) ** (a // 2) * ang * R2 ** (n // 2)
        return sp.Poly(sp.expand(tot), R2)
    qu = sp.Matrix([-q0v, 0, 0, q3v]); yu = sp.Matrix([y0v, 0, 0, 0]); q2 = dot(qu, qu)
    e1 = sp.Matrix([0, 1, 0, 0]); e2 = sp.Matrix([0, 0, 1, 0]); e3 = sp.Matrix([q3v, 0, 0, -q0v])
    pols = {2: (e1 * e1.T - e2 * e2.T, sp.Integer(0)), 1: (e1 * e3.T + e3 * e1.T, sp.Rational(1, 2)),
            0: (e3 * e3.T - dot(e3, e3) / 2 * (e1 * e1.T + e2 * e2.T), sp.Rational(2, 3))}
    c = sp.Rational(y0v ** 2, m_v ** 2)
    x_ = ((y0v ** 2 - m_v ** 2) * q2 + (y0v * q0v) ** 2) / (-m_v ** 2 * q2)
    nu = (x_ - 1) / c
    ok = []
    for h, (hh, phi) in pols.items():
        u = hh * etaS * kup
        uu = dot(u, u); ku = dot(kup, u); yuu = dot(yu, u); kk = dot(kup, kup); ky = dot(kup, yu); kq = dot(kup, qu); yq = dot(yu, qu); yy_ = dot(yu, yu)
        A2 = angular(q2 * uu / 4); A1s = angular((kq * yuu - ku * yq) ** 2)
        GM = sp.Matrix([[kk, ky, kq, ku], [ky, yy_, yq, yuu], [kq, yq, q2, 0], [ku, yuu, 0, uu]])
        P1s = angular(-GM.det(method='berkowitz'))
        tot = 0
        for (n,), co in A2.terms(): tot += 4 * co * E_Cp(n)
        for form, sg in ((A1s, 1), (P1s, -1)):
            for (n,), co in form.terms():
                if co != 0: tot += 2 * sg * co * E_Cpp(n)
        tot = tot.subs(sig, sp.sqrt(sig2))
        ser1 = sp.limit(sp.simplify(tot / s_), s_, 0)
        unit = ser1 / (-2)
        xiV = s_ * c / 2
        closed = unit * (-2 * s_) * sp.exp(-xiV / 2) * (1 - (1 + nu * phi) * xiV + (sp.Rational(2, 15) + nu * phi / 5) * xiV ** 2)
        ok.append(sp.simplify(tot - closed) == 0)
    return x_, ok
for args in ((sp.Rational(2, 5), sp.Rational(9, 10), 5, 3), (sp.Rational(3, 2), sp.Rational(1, 3), 5, 3), (sp.Rational(1, 7), sp.Rational(4, 3), 13, 5), (sp.Rational(5, 4), sp.Rational(1, 2), 5, 4)):
    x_, ok = run_case(*args)
    print("   q0=%s q3=%s (y0,m)=(%s,%s): x=%s; closed form exact for helicities 2,1,0: %s" % (args[0], args[1], args[2], args[3], x_, ok))
print("   F(M) > 0: F(0) = (16 - 64/5)/c^2 = %.5f at c = 25/9; numeric min over 2000 values of M in [0,1e4]: %.3e" % (Fres(0.0), min(Fres(M_) for M_ in np.logspace(-6, 4, 2000))))

# ---------- (N) ----------
print("\n(N) M*(x): roots of N(M;x) at (y0,y4) = (5,3) for sampled wave-vector classes, first-order T = 1/M^2 and frozen T = F(M); nan = no root in 1e-5 < M < 1e7")
def root(fn, a=1e-5, b=1e7, n=4000):
    ms = np.logspace(np.log10(a), np.log10(b), n); vals = [fn(M_) for M_ in ms]
    out = []
    for i in range(n - 1):
        if vals[i] == 0 or vals[i] * vals[i + 1] < 0:
            out.append(brentq(fn, ms[i], ms[i + 1]))
    return out
xs = [-2.70412, -1.90848, -16/9, -5.0, -50.0, 1.32902, 3.0, 50.0]
print("   x       lambda_L  | n  L/c  M*(first order)  | M*(frozen resummed) ")
for x in xs:
    for n in (30, 300):
        for Lc in (0, 1, 10):
            r1 = root(lambda M_: W_B(M_, n) * lamL(x) + (1 + 24 * Lc) / M_ ** 2)
            r2 = root(lambda M_: W_B(M_, n) * lamL(x) + Fres(M_) + 24 * Lc / M_ ** 2)
            if Lc == 0 or x in (-2.70412, 1.32902):
                print("   %+9.5f %+8.5f | %3d %2d | %s | %s" % (x, lamL(x), n, Lc, ["%.5f" % v for v in r1], ["%.5f" % v for v in r2]))
print("   lambda_L range: q spacelike x <= -l^2/m^2: -(6/5)(2 + 1/x) from %.5f (x=-l^2/m^2) to -12/5 (x -> -inf); q timelike x >= 1: from -18/5 (x=1) to -12/5 (x -> inf)" % lamL(-ell2 / m2))
print("   sign change of lambda_L at x = -1/2, on the leaf only if m^2 >= 2 l^2 (y4^2 >= 2 l^2); e.g. (13,12): l^2 = 25, m^2 = 144, x range includes -1/2, lambda_L(-0.17361) = %.4f" % lamL(-0.17361))
print("   L/c = 0, frozen: scan for a root over n = 2..300, x in a grid, c = 25/9:")
cnt = 0; tested = 0
for n in list(range(2, 31)) + [50, 100, 300]:
    for x in np.concatenate([-np.logspace(np.log10(16 / 9), 4, 15), np.logspace(0.001, 4, 15)]):
        tested += 1
        if len(root(lambda M_: W_B(M_, n) * lamL(x) + Fres(M_), n=400)) > 0: cnt += 1
print("      roots found in %d of %d (n, x) pairs" % (cnt, tested))

# ---------- (P) positivity ----------
print("\n(P) Peierls-Bogoliubov: v^K(s), tau^K(s) >= 0 for random non-commuting Hermitian data (dimension 6 block, vector and 8-dim spinor chirality-summed)")
sxn = np.array([[0, 1], [1, 0]], complex); syn = np.array([[0, -1j], [1j, 0]]); szn = np.diag([1., -1.]).astype(complex); I2n = np.eye(2)
def kron3(a, b, c): return np.kron(np.kron(a, b), c)
g6 = [kron3(sxn, I2n, I2n), kron3(syn, I2n, I2n), kron3(szn, sxn, I2n), kron3(szn, syn, I2n), kron3(szn, szn, sxn), kron3(szn, szn, syn)]
Sig6D = np.array([[0.25 * (g6[a] @ g6[b] - g6[b] @ g6[a]) for b in range(6)] for a in range(6)])
Sig6V = np.zeros((6, 6, 6, 6), complex)
for a in range(6):
    for b in range(6):
        Sig6V[a, b, a, b] += 1; Sig6V[a, b, b, a] -= 1
minv = []
for trial in range(12):
    Nm = 4
    Hr = rng.normal(size=(Nm, Nm)) + 1j * rng.normal(size=(Nm, Nm)); H0 = Hr @ Hr.conj().T
    Fij = np.zeros((6, 6, Nm, Nm), complex)
    for a in range(6):
        for b in range(a + 1, 6):
            A = rng.normal(size=(Nm, Nm)) + 1j * rng.normal(size=(Nm, Nm)); A = A + A.conj().T
            Fij[a, b] = A; Fij[b, a] = -A
    for sv in (0.1, 0.5, 2.0):
        for Sig, name in ((Sig6V, 'v'), (Sig6D, 't')):
            dim = Sig.shape[2]
            Z = sum(1j * np.kron(Sig[a, b], Fij[a, b]) for a in range(6) for b in range(6) if a != b)
            Htot = np.kron(np.eye(dim), H0) + Z
            assert np.allclose(Htot, Htot.conj().T)
            val = np.trace(expm(-sv * Htot)).real - dim * np.trace(expm(-sv * H0)).real
            minv.append(val)
print("   min of index part over %d evaluations: %.4e (non-negative: %s)" % (len(minv), min(minv), min(minv) >= -1e-9))
from scipy.integrate import quad
def m0(x_): return 1.0 if abs(x_) < 1e-12 else -np.expm1(-x_) / x_
def m1n(x_):
    if abs(x_) < 1e-3: return 6 * (1.0 / 6 - x_ / 12 + x_ * x_ / 40)
    e = np.exp(-x_); return 6 * (x_ - 2 + (x_ + 2) * e) / x_ ** 3
print("   B_0 - B_1 = int_0^1 (1 - 6a(1-a)) e^{-xa} da >= 0 for x >= 0: min over grid %.3e (Legendre coefficient of a convex function)" % min(m0(v) - m1n(v) for v in np.logspace(-3, 3, 200)))
print("   c_T(averaged, five) = (1/6)W_R - 2 W_X = (1/6)V + (1/12)T ; c_T^{TT} = (1/6)V0 + (1/12)T0 + (7/30)(V1 - T1) + (7/20)T2 with T2 >= T1: > 0 for non-zero flux")

# ---------- (B) ----------
print("\n(B) commuting fluxes, f1 = f2 + f3: v - tau")
for (a_, b_) in ((0.3, 0.7), (1.1, 0.2), (2.0, 2.0)):
    f = (a_ + b_, a_, b_)
    v = 2 * sum(np.cosh(2 * fi) - 1 for fi in f); tau = 8 * (np.cosh(f[0]) * np.cosh(f[1]) * np.cosh(f[2]) - 1)
    print("   f = %s: v = %.10f, tau = %.10f, difference %.1e" % (f, v, tau, v - tau))

# ---------- (O), (D) ----------
print("\n(O) on-shell limit: exact forms at nearly null q, base (5,3); expected lambda_2 -> -24/5, SC2 -> 2/5")
def forms(y0, y4, qq):
    F = cp12_forms(y0, y4, qq); f = D_forms(F)
    A = lambda k: np.array(f[k].evalf(), dtype=float)[:6, :6]
    Gm = gram(F); E1, E2, trv = cov_span_forms(Gm)
    Ntl = np.array(sp.Matrix.hstack(*trv.nullspace()).evalf(), dtype=float)
    E5 = Ntl.T @ A('EH1') @ Ntl
    ev = lambda Qm: np.sort(sl.eigvals(Ntl.T @ Qm @ Ntl, E5).real)
    return F, ev(A('IX2')), ev(A('SC2'))
for eps_ in (R(1, 10), R(1, 100), R(1, 1000)):
    qq = [R(1), R(0), R(0), 1 + eps_]
    F, ix, sc = forms(5, 3, qq)
    q2 = float(-1 + (1 + eps_) ** 2); x = (16 * q2 + 25) / (-9 * q2)
    print("   q^2 = %.5f x = %.3f: IX2 eigenvalues %s ; closed helicity-2 value %.6f ; SC2 %s ; closed %.6f"
          % (q2, x, np.round(ix, 5).tolist(), -(6 / 5) * (4 + 1 / x), np.round(sc, 5).tolist(), (8 + 1 / x) / 20))

print("\n(D) fibre-point decomposition: X_hat = -4 EH[h_n] + m^-4 q^2 (a.v)^2 at random fibre points, exact rational arithmetic")
okD = True
for trial in range(6):
    y0, y4 = random.choice([(5, 3), (5, 4), (13, 5)])
    qq = [R(random.randint(-5, 5), random.randint(1, 4)) for _ in range(4)]
    m = sp.Integer(y4); etaM = ETA; S, ell = Smodel(y0, y4)
    q = sp.Matrix(qq); s = [Si * q for Si in S]
    D = sp.Matrix(3, 3, lambda i, j: R(random.randint(-3, 3), random.randint(1, 3))); D = D + D.T
    # rational unit vector on the fibre
    u_, v_ = R(random.randint(1, 5), 3), R(random.randint(1, 5), 7)
    den = 1 + u_ ** 2 + v_ ** 2
    n = sp.Matrix([2 * u_ / den, 2 * v_ / den, (1 - u_ ** 2 - v_ ** 2) / den])
    alpha = sum((n[i] * D[i, j] * s[j] for i in range(3) for j in range(3)), sp.zeros(4, 1))
    v = sum((n[j] * s[j] for j in range(3)), sp.zeros(4, 1))
    gamma_bar = m ** 2 * etaM.inv()
    dgamma = m * (alpha * v.T + v * alpha.T)
    Gb = gamma_bar.inv(); dG = -Gb * dgamma * Gb
    eh = EH2(Gb, dG, q)
    q2 = (q.T * etaM.inv() * q)[0]
    aa = (alpha.T * etaM * alpha)[0]; vv = (v.T * etaM * v)[0]; av = (alpha.T * etaM * v)[0]
    Xhat = m ** -4 * q2 * vv * aa
    okD &= sp.simplify(Xhat - (-4 * eh + m ** -4 * q2 * av ** 2)) == 0
print("   identity holds at 6 random fibre points: %s" % okD)

print()
print("(G) algebra of the coefficients on the mass shell, helicity two; V_i, T_i weighted integrals of v^K, tau^K with level weights D, B_1, B_0")
V0, V1, T0, T1, T2, F_ = sp.symbols('V0 V1 T0 T1 T2 F')
WR0 = V0 - T0; WR1 = V1 - T1; WX0 = -T0 / 8; WX2 = -T2 / 8
cTT = sp.Rational(1, 6) * WR0 + sp.Rational(7, 30) * WR1 - 2 * WX0 - sp.Rational(14, 5) * WX2
print("   c_T^TT =", sp.expand(cTT))
print("   averaged c_T =", sp.expand(sp.Rational(1, 6) * WR0 - 2 * WX0))
for name, cA in (('fixed-state, finite mixed part', sp.Rational(1, 6) * WR0 - 2 * WX0), ('periodic', sp.Rational(1, 6) * WR0), ('smooth', -sp.Rational(1, 12) * WR0)):
    print("   %s: c_A - c_T^TT = %s" % (name, sp.expand(cA - cTT)))
print("   R[G] at the background: 18 c - 24, e = 2 - (3/4) c  (see s4 part (D))")
