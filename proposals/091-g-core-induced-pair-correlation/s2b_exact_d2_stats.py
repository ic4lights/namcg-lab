# s2b_exact_d2_stats.py - exact D=2 statistics for proposal 091 and the 089 density cross-check.
# Run: python -I proposals/091-g-core-induced-pair-correlation/s2b_exact_d2_stats.py
import sympy as sp
u, a, x, g1, g2, T, t = sp.symbols('u a x g1 g2 T t', positive=True)
# ---- (3) separation density f(u) = u^2 (1-u^2)^(a-1) on (0,1): the fixed-trace beta=2 member, D=2
f = u**2*(1-u**2)**(a-1)
Zn = sp.integrate(f, (u, 0, 1))                      # = B(3/2,a)/2
p = f/Zn                                              # density of u = |p1-p2|
Eu = sp.simplify(sp.integrate(u*p, (u, 0, 1)))
Eu2 = sp.simplify(sp.integrate(u**2*p, (u, 0, 1)))
Varp1 = sp.simplify(Eu2/4)                            # p1 = (1 +- u)/2 -> Var(p1) = E[u^2]/4
print("(3a) mode f'(u)=0 root:", sp.solve(sp.Eq(sp.diff(f, u), 0), u), "(interior iff a>1)")
print("(3b) E[u] =", Eu, " ; E[u]*sqrt(a) ->", sp.limit(Eu*sp.sqrt(a), a, sp.oo), " as a -> oo")
print("(3c) Var(p1) at beta=2:", Varp1, " ; claimed 3/(8a+12) equal:", sp.simplify(Varp1 - 3/(8*a+12)) == 0)
print("(3d) at a=1: Var(p1) =", Varp1.subs(a, 1), " ; beta=0 flat Dirichlet(a,a) Var = 1/(4(2a+1)) =",
      (1/(4*(2*a+1))).subs(a, 1))
tail = sp.integrate(p.subs(a, 1), (u, 0, eps))
print("(3e) a=1: P(u<eps) =", sp.simplify(tail), " ; = eps^3:", sp.simplify(tail - eps**3) == 0,
      " ; beta=0 gives", sp.simplify(sp.integrate(sp.Symbol('s', positive=True)*0 + 1*(sp.Symbol('s')*0+1),
      (sp.Symbol('s'), 0, eps))), "(flat)")
# ---- (4) integrated 089 formula cross-check, D=2:  1/( (g1 g2) (x/g1+(1-x)/g2)^2 )
# direct fibre integral of iid Exp(means s^2 g_i) under E_i = T p_i, p_1 = x, p_2 = 1-x:
dens089 = 1/(g1*g2*(x/g1 + (1-x)/g2)**2)
direct = sp.integrate(T*sp.exp(-T*(x/g1 + (1-x)/g2))/(g1*g2), (T, 0, sp.oo))
print("(4a) direct == 089 closed form:", sp.simplify(direct - dens089) == 0)
print("(4b) integrates to 1 over x in (0,1):", sp.simplify(sp.integrate(dens089, (x, 0, 1)) - 1) == 0)
print("(4c) uniform g1=g2=1 gives flat:", sp.simplify(dens089.subs({g1: 1, g2: 1}) - 1) == 0)
# rank-one slot law at uniform variance: |w_i|^2 of iid CN(0,1), D=2: normalized squares = flat
w1, w2 = sp.symbols('w1 w2', positive=True)           # |w_i|^2 ~ Exp(1)
r = w1/(w1+w2)
fflat = sp.integrate(sp.exp(-w1-w2)*sp.sqrt(1)/(sp.sqrt(1)), (w1, 0, sp.oo)).subs(w1, w1)
# Dirichlet(1,1) check: density of r = int_0^inf (t) e^{-t} e^{-t r}... use standard substitution w2=t(1-r)...
t2 = sp.symbols('tau2', positive=True)
jac = t2
fr = sp.simplify(sp.integrate(sp.exp(-t2)*sp.exp(-t2*r)*(t2*r)*0 + sp.exp(-t2)*sp.exp(-t2*r)*jac,
                              (t2, 0, sp.oo)))
print("(4d) D=2 iid-Exp normalized ratio density (should be 1, flat):", sp.simplify(fr),
      " ; == 1:", sp.simplify(fr - 1) == 0)
