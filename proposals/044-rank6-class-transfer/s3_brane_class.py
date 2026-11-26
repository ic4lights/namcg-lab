"""
s3_brane_class.py  (proposal 044)

D matrix coordinates, Poisson limit, four-dimensional symplectic leaf with constant theta in the chart y
(rho = 1/|Pf theta| constant), induced tensor g = dX.eta.dX, K = theta^T g theta, G = K^{-1}.

(i)  Algebra: with lam := sqrt|g| / rho and ghat := lam G one has  rho K = sqrt|ghat| ghat^{-1},
     1/rho = lam / sqrt|ghat|, |det ghat| = |det g|; hence the scalar operator
     -rho^{-1} d(rho K d .) equals -lam Lap_ghat  (exact rational / algebraic check, both signatures).
(ii) For O = -lam Lap_ghat on the metric G = ghat/lam, the Laplace-type data (Vassilevich convention
     O = -(g d d + a d + b), E_V) satisfy  sqrt|G| (R_G/6 + E_V) = (1/6) (sqrt|ghat|/lam) R[ghat]  pointwise,
     i.e. the scalar a_1 density is (1/6) rho R[ghat]  (symbolic check on a non-diagonal polynomial metric
     at a random point, Euclidean).
(iii) Rank of the linearised Einstein operator of ghat on the first-order image of delta x^I (frozen II,
     generic p), D = 4..11, Lorentzian g; and the Hamiltonian gauge direction is a linearised diffeomorphism
     of ghat.  (Adapted from proposals/009-matrix-coords-N8/check_brane_rank.py.)
(iv) Bending term: X_D = g^{rho lam} d_rho Theta^{IJ} d_lam Theta_{IJ}, Theta^{IJ} = theta^{mu nu} d_mu X^I d_nu X^J,
     about x^a = y^a, x^i = (1/2) II^i_{mu nu} y^mu y^nu (Euclidean target, D = 7), perturbed by
     delta X^i = eps phi_i cos(L p.y + alpha): the eps^2 coefficient at y = 0, averaged over alpha in {0, pi/2},
     is a polynomial in L whose L^4 coefficient is (p.p)(p.K.p)|phi|^2 (frozen-coefficient leading symbol).
"""
import sympy as sp, random
random.seed(7)
R = lambda: sp.Rational(random.randint(-5, 5), random.randint(1, 3))
out = []
def P(*a):
    line = " ".join(str(x) for x in a); print(line); out.append(line)

def rand_theta():
    while True:
        t = [R() for _ in range(6)]
        T = sp.Matrix([[0, t[0], t[1], t[2]], [-t[0], 0, t[3], t[4]], [-t[1], -t[3], 0, t[5]], [-t[2], -t[4], -t[5], 0]])
        if T.det() != 0: return T

def pf(T): return T[0, 1] * T[2, 3] - T[0, 2] * T[1, 3] + T[0, 3] * T[1, 2]

# ---------------- (i)
P("=== (i) algebraic identities for ghat = (sqrt|g|/rho) G ===")
for sig, eta in (("Euclidean", sp.eye(4)), ("Lorentzian", sp.diag(-1, 1, 1, 1))):
    for trial in range(3):
        th = rand_theta()
        while True:
            A = sp.Matrix(4, 4, lambda i, j: R())
            if A.det() != 0: break
        g = A.T * eta * A
        rho = 1 / abs(pf(th))
        K = th.T * g * th; G = K.inv()
        lam = sp.sqrt(abs(g.det())) / rho
        gh = lam * G
        sq = sp.sqrt(abs(gh.det()))
        c1 = sp.simplify(rho * K - sq * gh.inv()) == sp.zeros(4, 4)
        c2 = sp.simplify(1 / rho - lam / sq) == 0
        c3 = sp.simplify(abs(gh.det()) - abs(g.det())) == 0
        P(f"{sig} trial {trial}: rho K = sqrt|ghat| ghat^-1: {c1};  1/rho = lam/sqrt|ghat|: {c2};  |det ghat| = |det g|: {c3}")

# ---------------- (ii)
P("")
P("=== (ii) scalar a_1 density of O = -lam Lap_ghat on G = ghat/lam (jets to second order at y = 0) ===")
y = sp.symbols('y0:4')
def trunc(e, n=2):
    e = sp.expand(e)
    if e == 0: return e
    pol = sp.Poly(e, *y)
    return sum(c * sp.prod([y[i]**k for i, k in enumerate(m)]) for m, c in pol.terms() if sum(m) <= n)
def tmul(a, b): return trunc(a * b)
def tmat_mul(A, B): return sp.Matrix(A.shape[0], B.shape[1], lambda i, j: trunc(sum(A[i, k] * B[k, j] for k in range(A.shape[1]))))
def deg_part(e, d):
    e = sp.expand(e)
    if e == 0: return e
    pol = sp.Poly(e, *y)
    return sum(c * sp.prod([y[i]**k for i, k in enumerate(m)]) for m, c in pol.terms() if sum(m) == d)
def tinv(M):
    M0 = M.applyfunc(lambda e: deg_part(e, 0)); M1 = M.applyfunc(lambda e: deg_part(e, 1)); M2 = M.applyfunc(lambda e: deg_part(e, 2))
    A = M0.inv()
    return (A - A * M1 * A + A * M1 * A * M1 * A - A * M2 * A).applyfunc(trunc)
def tinv_scalar(f):
    f0 = deg_part(f, 0); x = trunc((f - f0) / f0)
    return trunc((1 - x + x * x) / f0)
def tsqrt(f):  # f(0) = 1 assumed
    x = trunc(f - 1)
    return trunc(1 + x / 2 - x * x / 8)
def rnd_lin_quad(a, b):
    return sum(R() * y[i] for i in range(4)) / a + sum(R() * y[i] * y[j] for i in range(4) for j in range(i, 4)) / b
gh = sp.zeros(4, 4)
for i in range(4):
    for j in range(i, 4):
        v = (1 if i == j else 0) + rnd_lin_quad(4, 5)
        gh[i, j] = v; gh[j, i] = v
lam = 1 + rnd_lin_quad(3, 4)
ilam = tinv_scalar(lam)
G = gh.applyfunc(lambda e: tmul(e, ilam))
def christoffel(gm):
    gi = tinv(gm)
    return [[[trunc(sum(gi[a, d] * (sp.diff(gm[d, b], y[c]) + sp.diff(gm[d, c], y[b]) - sp.diff(gm[b, c], y[d])) for d in range(4)) / 2, 1)
              for c in range(4)] for b in range(4)] for a in range(4)], gi
def ricci_scalar0(gm):
    Gam, gi = christoffel(gm)
    Rs = 0
    for b in range(4):
        for c in range(4):
            r = 0
            for a in range(4):
                r += sp.diff(Gam[a][b][c], y[a]) - sp.diff(Gam[a][b][a], y[c])
                for d in range(4):
                    r += Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a]
            Rs += gi[b, c] * r
    return sp.expand(Rs).subs({yy: 0 for yy in y})
ghi = tinv(gh)
sqgh = tsqrt(trunc(gh.det()))
Gi = ghi.applyfunc(lambda e: tmul(e, lam))
avec = [trunc(tmul(tmul(lam, tinv_scalar(sqgh)), sum(sp.diff(tmul(sqgh, ghi[m, n]), y[m]) for m in range(4))), 1) for n in range(4)]
GamG, _ = christoffel(G)
omega = [trunc(sp.Rational(1, 2) * sum(G[n, d] * (avec[n] + sum(Gi[m, s_] * GamG[n][m][s_] for m in range(4) for s_ in range(4))) for n in range(4)), 1) for d in range(4)]
EV0 = (-sum(Gi[n, m] * (sp.diff(omega[n], y[m]) + omega[n] * omega[m] - sum(omega[s_] * GamG[s_][n][m] for s_ in range(4))) for n in range(4) for m in range(4))).subs({yy: 0 for yy in y})
sqG0 = sp.sqrt(G.det().subs({yy: 0 for yy in y}))
lhs = sp.nsimplify(sqG0 * (ricci_scalar0(G) / 6 + EV0))
rhs = sp.nsimplify(sqgh.subs({yy: 0 for yy in y}) / lam.subs({yy: 0 for yy in y}) * ricci_scalar0(gh) / 6)
P(f"sqrt|G|(R_G/6 + E_V) at y=0  = {lhs}")
P(f"(1/6)(sqrt|ghat|/lam) R[ghat] = {rhs}")
P(f"difference = {sp.simplify(lhs - rhs)}")

# ---------------- (iii)
P("")
P("=== (iii) rank of the linearised Einstein operator of ghat on the first-order image (Lorentzian, frozen II) ===")
eta = sp.diag(-1, 1, 1, 1)
def rand_g():
    while True:
        A = sp.Matrix(4, 4, lambda i, j: R())
        if A.det() != 0: return A.T * eta * A
def rand_sym():
    S = sp.zeros(4, 4)
    for i in range(4):
        for j in range(i, 4): S[i, j] = S[j, i] = R()
    return S
idx = [(i, j) for i in range(4) for j in range(i, 4)]
vec = lambda h: [h[i, j] for (i, j) in idx]
odot = lambda a, b: a * b.T + b * a.T
def lin_einstein(h, gb, p):
    gi = gb.inv(); hu = gi * h; tr = hu.trace(); pu = gi * p; p2 = (p.T * pu)[0]; ph = h * pu; pph = (pu.T * h * pu)[0]
    Ric = sp.Matrix(4, 4, lambda a, b: sp.Rational(1, 2) * (-ph[b] * p[a] - ph[a] * p[b] + p2 * h[a, b] + p[a] * p[b] * tr))
    return Ric - sp.Rational(1, 2) * gb * (-pph + p2 * tr)
P("D | Hamiltonian gauge = diffeo of ghat | rank(Im) | rank E[ghat] on Im (max 6)")
for D in range(4, 12):
    th = rand_theta(); g = rand_g(); p = sp.Matrix([R() for _ in range(4)])
    K = th.T * g * th; G = K.inv(); gi = g.inv()
    lam0 = 1  # overall constant factor of ghat does not change ranks; delta ln lam = (1/2) tr(g^-1 delta g)
    IIs = [rand_sym() for _ in range(D - 4)]
    def dghat(dg):
        dG = -G * (th.T * dg * th) * G
        return dG + sp.Rational(1, 2) * (gi * dg).trace() * G
    modes = []
    for k_ in range(4):
        xi = sp.zeros(4, 1); xi[k_] = 1
        modes.append(dghat(odot(p, g * xi)))
    for S in IIs: modes.append(dghat(-2 * S))
    xiH = th.T * p
    gauge_ok = dghat(odot(p, g * xiH)) == odot(p, G * xiH)
    Im = [vec(m) for m in modes]
    rkIm = sp.Matrix(Im).rank()
    rkE = sp.Matrix([vec(lin_einstein(m, G, p)) for m in modes]).rank()
    P(f"{D:2d} | {gauge_ok} | {rkIm} | {rkE}")

# ---------------- (iv)
P("")
P("=== (iv) bending term of X_D on transverse plane waves (D = 7, Euclidean target) ===")
eps, L = sp.symbols('eps L')
th = rand_theta()
IIs = [rand_sym() for _ in range(3)]
p = sp.Matrix([R() for _ in range(4)])
phi = [R() for _ in range(3)]
K = th.T * th
def XD_at0(alpha):
    ph = L * sum(p[m] * y[m] for m in range(4)) + alpha
    Xs = [y[a] for a in range(4)] + [sp.Rational(1, 2) * sum(IIs[i][m, n] * y[m] * y[n] for m in range(4) for n in range(4)) + eps * phi[i] * sp.cos(ph) for i in range(3)]
    dX = [[sp.diff(Xs[I], y[m]) for m in range(4)] for I in range(7)]
    Th = [[sum(th[m, n] * dX[I][m] * dX[J][n] for m in range(4) for n in range(4)) for J in range(7)] for I in range(7)]
    g = sp.Matrix(4, 4, lambda m, n: sum(dX[I][m] * dX[I][n] for I in range(7)))
    gi0 = g.subs({yy: 0 for yy in y})
    gi0 = gi0.inv()
    dTh = [[[sp.diff(Th[I][J], y[r]).subs({yy: 0 for yy in y}) for r in range(4)] for J in range(7)] for I in range(7)]
    XD = sum(gi0[r, s] * dTh[I][J][r] * dTh[I][J][s] for I in range(7) for J in range(7) for r in range(4) for s in range(4))
    return sp.expand(sp.series(XD, eps, 0, 3).removeO())
X2 = sp.expand((XD_at0(0).coeff(eps, 2) + XD_at0(sp.pi / 2).coeff(eps, 2)) / 2)
X2 = sp.simplify(X2)
polyL = sp.Poly(sp.expand(X2), L)
pp = (p.T * p)[0]; pKp = (p.T * K * p)[0]; phi2 = sum(f * f for f in phi)
P(f"eps^2 coefficient (alpha-averaged) as a polynomial in L: degree {polyL.degree()}")
for k_ in range(polyL.degree() + 1):
    P(f"   L^{k_}: {sp.nsimplify(polyL.coeff_monomial(L**k_))}")
P(f"(p.p)(p.K.p)|phi|^2 = {sp.nsimplify(pp * pKp * phi2)}   -> L^4 coefficient matches: {sp.simplify(polyL.coeff_monomial(L**4) - pp * pKp * phi2) == 0}")

open(__file__.replace('.py', '.out.txt'), 'w').write("\n".join(out) + "\n")
