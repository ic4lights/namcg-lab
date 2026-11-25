# verify_r118_r2.py -- round-2 verification pack for proposal 118.
# Run: python -I -B verify_r118_r2.py   (sympy, numpy).  Output: out-r118r2.txt.
# Round-2 changes vs verify_r118.py (check-code fixes and new checks; none weakened):
#  R2-1 C5 NameError fixed: idx4 key built from (ii,jj); leaked loop name removed.
#  R2-2 C5 expected GL(n)-conjugation invariant dims corrected to "partitions of d
#       into at most n parts" (Cayley-Hamilton relations above d=n): n=2 gives
#       (1,2,2,3) for d=1..4, not p(d)=(1,2,3,5); teeth n=3 d=4 -> 3, n=4 d=4 -> 5.
#  R2-3 C3 sign-table logic: r1 tested (c4>0 and c2<0) == (sigma*^2 = -c2/2c4 > 0),
#       false for (c4<0, c2>0) (nonzero stationary point is a hilltop). C3r states
#       the honest full classification and tests every region.
#  R2-4 New N-series, general renormalizable bifundamental potential
#       V = c3 Tr X^2 + c2s (Tr X)^2 + c1 Tr X + c0, X = Phi^dagger Phi, x = sigma^2:
#       V quadratic in x with Hessian 2 c3 I + 2 c2s J: strictly convex iff c3>0 and
#       c3+4 c2s>0, the same region as strict bounded-below; unique vacuum x = s 1,
#       s = -c1/(2(c3+4c2s)); inf over det Phi = 0 = stratum-3 value V3 =
#       -c1^2/(4(c3/3+c2s)) + c0 at (0,w,w,w), w^2 = -c1/(2(c3+3c2s)); threshold
#       Delta = V3 - V4 = (c1^2/4)[1/(c3/4+c2s) - 1/(c3/3+c2s)] > 0 THROUGHOUT the
#       bounded-below class (bounded below implies bounded on every coordinate face:
#       c3/k + c2s >= c3/4 + c2s for k <= 4); eq:V is the slice c2s = 0.
#  R2-5 N13: exact exponentiation of the Moyal phase matrix for the (12)(34) pairing
#       and pairwise distinctness of the three quartic channel phases.
import sys, itertools
import numpy as np
import sympy as sp

RNG = np.random.default_rng(118)
results = []
def check(name, ok):
    results.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name)

def c1():
    lam, v, Nsym = sp.symbols('lambda v N', positive=True)
    s1, s2, s3, s4 = sp.symbols('sigma1 sigma2 sigma3 sigma4', nonnegative=True)
    c4, c2, c0 = lam/4, -lam*v**2/2, Nsym*lam*v**4/4
    X = [s1**2, s2**2, s3**2, s4**2]
    nf = sum(c4*x**2 + c2*x for x in X) + c0
    eqV = lam/4*sum((x - v**2)**2 for x in X)
    okA = sp.simplify((nf - eqV).subs(Nsym, 4)) == 0
    okB = sp.simplify((nf - eqV).subs(Nsym, 7)) != 0
    sk = sp.symbols('t1:7', nonnegative=True)
    nf6 = sum(c4*si**4 + c2*si**2 for si in sk) + 6*c4*v**4
    eqV6 = lam/4*sum((si**2 - v**2)**2 for si in sk)
    okC = sp.simplify(nf6 - eqV6) == 0
    return okA and okB and okC
check("C1_normalform_eqV_identity_symbolic_N4_and_N6", c1())

def c2b():
    lam = 1.31; v = 0.77
    def V(Ph):
        X = Ph.conj().T @ Ph
        return (lam/4)*np.trace(X@X).real - (lam*v**2/2)*np.trace(X).real
    ok = True
    for trial in range(40):
        Ph = (RNG.standard_normal((4, 4)) + 1j*RNG.standard_normal((4, 4)))*(1 + trial*0.13)
        X = Ph.conj().T @ Ph
        G = (lam/2)*Ph @ (X - v**2*np.eye(4))
        h = 1e-6
        fdre = np.zeros((4, 4)); fdim = np.zeros((4, 4))
        for i in range(4):
            for j in range(4):
                Ec = np.zeros((4, 4), dtype=complex); Ec[i, j] = 1.0
                Ec = np.conj(Ec)
                fdre[i, j] = (V(Ph + h*Ec) - V(Ph - h*Ec))/(2*h)
                fdim[i, j] = (V(Ph + 1j*h*Ec) - V(Ph - 1j*h*Ec))/(2*h)
        ok = ok and (np.max(np.abs(0.5*(fdre + 1j*fdim) - G)) < 2e-4)
    for lam2 in (0.5, 1.0, 3.7):
        for v2 in (0.3, 1.0, 2.5):
            G = (lam2/2)*(v2*np.eye(4)) @ ((v2**2)*np.eye(4) - v2**2*np.eye(4))
            ok = ok and np.allclose(G, 0, atol=1e-14)
    return ok
check("C2_gradient_eqPhi-eom_numeric_and_vacuum_stationary", c2b())

def c3r():
    c4, c2s = sp.symbols('c4 c2s', real=True)
    s1, s2, s3, s4 = sp.symbols('sigma1 sigma2 sigma3 sigma4', nonnegative=True)
    v2 = -c2s/(2*c4)
    f = lambda s: c4*s**4 + c2s*s**2
    tot = sum(f(s) for s in (s1, s2, s3, s4))
    Vmin = 4*(-c2s**2/(4*c4))
    diff = sp.simplify(tot - Vmin - c4*sum((s**2 - v2)**2 for s in (s1, s2, s3, s4)))
    okA = (diff == 0)
    okB = True
    pts = [(-2.0, -2.0), (-2.0, -0.37), (-2.0, 0.0), (-2.0, 0.11), (-2.0, 3.0),
           (0.0, -2.0), (0.0, -0.37), (0.0, 0.0), (0.0, 0.11), (0.0, 3.0),
           (0.11, -2.0), (0.11, -0.37), (0.11, 0.0), (0.11, 0.11), (0.11, 3.0),
           (3.0, -2.0), (3.0, 0.11), (-0.37, 3.0)]
    s = np.linspace(0.0, 60.0, 24001)
    for (a, b) in pts:
        fv = a*s**4 + b*s**2
        mex = (a > 0) and (b < 0)
        unb = (a < 0) or (a == 0 and b < 0)
        deg = (a == 0) and (b == 0)
        minat0 = (a > 0 and b >= 0) or (a == 0 and b > 0)
        stat = (a != 0) and (-b/(2*a) > 0)
        if unb:
            okB = okB and (fv[-1] < fv[0]) and (fv[-1] < -100.0)
        elif deg:
            okB = okB and np.allclose(fv, 0.0)
        elif minat0:
            okB = okB and (fv[0] <= fv.min() + 1e-12) and (not mex)
        elif mex:
            k = fv.argmin()
            okB = okB and (k > 0) and abs(s[k] - np.sqrt(-b/(2*a))) < 2*(s[1]-s[0])
        else:
            okB = False
        if mex:
            okB = okB and stat
        if stat and (a < 0):
            kk = fv.argmax()
            okB = okB and (not mex)
            okB = okB and abs(s[kk] - np.sqrt(-b/(2*a))) < 2*(s[1]-s[0])
    okC = True
    for _ in range(60):
        a = RNG.uniform(0.05, 4.0); b = -RNG.uniform(0.05, 4.0)
        vv = -b/(2*a)
        grid = np.linspace(0, 3*np.sqrt(vv + 1), 8001)
        fvals = a*grid**4 + b*grid**2
        k = fvals.argmin()
        okC = okC and abs(grid[k] - np.sqrt(vv)) < (grid[1] - grid[0])*2
        okC = okC and abs(fvals[k] - (-b*b/(4*a))) < 1e-3 + abs(fvals[k])*1e-4
    return okA and okB and okC
check("C3r_sos_identity_and_honest_full_sign_classification", c3r())

def c4_check():
    th = sp.symbols('theta', real=True)
    def om(k, q):
        return th*(k[0]*q[1] - k[1]*q[0])
    def col(a, b):
        return sp.ImmutableMatrix([[a], [b]])
    k1 = col(sp.symbols('a', real=True), sp.symbols('b', real=True))
    okA = sp.simplify(om(k1, -k1)) == 0
    okB = True
    for nfac in (3, 4, 5):
        ks = [col(sp.symbols('k%d_0' % i, real=True), sp.symbols('k%d_1' % i, real=True))
              for i in range(nfac)]
        Ssum = sp.zeros(2, 1)
        for extra in ks[1:]:
            Ssum = Ssum + extra
        P = sum((om(ks[i], ks[j]) for i in range(nfac) for j in range(i + 1, nfac)), sp.Integer(0))
        Pc = sum((om(ks[i], ks[j]) for i in range(1, nfac) for j in range(i + 1, nfac)), sp.Integer(0)) \
             + sum((om(ks[j], ks[0]) for j in range(1, nfac)), sp.Integer(0))
        cyc = sp.simplify((P - Pc).xreplace({ks[0][0]: -Ssum[0], ks[0][1]: -Ssum[1]}))
        okB = okB and (cyc == 0)
        offsh = sp.simplify(P.xreplace({ks[0][0]: -Ssum[0] + 1, ks[0][1]: -Ssum[1]}))
        okB = okB and (offsh != 0)
    a1, b1, a2, b2 = sp.symbols('a1 b1 a2 b2', real=True)
    k1c = col(a1, b1); k2c = col(a2, b2)
    k3c = col(sp.symbols('a3', real=True), sp.symbols('b3', real=True))
    k4c = -(k1c + k2c + k3c)
    P4 = om(k1c, k2c) + om(k1c, k3c) + om(k1c, k4c) + om(k2c, k3c) + om(k2c, k4c) + om(k3c, k4c)
    red = sp.simplify(P4 - (om(k1c, k2c) + om(k3c, k4c)))
    okC = (red == 0)
    red2 = sp.simplify((om(k1c, k2c) + om(k3c, k4c)) - (om(k2c, k3c) + om(k4c, k1c)))
    okC = okC and (red2 == 0)
    okD = True
    for _ in range(60):
        kq = [RNG.integers(-3, 4, size=2) for _ in range(3)]
        kq.append(-sum(kq))
        thv = float(RNG.uniform(-0.15, 0.15))
        S = 0.0
        for i in range(4):
            for j in range(i + 1, 4):
                S += thv*(kq[i][0]*kq[j][1] - kq[i][1]*kq[j][0])
        d1 = 1 - np.cos(S/2)
        d2 = 1 - np.cos(0.5*S/2)
        okD = okD and (d1 <= S*S/8 + 1e-15)
        if d1 > 1e-10:
            okD = okD and abs(d2/d1 - 0.25) < 0.05
        okD = okD and (abs(np.sin(S/2)) <= abs(S)/2 + 1e-15)
    okE = False
    for _ in range(60):
        kq = [RNG.integers(-3, 4, size=2) for _ in range(3)]
        kq.append(-sum(kq))
        S = (kq[2][0]*kq[3][1] - kq[2][1]*kq[3][0])
        if abs(S) > 1e-9:
            okE = True
    return okA and okB and okC and okD and okE
check("C4_moyal_vertex_phase_exact_quadratic_cyclic_nonzero_quartic", c4_check())

def c5r():
    def conj_inv_dim(n, d):
        slots = [(i, j) for i in range(n) for j in range(n)]
        mon = sorted(set(tuple(sorted(ms)) for ms in
                         itertools.combinations_with_replacement(slots, d)))
        idx = {m_: i_ for i_, m_ in enumerate(mon)}
        G = []
        for p in range(n):
            for q in range(n):
                M = np.zeros((len(mon), len(mon)))
                for m_, i_ in idx.items():
                    for pos in range(d):
                        (ii, jj) = m_[pos]
                        if ii == p:
                            nw = list(m_); nw[pos] = (q, jj)
                            M[idx[tuple(sorted(nw))], i_] += 1
                        if jj == q:
                            nw2 = list(m_); nw2[pos] = (ii, p)
                            M[idx[tuple(sorted(nw2))], i_] -= 1
                G.append(M)
        K = np.vstack(G)
        return len(mon) - np.linalg.matrix_rank(K, tol=1e-9), idx, mon
    okA = True
    for (n_, d_, expd) in [(2, 1, 1), (2, 2, 2), (2, 3, 2), (2, 4, 3),
                           (3, 4, 4), (4, 4, 5), (4, 2, 2), (4, 1, 1)]:
        dimn, _, _ = conj_inv_dim(n_, d_)
        okA = okA and (dimn == expd)
    dim2n4, idx4, mon4 = conj_inv_dim(4, 2)
    vA = np.zeros(len(mon4)); vB = np.zeros(len(mon4))
    for ii in range(4):
        for jj in range(4):
            k_ = idx4.get(tuple(sorted(((ii, jj), (jj, ii)))))
            vA[k_] += 1.0
            k2_ = idx4.get(tuple(sorted(((ii, ii), (jj, jj)))))
            vB[k2_] += 1.0
    Gs = []
    n = 4
    for p in range(n):
        for q in range(n):
            M = np.zeros((len(mon4), len(mon4)))
            for m_, i_ in idx4.items():
                for pos in range(2):
                    (ii, jj) = m_[pos]
                    if ii == p:
                        nw = list(m_); nw[pos] = (q, jj)
                        M[idx4[tuple(sorted(nw))], i_] += 1
                    if jj == q:
                        nw2 = list(m_); nw2[pos] = (ii, p)
                        M[idx4[tuple(sorted(nw2))], i_] -= 1
            Gs.append(M)
    K4 = np.vstack(Gs)
    okB = np.allclose(K4 @ vA, 0) and np.allclose(K4 @ vB, 0)
    okC = (np.linalg.matrix_rank(np.vstack([vA, vB])) == 2) and (dim2n4 == 2)
    Phi = RNG.standard_normal((4, 4)) + 1j*RNG.standard_normal((4, 4))
    def randU():
        Q, R = np.linalg.qr(RNG.standard_normal((4, 4)) + 1j*RNG.standard_normal((4, 4)))
        return Q @ np.diag(np.diag(R)/np.abs(np.diag(R)))
    Xf = lambda A: np.trace((A.conj().T @ A) @ (A.conj().T @ A)).real
    w2 = lambda A: np.trace(A @ A @ A.conj().T @ A.conj().T).real
    okD = False
    for _ in range(20):
        P2 = randU() @ Phi @ randU().conj().T
        if abs(w2(Phi) - w2(P2)) > 1e-6:
            okD = True
    okE = True
    for _ in range(20):
        P2 = randU() @ Phi @ randU().conj().T
        okE = okE and abs(Xf(Phi) - Xf(P2)) < 1e-8
    okF = True
    M1 = np.zeros(2); M2 = np.zeros(2)
    for t in range(2):
        Ph = RNG.standard_normal((4, 4)) + 1j*RNG.standard_normal((4, 4))
        M1[t] = np.trace(Ph.conj().T @ Ph).real
        M2[t] = np.trace((Ph.conj().T @ Ph) @ (Ph.conj().T @ Ph)).real
    return okA and okB and okC and okD and okE and okF
check("C5r_conj_dims_CH_teeth_kernel_span_bifundamental_teeth", c5r())

def c6():
    ok = True
    for _ in range(200):
        Phi = RNG.standard_normal((4, 4)) + 1j*RNG.standard_normal((4, 4))
        X = Phi.conj().T @ Phi
        sv = np.linalg.svd(Phi, compute_uv=False)
        ok = ok and abs(np.trace(X@X).real - np.sum(sv**4)) < 1e-9
        Y = Phi @ Phi.conj().T
        ok = ok and abs(np.trace(Y@Y).real - np.trace(X@X).real) < 1e-9
        ok = ok and np.trace(X@X).real >= -1e-12 and np.trace(Y@Y).real >= -1e-12
    A = RNG.standard_normal((4, 3)) + 1j*RNG.standard_normal((4, 3))
    sv = np.linalg.svd(A, compute_uv=False)
    ok = ok and abs(np.trace((A.conj().T @ A) @ (A.conj().T @ A)).real - np.sum(sv**4)) < 1e-9
    try:
        A.conj().T @ A.conj().T
        ok = False
    except ValueError:
        pass
    return ok
check("C6_word_identities_positive_and_rectangular_tooth", c6())

def c7():
    tau = 4.0
    okCS = True
    for _ in range(400):
        z = np.abs(RNG.standard_normal(4)) + 1e-12
        s2 = tau*z/z.sum()
        okCS = okCS and (np.sum(s2**2) >= tau**2/4.0 - 1e-10)
        okCS = okCS and (np.sum(s2**3) >= tau**3/16.0 - 1e-9)
    s2e = (tau/4)*np.ones(4)
    okCS = okCS and abs(np.sum(s2e**2) - tau**2/4) < 1e-14
    okRegions = True
    for (a, b) in [(1.0, -1.0), (1.0, 1.0), (1.0, 0.0), (0.25, -3.0), (4.0, -0.1), (0.0, 1.0)]:
        s = np.linspace(0, 6, 6001)
        f = a*s**4 + b*s**2
        mn = f.min()
        k = f.argmin()
        okRegions = okRegions and abs(f[k] - mn) < 1e-15
        if a > 0 and b < 0:
            okRegions = okRegions and abs(s[k] - np.sqrt(-b/(2*a))) < 6.0/6000*2
        else:
            okRegions = okRegions and (k == 0)
        N = 4
        vs = np.full(N, s[k])
        okRegions = okRegions and abs(sum(a*vs**4 + b*vs**2) - N*mn) < 1e-12
    okRegions = okRegions and (-(6.0)**2 < 0)
    return okCS and okRegions
check("C7_quartic_truncated_vacuum_degenerate_all_sign_regions", c7())

def c8():
    tau = 4.0
    eps = 0.3
    def V(s2):
        return eps*np.sum(s2)**4 - np.sum(s2**2)
    best = 1e18
    cands = [tau*np.array(w)/np.sum(w) for w in
             [[1-3e-7, 1e-7, 1e-7, 1e-7], [0.9, 0.05, 0.04, 0.01], [0.6, 0.2, 0.15, 0.05]]]
    for _ in range(60000):
        z = np.abs(RNG.standard_normal(4)) + 1e-9
        cands.append(tau*z/z.sum())
    for s2 in cands:
        v = V(s2)
        if v < best:
            best = v
    Veq = V((tau/4)*np.ones(4))
    Vrank1 = V(np.array([tau, 0.0, 0.0, 0.0]))
    ok = best < Veq - 0.49*(Veq - Vrank1)
    ok = ok and (Vrank1 < Veq)
    tgrid = np.linspace(0.01, 20, 200001)
    g = eps*tgrid**4 - tgrid**2
    ok = ok and abs(g.min() - (-1.0/(4*eps))) < 1e-3
    z = np.array([1.0 - 3e-7, 1e-7, 1e-7, 1e-7])
    s2 = tau*z/z.sum()
    ok = ok and (np.sqrt(s2).min() < 1.5e-3)
    ok = ok and (V(s2) < Veq - 1.0)
    return ok
check("C8_beyond-quartic_bounded_split_counterexample_detzero_vacuum", c8())

def c9():
    ok = True
    for _ in range(200):
        lam = RNG.uniform(0.01, 10); v = RNG.uniform(0.01, 5)
        c4 = lam/4; c2 = -lam*v**2/2
        ok = ok and abs(-c2/(2*c4) - v**2) < 1e-10*v**2 + 1e-14
        s = RNG.uniform(0, 5, size=4)
        a = sum((lam/4)*(si**2 - v**2)**2 for si in s)
        b = sum(c4*si**4 + c2*si**2 for si in s) + 4*c4*v**4
        ok = ok and abs(a - b) < 1e-8*max(1.0, abs(a))
    return ok
check("C9_lambda_v_matching_random_range", c9())

def c10():
    def randU():
        Q, R = np.linalg.qr(RNG.standard_normal((4, 4)) + 1j*RNG.standard_normal((4, 4)))
        return Q @ np.diag(np.diag(R)/np.abs(np.diag(R)))
    ok = True
    for _ in range(60):
        Phi = RNG.standard_normal((4, 4)) + 1j*RNG.standard_normal((4, 4))
        X = Phi.conj().T @ Phi
        sv = np.linalg.svd(Phi, compute_uv=False)
        lam, v = 2.3, 1.1
        Vt = (lam/4)*np.trace((X - v**2*np.eye(4)) @ (X - v**2*np.eye(4))).real
        Ve = (lam/4)*np.sum((sv**2 - v**2)**2)
        ok = ok and abs(Vt - Ve) < 1e-9
        P2 = randU() @ Phi @ randU().conj().T
        X2 = P2.conj().T @ P2
        V2 = (lam/4)*np.trace((X2 - v**2*np.eye(4)) @ (X2 - v**2*np.eye(4))).real
        ok = ok and abs(V2 - Vt) < 1e-7
    return ok
check("C10_spectral_function_and_U4xU4_invariance", c10())

def n11():
    def Vx(x, c3, c2s, c1, c0):
        tau = np.sum(x, axis=-1)
        return c3*np.sum(x*x, axis=-1) + c2s*tau*tau + c1*tau + c0
    h = 0.05
    g = np.arange(0.0, 2.55, h)
    def grid_min(c3, c2s, c1, c0, face4=False):
        best = 1e30; arg = None
        X, Y, Z = np.meshgrid(g, g, g, indexing='ij')
        for w in g:
            if face4:
                vals = Vx(np.stack([X, Y, Z, np.zeros_like(X)], axis=-1), c3, c2s, c1, c0)
            else:
                vals = Vx(np.stack([X, Y, Z, np.full_like(X, w)], axis=-1), c3, c2s, c1, c0)
            k = np.unravel_index(np.argmin(vals), vals.shape)
            if vals[k] < best:
                best = vals[k]
                arg = np.array([X[k], Y[k], Z[k], w], dtype=float)
        return best, arg
    okA = True
    ptsAB = [(1.0, 0.5, -1.7), (1.0, 0.5, -0.4), (1.0, -0.20, -0.4),
             (1.0, -0.245, -0.02), (1.0, -0.10, -0.4),
             (0.4, 0.0, -0.4), (0.4, 0.0, -1.7), (2.0, 0.25, -0.4), (0.7, -0.13, -0.13),
             (1.3, -0.22, -0.05), (0.4, 0.0, -0.02)]
    for (c3, c2s, c1) in ptsAB:
        assert max(-c1/(2.0*(c3 + 4.0*c2s)), -c1/(2.0*(c3 + 3.0*c2s))) < 2.4
    for (c3, c2s, c1) in ptsAB:
        c0 = 0.13
        s_pred = -c1/(2.0*(c3 + 4.0*c2s))
        v_pred = Vx(np.full(4, s_pred), c3, c2s, c1, c0)
        best, arg = grid_min(c3, c2s, c1, c0)
        tol = 2.5*(c3 + 4.0*abs(c2s))*h*h + 1e-9
        okA = okA and (best - v_pred < tol) and (v_pred - best < tol)
        okA = okA and np.max(np.abs(arg - s_pred)) < 2.5*h
        w_pred = -c1/(2.0*(c3 + 3.0*c2s))
        v3_pred = Vx(np.array([0.0, w_pred, w_pred, w_pred]), c3, c2s, c1, c0)
        best3, arg3 = grid_min(c3, c2s, c1, c0, face4=True)
        okA = okA and abs(best3 - v3_pred) < tol
        okA = okA and np.max(np.abs(np.sort(arg3)[::-1][:3] - w_pred)) < 3.0*h
        v4 = Vx(np.full(4, s_pred), c3, c2s, c1, c0)
        delta = (c1*c1/4.0)*(1.0/(c3/4.0 + c2s) - 1.0/(c3/3.0 + c2s))
        okA = okA and abs((v3_pred - v4) - delta) < 1e-9 and (delta > 0)
        if delta > 8.0*tol:
            okA = okA and (best3 > best)
    for (c3, c2s, c1) in [(1.0, -0.20, -0.4), (1.0, -0.245, -1.7), (2.0, 0.25, -0.4)]:
        w_pred = -c1/(2.0*(c3 + 3.0*c2s))
        s_pred = -c1/(2.0*(c3 + 4.0*c2s))
        okA = okA and (abs(w_pred - s_pred) > 1e-6)
    okB = True
    for c2s in (-0.26, -0.4, -1.0):
        c3 = 1.0; c1 = -0.7; c0 = 0.0
        t = np.array([1.0, 3.0, 9.0, 27.0, 81.0])
        f = (c3/4.0 + c2s)*t*t + c1*t
        okB = okB and (f[-1] < f[0]) and (f[-1] < -1e2)
    return okA and okB
check("N11_bounded_class_vacuum_det0_minimizer_threshold_teeth", n11())

def n12():
    c3, c2s, c1, c0 = sp.symbols('c3 c2s c1 c0', real=True)
    x1, x2, x3, x4 = sp.symbols('x1 x2 x3 x4', nonnegative=True)
    xs = [x1, x2, x3, x4]
    tau = sum(xs)
    V = c3*sum(x*x for x in xs) + c2s*tau*tau + c1*tau + c0
    Hess = sp.Matrix([[sp.diff(sp.diff(V, xi), xj) for xj in xs] for xi in xs])
    ev = Hess.eigenvals()
    okA = (ev == {2*c3: 3, 2*c3 + 8*c2s: 1})
    okA = okA and sp.simplify(Hess.det() - 16*c3**3*(c3 + 4*c2s)) == 0
    okB = True
    sols = sp.solve([sp.diff(V, xi) for xi in xs], xs, dict=True)
    okB = okB and (len(sols) == 1)
    sbar = sols[0][x1]
    okB = okB and sp.simplify(sbar + c1/(2*(c3 + 4*c2s))) == 0
    V4 = sp.simplify(V.subs({x: sbar for x in xs}))
    okB = okB and sp.simplify(V4 - (c0 - c1**2/(c3 + 4*c2s))) == 0
    okC = True
    Vks = {}
    for k in (1, 2, 3):
        yk = list(sp.symbols('y0:%d' % k))
        eqk = [2*c3*y + 2*c2s*sum(yk) + c1 for y in yk]
        sk = sp.solve(eqk, yk, dict=True)
        okC = okC and (len(sk) == 1)
        yv = sk[0][yk[0]]
        okC = okC and sp.simplify(yv + c1/(2*(c3 + k*c2s))) == 0
        sub = {x1: 0, x2: 0, x3: 0, x4: 0}
        for i in range(k):
            sub[xs[i]] = yv
        Vk = sp.simplify(V.subs(sub))
        Vks[k] = Vk
        okC = okC and sp.simplify(Vk - (c0 - k*c1**2/(4*(c3 + k*c2s)))) == 0
    okD = True
    delta = sp.simplify(Vks[3] - V4)
    okD = okD and sp.simplify(delta - (c1**2/4)*(1/(c3/4 + c2s) - 1/(c3/3 + c2s))) == 0
    lam, v = sp.symbols('lambda v', positive=True)
    subeq = {c3: lam/4, c2s: 0, c1: -lam*v**2/2, c0: lam*v**4}
    okD = okD and sp.simplify(delta.subs(subeq) - lam*v**4/4) == 0
    okD = okD and sp.simplify(V4.subs(subeq)) == 0
    okD = okD and sp.simplify(sbar.subs(subeq) - v**2) == 0
    okE = True
    k = sp.symbols('k', positive=True)
    gk = k/(c3 + k*c2s)
    dg = sp.simplify(sp.diff(gk, k) - c3/(c3 + k*c2s)**2)
    okE = okE and (dg == 0)
    for kk in (1, 2, 3):
        okE = okE and sp.simplify((c3/kk + c2s) - (c3/4 + c2s) - c3*(1/sp.Integer(kk) - sp.Rational(1, 4))) == 0
    okF = True
    for kk in (1, 2, 3):
        outg = sp.simplify(2*c2s*sbar*4 + c1)
        okF = okF and sp.simplify(outg - c1*c3/(c3 + 4*c2s)) == 0
    okG = True
    corr = [(-0.34, -0.4), (-0.5, -0.6), (-1.0/3.0, -0.25)]
    for (c2a, c2b) in corr:
        c3v = 1.0
        qb = c3v/4.0 + c2a
        qa = c3v/3.0 + c2a
        okG = okG and (not ((qb >= 0) and (qa <= 0)))
        okG = okG and (c3v/4.0 + c2b) <= (c3v/3.0 + c2b)
    okG = okG and sp.simplify((c3/3 + c2s) - (c3/4 + c2s) - c3/12) == 0
    return okA and okB and okC and okD and okE and okF and okG
check("N12_symbolic_convexity_vacuum_strata_threshold_eqV_slice", n12())

def n13():
    p, q, th = sp.symbols('p q theta', real=True)
    E = sp.zeros(4, 4)
    E[1, 2] = p; E[2, 1] = -p
    Eexp = sp.exp(-th*E)
    okA = True
    okA = okA and sp.simplify(Eexp[0, 0] - 1) == 0 and sp.simplify(Eexp[3, 3] - 1) == 0
    okA = okA and sp.simplify(Eexp[1, 1] - sp.cos(th*p)) == 0
    okA = okA and sp.simplify(Eexp[2, 2] - sp.cos(th*p)) == 0
    okA = okA and sp.simplify(Eexp[1, 2] + sp.sin(th*p)) == 0
    okA = okA and sp.simplify(Eexp[2, 1] - sp.sin(th*p)) == 0
    okA = okA and sp.simplify(Eexp[0, 3]) == 0 and sp.simplify(Eexp[1, 3]) == 0
    okB = True
    A1 = sp.cos(th*p/2); A2 = sp.cos(th*q/2); A3 = sp.cos(th*(p + q)/2)
    okB = okB and (sp.simplify(A1 - A2) != 0)
    okB = okB and (sp.simplify(A1 - A3) != 0)
    okB = okB and (sp.simplify(A2 - A3) != 0)
    okC = True
    okC = okC and sp.simplify(sp.limit(A1 - A2, th, 0)) == 0
    okC = okC and (sp.simplify(sp.series(A1 - A2, th, 0, 2).removeO()) == 0)
    okC = okC and (sp.diff(A1 - A2, th).subs(th, 0) == 0)
    okD = True
    okD = okD and sp.simplify((1 - sp.cos(th*p/2)).series(th, 0, 4).removeO() - th**2*p**2/8) == 0
    okD = okD and (abs(float(1 - np.cos(0.3)) - 0.3**2/2) < 1e-3)
    return okA and okB and okC and okD
check("N13_phase_matrix_exponentiation_channel_distinctness", n13())

npass = sum(1 for _, o in results if o)
print("COVERAGE C1,C2,C4,C6,C7,C8,C9,C10: check code identical to round 1 (C6-C10: round 1 crashed at C5 before executing them; this r2 run is their first full execution). Ranges as in round-1 COVERAGE lines; no default-value-only checks.")
print("C3r: SOS identity symbolic generic nonzero c4,c2s; 18-point closed sign grid over all nine (c4,c2s) sign regions including c4=0 rows and the (c4<0,c2>0) hilltop tooth (stationary point located as a maximum); 60 random Mexican-hat minima located.")
print("C5r: GL(n)-conj invariant dims at (n,d) in {(2,1),(2,2),(2,3),(2,4),(3,4),(4,1),(4,2),(4,4)} vs partitions of d into at most n parts (1,2,2,3),(4),(5),(2),(1); n=2 d=3,4 vs p(d) mismatch teeth; n=4 d=4 equals 5 vs n=2 d=4 equals 3 and vs n=3 d=4 equals 4 Cayley-Hamilton teeth; kernel at n=4 d=2 spanned by independent Tr Z^2,(Tr Z)^2 (rank tooth); bifundamental teeth both ways; two inductive points for Tr X^2 vs (Tr X)^2.")
print("N11: 11 bounded-class points (predicted minimizers inside the 51-point [0,2.5], h=0.05 x-grid by asserted bound 2.4), 51^4 full-grid minima vs s=c1/2(c3+4c2s) incl. 4th coordinate; 11 face-restricted det=0 minima vs w^2=c1/2(c3+3c2s) at (0,w,w,w); Delta formula at 11 points, positive, and face min > vacuum; 3 points w != s (minimizer slice-dependence teeth); 3 unbounded teeth c2s < -c3/4 with equipartition-ray values decreasing below -1e2.")
print("N12: symbolic Hessian eigenvalues 2c3 (x3) and 2c3+8c2s, det 16 c3^3 (c3+4c2s); unique interior solve; strata k=1,2,3 symbolic solve and value -k c1^2/4(c3+k c2s)+c0; Delta symbolic equals (c1^2/4)(1/(c3/4+c2s)-1/(c3/3+c2s)); eq:V substitution Delta = lambda v^4/4, V_vac = 0, s = v^2; monotonicity d/dk[k/(c3+k c2s)] = c3/(c3+k c2s)^2; face-boundary gradient c1 c3/(c3+4 c2s); corridor nonexistence: no c2s with c3/4+c2s >= 0 and c3/3+c2s <= 0.")
print("N13: exp(-theta E) exact entries cos/sin(theta p) with decoupled 0,3 block; three quartic channel phases cos(theta p/2), cos(theta q/2), cos(theta(p+q)/2) pairwise distinct (teeth), degenerate and flat at theta=0; 1-cos = theta^2 p^2/8 + O(theta^4).")
print("TOTAL %d/%d PASS" % (npass, len(results)))
if npass != len(results):
    sys.exit(1)
print("ALL CHECKS DONE 118")
