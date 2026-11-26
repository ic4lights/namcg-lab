"""028 script 2: identities used for ARBITRARY X^a (not only the background T^a), checked symbolically on a 4-dimensional canonical phase space (q1,q2,p1,p2)
with random polynomial X_a (a=0..3):
 (i)  [D_a,D_b] f = {F_ab, f},  F_ab={X_a,X_b},  D_a={X_a,.}
 (ii) (Gamma^a D_a)^2 = eta^{ab} D_a D_b + (1/2) Gamma^{ab} {F_ab,.}   (Gamma^{ab}=(1/2)[Gamma^a,Gamma^b], real 4x4 Clifford, eta=diag(-1,1,1,1))
 (iii) Euler-Lagrange operator of the ungauge-fixed second variation density
       Lag = 1/4 [ (D_a e_b - D_b e_a)(D^a e^b - D^b e^a) + 2 F^{ab}{e_a,e_b} + 2 mu2 e_a e^a ]  (e_a arbitrary functions)
     equals  (L e)^a,  (L e)_a = -Box e_a + D_a D_b e^b - 2 {F_ab, e^b} + mu2 e_a,  Box = eta^{ab} D_a D_b   (factor: E-L of Lag is (L e)^a)."""
import sympy as sp, random, itertools
from sympy.calculus.euler import euler_equations
random.seed(3)
q1, q2, p1, p2 = sp.symbols('q1 q2 p1 p2')
co = [q1, q2, p1, p2]
def PB(f, g):
    return sp.diff(f, q1)*sp.diff(g, p1) - sp.diff(f, p1)*sp.diff(g, q1) + sp.diff(f, q2)*sp.diff(g, p2) - sp.diff(f, p2)*sp.diff(g, q2)
mons = [q1, q2, p1, p2, q1*q2, q1*p1, q2*p2, p1*p2, q1**2, p2**2, q1*p2, q2*p1, q1**2*q2, p1*p2*q2]
X = [sum(random.randint(-2, 2)*m for m in random.sample(mons, 5)) for _ in range(4)]
eta = sp.diag(-1, 1, 1, 1)
D = lambda a, f: PB(X[a], f)
F = [[PB(X[a], X[b]) for b in range(4)] for a in range(4)]
f = sp.Function('f')(*co)
ok = True
for a in range(4):
    for b in range(4):
        lhs = D(a, D(b, f)) - D(b, D(a, f)); rhs = PB(F[a][b], f)
        ok &= sp.simplify(sp.expand(lhs - rhs)) == 0
print("(i) [D_a,D_b] f = {F_ab,f} for all a,b with random polynomial X:", ok)
# (ii) Dirac square
g0 = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, 1], [-1, 0, 0, 0], [0, -1, 0, 0]])
s1 = sp.Matrix([[0, 1], [1, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]])
from sympy.physics.quantum import TensorProduct as TP
G = [TP(sp.Matrix([[0, 1], [-1, 0]]), sp.eye(2)), TP(s1, sp.eye(2)), TP(s3, s1), TP(s3, s3)]
for a in range(4):
    for b in range(4):
        assert G[a]*G[b] + G[b]*G[a] == 2*eta[a, b]*sp.eye(4)
psi = sp.Matrix([sp.Function('psi%d' % i)(*co) for i in range(4)])
def Dslash(v): return sum((G[a]*v.applyfunc(lambda e: D(a, e)) for a in range(4)), sp.zeros(4, 1))
lhs = Dslash(Dslash(psi))
box = sum((eta[a, a]*psi.applyfunc(lambda e: D(a, D(a, e))) for a in range(4)), sp.zeros(4, 1))
spin = sp.zeros(4, 1)
for a in range(4):
    for b in range(4):
        Gab = (G[a]*G[b] - G[b]*G[a])/2
        spin += Gab*psi.applyfunc(lambda e: PB(F[a][b], e))/2
print("(ii) Dslash^2 = Box + (1/2) Gamma^{ab}{F_ab,.} (G^a lowered consistently: G^a D_a with X_a lower):", sp.simplify((lhs - box - spin).applyfunc(sp.expand)) == sp.zeros(4, 1))
# (iii) Hessian
mu2 = sp.Symbol('mu2')
e = [sp.Function('e%d' % a)(*co) for a in range(4)]     # lower-index components e_a
eu = [eta[a, a]*e[a] for a in range(4)]                  # e^a
Dl = lambda a, h: D(a, h)
# D^a = eta^{aa} D_a
Du = lambda a, h: eta[a, a]*D(a, h)
Fu = lambda a, b: eta[a, a]*eta[b, b]*F[a][b]
Lag = 0
for a in range(4):
    for b in range(4):
        Lag += sp.Rational(1, 4)*(Dl(a, e[b]) - Dl(b, e[a]))*(Du(a, e[b]) - Du(b, e[a]))*eta[b, b]/eta[b, b]
# careful: (D_a e_b - D_b e_a)(D^a e^b - D^b e^a) with e^b = eta^{bb} e_b and D^a = eta^{aa} D_a
Lag = 0
for a in range(4):
    for b in range(4):
        Lag += sp.Rational(1, 4)*(D(a, e[b]) - D(b, e[a]))*eta[a, a]*eta[b, b]*(D(a, e[b]) - D(b, e[a]))
        Lag += sp.Rational(1, 4)*2*Fu(a, b)*PB(e[a], e[b])
    Lag += sp.Rational(1, 4)*2*mu2*eta[a, a]*e[a]**2
eqs = euler_equations(Lag, e, co)
Lop = []
Boxe = lambda h: sum(eta[c, c]*D(c, D(c, h)) for c in range(4))
divE = sum(eta[b, b]*D(b, e[b]) for b in range(4))                       # D_b e^b
res = True
for a in range(4):
    # (L e)_a with lower index, then raise
    La = -Boxe(e[a]) + D(a, divE) - 2*sum(PB(F[a][b], eu[b]) for b in range(4)) + mu2*e[a]
    Lup = eta[a, a]*La
    el = eqs[a].lhs
    res &= sp.simplify(sp.expand(el - Lup)) == 0
    # note: E-L w.r.t. lower e_a is an upper-index object
print("(iii) E-L of the ungauge-fixed second-variation density = (L e)^a with L = -Box + D D - 2{F_ab,.} + mu2 (arbitrary polynomial X):", res)
