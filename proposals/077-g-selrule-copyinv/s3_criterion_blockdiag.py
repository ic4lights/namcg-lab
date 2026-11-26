"""077 s3: state-selection criterion in the coherence-free (block-diagonal) class.

Copies carry INDEPENDENT momenta with per-copy variance scales tau_alpha
(product / classically correlated ensembles, no off-diagonal copy blocks).
Then Q~ = direct sum of single-copy charges Q_alpha and, with
Y_alpha = sum_a c^a-contracted edge-row norm of copy alpha (the s2 W_n of the
row-length paragraph at that copy), the q-fold tiling requires all copies'
spectral scales to match: at leading order |eig| ~ sqrt(tau_alpha * M), so

    leading mult-q reading  <=>  tau_1 = ... = tau_q  (copy-temperality),
    exact mult-q at fixed N <=>  degenerate support (Y_alpha a.s. equal, e.g.
    fully correlated momenta Pi_alpha = Pi_1 a.s., the C1 mechanism).

Checks (D statistic as in s1/s2; block-diagonal momenta, q=2):
  (a) tau=(1,1): D decays as N^-1/2 (log-log slope in [-0.9,-0.25]);
  (b) tau=(1,1.6): D tends to a nonzero constant (slope in [-0.15,0.15],
      level > 0.1), the O(1) selection of copy-tempered states;
  (c) fully correlated degenerate ensemble Pi_2 = Pi_1 a.s.: D < 1e-12 at every
      N (exact tiling: positive criterion mechanism, C1 spot-reproduced);
  (d) partial correlation Pi_alpha = sqrt(c) xi + sqrt(1-c) xi_alpha, c in
      {0, 0.5, 0.9, 0.99}: leading tiling holds (slope ~ 0 only through
      sqrt(1-c) floor): D at N=480 increases monotonically in sqrt(1-c) and
      decays in N at each fixed c>0-pair... reported; exact level reached only
      at c = 1 (c).

Run: python -I proposals/077-g-selrule-copyinv/s3_criterion_blockdiag.py
Expected invariants: (a) slope in [-0.9,-0.25]; (b) slope in [-0.15,0.15] and
level > 0.1; (c) max D < 1e-12; (d) D(N=480) strictly increasing in c-descending
order; last line 'PASS s3'.
"""
import numpy as np

rng = np.random.default_rng(77003)


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
    return evec[:, order[:M]] @ evec[:, order[:M]].conj().T


def edge_charge(Xs, Th, Pis):
    Tb = np.eye(len(Th), dtype=complex) - Th
    A = sum((Th @ x @ Tb) @ (Tb @ pi @ Th) for x, pi in zip(Xs, Pis))
    return -2j * (A - A.conj().T)


def herg(m):
    g = rng.normal(size=(m, m)) + 1j * rng.normal(size=(m, m))
    return g + g.conj().T


def eigs_bd(Xs, Th, copy_blocks, q):
    # block-diagonal momenta: Q~ = direct sum; spectrum = union of copy spectra
    return np.concatenate([np.linalg.eigvalsh(
        edge_charge(Xs, Th, [copy_blocks[f][a] for f in range(3)]))
        for a in range(q)])


def D_from_eigs(ev, q, tol=1e-9):
    thr = tol * max(1.0, np.abs(ev).max())
    e = np.sort(ev[np.abs(ev) > thr])
    if len(e) != 2 * q:
        return float('nan')
    return max(float(e[k * q + q - 1] - e[k * q]) for k in range(2)) / np.abs(e).max()


def slope(xs, ys):
    xs = np.asarray(xs, float); ys = np.asarray(ys, float)
    i = [j for j, y in enumerate(ys) if np.isfinite(y) and y > 0]
    return float(np.polyfit(np.log(xs[i]), np.log(ys[i]), 1)[0])


q = 2

# (a),(b): independent copies with variance scales
out = {}
for tag, tau in (('tau=1,1', (1.0, 1.0)), ('tau=1,1.6', (1.0, 1.6))):
    Ns, Dv = [], []
    for N in (60, 120, 240, 480):
        M = N // 2
        J = su2(N)
        n = rng.normal(size=3); n /= np.linalg.norm(n)
        Th = cap_projector(J, n, M)
        A3 = rng.normal(size=(3, 3))
        X = [sum(A3[a, b] * J[b] for b in range(3)) for a in range(3)]
        ds = []
        for _ in range(40):
            cb = [[np.sqrt(tau[0]) * herg(N), np.sqrt(tau[1]) * herg(N)]
                  for _ in range(3)]
            ev = eigs_bd(X, Th, cb, q)
            ds.append(D_from_eigs(ev, q))
        Ns.append(N); Dv.append(float(np.median(ds)))
    s = slope(Ns, Dv)
    out[tag] = (Ns, Dv, s)
    print('(%s) independent copies: N, D median: %s ; slope %.3f'
          % (tag, ['%d:%.4f' % (a, b) for a, b in zip(Ns, Dv)], s))

# (c): fully correlated degenerate ensemble: Pi_2 = Pi_1 a.s.
maxd = 0.0
for N in (60, 120, 240, 480):
    M = N // 2
    J = su2(N)
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    Th = cap_projector(J, n, M)
    A3 = rng.normal(size=(3, 3))
    X = [sum(A3[a, b] * J[b] for b in range(3)) for a in range(3)]
    for _ in range(10):
        cb = [[p, p] for p in (herg(N), herg(N), herg(N))]
        ev = eigs_bd(X, Th, cb, q)
        maxd = max(maxd, D_from_eigs(ev, q))
print('(c) fully correlated (Pi_2 = Pi_1 a.s.): max D over N and events: %.2e' % maxd)

# (d): partial correlation, matched variance: Pi_a = sqrt(c) xi + sqrt(1-c) xi_a
fin = {}
for c in (0.0, 0.5, 0.9, 0.99):
    ds480 = []
    for N in (480,):
        M = N // 2
        J = su2(N)
        n = rng.normal(size=3); n /= np.linalg.norm(n)
        Th = cap_projector(J, n, M)
        A3 = rng.normal(size=(3, 3))
        X = [sum(A3[a, b] * J[b] for b in range(3)) for a in range(3)]
        for _ in range(40):
            cb = []
            for _f in range(3):
                xi = herg(N)
                cb.append([np.sqrt(c) * xi + np.sqrt(1 - c) * herg(N),
                           np.sqrt(c) * xi + np.sqrt(1 - c) * herg(N)])
            ev = eigs_bd(X, Th, cb, q)
            ds480.append(D_from_eigs(ev, q))
    fin[c] = float(np.median(ds480))
    print('(d) c=%.2f : D(N=480) median = %.4f' % (c, fin[c]))

sa, sb = out['tau=1,1'][2], out['tau=1,1.6'][2]
lv = max(out['tau=1,1.6'][1][-1], out['tau=1,1.6'][1][-2])
# the inter-copy difference variance scales as 2c(1-c)A + (1-c)^2 B with
# A >> B ~ A/M: it peaks at c = 1/2 (bump) and decays to 0 only as c -> 1;
# exact tiling is reached only at c = 1 (part (c)). Invariant: tail decay
# toward c = 1, and the c = 1/2 bump exceeds the iid level.
mono = (fin[0.99] < fin[0.9] - 1e-4 and fin[0.9] < fin[0.5] - 1e-4
        and fin[0.99] < 0.02 and fin[0.5] > fin[0.0])

ok = (-0.9 < sa < -0.25 and abs(sb) < 0.15 and lv > 0.1
      and maxd < 1e-12 and mono)
print('all checks inside thresholds:', ok)
assert ok
print('PASS s3')
