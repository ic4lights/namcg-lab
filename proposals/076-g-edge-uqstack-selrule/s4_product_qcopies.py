"""076 s4: product block-cut testbed with q_f coincident copies per factor.

072/075 product conventions (067 machinery, r1_moment_decomposition.py):
factor f = su(2) irrep dim N with X_f = A_f J, block Theta = Theta_1 (x)
Theta_2 (interval caps), E = sum_I Theta X^I Thetabar X^I Theta, gap-free
spectrum { s1^2 (M2-1), s2^2 (M1-1), s1^2+s2^2 (1) }, s_f^2 = k_f M_f(N-M_f).
Here factor f is REPLACED by q_f coincident copies: factor f matrices act as
I_{q_f} (x) (A_f J) on C^{q_f N}. Index order used throughout:
    C^{q1} (x) C^{q2} (x) C^N (x) C^N    (copies first, then factors),
so all lifts are plain Kronecker products with I_{q1 q2} or I_{q1}.
Charge as in s1: Q = -2i sum_I ( X^I_{S,Sb} Pi^I_{Sb,S} - h.c. ).

Checks:
  (a) edge operator (state-free): spectrum of E with copies = the single-copy
      multiset tiled q_1 q_2 times, EXACTLY, and
      rank E = q_1 q_2 (M_1 + M_2 - 1): background coincidence multiplies E;
  (b) FULLY copy-invariant state Pi^I = I_{q_1 q_2} (x) pi: Q = I (x) Q_0
      exactly (operator identity), spectrum = single-copy charge spectrum
      tiled q_1 q_2 times (uniform depth q_1 q_2 on every charge eigenvalue);
  (c) state copy-invariant in factor 1 only, Pi^I = I_{q_1} (x) pi_01 with
      pi_01 generic on C^{q_2 N} (x) C^N (x) C^N: then Q = I_{q_1} (x) Q_01
      exactly - the multiplicity q_1 applies to EVERY eigenvalue, including
      the factor-2 ones; copy invariance in one factor cannot raise the depth
      of one factor's rows alone;
  (d) generic state (full Gaussian Pi on the whole space): all nonzero charge
      eigenvalues simple (least gap reported).

Consequence recorded for the proposal: within the Gaussian product testbed the
charge-spectrum multiplicity realized by copy-invariant states is UNIFORM over
the whole spectrum (depth 1, q_1, q_2 or q_1 q_2); the per-factor asymmetric
stacked pattern (ell_1^{q_1}, ell_2^{q_2}) with q_1 != q_2 is not the
multiplicity pattern of the charge spectrum for any of these states.

Run: python -I proposals/076-g-edge-uqstack-selrule/s4_product_qcopies.py
Expected invariants: max deviations (E tiling, Q lifts, rank) < 1e-8;
generic-state least gap > 0.02; last line 'PASS s4'.
"""
import numpy as np

rng = np.random.default_rng(76004)


def su2(N):
    j3 = np.diag([(N - 1) / 2 - i for i in range(N)]).astype(complex)
    jp = np.zeros((N, N), complex)
    for i in range(1, N):
        jp[i - 1, i] = np.sqrt(i * (N - i))
    jm = jp.conj().T
    return [(jp + jm) / 2, (jp - jm) / (2j), j3]


def interval(M, N):
    return np.diag([1.0 if i < M else 0.0 for i in range(N)]).astype(complex)


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


def full_herm(d):
    g = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    return g + g.conj().T


worst = {'etile': 0.0, 'erank': 0.0, 'lift_full': 0.0, 'tile_full': 0.0,
         'lift_f1': 0.0, 'tile_f1': 0.0, 'assoc': 0.0}
gapmin_g = 1e9
for N in (5, 6):
    for q1, q2 in ((2, 1), (1, 2), (2, 2), (3, 2)):
        A1 = rng.normal(size=(3, 3))
        A2 = rng.normal(size=(3, 3))
        M1 = int(rng.integers(2, N - 1))
        M2 = int(rng.integers(2, N - 1))
        J = su2(N)
        Y1 = [sum(A1[a, b] * J[b] for b in range(3)) for a in range(3)]
        Y2 = [sum(A2[a, b] * J[b] for b in range(3)) for a in range(3)]
        Iq = np.eye(q1 * q2, dtype=complex)
        IN = np.eye(N, dtype=complex)
        # single-copy product data on C^N (x) C^N
        X0 = [np.kron(y, IN) for y in Y1] + [np.kron(IN, y) for y in Y2]
        Th0 = np.kron(interval(M1, N), interval(M2, N))
        Tb0 = np.eye(N * N, dtype=complex) - Th0
        # one-copy-per-space copies on C^{q1} (x) C^{q2} (x) C^N (x) C^N
        Xf1 = [np.kron(Iq, np.kron(y, IN)) for y in Y1]
        Xf2 = [np.kron(Iq, np.kron(IN, y)) for y in Y2]
        X = Xf1 + Xf2
        Th = np.kron(Iq, np.kron(interval(M1, N), interval(M2, N)))
        Tb = np.eye(q1 * q2 * N * N, dtype=complex) - Th
        # (a) E tiling vs single-copy base (state-free)
        E0 = sum(Th0 @ x @ Tb0 @ x @ Th0 for x in X0)
        Ec = sum(Th @ x @ Tb @ x @ Th for x in X)
        s0 = np.linalg.eigvalsh(np.real_if_close(E0, tol=1e8).astype(float))
        sc = np.linalg.eigvalsh(np.real_if_close(Ec, tol=1e8).astype(float))
        s0 = s0[s0 > 1e-9 * max(1.0, s0.max())]
        sc = sc[sc > 1e-9 * max(1.0, sc.max())]
        q = q1 * q2
        predE = np.sort(np.tile(s0, q))
        worst['etile'] = max(worst['etile'], abs(predE - sc).max()
                             if len(predE) == len(sc) else 1e9)
        worst['erank'] = max(worst['erank'], abs(len(sc) - q * (M1 + M2 - 1)))
        # (b) fully copy-invariant state
        Pi0 = [full_herm(N * N) for _ in range(6)]
        Q0 = edge_charge(X0, Th0, Pi0)
        e0 = nonzero_sorted(Q0)
        Pil = [np.kron(Iq, p) for p in Pi0]
        Ql = edge_charge(X, Th, Pil)
        el = nonzero_sorted(Ql)
        worst['lift_full'] = max(worst['lift_full'], float(np.abs(Ql - np.kron(Iq, Q0)).max()))
        worst['tile_full'] = max(worst['tile_full'], float(np.abs(el - np.sort(np.tile(e0, q))).max())
                                  if len(el) == q * len(e0) else 1e9)
        # (c) copy-invariant in factor 1 only: group C^{q1} (x) (C^{q2} (x) C^N (x) C^N)
        Iq2 = np.eye(q2, dtype=complex)
        X01 = [np.kron(Iq2, np.kron(y, IN)) for y in Y1]
        X01 += [np.kron(Iq2, np.kron(IN, y)) for y in Y2]
        Th01 = np.kron(Iq2, np.kron(interval(M1, N), interval(M2, N)))
        # associativity sanity: full data = I_{q1} (x) reduced data
        worst['assoc'] = max(
            worst['assoc'],
            max(float(np.abs(xf - np.kron(np.eye(q1, dtype=complex), xr)).max())
                for xf, xr in zip(X, X01)),
            float(np.abs(Th - np.kron(np.eye(q1, dtype=complex), Th01)).max()))
        Pi01 = [full_herm(q2 * N * N) for _ in range(6)]
        Q01 = edge_charge(X01, Th01, Pi01)
        e01 = nonzero_sorted(Q01)
        Pil1 = [np.kron(np.eye(q1, dtype=complex), p) for p in Pi01]
        Ql1 = edge_charge(X, Th, Pil1)
        el1 = nonzero_sorted(Ql1)
        worst['lift_f1'] = max(worst['lift_f1'], float(np.abs(Ql1 - np.kron(np.eye(q1, dtype=complex), Q01)).max()))
        worst['tile_f1'] = max(worst['tile_f1'], float(np.abs(el1 - np.sort(np.tile(e01, q1))).max())
                                if len(el1) == q1 * len(e01) else 1e9)
        # (d) generic state: simple spectrum
        Pg = [full_herm(q1 * q2 * N * N) for _ in range(6)]
        eg = nonzero_sorted(edge_charge(X, Th, Pg))
        if len(eg) > 1:
            gapmin_g = min(gapmin_g, float(np.abs(np.diff(eg)).min()))

print('E: max tiling (q1q2) deviation: %.3e ; max rank error: %.0f'
      % (worst['etile'], worst['erank']))
print('Q fully copy-invariant: max |Q - I(x)Q0|: %.3e ; max tiling deviation: %.3e'
      % (worst['lift_full'], worst['tile_full']))
print('Q invariant in factor 1 only: max |Q - I_{q1}(x)Q01|: %.3e ; max tiling deviation: %.3e'
      % (worst['lift_f1'], worst['tile_f1']))
print('associativity sanity max deviation: %.3e' % worst['assoc'])
print('generic state: least gap between consecutive nonzero eigenvalues: %.6f' % gapmin_g)
ok = (worst['etile'] < 1e-8 and worst['erank'] == 0 and worst['lift_full'] < 1e-8
      and worst['tile_full'] < 1e-8 and worst['lift_f1'] < 1e-8
      and worst['tile_f1'] < 1e-8 and worst['assoc'] < 1e-12 and gapmin_g > 0.02)
print('all checks inside thresholds:', ok)
assert ok
print('PASS s4')
