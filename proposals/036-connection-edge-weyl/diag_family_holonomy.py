"""Exact (all orders) delta content of the vector bundle curvature and of the metric for the diagonal Poisson family
   Theta^{12} = exp(-l1(x1,x2)),  Theta^{34} = exp(-l2(x1,x2)),   G = diag(e^{2 l1}, e^{2 l1}, e^{2 l2}, e^{2 l2}),  rho = e^{l1+l2}.
Extends 031 smooth_family_deltas.py (same Vassilevich conventions) from l2 = 0 to general l2.
Output: Omega_12 of the vector connection as a polynomial in l1_ij, l2_ij (Hessian entries) and first derivatives, and Riemann components.
For l_i = eps c_i ln r, Hess(l_i) = pi eps c_i delta_ab delta^2 + traceless PV, so the delta part of every Hessian-linear term is its trace part."""
import sympy as sp
x = sp.symbols('x1:5', real=True)
l1 = sp.Function('l1')(x[0], x[1]); l2 = sp.Function('l2')(x[0], x[1])
Th = sp.zeros(4, 4); Th[0,1] = sp.exp(-l1); Th[1,0] = -sp.exp(-l1); Th[2,3] = sp.exp(-l2); Th[3,2] = -sp.exp(-l2)
Ginv = sp.simplify(Th.T*Th); G = sp.simplify(Ginv.inv()); rho = sp.exp(l1+l2)
def christoffel(G, Gi):
    return [[[sp.simplify(sum(Gi[a,d]*(sp.diff(G[d,b],x[c])+sp.diff(G[d,c],x[b])-sp.diff(G[b,c],x[d])) for d in range(4))/2) for c in range(4)] for b in range(4)] for a in range(4)]
Gam = christoffel(G, Ginv)
def riemann(Gam):
    R = {}
    for r in range(4):
        for s in range(4):
            for m in range(4):
                for k in range(4):
                    t = sp.diff(Gam[r][k][s], x[m]) - sp.diff(Gam[r][m][s], x[k])
                    t += sum(Gam[r][m][q]*Gam[q][k][s] - Gam[r][k][q]*Gam[q][m][s] for q in range(4))
                    R[(r,s,m,k)] = sp.simplify(t)
    return R
Rm = riemann(Gam)
Rl = lambda a,b,c,d: sp.simplify(sum(G[a,p]*Rm[(p,b,c,d)] for p in range(4)))
A_s = [sp.simplify(sum(sp.diff(rho*Ginv[m,n], x[m]) for m in range(4))/rho) for n in range(4)]
Av = []
for s in range(4):
    M = sp.zeros(4,4)
    for mu in range(4):
        for nu in range(4):
            M[mu,nu] += 2*sum(Th[r,s]*sp.diff(Th[mu,nu], x[r]) for r in range(4))
        M[mu,mu] += A_s[s]
    Av.append(M)
C = [sum(Ginv[m,q]*Gam[nu][m][q] for m in range(4) for q in range(4)) for nu in range(4)]
om = [sp.simplify(sum((G[s,nu]*(Av[nu] + C[nu]*sp.eye(4)) for nu in range(4)), sp.zeros(4,4))/2) for s in range(4)]
Om12 = sp.simplify(sp.diff(om[1], x[0]) - sp.diff(om[0], x[1]) + om[0]*om[1] - om[1]*om[0])
h = sp.symbols('a11 a12 a22 b11 b12 b22')
a11,a12,a22,b11,b12,b22 = h
rep = {sp.Derivative(l1,(x[0],2)):a11, sp.Derivative(l1,x[0],x[1]):a12, sp.Derivative(l1,(x[1],2)):a22,
       sp.Derivative(l2,(x[0],2)):b11, sp.Derivative(l2,x[0],x[1]):b12, sp.Derivative(l2,(x[1],2)):b22}
Om12h = sp.simplify(Om12.subs(rep))
print('omega_s (vector), s=0,1 (first-derivative only):'); sp.pprint(sp.simplify(om[0])); sp.pprint(sp.simplify(om[1]))
print('Omega_12 (vector) with Hessian symbols a=l1_ij, b=l2_ij:'); sp.pprint(Om12h)
lin = Om12h.applyfunc(lambda e: sp.simplify(sp.expand(e).subs({sp.Derivative(l1,x[0]):0, sp.Derivative(l1,x[1]):0, sp.Derivative(l2,x[0]):0, sp.Derivative(l2,x[1]):0})))
print('Omega_12 Hessian-linear part (first derivatives set to 0):'); sp.pprint(lin)
# delta part: Hess -> trace part:  l_ij -> (1/2) delta_ij Lap l   <=>  l11,l22 -> Lap/2, l12 -> 0.  In units  d_a d_b (eps c ln r) -> pi eps c delta_ab delta^2
La, Lb = sp.symbols('La Lb')   # La = pi*eps*c_a*delta^2 (coefficient of delta_ab in Hess l1), Lb likewise for l2
delta = lin.subs({a11:La, a22:La, a12:0, b11:Lb, b22:Lb, b12:0})
delta = delta.applyfunc(sp.simplify)
print('delta part of Omega_12 (La = pi eps c_a, Lb = pi eps c_b):'); sp.pprint(delta)
# metric deltas  (at l=0 background, Hessian-linear)
z = {sp.Derivative(l1,x[0]):0, sp.Derivative(l1,x[1]):0, sp.Derivative(l2,x[0]):0, sp.Derivative(l2,x[1]):0}
def hl(e):
    return sp.simplify(sp.expand(sp.expand(e).subs(rep).subs(z)).subs({a11:La,a22:La,a12:0,b11:Lb,b22:Lb,b12:0}))
for idx in ((0,1,0,1),(0,2,0,2),(1,2,1,2),(0,3,0,3),(2,3,2,3),(0,2,1,3)):
    print('R_{%d%d%d%d} delta part ->' % tuple(i+1 for i in idx), hl(Rl(*idx)))
