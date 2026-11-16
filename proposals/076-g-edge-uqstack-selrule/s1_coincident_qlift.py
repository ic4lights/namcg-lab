"""076 s1: exact U(q)-lift of the block-cut edge charge for coincident caps.

Setting (065/072 edge data, one compact fuzzy factor, one cap):
  single copy: su(2) irrep of dimension N on C^N, X^a = nu * sum_b A[a,b] J[b],
  Theta = orthogonal projector on the M largest eigenvalues of n.J,
  momenta Pi^a Hermitian (state input).
  Block-cut edge charge (appH Row length paragraph):
      Q = -2i sum_a ( X^a_{S,Sb} Pi^a_{Sb,S} - Pi^a_{S,Sb} X^a_{Sb,S} ),
      with S the block (image of Theta) and Sb its complement.
  Coincident q-copy background: X^a~ = I_q (x) X^a, Theta~ = I_q (x) Theta
  (q coincident fuzzy spheres, reducible representation = q coincident caps).

Checks (exact finite-N matrix algebra):
  (a) single-copy rank-1 edge datum: Theta X^a Thetabar has rank <= 1;
  (b) COPY-INVARIANT STATE Pi^a~ = I_q (x) Pi^a: Q~ = I_q (x) Q exactly;
      nonzero spectrum of Q~ = nonzero spectrum of Q, each eigenvalue with
      multiplicity exactly q; moments Tr Q~^{2p} = q Tr Q^{2p}, p = 1..4;
      rank Q~ = q rank Q;
  (c) GENERIC STATE Pi^a~ full Hermitian on C^{qN}: rank Q~ = 2q (same rank
      as the copy-invariant case), but the 2q nonzero eigenvalues are simple
      (least pairwise gap reported) - the multiplicity q of (b) is a property
      of the state, not of the background alone;
  (d) edge operator E = sum Theta X Thetabar X Theta (Pi-free):
      rank E~ = q rank E, spectrum of E~ = spectrum of E repeated q times.

Run: python -I proposals/076-g-edge-uqstack-selrule/s1_coincident_qlift.py
Expected invariants: max deviations (lift, spec, moments, rank, E) < 1e-9;
generic-state least |gap| between consecutive nonzero eigenvalues > 0.05;
rank Q~ = rank Q_lift = q rank Q and #nz = q rank Q in every case;
last line 'PASS s1'.
"""
import numpy as np

rng = np.random.default_rng(76001)


def su2(N):
    j3 = np.diag([(N - 1) / 2 - i for i in range(N)]).astype(complex)
    jp = np.zeros((N, N), complex)
    for i in range(1, N):
        jp[i - 1, i] = np.sqrt(i * (N - i))
    jm = jp.conj().T
    return [(jp + jm) / 2, (jp - jm) / (2j), j3]


def cap_projector(J, n, M):
    nj = n[0] * J[0] + n[1] * J[1] + n[2] * J[2]
    ev, evec = np.linalg.eigh(nj)
    order = np.argsort(-np.real(ev))
    V = evec[:, order[:M]]
    return V @ V.conj().T


def edge_charge(Xs, Th, Pis):
    Tb = np.eye(Th.shape[0], dtype=complex) - Th
    A = np.zeros_like(Th)
    for x, pi in zip(Xs, Pis):
        A += (Th @ x @ Tb) @ (Tb @ pi @ Th)
    return -2j * (A - A.conj().T)


def nonzero_sorted(Q, tol=1e-9):
    ev = np.linalg.eigvalsh(Q)
    thr = tol * max(1.0, np.abs(ev).max())
    return np.sort(ev[np.abs(ev) > thr])


def rank_tol(Q, tol=1e-9):
    s = np.linalg.svd(Q, compute_uv=False)
    return int((s > tol * max(1.0, s.max())).sum())


worst = {'lift': 0.0, 'spec': 0.0, 'mom': 0.0, 'rank': 0, 'erank': 0,
         'espec': 0.0, 'rank1': 0}
gapmin = 1e9
rows = []
for N in (6, 8, 10):
    J = su2(N)
    for q in (2, 3):
        nu = 1.0 + 0.3 * rng.random()
        A = rng.normal(size=(3, 3))
        n = rng.normal(size=3)
        n = n / np.linalg.norm(n)
        M = int(rng.integers(2, N - 1))
        Th = cap_projector(J, n, M)
        X = [nu * sum(A[a, b] * J[b] for b in range(3)) for a in range(3)]
        Pi = []
        for _ in range(3):
            g = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
            Pi.append(g + g.conj().T)
        # (a) rank-1 edge datum for each direction
        Tb = np.eye(N, dtype=complex) - Th
        for a in range(3):
            worst['rank1'] += int(rank_tol(Th @ X[a] @ Tb) > 1)
        Q1 = edge_charge(X, Th, Pi)
        r1 = rank_tol(Q1)
        e1 = nonzero_sorted(Q1)
        # (b) copy-invariant state lift
        Iq = np.eye(q, dtype=complex)
        Xl = [np.kron(Iq, x) for x in X]
        Thl = np.kron(Iq, Th)
        Pil = [np.kron(Iq, p) for p in Pi]
        Ql = edge_charge(Xl, Thl, Pil)
        el = nonzero_sorted(Ql)
        pred = np.sort(np.tile(e1, q))
        worst['lift'] = max(worst['lift'], float(np.abs(Ql - np.kron(Iq, Q1)).max()))
        worst['spec'] = max(worst['spec'], float(np.abs(el - pred).max())
                            if len(el) == len(pred) else 1e9)
        for p in range(1, 5):
            lhs = float(np.trace(np.linalg.matrix_power(Ql, 2 * p)).real)
            rhs = q * float(np.trace(np.linalg.matrix_power(Q1, 2 * p)).real)
            worst['mom'] = max(worst['mom'], abs(lhs - rhs) / max(1.0, abs(rhs)))
        worst['rank'] = max(worst['rank'], abs(rank_tol(Ql) - q * r1))
        # (c) generic state on the same coincident background
        Pil_g = []
        for _ in range(3):
            g = rng.normal(size=(q * N, q * N)) + 1j * rng.normal(size=(q * N, q * N))
            Pil_g.append(g + g.conj().T)
        Qlg = edge_charge(Xl, Thl, Pil_g)
        eg = nonzero_sorted(Qlg)
        gap = float(np.abs(np.diff(eg)).min())
        gapmin = min(gapmin, gap)
        rg = rank_tol(Qlg)
        # (d) edge operator E (Pi-free), copy-invariant lift
        Tbl = np.eye(q * N, dtype=complex) - Thl
        E1 = sum((Th @ x @ Tb) @ (Tb @ x @ Th) for x in X)
        El = sum((Thl @ x @ Tbl) @ (Tbl @ x @ Thl) for x in Xl)
        sE1 = np.sort(np.linalg.eigvalsh(E1))
        sE1 = sE1[sE1 > 1e-9 * max(1.0, sE1.max())]
        sEl = np.sort(np.linalg.eigvalsh(El))
        sEl = sEl[sEl > 1e-9 * max(1.0, sEl.max())]
        worst['erank'] = max(worst['erank'], abs(len(sEl) - q * len(sE1)))
        predE = np.sort(np.tile(sE1, q))
        worst['espec'] = max(worst['espec'], float(np.abs(sEl - predE).max())
                             if len(sEl) == len(predE) else 1e9)
        rows.append((N, q, M, r1, rank_tol(Ql), rg, len(eg), gap))

print('rank-1 datum violations: %d' % worst['rank1'])
print('max |Q~ - I_q (x) Q| (copy-invariant): %.3e' % worst['lift'])
print('max spectrum multiplicity-q deviation: %.3e' % worst['spec'])
print('max relative moment deviation Tr Q~^{2p} = q Tr Q^{2p}: %.3e' % worst['mom'])
print('max |rank Q~ - q rank Q|: %d' % worst['rank'])
print('generic state: least |gap| between consecutive nonzero eigenvalues: %.6f' % gapmin)
print('edge operator: max |rank E~ - q rank E|: %d ; max spectrum deviation: %.3e'
      % (worst['erank'], worst['espec']))
print('cases (N,q,M,rankQ1,rankQlift,rankQgeneric,#nz,mingap):')
for r in rows:
    print('  N=%2d q=%d M=%2d r1=%d rlift=%d rgeneric=%d nnz=%d mingap=%.6f' % r)
# rows: (N, q, M, r1, rlift, rgeneric, nnz, mingap); every nonzero-spectrum
# count must equal q * rank Q(one copy); generic state has rank 2q = q * r1
# (rank Q = 2 for a single cap).
ok = (worst['lift'] < 1e-9 and worst['spec'] < 1e-9 and worst['mom'] < 1e-9
      and worst['rank'] == 0 and worst['rank1'] == 0 and worst['erank'] == 0
      and worst['espec'] < 1e-9 and gapmin > 0.05
      and all(r[3] == 2 and r[4] == r[1] * r[3] and r[5] == r[1] * r[3]
              and r[6] == r[1] * r[3] for r in rows))
print('all checks inside thresholds:', ok)
assert ok
print('PASS s1')
