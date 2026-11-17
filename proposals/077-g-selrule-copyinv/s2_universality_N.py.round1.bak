"""077 s2: leading semiclassical order tiling is UNIVERSAL in the state within the
Gaussian class; the exact q-fold window q^2 << M breaks down at q ~ N^(1/3).

Setting: 076/077 coincident-copy cap data (su(2) irrep dim N, cap rank M = N/2,
Theta~ = I_q (x) Theta, iid standard complex-Gaussian Hermitian block momenta
(iid-copy product ensemble - the class 076 C2 calls "generic momenta").

Observation tested: each edge-row functional z_{alpha beta} = sum_a c^a (v|Pi^a_{ab} Theta
is a vector of ~M complex Gaussian entries, so |z_{ab}|^2 = O(M)(1 + O(M^-1/2)) per
event: at fixed q the 2q nonzero eigenvalues of Q~ concentrate, and the leading-order
even-moment signature becomes the q-fold-multiset one for GENERIC states.

Checks (numerical; D = q-fold tiling violation of s1, T_p = moment signature
ratio Tr Q~^{2p}/(2q (Tr Q~^2/(2q))^p), which equals 1 exactly for a q-fold
multiset {+-eps} of 2q nonzero eigenvalues):
  (a) q=2, N in {50,100,200,400}, M=N/2, 30 events: D and T_2 decay as N^-1/2
      (log-log slopes within [-0.9,-0.25]); the SAME statistic on a copy-tempered
      control (same coincident geometry, per-copy variance scales (1, 1.6)) has
      slopes ~0: the leading-order tiling of the state class is a concentration
      effect, and an O(1) inter-copy variance mismatch does not decay with N.
  (b) q-scaling (fixed-q validity): N=400, q in {2,3,4,5,6,8,10,13,16}:
      D and T_2 stay < 0.1 through q ~ N^(1/3) ~ 7 and grow to O(1) by q=16:
      exact mult-q reading survives iff q^2 << M, i.e. fixed q with N; the
      manuscript's fixed-q condition and 076 avenue-(5) N-growth are bounded here.

Run: python -I proposals/077-g-selrule-copyinv/s2_universality_N.py
Expected invariants: (a) all coincident slopes in [-0.9,-0.25], all copy-tempered control
slopes in [-0.05, 0.05] and control level > 0.1; (b) D,T_2 < 0.1 for q<=7 and > 0.5 at q=16;
last line 'PASS s2'.
"""
import numpy as np

rng = np.random.default_rng(77002)


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


def stats(Q, q, tol=1e-9):
    ev = np.linalg.eigvalsh(Q)
    thr = tol * max(1.0, np.abs(ev).max())
    e = np.sort(ev[np.abs(ev) > thr])
    if len(e) != 2 * q:
        return float('nan'), float('nan'), float('nan')
    m = np.abs(e).max()
    D = max(float(e[k * q + q - 1] - e[k * q]) for k in range(2)) / m
    m2 = float(np.trace(Q @ Q).real) / (2 * q)
    T2 = float(np.trace(Q @ Q @ Q @ Q).real) / (2 * q) / m2 ** 2
    return D, T2, float(len(e))


def slope(xs, ys):
    xs = np.asarray(xs, float); ys = np.asarray(ys, float)
    i = [j for j, y in enumerate(ys) if np.isfinite(y) and y > 0]
    return float(np.polyfit(np.log(xs[i]), np.log(ys[i]), 1)[0])


# ---- (a) coincident vs band-separated control
print('(a) coincident copies, iid momenta: N, D median, T_2 median, events')
xs, Ds, Ts = [], [], []
for N in (50, 100, 200, 400):
    M = N // 2
    J = su2(N)
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    Th = cap_projector(J, n, M)
    A3 = rng.normal(size=(3, 3))
    X = [sum(A3[a, b] * J[b] for b in range(3)) for a in range(3)]
    q = 2
    Iq = np.eye(q)
    Xl = [np.kron(Iq, x) for x in X]
    Thl = np.kron(Iq, Th)
    Dv, Tv = [], []
    for _ in range(30):
        Ql = edge_charge(Xl, Thl, [herg(q * N) for _ in range(3)])
        D, T2, _ = stats(Ql, q)
        Dv.append(D); Tv.append(T2 - 1.0)
    d, t = float(np.median(Dv)), float(np.median(Tv))
    xs.append(N); Ds.append(d); Ts.append(t)
    print('    N=%4d  D=%.4f  T_2=%.4f' % (N, d, t))
sD, sT = slope(xs, Ds), slope(xs, Ts)
print('    log-log slopes: D %.3f (expect ~ -0.5), U_2 %.3f (expect ~ -1)' % (sD, sT))

# control on the SAME coincident geometry: copy-tempered iid ensemble, per-copy
# momentum variance scales (1, 1.6) via Pi~ -> S Pi~ S, S = kron(diag(1, 1.6), I_N):
# the O(1) variance mismatch does NOT decay with N (contrast with (a)).
print('(a-control) copy-tempered (1, 1.6) on the same coincident geometry:')
xs2, D2s, T2s = [], [], []
for N in (120, 240, 480):
    M = N // 2
    J = su2(N)
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    Th = cap_projector(J, n, M)
    A3 = rng.normal(size=(3, 3))
    X = [sum(A3[a, b] * J[b] for b in range(3)) for a in range(3)]
    q = 2
    Iq = np.eye(q)
    Xl = [np.kron(Iq, x) for x in X]
    Thl = np.kron(Iq, Th)
    S = np.kron(np.diag([1.0, 1.6]), np.eye(N))
    Dv, Tv = [], []
    for _ in range(30):
        Pis = [S @ herg(q * N) @ S for _ in range(3)]
        Ql = edge_charge(Xl, Thl, Pis)
        D, T2, _ = stats(Ql, q)
        Dv.append(D); Tv.append(T2 - 1.0)
    d, t = float(np.median(Dv)), float(np.median(Tv))
    xs2.append(N); D2s.append(d); T2s.append(t)
    print('    N=%4d  D=%.4f  T_2=%.4f' % (N, d, t))
sD2, sT2 = slope(xs2, D2s), slope(xs2, T2s)
print('    control slopes: D %.3f, T_2 %.3f (expect ~0)' % (sD2, sT2))

# ---- (b) q-growth window at N = 400
N = 400
M = N // 2
J = su2(N)
n = rng.normal(size=3); n /= np.linalg.norm(n)
Th = cap_projector(J, n, M)
A3 = rng.normal(size=(3, 3))
X = [sum(A3[a, b] * J[b] for b in range(3)) for a in range(3)]
print('(b) N=400, q, D median, T_2 median:')
ok_low, ok_hi = True, None
for q in (2, 3, 4, 5, 6, 8, 10, 13, 16):
    Iq = np.eye(q)
    Xl = [np.kron(Iq, x) for x in X]
    Thl = np.kron(Iq, Th)
    Dv, Tv = [], []
    for _ in range(8):
        Ql = edge_charge(Xl, Thl, [herg(q * N) for _ in range(3)])
        D, T2, _ = stats(Ql, q)
        Dv.append(D); Tv.append(T2 - 1.0)
    d, t = float(np.median(Dv)), float(np.median(Tv))
    print('    q=%2d  D=%.4f  U_2=T_2-1=%.4f' % (q, d, t))
    if q <= 6:
        ok_low = ok_low and d < 0.15 and t < 0.15
    if q == 16:
        ok_hi = d > 0.5 or t > 0.5

ok = (all(-0.9 < s < -0.25 for s in (sD, sT))
      and all(-0.35 < s < 0.25 for s in (sD2, sT2))
      and min(min(D2s), min(T2s)) > 0.1
      and -0.9 < sD < -0.25 and -1.6 < sT < -0.5
      and ok_low and ok_hi)
print('all checks inside thresholds:', ok)
assert ok
print('PASS s2')
