"""075 shared code. Imports the 068 linearisation core read-only (no bytecode written).

Matrix equation with the cubic term (derived in s1, g = 1, C_{mnl} = i c eps_{mnls} v^s):
   E_b = [D^a,[D_a,D_b]] + (c/2) eps_{bcdf} v^f [D^c,D^d] = 0,     X_a = i D_a.
With [D_c,D_d] = -T_cd^e D_e + 1/2 R_cd^{fg} S_fg + F_cd and the core's B1, B2 (first two brackets of the
quartic term), the D_e and 1/2 S_de coefficients of E_b are
   B1_b^e - (c/2) eps_b^{cd}_f v^f T_cd^e ,     B2_b^{de} + (c/2) eps_b^{cd}_f v^f R_cd^{de}.
In section values at the fibre point u the matrix-index vector v is replaced by w = u^{-1} v; cw := c * w.
"""
import itertools, os, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(HERE, '..', '068-d1-torsion-nonzero')))
import numpy as np
import core as K

eta = K.ETA
etai = np.linalg.inv(eta)
eps = np.zeros((4, 4, 4, 4))
for p in itertools.permutations(range(4)):
    eps[p] = np.linalg.det(np.eye(4)[list(p)])
epsL = -eps                                   # eps_{0123} = -1  (eps^{0123} = +1)
EPS_MIX = np.einsum('bxyf,xc,yd->bcdf', epsL, etai, etai)   # eps_b^{cd}_f
PAIRS = K.PAIRS


def brackets_c(cbar, wbar, Eop, vec, cw):
    """Full first two brackets with the cubic term; returns (B1, B2) as (background, linear) pairs."""
    B1, B2, T, Rup = K.brackets(cbar, wbar, Eop, vec)
    k = np.einsum('bcdf,f->bcd', EPS_MIX, np.asarray(cw, dtype=complex))   # eps_b^{cd}_f cw^f
    add1 = K.scal(-0.5, K.lin('bcd,cde->be', k, T))
    add2 = K.scal(0.5, K.lin('bcd,cdfe->bfe', k, Rup))
    return K.add(B1, add1), K.add(B2, add2)


def background_residual_c(cbar, wbar, cw):
    B1, B2 = brackets_c(cbar, wbar, K.chars(np.zeros(4)), np.zeros(K.NF), cw)
    return float(np.abs(B1[0]).max()), float(np.abs(B2[0]).max())


def M_c(cbar, wbar, Eop, cw):
    Eop = np.asarray(Eop, dtype=complex); N = Eop.shape[-1]
    M = np.zeros((K.NF * N, K.NF * N), dtype=complex)
    for n in range(K.NF * N):
        v = np.zeros(K.NF * N); v[n] = 1.0
        B1, B2 = brackets_c(cbar, wbar, Eop, v, cw)
        M[:, n] = K.pack(B1[1], B2[1])
    return M


def bivector_index(X):
    """Coordinates of an antisymmetric 4x4 X in the 6 PAIRS."""
    return np.array([X[c, d] for (c, d) in PAIRS])


def stabiliser_basis(v):
    """Basis (as 6-vectors in PAIRS) of the bivectors X^{cd} with X^{cd} eta_{de} v^e = 0 (Lie algebra of Stab(v))."""
    M = np.zeros((4, 6))
    for k, (c, d) in enumerate(PAIRS):
        X = np.zeros((4, 4)); X[c, d] = 1; X[d, c] = -1
        M[:, k] = X @ eta @ v
    _, s, Vh = np.linalg.svd(M)
    r = int((s > 1e-10).sum())
    return Vh[r:].T                             # 6 x (6 - r)


def reduction(Hb, N):
    """Embedding P: (16 + 4*dimH) N -> 40 N (fields) and projection Q: 40 N -> (16 + 4*dimH) N (equations)
    for a class whose fibre is the subgroup with Lie algebra spanned by the columns of Hb."""
    dH = Hb.shape[1]
    nf = 16 + 4 * dH
    P = np.zeros((K.NF, nf))
    P[:16, :16] = np.eye(16)
    for a in range(4):
        P[16 + 6 * a:16 + 6 * a + 6, 16 + dH * a:16 + dH * a + dH] = Hb
    Q = P.T.copy()
    Q[16:, :] = 0
    for a in range(4):
        Q[16 + dH * a:16 + dH * a + dH, 16 + 6 * a:16 + 6 * a + 6] = np.linalg.pinv(Hb)
    I = np.eye(N)
    return np.kron(P, I), np.kron(Q, I)


def rank(M, tol=1e-9):
    s = np.linalg.svd(M, compute_uv=False)
    return int((s > tol * max(1.0, s[0])).sum()), s


def boost(i, th):
    L = np.eye(4); L[0, 0] = L[i, i] = np.cosh(th); L[0, i] = L[i, 0] = np.sinh(th); return L


def rot(i, j, th):
    L = np.eye(4); L[i, i] = L[j, j] = np.cos(th); L[i, j] = -np.sin(th); L[j, i] = np.sin(th); return L


def rand_lorentz(rng, k=3, scale=0.8):
    L = np.eye(4)
    for _ in range(k):
        i, j = rng.choice([1, 2, 3], 2, replace=False)
        L = L @ boost(int(rng.integers(1, 4)), scale * rng.normal()) @ rot(int(i), int(j), rng.normal())
    return L


def cfj_matrix(q, cw):
    """Order-zero / single one-form sector about flat: Q_b[A] + (c/2) eps_b^{cd}_f w^f F_cd[A], F = dA,
    for A ~ exp(i q.y): -(q^2 A_b - q_b q.A) + i eps_b^{cd}_f cw^f q_c A_d."""
    q = np.asarray(q, dtype=complex)
    qu = etai @ q
    q2 = q @ qu
    M = -(q2 * np.eye(4) - np.outer(q, qu))
    M = M + 1j * np.einsum('bcdf,c,f->bd', EPS_MIX, q, np.asarray(cw, dtype=complex))
    return M
