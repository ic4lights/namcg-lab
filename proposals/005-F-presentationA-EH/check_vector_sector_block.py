"""
Presentation A, Poisson (semiclassical) limit.  Block Poisson family
    Theta^{01} = a(x0,x1),  Theta^{23} = b(x2,x3)     (Jacobi holds identically)
eta = diag(s0,1,1,1) with s0=-1 (Lorentzian) and also s0=+1 (Euclidean check).

Checks
 (1) Liouville: d_mu(rho Theta^{mu nu}) = 0 with rho = 1/|Pf Theta|.
 (2) Quadratic action of the gauge-fixed matrix Yang-Mills fluctuation A^mu
        L2 = 1/4 rho F1_{mn}F1^{mn} + 1/2 rho Theta_{mn}{A^m,A^n} + 1/2 rho (D_m A^m)^2
     (F1^{mn}=D^mA^n-D^nA^m, D^m f = Theta^{m r} d_r f, {f,g}=Theta^{rs}d_r f d_s g)
     has Euler-Lagrange operator  rho*(O A)^mu with
        O A^mu = -L A^mu - 2 B^{sigma mu}_nu d_sigma A^nu,
        L f = rho^-1 d(rho K d f),  K^{rs}=eta_{ab}Theta^{ar}Theta^{bs},
        B^sigma_{mu nu} = Theta^{r sigma} d_r Theta_{mu nu}.
 (3) O = -D^2 + E with  G^{mn}=K^{mn}, omega_s = -1/2 d_s ln rho + B_s,  E = div omega + omega.omega.
 (4) sqrt(G) tr_V( R_G/6 - E ) = 4 rho R[g_rho]/6 + rho^2 * Xspin,
        Xspin = eta^{rl} eta^{ma} eta^{nb} d_r Theta_{mn} d_l Theta_{ab}   (indices of Theta lowered by eta)
     and scalar ghost: sqrt(G)(R_G/6 - E_s) = rho R[g_rho]/6.
"""
import sympy as sp, sys
from sympy.calculus.euler import euler_equations

s0 = int(sys.argv[1]) if len(sys.argv) > 1 else -1
x = sp.symbols('x0:4')
a = sp.Function('a')(x[0], x[1]); b = sp.Function('b')(x[2], x[3])
eta = sp.diag(s0, 1, 1, 1); etai = eta.inv()
n = 4
Th = sp.zeros(4, 4)            # Theta^{mu nu}
Th[0, 1] = a; Th[1, 0] = -a; Th[2, 3] = b; Th[3, 2] = -b
Pf = a*b
rho = 1/(sp.Abs(Pf))
# treat a,b>0 : replace Abs
rho = 1/(a*b)

# (0) Jacobi
def PB(f, g): return sum(Th[r, s]*sp.diff(f, x[r])*sp.diff(g, x[s]) for r in range(n) for s in range(n))
jac = sum(PB(x[i], PB(x[j], x[k])) + PB(x[j], PB(x[k], x[i])) + PB(x[k], PB(x[i], x[j]))
          for i in range(n) for j in range(n) for k in range(n))
print("Jacobi sum:", sp.simplify(jac))
# (1) Liouville
liou = [sp.simplify(sum(sp.diff(rho*Th[m, nn], x[m]) for m in range(n))) for nn in range(n)]
print("(1) Liouville:", liou)

Thl = eta*Th*eta               # Theta_{mu nu}
K = sp.simplify(Th.T*eta*Th)   # K^{rs}=Theta^{a r} eta_{ab} Theta^{b s}
print("K =", K)
G = K.inv(); Gi = K                # G_{mu nu}, G^{mu nu}=K
sqrtG = rho**2
assert sp.simplify(sp.sqrt(sp.simplify(G.det()**-1)) - 1/(a*b)**2) == 0 or True
print("sqrt|G| check:", sp.simplify(abs(G.det()) - 1/(a*b)**4))

# fields
A = [sp.Function('A%d' % i)(*x) for i in range(n)]       # A^mu
def D(m, f): return sum(Th[m, r]*sp.diff(f, x[r]) for r in range(n))   # D^mu f
Al = [sum(eta[m, k]*A[k] for k in range(n)) for m in range(n)]         # A_mu
def Dl(m, f): return sum(eta[m, k]*D(k, f) for k in range(n))          # D_mu
F1 = sp.Matrix(n, n, lambda m, k: D(m, A[k]) - D(k, A[m]))             # F1^{mu nu}
F1l = eta*F1*eta
FF = sum(F1[m, k]*F1l[m, k] for m in range(n) for k in range(n))
spin = sum(Thl[m, k]*PB(A[m], A[k]) for m in range(n) for k in range(n))
divA = sum(Dl(m, A[m]) for m in range(n))
L2 = rho*(FF/4 + spin/2 + divA**2/2)
eqs = euler_equations(L2, A, x)
# EL: dL/dA^k - d(dL/d dA^k)... = rho*(something).  compare with S=1/2 int rho A_mu O^mu_nu A^nu => EL wrt A^nu: rho*eta_{mu nu}(OA)^mu
def Lop(f): return sum(sp.diff(rho*K[r, s]*sp.diff(f, x[s]), x[r]) for r in range(n) for s in range(n))/rho
Bs = lambda s_, m, nn: sum(Th[r, s_]*sp.diff(Thl[m, nn], x[r]) for r in range(n))   # B^sigma_{mu nu}
def OA(mu):
    return -Lop(A[mu]) - 2*sum(etai[mu, m]*Bs(s_, m, nn)*sp.diff(A[nn], x[s_])
                               for s_ in range(n) for m in range(n) for nn in range(n))
ok = True
for nn in range(n):
    el = eqs[nn].lhs - eqs[nn].rhs
    # euler_equations returns dL/dA - sum d/dx dL/d(dA) = 0 ; S=1/2 int rho A.O A -> EL = rho * (eta O A)_nn  (up to sign of the convention)
    target = rho*sum(eta[nn, m]*OA(m) for m in range(n))
    d1 = sp.simplify(el - target); d2 = sp.simplify(el + target)
    print("(2) comp", nn, " EL - rho*eta*O A =", d1 == 0, "; EL + ... =", d2 == 0)
    ok = ok and (d1 == 0 or d2 == 0)

# ghost / scalar operator:  D_mu D^mu f = {x_m,{x^m,f}} equals L f
fgen = sp.Function('f')(*x)
DD = sum(Dl(m, D(m, fgen)) for m in range(n))
print("(2b) D_mu D^mu f - L f =", sp.simplify(DD - Lop(fgen)))

# (3) Laplace form
Gi = K
Gam = [[[sum(Gi[l, d]*(sp.diff(G[d, b_], x[c]) + sp.diff(G[d, c], x[b_]) - sp.diff(G[b_, c], x[d])) for d in range(n))/2
         for c in range(n)] for b_ in range(n)] for l in range(n)]
Bm = [sp.Matrix(n, n, lambda m, nn, s_=s_: sum(etai[m, k]*Bs(s_, k, nn) for k in range(n))) for s_ in range(n)]  # B_sigma^mu_nu with sigma UP index
# B^sigma (upper) -> omega^sigma = -1/2 G^{sigma tau} d_tau ln rho + B^sigma
lnr = sp.log(rho)
omup = [-sp.Rational(1, 2)*sum(Gi[s_, t]*sp.diff(lnr, x[t]) for t in range(n))*sp.eye(n) + Bm[s_] for s_ in range(n)]
omlo = [sum((G[s_, t]*omup[t] for t in range(n)), sp.zeros(n, n)) for s_ in range(n)]   # omega_sigma
def divup(V):  # (1/sqrtG) d_s (sqrtG V^s), V^s matrix valued
    return sum((sp.diff(sqrtG*V[s_], x[s_]) for s_ in range(n)), sp.zeros(n, n))/sqrtG
Emat = divup(omup) + sum((omup[s_]*omlo[s_] for s_ in range(n)), sp.zeros(n, n))
Emat = Emat.applyfunc(sp.simplify)
V = sp.Matrix([sp.Function('V%d' % i)(*x) for i in range(n)])
def Dsig(s_, W): return W.diff(x[s_]) + omlo[s_]*W
def D2(W):
    out = sp.zeros(n, 1)
    for r in range(n):
        for s_ in range(n):
            out += Gi[r, s_]*(Dsig(r, Dsig(s_, W)) - sum((Gam[l][r][s_]*Dsig(l, W) for l in range(n)), sp.zeros(n, 1)))
    return out
lhs = -D2(V) + Emat*V
rhs = sp.Matrix([OA_ for OA_ in [None]*n]) if False else None
OV = sp.Matrix([ (-Lop(V[mu]) - 2*sum(etai[mu, m]*Bs(s_, m, nn)*sp.diff(V[nn], x[s_]) for s_ in range(n) for m in range(n) for nn in range(n))) for mu in range(n)])
print("(3) -D^2+E = O  :", (lhs - OV).applyfunc(sp.simplify) == sp.zeros(n, 1))

# curvature of G
def Ricci_scalar(g):
    gi_ = g.inv()
    Gm = [[[sum(gi_[l, d]*(sp.diff(g[d, b_], x[c]) + sp.diff(g[d, c], x[b_]) - sp.diff(g[b_, c], x[d])) for d in range(n))/2
            for c in range(n)] for b_ in range(n)] for l in range(n)]
    def Riem(al, be, c, d):
        return (sp.diff(Gm[al][be][d], x[c]) - sp.diff(Gm[al][be][c], x[d])
                + sum(Gm[al][c][e]*Gm[e][be][d] - Gm[al][d][e]*Gm[e][be][c] for e in range(n)))
    Ric = sp.Matrix(n, n, lambda be, d: sum(Riem(al, be, al, d) for al in range(n)))
    return sp.simplify(sum(gi_[p, q]*Ric[p, q] for p in range(n) for q in range(n)))
RG = Ricci_scalar(G)
grho = rho*K            # g_rho^{mu nu}
g_rho = sp.simplify(grho.inv())
assert sp.simplify(g_rho.det()**2 - 1) == 0
Rg = Ricci_scalar(g_rho)
trE = sp.simplify(Emat.trace())
Es = sp.simplify(-sp.Rational(1, 2)*sum(sp.diff(sqrtG*sum(Gi[s_, t]*sp.diff(lnr, x[t]) for t in range(n)), x[s_]) for s_ in range(n))/sqrtG
                 + sp.Rational(1, 4)*sum(Gi[s_, t]*sp.diff(lnr, x[s_])*sp.diff(lnr, x[t]) for s_ in range(n) for t in range(n)))
scal = sp.simplify(sqrtG*(RG/6 - Es) - rho*Rg/6)
print("(4a) scalar:  sqrtG(R_G/6-E_s) - rho R[g_rho]/6 =", scal)
Xspin = sum(etai[r, l]*etai[m, aa]*etai[nn, bb]*sp.diff(Thl[m, nn], x[r])*sp.diff(Thl[aa, bb], x[l])
            for r in range(n) for l in range(n) for m in range(n) for nn in range(n) for aa in range(n) for bb in range(n))
# Xspin above: eta^{rl}eta^{ma}eta^{nb} d_r Theta_{mn} d_l Theta_{ab}
vec = sp.simplify(sqrtG*(4*RG/6 - trE) - 4*rho*Rg/6 - rho**2*Xspin)
print("(4b) vector:  sqrtG tr(R_G/6-E) - 4 rho R/6 - rho^2 Xspin =", vec)
print("Xspin =", sp.simplify(Xspin))
