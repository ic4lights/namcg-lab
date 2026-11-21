"""076 s2: band-separated two-cap charge spectrum and its coincident q-copy lift.

One compact fuzzy factor (su(2) irrep dim N, J3 eigenbasis), one axis n = e3,
two caps on that axis: Theta = Theta_1 + Theta_2, Theta_1 = {i < M1} (top),
Theta_2 = {i >= N - M2} (bottom), middle width D = N - M1 - M2.
Momenta Pi^a = band-limited Hermitian in the J3 eigenbasis: (Pi)_{ij} = 0 for
|i - j| > W. Then the two-cap block-cut charge
    Q = -2i sum_a ( X^a_{S,Sb} Pi^a_{Sb,S} - h.c. )
splits EXACTLY into the union of the two single-cap charges because the edge
vectors are basis vectors (intervals on the J3 axis) and the band-limited
rows of Pi attached to the two cap edges have disjoint supports when the edge
separation D - 1 exceeds 2W (appH Row length paragraph: "separated by more
than twice the band width of Pi^a ... union of two single-cap pairs (exact)").

Checks:
  (a) union exactness: nonzero spectrum of Q(two caps) = multiset union of the
      nonzero spectra of Q(cap 1 alone) and Q(cap 2 alone), same Pi; max
      deviation < 1e-9;
  (b) multiplicity 1: all four nonzero eigenvalues simple (least pairwise gap
      reported);
  (c) coincident q-copy lift (q = 2, 3), copy-invariant band-limited state
      Pi~ = I_q (x) Pi: Q~ = I_q (x) Q exactly and the spectrum is the
      single-copy spectrum tiled q times - each cap eigenvalue has
      multiplicity exactly q;
  (d) control: for FULL (non-band-limited) Gaussian Pi the union exactness
      fails (deviation reported, large) - the band hypothesis in the exact
      union statement is essential.

Run: python -I proposals/076-g-edge-uqstack-selrule/s2_band_sep_two_caps.py
Expected invariants: max deviation (a) < 1e-9, (c) < 1e-9; least gap (b) > 0.05;
control deviation (d) > 1e-3; last line 'PASS s2'.
"""
import numpy as np

rng = np.random.default_rng(76002)


def su2(N):
    j3 = np.diag([(N - 1) / 2 - i for i in range(N)]).astype(complex)
    jp = np.zeros((N, N), complex)
    for i in range(1, N):
        jp[i - 1, i] = np.sqrt(i * (N - i))
    jm = jp.conj().T
    return [(jp + jm) / 2, (jp - jm) / (2j), j3]


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


def band_herm(N, W):
    g = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
    idx = np.abs(np.arange(N)[:, None] - np.arange(N)[None, :])
    g[idx > W] = 0.0
    return g + g.conj().T


worst = {'union': 0.0, 'lift': 0.0, 'tile': 0.0}
gapmin = 1e9
ctrl = []
for N, M1, M2, W in ((11, 3, 3, 1), (12, 3, 3, 2), (14, 4, 4, 2)):
    J = su2(N)
    A = rng.normal(size=(3, 3))
    nu = 1.0 + 0.3 * rng.random()
    X = [nu * sum(A[a, b] * J[b] for b in range(3)) for a in range(3)]
    th1 = np.diag([1.0 if i < M1 else 0.0 for i in range(N)]).astype(complex)
    th2 = np.diag([1.0 if i >= N - M2 else 0.0 for i in range(N)]).astype(complex)
    Th = th1 + th2
    D = N - M1 - M2
    assert D - 1 > 2 * W, (N, M1, M2, W)  # band separation condition
    Pi = [band_herm(N, W) for _ in range(3)]
    Q2 = edge_charge(X, Th, Pi)
    Q1 = edge_charge(X, th1, Pi)
    Q1b = edge_charge(X, th2, Pi)
    e2, e1, e1b = nonzero_sorted(Q2), nonzero_sorted(Q1), nonzero_sorted(Q1b)
    pred = np.sort(np.concatenate([e1, e1b]))
    worst['union'] = max(worst['union'], abs(pred - e2).max()
                         if len(pred) == len(e2) else 1e9)
    gap = float(np.abs(np.diff(e2)).min()) if len(e2) > 1 else 1e9
    gapmin = min(gapmin, gap)
    # (c) coincident q-copy lift with copy-invariant band-limited state
    for q in (2, 3):
        Iq = np.eye(q, dtype=complex)
        Ql = edge_charge([np.kron(Iq, x) for x in X], np.kron(Iq, Th),
                         [np.kron(Iq, p) for p in Pi])
        el = nonzero_sorted(Ql)
        worst['lift'] = max(worst['lift'], float(np.abs(Ql - np.kron(Iq, Q2)).max()))
        worst['tile'] = max(worst['tile'], float(np.abs(el - np.sort(np.tile(e2, q))).max())
                            if len(el) == q * len(e2) else 1e9)
    # (d) control: full Gaussian Pi violates the band condition
    PiF = []
    for _ in range(3):
        g = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
        PiF.append(g + g.conj().T)
    e2F = nonzero_sorted(edge_charge(X, Th, PiF))
    e1F = nonzero_sorted(edge_charge(X, th1, PiF))
    e1bF = nonzero_sorted(edge_charge(X, th2, PiF))
    predF = np.sort(np.concatenate([e1F, e1bF]))
    ctrl.append(max(abs(predF - e2F).max() if len(predF) == len(e2F) else 1e9,
                    1e-30))

print('max union-exactness deviation (band-limited Pi): %.3e' % worst['union'])
print('least gap between consecutive nonzero two-cap eigenvalues: %.6f' % gapmin)
print('max |Q~ - I_q (x) Q| (copy-invariant lift): %.3e' % worst['lift'])
print('max multiplicity-q tiling deviation: %.3e' % worst['tile'])
print('control deviations with full Gaussian Pi (union FAILS): '
      + ', '.join('%.3e' % c for c in ctrl))
ok = (worst['union'] < 1e-9 and worst['lift'] < 1e-9 and worst['tile'] < 1e-9
      and gapmin > 0.05 and max(ctrl) > 1e-3)
print('all checks inside thresholds:', ok)
assert ok
print('PASS s2')
