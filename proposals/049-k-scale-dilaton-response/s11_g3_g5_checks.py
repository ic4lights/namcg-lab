"""049 s11: checks for the texts G2-G6 of review-r2.md.

(A) Representation-independent: exact computation in the universal enveloping algebra, using only the commutation
    relations of so(3,1) over C and PBW normal ordering. No matrix for the orbital generators appears.
(B) A non-unitary infinite-dimensional check: su(2) Verma modules at complex label j, truncated; only entries that
    the truncation does not reach are compared. This includes the labels Xi = +-m_L + i varsigma.
(C) Sign of Z: Hessian by second differences of the action; the double commutator; Casimirs on T_a.
(D) Discriminant of the bracket in G4.
(E) G5: normalisation of the mixed term; 8 mu/chi^2 and 4 limits of -Sum c_i b_i/(b_i+mu) on S^2_N.
Prints only."""
import itertools
import numpy as np
import sympy as sp
import mpmath as mp

EPS = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}


class UEA:
    """Elements are dicts word -> complex; coefficients are dyadic, so double arithmetic is exact here."""

    def __init__(self, comm):
        self.comm = comm

    def clean(self, a):
        return {w: c for w, c in a.items() if c != 0}

    def add(self, a, b, f=1):
        r = dict(a)
        for w, c in b.items():
            r[w] = r.get(w, 0) + f * c
        return self.clean(r)

    def scal(self, a, f):
        return self.clean({w: f * c for w, c in a.items()})

    def normal(self, w, c, out):
        for i in range(len(w) - 1):
            if w[i] > w[i + 1]:
                self.normal(w[:i] + (w[i + 1], w[i]) + w[i + 2:], c, out)
                for g, f in self.comm.get((w[i], w[i + 1]), {}).items():
                    self.normal(w[:i] + (g,) + w[i + 2:], c * f, out)
                return
        out[w] = out.get(w, 0) + c

    def mul(self, a, b):
        out = {}
        for w1, c1 in a.items():
            for w2, c2 in b.items():
                self.normal(w1 + w2, c1 * c2, out)
        return self.clean(out)

    def gen(self, i):
        return {(i,): 1}

    def one(self):
        return {(): 1}


def su2_comm(off=0):
    d = {}
    for (i, j, k), e in EPS.items():
        d[(i + off, j + off)] = {k + off: 1j * e}
    return d


def mat_mul(U, X, Y):
    n = len(X)
    R = [[{} for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                R[i][j] = U.add(R[i][j], U.mul(X[i][k], Y[k][j]))
    return R


def mat_add(U, X, Y, f=1):
    n = len(X)
    return [[U.add(X[i][j], Y[i][j], f) for j in range(n)] for i in range(n)]


def scalar_mat(U, el, n):
    return [[el if i == j else {} for j in range(n)] for i in range(n)]


def trace(U, X):
    r = {}
    for i in range(len(X)):
        r = U.add(r, X[i][i])
    return r


def is_zero(X):
    return all(not X[i][j] for i in range(len(X)) for j in range(len(X)))


SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]


def dot_mat(U, off, sigs):
    """-2 Sum A_i sigs[i], an operator-valued matrix."""
    n = sigs[0].shape[0]
    R = [[{} for _ in range(n)] for _ in range(n)]
    for i in range(3):
        for a in range(n):
            for b in range(n):
                if sigs[i][a, b] != 0:
                    R[a][b] = U.add(R[a][b], U.scal(U.gen(i + off), -2 * complex(sigs[i][a, b])))
    return R


print("(A1) su(2) relations only: Z = -2 A.sigma on the chiral block")
U = UEA(su2_comm())
Z = dot_mat(U, 0, SIG)
Cas = {}
for i in range(3):
    Cas = U.add(Cas, U.mul(U.gen(i), U.gen(i)))
# Z from the definition C_tot - C_orb - C_S with C = -2 (Casimir), the tot generator being A_i + sigma_i/2.
Ctot = [[{} for _ in range(2)] for _ in range(2)]
for i in range(3):
    Gi = [[U.add(U.gen(i) if a == b else {}, {(): complex(SIG[i][a, b]) / 2}) for b in range(2)] for a in range(2)]
    Ctot = mat_add(U, Ctot, mat_mul(U, Gi, Gi))
diff = mat_add(U, Ctot, scalar_mat(U, Cas, 2), -1)
diff = mat_add(U, diff, scalar_mat(U, {(): 0.75}, 2), -1)
fromdef = [[U.scal(diff[a][b], -2) for b in range(2)] for a in range(2)]
print("    C_tot - C_orb - C_S minus (-2 A.sigma) vanishes in U(su2):", is_zero(mat_add(U, fromdef, Z, -1)))
Zm1 = mat_add(U, Z, scalar_mat(U, U.one(), 2), -1)
lhs = mat_mul(U, Zm1, Zm1)
Xi2 = U.add(U.scal(Cas, 4), U.one())
print("    (Z-1)^2 - (4 A^2 + 1) vanishes in U(su2):", is_zero(mat_add(U, lhs, scalar_mat(U, Xi2, 2), -1)))
print("    trace of Z over the block is zero in U(su2):", not trace(U, Z))

s, X2 = sp.symbols("s X2")
Xi = sp.sqrt(X2)
Pser = sp.series(sp.exp(-s) * (2 * sp.cosh(s * Xi) + 2 * sp.sinh(s * Xi) / Xi), s, 0, 9).removeO()
Pser = sp.expand(sp.simplify(Pser))


def poly_to_uea(U, expr, var_map):
    """Polynomial with rational coefficients in the keys of var_map, mapped to the algebra."""
    P = sp.Poly(expr, *var_map.keys())
    r = {}
    for mon, co in P.terms():
        t = U.one()
        for e, el in zip(mon, var_map.values()):
            for _ in range(e):
                t = U.mul(t, el)
        r = U.add(r, U.scal(t, complex(float(co))))
    return r


print("    block trace of Z^k against (-1)^k k! [s^k] P(Xi), with Xi^2 = 4A^2+1, exact in U(su2):")
Zk = scalar_mat(U, U.one(), 2)
for k in range(0, 9):
    if k > 0:
        Zk = mat_mul(U, Zk, Z)
    co = sp.expand((-1) ** k * sp.factorial(k) * Pser.coeff(s, k))
    tgt = poly_to_uea(U, co, {X2: Xi2}) if co.has(X2) else ({(): complex(float(co))} if co != 0 else {})
    r = U.add(trace(U, Zk), tgt, -1)
    print("      k=%d  coefficient %s  residual zero: %s" % (k, co, max([abs(c) for c in r.values()] or [0]) < 1e-9))

print("(A2) so(3,1) relations only: L_i = gens 0-2, N_i = gens 3-5; A = (L+iN)/2, B = (L-iN)/2")
comm31 = {}
for (i, j, k), e in EPS.items():
    comm31[(i, j)] = {k: 1j * e}
    comm31[(i, j + 3)] = {k + 3: 1j * e}
    comm31[(i + 3, j)] = {k + 3: 1j * e}
    comm31[(i + 3, j + 3)] = {k: -1j * e}
V = UEA(comm31)
Ag = [V.add(V.scal(V.gen(i), 0.5), V.scal(V.gen(i + 3), 0.5j)) for i in range(3)]
Bg = [V.add(V.scal(V.gen(i), 0.5), V.scal(V.gen(i + 3), -0.5j)) for i in range(3)]
ok = True
for i, j in itertools.product(range(3), repeat=2):
    cAA = V.add(V.mul(Ag[i], Ag[j]), V.mul(Ag[j], Ag[i]), -1)
    cBB = V.add(V.mul(Bg[i], Bg[j]), V.mul(Bg[j], Bg[i]), -1)
    cAB = V.add(V.mul(Ag[i], Bg[j]), V.mul(Bg[j], Ag[i]), -1)
    tA, tB = {}, {}
    for k in range(3):
        e = EPS.get((i, j, k), 0)
        if e:
            tA = V.add(tA, V.scal(Ag[k], 1j * e))
            tB = V.add(tB, V.scal(Bg[k], 1j * e))
    ok = ok and not V.add(cAA, tA, -1) and not V.add(cBB, tB, -1) and not cAB
print("    A and B close as two commuting su(2):", ok)
A2 = {}
B2 = {}
L2 = {}
N2 = {}
LN = {}
for i in range(3):
    A2 = V.add(A2, V.mul(Ag[i], Ag[i]))
    B2 = V.add(B2, V.mul(Bg[i], Bg[i]))
    L2 = V.add(L2, V.mul(V.gen(i), V.gen(i)))
    N2 = V.add(N2, V.mul(V.gen(i + 3), V.gen(i + 3)))
    LN = V.add(LN, V.mul(V.gen(i), V.gen(i + 3)))
C31 = V.add(N2, L2, -1)
print("    N^2 - L^2 + 2(A^2+B^2) vanishes:", not V.add(C31, V.scal(V.add(A2, B2), 2)))

print("(A3) vector block over su(2)+su(2): Z_V = Z_A + Z_B on (1/2,1/2), relations only")
W = UEA({**su2_comm(0), **su2_comm(3)})
I2 = np.eye(2, dtype=complex)
ZA = dot_mat(W, 0, [np.kron(S, I2) for S in SIG])
ZB = dot_mat(W, 3, [np.kron(I2, S) for S in SIG])
print("    [Z_A, Z_B] = 0:", is_zero(mat_add(W, mat_mul(W, ZA, ZB), mat_mul(W, ZB, ZA), -1)))
ZV = mat_add(W, ZA, ZB)
CasA, CasB = {}, {}
for i in range(3):
    CasA = W.add(CasA, W.mul(W.gen(i), W.gen(i)))
    CasB = W.add(CasB, W.mul(W.gen(i + 3), W.gen(i + 3)))
XA = W.add(W.scal(CasA, 4), W.one())
XB = W.add(W.scal(CasB, 4), W.one())
Y2 = sp.Symbol("Y2")
Pp = Pser
Pm = Pser.subs(X2, Y2)
prod = sp.expand(Pp * Pm)
Zk = scalar_mat(W, W.one(), 4)
print("    tr_V Z_V^k against (-1)^k k! [s^k] P_+ P_-, exact in U(su2+su2):")
for k in range(0, 7):
    if k > 0:
        Zk = mat_mul(W, Zk, ZV)
    co = sp.expand((-1) ** k * sp.factorial(k) * prod.coeff(s, k))
    tgt = poly_to_uea(W, co, {X2: XA, Y2: XB})
    r = W.add(trace(W, Zk), tgt, -1)
    print("      k=%d  residual zero: %s" % (k, max([abs(c) for c in r.values()] or [0]) < 1e-9))
Dt = sp.expand(prod - 2 * (Pp + Pm) + 4 - (Pp - 2) * (Pm - 2))
print("    tr_V - 2 tr_D + 4 - (P_+ - 2)(P_- - 2) as series:", Dt)
print("    P - 2 through s^3:", sp.factor(sp.expand(Pser.coeff(s, 2))), "* s^2 ,", sp.factor(sp.expand(Pser.coeff(s, 3))), "* s^3")

print("(B) Verma modules at complex j, truncated; interior entries only")


def verma(j, K):
    A3 = np.diag([j - k for k in range(K)]).astype(complex)
    Am = np.zeros((K, K), complex)
    Ap = np.zeros((K, K), complex)
    for k in range(K - 1):
        Am[k + 1, k] = 1.0
        Ap[k, k + 1] = (k + 1) * (2 * j - k)
    return (Ap + Am) / 2, (Ap - Am) / 2j, A3


def P_num(Xi_, s_):
    return np.exp(-s_) * (2 * np.cosh(s_ * Xi_) + 2 * np.sinh(s_ * Xi_) / Xi_)


K = 40
s_ = 0.2
for m_L, vs in ((0, 0.7), (1, 0.0 + 1.3), (2, 1.3), (5, 0.4), (3, 2.5)):
    for Xi_ in (m_L + 1j * vs, -m_L + 1j * vs):
        j = (Xi_ - 1) / 2
        A = verma(j, K)
        Zb = sum(-2 * np.kron(A[i], SIG[i]) for i in range(3))
        comm_res = np.abs((A[0] @ A[1] - A[1] @ A[0] - 1j * A[2])[:K - 4, :K - 4]).max()
        Id = np.eye(2 * K, dtype=complex)
        res = (Zb - Id) @ (Zb - Id) - Xi_ ** 2 * Id
        interior = 2 * (K - 4)
        r1 = np.abs(res[:interior, :interior]).max()
        # partial trace of the exponential on the state k = 0..3 by Taylor series; Z raises the level by at most one
        # per power, so 30 powers stay inside the truncation for k <= 8.
        term = Id.copy()
        ex = Id.copy()
        for q in range(1, 30):
            term = term @ (-s_ * Zb) / q
            ex = ex + term
        ptr = ex[0:2, 0:2].trace()
        print("    Xi=%-11s comm res %.1e  (Z-1)^2-Xi^2 res %.1e  partial tr Z %.1e  partial tr e^{-sZ} / P(Xi) - 1 = %.1e" % (
            complex(Xi_), comm_res, r1, abs(Zb[0:2, 0:2].trace()), abs(ptr / P_num(Xi_, s_) - 1)))
print("    conjugate factors on the principal series: min (P_+-2)(P_--2) and max |imag| over a grid, s in (0,6]")
mn, im = 1e9, 0
for m_L in range(0, 8):
    for vs in np.linspace(0.05, 12, 80):
        for s0 in np.linspace(0.02, 6, 60):
            v = (P_num(m_L + 1j * vs, s0) - 2) * (P_num(-m_L + 1j * vs, s0) - 2)
            mn = min(mn, v.real)
            im = max(im, abs(v.imag) / (1 + abs(v)))
print("      min %.3e, max relative |imag| %.1e" % (mn, im))

print("(C) sign of Z: Hessian of S = -(1/4) Sum Tr[X_a,X_b]^2 by second differences; D=4 random Hermitian, size 5")
rng = np.random.default_rng(49)


def herm(n):
    a = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    return (a + a.conj().T) / 2


def comm(a, b):
    return a @ b - b @ a


def S_act(X):
    return -0.25 * sum(np.trace(comm(X[a], X[b]) @ comm(X[a], X[b])).real for a in range(len(X)) for b in range(len(X)))


def Hess(X, A):
    D = len(X)
    out = []
    for b in range(D):
        v = sum(comm(X[a], comm(X[a], A[b])) for a in range(D))
        v = v + 2 * sum(comm(comm(X[b], X[a]), A[a]) for a in range(D))
        out.append(v)
    return out


n = 5
X = [herm(n) for _ in range(4)]
A = [herm(n) for _ in range(4)]
e = 1e-3
d2 = (S_act([x + e * a for x, a in zip(X, A)]) + S_act([x - e * a for x, a in zip(X, A)]) - 2 * S_act(X)) / e ** 2
gf = -np.trace(sum(comm(X[a], A[a]) for a in range(4)) @ sum(comm(X[a], A[a]) for a in range(4))).real
quad = sum(np.trace(a @ h).real for a, h in zip(A, Hess(X, A)))
print("    <A,HA> with H = Box + 2[[X_b,X_a],.]: %.8f ; second difference of S plus gauge term: %.8f" % (quad, d2 + gf))
HX = Hess(X, X)
BoxX = [sum(comm(X[a], comm(X[a], X[b])) for a in range(4)) for b in range(4)]
print("    max |H X_b - 3 Box X_b| = %.1e (mass-free form)" % max(np.abs(h - 3 * b).max() for h, b in zip(HX, BoxX)))


def so_gens(eta):
    d = len(eta)
    G = {}
    for a in range(d):
        for b in range(a + 1, d):
            M = np.zeros((d, d))
            M[a, b] = eta[b]
            M[b, a] = -eta[a]
            G[(a, b)] = M
    return G


eta5 = [-1, 1, 1, 1, 1]
G5 = so_gens(eta5)
keys5 = list(G5)
C_vec5 = sum(eta5[a] * eta5[b] * G5[(a, b)] @ G5[(a, b)] for a, b in keys5)
adj = {}
for k in keys5:
    Mx = np.zeros((10, 10))
    for col, kk in enumerate(keys5):
        c = G5[k] @ G5[kk] - G5[kk] @ G5[k]
        for row, (p, q) in enumerate(keys5):
            Mx[row, col] = c[p, q] / (G5[(p, q)][p, q])
    adj[k] = Mx
C_adj = sum(eta5[a] * eta5[b] * adj[(a, b)] @ adj[(a, b)] for a, b in keys5)
eta4 = eta5[:4]
G4 = so_gens(eta4)
C_v4 = sum(eta4[a] * eta4[b] * G4[(a, b)] @ G4[(a, b)] for a, b in G4)
print("    real generators, C = (1/2) J_ab J^ab: so(3,1) on the vector %s; so(4,1) on the adjoint %s" % (
    sorted(set(np.round(np.diag(C_v4), 10))), sorted(set(np.round(np.diag(C_adj), 10)))))
print("    T_a = M^{a4}: C_31 = -3, C_41 = -6, so H_0 = C_31 - C_41 = 3 and Box = C_41 - C_31 = -3 as in the merged text")
print("    singlet: C_tot = 0, C_Sigma = -3, so Z = 0 + 3 + 3 = 6 and C_tot - C_41 - C_Sigma = 9 = 3 H_0, without mass term")

print("(D) G4: bracket (15/4)th^2/D - th c/D^2 + 2c^2/D^3 = q(D)/D^3")
th, c, D = sp.symbols("vartheta c D", positive=True)
q = sp.Rational(15, 4) * th ** 2 * D ** 2 - th * c * D + 2 * c ** 2
print("    discriminant of q in D:", sp.factor(sp.discriminant(q, D)))
print("    at c = 0 (J = 0) the discriminant is 0 and q = (15/4) th^2 D^2 > 0 for D > 0; the bracket is 15 th^2/(4D) > 0")

print("(E) G5: normalisation; limits of S(mu) = -Sum_i c_i b_i/(b_i+mu) on S^2_N")
Xp, Xm, ss, b, mu, co, cJ = sp.symbols("Xp Xm s b mu co c_J", positive=True)
sig = sp.series(sp.exp(-ss) * (2 * sp.cosh(ss * Xp) + 2 * sp.sinh(ss * Xp) / Xp), ss, 0, 3).removeO() + \
    sp.series(sp.exp(-ss) * (2 * sp.cosh(ss * Xm) + 2 * sp.sinh(ss * Xm) / Xm), ss, 0, 3).removeO() - 4
print("    sigma through s^2:", sp.simplify(sig), " = -2 s^2 C with C = -(Xi_+^2+Xi_-^2-2)/2 = N^2 - c_J, so sigma gains +2 s^2 c_J")
integrand = -sp.Rational(1, 2) * ss ** (-3) * (-sp.Rational(1, 4)) * (2 * ss ** 2 * cJ) * co * (-2 * ss * b) * sp.exp(-ss * (b + mu))
print("    -(1/2) int ds/s s^-2 (-(1/4) 2 s^2 c_J tau^K) under d/dln chi, in units 1/16 pi^2:", sp.simplify(sp.integrate(integrand, (ss, 0, sp.oo))),
      " so -c_J c_i b_i/(b_i+mu) in units 1/32 pi^2")

l, Nn = sp.symbols("l N", positive=True, integer=True)
term = 8 * (l + 1) / l ** 2 + 8 * l / (l + 1) ** 2 - 8 * (2 * l + 1) / (l * (l + 1))
print("    Sum c_i/b_i summand times chi^2 minus 8(1/l^2 - 1/(l+1)^2):", sp.simplify(term - 8 * (1 / l ** 2 - 1 / (l + 1) ** 2)),
      " so S -> 8(1-1/N^2) mu/chi^2 for chi^2 >> mu")
u = sp.Symbol("u", positive=True)
print("    sum of c_i over the three towers at each l:", sp.simplify(4 * (2 * l + 2) + 8 * l - 8 * (2 * l + 1)))
print("    sum of c_i b_i/chi^2 at each l:", sp.simplify(4 * (2 * l + 2) * l ** 2 + 8 * l * (l + 1) ** 2 - 8 * (2 * l + 1) * l * (l + 1)))
mp.mp.dps = 40


def S_num(N_, r):
    """chi^2 = 1, mu = r. All levels l = 0..N-1; b = 0 terms vanish for r > 0."""
    t = mp.mpf(0)
    r = mp.mpf(r)
    for L in range(N_):
        L_ = mp.mpf(L)
        for cc, bb in ((8 * (L_ + 1), L_ * L_), (8 * L_, (L_ + 1) ** 2), (-8 * (2 * L_ + 1), L_ * (L_ + 1))):
            if bb > 0:
                t -= cc * bb / (bb + r)
    return t


print("      N       mu/chi^2         S          S/(8 mu/chi^2)      S/4")
peak = 0
for N_ in (2048, 8192):
    grid = ["0.0001", "0.001", "0.01", "0.1", "0.5", "1", "2", "5", "10", "30", "100", "1000", "10000"] + (["100000", "1000000"] if N_ == 8192 else ["100000"])
    for r in grid:
        v = S_num(N_, r)
        peak = max(peak, v)
        print("    %6d %12s  %s  %s  %s" % (N_, r, mp.nstr(v, 10), mp.nstr(v / (8 * mp.mpf(r)), 8), mp.nstr(v / 4, 10)))
print("    largest S on these grids:", mp.nstr(peak, 12), " below 4:", peak < 4)
print("    beyond the cutoff (mu >~ N^2 chi^2), where equal weights fail: S is smaller again")
for r in ("1e7", "1e8", "1e10"):
    print("    %6d %12s  %s" % (2048, r, mp.nstr(S_num(2048, r), 8)))

print("    relative size at equal weights: Sum_J (2J+1) c_J 4 / (F (15/2) th^2 N^2) = (4/15) n(n+2)/(th^2 N^2)")
for N_, n_ in ((1024, 10), (256, 10), (64, 5)):
    tot = sum((2 * J + 1) * J * (J + 1) for J in range(n_ + 1))
    F = (n_ + 1) ** 2
    print("      N=%d n=%d: <c_J> = %s, n(n+2)/2 = %s; ratio at th=1 %.3e; (n/N)^2 %.3e" % (
        N_, n_, sp.Rational(tot, F), sp.Rational(n_ * (n_ + 2), 2), 4 * tot / F / (7.5 * N_ ** 2), (n_ / N_) ** 2))
