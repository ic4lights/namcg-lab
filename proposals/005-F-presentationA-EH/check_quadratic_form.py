"""
Quadratic (in A) form of the Lambda^2 one-loop density about constant Theta-bar, Presentation A (Poisson limit).
 Theta = Tbar + eps*T,  T^{mn} = Tbar^{mr} d_r A^n - Tbar^{nr} d_r A^m ,  A^m = u^m cos(p.x)   (the linear part of
 the matrix field strength F^{mn}; the {A,A} part only enters through total derivatives, see proposal).
 Computes the theta-average of the O(eps^2) parts of
    Lh   = rho * R[g_rho]            (g_rho,mn = (rho K)^-1, det g_rho = +-1)
    Lx   = rho^2 * Xspin
 with rho=1/Pf(Theta), K^{rs}=eta_{ab}Theta^{ar}Theta^{bs}, Xspin = eta^{rl}eta^{ma}eta^{nb} d_rTheta_{mn} d_lTheta_{ab}.
 All x-dependence is through th = p.x, so d_mu = p_mu d/dth.
 Output: the 4x4 symmetric matrices Mh(p), Mx(p) with  <Lh^(2)> = u^T Mh u, <Lx^(2)> = u^T Mx u, for numeric p.
 Usage: python check_quadratic_form.py s0 a0 b0 p0 p1 p2 p3
"""
import sympy as sp, sys
s0 = sp.Rational(sys.argv[1]); a0 = sp.Rational(sys.argv[2]); b0 = sp.Rational(sys.argv[3])
pv = [sp.Rational(v) for v in sys.argv[4:8]]
eps, th = sp.symbols('eps th')
u = sp.symbols('u0:4')
n = 4
eta = sp.diag(s0, 1, 1, 1); etai = eta.inv()
Tb = sp.zeros(4, 4); Tb[0, 1] = a0; Tb[1, 0] = -a0; Tb[2, 3] = b0; Tb[3, 2] = -b0
A = [u[m]*sp.cos(th) for m in range(n)]
def dth(f): return sp.diff(f, th)
dA = lambda m, k: pv[k]*dth(A[m])            # d_k A^m
T = sp.Matrix(n, n, lambda m, k: sum(Tb[m, r]*dA(k, r) for r in range(n)) - sum(Tb[k, r]*dA(m, r) for r in range(n)))
Th = Tb + eps*T
def trunc(expr, order=2):
    expr = sp.expand(expr)
    return sum(expr.coeff(eps, k)*eps**k for k in range(order + 1))
def mtrunc(M, order=2): return M.applyfunc(lambda e: trunc(e, order))
Pf = Th[0, 1]*Th[2, 3] - Th[0, 2]*Th[1, 3] + Th[0, 3]*Th[1, 2]
Pf0 = a0*b0
assert Pf0 > 0
# dual
def dual(M):
    e = sp.LeviCivita
    return sp.Matrix(n, n, lambda m, k: sum(e(m, k, r, s)*M[r, s] for r in range(n) for s in range(n))/2)
Ts = dual(Th)
# g_rho = (1/Pf) (*Th) eta^-1 (*Th)^T   [lower indices]
num = mtrunc((Ts*etai*Ts.T))
# series for 1/Pf
Pfs = trunc(Pf)
x1 = sp.expand((Pfs - Pf0)/Pf0)
invPf = trunc((1 - x1 + x1**2)/Pf0)
rho = invPf
g = mtrunc(num*invPf)
# check det
g0 = g.subs(eps, 0); g1 = g.applyfunc(lambda e: sp.expand(e).coeff(eps, 1)); g2 = g.applyfunc(lambda e: sp.expand(e).coeff(eps, 2))
g0i = g0.inv()
gi = mtrunc(g0i - eps*g0i*g1*g0i + eps**2*(g0i*g1*g0i*g1*g0i - g0i*g2*g0i))
# check g*gi = 1 to O(eps^2)
chk = mtrunc(g*gi) - sp.eye(n)
assert chk.applyfunc(sp.simplify) == sp.zeros(n, n)
def dmu(f, m): return pv[m]*dth(f)
Gam = [[[trunc(sum(gi[l, d]*(dmu(g[d, b], c) + dmu(g[d, c], b) - dmu(g[b, c], d)) for d in range(n))/2)
         for c in range(n)] for b in range(n)] for l in range(n)]
def Riem(al, be, c, d):
    return trunc(dmu(Gam[al][be][d], c) - dmu(Gam[al][be][c], d)
                 + sum(Gam[al][c][e]*Gam[e][be][d] - Gam[al][d][e]*Gam[e][be][c] for e in range(n)))
Ric = sp.Matrix(n, n, lambda be, d: sum(Riem(al, be, al, d) for al in range(n)))
R = trunc(sum(gi[p, q]*Ric[p, q] for p in range(n) for q in range(n)))
Lh = trunc(rho*R)
# Xspin
Thl = eta*Th*eta
dT = lambda m, k, r: dmu(Thl[m, k], r)
X = trunc(sum(etai[r, l]*etai[m, a]*etai[nn, b]*dT(m, nn, r)*dT(a, b, l)
              for r in range(n) for l in range(n) for m in range(n) for nn in range(n) for a in range(n) for b in range(n)))
Lx = trunc(rho**2*X)
def avg(expr):
    return sp.simplify(sp.integrate(sp.expand(expr), (th, 0, 2*sp.pi))/(2*sp.pi))
out = {}
for name, L in (('Lh', Lh), ('Lx', Lx)):
    L0 = sp.expand(L).coeff(eps, 0); L1 = sp.expand(L).coeff(eps, 1); L2 = sp.expand(L).coeff(eps, 2)
    print(name, " O(eps^0) avg:", avg(L0), "  O(eps^1) avg:", avg(L1))
    q = sp.expand(avg(L2))
    M = sp.Matrix(n, n, lambda i, j: sp.diff(q, u[i], u[j])/2)
    out[name] = M
    print(name, " <L^(2)> = ", q)
    print(name, " M =", M.tolist())
    print(name, " gauge invariance M*p =", (M*sp.Matrix(pv)).T.tolist())
