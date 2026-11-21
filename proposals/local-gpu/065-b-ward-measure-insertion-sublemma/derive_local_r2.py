"""065 local round 2: independent re-derivation of the central identities (different code path
from derive_ward_r1.py).

L1  measure identity  d_eps lnZ = -<I> + <d_eps ln j>  for a NON-Gaussian 2-variable integral
    with a nontrivial Jacobian (numerical quadrature) and for a Gaussian (exact).
L2  null directions: unimodular field redefinitions x -> exp(eps B) x with tr B = 0 leave Z
    invariant for a non-invariant quartic action (so <I> = <d ln j> = 0), and a non-unimodular
    B gives d_eps lnZ = tr B exactly; tr B = 0 for eta-antisymmetric B (both signatures);
    tr ad_Lambda = 0 for random complex Lambda, N = 2..5.
L3  Gaussian conical-contact family A_n = A1 + (1/n - n) P + eps B on a 4-dim block with random
    rational data: d_eps S_D = Tr(G1 P G1 B) - 1/2 Tr(G1 B) exactly; replica-insertion form
    d_n<I_n>|_1 - <I_1>_1 agrees; at P = A1/2 the derivative vanishes for every B (the m5 case);
    for P != A1/2 the stationarity set is a hyperplane (functional B -> Tr(B K), K = G1(2P-A1)G1 != 0).
L4  content arithmetic for m4 / local 070: c_R = N_tot/6, kappa_X = 1 - n_D/2, c_T = c_R - 4 kappa_X,
    c_A = c_R + n_D (fixed-state); required edge coefficient relative to L0 is -(c_A - c_T) =
    -(4 kappa_X + n_D), equal to -4 kappa_X only at n_D = 0; at (6,2) -4 kappa_X = 0.
Run:  python -I derive_local_r2.py      (expected last line: ALL PASS)
"""
import random
import sympy as sp

ok_all = True


def check(tag, cond):
    global ok_all
    print("%-62s %s" % (tag, "PASS" if cond else "FAIL"))
    ok_all = ok_all and bool(cond)


# Gauss-Legendre tensor grid on [-L, L]^2 (double precision); derivatives by 5-point stencil.
import numpy as np
gx, gw = np.polynomial.legendre.leggauss(240)
Lbox = 7.0
X1, X2 = np.meshgrid(gx * Lbox, gx * Lbox, indexing="ij")
W2 = np.outer(gw, gw) * Lbox**2


def d5(f, x0, h=1e-3):
    return (-f(x0 + 2 * h) + 8 * f(x0 + h) - 8 * f(x0 - h) + f(x0 - 2 * h)) / (12 * h)


print("== L1 measure identity ==")
# non-Gaussian: S_eps = x^4/4 + y^4/4 + x^2 y^2/2 + x/3 + eps*(x^2 y + y/5), j_eps = exp(eps*(x^2 - y)/7)
S0 = X1**4 / 4 + X2**4 / 4 + X1**2 * X2**2 / 2 + X1 / 3
dS = X1**2 * X2 + X2 / 5
dlnj = (X1**2 - X2) / 7
wt = lambda e: np.exp(e * dlnj - (S0 + e * dS))
Z = lambda e: np.sum(W2 * wt(e))
e0 = 0.1
lhs = d5(lambda e: np.log(Z(e)), e0)
rhs = (-np.sum(W2 * dS * wt(e0)) + np.sum(W2 * dlnj * wt(e0))) / Z(e0)
print("  non-Gaussian: dlnZ = %.14f ; -<I>+<dlnj> = %.14f" % (lhs, rhs))
check("L1a non-Gaussian identity (|res| < 1e-9)", abs(lhs - rhs) < 1e-9)
x, eps, a, b, c, k = sp.symbols("x epsilon a b c k", positive=True)
# Gaussian: S = (a + eps b) x^2/2, ln j = eps c x^2; integrand exp(-k x^2/2), k = a + eps(b - 2c) > 0
Sg = (a + eps * b) * x**2 / 2
lj = eps * c * x**2
kk = a + eps * (b - 2 * c)
m0 = sp.integrate(sp.exp(-k * x**2 / 2), (x, -sp.oo, sp.oo))
m2 = sp.integrate(x**2 * sp.exp(-k * x**2 / 2), (x, -sp.oo, sp.oo))
Zg = m0.subs(k, kk)
x2 = (m2 / m0).subs(k, kk)
mI = sp.diff(Sg, eps).coeff(x, 2) * x2
mJ = sp.diff(lj, eps).coeff(x, 2) * x2
res = sp.simplify(sp.diff(sp.log(Zg), eps) - (-mI + mJ))
print("  Gaussian: dlnZ =", sp.simplify(sp.diff(sp.log(Zg), eps)), "; residual =", res)
check("L1b Gaussian identity exact (residual 0)", res == 0)

# ---------------- L2 ----------------
print("== L2 null directions ==")
from scipy.linalg import expm


def Zflow(e, Bm):
    E = expm(e * np.array(Bm, dtype=float))
    Y1 = E[0, 0] * X1 + E[0, 1] * X2
    Y2 = E[1, 0] * X1 + E[1, 1] * X2
    Sq = Y1**4 / 4 + Y2**4 / 3 + Y1 * Y2**3 / 5 + Y1**2 / 2 + Y2 / 3  # not invariant under the flows below
    return np.sum(W2 * np.exp(-Sq))


for name, Bm, trB in [("traceless non-orthogonal B=diag(1,-1)", [[1, 0], [0, -1]], 0),
                      ("rotation B=[[0,1],[-1,0]]", [[0, 1], [-1, 0]], 0),
                      ("boost-type B=[[0,1],[1,0]]", [[0, 1], [1, 0]], 0),
                      ("non-unimodular B=diag(1,0)", [[1, 0], [0, 0]], 1)]:
    dz = d5(lambda e: np.log(Zflow(e, Bm)), 0.0)
    # Z(eps) = Z(0)/det(exp(eps B)) => d lnZ = -tr B
    print("  %-40s dlnZ = %+.12f (expected %d)" % (name, dz, -trB))
    check("L2a " + name, abs(dz + trB) < 1e-8)
for sig in ([1, 1, 1, 1], [-1, 1, 1, 1]):
    eta = sp.diag(*sig)
    Om = sp.Matrix(4, 4, lambda i, j: sp.Symbol("w%d%d" % (min(i, j), max(i, j))) * (1 if i < j else (-1 if i > j else 0)))
    B = eta.inv() * Om  # B^a_b with eta_ac B^c_b = Om_ab antisymmetric
    check("L2b tr B = 0 for eta-antisymmetric B, eta=%s" % sig, sp.simplify(B.trace()) == 0 and (eta * B + (eta * B).T) == sp.zeros(4))
random.seed(65)
for N in (2, 3, 4, 5):
    L = sp.Matrix(N, N, lambda i, j: sp.Rational(random.randint(-9, 9), random.randint(1, 5)) + sp.I * random.randint(-5, 5))
    ad = sp.kronecker_product(sp.eye(N), L) - sp.kronecker_product(L.T, sp.eye(N))  # vec(LX - XL)
    Xr = sp.Matrix(N, N, lambda i, j: random.randint(-3, 3))
    vec = lambda M: sp.Matrix([M[i, j] for j in range(N) for i in range(N)])
    check("L2c tr ad_Lambda = 0, N=%d (and ad acts as [L,.])" % N, sp.simplify(ad.trace()) == 0 and ad * vec(Xr) == vec(L * Xr - Xr * L))

# ---------------- L3 ----------------
print("== L3 Gaussian conical-contact family ==")
n, e = sp.symbols("n e")
d = 4


def rsym(scale=5):
    M = sp.Matrix(d, d, lambda i, j: 0)
    for i in range(d):
        for j in range(i, d):
            v = sp.Rational(random.randint(-scale, scale), random.randint(1, 4))
            M[i, j] = v
            M[j, i] = v
    return M


R = sp.Matrix(d, d, lambda i, j: sp.Rational(random.randint(-3, 3), 2))
A1 = R * R.T + 3 * sp.eye(d)
P = sp.zeros(d)
P[0, 0], P[0, 1], P[1, 0], P[1, 1] = 1, sp.Rational(1, 3), sp.Rational(1, 3), sp.Rational(1, 2)  # "branch-locus" block
B = rsym()
G1 = A1.inv()


def SD_eps_derivative(Pm, Bm):
    An = A1 + (1 / n - n) * Pm + e * Bm
    lnZn = -sp.Rational(1, 2) * sp.log(An.det())
    lnZ1 = -sp.Rational(1, 2) * sp.log((A1 + e * Bm).det())
    W = lnZn - n * lnZ1
    SD = (W - n * sp.diff(W, n)).subs(n, 1)
    return sp.nsimplify(sp.simplify(sp.diff(SD, e).subs(e, 0)))


lhs = SD_eps_derivative(P, B)
closed = (G1 * P * G1 * B).trace() - sp.Rational(1, 2) * (G1 * B).trace()
print("  d_eps S_D =", lhs, "; closed form =", sp.nsimplify(closed))
check("L3a d_eps S_D = Tr(G1 P G1 B) - 1/2 Tr(G1 B) (exact)", sp.simplify(lhs - closed) == 0)
In = lambda m: sp.Rational(1, 2) * ((A1 + (1 / m - m) * P).inv() * B).trace()  # <I_n>_n = 1/2 Tr(B G_n)
rep = sp.diff(In(n), n).subs(n, 1) - In(1)
check("L3b equals d_n<I_n>|_1 - <I_1>_1 (replica-insertion form)", sp.simplify(rep - closed) == 0)
check("L3c generic B gives nonzero derivative", lhs != 0)
Phalf = A1 / 2
zero_all = all(SD_eps_derivative(Phalf, rsym()) == 0 for _ in range(3))
check("L3d at P = A1/2: derivative 0 for random B (m5 degenerate case)", zero_all)
K = G1 * (2 * P - A1) * G1
check("L3e P != A1/2: K = G1(2P-A1)G1 != 0, hyperplane Tr(BK)=0 is codim 1", K != sp.zeros(d) and K == K.T)
check("L3f closed form = 1/2 Tr(B K)", sp.simplify(closed - sp.Rational(1, 2) * (B * K).trace()) == 0)

# ---------------- L4 ----------------
print("== L4 content arithmetic (m4, local 070) ==")
Ns, nD = sp.symbols("N_s n_D")
Ntot = Ns + 2 - 4 * nD
cR = Ntot / 6
kX = 1 - nD / 2
cT = cR - 4 * kX
cA = cR + nD
gap = sp.expand(cA - cT)
print("  c_A - c_T =", gap, "; 4 kappa_X + n_D =", sp.expand(4 * kX + nD))
check("L4a c_A - c_T = 4 kappa_X + n_D", sp.simplify(gap - 4 * kX - nD) == 0)
check("L4b gap equals 4 kappa_X iff n_D = 0", sp.solve(sp.Eq(gap, 4 * kX), nD) == [0])
v = {Ns: 6, nD: 2}
print("  at (6,2): kappa_X=%s, -4kappa_X=%s, c_T=%s, c_A=%s" % (kX.subs(v), (-4 * kX).subs(v), cT.subs(v), cA.subs(v)))
check("L4c at (6,2): -4 kappa_X = 0, c_T = 0, c_A = 2 (0 = 0 only for periodic/smooth)", (-4 * kX).subs(v) == 0 and cT.subs(v) == 0 and cA.subs(v) == 2)
check("L4d at n_D = 0: -4 kappa_X = -4", (-4 * kX).subs(nD, 0) == -4)

# ---------------- L5 (avenue probe, proposal text only) ----------------
print("== L5 fork probe: stationarity on all 'fixed-volume' B with Tr(G1 B) = 0 ==")
# d_eps S_D = Tr(G1 P G1 B) on that subspace; vanishing for all such symmetric B <=> G1 P G1 = lam G1 <=> P = lam A1
syms = sp.symbols("q0:%d" % (d * (d + 1) // 2))
Bg = sp.zeros(d)
t = 0
for i in range(d):
    for j in range(i, d):
        Bg[i, j] = syms[t]
        Bg[j, i] = syms[t]
        t += 1
cons = (G1 * Bg).trace()
basis = []
sol = sp.solve(cons, syms[0], dict=True)[0]
Bfv = Bg.subs(sol)
lin = sp.expand((G1 * P * G1 * Bfv).trace())
coeffs = [lin.coeff(sy) for sy in syms[1:]]
check("L5a localized P: some fixed-volume B has nonzero derivative", any(cf != 0 for cf in coeffs))
lam = sp.Rational(3, 7)
lin2 = sp.expand((G1 * (lam * A1) * G1 * Bfv).trace())
check("L5b P = lam*A1: derivative vanishes on every fixed-volume B", all(lin2.coeff(sy) == 0 for sy in syms[1:]))
# converse: the conditions coeffs(P_general)=0 force P = lam A1 (solve for a general symmetric P)
psy = sp.symbols("p0:%d" % (d * (d + 1) // 2))
Pg = sp.zeros(d)
t = 0
for i in range(d):
    for j in range(i, d):
        Pg[i, j] = psy[t]
        Pg[j, i] = psy[t]
        t += 1
lin3 = sp.expand((G1 * Pg * G1 * Bfv).trace())
eqs = [lin3.coeff(sy) for sy in syms[1:]]
solP = sp.solve(eqs, psy, dict=True)[0]
Psol = Pg.subs(solP)
free = sorted(Psol.free_symbols, key=str)
ratio_ok = len(free) == 1 and sp.simplify(Psol - (Psol[0, 0] / A1[0, 0]) * A1) == sp.zeros(d)
print("  general solution P =", "lam*A1 with lam =", sp.simplify(Psol[0, 0] / A1[0, 0]))
check("L5c converse: stationarity on all fixed-volume B forces P proportional to A1", ratio_ok)

print("ALL PASS" if ok_all else "SOME CHECK FAILED")
