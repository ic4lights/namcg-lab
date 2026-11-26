"""S8 (exact, sympy; round 2).  The by-hand statements of the gap paragraph of appH_insert_r2.tex, in the r2 notation
(tilt angle phi, class shift varpi), from the displayed characteristic equation alone:
 (a) -(q_par + varpi k_par)^2 = q0^2 - p^2 + 2 varpi (q0 - p cos phi) + varpi^2 sin^2 phi, with q_par = (q0, 0, p, 0),
     k_par = (1, 0, cos phi, 0), signature (-,+,+,+); and the constant term equals -varpi^2 k_par^2 = varpi^2 sin^2 phi;
 (b) at p = 0 the roots are q0 = -varpi (1 -+ cos phi); their product is varpi^2 sin^2 phi (> 0 for real varpi != 0,
     sin phi != 0: same sign);
 (c) at q0 = 0 the equation is p^2 + (2 varpi cos phi + kappa l) p - varpi^2 sin^2 phi = 0; product of the p-roots is
     -varpi^2 sin^2 phi (< 0 for real varpi != 0, sin phi != 0: exactly one p > 0);
 (d) the r1 -> r2 renaming s = sin phi, c = cos phi, Lambda = varpi maps the r1 display onto the r2 display.
Run: python -I -B s8_root_algebra_r2.py"""
import sympy as sp

q0, p, ph, kap, l = sp.symbols('q0 p phi kappa l', real=True)
w = sp.Symbol('varpi')
eta = sp.diag(-1, 1, 1, 1)
qpar = sp.Matrix([q0, 0, p, 0]); kpar = sp.Matrix([1, 0, sp.cos(ph), 0])
sq = lambda v: (v.T * eta * v)[0]
lhs = -sq(qpar + w * kpar)
rhs = q0**2 - p**2 + 2 * w * (q0 - p * sp.cos(ph)) + w**2 * sp.sin(ph)**2
print("(a) -(q_par+varpi k_par)^2 - display LHS =", sp.simplify(sp.expand(lhs - rhs)))
print("    -varpi^2 k_par^2 - varpi^2 sin^2 phi =", sp.simplify(-w**2 * sq(kpar) - w**2 * sp.sin(ph)**2))
eq = rhs - kap * p * l
r = sp.solve(eq.subs(p, 0), q0)
print("(b) p = 0 roots:", [sp.simplify(x) for x in r],
      "; expected -varpi(1-+cos):", sp.simplify(sp.expand(sp.prod([q0 - x for x in r]) - (q0 + w * (1 - sp.cos(ph))) * (q0 + w * (1 + sp.cos(ph))))) == 0)
print("    product of p = 0 roots - varpi^2 sin^2 phi =", sp.simplify(sp.prod(r) - w**2 * sp.sin(ph)**2))
e0 = sp.expand(-eq.subs(q0, 0))
target = p**2 + (2 * w * sp.cos(ph) + kap * l) * p - w**2 * sp.sin(ph)**2
print("(c) -(equation at q0 = 0) - [p^2 + (2 varpi cos + kappa l) p - varpi^2 sin^2] =", sp.simplify(e0 - target))
P = sp.Poly(target, p)
print("    product of p-roots =", sp.simplify(P.all_coeffs()[2] / P.all_coeffs()[0]))
s, c, L = sp.symbols('s c Lambda')
r1 = q0**2 - p**2 + 2 * L * (q0 - c * p) + s**2 * L**2
print("(d) r1 display under s=sin, c=cos, Lambda=varpi minus r2 display =",
      sp.simplify(r1.subs({s: sp.sin(ph), c: sp.cos(ph), L: w}) - rhs))
