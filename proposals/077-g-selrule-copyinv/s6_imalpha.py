"""077 s6: the Im-alpha column of the exact mult-q criterion is subleading in N.

Exact classification for a block-diagonal pair of rank-2 charges (s5, Lemma 2):
mult-2 <=> Im alpha_1 = Im alpha_2 AND |w_perp,1| = |w_perp,2| (Re alpha
invisible), where alpha = (u|w), w_perp = w - alpha u, and the charge
eigenvalues are -2 Im alpha +- 2 sqrt(Im^2 alpha + |w_perp|^2) - the appH
'Row length' formula. The two copies of a coincident background generically
have DIFFERENT Im alpha (iid edge matrix elements): so EXACT tiling is not
even reachable by equalizing the row norms; but |w_perp| ~ sqrt(M) while
alpha stays O(1) per matrix element of an (unimodular-scaled) Gaussian
momentum, so the Im-alpha shift is relative O(M^-1/2) and vanishes at
leading order: only the norm equality has leading-order teeth.

Checks (numerical, finite N; charges built per copy as
Q_a = -2i(|u)(w_a| - |w_a)(u|) with w_a = sum_f c^f Pi^a_f edge rows):
  (a) median |alpha| = O(1) and median |w_perp| ~ sqrt(M) up to constants:
      |alpha|/|w_perp| decays with slope ~ -1/2 in N;
  (b) the relative leading eigenvalue scale 2 sqrt(Im^2 alpha + |w_perp|^2)
      deviates from 2|w_perp| by a relative amount with the same decay;
  (c) DIRECT: block-diagonal 2-copy charges with iid (matched-scale) row
      data: the exact mult-2 D statistic NEVER approaches the exact-tiling
      level (D_exact >= 0.05 at every N tested, >= 4e7 times the tiling
      threshold 1e-12: no tested product family achieves exact tiling by
      norms alone) but decays as M^(-1/2) with the |alpha|/|w| slope
      (CORRECTED ROUND 2: round 1 asserted an O(1) level with threshold
      > 0.3; measured D_exact 0.1317 -> 0.0536, slope -0.43): the Im-alpha
      column kills EXACT tiling but is subleading, invisible at leading
      order; the leading-order signature U_2 - 1 = O(1/N), slope ~ -1.

ROUND 2: the (c) assert min(rows_c1) > 0.3 encoded the wrong qualitative
claim; corrected to non-tiling level (> 0.01) plus M^(-1/2) decay slope.
Run: python -I proposals/077-g-selrule-copyinv/s6_imalpha.py
Expected invariants: (a) slope of |alpha|/|w_perp| in [-0.8,-0.25];
(b) slope of the relative deviation in [-1.6,-0.5]: rel-dev = sqrt(1+x^2)-1 = x^2/2 with x = Im(alpha)/|w_perp|, so its N-slope is 2 x (-1/2) = -1 (ROUND 3: the round-2 window copied the linear-decay check; a slope near 0 or -1/2 would still fail); (c) D level > 0.01 at
every N (round-2 text 'D level > 0.3' superseded by the corrected non-tiling level above) and U_2 - 1 slope in [-1.6,-0.5]; last line 'PASS s6'.
"""
import numpy as np

rng = np.random.default_rng(77017)


def su2(N):
    j3 = np.diag([(N - 1) / 2 - i for i in range(N)]).astype(complex)
    jp = np.zeros((N, N), complex)
    for i in range(1, N):
        jp[i - 1, i] = np.sqrt(i * (N - i))
    return [(jp + jp.conj().T) / 2, (jp - jp.conj().T) / 2j, j3]


def cap_data(J, n, M):
    nj = n[0] * J[0] + n[1] * J[1] + n[2] * J[2]
    ev, evec = np.linalg.eigh(nj)
    order = np.argsort(-np.real(ev))
    u = evec[:, order[M - 1]]
    v = evec[:, order[M]]
    Th = evec[:, order[:M]] @ evec[:, order[:M]].conj().T
    return Th, u, v


def herg(m):
    g = rng.normal(size=(m, m)) + 1j * rng.normal(size=(m, m))
    return g + g.conj().T


def slope(xs, ys):
    xs = np.asarray(xs, float); ys = np.asarray(ys, float)
    i = [j for j, y in enumerate(ys) if np.isfinite(y) and y > 0]
    return float(np.polyfit(np.log(xs[i]), np.log(ys[i]), 1)[0])


rows_a, rows_b, rows_c1, rows_c2 = [], [], [], []
for N in (60, 120, 240, 480):
    M = N // 2
    J = su2(N)
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    Th, u, v = cap_data(J, n, M)
    A3 = rng.normal(size=(3, 3))
    X = [sum(A3[a, b] * J[b] for b in range(3)) for a in range(3)]
    ca = [np.vdot(u, x @ v) for x in X]
    dA, dB, dc1, dc2 = [], [], [], []
    for _ in range(40):
        ws = []
        for k in range(2):
            Pis = [herg(N) for _ in range(3)]
            w = sum(np.conj(ca[f]) * (Pis[f] @ v) for f in range(3))
            ws.append(w)
        al = [np.vdot(u, w) for w in ws]
        wp = [w - a * u for w, a in zip(ws, al)]
        dA.append(np.mean([abs(a) for a in al]) /
                  np.mean([np.linalg.norm(x) for x in ws]))
        lead = [2 * np.sqrt(np.imag(a) ** 2 + np.linalg.norm(x) ** 2)
                for a, x in zip(al, wp)]
        norml = [2 * np.linalg.norm(x) for x in wp]
        dB.append(np.mean([abs(l - m) / m for l, m in zip(lead, norml)]))
        # (c) block-diagonal 2-copy charge with these row data
        Q = np.zeros((2 * N, 2 * N), complex)
        for k in range(2):
            blk = -2j * (np.outer(u, ws[k].conj()) - np.outer(ws[k], u.conj()))
            Q[k * N:(k + 1) * N, k * N:(k + 1) * N] = blk
        ev = np.linalg.eigvalsh(Q)
        thr = 1e-9 * max(1.0, np.abs(ev).max())
        e = np.sort(ev[np.abs(ev) > thr])
        if len(e) == 4:
            dc1.append(max(float(e[1] - e[0]), float(e[3] - e[2])) / np.abs(e).max())
        m2 = float(np.trace(Q @ Q).real) / 4.0
        dc2.append(float(np.trace(Q @ Q @ Q @ Q).real) / 4.0 / m2 ** 2 - 1.0)
    rows_a.append(float(np.median(dA)))
    rows_b.append(float(np.median(dB)))
    rows_c1.append(float(np.median(dc1)))
    rows_c2.append(float(np.median(dc2)))
    print('N=%4d  |alpha|/|w_perp| %.4f  rel dev lead-vs-norm %.4f  '
          'D_exact %.4f  U_2-1 %.5f'
          % (N, rows_a[-1], rows_b[-1], rows_c1[-1], rows_c2[-1]))

Ns = [60, 120, 240, 480]
sA = slope(Ns, rows_a)
sB = slope(Ns, rows_b)
sC2 = slope(Ns, rows_c2)
sC1 = slope(Ns, rows_c1)
ok = (-0.8 < sA < -0.25) and (-1.6 < sB < -0.5) \
     and min(rows_c1) > 0.01 and (-0.8 < sC1 < -0.25) and (-1.6 < sC2 < -0.5)
print('slopes: |alpha|/|w| %.3f ; rel-dev %.3f ; D_exact %.3f ; U_2-1 %.3f ; '
      'min D_exact %.3f' % (sA, sB, sC1, sC2, min(rows_c1)))
print('all checks inside thresholds:', ok)
assert ok
print('PASS s6')
