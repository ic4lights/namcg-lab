# s2_moment_map.py - exact checks of the moment-map coordinate on the profile simplex:
# m_{2p} = 2^(2p+1) p! s^{2p} h_p(g); rho_p = 2^{p-1} m_{2p}/m_2^p = p! h_p(g)/W^p;
# triangular Girard inversion sigma from h; chamber Jacobian det; root reconstruction.
# Run: python -I proposals/092-g-profile-coordinate-transport/s2_moment_map.py
import sympy as sp
from sympy.matrices import Matrix

fails = []
def chk(name, cond):
    print(("OK  " if cond else "FAIL") + " " + name)
    if not cond:
        fails.append(name)

# ---- (1) E[T^p] = p! h_p(g) for T = sum of independent exponentials of means g_i, exact
def laplace_moment(g, p):
    u = sp.symbols('u', positive=True)
    # E[e^{-u T}] = prod g_i/(1+u g_i) ... Laplace of Exp(mean g) is 1/(1+u g); E[T^p]=(-1)^p d^p/du^p at 0
    L = sp.prod(1/(1 + u*gi) for gi in g)
    return sp.simplify(sp.factorial(p) * L.series(u, 0, p+1).removeO().diff(u, p).subs(u, 0) / sp.factorial(p) * (-1)**p * (-1)**p)
def h_complete(g, p):
    u = sp.symbols('u')
    ser = sp.prod(1/(1 - u*gi) for gi in g).series(u, 0, p+1).removeO()
    return sp.simplify(ser.diff(u, p).subs(u, 0)/sp.factorial(p))

for D in (2, 3):
    g = sp.symbols('g0:%d' % D, positive=True)
    for p in range(1, D+2):
        u = sp.symbols('u', positive=True)
        L = sp.prod(1/(1 + u*gi) for gi in g)
        mpt = sp.simplify(((-1)**p * L.diff(u, p)).subs(u, 0))
        chk("D=%d p=%d E[T^p] = %d! h_p" % (D, p, p), sp.simplify(mpt - sp.factorial(p)*h_complete(g, p)) == 0)

# ---- (2) rho extraction from charge moments is state-free: m_{2p}=2*4^p*p!*s2^{2p/2}... with
# slots var s^2 g_i: E_i mean s^2 g_i, m_{2p} = 2*4^p*E[T^p] = 2^{2p+1} p! s^{2p} h_p(g)
s2 = sp.symbols('sigma2', positive=True)
W = sp.symbols('W', positive=True)
D = 3
g = sp.symbols('g0:%d' % D, positive=True)
tot = sum(g)
for p in range(1, D+1):
    m2p = 2*4**p * sp.factorial(p) * s2**p * h_complete(g, p)
    m2 = 2*4*1*s2*sum(g)
    rho = sp.simplify(2**(p-1) * m2p / m2**p)
    chk("rho_%d = %d! h_%d/W^p from moment ratio" % (p, p, p),
        sp.simplify(rho - sp.factorial(p)*h_complete(g, p)/tot**p) == 0)

# ---- (3) Girard inversion: from hhat_p = rho_p/p! recover sigma_k = s_k(g/W) via
# k*hhat_k = sum_{i=1}^k sigma_i hhat_{k-i}; then Newton e_k; roots = g_i/W. Exact D=2,3, numeric D=4.
def hhat_from_sigma(sig, D, hh={}):
    # sig dict 1..D -> sigma_k (normalized, sigma_1=1); returns hhat 1..D
    hhat = {0: sp.Integer(1)}
    for k in range(1, D+1):
        hhat[k] = sp.simplify(sum(sig[i]*hhat[k-i] for i in range(1, k+1))/k)
    return hhat
for D in (2, 3):
    sig = {1: sp.Integer(1)}
    gs = sp.symbols('g0:%d' % D, positive=True)
    tot = sum(gs)
    for k in range(2, D+1):
        sig[k] = sp.summation(0, (sp.symbols('j'), 0, 0))  # placeholder, replaced below
        sig[k] = sum(gi**k for gi in gs)/tot**k
    hhat = hhat_from_sigma(sig, D)
    # forward check: hhat_k must equal h_k(g/W)
    for k in range(1, D+1):
        gw = [gi/tot for gi in gs]
        chk("D=%d recursion forward hhat_%d = h_%d(g/W)" % (D, k, k),
            sp.simplify(hhat[k] - h_complete(gw, k)) == 0)
    # inversion: sigma from hhat by sigma_k = k*hhat_k - sum_{i<k} sigma_i hhat_{k-i}
    sig2 = {}
    for k in range(1, D+1):
        sig2[k] = sp.simplify(k*hhat[k] - sum(sig2[i]*hhat[k-i] for i in range(1, k)))
    for k in range(1, D+1):
        chk("D=%d inversion sigma_%d" % (D, k), sp.simplify(sig2[k] - sig[k]) == 0)
    # Newton e_k from sigma; then polynomial roots equal g_i/tot as a multiset
    e = {0: sp.Integer(1)}
    for k in range(1, D+1):
        e[k] = sp.simplify(sum((-1)**(i-1)*e[k-i]*sig[i] for i in range(1, k+1))/k)
    t = sp.symbols('t')
    poly = sum((-1)**k*e[k]*t**(D-k) for k in range(D+1))
    poly = sp.expand(poly)
    roots = sorted([sp.nsimplify(r, rational=False) for r in sp.Poly(poly, t).all_roots()]) if False else None
    # numeric witness
    vals = [sp.Float(v, 20) for v in ([2, 5] if D == 2 else [1, 2, 5])]
    subs = {gs[i]: vals[i] for i in range(D)}
    tv = sum(vals)
    pnum = sp.lambdify(t, poly.subs(subs), "mpmath")
    import mpmath
    mpmath.mp.dps = 30
    f = lambda x: pnum(x)
    # find all roots via polyroots on coefficients
    coeffs = [poly.coeff(t, k).subs(subs) for k in range(D, -1, -1)]  # descending for polyroots
    cs = [float(c) for c in coeffs]
    rts = sorted(mpmath.polyroots(cs))
    want = sorted([v/tv for v in vals])
    err = max(abs(r - w) for r, w in zip(rts, want))
    chk("D=%d root reconstruction of g/W from rho-data (err<1e-12)" % D, err < 1e-12)

# ---- (4) chamber Jacobian: det d(sigma_2..sigma_D)/d(g_2..g_D) on the slice W=1, g0>g1>...
for D in (2, 3, 4):
    gs = sp.symbols('g0:%d' % D, positive=True)
    # slice: g_{D-1} = 1 - sum_{i<D-1} g_i ; sigma_k for k=2..D
    free = list(gs[:D-1])
    gfull = free + [1 - sum(free)]
    sig = [sum(gi**k for gi in gfull) for k in range(2, D+1)]
    Jm = Matrix(sig).jacobian(free)
    det = sp.simplify(Jm.det())
    V = sp.prod(gfull[i] - gfull[j] for i in range(D) for j in range(i+1, D))
    ratio = sp.simplify(det/V)
    print("   D=%d det/V = %s (V = prod_{i<j}(g_i-g_j) on the slice W=1)" % (D, ratio))
    chk("D=%d Jacobian det = const_D * Vandermonde (const independent of g)" % D,
        ratio.free_symbols == set())

# ---- (5) partition form of rho: rho_p = sum_{lambda|-p} (p!/z_lambda) prod (sigma_k)^{m_k}, sigma=s_k/W^k
import itertools
def partitions(n, mx=None):
    if mx is None: mx = n
    if n == 0:
        yield []
        return
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n-k, k):
            yield [k] + rest
for p in (2, 3, 4):
    gs = sp.symbols('g0:4', positive=True)
    tot = sum(gs)
    sig = {k: sum(gi**k for gi in gs)/tot**k for k in range(1, p+1)}
    rhs = 0
    for lam in partitions(p):
        mult = {}
        for part in lam:
            mult[part] = mult.get(part, 0) + 1
        z = 1
        for k, m in mult.items():
            z *= k**m * sp.factorial(m)
        rhs += sp.factorial(p)/z * sp.prod(sig[k]**m for k, m in mult.items())
    chk("partition form rho_%d" % p, sp.simplify(rhs - sp.factorial(p)*h_complete(gs, p)/tot**p) == 0)

print("S2:", "PASS" if not fails else "FAIL " + str(fails))
