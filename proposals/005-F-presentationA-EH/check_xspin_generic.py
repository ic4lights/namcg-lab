"""
Generic nondegenerate Poisson bivector via Darboux pushforward:
  x^mu = phi^mu(y) (random polynomial, near identity), Theta^{mu nu}(x) = Theta0^{ab} d_a x^mu d_b x^nu,
  Theta0 constant block (1 in 01 and 23).  x-derivatives: d/dx^m = (J^{-1})^a_m d/dy^a,  J^m_a = d x^m/d y^a.
Compares  Xspin = eta^{rl} eta^{ma} eta^{nb} d_r Theta_{mn} d_l Theta_{ab}  with  Y = K^{mn} d_m ln(rho) d_n ln(rho),
rho = 1/|Pf Theta|, K^{rs}=eta_{ab}Theta^{ar}Theta^{bs}.  (Block family: X = 2Y.)
Also checks Jacobi (the pushforward guarantees it) and Liouville numerically.
"""
import sympy as sp, random
random.seed(3)
y = sp.symbols('y0:4')
eta = sp.diag(-1, 1, 1, 1)
Th0 = sp.zeros(4, 4); Th0[0, 1] = 1; Th0[1, 0] = -1; Th0[2, 3] = 1; Th0[3, 2] = -1
def rnd(): return sp.Rational(random.randint(-3, 3), 10)
phi = []
for m in range(4):
    expr = y[m]
    for i in range(4):
        for j in range(i, 4):
            expr += rnd()*y[i]*y[j]
    for i in range(4):
        expr += rnd()*y[i]**2*y[(i+1) % 4]
    phi.append(expr)
J = sp.Matrix(4, 4, lambda m, a: sp.diff(phi[m], y[a]))
Th = J*Th0*J.T
pt = {y[i]: sp.Rational(random.randint(-2, 2), 10) for i in range(4)}
Jp = J.subs(pt); Ji = Jp.inv()
def dx(f, m):  # d f / d x^m at the point, f a function of y
    return sum(Ji[a, m]*sp.diff(f, y[a]) for a in range(4)).subs(pt)
Thl = eta*Th*eta
n = 4
Thp = Th.subs(pt)
K = Thp.T*eta*Thp
Pf = (Th[0, 1]*Th[2, 3] - Th[0, 2]*Th[1, 3] + Th[0, 3]*Th[1, 2])
lnrho = -sp.log(sp.Abs(Pf))
Pf_sign = sp.sign(Pf.subs(pt))
lnrho = -sp.log(Pf*Pf_sign)
dlnr = [dx(lnrho, m) for m in range(n)]
Y = sum(K[m, k]*dlnr[m]*dlnr[k] for m in range(n) for k in range(n))
etai = eta.inv()
X = sum(etai[r, l]*etai[m, a]*etai[nn, b]*dx(Thl[m, nn], r)*dx(Thl[a, b], l)
        for r in range(n) for l in range(n) for m in range(n) for nn in range(n) for a in range(n) for b in range(n))
# Liouville  d_m (rho Theta^{m n}) = 0
rho = sp.exp(lnrho)
liou = [sum(dx(rho*Th[m, k], m) for m in range(n)) for k in range(n)]
print("Liouville (numeric):", [sp.N(l, 8) for l in liou])
print("X  =", sp.N(X, 10))
print("2Y =", sp.N(2*Y, 10))
print("X - 2Y =", sp.N(X - 2*Y, 10))
