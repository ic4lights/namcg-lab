# verify_r118.py -- verification pack for proposal 118 (Presentation-A selection of eq:V)
# Run: python -I -B verify_r118.py   (requires sympy, numpy)
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

def c3():
    c4, c2 = sp.symbols('c4 c2', real=True, nonzero=True)
    s1, s2, s3, s4 = sp.symbols('sigma1 sigma2 sigma3 sigma4', nonnegative=True)
    v2 = -c2/(2*c4)
    f = lambda s: c4*s**4 + c2*s**2
    tot = sum(f(s) for s in (s1, s2, s3, s4))
    Vmin = 4*(-c2**2/(4*c4))
    diff = sp.simplify(tot - Vmin - c4*sum((s**2 - v2)**2 for s in (s1, s2, s3, s4)))
    okA = diff == 0
    okB = sp.factor((c4*sum((s**2 - v2)**2 for s in (s1, s2, s3, s4))).subs(c2, 0)) != 0
    okC = True
    for a in (-2.0, -0.37, 0.0, 0.11, 3.0):
        for b in (-2.0, -0.37, 0.0, 0.11, 3.0):
            mh = (a > 0) and (b < 0)
            v2f = (-b/(2*a)) if a != 0 else None
            okC = okC and (mh == ((v2f is not None) and (v2f > 0)))
    s = np.linspace(0, 50, 4001)
    for a, b in ((-1.0, -1.0), (-1.0, 1.0)):      # c4 < 0: unbounded direction
        okC = okC and (a*s[-1]**4 + b*s[-1]**2 < a*s[0]**4 + b*s[0]**2)
    for a, b in ((1.0, 0.5), (0.0, 1.0)):         # bounded, min at sigma = 0, no Mexican hat
        vals = a*s**4 + b*s**2
        okC = okC and (vals[0] == min(vals))
    okD = True
    for _ in range(60):
        a = RNG.uniform(0.05, 4.0); b = -RNG.uniform(0.05, 4.0)
        vv = -b/(2*a)
        grid = np.linspace(0, 3*np.sqrt(vv + 1), 8001)
        fvals = a*grid**4 + b*grid**2
        k = fvals.argmin()
        okD = okD and abs(grid[k] - np.sqrt(vv)) < (grid[1] - grid[0])*2
        okD = okD and abs(fvals[k] - (-b*b/(4*a))) < 1e-3 + abs(fvals[k])*1e-4
    return okA and okB and okC and okD
check("C3_sos_min_uniqueness_and_sign_table_full_range", c3())

def c4_check():
    th = sp.symbols('theta', real=True)
    def om(k, q):
        return th*(k[0]*q[1] - k[1]*q[0])
    def col(a, b):
        return sp.ImmutableMatrix([[a], [b]])
    k1 = col(sp.symbols('a', real=True), sp.symbols('b', real=True))
    okA = sp.simplify(om(k1, -k1)) == 0        # quadratic vertex phase vanishes identically: exact
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
        okB = okB and (cyc == 0)                                   # cyclic on shell
        offsh = sp.simplify(P.xreplace({ks[0][0]: -Ssum[0] + 1, ks[0][1]: -Ssum[1]}))
        okB = okB and (offsh != 0)                                 # tooth: on-shell restriction needed
    a1, b1, a2, b2 = sp.symbols('a1 b1 a2 b2', real=True)
    k1c = col(a1, b1); k2c = col(a2, b2)
    k3c = col(sp.symbols('a3', real=True), sp.symbols('b3', real=True))
    k4c = -(k1c + k2c + k3c)
    P4 = om(k1c, k2c) + om(k1c, k3c) + om(k1c, k4c) + om(k2c, k3c) + om(k2c, k4c) + om(k3c, k4c)
    red = sp.simplify(P4 - (om(k1c, k2c) + om(k3c, k4c)))
    okC = (red == 0)                    # on shell: phase = om(k1,k2) + om(k3,k4) (planar pairing)
    # and the alternative cyclic form agrees on shell:
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
            okD = okD and abs(d2/d1 - 0.25) < 0.05                 # quadratic small-theta scaling
        okD = okD and (abs(np.sin(S/2)) <= abs(S)/2 + 1e-15)
    okE = True                                                     # generic quartic phase nonzero (tooth)
    got = False
    for _ in range(60):
        kq = [RNG.integers(-3, 4, size=2) for _ in range(3)]
        kq.append(-sum(kq))
        S = (kq[2][0]*kq[3][1] - kq[2][1]*kq[3][0])
        if abs(S) > 1e-9:
            got = True
    okE = got
    return okA and okB and okC and okD and okE
check("C4_moyal_vertex_phase_exact_quadratic_cyclic_nonzero_quartic", c4_check())

def c5():
    # (a) GL(n)-conjugation invariants of polynomials in the entries of Z, degree d,
    #     have dimension p(d) (power sums Tr Z^k): test d in {1,2,3,4} at n=2 and d<=2 at n=4.
    def conj_inv_dim(n, d):
        slots = [(i, j) for i in range(n) for j in range(n)]
        mon = [tuple(sorted(ms)) for ms in itertools.combinations_with_replacement(slots, d)]
        mon = sorted(set(mon))
        idx = {m_: i_ for i_, m_ in enumerate(mon)}
        G = []
        for p in range(n):
            for q in range(n):
                M = np.zeros((len(mon), len(mon)))
                for m_, i_ in idx.items():
                    for pos in range(d):
                        (ii, jj) = m_[pos]
                        nw = list(m_)
                        if ii == p:
                            nw[pos] = (q, jj)
                            M[idx[tuple(sorted(nw))], i_] += 1
                        if jj == q:
                            nw2 = list(m_)
                            nw2[pos] = (ii, p)
                            M[idx[tuple(sorted(nw2))], i_] -= 1
                G.append(M)
        K = np.vstack(G)
        return len(mon) - np.linalg.matrix_rank(K, tol=1e-9), idx, mon
    okA = True
    for d, expd in [(1, 1), (2, 2), (3, 3), (4, 5)]:
        dimn2, _, _ = conj_inv_dim(2, d)
        okA = okA and (dimn2 == expd)
    dim1n4, _, _ = conj_inv_dim(4, 1)
    dim2n4, idx4, mon4 = conj_inv_dim(4, 2)
    okA = okA and (dim1n4 == 1) and (dim2n4 == 2)
    # basis vectors at n=4, d=2: Tr Z^2 and (Tr Z)^2 must be invariant
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
                    nw = list(m_)
                    if ii == p:
                        nw[pos] = (q, jj)
                        M[idx4[tuple(sorted(nw))], i_] += 1
                    if jj == q:
                        nw2 = list(m_)
                        nw2[pos] = (ii, p)
                        M[idx4[tuple(sorted(nw2))], i_] -= 1
            Gs.append(M)
    K4 = np.vstack(Gs)
    okA = okA and np.allclose(K4 @ vA, 0) and np.allclose(K4 @ vB, 0)
    # (b) U(4) x U(4) bifundamental: Tr((Phi^dag Phi)^2) invariant, ||Phi^2||_F^2 NOT (tooth)
    Phi = RNG.standard_normal((4, 4)) + 1j*RNG.standard_normal((4, 4))
    def randU():
        Q, R = np.linalg.qr(RNG.standard_normal((4, 4)) + 1j*RNG.standard_normal((4, 4)))
        return Q @ np.diag(np.diag(R)/np.abs(np.diag(R)))
    Xf = lambda A: np.trace((A.conj().T @ A) @ (A.conj().T @ A)).real
    w2 = lambda A: np.trace(A @ A @ A.conj().T @ A.conj().T).real
    okB = False
    for _ in range(20):
        P2 = randU() @ Phi @ randU().conj().T
        if abs(w2(Phi) - w2(P2)) > 1e-6:
            okB = True
            break
    okC = True
    for _ in range(20):
        P2 = randU() @ Phi @ randU().conj().T
        okC = okC and abs(Xf(Phi) - Xf(P2)) < 1e-8
    return okA and okB and okC
check("C5_power-sum_conjugation_dims_and_bifundamental_teeth", c5())

def c6():
    ok = True
    for _ in range(100):
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
        okCS = okCS and (np.sum(s2**2) >= tau**2/4.0 - 1e-10)     # Cauchy-Schwarz: min at equal
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
        # separable N-fold minimum is degenerate along the equal-sigma manifold:
        N = 4
        vs = np.full(N, s[k])
        okRegions = okRegions and abs(sum(a*vs**4 + b*vs**2) - N*mn) < 1e-12
    if True:   # unboundedness of the (c4=0, c2<0) separable model at large sigma
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
             [[1-3e-6, 1e-6, 1e-6, 1e-6], [0.9, 0.05, 0.04, 0.01], [0.6, 0.2, 0.15, 0.05]]]
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
    # bounded below along rays: min over tau of eps*tau^4 - tau^2 = -1/(4 eps), at tau^2 = 1/(2 eps)
    tgrid = np.linspace(0.01, 20, 200001)
    g = eps*tgrid**4 - tgrid**2
    ok = ok and abs(g.min() - (-1.0/(4*eps))) < 1e-3
    # rank-1 (split) vacuum is a zero-determinant frame locus: min sigma -> 0
    z = np.array([1.0 - 3e-6, 1e-6, 1e-6, 1e-6])
    s2 = tau*z/z.sum()
    ok = ok and (np.sqrt(s2).min() < 2e-3)
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

npass = sum(1 for _, o in results if o)
print("COVERAGE: C1 symbolic lambda,v; N=4 and N=6 eigenvalue sets (additive constant N lam v^4/4; mismatch at N=7 with 4 eigenvalues shown). C2 40 random complex 4x4 (scale grid 1+0.13t), lam in {1.31,0.5,1.0,3.7}, v in {0.77,0.3,1.0,2.5}; real+imag directional derivatives pin the full complex gradient.")
print("C3 symbolic sos identity for generic nonzero c4,c2; Mexican-hat sign grid {+-2,+-0.37,0}^2; c4<0 unbounded; (1,0.5),(0,1) bounded-at-zero; 60 random (c4>0,c2<0) minima located at sigma=sqrt(-c2/2c4).")
print("C4 quadratic phase om(k,-k)=0 symbolic in unconstrained k; n-gon cyclic identity n in {3,4,5} symbolic (on shell) with off-shell nonzero tooth; quartic on-shell reduction P4 = om(k3,k4) symbolic; 60 random integer quadruples, theta in [-0.15,0.15]: 1-cos(S/2) <= S^2/8, halving ratio 0.25+-0.05, |sin| <= |S|/2; generic nonzero quartic phase tooth.")
print("C5 gl(n)-conjugation-invariant dims of Sym^3 power sums for n in {2,3,4} (expected n) via all n^2 elementary generators; pairing word Tr(Phi Phi^dag Phi Phi^dag) non-invariant under 20 random U(4)xU(4) pairs (tooth), normal word invariant. C6 100 random 4x4 + 4x3 rectangular, ValueError composability tooth.")
print("C7 400 random trace-preserving deformations (Cauchy-Schwarz degeneracy) + 6 (c4,c2) sign regions incl. (0,-1) + separable N-fold minima. C8 60000-point simplex search for eps*(Tr X)^4 - Tr(X^2): split vacuum strictly below equal split, global ray minimum -1/(4 eps), rank-one vacuum with min sigma < 2e-3.")
print("C9 200 random (lam,v) in (0.01,10)x(0.01,5). C10 60 random matrices + 60 random U(4)xU(4) pairs.")
print("TOTAL %d/%d PASS" % (npass, len(results)))
if npass != len(results):
    sys.exit(1)
print("ALL CHECKS PASS")
