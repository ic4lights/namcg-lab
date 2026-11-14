"""
067 e3: classicalised edge charge of a toric block on S^2_N x S^2_N.

Q = -2i sum_a (X^a_{S S'} Pi^a_{S' S} - Pi^a_{S S'} X^a_{S' S})  [arXiv:2408.05274 Eq. (4.4)],  Y := sum_a X^a_{S S'} Pi^a_{S' S},
so Q = -2i (Y - Y^dagger).  The range of Y lies in the span of the edge sites (columns of U, M x r).

Part 0 (exact, operator level): block cap x whole second sphere, generic A1, A2: edge map of rank N, E = s1^2 on the
        N edge sites, T = N s1, s^2 = N s1^2, independent of A2.
Part 1 (exact second moments, N=6, generic A1, A2): Gaussian momenta, independent over a, with variance f(l1,l2) on
        the (spin l1) (x) (spin l2) matrices.  Then D_{v v'} = sum_{j in S} <Pi_{v j} conj Pi_{v' j}> is diagonal, and
        <Y Y^dagger> = diag over edge sites u of  Et_u = sum_{links u->v} kappa_link D_vv   (state-weighted E of e1).
        For cap x whole sphere: D_vv = W = sum f(l1,l2) (2 l2 + 1)/N w_{l1}(M1) on every edge link, <Y Y^dagger> = s1^2 W 1_N.
        Also reports Re<Tr Y^2>/<Tr Y Y^dagger>  (<Tr Q^2> = 8 <Tr Y Y^dagger> - 8 Re <Tr Y^2>).
Part 2 (exact reduction, any Hermitian Pi): with C = U^dagger Y, alpha = C U, C_perp = C (1 - U U^dagger) = Rm^dagger V^dagger,
        the nonzero spectrum of Q is that of [[-2i(alpha - alpha^dagger), -2i Rm^dagger], [2i Rm, 0]];
        for alpha = 0 it is +-2 (singular values of C_perp).
Part 3 (Monte Carlo, N=16, cap x whole sphere): sum of the positive eigenvalues of Q against 2 sum_u sqrt(Et_u) = 2 N s1 sqrt(W)
        and against the same with W_perp (edge sites removed from the row sum), for several cut-offs.
Output to stdout only.
"""
import numpy as np

rng = np.random.default_rng(67003)

def su2(N):
    j3 = np.diag([(N - 1) / 2 - i for i in range(N)]).astype(complex)
    jp = np.zeros((N, N), complex)
    for i in range(1, N):
        jp[i - 1, i] = np.sqrt(i * (N - i))
    jm = jp.conj().T
    return [(jp + jm) / 2, (jp - jm) / (2j), j3]

def config(N, A1, A2):
    J = su2(N); I = np.eye(N)
    X = [np.kron(sum(A1[a, b] * J[b] for b in range(3)), I) for a in range(3)]
    X += [np.kron(I, sum(A2[a, b] * J[b] for b in range(3))) for a in range(3)]
    return X

def spin_projectors(N):
    """P[l] : N^2 x N^2 real symmetric projector on the spin-l matrices, vec index r*N + c."""
    J = su2(N); I = np.eye(N)
    C = np.zeros((N * N, N * N), complex)
    for Ja in J:
        ad = np.kron(Ja, I) - np.kron(I, Ja.T)
        C += ad @ ad
    assert np.abs(C.imag).max() < 1e-12
    lam, V = np.linalg.eigh(C.real)
    l = np.rint((-1 + np.sqrt(1 + 4 * np.clip(lam, 0, None))) / 2).astype(int)
    assert np.allclose(l * (l + 1), lam, atol=1e-8)
    return [V[:, l == k] @ V[:, l == k].T for k in range(N)]

def k_of(A): return 0.25 * (A[:, 0] ** 2 + A[:, 1] ** 2).sum()

# ------------------------------------------------------------ Part 0
N = 7; M1 = 3
A1 = rng.normal(size=(3, 3)); A2 = rng.normal(size=(3, 3))
X = config(N, A1, A2)
ii1, ii2 = np.meshgrid(np.arange(N), np.arange(N), indexing='ij')
Om = (ii1 < M1)
th = Om.reshape(-1).astype(float); Th = np.diag(th); Tb = np.eye(N * N) - Th
Eop = sum(Th @ x @ Tb @ x @ Th for x in X)
s1sq = k_of(A1) * M1 * (N - M1)
ev = np.linalg.eigvalsh(Eop); ev = ev[ev > 1e-9]
rank = np.linalg.matrix_rank(np.hstack([Th @ x @ Tb for x in X]), tol=1e-8)
dev0 = max(np.abs(Eop - np.diag(np.diag(Eop))).max(), np.abs(ev - s1sq).max(), abs(np.sqrt(ev).sum() - N * np.sqrt(s1sq)))
X2 = config(N, A1, 3.7 * rng.normal(size=(3, 3)))
dev0 = max(dev0, np.abs(sum(Th @ x @ Tb @ x @ Th for x in X2) - Eop).max())
print('Part 0  cap x whole sphere N=%d M1=%d: rank %d (N=%d), nonzero eigenvalues of E: %d, all = s1^2; T - N s1, offdiag, A2-dependence: max dev %.1e'
      % (N, M1, rank, N, len(ev), dev0))
assert rank == N and len(ev) == N and dev0 < 1e-9

# ------------------------------------------------------------ Part 1
N = 6
P = spin_projectors(N)
P4 = [p.reshape(N, N, N, N) for p in P]               # [r, c, r', c']
A1 = rng.normal(size=(3, 3)); A2 = rng.normal(size=(3, 3))
X = config(N, A1, A2)
lc1, lc2 = 4, 3
f = lambda l1, l2: 0.5 * (l1 + l2) + 0.1
# cov[(a,b),(a',b') ; (c,d),(c',d')] = <Pi_{(ab),(a'b')} conj Pi_{(cd),(c'd')}>
cov = np.zeros((N,) * 8)
for l1 in range(lc1 + 1):
    for l2 in range(lc2 + 1):
        cov += f(l1, l2) * np.einsum('aAcC,bBdD->abABcdCD', P4[l1], P4[l2])
cov = cov.reshape(N * N, N * N, N * N, N * N)          # [row, col, row', col']
ii1, ii2 = np.meshgrid(np.arange(N), np.arange(N), indexing='ij')

def second_moments(Om, label):
    inn = np.flatnonzero(Om.reshape(-1)); out = np.flatnonzero(~Om.reshape(-1))
    D = np.einsum('vjwj->vw', cov[np.ix_(out, inn, out, inn)])
    offD = np.abs(D - np.diag(np.diag(D))).max()
    YY = sum(x[np.ix_(inn, out)] @ D @ x[np.ix_(out, inn)] for x in X)
    # link formula
    k1, k2 = k_of(A1), k_of(A2)
    Dfull = np.zeros(N * N); Dfull[out] = np.diag(D); Dg = Dfull.reshape(N, N)
    Et = np.zeros((N, N))
    for i1 in range(N):
        for i2 in range(N):
            if not Om[i1, i2]: continue
            e = 0.0
            if i1 - 1 >= 0 and not Om[i1 - 1, i2]: e += k1 * i1 * (N - i1) * Dg[i1 - 1, i2]
            if i1 + 1 < N and not Om[i1 + 1, i2]: e += k1 * (i1 + 1) * (N - i1 - 1) * Dg[i1 + 1, i2]
            if i2 - 1 >= 0 and not Om[i1, i2 - 1]: e += k2 * i2 * (N - i2) * Dg[i1, i2 - 1]
            if i2 + 1 < N and not Om[i1, i2 + 1]: e += k2 * (i2 + 1) * (N - i2 - 1) * Dg[i1, i2 + 1]
            Et[i1, i2] = e
    devY = np.abs(YY - np.diag(Et.reshape(-1)[inn])).max()
    # <Y^2> = sum_a X_{SS'} <Pi_{S'S} X_{SS'} Pi_{S'S}>, <Pi_{vj} Pi_{v'j'}> = cov[(v,j),(j',v')]
    c2 = cov[np.ix_(out, inn, inn, out)]               # [v, j, j', v']
    trY2 = 0.0
    for x in X:
        A = x[np.ix_(inn, out)]
        mid = np.einsum('vjkw,jw->vk', c2, A)          # sum_{j,v'} A[j,v'] cov[(v,j),(j',v')] -> [v, j']
        trY2 += np.trace(A @ mid).real
    print('Part 1  %-26s offdiag(D)=%.1e  |<YY^+> - diag(Et)|=%.1e  <Tr YY^+>=%.5f  Re<Tr Y^2>/<Tr YY^+>=%+.4f'
          % (label, offD, devY, np.trace(YY).real, trY2 / np.trace(YY).real))
    return offD, devY, D, Et

worst = 0.0
M1 = 2
o, d, D, Et = second_moments(ii1 < M1, 'cap x whole sphere M1=2'); worst = max(worst, o, d)
w = [sum(P4[l1][M1, a, M1, a] for a in range(M1)) for l1 in range(N)]
W = sum(f(l1, l2) * (2 * l2 + 1) / N * w[l1] for l1 in range(lc1 + 1) for l2 in range(lc2 + 1))
edge_out = (ii1 == M1).reshape(-1)[np.flatnonzero(~(ii1 < M1).reshape(-1))]
devW = np.abs(np.diag(D)[edge_out] - W).max()
devE = np.abs(Et[M1 - 1, :] - k_of(A1) * M1 * (N - M1) * W).max()
print('        uniform row sum on the edge: |D_vv - W| = %.1e, |Et_u - s1^2 W| = %.1e  (W = %.6f)' % (devW, devE, W))
worst = max(worst, devW, devE)
o, d, *_ = second_moments((ii1 < 3) & (ii2 < 4), 'product block 3 x 4'); worst = max(worst, o, d)
o, d, *_ = second_moments(1.0 * ii1 + 0.62 * ii2 < 3.9, 'half-plane b/a=0.62'); worst = max(worst, o, d)
o, d, *_ = second_moments(((ii1 < 2) & (ii2 < 2)) | ((ii1 > 3) & (ii2 > 3)), 'two corner blocks'); worst = max(worst, o, d)
assert worst < 1e-10

# ------------------------------------------------------------ Part 2
def charge(X, Pis, inn, out):
    Y = sum(x[np.ix_(inn, out)] @ p[np.ix_(out, inn)] for x, p in zip(X, Pis))
    return Y, -2j * (Y - Y.conj().T)

def reduced(Y, U):
    C = U.conj().T @ Y; al = C @ U; Cp = C - al @ U.conj().T
    V, Rm = np.linalg.qr(Cp.conj().T)
    r = U.shape[1]
    Rd = np.block([[-2j * (al - al.conj().T), -2j * Rm.conj().T], [2j * Rm, np.zeros((r, r))]])
    return np.linalg.eigvalsh(Rd), np.linalg.svd(Cp, compute_uv=False)

worst2 = 0.0
for Om, label in (((ii1 < 2), 'cap x whole sphere'), ((ii1 < 3) & (ii2 < 4), 'product block 3 x 4'), (1.0 * ii1 + 0.62 * ii2 < 3.9, 'half-plane')):
    inn = np.flatnonzero(Om.reshape(-1)); out = np.flatnonzero(~Om.reshape(-1))
    Pis = []
    for a in range(6):
        Z = rng.normal(size=(N * N, N * N)) + 1j * rng.normal(size=(N * N, N * N)); Pis.append((Z + Z.conj().T) / 2)
    Y, Q = charge(X, Pis, inn, out)
    edge = np.flatnonzero(np.abs(Y).sum(axis=1) > 1e-12)
    U = np.eye(len(inn))[:, edge]
    assert np.abs(Y - U @ U.T @ Y).max() < 1e-12
    evQ = np.linalg.eigvalsh(Q); evR, sv = reduced(Y, U)
    r = len(edge)
    nzQ = np.sort(evQ[np.argsort(np.abs(evQ))[len(evQ) - min(2 * r, len(evQ)):]])
    if 2 * r <= len(inn):
        dev = np.abs(nzQ - np.sort(evR)).max(); worst2 = max(worst2, dev)
        print('Part 2  %-22s M=%2d r=%2d  |spec(Q)_nonzero - spec(reduced)| = %.1e ; 4 Im Tr Y = Tr Q = %+.2f (unconstrained momenta)' % (label, len(inn), r, dev, np.trace(Q).real))
    else:
        print('Part 2  %-22s M=%2d r=%2d  2r > M: reduction not applicable' % (label, len(inn), r))
assert worst2 < 1e-9

# ------------------------------------------------------------ Part 3
N = 16; M1 = 8
P = spin_projectors(N)
A1 = np.diag([1.0, 1.0, 1.0]); A2 = 1.4 * np.eye(3)
X = config(N, A1, A2)
ii1, ii2 = np.meshgrid(np.arange(N), np.arange(N), indexing='ij')
Om = ii1 < M1
inn = np.flatnonzero(Om.reshape(-1)); out = np.flatnonzero(~Om.reshape(-1))
edge = np.flatnonzero((ii1 == M1 - 1).reshape(-1)[inn]); U = np.eye(len(inn))[:, edge]
s1 = np.sqrt(k_of(A1) * M1 * (N - M1))
P4 = [p.reshape(N, N, N, N) for p in P]
print('Part 3  cap x whole sphere, N=%d M1=%d (M=%d, r=%d), round, f = (l1/2) 1[l1<=lc1] 1[l2<=lc2], 60 samples' % (N, M1, len(inn), N))
for lc1, lc2 in ((3, 3), (8, 3), (15, 3), (15, 8)):
    f1 = np.array([0.5 * l if l <= lc1 else 0.0 for l in range(N)])
    f2 = np.array([1.0 if l <= lc2 else 0.0 for l in range(N)])
    F1 = sum(np.sqrt(f1[l]) * P[l] for l in range(N)); F2 = sum(np.sqrt(f2[l]) * P[l] for l in range(N))
    wl = np.array([sum(P4[l][M1, a, M1, a] for a in range(M1)) for l in range(N)])
    wlp = np.array([sum(P4[l][M1, a, M1, a] for a in range(M1 - 1)) for l in range(N)])
    fib = sum((2 * l + 1) * f2[l] for l in range(N)) / N
    W = (f1 * wl).sum() * fib; Wp = (f1 * wlp).sum() * fib
    pos = []; trYY = []; cv = []; npos = []; posp = []
    for smp in range(60):
        Pis = []
        for a in range(3):                                # X^4..6 have no edge on this block
            Z = rng.normal(size=(N * N, N * N)) + 1j * rng.normal(size=(N * N, N * N)); G = (Z + Z.conj().T) / 2          # <|G_ij|^2> = 1
            G4 = G.reshape(N, N, N, N).transpose(0, 2, 1, 3).reshape(N * N, N * N)      # [(a,a'),(b,b')]
            G4 = F1 @ G4 @ F2.T
            Pis.append(G4.reshape(N, N, N, N).transpose(0, 2, 1, 3).reshape(N * N, N * N))
        Y, Q = charge(X[:3], Pis, inn, out)
        ev = np.linalg.eigvalsh(Q); p = ev[ev > 1e-9 * abs(ev).max()]
        top = np.sort(p)[-N:]
        pos.append(p.sum()); trYY.append(np.trace(Y @ Y.conj().T).real); cv.append(top.std() / top.mean()); npos.append(len(p))
        evR, sv = reduced(Y, U); posp.append(2 * sv.sum())
    print('    lc1=%2d lc2=%2d  <TrYY^+>/(N s1^2 W)=%.4f  W_perp/W=%.4f  <sum pos Q>/(2 N s1 sqrt W)=%.4f  <2 sum sv(C_perp)>/(2 N s1 sqrt W_perp)=%.4f'
          '  <sum pos Q>/<2 sum sv(C_perp)>=%.4f  #pos=%.1f  cv(rows)=%.3f'
          % (lc1, lc2, np.mean(trYY) / (N * s1 ** 2 * W), Wp / W, np.mean(pos) / (2 * N * s1 * np.sqrt(W)),
             np.mean(posp) / (2 * N * s1 * np.sqrt(Wp)), np.mean(pos) / np.mean(posp), np.mean(npos), np.mean(cv)))
    assert abs(np.mean(trYY) / (N * s1 ** 2 * W) - 1) < 0.05
print('PASS e3')
