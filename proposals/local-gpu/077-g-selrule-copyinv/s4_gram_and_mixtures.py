"""077 s4: the Gram-concentration criterion; scale-mixture counterexample;
mixture-support frequency of exact tiling.

For coincident copies, the charge depends on the momenta only through the
q^2 edge-row vectors z_{ab} = sum_a conj(c^a) Theta Pi^a_{ab} v (c^a, u, v the
rank-1 cap edge datum, appH edge-datum paragraph). The nonzero spectrum of Q~
is determined by the Gram data G = [[I, C],[C*, Z]], Z[(ab),(a'b')] = (z_ab|z_a'b').

Criterion tested: leading-order mult-q reading <=> the edge-row Gram Z has all
q^2 eigenvalues equal to relative o(1) (single-value concentration).
  (a) iid absolutely-continuous block ensembles: Z eigenvalue relative spread
      decays as N^-1/2 at fixed q (q=2,3): criterion SATISFIED for the whole
      class (leading-order universality mechanism, s2);
  (b) scale-mixture ensemble with copy-randomized lognormal variance (mean 1,
      CV 0.4): Z spread stays O(CV) and does NOT decay with N: criterion FAILS
      at leading order: state-selection has O(1) teeth outside the
      uniformly-nondegenerate class;
  (c) mixture ensemble: with prob 1/2 fully correlated momenta (Pi_2 = Pi_1
      a.s.), else independent: EXACT tiling (D < 1e-10) frequency = 1/2:
      the exact-level mult-q probability equals the mass of the degenerate
      copy-diagonal support component (0 events otherwise, s1).

Run: python -I proposals/077-g-selrule-copyinv/s4_gram_and_mixtures.py
Expected invariants: (a) spread slope in [-0.9,-0.25] for q=2,3; (b) slope in
[-0.15,0.15], level > 0.1; (c) empirical frequency in [0.40,0.60] over 300
draws (binomial-tight); last line 'PASS s4'.
"""
import numpy as np

rng = np.random.default_rng(77004)


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


def edge_charge(Xs, Th, Pis):
    Tb = np.eye(len(Th), dtype=complex) - Th
    A = sum((Th @ x @ Tb) @ (Tb @ pi @ Th) for x, pi in zip(Xs, Pis))
    return -2j * (A - A.conj().T)


def herg(m):
    g = rng.normal(size=(m, m)) + 1j * rng.normal(size=(m, m))
    return g + g.conj().T


def blocks(G, q, N):
    return [[G[a * N:(a + 1) * N, b * N:(b + 1) * N] for b in range(q)]
            for a in range(q)]


def gram_Z(Xs, Th, u, v, Pis, q, N):
    ca = [np.vdot(u, x @ v) for x in Xs]      # c^a = (u|X^a v)
    zs = []
    for f in range(3):
        for a in range(q):
            for b in range(q):
                zs.append(Th @ (np.conj(ca[f]) * Pis[f][a * N:(a + 1) * N,
                                                         b * N:(b + 1) * N]) @ v)
    # sum over flavors: stack the flavor-contracted rows per (ab)
    zc = []
    for a in range(q):
        for b in range(q):
            zc.append(sum(Th @ (np.conj(ca[f]) * Pis[f][a * N:(a + 1) * N,
                                                        b * N:(b + 1) * N]) @ v
                          for f in range(3)))
    q2 = q * q
    Z = np.zeros((q2, q2), complex)
    for i in range(q2):
        for j in range(q2):
            Z[i, j] = np.vdot(zc[i], zc[j])
    return Z


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


slopes_a = []
for q in (2, 3):
    Ns, S = [], []
    for N in (100, 200, 400):
        M = N // 2
        J = su2(N)
        n = rng.normal(size=3); n /= np.linalg.norm(n)
        Th, u, v = cap_data(J, n, M)
        A3 = rng.normal(size=(3, 3))
        X = [sum(A3[a, b] * J[b] for b in range(3)) for a in range(3)]
        sp = []
        for _ in range(20):
            Pis = [herg(q * N) for _ in range(3)]
            Z = gram_Z(X, Th, u, v, Pis, q, N)
            lz = np.linalg.eigvalsh(Z)
            sp.append(float((lz[-1] - lz[0]) / lz.mean()))
        Ns.append(N); S.append(float(np.median(sp)))
    s = slope(Ns, S)
    slopes_a.append(s)
    print('(a) q=%d iid ensemble: Z spread %s ; slope %.3f'
          % (q, ['%d:%.4f' % (a, b) for a, b in zip(Ns, S)], s))

# (b) copy-randomized scale mixture: per-event lognormal variance per copy
s = np.sqrt(np.log(1.4 ** 2))          # CV 0.4 lognormal
Ns, S = [], []
for N in (100, 200, 400):
    M = N // 2
    J = su2(N)
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    Th, u, v = cap_data(J, n, M)
    A3 = rng.normal(size=(3, 3))
    X = [sum(A3[a, b] * J[b] for b in range(3)) for a in range(3)]
    q = 2
    sp, dv = [], []
    for _ in range(40):
        t1, t2 = np.exp(rng.normal(-s ** 2 / 2, s, 2))   # mean 1
        Sq = np.kron(np.diag([np.sqrt(t1), np.sqrt(t2)]), np.eye(N))
        Pis = [Sq @ herg(q * N) @ Sq for _ in range(3)]
        Z = gram_Z(X, Th, u, v, Pis, q, N)
        lz = np.linalg.eigvalsh(Z)
        sp.append(float((lz[-1] - lz[0]) / lz.mean()))
        Ql = edge_charge([np.kron(np.eye(q), x) for x in X],
                         np.kron(np.eye(q), Th), Pis)
        dv.append(D_from_eigs(np.linalg.eigvalsh(Ql), q))
    Ns.append(N)
    S.append(float(np.median(sp)))
    print('(b) scale mixture: Z spread %.4f  charge D %.4f at N=%d'
          % (S[-1], float(np.median(dv)), N))
s_b = slope(Ns, S)
lv_b = S[-1]
print('(b) slope %.3f' % s_b)

# (c) mixture with 1/2 degenerate component
q, N = 2, 160
M = N // 2
J = su2(N)
n = rng.normal(size=3); n /= np.linalg.norm(n)
Th, u, v = cap_data(J, n, M)
A3 = rng.normal(size=(3, 3))
X = [sum(A3[a, b] * J[b] for b in range(3)) for a in range(3)]
Iq = np.eye(q)
Xl = [np.kron(Iq, x) for x in X]
Thl = np.kron(Iq, Th)
hits = 0
nev = 300
for _ in range(nev):
    base = [herg(N) for _ in range(3)]
    if rng.random() < 0.5:
        Pil = [np.kron(Iq, p) for p in base]           # degenerate component
    else:
        Pil = [herg(q * N) for _ in range(3)]          # absolutely continuous
    Dv = D_from_eigs(np.linalg.eigvalsh(edge_charge(Xl, Thl, Pil)), q)
    if Dv < 1e-10:
        hits += 1
freq = hits / nev
print('(c) exact-tiling frequency in 1/2-degenerate mixture: %d/%d = %.3f'
      % (hits, nev, freq))

ok = (all(-0.9 < s < -0.25 for s in slopes_a)
      and abs(s_b) < 0.15 and lv_b > 0.1
      and 0.40 < freq < 0.60)
print('all checks inside thresholds:', ok)
assert ok
print('PASS s4')
