"""077 s1: exact multiplicity-q is measure-zero and first-order fragile; the edge-row null cone.

Setting: 076 s1 coincident-copy data (su(2) irrep dim N, X^a = nu * A[a,b] J[b],
Theta = cap projector on M largest of n.J, X~ = I_q (x) X, Theta~ = I_q (x) Theta,
Q~ = -2i sum_a (X~^a_{S,Sb} Pi~^a_{Sb,S} - Pi~^a_{S,Sb} X~^a_{Sb,S}), 3 flavors,
Pi~ Hermitian (qN x qN). Reference ensemble: 3 iid standard complex-Gaussian
Hermitian momenta (iid-copy / product block ensemble of the 077 package).

Note: the single-copy block-cut charge is NOT +-symmetric (its two nonzero
eigenvalues are -2 Im(alpha) +/- 2 sqrt(Im^2 alpha + |w_perp|^2), appH row-length
paragraph), so the tiling statistic is the MULTSET violation
    D(Q~) = max_k (e_{(k+1)q-1} - e_{kq}) / max|e| on the 2q signed nonzero eigs e
(sorted ascending, consecutive blocks of q), which vanishes exactly when the
signed nonzero spectrum is a q-fold multiset. This replaces any +-pairing assumption.

Checks (numerical, finite N):
  (a) exact mult-q events among 6000 iid draws (q=2 N=6 M=3; q=3 N=9 M=4) with
      nu < 1e-7: expect 0 (exact tiling is a null set of the ensemble);
  (b) #nz(Q~) = 2q per event; D of the generic spectra is O(1) (report);
  (c) first-order breakdown at a copy-invariant base Q~(0) (D(Q~(0)) < 1e-12):
      D vs the normalized perturbation size t: D/t converges to a nonzero limit
      -> exact tiling breaks at FIRST order in a generic transverse direction;
  (d) edge-row null cone: Hermitian G with P_S G P_T + P_T G P_S = 0 removed,
      P_S = span of the edge vectors |v_alpha), P_T = block-cap projector: the
      charge is EXACTLY invariant under such directions (invisible), while
      generic directions split at first order.

Run: python -I proposals/077-g-selrule-copyinv/s1_typicality_exact.py
Expected invariants: (a) 0 exact events; (b) 0 bad events, generic nu > 0.1;
(c) base nu < 1e-12, D/t in [0.5, 2] * plateau across three decades, plateau
limit > 0.2; (d) null-cone charge deviation < 1e-9, its nu < 1e-12, generic
D(t=1) > 0.2; last line 'PASS s1'.
"""
import numpy as np

rng = np.random.default_rng(77001)


def su2(N):
    j3 = np.diag([(N - 1) / 2 - i for i in range(N)]).astype(complex)
    jp = np.zeros((N, N), complex)
    for i in range(1, N):
        jp[i - 1, i] = np.sqrt(i * (N - i))
    return [(jp + jp.conj().T) / 2, (jp - jp.conj().T) / 2j, j3]


def cap_projector(J, n, M):
    nj = n[0] * J[0] + n[1] * J[1] + n[2] * J[2]
    ev, evec = np.linalg.eigh(nj)
    order = np.argsort(-np.real(ev))
    V = evec[:, order[:M]]
    return V @ V.conj().T, evec[:, order], nj


def edge_charge(Xs, Th, Pis):
    Tb = np.eye(len(Th), dtype=complex) - Th
    A = sum((Th @ x @ Tb) @ (Tb @ pi @ Th) for x, pi in zip(Xs, Pis))
    return -2j * (A - A.conj().T)


def charge_from_G(Xl, Thl, Gs):
    Tb = np.eye(len(Thl), dtype=complex) - Thl
    A = sum((Thl @ x @ Tb) @ (Tb @ g @ Thl) for x, g in zip(Xl, Gs))
    return -2j * (A - A.conj().T)


def herg(m):
    g = rng.normal(size=(m, m)) + 1j * rng.normal(size=(m, m))
    return g + g.conj().T


def signed_nz(Q, tol=1e-9):
    ev = np.linalg.eigvalsh(Q)
    thr = tol * max(1.0, np.abs(ev).max())
    return np.sort(ev[np.abs(ev) > thr])


def tiling_nu(Q, q, tol=1e-9):
    # q-fold-multiset violation: sorted signed nonzero eigs, consecutive blocks of
    # q (optimal fixed-size 1D clustering), max within-block spread / max|e|.
    e = signed_nz(Q, tol)
    if len(e) != 2 * q:
        return float('nan'), len(e)
    m = np.abs(e).max()
    blocks = [e[k * q:(k + 1) * q] for k in range(2)]
    d = max(float(b[-1] - b[0]) for b in blocks) / m
    return d, 2 * q


# ---- (a),(b): iid reference ensemble
bad_exact = bad_nnz = 0
nu_iid = []
for (N, q, M, nev) in ((6, 2, 3, 4000), (9, 3, 4, 2000)):
    J = su2(N)
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    Th, _, _ = cap_projector(J, n, M)
    A3 = rng.normal(size=(3, 3)); nuA = 1.2
    X = [nuA * sum(A3[a, b] * J[b] for b in range(3)) for a in range(3)]
    Iq = np.eye(q)
    Xl = [np.kron(Iq, x) for x in X]
    Thl = np.kron(Iq, Th)
    for _ in range(nev):
        Ql = edge_charge(Xl, Thl, [herg(q * N) for _ in range(3)])
        nuv, nnz = tiling_nu(Ql, q)
        if nnz != 2 * q:
            bad_nnz += 1
            continue
        if nuv < 1e-7:
            bad_exact += 1
        nu_iid.append(nuv)
print('(a) exact mult-q events (nu<1e-7) in 6000 iid draws: %d' % bad_exact)
print('(b) events with #nz != 2q: %d ; generic nu: median %.4f min %.4f'
      % (bad_nnz, float(np.median(nu_iid)), min(nu_iid)))

# ---- one fixed background + copy-invariant base for (c),(d)
N, q, M = 8, 2, 4
J = su2(N)
nn = rng.normal(size=3); nn /= np.linalg.norm(nn)
Th, evec_ord, njop = cap_projector(J, nn, M)
order = np.argsort(-np.real(np.linalg.eigvalsh(njop)))
A3 = rng.normal(size=(3, 3)); nuA = 1.1
X = [nuA * sum(A3[a, b] * J[b] for b in range(3)) for a in range(3)]
Iq = np.eye(q)
Xl = [np.kron(Iq, x) for x in X]
Thl = np.kron(Iq, Th)
qN = q * N
Pi0 = [herg(N) for _ in range(3)]
Q0 = edge_charge(Xl, Thl, [np.kron(Iq, p) for p in Pi0])
nu0, _ = tiling_nu(Q0, q)
Gp = [herg(qN) for _ in range(3)]
Qp = charge_from_G(Xl, Thl, Gp)
np0 = np.abs(np.linalg.eigvalsh(Qp)).max()
n0 = np.abs(np.linalg.eigvalsh(Q0)).max()

print('(c) base D(Q~(0)) = %.2e ; t, nu, D/t:' % nu0)
plateau = []
for k in range(4):
    t = 10.0 ** (-4 + k)
    nuv, _ = tiling_nu(Q0 + t * n0 / np0 * Qp, q)
    plateau.append(nuv / t)
    print('    t=%.1e  nu=%.3e  D/t=%.4f' % (t, nuv, nuv / t))
ratio_ok = all(0.5 < plateau[i] / plateau[-1] < 2.0 for i in range(3))
first_order = plateau[-1] > 0.2

# ---- (d) edge-row null cone (Hermitian, exact): remove P_S G P_T + h.c.
v1 = evec_ord[:, M]                       # edge vector just below the cap
Ps = np.kron(np.eye(q), np.outer(v1, v1.conj()))
Pt = np.kron(np.eye(q), Th)
Gn = [g - Ps @ g @ Pt - Pt @ g @ Ps for g in Gp]
dev = max(float(np.abs(charge_from_G(Xl, Thl, Gn)).max()) for _ in [0])
# exact block check: residual forbidden blocks
blk_res = max(float(np.abs(Ps @ g @ Pt).max()) for g in Gn)
nu_n, _ = tiling_nu(Q0 + n0 * 0 + charge_from_G(Xl, Thl, Gn), q)
nu_n = tiling_nu(Q0 + charge_from_G(Xl, Thl, Gn), q)[0]
nu_g1 = tiling_nu(Q0 + 1.0 * n0 / np0 * Qp, q)[0]
print('(d) null-cone: |dQ~| = %.3e (residual edge blocks %.3e): nu(Q~+dQ~) = %.3e ;'
      ' generic D(t=1) = %.4f' % (dev, blk_res, nu_n, nu_g1))

ok = (bad_exact == 0 and bad_nnz == 0 and min(nu_iid) > 0.1
      and nu0 < 1e-12 and ratio_ok and first_order
      and dev < 1e-9 and blk_res < 1e-12 and nu_n < 1e-12 and nu_g1 > 0.2)
print('all checks inside thresholds:', ok)
assert ok
print('PASS s1')
