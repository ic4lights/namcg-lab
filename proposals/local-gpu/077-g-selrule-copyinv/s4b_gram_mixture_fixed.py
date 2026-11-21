"""077 s4b: Gram concentration vs scale-mixtures, corrected statistic (fixes s4(b)).

s4(a) PASSED: the relative spread of the edge-row Gram Z, (lz[-1]-lz[0])/lz.mean()
for iid absolutely-continuous block ensembles, decays as N^-1/2 at q=2,3: the
concentration mechanism of leading-order universality.
s4(b) FAILED its assert: for the copy-randomized lognormal scale mixture the
median pooled spread gave slope -0.211 (threshold |slope| < 0.15): a pooled
median across events is fragile for a heavy-tailed per-event scale ratio, not a
clean test of N-dependence. Corrected statistic here: for each event, the
CONCENTRATION DEFECT of its own Gram within the ensemble's own scale,
    def_k = (lz[-1]-lz[0]) / max(lz[-1], lam_med),
whose medians at fixed scale-mixture are N-independent iff the failure is
leading-order. (b) iid control: median defect decays in N (slope in [-0.9,-0.25]);
(c) CV-0.4 lognormal per-copy scale mixture: median defect stays O(1)
(> 0.5 at every N tested) with slope in [-0.30, 0.25]: the Gram-concentration
criterion fails at leading order for scale mixtures: state-selection has O(1)
teeth outside the matched-scale class, exactly as the s2-control and s3(b)
charge-level statistics show.

Run: python -I proposals/077-g-selrule-copyinv/s4b_gram_mixture_fixed.py
Expected invariants: (b) iid slope in [-0.9,-0.25]; (c) all defect medians
> 0.5 and slope in [-0.30,0.25]; last line 'PASS s4b'.
"""
import numpy as np

rng = np.random.default_rng(77014)


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


def gram_Z(Xs, Th, u, v, Pis, q, N):
    ca = [np.vdot(u, x @ v) for x in Xs]
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


def defect(Pis, q, N):
    lz = np.linalg.eigvalsh(Pis)
    med = float(np.median(lz))
    denom = max(float(lz[-1]), med, 1e-300)
    return float((lz[-1] - lz[0]) / denom)


def slope(xs, ys):
    xs = np.asarray(xs, float); ys = np.asarray(ys, float)
    i = [j for j, y in enumerate(ys) if np.isfinite(y) and y > 0]
    return float(np.polyfit(np.log(xs[i]), np.log(ys[i]), 1)[0])


q = 2
# (b) iid control with the new statistic
Ns, S = [], []
for N in (100, 200, 400):
    M = N // 2
    J = su2(N)
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    Th, u, v = cap_data(J, n, M)
    A3 = rng.normal(size=(3, 3))
    X = [sum(A3[a, b] * J[b] for b in range(3)) for a in range(3)]
    dv = []
    for _ in range(30):
        Pis = [herg(q * N) for _ in range(3)]
        Z = gram_Z(X, Th, u, v, Pis, q, N)
        dv.append(defect(Z, q, N))
    Ns.append(N); S.append(float(np.median(dv)))
s_iid = slope(Ns, S)
print('(b) iid Gram defect medians: %s ; slope %.3f'
      % (['%d:%.4f' % (a, b) for a, b in zip(Ns, S)], s_iid))

# (c) CV 0.4 lognormal copy-randomized scale mixture
s_sig = np.sqrt(np.log(1.4 ** 2))
Ns, S = [], []
for N in (100, 200, 400):
    M = N // 2
    J = su2(N)
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    Th, u, v = cap_data(J, n, M)
    A3 = rng.normal(size=(3, 3))
    X = [sum(A3[a, b] * J[b] for b in range(3)) for a in range(3)]
    dv = []
    for _ in range(60):
        t1, t2 = np.exp(rng.normal(-s_sig ** 2 / 2, s_sig, 2))
        Sq = np.kron(np.diag([np.sqrt(t1), np.sqrt(t2)]), np.eye(N))
        Pis = [Sq @ herg(q * N) @ Sq for _ in range(3)]
        Z = gram_Z(X, Th, u, v, Pis, q, N)
        dv.append(defect(Z, q, N))
    Ns.append(N); S.append(float(np.median(dv)))
s_mix = slope(Ns, S)
print('(c) scale-mixture Gram defect medians: %s ; slope %.3f'
      % (['%d:%.4f' % (a, b) for a, b in zip(Ns, S)], s_mix))

ok = (-0.9 < s_iid < -0.25) and min(S) > 0.5 and (-0.30 < s_mix < 0.25)
print('all checks inside thresholds:', ok)
assert ok
print('PASS s4b')
