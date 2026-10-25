"""Truncated second-order jets in four variables, exact rational arithmetic.

A field is a sympy Poly in h0..h3 over QQ, truncated at total degree 2
(degree kept = DEG).  Products are truncated; derivatives lower the
accuracy by one order, which is tracked by the caller (values of
first derivatives and second derivatives at h = 0 are exact as long as
the inputs are exact to degree 2).
"""
import itertools
import sympy as sp

H = sp.symbols('h0:4')
DEG = 2
N = 4


def P(expr):
    return trunc(sp.Poly(sp.expand(expr), *H, domain='QQ'))


def trunc(p, deg=DEG):
    d = {m: c for m, c in p.as_dict().items() if sum(m) <= deg}
    if not d:
        return sp.Poly(0, *H, domain='QQ')
    return sp.Poly.from_dict(d, *H, domain='QQ')


ZERO = sp.Poly(0, *H, domain='QQ')


def mul(a, b):
    return trunc(a * b)


def val(p):
    return p.coeff_monomial(1)


def d(p, i):
    return p.diff(H[i])


def mat(n=N, m=N):
    return [[ZERO for _ in range(m)] for _ in range(n)]


def mmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    C = mat(n, m)
    for i in range(n):
        for j in range(m):
            s = ZERO
            for l in range(k):
                s = s + A[i][l] * B[l][j]
            C[i][j] = trunc(s)
    return C


def mT(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def madd(A, B, sa=1, sb=1):
    return [[A[i][j] * sa + B[i][j] * sb for j in range(len(A[0]))] for i in range(len(A))]


def mconst(M):
    return [[sp.Poly(M[i, j], *H, domain='QQ') for j in range(M.shape[1])] for i in range(M.shape[0])]


def minv(A):
    """Series inverse to degree 2: A = A0 + Nn, A^-1 = B - B Nn B + B Nn B Nn B."""
    n = len(A)
    A0 = sp.Matrix(n, n, lambda i, j: val(A[i][j]))
    B = A0.inv()
    Bp = mconst(B)
    Nn = [[A[i][j] - sp.Poly(A0[i, j], *H, domain='QQ') for j in range(n)] for i in range(n)]
    BN = mmul(Bp, Nn)
    BNB = mmul(BN, Bp)
    BNBNB = mmul(BN, BNB)
    return [[trunc(Bp[i][j] - BNB[i][j] + BNBNB[i][j]) for j in range(n)] for i in range(n)]


def christoffel(g, gi):
    """Gamma[a][b][c] = 1/2 g^{ad}(d_b g_dc + d_c g_db - d_d g_bc); accurate to degree 1."""
    G = [[[ZERO] * N for _ in range(N)] for _ in range(N)]
    dg = [[[d(g[i][j], k) for k in range(N)] for j in range(N)] for i in range(N)]
    for a, b, c in itertools.product(range(N), repeat=3):
        s = ZERO
        for e in range(N):
            s = s + gi[a][e] * (dg[e][c][b] + dg[e][b][c] - dg[b][c][e])
        G[a][b][c] = trunc(s * sp.Rational(1, 2))
    return G


def riemann0(Gam):
    """R^a_{bcd} at h=0, convention R^a_{bcd} = d_c Gam^a_{db} - d_d Gam^a_{cb} + Gam^a_{ce}Gam^e_{db} - Gam^a_{de}Gam^e_{cb}."""
    R = [[[[0] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]
    G0 = [[[val(Gam[a][b][c]) for c in range(N)] for b in range(N)] for a in range(N)]
    for a, b, c, dd in itertools.product(range(N), repeat=4):
        s = val(d(Gam[a][dd][b], c)) - val(d(Gam[a][c][b], dd))
        for e in range(N):
            s += G0[a][c][e] * G0[e][dd][b] - G0[a][dd][e] * G0[e][c][b]
        R[a][b][c][dd] = s
    return R


def ricci_scalar0(g, gi):
    Gam = christoffel(g, gi)
    R = riemann0(Gam)
    gi0 = [[val(gi[i][j]) for j in range(N)] for i in range(N)]
    return sum(gi0[b][dd] * R[a][b][a][dd] for a in range(N) for b in range(N) for dd in range(N)), Gam


def torsion_package(gam, om):
    """Covariant torsion data of e^alpha_mu = gam^{alpha beta} om_{mu beta} with the gam connection.

    Returns dict of scalars at h=0: X, TTp, V2, calT, divV, R_G, R_W, and the Poly fields G, Gi.
    gam: metric (matrix of Polys), om: closed two-form (matrix of Polys), both exact to degree 2.
    """
    gi = minv(gam)
    E = mmul(gi, mT(om))                     # E[alpha][mu] = gam^{alpha beta} om_{mu beta}
    G = mmul(mmul(om, gi), mT(om))           # G_{mu nu} = om gam^{-1} om^T
    Gi = minv(G)
    Einv = minv(E)                           # Einv[mu][alpha]
    Gg = christoffel(gam, gi)
    # T^alpha_{mu nu}
    Ta = [[[ZERO] * N for _ in range(N)] for _ in range(N)]
    for al, mu, nu in itertools.product(range(N), repeat=3):
        s = d(E[al][nu], mu) - d(E[al][mu], nu)
        for be in range(N):
            s = s + Gg[al][mu][be] * E[be][nu] - Gg[al][nu][be] * E[be][mu]
        Ta[al][mu][nu] = trunc(s)
    # T^lam_{mu nu} (coordinate first index), T_{lam mu nu}
    Tl = [[[trunc(sum((Einv[la][al] * Ta[al][mu][nu] for al in range(N)), ZERO)) for nu in range(N)] for mu in range(N)] for la in range(N)]
    Tlow = [[[trunc(sum((G[la][ka] * Tl[ka][mu][nu] for ka in range(N)), ZERO)) for nu in range(N)] for mu in range(N)] for la in range(N)]
    # V_mu = G^{lam nu} T_{lam mu nu}
    Vl = [trunc(sum((Gi[la][nu] * Tlow[la][mu][nu] for la in range(N) for nu in range(N)), ZERO)) for mu in range(N)]
    Vu = [trunc(sum((Gi[mu][nu] * Vl[nu] for nu in range(N)), ZERO)) for mu in range(N)]
    # values at 0
    G0 = sp.Matrix(N, N, lambda i, j: val(G[i][j]))
    Gi0 = G0.inv()
    T0 = [[[val(Tlow[a][b][c]) for c in range(N)] for b in range(N)] for a in range(N)]
    Tup = [[[0] * N for _ in range(N)] for _ in range(N)]
    for a, b, c in itertools.product(range(N), repeat=3):
        Tup[a][b][c] = sum(Gi0[a, i] * Gi0[b, j] * Gi0[c, k] * T0[i][j][k]
                           for i in range(N) for j in range(N) for k in range(N))
    X = sum(T0[a][b][c] * Tup[a][b][c] for a in range(N) for b in range(N) for c in range(N))
    TTp = sum(T0[a][b][c] * Tup[b][a][c] for a in range(N) for b in range(N) for c in range(N))
    V0 = [val(v) for v in Vl]
    V2 = sum(Gi0[i, j] * V0[i] * V0[j] for i in range(N) for j in range(N))
    calT = sp.Rational(1, 4) * X + sp.Rational(1, 2) * TTp - V2
    RG, GamG = ricci_scalar0(G, Gi)
    divV = sum(val(d(Vu[m], m)) for m in range(N)) + sum(val(GamG[m][m][l]) * val(Vu[l]) for m in range(N) for l in range(N))
    # Weitzenboeck curvature scalar R_W = G^{sig nu} Einv[mu][al] Rgam^al_{be mu nu} E[be][sig]
    Rg = riemann0(Gg)
    E0 = sp.Matrix(N, N, lambda i, j: val(E[i][j]))
    Ei0 = E0.inv()
    RW = 0
    for sg, nu, mu, al, be in itertools.product(range(N), repeat=5):
        RW += Gi0[sg, nu] * Ei0[mu, al] * Rg[al][be][mu][nu] * E0[be, sg]
    return dict(X=X, TTp=TTp, V2=V2, calT=calT, divV=divV, R_G=RG, R_W=RW, G0=G0)
