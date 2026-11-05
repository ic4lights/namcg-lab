"""
s2_duhamel_interpolation.py  (proposal 046)

Second-order Duhamel (proper-time) weights of the one-loop trace over the fibre levels, and the resulting
two-derivative quadratic forms on the six level-one polarisations of CP^{1,2} x K, as functions of the ratio
of the K scale to the fibre gap.  Frozen leading symbol at a base point, as in proposal 045 (forms_lib.py).

Loop modes: phi(y) Y_{Jm}(n), fibre level J with H_0 eigenvalue m^2 k.gbar.k + mu_J (s1: mu_J = J(J+2), units R = 1).
A fluctuation vertex that is a multiplication operator on the fibre, f(n) = f_0 + f_2(n) (harmonic degrees 0, 2),
connects J -> J (f_0, f_2) and J -> J +- 2 (f_2).  For real f, g:
   sum_{m,m'} <Jm|f|J'm'><J'm'|g|Jm> = (2J+1) [ delta_{JJ'} f_0 g_0 + c(J,J') <f_2 g_2> ],
   c(J,J') = <J 0 2 0 | J' 0>^2   (checked against sympy CG; sum over J' = 1).

Part (A): exact Gaussian kernel of the scalar operator -d_mu gamma^{mu nu} d_nu at second order in a cometric wave
h cos(q.y), with the intermediate level shifted by Delta:
   q^2-part  propto  int_0^1 da e^{-s Delta a} [ a(1-a) F1(h) + (1-2a)^2 F2(h) ],
   F1 = -(q.gbar.q) ((tr hG)^2 + 2 tr hGhG)/4 - (q.h.q) tr(hG),   F2 = (q.h.G.h.q)/2,   G = gbar^{-1};
   checked by an independent Isserlis computation, and at Delta = 0 against the a_1 density of forms_lib.scalar_form
   (fixed constant ratio).  The index (torsion) vertex is linear in the loop momentum and already of order q^2, so its
   weight is int_0^1 da e^{-s Delta a} = m0(s Delta).
Part (B): the l = 2 forms on the six polarisations at the seven 045 cases; consistency (1/6)F1 + (1/3)F2 -> SC2 - SC1.
Part (C): fibre weights D(s), B_0(s), B_1(s), B_2(s) and the K-weighted ratios
   beta_X = W_X^(2)/W_X^(0),  beta_R1, beta_R2  (model tau^K, v^K - tau^K proportional to s^2 e^{-s M}),
   for the spectrum J(J+2) and, for comparison, 3J;  fibre truncation n.
Part (D): generalised eigenvalues on the five traceless polarisations of IX1 + beta_X (IX2 - IX1) relative to EH,
   and of the scalar leakage forms, as functions of M.
"""
import sympy as sp, numpy as np, itertools, random
from scipy.integrate import quad
from forms_lib import *

out = []
def P(*a):
    line = " ".join(str(x) for x in a); print(line); out.append(line)
random.seed(46)
def rrat(): return R(random.randint(-6, 6), random.randint(1, 4))

# ---------------- CG coefficients ----------------
from sympy.physics.quantum.cg import CG
def cJJ(J, Jp):
    if Jp < 0: return R(0)
    return sp.nsimplify(CG(J, 0, 2, 0, Jp, 0).doit() ** 2)
def cJJ_closed(J, Jp):
    if Jp == J + 2: return R(3 * (J + 1) * (J + 2), 2 * (2 * J + 1) * (2 * J + 3))
    if Jp == J: return R(J * (J + 1), (2 * J - 1) * (2 * J + 3))
    if Jp == J - 2 and J >= 2: return R(3 * J * (J - 1), 2 * (2 * J - 1) * (2 * J + 1))
    return R(0)
ok = all(sp.simplify(cJJ(J, Jp) - cJJ_closed(J, Jp)) == 0 for J in range(0, 7) for Jp in range(0, 9))
sums = [sp.simplify(sum(cJJ_closed(J, Jp) for Jp in range(J - 2, J + 3))) for J in range(0, 7)]
P("(CG) c(J,J') = <J0 20|J'0>^2: closed forms agree with sympy for J <= 6: %s; sum over J' = %s" % (ok, sums))

# ---------------- (A) Gaussian kernel ----------------
P("\n(A) second-order kernel of -d gamma d with an intermediate-level shift")
a = sp.Symbol('a', nonnegative=True); ssym = sp.Symbol('s', positive=True)
def F1F2(gb, h, q):
    G = gb.inv()
    qgq = (q.T * gb * q)[0]; qhq = (q.T * h * q)[0]
    trhG = (h * G).trace(); T1 = trhG ** 2 + 2 * (h * G * h * G).trace()
    qhGhq = (q.T * h * G * h * q)[0]
    return -qgq * T1 / 4 - qhq * trhG, qhGhq / 2
def isserlis_q2(gb, h, q):
    """independent: shift k = p - a q, Gaussian in p with <p p> = G/(2s), expand e^{-s a(1-a) q.gb.q} and the
       polynomial to order q^2 (tag q by eps)."""
    eps = sp.Symbol('eps'); p = sp.symbols('p0:4'); pv = sp.Matrix(p)
    G = gb.inv()
    k = pv - a * eps * q; kq = k + eps * q
    poly = sp.expand(((kq.T * h * k)[0]) ** 2 * (1 - eps ** 2 * ssym * a * (1 - a) * (q.T * gb * q)[0]))
    poly = sp.expand(poly).coeff(eps, 2)
    # Isserlis for monomials in p with covariance C = G/(2s)
    C = G / (2 * ssym)
    Pp = sp.Poly(poly, *p)
    tot = 0
    for mon, co in Pp.terms():
        idx = [i for i in range(4) for _ in range(mon[i])]
        if len(idx) % 2: continue
        def pairings(lst):
            if not lst: yield []; return
            f = lst[0]
            for j in range(1, len(lst)):
                rest = lst[1:j] + lst[j + 1:]
                for pr in pairings(rest): yield [(f, lst[j])] + pr
        val = 0
        for pr in pairings(idx):
            v = 1
            for (i, j) in pr: v *= C[i, j]
            val += v
        tot += co * val
    return sp.simplify(tot)
for trial in range(2):
    gb = sp.diag(*[rrat() ** 2 + 1 for _ in range(4)]) if trial == 0 else sp.diag(-R(4), R(9, 4), R(1), R(16, 9))
    gb[0, 1] = gb[1, 0] = R(1, 3) if trial == 0 else 0
    h = sp.zeros(4, 4)
    for i in range(4):
        for j in range(i, 4): h[i, j] = h[j, i] = rrat()
    q = sp.Matrix([rrat() for _ in range(4)])
    f1, f2 = F1F2(gb, h, q)
    lhs = isserlis_q2(gb, h, q)
    rhs = (a * (1 - a) * f1 + (1 - 2 * a) ** 2 * f2) / ssym
    P("   draw %d (%s gbar): Isserlis q^2 coefficient = [a(1-a) F1 + (1-2a)^2 F2]/s exactly: %s"
      % (trial, 'Euclidean' if trial == 0 else 'Lorentzian', sp.simplify(sp.expand(lhs - rhs)) == 0))
# calibration against the a_1 density of forms_lib at Delta = 0: (1/6)F1 + (1/3)F2 versus scalar_form
ratios = []
for trial in range(4):
    if trial < 2:
        gb = sp.diag(*[rrat() ** 2 + 1 for _ in range(4)])
    else:
        gb = sp.diag(-R(random.randint(1, 5)), R(random.randint(1, 5)), R(random.randint(1, 5)), R(random.randint(1, 5)))
    h = sp.zeros(4, 4)
    for i in range(4):
        for j in range(i, 4): h[i, j] = h[j, i] = rrat()
    q = sp.Matrix([rrat() for _ in range(4)])
    f1, f2 = F1F2(gb, h, q)
    sc, eh = scalar_form(gb, h, q)
    lhs = (R(1, 6) * f1 + R(1, 3) * f2) / sp.sqrt(sp.Abs(gb.det()))
    ratios.append(sp.nsimplify(sp.simplify(sc / lhs)))
P("   a_1 density (forms_lib.scalar_form) / [((1/6)F1 + (1/3)F2)/sqrt|det gbar|] at 4 draws (2 Euclidean, 2 Lorentzian): %s" % ratios)
KAPPA = ratios[0]
assert all(r == KAPPA for r in ratios)

# ---------------- (B) l = 2 forms at the 045 cases ----------------
P("\n(B) l = 2 (second fibre harmonic) forms on the six polarisations, inert amplitudes set to zero")
cases = [((5, 3), [R(3, 7), R(1, 2), R(-2, 3), R(1, 5)], 1),
         ((5, 3), [R(-1, 3), R(2, 5), R(1, 4), R(-3, 2)], 1),
         ((5, 3), [R(2, 1), R(1, 3), R(-1, 2), R(1, 4)], 1),
         ((13, 5), [R(2, 3), R(-1, 2), R(1, 3), R(1, 7)], 1),
         ((5, 4), [R(1, 9), R(3, 4), R(-1, 2), R(2, 3)], 1),
         ((-5, 3), [R(3, 7), R(1, 2), R(-2, 3), R(1, 5)], 1),
         ((-5, 3), [R(3, 7), R(1, 2), R(-2, 3), R(1, 5)], -1)]
Es, Ea = sym_ant_basis()
Bsym = sp.Matrix.hstack(*[sp.Matrix(list(M)) for M in Es])
store = []
for (y0, y4), qq, chi in cases:
    F = cp12_forms(y0, y4, qq, chi=chi)
    sub0 = {g: 0 for g in F['gv']}
    gb = F['m'] ** 2 * ETA.inv()
    h2 = (F['dgamma'] - F['dgbar']).subs(sub0).applyfunc(sp.expand)
    f1, f2 = F1F2(gb, h2, F['q'])
    pref = KAPPA / sp.sqrt(sp.Abs(gb.det()))
    L1 = fibre_avg(sp.expand(pref * R(1, 6) * f1)); L2 = fibre_avg(sp.expand(pref * R(1, 3) * f2))
    to6 = lambda Q: (Bsym.T * quad_matrix(sp.expand(Q.subs(sub0)), list(F['Dv'])) * Bsym).applyfunc(sp.expand)
    f = D_forms(F)
    SC2, SC1, IX2, IX1, EH = f['SC2'][:6, :6], f['SC1'][:6, :6], f['IX2'][:6, :6], f['IX1'][:6, :6], f['EH1'][:6, :6]
    M1, M2 = to6(L1), to6(L2)
    cons = (M1 + M2 - (SC2 - SC1)).applyfunc(sp.simplify).is_zero_matrix
    G = gram(F); E1, E2, trv = cov_span_forms(G)
    Ntl = sp.Matrix.hstack(*trv.nullspace())
    r5 = lambda Q: Ntl.T * Q * Ntl
    E5 = r5(EH)
    ev = lambda Q: ["%.5g" % z.real for z in gen_eigs(r5(Q), E5)]
    LX = IX2 - IX1
    P("  case %s q=%s chi=%d: (1/6)L_F1 + (1/3)L_F2 = SC2 - SC1 exactly: %s" % ((y0, y4), [str(x) for x in qq], chi, cons))
    P("     generalised eigenvalues on the five traceless polarisations, relative to EH(hbar): IX2-IX1: %s ; scalar F1-leak: %s ; scalar F2-leak: %s"
      % (ev(LX), ev(M1), ev(M2)))
    store.append(dict(case=((y0, y4), chi), LX=LX, M1=M1, M2=M2, EH=EH, IX1=IX1, SC1=SC1, Ntl=Ntl, E5=E5))

# ---------------- (C) fibre weights and K-weighted ratios ----------------
P("\n(C) fibre weights and K-weighted ratios; model tau^K(s) and (v^K - tau^K)(s) proportional to s^2 exp(-s M)")
def m0(x):
    return 1.0 if abs(x) < 1e-12 else -np.expm1(-x) / x
def m1n(x):   # int a(1-a) e^{-xa} da, normalised by 1/6
    if abs(x) < 1e-3: return 6 * (1.0 / 6 - x / 12 + x * x / 40)
    e = np.exp(-x)
    val = (x - 2 + (x + 2) * e) / x ** 3
    return 6 * val
def m2n(x):   # int (1-2a)^2 e^{-xa} da, normalised by 1/3
    if abs(x) < 1e-3: return 3 * (1.0 / 3 - x / 6 + x * x / 15)
    e = np.exp(-x)
    val = ((x * x - 4 * x + 8) - (x * x + 4 * x + 8) * e) / x ** 3
    return 3 * val
# check moment closed forms by quadrature
for x in (0.3, 2.0, 15.0, -1.5):
    q1 = quad(lambda t: t * (1 - t) * np.exp(-x * t), 0, 1)[0] * 6
    q2 = quad(lambda t: (1 - 2 * t) ** 2 * np.exp(-x * t), 0, 1)[0] * 3
    q0 = quad(lambda t: np.exp(-x * t), 0, 1)[0]
    assert abs(q1 - m1n(x)) < 1e-9 and abs(q2 - m2n(x)) < 1e-9 and abs(q0 - m0(x)) < 1e-12, (x, q1, m1n(x), q2, m2n(x))
P("   moment functions m0, m1, m2 (closed forms) agree with quadrature at x = 0.3, 2, 15, -1.5")
cnum = {}
def cJJf(J, Jp):
    key = (J, Jp)
    if key not in cnum: cnum[key] = float(cJJ_closed(J, Jp))
    return cnum[key]
def weights(s, mu, nmax):
    """D = sum_J (2J+1) e^{-s mu_J};  B_i = sum_{J,J'} (2J+1) c(J,J') int_0^1 da w_i(a) e^{-s((1-a) mu_J + a mu_J')},
       normalised so that B_i = D for degenerate levels; w_0 = 1, w_1 = 6 a(1-a), w_2 = 3 (1-2a)^2 (all symmetric under
       a -> 1-a, so the integral is e^{-s min(mu_J, mu_J')} m_i(s |mu_J' - mu_J|), evaluated in that stable form)."""
    Dd = 0.0; B0 = B1 = B2 = 0.0
    for J in range(nmax + 1):
        Dd += (2 * J + 1) * np.exp(-s * mu(J))
        for Jp in (J - 2, J, J + 2):
            if Jp < 0 or Jp > nmax: continue
            c = cJJf(J, Jp)
            if c == 0: continue
            lo = min(mu(J), mu(Jp)); x = s * abs(mu(Jp) - mu(J))
            w = (2 * J + 1) * c * np.exp(-s * lo)
            B0 += w * m0(x); B1 += w * m1n(x); B2 += w * m2n(x)
    return Dd, B0, B1, B2
specs = {'J(J+2)': lambda J: J * (J + 2), '3J': lambda J: 3 * J}
nmax = 30
Mgrid = [0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 8.0, 30.0, 100.0, 1000.0, 1e4]
betas = {}
for name, mu in specs.items():
    P("   spectrum mu_J = %s, fibre truncation n = %d (beta = W^(2)/W^(0); 1 = trace reading, 0 = averaged frame):" % (name, nmax))
    for M in Mgrid:
        def integ(k):
            f = lambda s: s ** -2 * (s ** 2 * np.exp(-s * M)) * weights(s, mu, nmax)[k]
            return quad(f, 0, np.inf, limit=400)[0]
        W0, W2, W1r, W2r = integ(0), integ(1), integ(2), integ(3)
        betas[(name, M)] = (W2 / W0, W1r / W0, W2r / W0)
        approx = (M / 8) * np.log(1 + 8 / M) if name == 'J(J+2)' else (M / 6) * np.log(1 + 6 / M)
        P("      M = m_K^2 = %-7g beta_X = %.5f (J=0 channel only: (M/mu_2) ln(1+mu_2/M) = %.5f) ; beta_R1 = %.5f ; beta_R2 = %.5f"
          % (M, W2 / W0, approx, W1r / W0, W2r / W0))

# ---------------- (D) five traceless polarisations ----------------
P("\n(D) index part: generalised eigenvalues of IX1 + beta_X (IX2 - IX1) relative to EH on the five traceless polarisations (case 1)")
st = store[0]
ev = lambda Q: sorted([z.real for z in gen_eigs(st['Ntl'].T * Q * st['Ntl'], st['E5'])])
lam = ev(st['LX'])
for M in Mgrid:
    b = betas[('J(J+2)', M)][0]
    e = [-2 + b * l for l in lam]
    P("   M = %-7g beta_X = %.4f: eigenvalues %s ; spread (max - min)/2 = %.4f" % (M, b, ["%.4f" % x for x in e], (max(e) - min(e)) / 2))
P("   (eigenvalues of IX2 - IX1 relative to EH on the five: %s; the spread is beta_X times %.4f/2)" % (["%.4f" % x for x in lam], max(lam) - min(lam)))
open(__file__.replace('.py', '.out.txt'), 'w').write("\n".join(out) + "\n")
