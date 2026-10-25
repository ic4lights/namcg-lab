"""043 / s2: superpotentials of a stress linear in h on a flat background, and their boost charges.

(a) Classification. The most general symmetric tensor linear in a symmetric h_{mu nu}, with two
    derivatives and built with eta, is T = c1 box h + c2 (d_mu d.h_nu + d_nu d.h_mu) + c3 d_mu d_nu h
    + c4 eta box h + c5 eta dd.h.  Identical conservation (k^mu T_mu nu = 0 for all h, all k) leaves a
    two-dimensional space: the linearised Einstein tensor G1[h] and (d d - eta box) h.  On traceless h
    (and k.h-independent trace part dropped) the space is one-dimensional: proportional to G1[h].
(b) Single divergence. The most general Sigma_{rho mu nu} linear in d h, antisymmetric in (rho mu),
    whose divergence d^rho Sigma_{rho mu nu} is symmetric in (mu nu) for every h: its divergence again
    lies in span{G1[h], (dd - eta box) h}.
(c) Abbott-Deser form: G1[h]_{mu nu} = d^rho d^sigma K_{mu rho nu sigma}[h] with K having the
    symmetries of a curvature tensor (exact).
(d) Boost charge of a double divergence: for U with curvature-tensor symmetries and a Killing xi of
    eta (d d xi = 0), xi^nu d^rho d^sigma U_{mu rho nu sigma} = d^rho(W_{rho mu} - V_{rho mu}) with
    W, V antisymmetric, W = xi^nu d^sigma U_{mu rho nu sigma}, V_{rho mu} = d^a xi^b U_{mu a b rho}...
    checked as an exact polynomial identity; on Sigma (xi = 0) only V survives: the charge is the
    edge term d xi . U.  For the conformal Killing field of a diamond (d d xi != 0) a bulk remainder
    (d d xi) U survives (exact check that it is nonzero for a sample U).
Both signatures for (a)-(c); Lorentzian boost and Euclidean rotation for (d).
"""
import itertools
import random
import sympy as sp

random.seed(7)
allok = True
for sig, eta in [('Lorentzian', sp.diag(-1, 1, 1, 1)), ('Euclidean', sp.diag(1, 1, 1, 1))]:
    ei = eta.inv()
    k = sp.Matrix(sp.symbols('k0:4'))                 # covector k_mu
    kup = ei * k
    hs = sp.symbols('h0:10')
    idx = [(i, j) for i in range(4) for j in range(i, 4)]
    h = sp.zeros(4, 4)                                  # h_{mu nu} lower
    for s, (i, j) in zip(hs, idx):
        h[i, j] = s
        h[j, i] = s
    hup = ei * h * ei
    tr = sum(ei[i, j] * h[i, j] for i in range(4) for j in range(4))
    k2 = (k.T * kup)[0]
    kh = h * kup                                        # (k.h)_nu = k^rho h_{rho nu}
    khk = (kup.T * h * kup)[0]
    c = sp.symbols('c1:6')
    # Fourier: d -> i k ; overall factor -1 dropped (two derivatives)
    T = sp.Matrix(4, 4, lambda m, n: c[0] * k2 * h[m, n] + c[1] * (k[m] * kh[n] + k[n] * kh[m])
                  + c[2] * k[m] * k[n] * tr + c[3] * eta[m, n] * k2 * tr + c[4] * eta[m, n] * khk)
    div = (kup.T * T)                                   # k^mu T_{mu nu}
    eqs = []
    for n in range(4):
        p = sp.Poly(sp.expand(div[n]), *hs, *k)
        eqs += list(p.coeffs())
    sol = sp.solve(eqs, c, dict=True)
    free = set(c) - set(sol[0].keys())
    Tsol = T.subs(sol[0])
    basis = [sp.Matrix(4, 4, lambda m, n: sp.diff(Tsol[m, n], f)) for f in free]
    # linearised Einstein tensor (up to the sign of the Fourier factor): G1 = R1 - 1/2 eta R1
    # R1_{mn} = 1/2(k_r k_m h^r_n + k_r k_n h^r_m - k^2 h_mn - k_m k_n tr) (times -1 from i^2)
    R1 = sp.Matrix(4, 4, lambda m, n: sp.Rational(1, 2) * (k[m] * kh[n] + k[n] * kh[m] - k2 * h[m, n] - k[m] * k[n] * tr))
    Rs = sum(ei[i, j] * R1[i, j] for i in range(4) for j in range(4))
    G1 = (R1 - sp.Rational(1, 2) * eta * Rs).applyfunc(sp.expand)
    trterm = sp.Matrix(4, 4, lambda m, n: k[m] * k[n] * tr - eta[m, n] * k2 * tr)
    # check G1 and trterm lie in the solution space and span it
    def in_span(M, B):
        a = sp.symbols('a0:%d' % len(B))
        E = (M - sum((ai * Bi for ai, Bi in zip(a, B)), sp.zeros(4, 4))).applyfunc(sp.expand)
        eq = []
        for m in range(4):
            for n in range(4):
                eq += list(sp.Poly(E[m, n], *hs, *k).coeffs())
        s = sp.solve(eq, a, dict=True)
        return len(s) > 0
    ok_a = len(free) == 2 and in_span(G1, basis) and in_span(trterm, basis) and in_span(basis[0], [G1, trterm]) \
        and in_span(basis[1], [G1, trterm])
    # traceless h with k-independent: set tr = 0 -> only G1 (trterm vanishes)
    print(f"[{sig}] (a) identically conserved two-derivative tensors linear in h: dim = {len(free)}; "
          f"span = {{G1, (kk - eta k^2) tr h}}: {ok_a}")
    allok &= ok_a

    # (b) single divergence Sigma_{rho mu nu}, linear in k (one derivative) and h, antisym in rho mu
    struct = []
    for (r, m, n) in [(0, 0, 0)]:
        pass
    def S_basis():
        out = []
        # all rank-3 structures linear in k and h with eta
        out.append(lambda r, m, n: k[r] * h[m, n])
        out.append(lambda r, m, n: k[m] * h[r, n])
        out.append(lambda r, m, n: k[n] * h[r, m])
        out.append(lambda r, m, n: eta[r, m] * kh[n])
        out.append(lambda r, m, n: eta[r, n] * kh[m])
        out.append(lambda r, m, n: eta[m, n] * kh[r])
        out.append(lambda r, m, n: eta[r, m] * k[n] * tr)
        out.append(lambda r, m, n: eta[r, n] * k[m] * tr)
        out.append(lambda r, m, n: eta[m, n] * k[r] * tr)
        return out
    bs = S_basis()
    d = sp.symbols('d0:%d' % len(bs))
    Sig = [[[sum(d[i] * (bs[i](r, m, n) - bs[i](m, r, n)) for i in range(len(bs)))
             for n in range(4)] for m in range(4)] for r in range(4)]   # antisym in (r,m)
    D = sp.Matrix(4, 4, lambda m, n: sp.expand(sum(kup[r] * Sig[r][m][n] for r in range(4))))
    eqs = []
    for m in range(4):
        for n in range(4):
            eqs += list(sp.Poly(sp.expand(D[m, n] - D[n, m]), *hs, *k).coeffs())
    sold = sp.solve(eqs, d, dict=True)
    Dsol = D.subs(sold[0]).applyfunc(sp.expand)
    freed = sorted(set(d) - set(sold[0].keys()), key=lambda s: s.name)
    Db = [Dsol.applyfunc(lambda e: sp.diff(e, f)) for f in freed]
    # Sigma linear in k gives D quadratic in k: compare with G1 and trterm
    ok_b = all(in_span(M, [G1, trterm]) for M in Db if M != sp.zeros(4, 4))
    print(f"[{sig}] (b) single divergences with symmetric divergence: {len(freed)} free parameters; "
          f"every divergence in span{{G1, trace term}}: {ok_b}")
    allok &= ok_b

    # (c) Abbott-Deser: G1_{mn} = k^r k^s K_{m r n s} with
    # K_{mrns} = 1/2(eta_mn H_rs + eta_rs H_mn - eta_ms H_rn - eta_rn H_ms), H = h - 1/2 eta tr  (sign fixed by fit)
    Hm = h - sp.Rational(1, 2) * eta * tr
    K = lambda m, r, n, s: sp.Rational(1, 2) * (eta[m, n] * Hm[r, s] + eta[r, s] * Hm[m, n] - eta[m, s] * Hm[r, n] - eta[r, n] * Hm[m, s])
    lam = sp.symbols('lam')
    AD = sp.Matrix(4, 4, lambda m, n: sp.expand(sum(kup[r] * kup[s] * K(m, r, n, s) for r in range(4) for s in range(4))))
    diff_ = (G1 - lam * AD).applyfunc(sp.expand)
    eq = []
    for m in range(4):
        for n in range(4):
            eq += list(sp.Poly(diff_[m, n], *hs, *k).coeffs())
    sl = sp.solve(eq, lam, dict=True)
    symK = all(sp.expand(K(m, r, n, s) + K(r, m, n, s)) == 0 and sp.expand(K(m, r, n, s) - K(n, s, m, r)) == 0
               for m, r, n, s in itertools.product(range(4), repeat=4))
    print(f"[{sig}] (c) G1 = lambda * k^r k^s K_(m r n s) with curvature-symmetric K: lambda = {sl}, K symmetries: {symK}")
    allok &= len(sl) == 1 and symK

# (d) boost charge of a double divergence, position space, Lorentzian boost and Euclidean rotation
x = sp.symbols('x0:4')
for sig, eta, xi in [('Lorentzian boost', sp.diag(-1, 1, 1, 1), [x[1], x[0], 0, 0]),
                     ('Euclidean rotation', sp.diag(1, 1, 1, 1), [-x[1], x[0], 0, 0])]:
    ei = eta.inv()
    # generic U with curvature symmetries: U = Kulkarni-Nomizu of eta with a random polynomial symmetric s
    s = sp.zeros(4, 4)
    for i in range(4):
        for j in range(i, 4):
            p = sum(random.randint(-2, 2) * x[a] * x[b] for a in range(4) for b in range(a, 4)) + random.randint(-2, 2) * x[(i + j) % 4] ** 3
            s[i, j] = p
            s[j, i] = p
    # second piece: s (x) s' Kulkarni-Nomizu with another symmetric constant matrix
    t = sp.Matrix(4, 4, lambda i, j: random.randint(-2, 2) if i <= j else 0)
    t = t + t.T
    KN = lambda A, B, m, r, n, q: A[m, n] * B[r, q] + A[r, q] * B[m, n] - A[m, q] * B[r, n] - A[r, n] * B[m, q]
    U = lambda m, r, n, q: KN(eta, s, m, r, n, q) + KN(t, s, m, r, n, q)
    up = lambda e, a: sum(ei[a, b] * sp.diff(e, x[b]) for b in range(4))   # d^a
    xil = [sum(eta[a, b] * xi[b] for b in range(4)) for a in range(4)]       # xi_a
    # j_mu = xi^nu d^rho d^sigma U_{mu rho nu sigma}
    j = [sp.expand(sum(xi[n] * up(up(U(m, r, n, q), q), r) for r in range(4) for n in range(4) for q in range(4))) for m in range(4)]
    W = lambda r, m: sum(xi[n] * up(U(m, r, n, q), q) for n in range(4) for q in range(4))
    dxi = lambda a, b: up(xi[b], a)                   # d^a xi^b
    V = lambda q, m: sum(dxi(r, n) * U(m, r, n, q) for r in range(4) for n in range(4))
    F = lambda r, m: W(r, m) - V(r, m)
    antisymF = all(sp.expand(F(r, m) + F(m, r)) == 0 for r in range(4) for m in range(4))
    divF = [sp.expand(sum(up(F(r, m), r) for r in range(4))) for m in range(4)]
    ok_d = all(sp.expand(j[m] - divF[m]) == 0 for m in range(4)) and antisymF
    onS = {x[0]: 0, x[1]: 0}
    Wsig = [sp.expand(W(r, m).subs(onS)) for r in range(4) for m in range(4)]
    print(f"[{sig}] (d) xi.dd U = d(F), F antisymmetric: {ok_d}; W = 0 on Sigma: {all(w == 0 for w in Wsig)}; "
          f"edge term V^01 on Sigma nonzero: {sp.expand(V(0, 1).subs(onS)) != 0}")
    allok &= ok_d and all(w == 0 for w in Wsig)
    # conformal Killing field of a diamond (Lorentzian only): bulk remainder (dd xi) U nonzero
    if sig.startswith('Lorentzian'):
        l = sp.Rational(1)
        r2 = x[1] ** 2 + x[2] ** 2 + x[3] ** 2
        xic = [(l ** 2 - x[0] ** 2 - r2) / 2, -x[0] * x[1], -x[0] * x[2], -x[0] * x[3]]   # Jacobson's diamond field / (2 l)
        xicl = [sum(eta[a, b] * xic[b] for b in range(4)) for a in range(4)]
        dv = sum(sp.diff(xic[a], x[a]) for a in range(4))
        ckv = all(sp.expand(sp.diff(xicl[b], x[a]) + sp.diff(xicl[a], x[b]) - eta[a, b] * dv / 2) == 0
                  for a in range(4) for b in range(4))
        sgn = [(l ** 2 - x[0] ** 2 - r2) / 2, x[0] * x[1], x[0] * x[2], x[0] * x[3]]
        sgnl = [sum(eta[a, b] * sgn[b] for b in range(4)) for a in range(4)]
        dv2 = sum(sp.diff(sgn[a], x[a]) for a in range(4))
        ckv_plus = all(sp.expand(sp.diff(sgnl[b], x[a]) + sp.diff(sgnl[a], x[b]) - eta[a, b] * dv2 / 2) == 0
                       for a in range(4) for b in range(4))
        print(f"[diamond field] (l^2-t^2-r^2)/2 d_t - t x^i d_i is conformal Killing: {ckv}; "
              f"with +t x^i d_i instead: {ckv_plus}")
        allok &= ckv
        jc = [sp.expand(sum(xic[n] * up(up(U(m, r, n, q), q), r) for r in range(4) for n in range(4) for q in range(4))) for m in range(4)]
        Wc = lambda r, m: sum(xic[n] * up(U(m, r, n, q), q) for n in range(4) for q in range(4))
        Vc = lambda q, m: sum(up(xic[n], r) * U(m, r, n, q) for r in range(4) for n in range(4))
        rem = [sp.expand(jc[m] - sum(up(Wc(r, m) - Vc(r, m), r) for r in range(4))) for m in range(4)]
        print(f"[diamond conformal Killing field] bulk remainder (dd xi).U nonzero: {any(e != 0 for e in rem)}")
        allok &= any(e != 0 for e in rem)
print("ALL CHECKS PASSED" if allok else "SOME CHECK FAILED")
