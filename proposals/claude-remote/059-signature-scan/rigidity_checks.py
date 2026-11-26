#!/usr/bin/env python3
"""Package 059 checks: signature rigidity of real target contractions h0 in S_b.

Checks (each prints PASS/FAIL with the numbers it rests on):
 A  sympy: for real 2x2 symmetric r, s:  Im det(r + i s) = tr(adj(r) s)  (exact).
 B  S_b at N=2 equals c * sum_{a<b} [G_aa G_bb - G_ab^2], G_ab = h(x^a, x^b), h = L^T h0 L, with one
    positive constant c, for random complex L and h0 of every signature; S_b(-h0) = S_b(h0);
    an su(2) block in N=3 gives the same value; for real h, S_b is real at N=3 on general X.
 C  Rigidity lemma: for Re h = R nondegenerate with p>=2 positive and q>=2 negative eigenvalues and
    Im h = S != 0, the constructive plane of the proof has Im det(h|E) < 0.
 D  The lemma fails for q<=1 as it must: R_u (t=1) and e^{i theta} delta (t=0) satisfy the closed
    condition on sampled planes with S != 0 (they are in the damped set).
 E  Claim A: on random elements of C_0, Re h has >= 9 positive eigenvalues.
 F  Generalised inertia: h0 = diag(+1 x (10-t), -1 x t), Re(L^T L) positive definite ==> Re(L^T h0 L)
    has exactly t negative and 10-t positive eigenvalues.
 G  Witten comparison: diag(-(1 - i e), 1 + i e',...) is damped for e^{iS_b}; its complex conjugate has
    Im det < 0 on some plane (damps e^{-iS_b}); -h lies in -C_0 (>= 9 negative Re eigenvalues).
 H  Majorana-Weyl bookkeeping in d = 10 from Van Proeyen (3.25) and (3.28).
 I  Per-index phases: for 2<=t<=8, every small nonzero phase perturbation violates the closed condition.
"""
import numpy as np, sympy as sp, itertools
rng = np.random.default_rng(59059)
n = 10
ok_all = True
def report(name, ok, msg=""):
    global ok_all
    ok_all &= bool(ok)
    print(("PASS " if ok else "FAIL ") + name + (": " + msg if msg else ""))

# ---------- A
r11, r12, r22, s11, s12, s22 = sp.symbols('r11 r12 r22 s11 s12 s22', real=True)
r = sp.Matrix([[r11, r12], [r12, r22]]); s = sp.Matrix([[s11, s12], [s12, s22]])
lhs = sp.im(sp.expand((r + sp.I*s).det()))
rhs = (r.adjugate()*s).trace()
report("A Im det(r+is) = tr(adj(r)s)", sp.simplify(sp.expand(lhs - rhs)) == 0)

# ---------- B
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
def Sb(A, h0):
    # S_b = -(1/4) sum h0_{mu rho} h0_{nu sigma} Tr [A_mu,A_nu][A_rho,A_sigma]   (g_YM = 1)
    D = len(A)
    C = [[A[m] @ A[k] - A[k] @ A[m] for k in range(D)] for m in range(D)]
    tot = 0
    for m, k, rr, ss in itertools.product(range(D), repeat=4):
        c = h0[m, rr]*h0[k, ss]
        if c != 0:
            tot += c*np.trace(C[m][k] @ C[rr][ss])
    return -0.25*tot
def Sb_fast(A, h0):
    D = len(A)
    C = np.array([[A[m] @ A[k] - A[k] @ A[m] for k in range(D)] for m in range(D)])
    T = np.einsum('mkij,rsji->mkrs', C, C)
    return -0.25*np.einsum('mr,ks,mkrs->', h0, h0, T)
def minors(x, h):
    G = x.T @ h @ x   # x: 10 x 3 columns x^a
    return sum(G[a, a]*G[b, b] - G[a, b]**2 for a, b in [(0, 1), (0, 2), (1, 2)])
ratios = []; even_err = 0; n3_err = 0; real_err = 0
for t in range(0, 11):
    h0 = np.diag([1.0]*(n - t) + [-1.0]*t)
    for _ in range(3):
        L = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n))
        x = rng.normal(size=(n, 3))
        X = [sum(x[nu, a]*sig[a]/2 for a in range(3)) for nu in range(n)]
        A = [sum(L[mu, nu]*X[nu] for nu in range(n)) for mu in range(n)]
        val = Sb_fast(A, h0)
        h = L.T @ h0 @ L
        ratios.append(val/minors(x, h))
        even_err = max(even_err, abs(Sb_fast(A, -h0) - val)/abs(val))
        # N=3 su(2) block
        A3 = []
        for mu in range(n):
            M3 = np.zeros((3, 3), complex); M3[:2, :2] = A[mu]; A3.append(M3)
        n3_err = max(n3_err, abs(Sb_fast(A3, h0) - val)/abs(val))
    # real h at N=3, general traceless Hermitian X, real L
    Lr = rng.normal(size=(n, n))
    Xg = []
    for nu in range(n):
        Z = rng.normal(size=(3, 3)) + 1j*rng.normal(size=(3, 3)); Hm = (Z + Z.conj().T)/2
        Hm -= np.trace(Hm)/3*np.eye(3); Xg.append(Hm)
    Ag = [sum(Lr[mu, nu]*Xg[nu] for nu in range(n)) for mu in range(n)]
    v = Sb_fast(Ag, h0); real_err = max(real_err, abs(v.imag)/abs(v))
ratios = np.array(ratios)
check_slow = Sb(A, h0)  # one cross-check of the fast contraction against the explicit sum
report("B S_b = c*sum of 2-minors, one constant c>0", np.allclose(ratios, ratios[0], rtol=1e-9) and abs(ratios[0].imag) < 1e-12 and ratios[0].real > 0,
       "c = %.12f, spread %.1e" % (ratios[0].real, np.max(np.abs(ratios - ratios[0]))))
report("B fast contraction equals explicit sum", abs(check_slow - Sb_fast(A, h0)) < 1e-9*abs(check_slow))
report("B S_b(-h0) = S_b(h0)", even_err < 1e-10, "max rel err %.1e" % even_err)
report("B su(2) block at N=3 gives the N=2 value", n3_err < 1e-10, "max rel err %.1e" % n3_err)
report("B real h => S_b real at N=3 (general X)", real_err < 1e-12, "max |Im|/|S| %.1e" % real_err)

# ---------- C  constructive certificate of the rigidity lemma
def imdet_plane(h, a, b):
    return ((a @ h @ a)*(b @ h @ b) - (a @ h @ b)**2).imag
def certificate(R, S):
    w, V = np.linalg.eigh(R)
    B = V/np.sqrt(np.abs(w))           # B^T R B = diag(sign w)
    pos = np.where(w > 0)[0]; neg = np.where(w < 0)[0]
    Bp, Bm = B[:, pos], B[:, neg]
    Spp = Bp.T @ S @ Bp; Smm = Bm.T @ S @ Bm; Spm = Bp.T @ S @ Bm
    lam, U = np.linalg.eigh(Spp); mu, W = np.linalg.eigh(Smm)
    h = R + 1j*S
    tol = 1e-10*np.linalg.norm(S)
    if lam[0] + lam[1] < -tol:
        a, b = Bp @ U[:, 0], Bp @ U[:, 1]; case = 1
    elif mu[-1] + mu[-2] > tol:
        a, b = Bm @ W[:, -1], Bm @ W[:, -2]; case = 2
    elif lam[-1] > mu[0] + tol:
        a, b = Bp @ U[:, -1], Bm @ W[:, 0]; case = 3
    else:
        Uu, sv, Vv = np.linalg.svd(Spm)
        e1, f1 = Bp @ Uu[:, 0], Bm @ Vv[0, :]
        f2 = Bm @ Vv[1, :]
        best = None
        for aa in (0.3, -0.3):
            e = np.cosh(aa)*e1 + np.sinh(aa)*f1
            val = imdet_plane(h, e, f2)
            if best is None or val < best[0]:
                best = (val, e, f2)
        a, b = best[1], best[2]; case = 4
    return imdet_plane(h, a, b), case
worst = -np.inf; cases = {1: 0, 2: 0, 3: 0, 4: 0}; ntr = 0
for t in range(2, 9):
    for trial in range(400):
        Q = np.linalg.qr(rng.normal(size=(n, n)))[0]
        d = np.concatenate([rng.uniform(0.2, 3, n - t), -rng.uniform(0.2, 3, t)])
        R = Q.T @ np.diag(d) @ Q
        scale = 10.0**rng.uniform(-8, 1)
        S0 = rng.normal(size=(n, n)); S = scale*(S0 + S0.T)/2
        if trial % 4 == 0:   # adversarial: S vanishing on both definite blocks in the R-adapted basis
            w, V = np.linalg.eigh(R); B = V/np.sqrt(np.abs(w)); Binv = np.linalg.inv(B)
            pos = w > 0; Sb_ = np.zeros((n, n)); K = rng.normal(size=(pos.sum(), (~pos).sum()))*scale
            Sb_[np.ix_(pos, ~pos)] = K; Sb_[np.ix_(~pos, pos)] = K.T
            S = Binv.T @ Sb_ @ Binv
        if trial % 4 == 1:   # adversarial: S positive on V+ and negative on V- (tries to satisfy blocks)
            w, V = np.linalg.eigh(R); B = V/np.sqrt(np.abs(w)); Binv = np.linalg.inv(B)
            pos = w > 0; Sb_ = np.zeros((n, n))
            Sb_[np.ix_(pos, pos)] = scale*np.eye(pos.sum()); Sb_[np.ix_(~pos, ~pos)] = -scale*np.eye((~pos).sum())
            S = Binv.T @ Sb_ @ Binv
        val, c = certificate(R, S)
        cases[c] += 1; ntr += 1
        worst = max(worst, val/np.linalg.norm(S))
report("C rigidity certificate gives Im det < 0 for every S != 0 (t=2..8)", worst < 0,
       "%d trials, cases %s, max (Im det)/|S| = %.3e" % (ntr, cases, worst))

# ---------- D  q<=1: the closed condition admits S != 0
def min_imdet_sampled(h, m=20000):
    a = rng.normal(size=(m, n)); b = rng.normal(size=(m, n))
    a /= np.linalg.norm(a, axis=1)[:, None]; b /= np.linalg.norm(b, axis=1)[:, None]
    haa = np.einsum('ij,jk,ik->i', a, h, a); hbb = np.einsum('ij,jk,ik->i', b, h, b); hab = np.einsum('ij,jk,ik->i', a, h, b)
    return (haa*hbb - hab**2).imag.min()
u = 0.3
hRu = np.diag([-np.exp(-3j*np.pi*u/4)] + [np.exp(1j*np.pi*u/4)]*9)
hE = np.exp(0.2j)*np.eye(n)
mRu, mE = min_imdet_sampled(hRu), min_imdet_sampled(hE)
report("D t=1: R_u (u=0.3) satisfies the closed condition with Im h != 0", mRu > 0, "min sampled Im det = %.3e" % mRu)
report("D t=0: e^{0.2 i} delta satisfies it with Im h != 0", mE > 0, "min sampled Im det = %.3e" % mE)

# ---------- E  Claim A
cnt_ok = True; minpos = 10
for _ in range(2000):
    beta = rng.uniform(1e-3, np.pi/2 - 1e-3, n)
    if rng.random() < 0.5:   # one index may leave (0, pi/2) as allowed in C_0
        k = rng.integers(n); beta[k] = rng.uniform(-np.pi/2, np.pi)
        others = np.delete(beta, k)
        lo, hi = max(-others.min(), -np.pi/2) + 1e-3, min(np.pi - others.max(), np.pi) - 1e-3
        if lo >= hi: continue
        beta[k] = rng.uniform(lo, hi)
    T = rng.normal(size=(n, n)); dmod = rng.uniform(0.2, 3, n)
    h = T.T @ np.diag(dmod*np.exp(1j*beta)) @ T
    npos = int((np.linalg.eigvalsh(h.real) > 0).sum()); minpos = min(minpos, npos)
    if npos < 9: cnt_ok = False
report("E C_0 elements: Re h has >= 9 positive eigenvalues", cnt_ok, "minimum count %d" % minpos)

# ---------- F  generalised inertia
okF = True; tested = 0
for t in range(0, 11):
    h0 = np.diag([1.0]*(n - t) + [-1.0]*t)
    for _ in range(300):
        L = rng.normal(size=(n, n)) + 1j*rng.uniform(0, 1.5)*rng.normal(size=(n, n))
        M = L.T @ L
        if np.linalg.eigvalsh(M.real).min() <= 1e-9: continue
        tested += 1
        ev = np.linalg.eigvalsh((L.T @ h0 @ L).real)
        if not ((ev < 0).sum() == t and (ev > 0).sum() == n - t): okF = False
report("F Re M > 0 ==> Re h has the inertia (10-t, t) of h0", okF, "%d admissible contours over t=0..10" % tested)

# ---------- G  Witten comparison
e, ep = 0.2, 0.05
hF = np.diag([-(1 - 1j*e)] + [1 + 1j*ep]*9)
mF = min_imdet_sampled(hF); mC = min_imdet_sampled(hF.conj())
negs = int((np.linalg.eigvalsh((-hF).real) < 0).sum())
report("G -(1-i e) time entry: damped for e^{iS_b}", mF > 0, "min Im det %.3e" % mF)
report("G complex conjugate: Im det < 0 somewhere (damps e^{-iS_b} instead)", mC < 0, "min Im det %.3e" % mC)
report("G -h: Re(-h) has 9 negative eigenvalues (class -C_0, adjacent to -eta)", negs == 9)

# ---------- H  Majorana-Weyl bookkeeping, d=10 (Van Proeyen hep-th/9910030, Eqs. (3.25), (3.28))
maj = lambda st: st % 8 in (0, 1, 7, 2, 6)      # (3.25); 2 and 6 mod 8 with a sign choice of eta
chir = lambda st: st % 4 == 0                     # (3.28)
mw = [t for t in range(11) if maj((10 - t) - t) and chir((10 - t) - t)]
mod8 = [t for t in range(11) if ((10 - t) - t) % 8 == 0]
report("H MW in d=10 exactly for t in {1,5,9}, i.e. s-t = 0 mod 8", mw == [1, 5, 9] and mod8 == mw, "MW t = %s" % mw)
allowed_P1 = [0, 1, 9, 10]
report("H intersection with t in {0,1,9,10}", sorted(set(mw) & set(allowed_P1)) == [1, 9])

# ---------- I  per-index phases
okI = True
for t in range(2, 9):
    h0 = np.array([1.0]*(n - t) + [-1.0]*t)
    for _ in range(200):
        dbeta = rng.normal(size=n)*10.0**rng.uniform(-4, -1)
        h = np.diag(h0*np.exp(1j*dbeta))
        # closed condition on coordinate planes: Im(d_mu d_nu) >= 0 for all mu != nu
        dd = h0*np.exp(1j*dbeta)
        vals = [(dd[i]*dd[j]).imag for i in range(n) for j in range(i + 1, n)]
        if min(vals) >= 0: okI = False
report("I per-index phases: every small nonzero perturbation violates the closed condition (t=2..8)", okI)

print("ALL PASS" if ok_all else "SOME FAIL")
