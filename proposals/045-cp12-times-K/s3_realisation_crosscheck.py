"""
s3_realisation_crosscheck.py  (proposal 045)

Independent numerical cross-check of the trace-reading forms of s2 on the explicit orbit realisation:
  * the pointwise frame and torsion perturbations are taken from the Lie-Poisson leading symbols (sympy
    engine of s1, lambdified), not from the closed formulas;
  * the fibre average is a Monte Carlo average over the stabiliser (Haar), not the exact moments;
  * the fibre basis S_i and harmonics e^i come from the realisation (exact invariant quadric), not from the
    013 model.
Compared quantities are basis independent: generalised eigenvalues of the index form (trace reading, IX2), of
the scalar a_1 form (SC2) and of the averaged-frame index form (IX1) relative to the Einstein-Hilbert form of
the averaged metric, on the five traceless physical polarisations, at the base point y = (-5,0,0,0,3) and
q = (3/7, 1/2, -2/3, 1/5) of s2 (case (-5,3)).  A second evaluation uses the closed formulas with the realisation's S_i and an exact
average (the 12 icosahedron vertices, a spherical 5-design, exact for the degree-4 integrands), to separate
Monte Carlo noise from model differences.
"""
import numpy as np, sympy as sp, scipy.linalg as sl
from scipy.linalg import expm
from cp12_realisation import Mfun, PB, lie, Sig, point_at_rest

rng = np.random.default_rng(4545)
out = []
def P(*a):
    line = " ".join(str(x) for x in a); print(line); out.append(line)

n = 8.0
z0, _ = point_at_rest(n=n, seed=3)
Ub = expm(1j * (-np.arctanh(3.0 / 5.0)) * Sig[0, 4])
gens = [(a, b) for a in range(1, 5) for b in range(a + 1, 5)]
def rand_rot():
    U = np.eye(4, dtype=complex)
    for k in range(6):
        for (a, b) in gens:
            U = expm(1j * rng.uniform(0, 2 * np.pi) * Sig[a, b]) @ U
    return U
zb = Ub @ z0; Mb = Mfun(zb); yb = Mb[:5, 5]; m = Mb[4, 5]
s_br = int(round(PB(0, 4, 1, 4, zb) / lie(0, 4, 1, 4, Mb)))
P("base point y =", np.round(yb, 9), " m = M^45 =", round(m, 9), " bracket sign", s_br)

# ---- fibre basis from the realisation (as in s1)
idx6 = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
samp = [Ub @ rand_rot() @ z0 for _ in range(3000)]
W6 = np.array([[Mfun(z)[i, j] for (i, j) in idx6] for z in samp])
_, _, Vh = np.linalg.svd(W6, full_matrices=False); Bas = Vh[:3]; w3 = W6 @ Bas.T
rows = np.array([[w[0]*w[0], w[1]*w[1], w[2]*w[2], 2*w[0]*w[1], 2*w[0]*w[2], 2*w[1]*w[2]] for w in w3])
qv_ = np.linalg.lstsq(rows, np.ones(len(w3)), rcond=None)[0]
Qm = np.array([[qv_[0], qv_[3], qv_[4]], [qv_[3], qv_[1], qv_[5]], [qv_[4], qv_[5], qv_[2]]])
ev_, U_ = np.linalg.eigh(Qm)
Lw = U_ @ np.diag(ev_ ** 0.5) @ U_.T @ Bas          # n = Lw . M6 is a unit vector of S^2
Bmat = np.linalg.pinv(Lw)
S = []
for i in range(3):
    Si = np.zeros((4, 4))
    for k, (mu, rho) in enumerate(idx6):
        Si[mu, rho] = Bmat[k, i]; Si[rho, mu] = -Bmat[k, i]
    S.append(Si)
P("unit-sphere check: max | |n|^2 - 1 | = %.1e" % np.abs(np.einsum('ni,ni->n', w3 @ (U_ @ np.diag(ev_ ** 0.5) @ U_.T).T, w3 @ (U_ @ np.diag(ev_ ** 0.5) @ U_.T).T) - 1).max())

# ---- Lie-Poisson engine (as in s1)
syms = {}
for A in range(6):
    for B in range(A + 1, 6):
        syms[(A, B)] = sp.Symbol('M%d%d' % (A, B))
def Ms(A, B):
    if A == B: return sp.Integer(0)
    return syms[(A, B)] if A < B else -syms[(B, A)]
eta6 = [-1, 1, 1, 1, 1, -1]
def lieS(A, B, C, D):
    e = lambda X, Y: eta6[X] if X == Y else 0
    return s_br * (e(A, C) * Ms(B, D) - e(A, D) * Ms(B, C) - e(B, C) * Ms(A, D) + e(B, D) * Ms(A, C))
pairs = sorted(syms.keys()); STRUCT = {(p1, p2): lieS(*p1, *p2) for p1 in pairs for p2 in pairs}
lam = sp.Symbol('lam'); Ex = sp.Symbol('Ex'); qsym = sp.symbols('q0:4')
phi = sum(qsym[mu] * Ms(mu, 5) for mu in range(4))
def D(f, p): return sp.diff(f, syms[p]) + sp.diff(f, Ex) * sp.I * lam * Ex * sp.diff(phi, syms[p])
def br(f, g):
    df = {p: D(f, p) for p in pairs}; dg = {p: D(g, p) for p in pairs}; tot = 0
    for p1 in pairs:
        if df[p1] == 0: continue
        for p2 in pairs:
            if dg[p2] == 0: continue
            st = STRUCT[(p1, p2)]
            if st != 0: tot += df[p1] * dg[p2] * st
    return sp.expand(tot)
Tm = [Ms(a, 4) for a in range(4)]; ym = [Ms(mu, 5) for mu in range(4)]
esym = [sum(Lw[i, k] * Ms(*idx6[k]) for k in range(6)) for i in range(3)]
csym = [[sp.Symbol('c%d_%d' % (i, a)) for a in range(4)] for i in range(3)]
A = [sum(csym[i][a] * esym[i] for i in range(3)) * Ex for a in range(4)]
dE = [[br(A[a], ym[mu]) for mu in range(4)] for a in range(4)]
dF = [[sp.expand(br(Tm[a], A[b]) + br(A[a], Tm[b])) for b in range(4)] for a in range(4)]
dT = [[[br(dF[a][b], ym[mu]) for mu in range(4)] for b in range(4)] for a in range(4)]
co = lambda e, k: sp.expand(e.subs(Ex, 1)).coeff(lam, k)
argl = [list(syms.values()), qsym, [c for row in csym for c in row]]
fE = sp.lambdify(argl, [[co(dE[a][mu], 1) for mu in range(4)] for a in range(4)], 'numpy')
fT = sp.lambdify(argl, [[[co(dT[a][b][mu], 2) for mu in range(4)] for b in range(4)] for a in range(4)], 'numpy')
keys = list(syms.keys())

# ---- numeric forms
eta = np.diag([-1., 1, 1, 1])
q = np.array([3 / 7, 1 / 2, -2 / 3, 1 / 5]); qu = eta @ q; q2 = q @ eta @ q
gb = m ** 2 * eta; Gb = np.linalg.inv(gb); sqG = np.sqrt(abs(np.linalg.det(Gb)))
def EH2n(gbar, H):
    gi = np.linalg.inv(gbar); sq = np.sqrt(abs(np.linalg.det(gbar)))
    Hu = gi @ H @ gi; qq = q @ gi @ q; HH = np.sum(H * Hu); trH = np.sum(gi * H); qH = Hu @ q
    return sq * 0.25 * (-0.5 * qq * HH + qH @ gbar @ qH - (q @ Hu @ q) * trH + 0.5 * qq * trH ** 2)
def scalar_n(dgam):
    dG = -Gb @ dgam @ Gb; dphi = -0.25 * np.sum(gb * dG)
    return EH2n(Gb, dG) / 6 - sqG * (q @ gb @ q) * dphi ** 2 * 0.5, EH2n(Gb, dG)
def index_n(dTa):
    return sqG * 0.5 * np.einsum('mn,ac,bd,abm,cdn->', Gb, eta, eta, dTa, dTa)
def bilinear(fun, vecs):
    """symmetric matrix of a quadratic function evaluated on basis vectors (polarisation)."""
    nb = len(vecs); Mx = np.zeros((nb, nb))
    val = [fun(v) for v in vecs]
    for i in range(nb):
        for j in range(i, nb):
            if i == j: Mx[i, i] = val[i]
            else:
                Mx[i, j] = Mx[j, i] = 0.5 * (fun(vecs[i] + vecs[j]) - val[i] - val[j])
    return Mx
Eb = m * eta   # E^{a mu} = m eta^{a mu}  (sign of the realisation irrelevant for quadratic forms)
basis12 = [np.eye(12)[k] for k in range(12)]

def pointwise_maps(z):
    Mz = Mfun(z); Mvals = [Mz[A_, B_] for (A_, B_) in keys]
    LE = np.zeros((16, 12)); LT = np.zeros((64, 12))
    for k in range(12):
        e_ = np.array(fE(Mvals, q, basis12[k]), dtype=complex)
        t_ = np.array(fT(Mvals, q, basis12[k]), dtype=complex)
        LE[:, k] = (1j * e_).real.flatten()          # dE = -i x real
        LT[:, k] = (-t_).real.flatten()              # dT = - real
    return LE, LT

def forms_from_maps(LE, LT):
    def dgam(c):
        dEm = (LE @ c).reshape(4, 4); return Eb.T @ eta @ dEm + dEm.T @ eta @ Eb
    SC = bilinear(lambda c: scalar_n(dgam(c))[0], basis12)
    EHp = bilinear(lambda c: scalar_n(dgam(c))[1], basis12)
    IX = bilinear(lambda c: index_n((LT @ c).reshape(4, 4, 4)), basis12)
    return SC, EHp, IX

Nmc = 6000
SCa = np.zeros((12, 12)); IXa = np.zeros((12, 12)); LEa = np.zeros((16, 12)); LTa = np.zeros((64, 12))
for t in range(Nmc):
    z = Ub @ rand_rot() @ z0
    LE, LT = pointwise_maps(z)
    SC, EHp, IX = forms_from_maps(LE, LT)
    SCa += SC; IXa += IX; LEa += LE; LTa += LT
SCa /= Nmc; IXa /= Nmc; LEa /= Nmc; LTa /= Nmc
SC1, EH1, IX1 = forms_from_maps(LEa, LTa)          # averaged-frame reading

# ---- change to (D, gamma) coordinates: c_i = D_ij s_j + g_i q^a
s = [Si @ q for Si in S]
Cmap = np.zeros((12, 12))   # columns: D (row-major 9) then g (3); rows: c_i^a (i major)
for i in range(3):
    for j in range(3):
        Cmap[4 * i:4 * i + 4, 3 * i + j] = s[j]
    Cmap[4 * i:4 * i + 4, 9 + i] = qu
Es = []
for (i, j) in [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]:
    Mx = np.zeros((3, 3)); Mx[i, j] = Mx[j, i] = 1; Es.append(Mx.flatten())
Bs = np.array(Es).T   # 9 x 6
Gs = np.array([[s[i] @ eta @ s[j] for j in range(3)] for i in range(3)])
trrow = np.array([np.trace(Gs @ e.reshape(3, 3)) for e in Es])
Ntl = sl.null_space(trrow[None, :])
def restrict(F12):
    F9 = (Cmap.T @ F12 @ Cmap)[:9, :9]
    F6 = Bs.T @ F9 @ Bs
    return Ntl.T @ F6 @ Ntl, F6
EH5, EH6 = restrict(EH1)
P("gauge check (forms on the gauge amplitudes, relative): IX2 %.1e, SC2 %.1e"
  % (np.abs((Cmap.T @ IXa @ Cmap)[9:, :]).max() / np.abs(IXa).max(), np.abs((Cmap.T @ SCa @ Cmap)[9:, :]).max() / np.abs(SCa).max()))
def gev(F, ref):
    Q5, _ = restrict(F); R5, _ = restrict(ref); ev = sl.eigvals(Q5, R5)
    return np.sort_complex(ev)

# ---- exact-moment version with the realisation's S_i (formula based)
def exact_moment_forms():
    # pointwise maps from the closed formulas, averaged with exact isotropic moments via a spherical design:
    # a degree-4 exact average on S^2 is obtained from the 12 vertices of an icosahedron (spherical 5-design)
    ph = (1 + 5 ** 0.5) / 2
    V = []
    for a in (-1, 1):
        for b in (-1, 1):
            V += [(0, a, b * ph), (a, b * ph, 0), (b * ph, 0, a)]
    V = np.array(V, float); V /= np.linalg.norm(V[0])
    SCs = np.zeros((12, 12)); IXs = np.zeros((12, 12)); LEs = np.zeros((16, 12)); LTs = np.zeros((64, 12))
    for nvec in V:
        NN = np.outer(nvec, nvec)
        LE = np.zeros((16, 12)); LT = np.zeros((64, 12))
        for k in range(12):
            c = basis12[k].reshape(3, 4)
            dEm = sum(NN[i, j] * np.outer(c[i], s[j]) for i in range(3) for j in range(3))
            K = [np.outer(qu, c[i]) - np.outer(c[i], qu) for i in range(3)]
            dTm = -m * sum(NN[i, j] * np.einsum('ab,m->abm', K[i], s[j]) for i in range(3) for j in range(3))
            LE[:, k] = dEm.flatten(); LT[:, k] = dTm.flatten()
        SC, EHp, IX = forms_from_maps(LE, LT)
        SCs += SC; IXs += IX; LEs += LE; LTs += LT
    SC1x, EH1x, IX1x = forms_from_maps(LEs / len(V), LTs / len(V))
    return SCs / len(V), IXs / len(V), SC1x, EH1x, IX1x
SCx, IXx, SC1x, EH1x, IX1x = exact_moment_forms()

P("\nGeneralised eigenvalues on the five traceless polarisations, relative to EH of the averaged metric")
P("(s2 exact model at (y0,y4) = (-5,3), same q:  IX2: -4.35623 x2, -0.733169 x2, 0.474519;  SC2: -0.0231477 x2, 0.180228, 0.38151 x2;  IX1: -2 x5)")
for name, F, ref in (("IX2 Monte Carlo + Lie-Poisson", IXa, EH1), ("IX2 exact moments, realisation S", IXx, EH1x),
                ("SC2 Monte Carlo + Lie-Poisson", SCa, EH1), ("SC2 exact moments, realisation S", SCx, EH1x),
                ("IX1 (averaged frame, MC)", IX1, EH1), ("IX1 (averaged frame, exact)", IX1x, EH1x),
                ("SC1 (averaged frame, MC)", SC1, EH1), ("SC1 (averaged frame, exact)", SC1x, EH1x)):
    ev = gev(F, ref)
    P("  %-34s %s" % (name, ["%.5g" % z.real + ("%+.1ei" % z.imag if abs(z.imag) > 1e-6 else "") for z in ev]))
P("(Monte Carlo with %d fibre samples; statistical error of order 1/sqrt(N) ~ %.1e relative)" % (Nmc, 1 / np.sqrt(Nmc)))
open(__file__.replace('.py', '.out.txt'), 'w').write("\n".join(out) + "\n")
