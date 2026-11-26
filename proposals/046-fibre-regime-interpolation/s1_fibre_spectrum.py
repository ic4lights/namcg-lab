"""
s1_fibre_spectrum.py  (proposal 046)

Spectrum of the loop scalar operator H_0 = -Box, Box = eta_ab {T^a,{T^b, . }}, on the fibre harmonics of the
conjugate-coordinate class (leaf CP^{1,2} of so(4,2), T^a = M^{a4}, y^mu = M^{mu5}, m = M^{45}, units R = 1),
and the structure of the base-fibre cross term.

Exact part (polynomial Lie-Poisson algebra, sympy, both bracket signs):
  (E1) Box t^mu = -3 t^mu                                   (t^mu := T^mu = M^{mu4})
  (E2) Box(t^mu t^nu) = -6 t^mu t^nu + 2 eta_ab M^{a mu} M^{b nu}
  (E3) Box(t^mu t^nu t^rho) = -9 ttt + 2 sum over the three pairs of eta_ab M^{a.}M^{b.} t^.
Numerical part (explicit realisation of the orbit, cp12_realisation.py):
  (N1) eta_ab M^{a mu} M^{b nu} = c_theta eta^{mu nu} + y^mu y^nu - t^mu t^nu at random orbit points (fit c_theta);
  (N2) on the fibre over a base point: y fixed, t.y = 0, t.t constant (t is a radius vector of the fibre sphere);
  (N3) for C symmetric, traceless with respect to eta on y^perp and transverse to y (spin J harmonic of the fibre),
       Box(C.t^J) = -J(J+2) C.t^J on that fibre, J = 1, 2, 3, at two base points (one with y^i != 0);
       compared with 3J (Steinacker 2303.08012, eq. (7.5)).
  (N4) the cross term 2 eta_ab {T^a, phi}{T^b, Y} for phi = exp(i lam q.y): its leading (order lam) part, as an
       operator on the spin-1 and spin-2 fibre harmonics: maps J -> J, J +- 2 only; its norm in units of m|q|_E
       compared with tanh(tau), tanh(tau) = y^4/y^0 at y^i = 0.
"""
import numpy as np, sympy as sp, itertools
from scipy.linalg import expm
from cp12_realisation import Mfun, PB, lie, eta6, Sig, point_at_rest

rng = np.random.default_rng(46)
out = []
def P(*a):
    line = " ".join(str(x) for x in a); print(line); out.append(line)

# ---------------- sympy Lie-Poisson engine (as in 045 s1) ----------------
syms = {}
for A in range(6):
    for B in range(A + 1, 6):
        syms[(A, B)] = sp.Symbol('M%d%d' % (A, B))
def Ms(A, B):
    if A == B: return sp.Integer(0)
    return syms[(A, B)] if A < B else -syms[(B, A)]
eta = [-1, 1, 1, 1, 1, -1]
pairs = sorted(syms.keys())
def make_struct(s_br):
    def lieS(A, B, C, D):
        e = lambda X, Y: eta[X] if X == Y else 0
        return s_br * (e(A, C) * Ms(B, D) - e(A, D) * Ms(B, C) - e(B, C) * Ms(A, D) + e(B, D) * Ms(A, C))
    return {(p1, p2): lieS(*p1, *p2) for p1 in pairs for p2 in pairs}
lam = sp.Symbol('lam'); Ex = sp.Symbol('Ex'); qsym = sp.symbols('q0:4')
phi = sum(qsym[mu] * Ms(mu, 5) for mu in range(4))
def D(f, p):
    return sp.diff(f, syms[p]) + sp.diff(f, Ex) * sp.I * lam * Ex * sp.diff(phi, syms[p])
def br(f, g, ST):
    df = {p: D(f, p) for p in pairs}; dg = {p: D(g, p) for p in pairs}
    tot = 0
    for p1 in pairs:
        if df[p1] == 0: continue
        for p2 in pairs:
            if dg[p2] == 0: continue
            st = ST[(p1, p2)]
            if st != 0: tot += df[p1] * dg[p2] * st
    return sp.expand(tot)
etam4 = [-1, 1, 1, 1]
Tm = [Ms(a, 4) for a in range(4)]
def Box(f, ST):
    return sp.expand(sum(etam4[a] * br(Tm[a], br(Tm[a], f, ST), ST) for a in range(4)))

P("(E) exact identities in the polynomial Lie-Poisson algebra")
for s_br in (1, -1):
    ST = make_struct(s_br)
    ok1 = all(sp.expand(Box(Tm[m], ST) + 3 * Tm[m]) == 0 for m in range(4))
    MM = lambda mu, nu: sum(etam4[a] * Ms(a, mu) * Ms(a, nu) for a in range(4))
    ok2 = all(sp.expand(Box(Tm[m] * Tm[n], ST) + 6 * Tm[m] * Tm[n] - 2 * MM(m, n)) == 0 for m in range(4) for n in range(m, 4))
    ok3 = True
    for (m, n, r) in [(1, 2, 3), (1, 1, 2), (0, 1, 2), (3, 3, 3)]:
        lhs = Box(Tm[m] * Tm[n] * Tm[r], ST)
        rhs = -9 * Tm[m] * Tm[n] * Tm[r] + 2 * (MM(m, n) * Tm[r] + MM(m, r) * Tm[n] + MM(n, r) * Tm[m])
        ok3 &= sp.expand(lhs - rhs) == 0
    P("   bracket sign %+d: (E1) Box t = -3 t: %s; (E2) Box(tt) = -6tt + 2 eta M M: %s; (E3) cubic identity (4 index triples): %s"
      % (s_br, ok1, ok2, ok3))
ST = make_struct(-1)      # sign of the realisation (045 s1: bracket sign s = -1)

# ---------------- (N1) theta-theta identity on the orbit ----------------
etaL = np.diag([-1., 1, 1, 1])
def rand_orbit_point(n=8.0):
    from cp12_realisation import rand_z_pos
    return rand_z_pos(rng, n)
maxres = 0; cth = []
for k in range(40):
    z = rand_orbit_point(); M = Mfun(z)
    y = M[:4, 5]; t = M[:4, 4]
    MMn = np.array([[sum(etaL[a, a] * M[a, mu] * M[a, nu] for a in range(4)) for nu in range(4)] for mu in range(4)])
    R0 = MMn - np.outer(y, y) + np.outer(t, t)
    c = np.trace(etaL @ R0) / 4.0           # R0 = c eta^{-1} expected; eta^{-1} = etaL
    cth.append(c)
    maxres = max(maxres, np.abs(R0 - c * etaL).max() / max(1, np.abs(MMn).max()))
P("\n(N1) eta_ab M^{a mu}M^{b nu} = c_theta eta^{mu nu} + y^mu y^nu - t^mu t^nu at 40 random orbit points: max relative residual %.1e"
  % maxres)

# ---------------- fibre over a base point ----------------
nlev = 8.0
z0, resid0 = point_at_rest(n=nlev, seed=3)
gens = [(a, b) for a in range(1, 5) for b in range(a + 1, 5)]
def rand_rot():
    U = np.eye(4, dtype=complex)
    for k in range(6):
        for (a, b) in gens:
            U = expm(1j * rng.uniform(0, 2 * np.pi) * Sig[a, b]) @ U
    return U
def make_fibre(beta, extra=None, N=400):
    Ub = expm(1j * beta * Sig[0, 4])
    if extra is not None: Ub = extra @ Ub
    return [Ub @ rand_rot() @ z0 for _ in range(N)]

keys = list(syms.keys())
def evalpoly(f):
    fl = sp.lambdify([list(syms.values())], f, 'numpy')
    return lambda z: fl([Mfun(z)[A, B] for (A, B) in keys])

def perp_basis(y4vec):
    yv = np.array(y4vec, float)
    Pp = np.eye(4) - np.outer(yv, yv @ etaL) / (yv @ etaL @ yv)
    bas = []
    for v in np.eye(4):
        w = Pp @ v
        for b in bas: w = w - (b @ etaL @ w) * b
        if np.sqrt(abs(w @ etaL @ w)) > 1e-8: bas.append(w / np.sqrt(w @ etaL @ w))
        if len(bas) == 3: break
    return np.array(bas).T                 # 4 x 3, columns e_i with e_i.eta.e_j = delta_ij

def harmonic3(J, T3=None):
    """symmetric traceless rank-J tensor in 3 dims (random unless given)"""
    if T3 is None: T3 = rng.normal(size=(3,) * J)
    perms = list(itertools.permutations(range(J)))
    T = sum(np.transpose(T3, p) for p in perms) / len(perms)
    d = np.eye(3)
    if J == 2:
        T = T - np.trace(T) / 3 * d
    elif J == 3:
        tr = np.einsum('iij->j', T)
        T = T - (np.einsum('ij,k->ijk', d, tr) + np.einsum('ik,j->ijk', d, tr) + np.einsum('jk,i->ijk', d, tr)) / 5
    return T

def spinJ_tensor(J, y4vec, T3=None):
    """C^{mu...} = E3^{mu i}... T_{i...}: transverse to y, traceless w.r.t. eta on y^perp"""
    E3 = perp_basis(y4vec); T = harmonic3(J, T3); C = T
    for k in range(J):
        C = np.moveaxis(np.tensordot(E3, C, axes=([1], [k])), 0, k)
    return C, E3

def poly_from_C(C):
    """Y = C_{mu...} t^mu ..., with the indices of C (built upper) lowered by eta"""
    J = C.ndim
    for k in range(J):
        C = np.moveaxis(np.tensordot(etaL, C, axes=([1], [k])), 0, k)
    f = 0
    for idx in itertools.product(range(4), repeat=J):
        if abs(C[idx]) < 1e-14: continue
        f += sp.Float(C[idx], 18) * sp.Mul(*[tsym[i] for i in idx])
    return sp.expand(f)

tsym = [Ms(mu, 4) for mu in range(4)]
P("\n(N2)-(N3) fibre harmonics: Box(C.t^J) on the fibre over a base point")
results = {}
for label, beta, extra in (("base point A (y^i = 0)", -np.arctanh(3.0 / 5.0), None),
                           ("base point B (y^i != 0)", -np.arctanh(0.5), expm(1j * 0.7 * Sig[0, 1]) @ expm(1j * 0.4 * Sig[0, 2]))):
    fib = make_fibre(beta, extra, N=300)
    Ys = np.array([Mfun(z)[:5, 5] for z in fib]); ts = np.array([Mfun(z)[:4, 4] for z in fib])
    yb = Ys[0]; y4v = yb[:4]
    tdoty = np.abs(np.einsum('ni,ij,j->n', ts, etaL, y4v)).max()
    tt = np.einsum('ni,ij,nj->n', ts, etaL, ts)
    ell = np.sqrt(-(yb[:4] @ etaL @ yb[:4]) - yb[4] ** 2)
    P("  %s: y^A = %s, ell = %.6f, y^4 = %.6f; fibre: max|y - y_b| = %.1e, max|t.y| = %.1e, t.t = %.6f +- %.1e (y.y_4 + ... check: t.t/((y^0)^2) = %.6f)"
      % (label, np.round(yb, 6), ell, yb[4], np.abs(Ys - yb).max(), tdoty, tt.mean(), tt.std(), tt.mean() / (yb[0] ** 2)))
    for J in (1, 2, 3):
        C, E3 = spinJ_tensor(J, y4v)
        f = poly_from_C(C)
        Bf = Box(f, ST)
        fe = evalpoly(f); Be = evalpoly(Bf)
        vals = np.array([fe(z) for z in fib]); bvals = np.array([Be(z) for z in fib])
        ratio = np.vdot(vals, bvals).real / np.vdot(vals, vals).real
        res = np.linalg.norm(bvals - ratio * vals) / np.linalg.norm(bvals)
        results[(label, J)] = ratio
        P("     J = %d: Box(C.t^J) = %.10f x C.t^J on the fibre (relative residual %.1e); -J(J+2) = %d; Steinacker -3J = %d"
          % (J, ratio, res, -J * (J + 2), -3 * J))

# ---------------- (N4) cross term ----------------
P("\n(N4) base-fibre cross term 2 eta_ab {T^a, exp(i lam q.y)}{T^b, Y}, order lam, at base point A")
fib = make_fibre(-np.arctanh(3.0 / 5.0), None, N=2000)
Mf = [Mfun(z) for z in fib]
yb = Mf[0][:5, 5]; y4v = yb[:4]; m = yb[4]
ts = np.array([M[:4, 4] for M in Mf])
nvec = ts[:, 1:] / np.linalg.norm(ts[:, 1:], axis=1)[:, None]
P("   t^0 on the fibre: max |t^0| = %.1e ; |t| = %.6f, y^0 = %.6f" % (np.abs(ts[:, 0]).max(), np.linalg.norm(ts[0, 1:]), yb[0]))
def real_harm(n, Lmax):
    feats, labs = [], []
    for L in range(Lmax + 1):
        for c in itertools.combinations_with_replacement(range(3), L):
            feats.append(np.prod([n[:, i] for i in c], axis=0) if L > 0 else np.ones(len(n))); labs.append(L)
    return np.array(feats).T, np.array(labs)
F, labs = real_harm(nvec, 4)
Qo, _ = np.linalg.qr(F)
Qo = Qo * np.sqrt(len(F))                       # MC-orthonormal, graded by degree (QR in increasing degree)
qv = [sp.Rational(3, 10), sp.Rational(-1, 2), sp.Rational(2, 5), sp.Rational(1, 5)]
qE = float(sp.sqrt(sum(x ** 2 for x in qv)))
for J in (1, 2):
    E3 = perp_basis(y4v)
    basisT = []
    if J == 1:
        for i in range(3):
            T3 = np.zeros(3); T3[i] = 1; basisT.append(T3)
    else:
        for (i, j) in [(0, 0), (1, 1), (0, 1), (0, 2), (1, 2)]:
            T3 = np.zeros((3, 3)); T3[i, j] = T3[j, i] = 1
            if (i, j) == (0, 0): T3 = np.diag([1., -1, 0])
            if (i, j) == (1, 1): T3 = np.diag([0., 1, -1])
            basisT.append(T3)
    imgs, srcs = [], []
    for T3 in basisT:
        C, _ = spinJ_tensor(J, y4v, T3)
        Y = poly_from_C(C)
        cr = 2 * sum(etam4[a] * br(Tm[a], Ex, ST) * br(Tm[a], Y, ST) for a in range(4))
        cr = sp.expand(cr.subs({qsym[i]: qv[i] for i in range(4)})).subs(Ex, 1).coeff(lam, 1)
        fe = evalpoly(cr); fy = evalpoly(Y)
        imgs.append(np.array([complex(fe(z)) for z in fib])); srcs.append(np.array([fy(z) for z in fib]))
    imgs = np.array(imgs).T; srcs = np.array(srcs).T
    # projection of the images onto harmonic degrees: use orthonormal columns by degree
    degcols = {L: Qo[:, np.where(labs == L)[0]] for L in range(5)}
    tot = np.linalg.norm(imgs)
    fr = []
    for L in range(5):
        co = degcols[L].conj().T @ imgs / len(F)
        fr.append(np.linalg.norm(degcols[L] @ co) / tot)
    # J -> J block in the basis of the sources (sources are spin-J harmonics on this fibre)
    G = srcs.conj().T @ srcs / len(F)
    Bk = np.linalg.solve(G, srcs.conj().T @ imgs / len(F))
    Gh = np.linalg.cholesky(G)
    Bn = Gh.conj().T @ Bk @ np.linalg.inv(Gh.conj().T)
    sv = np.linalg.svd(Bn, compute_uv=False)
    P("   J = %d: image norm fraction in harmonic degrees 0..4: %s ; J->J block (orthonormalised) singular values / (m |q|_E): %s ; tanh(tau) = y^4/y^0 = %.6f ; image purely imaginary: %s"
      % (J, [round(x, 4) for x in fr], np.round(sv / (m * qE), 4).tolist(), m / yb[0], np.abs(imgs.real).max() < 1e-9 * np.abs(imgs).max()))
qn = np.array([float(x) for x in qv]); ellA = np.sqrt(yb[0] ** 2 - yb[4] ** 2)
for J in (1, 2):
    pred = sorted([2 * m / abs(yb[0]) * np.sqrt((yb[4] * qn[0] * J) ** 2 + (ellA * np.linalg.norm(qn[1:]) * mL) ** 2) / (m * qE)
                   for mL in range(-J, J + 1)], reverse=True)
    P("   closed form at y^i = 0: singular values (2m/|y^0|) sqrt((y^4 q_0 J)^2 + (ell |q_vec| m_L)^2), m_L = -J..J, / (m |q|_E): J = %d: %s" % (J, np.round(pred, 4).tolist()))
P("   (Monte Carlo fibre quadrature with 2000 points: fractions and singular values accurate to about 1e-2.)")
open(__file__.replace('.py', '.out.txt'), 'w').write("\n".join(out) + "\n")
