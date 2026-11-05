"""
s4_window_scan.py  (proposal 046)

Combines s2 (Duhamel fibre weights) and s3 (background torsion) on the five traceless level-one polarisations.

(S) Structure.  At the sampled cases, every correction form computed in this package lies, on the five traceless
    polarisations, in the two-dimensional span of EH(hbar) and one further form H2: the second-harmonic leakage of the
    index form L_X = IX2 - IX1, the scalar leakages (F1 part of s2; the F2 part vanishes there), the mixed-term
    background-torsion correction Q2_D/m^4 and the first-term base-torsion form P2/m^4 = (Q2_V - 2 Q2_D)/m^4.  Tested
    by least squares against {Q2_D/m^4, EH} (residual reported).  Equivalently, each form's generalised eigenvalue
    relative to EH is affine in the square of the helicity about the spatial direction of q (h = 0, 1, 2).
(N) Non-Einstein coefficient.  With tau^K = F^2 s^2 e^{-sM}, s0^K = e^{-sM} per K mode, F^2 = c M^2, and the weights
       index form / m^4 = W1 [ IX1 + beta_X L_X ] + W2 Q2_D/m^4 - 4 (L/F^2) P2/m^4      (units 1/(128 pi^2) F^2),
       W1 = sum_J (2J+1)/(M + mu_J),  W2 = 1/M^2 (J = 0 loop modes only),  L = int ds/s s0^K (logarithmic, a parameter),
    the coefficient of H2 on the five is N(M) = W1 beta_X lambda_L + W2 + 24 (L/c) M^-2 (lambda_L, -1/6 from (S)).
    Reported: the sign of N at small and large M, the zero M* for L/c = 0, 1, 10, and at M* the size of the expansion
    parameters (beta_X; torsion weight W2/W1, to be compared with the first-order truncation).
"""
import numpy as np, sympy as sp, scipy.linalg as sl
from forms_lib import *
import importlib.util, sys, os
here = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(here, 's3_background_torsion.py')).read().split("cases = [")[0].split('"""', 2)[2])   # representations and helpers
out = []
def P(*a):
    line = " ".join(str(x) for x in a); print(line); out.append(line)


# reuse the closed forms of s2 (weights) without rerunning its symbolic parts
from scipy.integrate import quad
def cJJ_closed(J, Jp):
    if Jp == J + 2: return 3 * (J + 1) * (J + 2) / (2 * (2 * J + 1) * (2 * J + 3))
    if Jp == J: return J * (J + 1) / ((2 * J - 1) * (2 * J + 3))
    if Jp == J - 2 and J >= 2: return 3 * J * (J - 1) / (2 * (2 * J - 1) * (2 * J + 1))
    return 0.0
def W_index(M, mu, n):
    """analytic K-weighted fibre sums for tau^K = s^2 e^{-sM}:
       W1 = sum_J (2J+1)/(M+mu_J);
       W1 beta_X = sum_{J,J'} (2J+1) c(J,J') int_0^inf ds e^{-s(M+lo)} m0(s|Delta|)
                 = sum (2J+1) c (1/|Delta|) ln(1 + |Delta|/(M+lo))   (Delta != 0),  1/(M+lo)  (Delta = 0)."""
    W1 = 0.0; WB = 0.0
    for J in range(n + 1):
        W1 += (2 * J + 1) / (M + mu(J))
        for Jp in (J - 2, J, J + 2):
            if Jp < 0 or Jp > n: continue
            c = cJJ_closed(J, Jp)
            if c == 0: continue
            lo = min(mu(J), mu(Jp)); d = abs(mu(Jp) - mu(J))
            WB += (2 * J + 1) * c * (np.log1p(d / (M + lo)) / d if d > 0 else 1.0 / (M + lo))
    return W1, WB / W1
# cross-check the analytic sum against direct quadrature of the s2 weights at two values
def m0(x): return 1.0 if abs(x) < 1e-12 else -np.expm1(-x) / x
def num_beta(M, mu, n):
    def B(s):
        Dd = 0.0; B0 = 0.0
        for J in range(n + 1):
            Dd += (2 * J + 1) * np.exp(-s * mu(J))
            for Jp in (J - 2, J, J + 2):
                if Jp < 0 or Jp > n: continue
                c = cJJ_closed(J, Jp)
                if c == 0: continue
                lo = min(mu(J), mu(Jp)); x = s * abs(mu(Jp) - mu(J))
                B0 += (2 * J + 1) * c * np.exp(-s * lo) * m0(x)
        return Dd, B0
    W1 = quad(lambda s: np.exp(-s * M) * B(s)[0], 0, np.inf, limit=400)[0]
    WB = quad(lambda s: np.exp(-s * M) * B(s)[1], 0, np.inf, limit=400)[0]
    return W1, WB / W1
specs = {'J(J+2)': lambda J: J * (J + 2), '3J': lambda J: 3 * J}
for M in (0.1, 3.0):
    a1 = W_index(M, specs['J(J+2)'], 30); a2 = num_beta(M, specs['J(J+2)'], 30)
    P("check: analytic K-weighted sums vs quadrature at M = %g, n = 30: W1 %.6f / %.6f, beta_X %.6f / %.6f" % (M, a1[0], a2[0], a1[1], a2[1]))

# ---------------- forms at a case ----------------
etaN = np.diag([-1., 1, 1, 1])
def forms_at(y0, y4, qq, chi=1):
    F = cp12_forms(y0, y4, qq, chi=chi)
    sub0 = {g: 0 for g in F['gv']}
    m = float(F['m']); G = etaN / m ** 2
    ybv = np.array([float(y0), 0., 0., 0.])
    Tbar = np.zeros((4, 4, 4))
    for a_ in range(4):
        for b_ in range(4):
            for mu in range(4):
                Tbar[a_, b_, mu] = etaN[a_, mu] * ybv[b_] - etaN[b_, mu] * ybv[a_]
    Es, Ea = sym_ant_basis(); Dv = list(F['Dv'])
    lin = [np.array([[[float(sp.expand(F['dTbar'][a_][b_][mu].subs(sub0).subs(dict(zip(Dv, list(M_))))))
                       for mu in range(4)] for b_ in range(4)] for a_ in range(4)]) for M_ in Es]
    dT_of = lambda D: sum(D[p] * lin[p] for p in range(6))
    Q2D = quad_form(lambda D: Q2(Zmats(Tbar + dT_of(D), SigD), G), 6).real
    Q2V = quad_form(lambda D: Q2(Zmats(Tbar + dT_of(D), SigV), G), 6).real
    f = D_forms(F)
    EH = np.array(f['EH1'][:6, :6].evalf(), dtype=float)
    IX1 = np.array(f['IX1'][:6, :6].evalf(), dtype=float); IX2 = np.array(f['IX2'][:6, :6].evalf(), dtype=float)
    Gm = gram(F); E1, E2, trv = cov_span_forms(Gm)
    Ntl = np.array(sp.Matrix.hstack(*trv.nullspace()).evalf(), dtype=float)
    gbS = F['m'] ** 2 * ETA.inv(); Gs = gbS.inv(); qS = F['q']
    h2 = (F['dgamma'] - F['dgbar']).subs(sub0).applyfunc(sp.expand)
    trhG = (h2 * Gs).trace(); T1 = trhG ** 2 + 2 * (h2 * Gs * h2 * Gs).trace()
    F1 = -(qS.T * gbS * qS)[0] * T1 / 4 - (qS.T * h2 * qS)[0] * trhG
    L1 = fibre_avg(sp.expand(R(1, 4) / sp.sqrt(sp.Abs(gbS.det())) * R(1, 6) * F1))
    Bsym = sp.Matrix.hstack(*[sp.Matrix(list(M_)) for M_ in Es])
    M1 = np.array((Bsym.T * quad_matrix(L1, Dv) * Bsym).evalf(), dtype=float)
    SCd = np.array((f['SC2'][:6, :6] - f['SC1'][:6, :6]).evalf(), dtype=float)
    return dict(M1=M1, SCd=SCd, EH=EH, IX1=IX1, LX=IX2 - IX1, Q2=Q2D / m ** 4, P2=(Q2V - 2 * Q2D) / m ** 4, Ntl=Ntl, coth2=(y0 / y4) ** 2)
def dev(Qm, d):
    z = sl.eigvals(d['Ntl'].T @ Qm @ d['Ntl'], d['Ntl'].T @ d['EH'] @ d['Ntl']).real
    return (z.max() - z.min()) / (2 * abs(z.mean())), np.sort(z)

def span_test(d, key):
    N = d['Ntl']; E5 = N.T @ d['EH'] @ N; Q5 = N.T @ d['Q2'] @ N; X5 = N.T @ d[key] @ N
    A = np.stack([Q5.flatten(), E5.flatten()], 1)
    sol = np.linalg.lstsq(A, X5.flatten(), rcond=None)[0]
    return sol, np.linalg.norm(A @ sol - X5.flatten()) / np.linalg.norm(X5)
cases = [((5, 3), [R(3, 7), R(1, 2), R(-2, 3), R(1, 5)]), ((5, 3), [R(-1, 3), R(2, 5), R(1, 4), R(-3, 2)]),
         ((5, 3), [R(2, 1), R(1, 3), R(-1, 2), R(1, 4)]), ((13, 5), [R(2, 3), R(-1, 2), R(1, 3), R(1, 7)]),
         ((5, 4), [R(1, 9), R(3, 4), R(-1, 2), R(2, 3)]), ((25, 7), [R(3, 7), R(1, 2), R(-2, 3), R(1, 5)]),
         ((17, 15), [R(3, 7), R(1, 2), R(-2, 3), R(1, 5)])]
P("\n(S) on the five traceless polarisations: X = a Q2_D/m^4 + b EH  (least squares; relative residual)")
data = []
for (y0, y4), qq in cases:
    d = forms_at(y0, y4, qq)
    row = []
    for key in ('LX', 'P2', 'M1', 'SCd'):
        sol, r = span_test(d, key)
        row.append((key, sol, r))
    data.append(((y0, y4), qq, d, row))
    P("  (y0,y4)=(%d,%d) q=%s coth^2=%.4f: " % (y0, y4, [str(x) for x in qq], d['coth2'])
      + " ; ".join("%s: a=%.6g b=%.6g res=%.1e" % (k, s[0], s[1], r) for k, s, r in row))
    z = sl.eigvals(d['Ntl'].T @ d['Q2'] @ d['Ntl'], d['Ntl'].T @ d['EH'] @ d['Ntl']).real
    zs = np.sort(z)
    P("     Q2_D/m^4 relative to EH: %s (pattern: one singlet h = 0 and two doublets h = 1, 2; affine in h^2 iff d2 - d0 = 4 (d1 - d0))" % np.round(zs, 6).tolist())

P("\n(N) coefficient of the non-Einstein form on the five, case (5,3), q = (3/7,1/2,-2/3,1/5); spectrum J(J+2)")
(_, _, d, row) = data[0]
lamL = row[0][1][0]; lamP = row[1][1][0]
P("   lambda_L = %.6f (L_X = lambda_L Q2hat + ...), lambda_P = %.6f (P2hat = lambda_P Q2hat + ...)" % (lamL, lamP))
grid = np.logspace(-3, 3, 241)
for n in (2, 30, 300):
    for Lc in (0.0, 1.0, 10.0):
        Ns = []
        for M in grid:
            W1, b = W_index(M, lambda J: J * (J + 2), n)
            W2 = 1.0 / M ** 2
            Ns.append((W1 * b * lamL + W2 - 4 * Lc / M ** 2 * lamP) / W1)
        Ns = np.array(Ns)
        sc = np.where(np.sign(Ns[:-1]) != np.sign(Ns[1:]))[0]
        if len(sc):
            k = sc[0]; Ms = grid[k]
            W1, b = W_index(Ms, lambda J: J * (J + 2), n)
            P("   n = %-3d L/c = %-4g: N/W1 at M = 1e-3: %+.3g, at M = 1e3: %+.3g; zero at M* = %.3g with beta_X = %.3f, torsion weight W2/W1 = %.3f, s-expansion parameter coth^2 tau / M* = %.3g"
              % (n, Lc, Ns[0], Ns[-1], Ms, b, (1 / Ms ** 2) / W1, d['coth2'] / Ms))
        else:
            P("   n = %-3d L/c = %-4g: N/W1 at M = 1e-3: %+.3g, at M = 1e3: %+.3g; no zero on the grid" % (n, Lc, Ns[0], Ns[-1]))
open(__file__.replace('.py', '.out.txt'), 'w').write("\n".join(out) + "\n")
