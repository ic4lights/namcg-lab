"""
Proposal 059 (local round 2), check E2: finite-N realisations, numpy float64
(Clebsch-Gordan coefficients from sympy, Condon-Shortley).

Class relations (Euclidean contraction, Problem D first-order class):
  (I)  [S_cd, D_a] = d_ad D_c - d_ac D_d,   (II) [D_a, D_b] = -T D + 1/2 R S + F,
with Hermitian matrices Xh_a = i D_a and anti-Hermitian S_cd.

Part A  (isometry-equivariant Berezin-Toeplitz / fuzzy sphere, End(C^N)):
  A1 L_a = ad_{X_a}/hbar Leibniz and [L_i,L_j] = i eps L_k exact; L_i(X_j) = i eps X_k
  A2 ghost sum_i ad_{X_i}^2 / hbar^2: spectrum {l(l+1)}, multiplicity 2l+1, l<=N-1
  A3 one-sided redundancy: sum_i X_i [X_i, F] = (hbar^2/2) l(l+1) F on the spin-l
     sector (exact), i.e. sum_i X_i L_i F = (hbar/2) l(l+1) F;
     symmetric ordering 1/2 sum_i {X_i,[X_i,F]} = 0 exactly
  A4 Moyal-vs-Poisson error for x1^2 x2, x3: log-log slope -1 in N (numerical)
Part B  (exact class relations at finite N, constant coefficients):
  B1 su(2), spin j, N=2j+1:  Xh_1=J_1, Xh_2=J_2, S_12 = i J_3:  (I), and (II) with
     T=0, R_12^12=-1, F=0
  B2 so(5) in the 5, the spinor 4 and 4x5=20: D_a = rho(E_a5), S_ab = rho(E_ab):
     (I), (II) with T=0, R_ab^cd = -(d_a^c d_b^d - d_a^d d_b^c), F=0 (unit S^4)
  B3 so(4,1) fundamental with eta=diag(-1,1,1,1): (I),(II) with eta hold, the
     generators are eta-anti-self-adjoint, the boosts are not anti-Hermitian
Part C  (frame-equivariant Peter-Weyl truncation H_L = (+)_{j<=L} V_j (x) V_j^*,
         functions on SO(3), integer j):
  C1 right generators Xh_a: (I),(II) exact with S_12 = i Xh_3 (T=0, R=-1, F=0)
  C2 conventions: [Xh_a, M_f] = M_{Xh_a f}, [Lam_a, M_f] = M_{Lam_a f}, [Xh_a, Lam_b] = 0
  C3 ghost G(Y) = sum_{a=1,2} [Xh_a,[Xh_a,Y]] on Y_{l mu} = P M_{D^l_{mu 0}} P:
     G(Y) = l(l+1) Y, [S_12, Y] = 0, for 0<=l<=2L, and the Y_{l mu} are
     linearly independent: spectrum l(l+1), multiplicity 2l+1, l<=2L
  C4 bundle redundancy at finite truncation: sum_i (P M_{x_i} P) Lam_i = c Xh_3 P,
     |c| = 1, exact
  C5 commutative algebra lost at the cutoff: [P M_x P, P M_y P] != 0, and
     P M_f P M_g P - P M_{fg} P vanishes on the blocks j < L (l_g = 1)
  C6 the Berezin-Toeplitz subspace span{phi^j_{m,n=j}} is not preserved by Xh_1
Run:  python -I d1_equivariant_finiteN.py
"""
from functools import lru_cache
import itertools
import numpy as np
from sympy.physics.quantum.cg import CG
from sympy import Rational, S as Sy

res = []


def rep(ok, name):
    res.append(bool(ok))
    print(("PASS  " if ok else "FAIL  ") + name)


def spin(j):
    m = np.arange(j, -j - 1.0, -1.0)
    n = len(m)
    Jp = np.zeros((n, n))
    for i in range(n - 1):
        Jp[i, i + 1] = np.sqrt(j * (j + 1) - m[i + 1] * (m[i + 1] + 1))
    return [(Jp + Jp.T) / 2.0 + 0j, (Jp - Jp.T) / 2.0j, np.diag(m) + 0j]


def comm(A, B):
    return A @ B - B @ A


def nrm(A):
    return float(np.linalg.norm(A))


eps = np.zeros((3, 3, 3))
for i, j, k in itertools.permutations(range(3)):
    eps[i, j, k] = np.linalg.det(np.eye(3)[[i, j, k]])

# ---------------- Part A: fuzzy sphere ----------------
def sad(A):
    N = A.shape[0]
    I = np.eye(N)
    return np.kron(A, I) - np.kron(I, A.T)

pts = []
for N in [5, 7, 9, 11, 13, 15, 17, 21, 25, 31]:
    j = (N - 1) / 2.0
    J = spin(j)
    h = 1.0 / np.sqrt(j * (j + 1))
    Xs = [Ji * h for Ji in J]
    L = [sad(Xi) / h for Xi in Xs]
    rng = np.random.default_rng(100 + N)
    r1 = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
    r2 = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
    Lm = lambda a, M: (L[a] @ M.reshape(N * N)).reshape(N, N)
    leb = max(nrm(Lm(a, r1 @ r2) - Lm(a, r1) @ r2 - r1 @ Lm(a, r2)) for a in range(3))
    clo = max(nrm(L[a] @ L[b] - L[b] @ L[a] - sum(1j * eps[a, b, c] * L[c] for c in range(3)))
              for a in range(3) for b in range(3))
    act = max(nrm(comm(Xs[a], Xs[b]) / h - sum(1j * eps[a, b, c] * Xs[c] for c in range(3)))
              for a in range(3) for b in range(3))
    G = sum(sad(Xi) @ sad(Xi) for Xi in Xs)
    G = (G + G.conj().T) / 2
    ev, V = np.linalg.eigh(G / h ** 2)
    exp = np.sort(np.concatenate([np.full(2 * l + 1, float(l * (l + 1))) for l in range(N)]))
    gd = np.max(np.abs(np.sort(ev) - exp))
    # A3 on each l-sector: projector from eigenvectors with eigenvalue l(l+1)
    red1 = red2 = 0.0
    for l in range(N):
        sel = np.abs(ev - l * (l + 1)) < 1e-6
        Pl = V[:, sel]
        F = (Pl @ (Pl.conj().T @ (r1.reshape(N * N)))).reshape(N, N)
        one = sum(Xs[i] @ comm(Xs[i], F) for i in range(3))
        sym = sum(Xs[i] @ comm(Xs[i], F) + comm(Xs[i], F) @ Xs[i] for i in range(3)) / 2
        red1 = max(red1, nrm(one - 0.5 * h ** 2 * l * (l + 1) * F) / max(nrm(F), 1e-30))
        red2 = max(red2, nrm(sym) / max(nrm(F), 1e-30))
    ok = leb < 1e-9 and clo < 1e-9 and act < 1e-9 and gd < 1e-7 and red1 < 1e-9 and red2 < 1e-9
    rep(ok, f"A  N={N}: Leibniz {leb:.1e}, closure {clo:.1e}, L_i(X_j) {act:.1e}, "
            f"ghost multiset {gd:.1e}, one-sided redundancy = (hbar^2/2) l(l+1) F {red1:.1e}, symmetric = 0 {red2:.1e}")
    P_ = Xs[0] @ Xs[0] @ Xs[1]
    sym3 = (Xs[0] @ Xs[1] @ Xs[1] + Xs[1] @ Xs[0] @ Xs[1] + Xs[1] @ Xs[1] @ Xs[0]) / 3.0
    cl = Xs[0] @ Xs[0] @ Xs[0] - 2.0 * sym3
    moy = comm(P_, Xs[2]) / (1j * h)
    pts.append((np.log(N), np.log(nrm(moy - cl) / nrm(moy))))
s4 = np.polyfit([p[0] for p in pts], [p[1] for p in pts], 1)[0]
rep(abs(s4 + 1) < 0.15, f"A4 Moyal-vs-Poisson relative error ~ N^(-1) ~ hbar_eff: slope {s4:.3f} (numerical)")

# ---------------- Part B: exact class relations ----------------
def check_class(Dm, Sm, eta, R_sign=-1.0):
    """Dm[a] anti-Hermitian-or-not matrices, Sm[(c,d)] for c<d; checks (I),(II)."""
    n = len(Dm)
    Sfull = {}
    for c in range(n):
        for d in range(n):
            if c < d:
                Sfull[(c, d)] = Sm[(c, d)]
            elif c > d:
                Sfull[(c, d)] = -Sm[(d, c)]
            else:
                Sfull[(c, d)] = 0 * Dm[0]
    e1 = max(nrm(comm(Sfull[(c, d)], Dm[a]) - (eta[a, d] * Dm[c] - eta[a, c] * Dm[d]))
             for a in range(n) for c in range(n) for d in range(n))
    # (II) with T = F = 0 and R_ab^cd = R_sign (d_a^c d_b^d - d_a^d d_b^c): [D_a,D_b] = R_sign S_ab
    e2 = max(nrm(comm(Dm[a], Dm[b]) - R_sign * Sfull[(a, b)]) for a in range(n) for b in range(n))
    return e1, e2

ok = True
for N in range(2, 32):
    j = (N - 1) / 2.0
    J = spin(j)
    D = [-1j * J[0], -1j * J[1]]          # D_a = -i Xh_a, Xh_a = J_a
    S12 = 1j * J[2]
    e1, e2 = check_class(D, {(0, 1): S12}, np.eye(2))
    ok &= e1 < 1e-10 and e2 < 1e-10
rep(ok, "B1 su(2), N=2..31: Xh_a=J_a (a=1,2), S_12=iJ_3 satisfy (I) and (II) with T=0, R_12^12=-1, F=0 exactly")


def so_gen(n, eta):
    E = {}
    for A in range(n):
        for B in range(n):
            M = np.zeros((n, n), complex)
            for C in range(n):
                for Dd in range(n):
                    M[C, Dd] = (C == A) * eta[B, Dd] - (C == B) * eta[A, Dd]
            E[(A, B)] = M
    return E

E5 = so_gen(5, np.eye(5))
# spinor of so(5): Hermitian gammas, Sigma_AB = 1/4 [G_A, G_B] ; fix sign against E5 structure
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1]).astype(complex)
I2 = np.eye(2)
Gam = [np.kron(sx, sx), np.kron(sx, sy), np.kron(sx, sz), np.kron(sy, I2), np.kron(sz, I2)]
Sig = {(A, B): 0.25 * comm(Gam[A], Gam[B]) for A in range(5) for B in range(5)}
# determine sign s with [sG_AB, sG_CD] matching E5 structure constants
def matches(G):
    err = 0.0
    for (A, B), (C, Dd) in itertools.product(E5.keys(), repeat=2):
        X = comm(E5[(A, B)], E5[(C, Dd)])
        # express X in the E basis (A'<B')
        coeffs = {(p, q): -0.5 * np.trace(X @ E5[(p, q)]).real for p in range(5) for q in range(p + 1, 5)}
        Y = sum(coeffs[k] * G[k] for k in coeffs)
        err = max(err, nrm(comm(G[(A, B)], G[(C, Dd)]) - Y))
    return err
sgn = 1.0 if matches(Sig) < 1e-10 else -1.0
Sig = {k: sgn * v for k, v in Sig.items()}
rep(matches(Sig) < 1e-10 and max(nrm(v + v.conj().T) for v in Sig.values()) < 1e-12,
    f"B2 spinor generators ({sgn:+.0f}) (1/4)[G_A,G_B] represent so(5), anti-Hermitian")
reps = {"5": E5, "4": Sig,
        "20": {k: np.kron(E5[k], np.eye(4)) + np.kron(np.eye(5), Sig[k]) for k in E5}}
okB2 = True
for name, G in reps.items():
    Dm = [G[(a, 4)] for a in range(4)]
    Sm = {(c, d): G[(c, d)] for c in range(4) for d in range(c + 1, 4)}
    e1, e2 = check_class(Dm, Sm, np.eye(4), R_sign=-1.0)
    herm = max(nrm(1j * Da - (1j * Da).conj().T) for Da in Dm)
    okB2 &= e1 < 1e-10 and e2 < 1e-10 and herm < 1e-12
    print(f"info  so(5) rep {name}: (I) err {e1:.1e}, (II) err {e2:.1e}, Xh_a Hermitian err {herm:.1e}")
rep(okB2, "B2 so(5) reps 5, 4, 20: D_a=rho(E_a5), S_ab=rho(E_ab) satisfy (I),(II), T=0, R=-(dd-dd) (unit S^4), F=0")

eta5 = np.diag([-1.0, 1, 1, 1, 1])
E41 = so_gen(5, eta5)
Dm = [E41[(a, 4)] for a in range(4)]
Sm = {(c, d): E41[(c, d)] for c in range(4) for d in range(c + 1, 4)}
e1, e2 = check_class(Dm, Sm, eta5[:4, :4], R_sign=-1.0)
etaadj = max(nrm(eta5 @ G.conj().T @ eta5 + G) for G in E41.values())
boost_antiherm = nrm(E41[(0, 1)] + E41[(0, 1)].conj().T)
rep(e1 < 1e-12 and e2 < 1e-12 and etaadj < 1e-12 and boost_antiherm > 1,
    f"B3 so(4,1) fundamental: (I),(II) with eta exact; generators eta-anti-self-adjoint; boost S_01 not anti-Hermitian (|S+S^dag| = {boost_antiherm:.2f})")

# ---------------- Part C: Peter-Weyl truncation ----------------
@lru_cache(maxsize=None)
def cg(j1, m1, j2, m2, J, M):
    if abs(m1) > j1 or abs(m2) > j2 or abs(M) > J or m1 + m2 != M:
        return 0.0
    if J < abs(j1 - j2) or J > j1 + j2:
        return 0.0
    return float(CG(Sy(j1), Sy(m1), Sy(j2), Sy(m2), Sy(J), Sy(M)).doit())


def basis(L):
    idx = []
    for j in range(L + 1):
        for m in range(j, -j - 1, -1):
            for n in range(j, -j - 1, -1):
                idx.append((j, m, n))
    return idx, {b: i for i, b in enumerate(idx)}


def right_left(L):
    idx, pos = basis(L)
    d = len(idx)
    Xh = [np.zeros((d, d), complex) for _ in range(3)]
    Lam = [np.zeros((d, d), complex) for _ in range(3)]
    for j in range(L + 1):
        J = spin(j)
        ms = list(range(j, -j - 1, -1))
        for a in range(3):
            for (ii, m), (kk, k) in itertools.product(enumerate(ms), enumerate(ms)):
                for nn, n in enumerate(ms):
                    # Xh_a phi_{m n} = sum_k phi_{m k} (J_a)_{k n}
                    Xh[a][pos[(j, m, k)], pos[(j, m, n)]] += J[a][kk, nn]
                    # Lam_a phi_{m n} = sum_k (J_a)_{m k} phi_{k n}
                    Lam[a][pos[(j, k, n)], pos[(j, m, n)]] += J[a][ii, kk]
    return idx, pos, Xh, Lam


def mult(L, l, mu, nu):
    """Matrix of multiplication by D^l_{mu nu} on H_L (compressed: P M P)."""
    idx, pos = basis(L)
    d = len(idx)
    M = np.zeros((d, d), complex)
    for (j, m, n) in idx:
        for (J, Mq, Nq) in idx:
            if Mq != mu + m or Nq != nu + n:
                continue
            c1 = cg(l, mu, j, m, J, Mq)
            if c1 == 0.0:
                continue
            c2 = cg(l, nu, j, n, J, Nq)
            M[pos[(J, Mq, Nq)], pos[(j, m, n)]] = np.sqrt((2 * j + 1) / (2 * J + 1)) * c1 * c2
    return M


def block_proj(L, Lsmall, idx):
    return np.diag([1.0 if b[0] <= Lsmall else 0.0 for b in idx])

for L in (1, 2, 3):
    idx, pos, Xh, Lam = right_left(L)
    D = [-1j * Xh[0], -1j * Xh[1]]
    S12 = 1j * Xh[2]
    e1, e2 = check_class(D, {(0, 1): S12}, np.eye(2))
    rep(e1 < 1e-10 and e2 < 1e-10, f"C1 L={L} (dim {len(idx)}): right generators satisfy (I),(II), T=0, R_12^12=-1, F=0, S_12=i Xh_3")

# C2 conventions on H_3 restricted to inputs in blocks j<=2, functions with l=1
L = 3
idx, pos, Xh, Lam = right_left(L)
P2 = block_proj(L, 2, idx)
J1 = spin(1)
ms1 = [1, 0, -1]
err_r = err_l = 0.0
for mu in ms1:
    for nu in ms1:
        M = mult(L, 1, mu, nu)
        for a in range(3):
            # Xh_a D^1_{mu nu} = sum_k D^1_{mu k} (J_a)_{k nu}
            Mr = sum(J1[a][ms1.index(k), ms1.index(nu)] * mult(L, 1, mu, k) for k in ms1)
            Ml = sum(J1[a][ms1.index(mu), ms1.index(k)] * mult(L, 1, k, nu) for k in ms1)
            err_r = max(err_r, nrm((comm(Xh[a], M) - Mr) @ P2))
            err_l = max(err_l, nrm((comm(Lam[a], M) - Ml) @ P2))
crl = max(nrm(comm(Xh[a], Lam[b])) for a in range(3) for b in range(3))
rep(err_r < 1e-10 and err_l < 1e-10 and crl < 1e-12,
    f"C2 [Xh_a,M_f]=M_(Xh_a f) ({err_r:.1e}), [Lam_a,M_f]=M_(Lam_a f) ({err_l:.1e}), [Xh_a,Lam_b]=0 ({crl:.1e})")

# C3 ghost on compressed base functions
for L in (1, 2, 3):
    idx, pos, Xh, Lam = right_left(L)
    S12 = 1j * Xh[2]
    gerr = serr = 0.0
    vecs = []
    for l in range(0, 2 * L + 1):
        for mu in range(-l, l + 1):
            Y = mult(L, l, mu, 0)
            G = sum(comm(Xh[a], comm(Xh[a], Y)) for a in range(2))
            gerr = max(gerr, nrm(G - l * (l + 1) * Y) / nrm(Y))
            serr = max(serr, nrm(comm(S12, Y)))
            vecs.append(Y.reshape(-1))
    rank = np.linalg.matrix_rank(np.array(vecs), tol=1e-9)
    expect = sum(2 * l + 1 for l in range(2 * L + 1))
    zero_above = max(nrm(mult(L, l, mu, 0)) for l in (2 * L + 1, 2 * L + 2) for mu in range(-l, l + 1))
    rep(gerr < 1e-10 and serr < 1e-12 and rank == expect and zero_above < 1e-12,
        f"C3 L={L}: ghost sum_(a=1,2)[Xh_a,[Xh_a,Y_l]] = l(l+1) Y_l ({gerr:.1e}), [S_12,Y]=0, "
        f"rank {rank} = sum_(l<=2L)(2l+1) = {expect}; Y_l = 0 for l > 2L")

# C4 bundle redundancy; x_i = R(g)_{i3} with spherical-to-Cartesian U
Lc = [np.zeros((3, 3), complex) for _ in range(3)]
for a in range(3):
    for i in range(3):
        for k in range(3):
            Lc[a][i, k] = -1j * eps[a, i, k]
w, v = np.linalg.eigh(Lc[2])
v1 = v[:, np.argmin(np.abs(w - 1))]
Lminus = Lc[0] - 1j * Lc[1]
v0 = Lminus @ v1 / np.sqrt(2)
vm = Lminus @ v0 / np.sqrt(2)
U = np.column_stack([v1, v0, vm])
ph = U[2, 1] / abs(U[2, 1])
U = U / ph                               # make the z-component of v0 real positive
Uerr = max(nrm(U @ J1[a] @ U.conj().T - Lc[a]) for a in range(3))
rep(Uerr < 1e-12, f"C4 spherical-to-Cartesian U: U J^(1)_a U^dag = L_a ({Uerr:.1e})")
for L in (1, 2, 3):
    idx, pos, Xh, Lam = right_left(L)
    Mx = []
    for i in range(3):
        Mi = sum(U[i, ms1.index(mu)] * np.conj(U[2, 1]) * mult(L, 1, mu, 0) for mu in ms1)
        Mx.append(Mi)
    herm = max(nrm(M - M.conj().T) for M in Mx)
    Rd = sum(Mx[i] @ Lam[i] for i in range(3))
    c = np.trace(Rd @ Xh[2].conj().T) / np.trace(Xh[2] @ Xh[2].conj().T)
    err = nrm(Rd - c * Xh[2])
    rep(herm < 1e-12 and err < 1e-10 and abs(abs(c) - 1) < 1e-10,
        f"C4 L={L}: P M_(x_i) P Hermitian; sum_i (P M_(x_i) P) Lam_i = c Xh_3, c = {c.real:+.6f}{c.imag:+.6f}i (err {err:.1e})")
    # C5 noncommutativity and support of the product defect
    cxy = nrm(comm(Mx[0], Mx[1]))
    PL1 = block_proj(L, L - 1, idx)
    dmax_low = dmax_top = 0.0
    for i in range(3):
        for k in range(3):
            # x_i x_k as a function: compute M_{x_i x_k} on a larger space and compress
            Lb = L + 1
            idb, posb, _, _ = right_left(Lb)
            Mb = [sum(U[q, ms1.index(mu)] * np.conj(U[2, 1]) * mult(Lb, 1, mu, 0) for mu in ms1) for q in range(3)]
            Pb = block_proj(Lb, L, idb)
            keep = [t for t, b in enumerate(idb) if b[0] <= L]
            Mprod = (Mb[i] @ Mb[k])[np.ix_(keep, keep)]       # P M_{x_i x_k} P (exact: M_x preserves l-range by 1)
            defect = Mx[i] @ Mx[k] - Mprod
            dmax_low = max(dmax_low, nrm(defect @ PL1))
            dmax_top = max(dmax_top, nrm(defect))
    rep(cxy > 1e-3 and dmax_low < 1e-12 and dmax_top > 1e-3,
        f"C5 L={L}: |[P M_x P, P M_y P]| = {cxy:.3f}; product defect on blocks j<L {dmax_low:.1e}, on block L {dmax_top:.3f}")

# C6 Berezin-Toeplitz subspace (right weight n = j) not preserved by Xh_1
L = 2
idx, pos, Xh, Lam = right_left(L)
W = np.diag([1.0 if (b[0] == L and b[2] == L) else 0.0 for b in idx])
leak = nrm((np.eye(len(idx)) - W) @ Xh[0] @ W)
leakL = nrm((np.eye(len(idx)) - W) @ Lam[0] @ W)
rep(leak > 0.5 and leakL < 1e-12,
    f"C6 span(phi^j_(m,n=j)) is Lam-invariant (leak {leakL:.1e}) but not Xh_1-invariant (leak {leak:.3f})")

print()
print("ALL PASS" if all(res) else "SOME FAIL")
