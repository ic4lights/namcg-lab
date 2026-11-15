"""072 s1: exact edge-spectrum and moment decomposition for product blocks on
S^2 x S^2, derived from the 067-remote edge-operator machinery
(proposals/claude-remote/067-product-sphere-edge/e1_edge_operator.py, functions
su2/config and the proven per-site eigenvalue formula quoted there).

Checks (all at exact finite N, numpy):
  (a) E = sum_I Theta X^I Thetabar X^I Theta is diagonal (gap-free Omega) and
      matches the 067 per-site formula;
  (b) NEW: for 2 <= M1, M2 <= N-2 the nonzero spectrum of E is the multiset
      { s1^2 (M2-1 times), s2^2 (M1-1 times), s1^2+s2^2 (once) },
      s_f^2 = k_f M_f (N-M_f);
  (c) NEW: Tr E^p = (M2-1) s1^{2p} + (M1-1) s2^{2p} + (s1^2+s2^2)^p, p=1..5
      (relative accuracy);
  (d) rank E = M1+M2-1 and Tr E = M2 s1^2 + M1 s2^2 (relative);
  (e) direction-wise split: the factor-1 part E1 = sum_{a<=3} Theta X^a
      Thetabar X^a Theta has diagonal 1_Omega * (d1 (+) 1), d1 the
      single-factor interval edge diagonal (d1[M1-1] = s1^2, else 0), and
      likewise for factor 2.

Run: python -I proposals/072-g-edge-resum-dominant-rep/s1_moment_decomposition.py
Expected invariants: max absolute deviation (diag, site, spec, rank, kroneck)
< 1e-9; max relative deviation (mom, add) < 1e-12; last line 'PASS s1'.
"""
import numpy as np

rng = np.random.default_rng(72001)


def su2(N):
    j3 = np.diag([(N - 1) / 2 - i for i in range(N)]).astype(complex)
    jp = np.zeros((N, N), complex)
    for i in range(1, N):
        jp[i - 1, i] = np.sqrt(i * (N - i))
    jm = jp.conj().T
    return [(jp + jm) / 2, (jp - jm) / (2j), j3]


def config(N, A1, A2):
    J = su2(N)
    I = np.eye(N)
    X = [np.kron(sum(A1[a, b] * J[b] for b in range(3)), I) for a in range(3)]
    X += [np.kron(I, sum(A2[a, b] * J[b] for b in range(3))) for a in range(3)]
    return X


def per_site(N, Om, k1, k2):
    """067-proven per-site eigenvalue formula (same as e1_edge_operator.formula)."""
    E = np.zeros((N, N))
    for i1 in range(N):
        for i2 in range(N):
            if not Om[i1, i2]:
                continue
            e = 0.0
            if i1 - 1 >= 0 and not Om[i1 - 1, i2]:
                e += k1 * i1 * (N - i1)
            if i1 + 1 <= N - 1 and not Om[i1 + 1, i2]:
                e += k1 * (i1 + 1) * (N - i1 - 1)
            if i2 - 1 >= 0 and not Om[i1, i2 - 1]:
                e += k2 * i2 * (N - i2)
            if i2 + 1 <= N - 1 and not Om[i1, i2 + 1]:
                e += k2 * (i2 + 1) * (N - i2 - 1)
            E[i1, i2] = e
    return E


def kfac(A):
    return 0.25 * (A[:, 0] ** 2 + A[:, 1] ** 2).sum()


def fact_diag(N, M, k):
    """Single-factor interval-edge diagonal of Omega = {i < M}: s^2 at i = M-1."""
    d = np.zeros(N)
    d[M - 1] = k * M * (N - M)
    return d


worst = {'diag': 0.0, 'site': 0.0, 'spec': 0.0, 'momrel': 0.0,
         'rank': 0.0, 'addrel': 0.0, 'kroneck': 0.0}
cases = []
for N in (6, 9, 12):
    ii1, ii2 = np.meshgrid(np.arange(N), np.arange(N), indexing='ij')
    for trial in range(4):
        A1 = rng.normal(size=(3, 3))
        A2 = rng.normal(size=(3, 3))
        k1, k2 = kfac(A1), kfac(A2)
        X = config(N, A1, A2)
        M1 = int(rng.integers(2, N - 1))
        M2 = int(rng.integers(2, N - 1))
        Om = (ii1 < M1) & (ii2 < M2)
        mask = Om.reshape(-1).astype(float)
        Th = np.diag(mask)
        Tb = np.eye(N * N) - Th
        Eop = sum(Th @ x @ Tb @ x @ Th for x in X)
        Eop = np.real_if_close(Eop, tol=1e6).astype(float)
        worst['diag'] = max(worst['diag'], np.abs(Eop - np.diag(np.diag(Eop))).max())
        Ef = per_site(N, Om, k1, k2)
        worst['site'] = max(worst['site'], np.abs(np.diag(Eop) - Ef.reshape(-1)).max())
        # (b) spectrum multiset
        s1sq = k1 * M1 * (N - M1)
        s2sq = k2 * M2 * (N - M2)
        pred = np.sort(np.concatenate([np.full(M2 - 1, s1sq), np.full(M1 - 1, s2sq),
                                       [s1sq + s2sq]]))
        got = np.sort(np.diag(Eop)[np.diag(Eop) > 1e-12])
        worst['spec'] = max(worst['spec'], abs(pred - got).max() if len(pred) == len(got) else 1e9)
        # (c) moments p = 1..5, (d) rank and Tr E additivity
        d = np.diag(Eop)
        for p in range(1, 6):
            lhs = (d ** p).sum()
            rhs = (M2 - 1) * s1sq ** p + (M1 - 1) * s2sq ** p + (s1sq + s2sq) ** p
            worst['momrel'] = max(worst['momrel'], abs(lhs - rhs) / max(abs(rhs), 1e-12))
        rank = int((d > 1e-12).sum())
        worst['rank'] = max(worst['rank'], abs(rank - (M1 + M2 - 1)))
        rhs_add = M2 * s1sq + M1 * s2sq
        worst['addrel'] = max(worst['addrel'], abs(d.sum() - rhs_add) / rhs_add)
        cases.append((N, M1, M2, k1, k2, s1sq, s2sq))
        # (e) direction-wise split
        d1 = fact_diag(N, M1, k1)
        d2 = fact_diag(N, M2, k2)
        E1 = sum(Th @ x @ Tb @ x @ Th for x in X[:3])
        E2 = sum(Th @ x @ Tb @ x @ Th for x in X[3:])
        E1 = np.real_if_close(E1, tol=1e6).astype(float)
        E2 = np.real_if_close(E2, tol=1e6).astype(float)
        k1exp = mask * np.outer(d1, np.ones(N)).reshape(-1)
        k2exp = mask * np.outer(np.ones(N), d2).reshape(-1)
        worst['kroneck'] = max(worst['kroneck'],
                               np.abs(np.diag(E1) - k1exp).max(),
                               np.abs(np.diag(E2) - k2exp).max())

for key in sorted(worst):
    print('max %-8s deviation: %.3e' % (key, worst[key]))
print('cases (N,M1,M2,k1,k2,s1^2,s2^2):')
for c in cases:
    print('  N=%2d M1=%2d M2=%2d k1=%.6f k2=%.6f s1sq=%10.4f s2sq=%10.4f' % c)
ok = (worst['diag'] < 1e-9 and worst['site'] < 1e-9 and worst['spec'] < 1e-9
      and worst['rank'] == 0.0 and worst['kroneck'] < 1e-9
      and worst['momrel'] < 1e-12 and worst['addrel'] < 1e-12)
print('all checks inside thresholds:', ok)
assert ok
print('PASS s1')
