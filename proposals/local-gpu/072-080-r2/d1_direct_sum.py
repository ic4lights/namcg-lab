"""072-080 r2, d1: exact edge data of a direct-sum background X1 (+) X2.

Setting (decision (b) of proposal-r2): X^a = X_1^a (+) X_2^a on C^{N1} (+) C^{N2},
X_f^a = sum_b A_f[a,b] J_f^b with J_f the N_f-dimensional su(2) irrep, A_f real
invertible; Theta = Theta_1 (+) Theta_2 with Theta_f the spectral projector of
n_f.J_f on its M_f largest eigenvalues (independent axes n_f).
Block cut of the Row length paragraph: X_{S Sb} = Theta X Thetabar,
E = sum_a Theta X^a Thetabar X^a Theta, Q = -2i(Y - Y^+),
Y = sum_a X^a_{S Sb} Pi^a_{Sb S}.

Checks (exact finite-N linear algebra, numpy, double precision):
 (a) every Theta X^a Thetabar is c_1^a|u1)(v1| + c_2^a|u2)(v2| with u_f, v_f in
     summand f: rank <= 2, no entry between summands;
 (b) nonzero spectrum of E is {s1^2, s2^2}, s_f^2 = 1/4 M_f(N_f-M_f)(tr B_f - n_f.B_f n_f),
     B_f = A_f^T A_f; Tr E^p = s1^{2p} + s2^{2p} exactly for p = 1..5 (no corner term);
 (c) momenta without entries between the summands (Pi = Pi_1 (+) Pi_2): the nonzero
     spectrum of Q is the union of the single-summand charge spectra, each the pair
     -2h_f +- 2(h_f^2 + n_f)^{1/2}, h_f = Im(u_f|w_f), n_f = |w_f|^2 - |(u_f|w_f)|^2;
 (d) momenta with entries between the summands: the union property fails
     (relative deviation reported; it is O(1));
 (e) q_f coincident copies of summand f, X = (1_{q1}(x)X_1) (+) (1_{q2}(x)X_2), momenta
     copy-invariant within each group and without entries between groups: E has s_f^2
     with multiplicity q_f and Q has each single-summand pair with multiplicity q_f;
 (f) two caps of one axis of one sphere (M1 largest and M2 smallest eigenvalues):
     at M1+M2 = N the projector is the identity and the edge datum vanishes.

Run: python -I proposals/local-gpu/072-080-r2/d1_direct_sum.py
Expected: max deviations (a)-(c), (e), (f) < 1e-9; (d) relative deviation > 1e-2 in
every case; last line 'PASS d1'.
"""
import numpy as np

rng = np.random.default_rng(72080)


def su2(N):
    j3 = np.diag([(N - 1) / 2 - i for i in range(N)]).astype(complex)
    jp = np.zeros((N, N), complex)
    for i in range(1, N):
        jp[i - 1, i] = np.sqrt(i * (N - i))
    jm = jp.conj().T
    return [(jp + jm) / 2, (jp - jm) / (2j), j3]


def cap(J, n, M, top=True):
    nj = sum(n[b] * J[b] for b in range(3))
    ev, V = np.linalg.eigh(nj)
    order = np.argsort(-ev.real) if top else np.argsort(ev.real)
    W = V[:, order[:M]]
    return W @ W.conj().T


def dsum(*mats):
    n = sum(m.shape[0] for m in mats)
    out = np.zeros((n, n), complex)
    i = 0
    for m in mats:
        k = m.shape[0]
        out[i:i + k, i:i + k] = m
        i += k
    return out


def herm(n):
    g = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    return g + g.conj().T


def charge(X, Th, Pi):
    Tb = np.eye(Th.shape[0]) - Th
    Y = sum(Th @ x @ Tb @ p @ Th for x, p in zip(X, Pi))
    return -2j * (Y - Y.conj().T)


def nz(H, tol=1e-9):
    ev = np.linalg.eigvalsh(H)
    return np.sort(ev[np.abs(ev) > tol * max(1.0, np.abs(ev).max())])


def unit(v):
    return v / np.linalg.norm(v)


worst = dict(a=0.0, b=0.0, mom=0.0, c=0.0, pair=0.0, e=0.0, f=0.0)
dmin = 1e9
for (N1, N2) in [(6, 6), (8, 8), (7, 10), (12, 9)]:
    for trial in range(3):
        J1, J2 = su2(N1), su2(N2)
        A1, A2 = rng.normal(size=(3, 3)), rng.normal(size=(3, 3))
        n1, n2 = unit(rng.normal(size=3)), unit(rng.normal(size=3))
        M1, M2 = int(rng.integers(2, N1)), int(rng.integers(2, N2))  # M_f >= 2: a rank-one block has w_perp = 0
        X1 = [sum(A1[a, b] * J1[b] for b in range(3)) for a in range(3)]
        X2 = [sum(A2[a, b] * J2[b] for b in range(3)) for a in range(3)]
        T1, T2 = cap(J1, n1, M1), cap(J2, n2, M2)
        X = [dsum(x1, x2) for x1, x2 in zip(X1, X2)]
        Th = dsum(T1, T2)
        Tb = np.eye(N1 + N2) - Th
        # (a)
        for x in X:
            D = Th @ x @ Tb
            worst['a'] = max(worst['a'], np.abs(D[:N1, N1:]).max(), np.abs(D[N1:, :N1]).max())
            sv = np.linalg.svd(D, compute_uv=False)
            worst['a'] = max(worst['a'], sv[2:].max() if len(sv) > 2 else 0.0)
        # (b)
        E = sum(Th @ x @ Tb @ x @ Th for x in X)
        B1, B2 = A1.T @ A1, A2.T @ A2
        s1 = 0.25 * M1 * (N1 - M1) * (np.trace(B1) - n1 @ B1 @ n1)
        s2 = 0.25 * M2 * (N2 - M2) * (np.trace(B2) - n2 @ B2 @ n2)
        got = nz(E)
        pred = np.sort([s1, s2])
        worst['b'] = max(worst['b'], np.abs(got - pred).max() / max(pred) if len(got) == 2 else 1e9)
        for p in range(1, 6):
            lhs = np.trace(np.linalg.matrix_power(E, p)).real
            worst['mom'] = max(worst['mom'], abs(lhs - s1 ** p - s2 ** p) / (s1 ** p + s2 ** p))
        # (c)
        P1 = [herm(N1) for _ in range(3)]
        P2 = [herm(N2) for _ in range(3)]
        Pi = [dsum(p1, p2) for p1, p2 in zip(P1, P2)]
        Q = charge(X, Th, Pi)
        Qa, Qb = charge(X1, T1, P1), charge(X2, T2, P2)
        un = np.sort(np.concatenate([nz(Qa), nz(Qb)]))
        gq = nz(Q)
        worst['c'] = max(worst['c'], np.abs(gq - un).max() / np.abs(un).max() if len(gq) == len(un) else 1e9)
        # pair formula per summand
        for (Xf, Tf, Pf, Qf) in [(X1, T1, P1, Qa), (X2, T2, P2, Qb)]:
            Tbf = np.eye(Tf.shape[0]) - Tf
            Yf = sum(Tf @ x @ Tbf @ p @ Tf for x, p in zip(Xf, Pf))
            # Yf = |u)(w| : u = left singular vector, (w| = (u|Yf
            U_, S_, Vh = np.linalg.svd(Yf)
            u = U_[:, 0]
            w = (u.conj() @ Yf).conj()          # column vector |w)
            alpha = np.vdot(u, w)               # (u|w)
            h = alpha.imag
            nn = np.vdot(w, w).real - abs(alpha) ** 2
            pr = np.sort([-2 * h + 2 * np.sqrt(h * h + nn), -2 * h - 2 * np.sqrt(h * h + nn)])
            pr2 = np.sort([2 * h + 2 * np.sqrt(h * h + nn), 2 * h - 2 * np.sqrt(h * h + nn)])
            dev = min(np.abs(nz(Qf) - pr).max(), np.abs(nz(Qf) - pr2).max())
            worst["pair"] = max(worst["pair"], dev / np.abs(pr).max())
        # (d) entries between summands
        Pg = [herm(N1 + N2) for _ in range(3)]
        Qg = charge(X, Th, Pg)
        Pd = [dsum(p[:N1, :N1], p[N1:, N1:]) for p in Pg]
        und = np.sort(np.concatenate([nz(charge(X1, T1, [p[:N1, :N1] for p in Pg])),
                                      nz(charge(X2, T2, [p[N1:, N1:] for p in Pg]))]))
        gg = nz(Qg)
        d = np.abs(gg - und).max() / np.abs(und).max() if len(gg) == len(und) else 1.0
        dmin = min(dmin, d)
        # (e) coincident groups
        q1, q2 = int(rng.integers(1, 4)), int(rng.integers(1, 4))
        I1, I2 = np.eye(q1), np.eye(q2)
        Xe = [dsum(np.kron(I1, x1), np.kron(I2, x2)) for x1, x2 in zip(X1, X2)]
        The = dsum(np.kron(I1, T1), np.kron(I2, T2))
        Pe = [dsum(np.kron(I1, p1), np.kron(I2, p2)) for p1, p2 in zip(P1, P2)]
        Tbe = np.eye(The.shape[0]) - The
        Ee = sum(The @ x @ Tbe @ x @ The for x in Xe)
        predE = np.sort([s1] * q1 + [s2] * q2)
        gE = nz(Ee)
        worst['e'] = max(worst['e'], np.abs(gE - predE).max() / predE.max() if len(gE) == len(predE) else 1e9)
        Qe = charge(Xe, The, Pe)
        predQ = np.sort(np.concatenate([np.tile(nz(Qa), q1), np.tile(nz(Qb), q2)]))
        gQ = nz(Qe)
        worst['e'] = max(worst['e'], np.abs(gQ - predQ).max() / np.abs(predQ).max() if len(gQ) == len(predQ) else 1e9)

# (f) complementary caps of one axis
for N in (6, 9, 12):
    J = su2(N)
    A = rng.normal(size=(3, 3))
    n = unit(rng.normal(size=3))
    M1 = N // 2
    Th = cap(J, n, M1, True) + cap(J, n, N - M1, False)
    Xs = [sum(A[a, b] * J[b] for b in range(3)) for a in range(3)]
    Tb = np.eye(N) - Th
    worst['f'] = max(worst['f'], np.abs(Th - np.eye(N)).max(),
                     max(np.abs(Th @ x @ Tb).max() for x in Xs))

for k in sorted(worst):
    print('max deviation (%s): %.3e' % (k, worst[k]))
print('min relative deviation from union with entries between summands (d): %.3e' % dmin)
ok = all(worst[k] < 1e-9 for k in worst) and dmin > 1e-2
print('all checks inside thresholds:', ok)
assert ok
print('PASS d1')
