"""
065 s3: spectrum of the classicalised edge charge for a rank-one off-diagonal block.

Q_cl = -2i sum_a ( X^a_{SS'} Pi^a_{S'S} - Pi^a_{SS'} X^a_{S'S} )   (M x M; Pi^a Hermitian momentum matrices),
as in Eq. (4.4) [eqn:q-sc] of arXiv:2408.05274 with X_V -> X. If X^a_{SS'} = c^a |u)(v| (u in S, v in S'), then
Q_cl = -2i ( |u)(w| - |w)(u| ),  (w|_j = sum_a c^a (v|Pi^a|j), j in S,
and with alpha = (u|w), w_perp = w - alpha u, the nonzero eigenvalues are
    -2 Im(alpha) +- 2 sqrt( Im(alpha)^2 + |w_perp|^2 ),
i.e. +-2|w_perp| when Im(alpha)=0. Checked exactly on the fuzzy-sphere cap block (s2) with random Pi.
Output to stdout only.
"""
import numpy as np

rng = np.random.default_rng(65003)

def su2(N):
    j3 = np.diag([(N - 1) / 2 - i for i in range(N)]).astype(complex)
    jp = np.zeros((N, N), complex)
    for i in range(1, N):
        jp[i - 1, i] = np.sqrt(i * (N - i))
    jm = jp.conj().T
    return [(jp + jm) / 2, (jp - jm) / (2j), j3]

def herm(n):
    a = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    return (a + a.conj().T) / 2

worst = 0.0
for N in (4, 9, 20, 50):
    J = su2(N)
    for M in sorted({1, 2, N // 2, N - 1}):
        A = rng.normal(size=(3, 3))
        X = [sum(A[a, b] * J[b] for b in range(3)) for a in range(3)]
        Pi = [herm(N) for _ in range(3)]
        Q = -2j * sum(X[a][:M, M:] @ Pi[a][M:, :M] - Pi[a][:M, M:] @ X[a][M:, :M] for a in range(3))
        c = np.array([X[a][M - 1, M] for a in range(3)])
        w = sum(c[a] * Pi[a][M, :M] for a in range(3))          # row vector (w|
        u = np.zeros(M, complex); u[M - 1] = 1
        wk = w.conj()                                           # ket |w)
        wperp = wk - np.vdot(u, wk) * u
        a_ = np.vdot(u, wk)
        pred = sorted([-2 * a_.imag + 2 * np.sqrt(a_.imag ** 2 + np.vdot(wperp, wperp).real),
                       -2 * a_.imag - 2 * np.sqrt(a_.imag ** 2 + np.vdot(wperp, wperp).real)])
        ev = np.linalg.eigvalsh(Q)
        nz = sorted(ev[np.argsort(-np.abs(ev))][:2]) if M >= 2 else sorted([ev[0], 0.0])
        rest = np.sort(np.abs(ev))[:-2] if M >= 2 else np.array([])
        if M >= 2:
            err = max(abs(nz[0] - pred[0]), abs(nz[1] - pred[1])) / max(1, abs(pred[1]))
            err = max(err, rest.max() / max(1, abs(pred[1])) if rest.size else 0)
        else:
            err = abs(ev[0] - (-4 * a_.imag)) / max(1, abs(ev[0]))
        worst = max(worst, err)
print('rank-one edge charge: Q_cl = -2i(|u)(w|-|w)(u|), spectrum -2Im(alpha) +- 2 sqrt(Im(alpha)^2+|w_perp|^2), rest 0')
print('max rel. deviation: %.2e' % worst)
assert worst < 1e-10
print('PASS s3')

# Two disjoint caps on the round fuzzy sphere: Theta = projector on the first M1 and the last M2 J^3-eigenvectors.
# With momentum matrices of band width b (|i-j| <= b, as for modes with l <= b) and boundaries farther apart than
# 2b, the nonzero spectrum of Q_cl is the union of the two single-cap pairs (each computed with its own block).
def band_herm(n, b):
    H = herm(n)
    i, j = np.indices((n, n))
    H[np.abs(i - j) > b] = 0
    return H

worst2 = 0.0
for (N, M1, M2, b) in ((60, 15, 20, 5), (90, 30, 25, 8), (120, 50, 40, 10)):
    J = su2(N)
    X = [J[0], J[1], J[2]]
    Pi = [band_herm(N, b) for _ in range(3)]
    S = list(range(M1)) + list(range(N - M2, N))
    Sb = list(range(M1, N - M2))
    def Qof(Sset, Sbset):
        return -2j * sum(X[a][np.ix_(Sset, Sbset)] @ Pi[a][np.ix_(Sbset, Sset)] -
                         Pi[a][np.ix_(Sset, Sbset)] @ X[a][np.ix_(Sbset, Sset)] for a in range(3))
    ev = np.linalg.eigvalsh(Qof(S, Sb))
    big = np.sort(ev[np.argsort(-np.abs(ev))][:4])
    e1 = np.linalg.eigvalsh(Qof(list(range(M1)), list(range(M1, N))))
    e2 = np.linalg.eigvalsh(Qof(list(range(N - M2, N)), list(range(N - M2))))
    pair = lambda e: np.sort(e[np.argsort(-np.abs(e))][:2])
    ref = np.sort(np.concatenate([pair(e1), pair(e2)]))
    rest = np.sort(np.abs(ev))[:-4]
    worst2 = max(worst2, np.abs(big - ref).max() / np.abs(ref).max(), rest.max() / np.abs(ref).max())
print('two disjoint caps (band-limited momenta): nonzero spectrum = union of single-cap pairs, max rel dev %.2e' % worst2)
assert worst2 < 1e-10
print('PASS s3 (two caps)')
