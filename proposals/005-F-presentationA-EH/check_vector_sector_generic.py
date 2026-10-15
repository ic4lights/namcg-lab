"""
Generic (non-block) check of the Presentation-A vector/ghost sector formulas via a Darboux pushforward, evaluated at a rational point.
  x^mu = phi^mu(y), J^mu_c = d phi^mu/d y^c (lower triangular), Theta0 = block (1 on 01, 1 on 23),
  Theta^{mu nu}(x) = J Theta0 J^T,  Pf Theta = det J,  rho = 1/det J,   d/dx^m = (J^{-1})^c_m d/dy^c,   rho d^4x = d^4y.
  G_{cd} (y-tensor) = (Theta0^T (J^T eta J) Theta0)^{-1},  sqrt|G_y| = rho.   eta = diag(-1,1,1,1).
Checks:
 (i)  Euler-Lagrange operator of L2 = 1/4 F1^2 + 1/2 Theta_{mn}{A^m,A^n} + 1/2 (D.A)^2  (measure d^4y) equals eta*(O A),
      O A^mu = -L A^mu - 2 eta^{mu m} B^s_{mn} d_s A^n,  L f = d_c(K_y^{cd} d_d f),  B^s_{mn} d_s = Theta0^{bc} d_b Theta_{mn} d_c  (= {Theta_{mn}, .}),
      tested on random polynomial fields A^mu(y) at the point.
 (ii) -D^2 + E = O on random polynomial V^mu(y), with omega^c = -1/2 G^{cd} d_d ln rho + B^c, E = div omega + omega.omega.
 (iii) scalars:  R_G/6 - E_s = R[g_rho]/(6 rho)   and   4 R_G/6 - tr E = (4/6) R[g_rho]/rho + Xspin,  g_rho = G/rho,
       Xspin = eta^{rl} eta^{ma} eta^{nb} d_{x^r}Theta_{mn} d_{x^l}Theta_{ab}.
"""
import sympy as sp, random
random.seed(11)
y = sp.symbols('y0:4'); n = 4
eta = sp.diag(-1, 1, 1, 1); etai = eta.inv()
Th0 = sp.zeros(4, 4); Th0[0, 1] = 1; Th0[1, 0] = -1; Th0[2, 3] = 1; Th0[3, 2] = -1
Th0i = Th0.inv()
c = [sp.Rational(random.randint(-4, 4), 10) for _ in range(8)]
phi = [y[0] + c[0]*y[0]**2,
       y[1] + c[1]*y[0]*y[1] + c[2]*y[0]**2,
       y[2] + c[3]*y[1]**2 + c[4]*y[0]*y[2],
       y[3] + c[5]*y[2]*y[3] + c[6]*y[0]*y[1] + c[7]*y[3]**2]
J = sp.Matrix(n, n, lambda m, a: sp.diff(phi[m], y[a]))
Ji = J.inv()
detJ = sp.expand(J.det())
rho = 1/detJ
pt = {y[0]: sp.Rational(1, 7), y[1]: sp.Rational(-1, 5), y[2]: sp.Rational(1, 6), y[3]: sp.Rational(1, 9)}
assert detJ.subs(pt) > 0
Thx = (J*Th0*J.T).applyfunc(sp.expand); Thl = eta*Thx*eta
Kx = (Thx.T*eta*Thx)
Ky = Ji*Kx*Ji.T                       # K_y^{cd}  = G^{cd}
G = Th0i*(Ji*etai*Ji.T)*Th0i.T          # = (Theta0^T h Theta0)^{-1}, h = J^T eta J
chk = (Ky*G).subs(pt)
print("K_y * G = 1 at pt:", sp.simplify(chk - sp.eye(4)) == sp.zeros(4, 4))
Gi = Ky
sqrtG = rho                            # sqrt|det G_y| = 1/|det J|  (shown in the docstring)
print("det G_y at pt vs -rho^2:", sp.simplify(G.det().subs(pt) + rho.subs(pt)**2))
def PBy(f, g): return sum(Th0[a, b]*sp.diff(f, y[a])*sp.diff(g, y[b]) for a in range(n) for b in range(n))
Dm = lambda m, f: PBy(phi[m], f)
Dl = lambda m, f: sum(eta[m, k]*Dm(k, f) for k in range(n))
def rpoly(deg=3):
    mons = [sp.Integer(1)] + list(y) + [y[i]*y[j] for i in range(4) for j in range(i, 4)] + [y[i]*y[j]*y[k] for i in range(4) for j in range(i, 4) for k in range(j, 4)]
    return sum(sp.Rational(random.randint(-3, 3), 2)*m for m in mons)
Af = [sp.Function('A%d' % i)(*y) for i in range(n)]
F1 = sp.Matrix(n, n, lambda m, k: Dm(m, Af[k]) - Dm(k, Af[m])); F1l = eta*F1*eta
FF = sum(F1[m, k]*F1l[m, k] for m in range(n) for k in range(n))
spin = sum(Thl[m, k]*PBy(Af[m], Af[k]) for m in range(n) for k in range(n))
divA = sum(Dl(m, Af[m]) for m in range(n))
L2 = FF/4 + spin/2 + divA**2/2
from sympy.calculus.euler import euler_equations
eqs = euler_equations(L2, Af, y)
def Lop(f): return sum(sp.diff(Ky[a, b]*sp.diff(f, y[b]), y[a]) for a in range(n) for b in range(n))
def Bd(m, nn, f): return sum(Th0[b, cc]*sp.diff(Thl[m, nn], y[b])*sp.diff(f, y[cc]) for cc in range(n) for b in range(n))
def OA(mu, fields): return -Lop(fields[mu]) - 2*sum(etai[mu, m]*Bd(m, nn, fields[nn]) for m in range(n) for nn in range(n))
Ap = [rpoly() for _ in range(n)]
subsA = {Af[i]: Ap[i] for i in range(n)}
for nn in range(n):
    el = (eqs[nn].lhs - eqs[nn].rhs).subs(subsA).doit().subs(pt)
    target = sum(eta[nn, m]*OA(m, Ap) for m in range(n)).subs(pt)
    print("(i) comp", nn, ": EL - eta*O A =", sp.nsimplify(sp.simplify(el - target)), "   (EL = %s)" % sp.N(el, 8))
# Laplace form data
def Gamma(l, a, b): return sum(Gi[l, d]*(sp.diff(G[d, a], y[b]) + sp.diff(G[d, b], y[a]) - sp.diff(G[a, b], y[d])) for d in range(n))/2
Gam = [[[Gamma(l, a, b) for b in range(n)] for a in range(n)] for l in range(n)]
lnr = sp.log(rho)
Bup = [sp.Matrix(n, n, lambda m, nn, cc=cc: sum(etai[m, k]*Th0[b, cc]*sp.diff(Thl[k, nn], y[b]) for k in range(n) for b in range(n))) for cc in range(n)]
omup = [-sp.Rational(1, 2)*sum(Gi[cc, t]*sp.diff(lnr, y[t]) for t in range(n))*sp.eye(n) + Bup[cc] for cc in range(n)]
omlo = [sum((G[cc, t]*omup[t] for t in range(n)), sp.zeros(n, n)) for cc in range(n)]
def divup(V): return sum((sp.diff(sqrtG*V[cc], y[cc]) for cc in range(n)), sp.zeros(n, n))/sqrtG
Emat = divup(omup) + sum((omup[cc]*omlo[cc] for cc in range(n)), sp.zeros(n, n))
Vp = sp.Matrix([rpoly() for _ in range(n)])
def Dsig(cc, W): return W.diff(y[cc]) + omlo[cc]*W
def D2(W):
    out = sp.zeros(n, 1)
    for r in range(n):
        for s in range(n):
            out += Gi[r, s]*(Dsig(r, Dsig(s, W)) - sum((Gam[l][r][s]*Dsig(l, W) for l in range(n)), sp.zeros(n, 1)))
    return out
lhs = (-D2(Vp) + Emat*Vp).subs(pt)
rhs = sp.Matrix([OA(mu, list(Vp)) for mu in range(n)]).subs(pt)
print("(ii) -D^2 V + E V - O V at pt:", [sp.nsimplify(sp.simplify(e)) for e in (lhs - rhs)])
def Rscalar(g):
    gi_ = g.inv()
    Gm = [[[sum(gi_[l, d]*(sp.diff(g[d, b], y[cc]) + sp.diff(g[d, cc], y[b]) - sp.diff(g[b, cc], y[d])) for d in range(n))/2
            for cc in range(n)] for b in range(n)] for l in range(n)]
    def Riem(al, be, cc, d):
        return (sp.diff(Gm[al][be][d], y[cc]) - sp.diff(Gm[al][be][cc], y[d])
                + sum(Gm[al][cc][e]*Gm[e][be][d] - Gm[al][d][e]*Gm[e][be][cc] for e in range(n)))
    Ric = sp.Matrix(n, n, lambda be, d: sum(Riem(al, be, al, d) for al in range(n)))
    return sum(gi_[p, q]*Ric[p, q] for p in range(n) for q in range(n))
RG = Rscalar(G)
Rg = Rscalar(G/rho)
trE = Emat.trace()
Es = (-sp.Rational(1, 2)*sum(sp.diff(sqrtG*sum(Gi[cc, t]*sp.diff(lnr, y[t]) for t in range(n)), y[cc]) for cc in range(n))/sqrtG
      + sp.Rational(1, 4)*sum(Gi[cc, t]*sp.diff(lnr, y[cc])*sp.diff(lnr, y[t]) for cc in range(n) for t in range(n)))
dx = lambda f, r: sum(Ji[cc, r]*sp.diff(f, y[cc]) for cc in range(n))
Xs = sum(etai[r, l]*etai[m, a]*etai[nn, b]*dx(Thl[m, nn], r)*dx(Thl[a, b], l)
         for r in range(n) for l in range(n) for m in range(n) for nn in range(n) for a in range(n) for b in range(n))
val = lambda e: sp.N(e.subs(pt), 15)
print("(iii-a) scalar:  R_G/6 - E_s - R[g_rho]/(6 rho)               =", val((RG/6 - Es) - Rg/(6*rho)))
print("(iii-b) vector:  4R_G/6 - trE - (4/6)R[g_rho]/rho - Xspin     =", val((4*RG/6 - trE) - sp.Rational(4, 6)*Rg/rho - Xs))
print("   magnitudes: R_G/6 =", val(RG/6), " trE =", val(trE), " Xspin =", val(Xs), " (4/6)R[g_rho]/rho =", val(sp.Rational(4, 6)*Rg/rho))
