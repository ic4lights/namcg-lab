"""
s1_lie_poisson_torsion.py  (proposal 045)

Direct Lie-Poisson check, on the explicit realisation of the coadjoint orbit CP^{1,2} of SO(4,2)
(cp12_realisation.py, copied from proposals/013), of the leading-symbol frame and torsion of the
level-one amplitudes, and of the fibre moments used in s2.

Setting (merged Appendix H, conjugate-coordinate class): matrices X^a = T^a + eps A^a, T^a = M^{a4}
(R = 1), base functions y^mu = M^{mu5}, frame E^{a mu} = {X^a, y^mu}, flux F^{ab} = {X^a, X^b},
torsion T^{ab mu} = {F^{ab}, y^mu}.  Level-one amplitudes A^a = sum_i c_i^a e^i exp(i lam q.y), with e^i
the three fibre first harmonics, defined as linear functions of M^{mu rho} (mu,rho <= 3) frozen at the
base point and whitened so that <e^i e^j>_fibre = delta^{ij}; M^{mu rho} = sum_i e^i S_i^{mu rho} on the
base fibre.

Brackets are computed exactly in the polynomial Lie-Poisson algebra (sympy), the factor exp(i lam q.y)
being differentiated by the chain rule; the result is evaluated at numerical orbit points of one fibre.

Checks:
 (A) bracket sign s of the realisation; {T^a, y^mu} = s eta^{a mu} M^{45}; background torsion
     {F^{ab}, y^mu} = eta^{a mu} y^b - eta^{b mu} y^a (fibre independent).
 (B) leading symbols (highest power of lam):
       dE^{a mu}  = k1 * sum_ij e^i e^j c_i^a s_j^mu              (order lam^1)
       dF^{ab}    = k3 * m * sum_i e^i (q^a c_i^b - q^b c_i^a)     (order lam^1),  m = M^{45}
       dT^{ab mu} = k2 * m * sum_ij e^i e^j s_j^mu K_i^{ab}        (order lam^2),  K_i^{ab} = q^a c_i^b - q^b c_i^a
     with s_j^mu = S_j^{mu nu} q_nu, q^a = eta^{a mu} q_mu; constants k1,k2,k3 fitted once, residual reported.
 (C) fibre moments: <e^i e^j e^k e^l> = (3/5)(d^ij d^kl + d^ik d^jl + d^il d^jk) for whitened e (isotropy),
     Monte Carlo over the stabiliser (Haar), and <e^i> = 0.
"""
import numpy as np, sympy as sp
from cp12_realisation import Mfun, PB, lie, eta6, Sig, point_at_rest
from scipy.linalg import expm

rng = np.random.default_rng(45)
out = []
def P(*a):
    line = " ".join(str(x) for x in a); print(line); out.append(line)

# ---------------- orbit points of one fibre ----------------
n = 8.0
z0, resid = point_at_rest(n=n, seed=3)
beta = -np.arctanh(3.0 / 5.0)
Ub = expm(1j * beta * Sig[0, 4])
gens = [(a, b) for a in range(1, 5) for b in range(a + 1, 5)]
def rand_rot():
    U = np.eye(4, dtype=complex)
    for k in range(6):
        for (a, b) in gens:
            U = expm(1j * rng.uniform(0, 2 * np.pi) * Sig[a, b]) @ U
    return U
def fibre_point():
    return Ub @ rand_rot() @ z0

zb = fibre_point(); Mb = Mfun(zb)
yb = Mb[:5, 5]
P("base point y^A = M^{A5} =", np.round(yb, 10), "; ell^2 = -y.y =", round(-(yb @ np.diag([-1, 1, 1, 1, 1]) @ yb), 8))

# (A) bracket sign
sgn = None
for (A, B, C, D) in [(0, 4, 1, 4), (1, 2, 2, 3), (0, 5, 1, 5), (0, 1, 1, 4)]:
    num = PB(A, B, C, D, zb); ref = lie(A, B, C, D, Mb)
    if abs(ref) > 1e-6:
        r = num / ref
        sgn = r if sgn is None else sgn
        P("  {M^%d%d, M^%d%d} / lie(...) = %.12f" % (A, B, C, D, r))
s_br = int(round(sgn))
P("bracket sign s =", s_br)

# ---------------- sympy Lie-Poisson engine ----------------
syms = {}
for A in range(6):
    for B in range(A + 1, 6):
        syms[(A, B)] = sp.Symbol('M%d%d' % (A, B))
def Ms(A, B):
    if A == B: return sp.Integer(0)
    return syms[(A, B)] if A < B else -syms[(B, A)]
eta = [-1, 1, 1, 1, 1, -1]
def lieS(A, B, C, D):
    e = lambda X, Y: eta[X] if X == Y else 0
    return s_br * (e(A, C) * Ms(B, D) - e(A, D) * Ms(B, C) - e(B, C) * Ms(A, D) + e(B, D) * Ms(A, C))
pairs = sorted(syms.keys())
STRUCT = {(p1, p2): lieS(*p1, *p2) for p1 in pairs for p2 in pairs}

lam = sp.Symbol('lam'); Ex = sp.Symbol('Ex')
qsym = sp.symbols('q0:4')
phi = sum(qsym[mu] * Ms(mu, 5) for mu in range(4))
def D(f, p):
    """derivative along M_p, Ex = exp(i lam phi) treated by the chain rule"""
    return sp.diff(f, syms[p]) + sp.diff(f, Ex) * sp.I * lam * Ex * sp.diff(phi, syms[p])
def br(f, g):
    df = {p: D(f, p) for p in pairs}; dg = {p: D(g, p) for p in pairs}
    tot = 0
    for p1 in pairs:
        if df[p1] == 0: continue
        for p2 in pairs:
            if dg[p2] == 0: continue
            st = STRUCT[(p1, p2)]
            if st != 0: tot += df[p1] * dg[p2] * st
    return sp.expand(tot)

etam = np.diag([-1., 1, 1, 1])
# check {T^a, y^mu} and background torsion symbolically
Tm = [Ms(a, 4) for a in range(4)]; ym = [Ms(mu, 5) for mu in range(4)]
ok = True
for a in range(4):
    for mu in range(4):
        v = sp.simplify(br(Tm[a], ym[mu]) - s_br * etam[a, mu] * Ms(4, 5))
        ok &= (v == 0)
P("(A) {T^a, y^mu} = s eta^{a mu} M^{45} exactly:", ok)
ok = True
Fbar = [[br(Tm[a], Tm[b]) for b in range(4)] for a in range(4)]
for a in range(4):
    for b in range(4):
        for mu in range(4):
            v = sp.simplify(br(Fbar[a][b], ym[mu]) - (etam[a, mu] * ym[b] - etam[b, mu] * ym[a]))
            ok &= (v == 0)
P("(A) background torsion {F^{ab}, y^mu} = eta^{a mu} y^b - eta^{b mu} y^a exactly (fibre independent):", ok)

# ---------------- fibre harmonics e^i at this base point ----------------
idx6 = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
def boosted_fibre(N):
    pts = []
    for t in range(N):
        pts.append(Ub @ rand_rot() @ z0)
    return pts
samp = boosted_fibre(4000)
W6 = np.array([[Mfun(z)[i, j] for (i, j) in idx6] for z in samp])
Ysamp = np.array([Mfun(z)[:5, 5] for z in samp])
P("fibre check: max |y(z) - y_b| over samples = %.2e" % np.abs(Ysamp - yb).max())
U_, sv, Vh = np.linalg.svd(W6, full_matrices=False)
P("singular values of the fibre samples of M^{mu rho} (expect 3 nonzero):", np.round(sv / sv[0], 8))
Bas = Vh[:3]                          # 3 x 6 orthonormal rows spanning W_y
w3 = W6 @ Bas.T                       # coordinates in W_y
# the fibre is an orbit of the compact stabiliser acting linearly on W_y: its points lie on the ellipsoid
# w^T Qm w = 1 of the invariant form; fit Qm exactly (least squares on 4000 points) and use e = sqrt(3) Qm^{1/2} w
rows = np.array([[w[0]*w[0], w[1]*w[1], w[2]*w[2], 2*w[0]*w[1], 2*w[0]*w[2], 2*w[1]*w[2]] for w in w3])
qv = np.linalg.lstsq(rows, np.ones(len(w3)), rcond=None)[0]
Qm = np.array([[qv[0], qv[3], qv[4]], [qv[3], qv[1], qv[5]], [qv[4], qv[5], qv[2]]])
P("invariant quadric fit: max |w^T Q w - 1| = %.2e" % np.abs(np.einsum('ni,ij,nj->n', w3, Qm, w3) - 1).max())
evals, evecs = np.linalg.eigh(Qm)
Lw = np.sqrt(3.0) * evecs @ np.diag(evals ** 0.5) @ evecs.T @ Bas        # e = Lw . M6, 3 x 6, |e|^2 = 3
Bmat = np.linalg.pinv(Lw)                           # M6 = Bmat . e  on W_y
S = []
for i in range(3):
    Si = np.zeros((4, 4))
    for k, (mu, rho) in enumerate(idx6):
        Si[mu, rho] = Bmat[k, i]; Si[rho, mu] = -Bmat[k, i]
    S.append(Si)
# exact-on-fibre reconstruction check
res = max(np.abs(np.array([Mfun(z)[i, j] for (i, j) in idx6]) - Bmat @ (Lw @ np.array([Mfun(z)[i, j] for (i, j) in idx6]))).max() for z in samp[:200])
P("reconstruction M^{mu rho} = sum_i e^i S_i^{mu rho} on the fibre: max residual %.2e" % res)

esym = [sum(Lw[i, k] * Ms(*idx6[k]) for k in range(6)) for i in range(3)]

# ---------------- (B) leading symbols ----------------
csym = [[sp.Symbol('c%d_%d' % (i, a)) for a in range(4)] for i in range(3)]
A = [sum(csym[i][a] * esym[i] for i in range(3)) * Ex for a in range(4)]
dE = [[br(A[a], ym[mu]) for mu in range(4)] for a in range(4)]
dF = [[sp.expand(br(Tm[a], A[b]) + br(A[a], Tm[b])) for b in range(4)] for a in range(4)]
dT = [[[br(dF[a][b], ym[mu]) for mu in range(4)] for b in range(4)] for a in range(4)]

def coeff(expr, k):
    return sp.expand(expr.subs(Ex, 1)).coeff(lam, k)
lead_E = [[coeff(dE[a][mu], 1) for mu in range(4)] for a in range(4)]
lead_F = [[coeff(dF[a][b], 1) for b in range(4)] for a in range(4)]
lead_T = [[[coeff(dT[a][b][mu], 2) for mu in range(4)] for b in range(4)] for a in range(4)]
P("(B) highest lam power: dE has lam^2 terms:", any(coeff(dE[a][mu], 2) != 0 for a in range(4) for mu in range(4)),
  "; dT has lam^3 terms:", any(coeff(dT[a][b][mu], 3) != 0 for a in range(4) for b in range(4) for mu in range(4)))

fE = sp.lambdify([list(syms.values()), qsym, [c for row in csym for c in row]], lead_E, 'numpy')
fF = sp.lambdify([list(syms.values()), qsym, [c for row in csym for c in row]], lead_F, 'numpy')
fT = sp.lambdify([list(syms.values()), qsym, [c for row in csym for c in row]], lead_T, 'numpy')
keys = list(syms.keys())

ratios = {'E': [], 'F': [], 'T': []}; resid = {'E': 0, 'F': 0, 'T': 0}
for trial in range(12):
    z = samp[trial * 37]
    Mz = Mfun(z); Mvals = [Mz[A_, B_] for (A_, B_) in keys]
    q = rng.normal(size=4); c = rng.normal(size=(3, 4))
    e = Lw @ np.array([Mz[i, j] for (i, j) in idx6]); m = Mz[4, 5]
    qu = etam @ q
    s = [Si @ q for Si in S]                       # s_j^mu = S_j^{mu nu} q_nu
    K = [np.outer(qu, ci) - np.outer(ci, qu) for ci in c]
    predE = sum(e[i] * e[j] * np.outer(c[i], s[j]) for i in range(3) for j in range(3))
    predF = m * sum(e[i] * K[i] for i in range(3))
    predT = m * sum(e[i] * e[j] * np.einsum('ab,m->abm', K[i], s[j]) for i in range(3) for j in range(3))
    gotE = np.array(fE(Mvals, q, c.flatten()), dtype=complex)
    gotF = np.array(fF(Mvals, q, c.flatten()), dtype=complex)
    gotT = np.array(fT(Mvals, q, c.flatten()), dtype=complex)
    for key, got, pred in (('E', gotE, predE), ('F', gotF, predF), ('T', gotT, predT)):
        k = np.vdot(pred.flatten(), got.flatten()) / np.vdot(pred.flatten(), pred.flatten())
        ratios[key].append(k)
        resid[key] = max(resid[key], np.linalg.norm(got - k * pred) / np.linalg.norm(got))
for key in ('E', 'F', 'T'):
    r = np.array(ratios[key])
    P("(B) d%s: fitted constant k = %s (spread %.1e over 12 random points/q/c), max relative residual %.2e"
      % (key, np.round(r[0], 10), np.abs(r - r[0]).max(), resid[key]))

# ---------------- (C) fibre moments ----------------
E = np.array([Lw @ np.array([Mfun(z)[i, j] for (i, j) in idx6]) for z in boosted_fibre(20000)])
m1 = E.mean(0); m2 = E.T @ E / len(E)
m4 = np.einsum('ni,nj,nk,nl->ijkl', E, E, E, E) / len(E)
d = np.eye(3)
iso = (np.einsum('ij,kl->ijkl', d, d) + np.einsum('ik,jl->ijkl', d, d) + np.einsum('il,jk->ijkl', d, d)) * 3 / 5
P("(C) <e^i> max |.| = %.3f ; <e e> - 1 max |.| = %.3f ; ||<eeee> - (3/5)iso|| / ||(3/5)iso|| = %.3f  (Monte Carlo, N = 20000, noise ~ %.3f)"
  % (np.abs(m1).max(), np.abs(m2 - d).max(), np.linalg.norm(m4 - iso) / np.linalg.norm(iso), 3 / np.sqrt(20000)))
P("    |e|^2 on the fibre: mean %.6f, std %.2e (a constant radius: e/|e| is a point of S^2)" % ((E ** 2).sum(1).mean(), (E ** 2).sum(1).std()))
# Gram of S_i in the eta^{-1} contraction of 2-forms, for the record
gramS = np.array([[0.5 * np.einsum('ab,ac,bd,cd->', Si, etam, etam, Sj) for Sj in S] for Si in S])
P("    Gram (1/2) S_i.S_j (eta contraction):", np.round(gramS, 6).tolist())
open(__file__.replace('.py', '.out.txt'), 'w').write("\n".join(out) + "\n")
