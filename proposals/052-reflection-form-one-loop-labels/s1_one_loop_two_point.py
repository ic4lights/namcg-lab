"""052 s1: one-loop determinant of the matrix model at finite N about commuting and non-commuting matrices.

Gamma_eps[X] = (1/2) log det(H_V+eps) - log det(H_gh+eps) - w_F log det(H_F+eps), with P_a = ad X_a,
H_gh = P^2, (H_V)^b_a = P^2 delta^b_a - 2 [P_a, P^b], H_F = P^2 + (1/4)[G^a,G^b][P_a,P_b] on the chiral (or Majorana) block.
eps is one regulator common to all species.  It is a numerical check at sampled data, not a proof; the proof is the supertrace
algebra in the proposal.  Checked: the power of t in Gamma_eps[X0 + t A] - Gamma_eps[X0]:
  (a) d = 10, Weyl content, commuting X0, Euclidean: t^4
  (b) d = 10, Weyl content, commuting X0, Lorentzian contraction with complex eps: t^4
  (c) d = 10, no fermions (bosonic): t for generic A (the potential of the eigenvalues), t^2 for off-diagonal A
  (d) d = 4, N = 1 content, where Str 1 = 0 only: t^2
  (e) d = 10, Weyl content, background with nonzero commutators (random; and M x K with A commuting with K): t^2
  (f) the sum rule Str 1 and the second spin moment for each content.
Seeded.  Deterministic.  Requires numpy only."""
import numpy as np

np.set_printoptions(precision=6, suppress=False, linewidth=140)


def gammas(d):
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    I = np.eye(2, dtype=complex)
    n = d // 2
    out = []
    for k in range(n):
        for s in (s1, s2):
            m = np.array([[1]], dtype=complex)
            for j in range(n):
                m = np.kron(m, s3 if j < k else (s if j == k else I))
            out.append(m)
    chi = np.array([[1]], dtype=complex)
    for j in range(n):
        chi = np.kron(chi, s3)
    return out, chi


def ad_ops(X):
    N = X[0].shape[0]
    I = np.eye(N)
    return [np.kron(x, I) - np.kron(I, x.T) for x in X]


def gamma_eps(X, eta, eps, content):
    """content: 'bos', 'weyl10', 'maj4'.  eta: list of +-1."""
    d = len(X)
    P = ad_ops(X)
    n = P[0].shape[0]
    P2 = sum(eta[a] * P[a] @ P[a] for a in range(d))
    idn = np.eye(n, dtype=complex)
    comm = {(a, b): P[a] @ P[b] - P[b] @ P[a] for a in range(d) for b in range(d)}
    HV = np.zeros((d * n, d * n), dtype=complex)
    for b in range(d):
        for a in range(d):
            blk = -2 * comm[(a, b)] * eta[b]
            if a == b:
                blk = blk + P2
            HV[b * n:(b + 1) * n, a * n:(a + 1) * n] = blk
    val = 0.5 * logdet(HV + eps * np.eye(d * n))
    val = val - logdet(P2 + eps * idn)
    if content == 'bos':
        return val
    if content == 'weyl10':
        G, chi = gammas(10)
        dim_s = 32
        w = 0.25
    elif content == 'maj4':
        G, chi = gammas(4)
        dim_s = 4
        w = 0.25
    else:
        raise ValueError(content)
    G = [(1j * G[a] if eta[a] < 0 else G[a]) for a in range(d)]  # {G^a,G^b} = 2 eta^{ab}; here G carries upper index
    if content == 'weyl10':
        vals, vecs = np.linalg.eigh(chi)
        Pz = vecs[:, vals > 0]
        G2 = {(a, b): Pz.conj().T @ (0.25 * (G[a] @ G[b] - G[b] @ G[a])) @ Pz for a in range(d) for b in range(d)}
        ds = Pz.shape[1]
    else:
        G2 = {(a, b): 0.25 * (G[a] @ G[b] - G[b] @ G[a]) for a in range(d) for b in range(d)}
        ds = dim_s
    HF = np.kron(np.eye(ds), P2).astype(complex)
    for a in range(d):
        for b in range(d):
            if a != b:
                HF = HF + np.kron(G2[(a, b)], comm[(a, b)])
    val = val - w * logdet(HF + eps * np.eye(ds * n))
    return val


def logdet(M):
    """log det with a continuous branch from the eigenvalues; only differences at nearby t are used."""
    ev = np.linalg.eigvals(M)
    return np.sum(np.log(ev))


def rand_herm(rng, N):
    M = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
    return (M + M.conj().T) / 2


def powers(X0, A, eta, eps, content, ts=(0.01, 0.005, 0.0025)):
    base = gamma_eps(X0, eta, eps, content)
    out = []
    for t in ts:
        X = [x + t * a for x, a in zip(X0, A)]
        out.append(gamma_eps(X, eta, eps, content) - base)
    out = np.array(out)
    slopes = np.log(np.abs(out[:-1] / out[1:])) / np.log(ts[0] / ts[1])
    return out, slopes


def report(name, X0, A, eta, eps, content, expect, ts=(0.01, 0.005, 0.0025)):
    vals, sl = powers(X0, A, eta, eps, content, ts)
    print(('%-60s |dGamma| at t=' + str(ts) + ': %s ; log-slopes %s ; expected power %d') % (name, np.array2string(np.abs(vals), precision=3, formatter={'float_kind': lambda v: '%.3e' % v}), np.array2string(sl, precision=3), expect))
    assert abs(sl[-1] - expect) < 0.35, (name, sl)


def main():
    rng = np.random.default_rng(52001)
    N = 3
    print('sum rules: Str 1 (d=10 Weyl) = 10 - 2 - 8 =', 10 - 2 - 8, '; (d=4 N=1) = 4 - 2 - 2 =', 4 - 2 - 2)
    for name, d, ds, wt in (('d=10, 16-component Weyl, weight 1/2 relative to vector', 10, 16, 0.5), ('d=4, 4-component Majorana, weight 1/2', 4, 4, 0.5)):
        G, chi = gammas(d)
        if d == 10:
            vals, vecs = np.linalg.eigh(chi)
            Pz = vecs[:, vals > 0]
            S = lambda a, b: Pz.conj().T @ (0.25 * (G[a] @ G[b] - G[b] @ G[a])) * 2 @ Pz
        else:
            S = lambda a, b: 0.25 * (G[a] @ G[b] - G[b] @ G[a]) * 2
        # generator normalised so that the fermion operator is P^2 + sum_{a<b} S_ab [P_a,P_b]
        V = lambda a, b: np.array([[(-2.0) * ((i == a) * (j == b) - (i == b) * (j == a)) for j in range(d)] for i in range(d)], dtype=complex)
        tv = np.trace(V(0, 1) @ V(0, 1))
        ts_ = np.trace(S(0, 1) @ S(0, 1))
        print('  ', name, ': tr V01 V01 =', tv.real, '; tr S01 S01 =', ts_.real, '; tr V^2 - wt tr S^2 =', (tv - wt * ts_).real)
    print()
    # commuting background in 4 of d directions
    d = 10
    X0 = [np.diag(rng.normal(size=N)) * 2.0 for _ in range(4)] + [np.zeros((N, N), dtype=complex) for _ in range(6)]
    X0 = [x.astype(complex) for x in X0]
    A = [rand_herm(rng, N) for _ in range(d)]
    eta = [1] * 10
    report('(a) d=10 Weyl, commuting X0, Euclid, eps=0.3', X0, A, eta, 0.3, 'weyl10', 4)
    report('(a2) same, eps=1.0', X0, A, eta, 1.0, 'weyl10', 4)
    etaL = [-1] + [1] * 9
    report('(b) d=10 Weyl, commuting X0, Lorentz, eps=0.5i+0.3', X0, A, etaL, 0.3 + 0.5j, 'weyl10', 4)
    report('(c) d=10 bosonic, commuting X0, generic A (diagonal part: potential of the eigenvalues)', X0, A, eta, 0.3, 'bos', 1)
    Aoff = [a - np.diag(np.diag(a)) for a in A]
    report('(c2) d=10 bosonic, commuting X0, off-diagonal A', X0, Aoff, eta, 0.3, 'bos', 2, (0.0012, 0.0006, 0.0003))
    report('(c3) d=10 Weyl, commuting X0, off-diagonal A', X0, Aoff, eta, 0.3, 'weyl10', 4)
    X04 = X0[:4]
    A4 = A[:4]
    report('(d) d=4 N=1, commuting X0, Euclid, eps=0.3', X04, A4, [1] * 4, 0.3, 'maj4', 2, (0.0012, 0.0006, 0.0003))
    X1 = [rand_herm(rng, N) for _ in range(d)]
    report('(e1) d=10 Weyl, random non-commuting X0, Euclid, eps=60 (operators positive)', X1, A, eta, 60.0, 'weyl10', 1)
    # M x K, N = 4: 4 commuting matrices tensored with the identity on C^2, three su(2) generators
    sx = np.array([[0, 1], [1, 0]], dtype=complex) / 2
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex) / 2
    sz = np.array([[1, 0], [0, -1]], dtype=complex) / 2
    I2 = np.eye(2)
    m = [np.diag(rng.normal(size=2)) * 2.0 for _ in range(4)]
    XMK = [np.kron(x, I2).astype(complex) for x in m] + [np.kron(I2, s) for s in (sx, sy, sz)] + [np.zeros((4, 4), dtype=complex) for _ in range(3)]
    am = [rand_herm(rng, 2) for _ in range(4)]
    AMK = [np.kron(a, I2) for a in am] + [np.zeros((4, 4), dtype=complex) for _ in range(6)]
    vals, sl = powers(XMK, AMK, eta, 0.3, 'weyl10', (0.0012, 0.0006, 0.0003))
    print('(e2) d=10 Weyl, M x K (fuzzy su(2), N=2), A along M only  |dGamma|', np.abs(vals), 'slopes', sl)
    # the linear term vanishes only on a solution; here the fluctuation has no K component and the flux of M vanishes, so it is even in t
    assert abs(sl[-1] - 2) < 0.35
    # second-order coefficient of (e2) at two regulators
    t = 0.0006
    for e in (0.3, 1.0, 3.0):
        g0 = gamma_eps(XMK, eta, e, 'weyl10')
        gp = gamma_eps([x + t * a for x, a in zip(XMK, AMK)], eta, e, 'weyl10')
        print('    eps=%.1f: (Gamma[t]-Gamma[0])/t^2 = %s' % (e, np.array2string(np.array((gp - g0) / t**2), precision=5)))
    # the same M-part fluctuation with K removed: back to t^4
    X_noK = [np.kron(x, I2).astype(complex) for x in m] + [np.zeros((4, 4), dtype=complex) for _ in range(6)]
    report('(e3) same without K flux: commuting again', X_noK, AMK, eta, 0.3, 'weyl10', 4)
    print('ALL ASSERTIONS PASSED')


if __name__ == '__main__':
    main()
