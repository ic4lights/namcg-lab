# s2b_exact_d2_stats_v2.py - corrected (4d): D=2 iid-Exp normalized ratio is exactly flat.
# Run: python -I proposals/091-g-core-induced-pair-correlation/s2b_exact_d2_stats_v2.py
# Parts (3) and (4a-c) are identical to s2b_exact_d2_stats.py; (4d) fixed (substitution w1=r*t, w2=(1-r)*t).
import sympy as sp
u, a, x, g1, g2, T, eps, r, t2 = sp.symbols('u a x g1 g2 T eps r tau2', positive=True)
f = u**2*(1-u**2)**(a-1)
Zn = sp.integrate(f, (u, 0, 1))
p = f/Zn
Eu = sp.simplify(sp.integrate(u*p, (u, 0, 1)))
Eu2 = sp.simplify(sp.integrate(u**2*p, (u, 0, 1)))
Varp1 = sp.simplify(Eu2/4)
print("(3a) mode root:", sp.solve(sp.Eq(sp.diff(f, u), 0), u), "(interior iff a>1)")
print("(3b) E[u] =", Eu, " ; lim E[u]*sqrt(a) =", sp.limit(Eu*sp.sqrt(a), a, sp.oo))
print("(3c) Var(p1) beta=2:", Varp1, " ; == 3/(8a+12):", sp.simplify(Varp1 - 3/(8*a+12)) == 0)
print("(3d) a=1: Var(p1) =", Varp1.subs(a, 1), " ; beta=0 flat member 1/(4(2a+1)) at a=1:",
      sp.Rational(1, 12))
tail = sp.integrate(p.subs(a, 1), (u, 0, eps))
print("(3e) a=1: P(u<eps) =", sp.simplify(tail), " ; == eps^3:", sp.simplify(tail - eps**3) == 0)
dens089 = 1/(g1*g2*(x/g1 + (1-x)/g2)**2)
direct = sp.integrate(T*sp.exp(-T*(x/g1 + (1-x)/g2))/(g1*g2), (T, 0, sp.oo))
print("(4a) direct == 089 closed form:", sp.simplify(direct - dens089) == 0)
print("(4b) integrates to 1:", sp.simplify(sp.integrate(dens089, (x, 0, 1)) - 1) == 0)
print("(4c) uniform g=1 gives flat:", sp.simplify(dens089.subs({g1: 1, g2: 1}) - 1) == 0)
fr = sp.simplify(sp.integrate(sp.exp(-t2)*t2, (t2, 0, sp.oo)))
print("(4d) D=2 iid-Exp normalized-ratio density (flat == 1):", fr, " ; == 1:", fr == 1)
