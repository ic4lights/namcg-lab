"""
Algebraic structure of the Poisson-limit map Theta -> K = Theta^T eta Theta  (G = K^{-1}), four matrix coordinates.
Conventions as in appH Presentation-A paragraph: K^{rs} = Theta^{a r} eta_{ab} Theta^{b s}.
(1) Characteristic polynomial of N = Theta eta in terms of E,B (Theta^{0i}=E_i, Theta^{ij}=eps_{ijk}B_k):
      p(z) = z^4 + (B^2 - E^2) z^2 - (E.B)^2   (Lorentzian eta).   Pf(Theta) = +-(E.B).
(2) S := N^2 has exactly two eigenvalues, each doubly degenerate, hence satisfies a quadratic minimal polynomial:
      S^2 - (tr S / 2) S - (E.B)^2 * 1 = 0   (symbolic check), i.e. the traceless part S0 of S obeys S0^2 = (tr S0^2 / 4) 1.
(3) Jacobian of Theta -> K (6 -> 10): symbolic Gram determinant det(J^T J) is Pf^2 times a polynomial that is positive
    at random points; rank 6 whenever Pf != 0, rank drops at Pf = 0.  (analytic argument in the proposal: kernel of dN -> d(N^2)).
(4) N^2 = -c 1 is impossible for Lorentzian eta and real Theta with c != 0 (constant term of p(z) is -(E.B)^2 <= 0 but c^2 > 0),
    and N^2 = 0 is excluded for invertible N.  In Euclidean signature N^2 = -c 1 is possible (Theta = theta J).
"""
import sympy as sp, random, itertools
random.seed(1)
E = sp.symbols('E1 E2 E3', real=True); B = sp.symbols('B1 B2 B3', real=True)
def Theta_EB(E, B):
    T = sp.zeros(4, 4)
    for i in range(3):
        T[0, i+1] = E[i]; T[i+1, 0] = -E[i]
    T[1, 2] = B[2]; T[2, 1] = -B[2]
    T[2, 3] = B[0]; T[3, 2] = -B[0]
    T[3, 1] = B[1]; T[1, 3] = -B[1]
    return T
Th = Theta_EB(E, B)
eta = sp.diag(-1, 1, 1, 1)
N = Th*eta
z = sp.symbols('z')
cp = sp.expand((z*sp.eye(4) - N).det())
E2 = sum(e**2 for e in E); B2 = sum(b**2 for b in B); EB = sum(e*b for e, b in zip(E, B))
target = z**4 + (B2 - E2)*z**2 - EB**2
print("(1) char poly of N=Theta eta equals z^4+(B^2-E^2) z^2-(E.B)^2 :", sp.expand(cp - target) == 0)
Pf = Th[0, 1]*Th[2, 3] - Th[0, 2]*Th[1, 3] + Th[0, 3]*Th[1, 2]
print("    Pf(Theta)^2 - (E.B)^2 =", sp.expand(Pf**2 - EB**2))

# (2) S = N^2 minimal polynomial
S = N*N
a = sp.symbols('a')
trS = sp.expand(S.trace())
detS = sp.expand(S.det())            # = (zeta1 zeta2)^2 = (E.B)^4
Q = sp.expand(S*S - (trS/2)*S - EB**2*sp.eye(4))
print("(2) S^2 - (trS/2) S - (E.B)^2 1 == 0 :", Q == sp.zeros(4, 4), "; det S == (E.B)^4 :", sp.expand(detS - EB**4) == 0)
S0 = S - (trS/4)*sp.eye(4)
R = sp.expand(S0*S0 - (sp.expand((S0*S0).trace())/4)*sp.eye(4))
print("    traceless part obeys S0^2 = (tr S0^2/4) 1 :", R == sp.zeros(4, 4))

# (2b) same relation in terms of K eta and of S_rho = g_rho^{mu nu} eta_{nu lambda} = rho K eta
Kk = Th.T*eta*Th
KE = Kk*eta
rel = sp.expand(KE*KE - (KE.trace()/2)*KE - Pf**2*sp.eye(4))
print("(2b) (K eta)^2 - (tr(K eta)/2) K eta - Pf^2 1 == 0 :", rel == sp.zeros(4, 4), "; K eta = -N^2 :", sp.expand(KE + N*N) == sp.zeros(4, 4))
print("     hence S_rho = rho K eta (rho = 1/|Pf|) obeys S_rho^2 - (tr S_rho/2) S_rho = 1 (and det S_rho = -1 for Lorentzian eta).")

# (3) Jacobian rank / Gram determinant (partially symbolic: two symbols, four random integer entries)
iu = [(i, j) for i in range(4) for j in range(i, 4)]
def Tmat(t):
    return sp.Matrix([[0, t[0], t[1], t[2]], [-t[0], 0, t[3], t[4]], [-t[1], -t[3], 0, t[5]], [-t[2], -t[4], -t[5], 0]])
x, y = sp.symbols('x y')
for name, et in (("Lorentz", sp.diag(-1, 1, 1, 1)), ("Euclid", sp.eye(4))):
    for trial in range(3):
        r = [random.randint(-4, 4) for _ in range(4)]
        t = [x, r[0], r[1], r[2], r[3], y]               # t01=x, t02,t03,t12,t13 random, t23=y
        th6 = sp.symbols('s0:6')
        Ts = Tmat(th6)
        Ks = Ts.T*et*Ts
        vec = sp.Matrix([Ks[i, j] for (i, j) in iu])
        Jm = vec.jacobian(sp.Matrix(th6)).subs(dict(zip(th6, t)))
        gram = sp.factor((Jm.T*Jm).det())
        Pf_ = t[0]*t[5] - t[1]*t[4] + t[2]*t[3]
        quo, rem = sp.div(sp.Poly(sp.expand(gram), x, y), sp.Poly(sp.expand(Pf_**2), x, y))
        print("(3)", name, "trial", trial, ": Pf^2 divides Gram det:", rem.is_zero, "; quotient total degree", quo.total_degree())
    ok = 0; tot = 0
    for _ in range(40):
        pt = [random.randint(-6, 6) for _ in range(6)]
        Tn = Tmat(pt); Pv = Tn[0, 1]*Tn[2, 3] - Tn[0, 2]*Tn[1, 3] + Tn[0, 3]*Tn[1, 2]
        Ks = Tmat(th6).T*et*Tmat(th6)
        Jn = sp.Matrix([Ks[i, j] for (i, j) in iu]).jacobian(sp.Matrix(th6)).subs(dict(zip(th6, pt)))
        rk = Jn.rank()
        if Pv != 0:
            tot += 1; ok += (rk == 6)
    print("    random integer points with Pf != 0:", tot, " of which rank 6:", ok)
    pt0 = [1, 0, 0, 0, 0, 0]
    Ks = Tmat(th6).T*et*Tmat(th6)
    Jn = sp.Matrix([Ks[i, j] for (i, j) in iu]).jacobian(sp.Matrix(th6)).subs(dict(zip(th6, pt0)))
    print("    rank at the Pf=0 point (only Theta^{01} != 0):", Jn.rank())

# (4) N^2 = -c 1
print("(4) constant term of p(z) is -(E.B)^2 <= 0, while (z^2+c)^2 has constant term c^2 > 0 for c != 0 real;")
print("    c = 0 would give N^2 = 0 but det N = (E.B)^2 != 0 when Pf != 0.  Hence no real nondegenerate Theta has Theta eta Theta eta = -c 1, c != 0 (Lorentzian eta).")
# direct numerical confirmation: minimise ||N^2 + c 1||^2 over Theta at fixed c = +-1, +-0.1, with several random starts
import numpy as np
from scipy.optimize import minimize
def Tn(v):
    T = np.zeros((4, 4)); k = 0
    for i in range(4):
        for j in range(i+1, 4):
            T[i, j] = v[k]; T[j, i] = -v[k]; k += 1
    return T
rng = np.random.default_rng(0)
for label, etan in (("Lorentzian", np.diag([-1., 1, 1, 1])), ("Euclidean", np.eye(4))):
    for cval in (1.0, -1.0, 0.1, -0.1):
        best = 1e9
        for _ in range(60):
            v0 = rng.normal(size=6)
            res = minimize(lambda v: np.sum(((Tn(v)@etan)@(Tn(v)@etan) + cval*np.eye(4))**2), v0, method='BFGS')
            best = min(best, res.fun)
        print("    %s eta, c = %5.2f: min_Theta ||N^2 + c 1||^2 = %.3e" % (label, cval, best))
