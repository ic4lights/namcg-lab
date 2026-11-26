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


def gamma_slog(X, sig):
    """Same operators and weights as gamma_eps with content 'weyl10' and the Euclidean contraction, using slogdet (r2 section)."""
    d = len(X)
    P = ad_ops(X)
    n = P[0].shape[0]
    P2 = sum(P[a] @ P[a] for a in range(d))
    comm = {(a, b): P[a] @ P[b] - P[b] @ P[a] for a in range(d) for b in range(d)}
    Hg = P2 + sig * np.eye(n)
    HV = np.kron(np.eye(d), Hg).astype(complex)
    for b in range(d):
        for a in range(d):
            HV[b * n:(b + 1) * n, a * n:(a + 1) * n] += -2 * comm[(a, b)]
    G, chi = gammas(10)
    vals, vecs = np.linalg.eigh(chi)
    Pz = vecs[:, vals > 0]
    HF = np.kron(np.eye(16), Hg).astype(complex)
    for a in range(d):
        for b in range(d):
            if a != b:
                HF = HF + np.kron(Pz.conj().T @ (0.25 * (G[a] @ G[b] - G[b] @ G[a])) @ Pz, comm[(a, b)])
    ld = lambda M: np.linalg.slogdet(M)[1]
    return 0.5 * ld(HV) - ld(Hg) - 0.25 * ld(HF)


def gamma_offdiag(X0, X, sig):
    """The same three operators restricted, for every species, to the index pairs with nonzero difference of the eigenvalues of X0.

    Each restricted operator is still one common operator plus constant spin matrices times one operator, so the species identities
    apply as before.  This removes the Q = 0 modes and tests where the sigma^-2 comes from.  It is not the standard object, in which
    the diagonal elements are treated as moduli and no statement is made about it here."""
    d = len(X)
    n = X[0].shape[0]
    N2 = n * n
    keep = [i * n + j for i in range(n) for j in range(n) if i != j]
    P = ad_ops(X)
    P2 = sum(P[a] @ P[a] for a in range(d))
    comm = {(a, b): P[a] @ P[b] - P[b] @ P[a] for a in range(d) for b in range(d)}
    Hg = P2 + sig * np.eye(N2)
    HV = np.kron(np.eye(d), Hg).astype(complex)
    for b in range(d):
        for a in range(d):
            HV[b * N2:(b + 1) * N2, a * N2:(a + 1) * N2] += -2 * comm[(a, b)]
    G, chi = gammas(10)
    vals, vecs = np.linalg.eigh(chi)
    Pz = vecs[:, vals > 0]
    HF = np.kron(np.eye(16), Hg).astype(complex)
    for a in range(d):
        for b in range(d):
            if a != b:
                HF = HF + np.kron(Pz.conj().T @ (0.25 * (G[a] @ G[b] - G[b] @ G[a])) @ Pz, comm[(a, b)])
    kV = [c * N2 + k for c in range(d) for k in keep]
    kF = [c * N2 + k for c in range(16) for k in keep]
    ld = lambda M, K: np.linalg.slogdet(M[np.ix_(K, K)])[1]
    return 0.5 * ld(HV, kV) - ld(Hg, keep) - 0.25 * ld(HF, kF)


def gamma_mp(X, sig, dps=60):
    """The same trace in mpmath at dps digits, as a roundoff check of gamma_slog at one point."""
    import mpmath as mp
    mp.mp.dps = dps
    d = len(X)
    P = ad_ops(X)
    n = P[0].shape[0]
    P2 = sum(P[a] @ P[a] for a in range(d))
    comm = {(a, b): P[a] @ P[b] - P[b] @ P[a] for a in range(d) for b in range(d)}
    Hg = P2 + 0j * P2
    HV = np.kron(np.eye(d), Hg).astype(complex)
    for b in range(d):
        for a in range(d):
            HV[b * n:(b + 1) * n, a * n:(a + 1) * n] += -2 * comm[(a, b)]
    G, chi = gammas(10)
    vals, vecs = np.linalg.eigh(chi)
    Pz = vecs[:, vals > 0]
    HF = np.kron(np.eye(16), Hg).astype(complex)
    for a in range(d):
        for b in range(d):
            if a != b:
                HF = HF + np.kron(Pz.conj().T @ (0.25 * (G[a] @ G[b] - G[b] @ G[a])) @ Pz, comm[(a, b)])

    def ldm(M):
        A = mp.matrix(M.shape[0], M.shape[1])
        for i, j in zip(*np.nonzero(M)):
            A[int(i), int(j)] = mp.mpc(float(M[i, j].real), float(M[i, j].imag))
        for i in range(M.shape[0]):
            A[i, i] += mp.mpf(float(sig))
        return mp.log(abs(mp.det(A)))
    return 0.5 * ldm(HV) - ldm(Hg) - mp.mpf(1) / 4 * ldm(HF)


def draw_gatekeeper_data():
    """The draws of the review's own script: seed 52, N=3, ten diagonal matrices, then ten Hermitian matrices."""
    rng = np.random.default_rng(52)
    n = 3
    X0 = [np.diag(rng.normal(size=n)).astype(complex) for _ in range(10)]
    A = []
    for _ in range(10):
        a = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        A.append((a + a.conj().T) / 2)
    return X0, A


def draw_s1_data():
    """The draws of main(): seed 52001, X0 diagonal in four directions.  Independent of the review's data."""
    rng = np.random.default_rng(52001)
    X0 = [(np.diag(rng.normal(size=3)) * 2.0).astype(complex) for _ in range(4)] + [np.zeros((3, 3), dtype=complex) for _ in range(6)]
    A = [rand_herm(rng, 3) for _ in range(10)]
    return X0, A


def dG(X0, A, t, sig, base=None):
    b = gamma_slog(X0, sig) if base is None else base
    return gamma_slog([x + t * a for x, a in zip(X0, A)], sig) - b


def r2_section():
    print()
    print('R2 SECTION: dependence on the regulator, for R1 of the review.  Euclidean contraction, common shift sigma, Q = 0 modes included.')
    Xg, Ag = draw_gatekeeper_data()
    Xs, As = draw_s1_data()
    print('consistency gamma_slog vs gamma_eps at t=0.1, sigma=0.3:', gamma_slog([x + 0.1 * a for x, a in zip(Xs, As)], 0.3), gamma_eps([x + 0.1 * a for x, a in zip(Xs, As)], [1] * 10, 0.3, 'weyl10').real)
    print()
    print('A. Table of the review: seed 52, amplitudes halving from 0.32.  dGamma and successive log2 slopes.')
    amps = [.32, .16, .08, .04, .02, .01, .005]
    for sig in (1.0, 0.3, 1e-2, 1e-4):
        base = gamma_slog(Xg, sig)
        v = [dG(Xg, Ag, t, sig, base) for t in amps]
        sl = [np.log(abs(v[i] / v[i + 1])) / np.log(2) for i in range(len(v) - 1)]
        print('  sigma=%-7g vals %s' % (sig, ' '.join('%.2e' % x for x in v)))
        print('  %s slopes %s ; dGamma/t^4 at t=0.005: %.3e' % (' ' * 13, ' '.join('%.2f' % x for x in sl), v[-1] / amps[-1]**4))
    print()
    for name, X0, A in (('seed 52 (review data)', Xg, Ag), ('seed 52001 (s1 data)', Xs, As)):
        print('B. %s: coefficient C = dGamma/t^4 at small x = t/sigma^(1/2), x = 0.03, and its local exponent in sigma.' % name)
        prev = None
        for sig in (1.0, 0.3, 0.1, 0.03, 0.01, 1e-3, 1e-4, 1e-5):
            t = 0.03 * sig**0.5
            base = gamma_slog(X0, sig)
            c = dG(X0, A, t, sig, base) / t**4
            c2 = dG(X0, A, t / 2, sig, base) / (t / 2)**4
            ex = '' if prev is None else 'local exponent %+.3f' % (np.log(abs(c / prev[1])) / np.log(sig / prev[0]))
            assert prev is None or abs(np.log(abs(c / prev[1])) / np.log(sig / prev[0]) + 2) < 0.1
            print('  sigma=%-7g t=%.3e C=%.4e C(t/2)=%.4e  C*sigma^2=%.4e  %s' % (sig, t, c, c2, c * sig**2, ex))
            prev = (sig, c)
        print('C. %s: local slope d ln|dGamma| / d ln t against x = t/sigma^(1/2).' % name)
        xs = [0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0]
        print('  sigma     ' + ' '.join('x=%-6g' % x for x in xs))
        for sig in (1e-2, 1e-3, 1e-4, 1e-5, 1e-6):
            base = gamma_slog(X0, sig)
            row = []
            for x in xs:
                t = x * sig**0.5
                row.append(np.log(abs(dG(X0, A, t * 2**0.25, sig, base) / dG(X0, A, t * 2**-0.25, sig, base))) / np.log(2**0.5))
            print('  %-9g ' % sig + ' '.join('%-8.2f' % r for r in row))
            assert abs(row[0] - 4) < 0.02 and abs(row[1] - 4) < 0.05 and max(abs(r) for r in row[5:]) < 1.3
        print('D. %s: dGamma at fixed x across sigma (collapse onto a function of x alone when sigma and t are small against Q^2 and Q).' % name)
        for x in (0.1, 0.3, 1.0, 3.0):
            print('  x=%-4g ' % x + ' '.join('sigma=%g: %.4e' % (sig, dG(X0, A, x * sig**0.5, sig)) for sig in (1e-3, 1e-4, 1e-5, 1e-6)))
    Aoff = [a - np.diag(np.diag(a)) for a in Ag]
    print('E. Off-diagonal A only, seed 52: slopes as for table A.')
    for sig in (1e-2, 1e-4):
        base = gamma_slog(Xg, sig)
        am = [.08, .04, .02, .01, .005, .0025]
        v = [dG(Xg, Aoff, t, sig, base) for t in am]
        print('  sigma=%-7g vals %s slopes %s' % (sig, ' '.join('%.2e' % x for x in v), ' '.join('%.2f' % (np.log(abs(v[i] / v[i + 1])) / np.log(2)) for i in range(len(v) - 1))))
    print('F. Roundoff check at 60 digits, seed 52: sigma=1e-4, t=3e-4 (x=0.03) and t=1e-3 (x=0.1).')
    for t in (3e-4, 1e-3):
        sig = 1e-4
        Xp = [x + t * a for x, a in zip(Xg, Ag)]
        m = gamma_mp(Xp, sig) - gamma_mp(Xg, sig)
        print('  t=%g: slogdet %.10e ; mpmath %s' % (t, dG(Xg, Ag, t, sig), str(m)[:18]))
    print('G. Same data with the Q = 0 modes removed from every species: coefficient dGamma/t^4 at fixed t, and exponents in t.')
    for name, X0, A in (('seed 52', Xg, Ag), ('seed 52001', Xs, As)):
        for sig in (1.0, 0.3, 1e-2, 1e-4, 1e-6, 1e-8):
            base = gamma_offdiag(X0, X0, sig)
            v = [gamma_offdiag(X0, [x + t * a for x, a in zip(X0, A)], sig) - base for t in (0.08, 0.04, 0.02)]
            sl = [np.log(abs(v[i] / v[i + 1])) / np.log(2) for i in range(2)]
            print('  %-10s sigma=%-7g dGamma/t^4 at t=0.02: %.4e ; slopes %.3f %.3f' % (name, sig, v[-1] / 0.02**4, sl[0], sl[1]))
            assert abs(sl[1] - 4) < 0.15
    print('R2 SECTION DONE')


if __name__ == '__main__':
    main()
    r2_section()
