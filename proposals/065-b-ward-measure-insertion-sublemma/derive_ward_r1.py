"""Proposal 065 (B.ward) exact checks. Deterministic; run: python -I derive_ward_r1.py

Check 1  Insertion identity with a measure Jacobian: for Z(eps)=Int dmu j_eps exp(-S_eps),
         d lnZ/deps = -<I>_ + <d ln j/deps>_, verified on a convergent Gaussian example.
Check 2  Schwinger-Dyson/loop kernel for a matrix Gaussian: with S = 1/2 x^T A x - J.x,
         (a) EOM insertions have zero expectation; (b) <(AX-J)_k X_i> = delta_ki (contact term);
         (c) the linear change-of-variables insertion satisfies <(Mx).(Ax)> = tr M = Div,
             so a traceless M gives a null insertion.
Check 3  Unimodularity of the compensating rotation and of adjoint flows:
         (a) a general so(1,3) generator B (eta = diag(-1,1,1,1)) has tr B = 0, so
             (det exp(tB))^(N^2) = exp(t N^2 tr B) = 1 on the N^2 matrix entries;
         (b) tr ad_Lambda = 0 for a general 2x2 Lambda (4x4 adjoint representation);
         (c) numeric det(exp M) = exp(tr M) sanity for a concrete nonnormal M.
Check 4  Gaussian conical-contact family A_n = A + (1/n - n) P + eps B (A diagonal 3x3,
         P = diag(1,0,0), B a general symmetric 3x3):
         (a) d deps ln Z_n = -<I_n>_n exactly, with I_n = 1/2 x^T B x;
         (b) d deps S_D |_0 = Tr(G1 B G1 P) - 1/2 Tr(G1 B), the closed form;
         (c) nonzero for B = b*E11 (generic block deformation);
         (d) stationarity d deps S_D = 0 is a codimension-one linear condition on B
             (solved explicitly), and B = E12+E21 is in the kernel;
         (e) c(n) = 1/n - n has c(1) = 0, c'(1) = -2, and the flat-cone coefficient
             (1/12)(1/n - n) of the manuscript equals +(1/12) c(n).
"""
import sympy as sp


def banner(t):
    print()
    print("=" * 72)
    print(t)
    print("=" * 72)


# ---------------------------------------------------------------- Check 1
banner("Check 1: insertion identity with measure Jacobian")
x, eps, a, c1 = sp.symbols("x eps a c", positive=True)
S1 = sp.Rational(1, 2) * a * x ** 2
j1 = sp.exp(-sp.Rational(1, 2) * eps * c1 * x ** 2)
Z = sp.integrate(j1 * sp.exp(-S1), (x, -sp.oo, sp.oo))
lnZ = sp.log(sp.simplify(Z))
dlnZ = sp.simplify(sp.diff(lnZ, eps))
measure = j1 * sp.exp(-S1)
avg_I = sp.simplify(sp.integrate(sp.diff(S1, eps) * measure, (x, -sp.oo, sp.oo)) / Z)
avg_dlnj = sp.simplify(sp.integrate(sp.diff(sp.log(j1), eps) * measure, (x, -sp.oo, sp.oo)) / Z)
res1 = sp.simplify(dlnZ - (-avg_I + avg_dlnj))
print("d deps lnZ          =", dlnZ)
print("-<d deps S>_        =", sp.simplify(-avg_I))
print("<d deps ln j>_      =", avg_dlnj)
print("identity residual   =", res1)
print("PASS" if res1 == 0 else "FAIL")

# ---------------------------------------------------------------- Check 2
banner("Check 2: SD/loop kernel for a Gaussian (explicit data, exact rationals)")
# A = [[2, 1/2], [1/2, 3]], J = (1, -1); S = 1/2 x^T A x - J.x
A = sp.Matrix([[2, sp.Rational(1, 2)], [sp.Rational(1, 2), 3]])
J = sp.Matrix([1, -1])
x1, x2 = sp.symbols("x1 x2", real=True)
xs = sp.Matrix([x1, x2])
S2 = (sp.Rational(1, 2) * (xs.T * A * xs)[0] - (J.T * xs)[0])
EOM = A * xs - J  # dS/dx
Zg = sp.integrate(sp.exp(-S2), (x1, -sp.oo, sp.oo), (x2, -sp.oo, sp.oo))
Zg = sp.simplify(sp.nsimplify(Zg))
def Av(f):
    return sp.simplify(sp.integrate(sp.exp(-S2) * f, (x1, -sp.oo, sp.oo), (x2, -sp.oo, sp.oo)) / Zg)
ok2a = all(sp.simplify(Av(EOM[i])) == 0 for i in range(2))
print("(a) <d_i S> = 0 for all i :", ok2a)
ok2b = True
for k in range(2):
    for ii in range(2):
        r = sp.simplify(Av(EOM[k] * xs[ii]) - sp.KroneckerDelta(k, ii))
        ok2b = ok2b and (r == 0)
print("(b) <(d_k S) x_i> = delta_ki (contact) :", ok2b)
m, nn = sp.symbols("m n", real=True)
M = sp.Matrix([[0, m], [nn, 0]])  # traceless linear vector field
S0 = sp.Rational(1, 2) * (xs.T * A * xs)[0]
Z0 = sp.integrate(sp.exp(-S0), (x1, -sp.oo, sp.oo), (x2, -sp.oo, sp.oo))
def Av0(f):
    return sp.simplify(sp.integrate(sp.exp(-S0) * f, (x1, -sp.oo, sp.oo), (x2, -sp.oo, sp.oo)) / Z0)
ins = Av0(((M * xs).T * (A * xs))[0])
print("(c) <(Mx).(Ax)> =", ins, " ; Div(Mx) = tr M = 0")
print("PASS" if (ok2a and ok2b and ins == 0) else "FAIL")

# ---------------------------------------------------------------- Check 3
banner("Check 3: unimodularity of compensating rotations and adjoint flows")
eta = sp.diag(-1, 1, 1, 1)
# eta-antisymmetric generator: B = eta^{-1} * (antisymmetric matrix)
Asym = sp.zeros(4)
sy = sp.symbols("s01 s02 s03 s12 s13 s23", real=True)
vals = {(0, 1): sy[0], (0, 2): sy[1], (0, 3): sy[2], (1, 2): sy[3], (1, 3): sy[4], (2, 3): sy[5]}
for (p, q), v in vals.items():
    Asym[p, q] = v
    Asym[q, p] = -v
Bfull = sp.simplify(eta.inv() * Asym)
trB = sp.simplify(Bfull.trace())
etaanti = sp.simplify(Bfull.T * eta + eta * Bfull)
t, Nsym = sp.symbols("t N", positive=True)
print("(a) tr B (general so(1,3) generator)      :", trB)
print("    eta-antisymmetry residual            :", etaanti == sp.zeros(4))
print("    (det exp(tB))^(N^2) = exp(t N^2 trB) :", sp.simplify(sp.exp(t * Nsym ** 2 * trB)) == 1)
# concrete rotation+boost expm determinant (mpmath series, dps fixed)
from mpmath import mp
from itertools import permutations
mp.dps = 40
def to_mp(M):
    return mp.matrix([[mp.mpf(x.p) / x.q if isinstance(x, sp.Rational) else mp.mpf(x) for x in row] for row in M.tolist()])
def mexp(M, terms=80):
    n = M.rows
    S = mp.eye(n); term = mp.eye(n)
    for k in range(1, terms + 1):
        term = term * M / k
        S += term
    return S
def det4(M):
    tot = mp.mpf(0)
    for p in permutations(range(4)):
        sgn = 1
        pi = list(p)
        for i in range(4):
            for j in range(i + 1, 4):
                if pi[i] > pi[j]:
                    sgn = -sgn
        prod = mp.mpf(1)
        for i in range(4):
            prod *= M[i, pi[i]]
        tot += sgn * prod
    return tot
bv = Bfull.subs({sy[0]: sp.Rational(3, 5), sy[3]: sp.Rational(7, 10), sy[1]: 0, sy[2]: 0, sy[4]: 0, sy[5]: 0})
detbv = det4(mexp(to_mp(bv))) - 1
print("    det(exp(rotation+boost sample)) - 1  :", mp.nstr(detbv, 12))
# adjoint flow
Lam = sp.Matrix(sp.symbols("l11 l12 l21 l22", real=True)).reshape(2, 2)
ad = sp.zeros(4)
basis = [sp.Matrix([[1, 0], [0, 0]]), sp.Matrix([[0, 1], [0, 0]]),
         sp.Matrix([[0, 0], [1, 0]]), sp.Matrix([[0, 0], [0, 1]])]
for j, Ej in enumerate(basis):
    col = (Lam * Ej - Ej * Lam).reshape(4, 1)
    ad[:, j] = col
trad = sp.simplify(ad.trace())
print("(b) tr ad_Lambda (general 2x2 Lambda)     :", trad)
adnum = ad.subs(dict(zip(Lam, [sp.Integer(1), sp.Integer(2), sp.Integer(3), sp.Integer(4)])))
deta = det4(mexp(to_mp(adnum))) - 1
print("    det(exp(ad sample)) - 1 (numeric)    :", mp.nstr(deta, 12))
print("PASS" if (trB == 0 and trad == 0 and etaanti == sp.zeros(4) and abs(detbv) < mp.mpf(10) ** -20 and abs(deta) < mp.mpf(10) ** -20) else "FAIL")

# ---------------------------------------------------------------- Check 4
banner("Check 4: Gaussian conical-contact family A_n = A + (1/n-n) P + eps B")
n, b = sp.symbols("n b", positive=True)
a1, a2, a3 = sp.symbols("a1 a2 a3", positive=True)
b11, b12, b13, b22, b23, b33 = sp.symbols("b11 b12 b13 b22 b23 b33", real=True)
Am = sp.diag(a1, a2, a3)
Pm = sp.diag(1, 0, 0)
Bm = sp.Matrix([[b11, b12, b13], [b12, b22, b23], [b13, b23, b33]])
cn = 1 / n - n
An = Am + cn * Pm + eps * Bm
Xv = sp.Matrix(sp.symbols("y1 y2 y3", real=True))
# (a) d deps ln Z_n = -<I_n>_n with I_n = 1/2 x^T B x
lnZn = sp.log(sp.det(An))  # up to eps-independent constants; sign: lnZ ~ -1/2 ln det
Wn = -sp.Rational(1, 2) * lnZn
In = sp.Rational(1, 2) * (Xv.T * Bm * Xv)[0]
Gn = An.inv()
avg_In = sp.Rational(1, 2) * sp.simplify((Bm * Gn).trace())  # <x^T B x> = Tr(B G_n)
lhs = sp.simplify(sp.diff(Wn, eps))
res4a = sp.simplify(lhs + avg_In)
print("(a) d deps lnZ_n + <I_n>_n residual       :", res4a)
# (b) closed form of d deps S_D at eps=0
S_D = sp.simplify(Wn - n * sp.diff(Wn, n)).subs(n, 1)
dSd = sp.simplify(sp.diff(S_D, eps).subs(eps, 0))
G1 = Am.inv()
closed = sp.simplify((G1 * Bm * G1 * Pm).trace() - sp.Rational(1, 2) * (G1 * Bm).trace())
print("(b) d deps S_D (exact)                    :", dSd)
print("    closed form Tr(G1 B G1 P) - 1/2 Tr(G1 B) :", closed)
print("    residual                                :", sp.simplify(dSd - closed))
# (c) nonzero for B = b E11
Bd = Bm.subs({b11: b, b12: 0, b13: 0, b22: 0, b23: 0, b33: 0})
val = sp.simplify(((G1 * Bd * G1 * Pm).trace() - sp.Rational(1, 2) * (G1 * Bd).trace()))
print("(c) B = b E11 :", val, "(nonzero for generic a1)")
# (d) stationarity is linear in B: solve d deps S_D = 0 for b11
dSd_lin = sp.expand(dSd)
sol = sp.solve(sp.Eq(dSd_lin, 0), b11)
print("(d) b11 solving stationarity              :", sol)
print("    residual after substituting solution   :", sp.simplify(dSd_lin.subs(b11, sol[0])))
Boff = Bm.subs({b11: 0, b13: 0, b22: 0, b23: 0, b33: 0, b12: 1})
print("    B = E12+E21 in kernel                  :", sp.simplify((G1 * Boff * G1 * Pm).trace() - sp.Rational(1, 2) * (G1 * Boff).trace()) == 0)
# (e) cone n-structure
print("(e) c(1)=", cn.subs(n, 1), " c'(1)=", sp.diff(cn, n).subs(n, 1),
      " (1/12)(1/n-n) equals (1/12) c(n) :", sp.simplify(sp.Rational(1, 12) * (1 / n - n) - sp.Rational(1, 12) * cn) == 0)
ok4 = (res4a == 0 and sp.simplify(dSd - closed) == 0 and val != 0
       and sp.simplify(dSd_lin.subs(b11, sol[0])) == 0)
print("PASS" if ok4 else "FAIL")

banner("SUMMARY")
print("C1 insertion+measure:", res1 == 0)
print("C2 SD kernel:", ok2a and ok2b and ins == 0)
print("C3 unimodular null directions:", trB == 0 and trad == 0)
print("C4 conical Gaussian: identity exact, generic d deps S_D nonzero, stationarity linear:", ok4)
