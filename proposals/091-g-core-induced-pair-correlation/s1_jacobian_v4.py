import sympy as sp
# s1 v4 (v1-v3 drafts removed: over-parameterised fibre charts / malformed Jacobian assembly).
# Exact D=2 identities: eigenvalue-fibre Jacobian exponent, 090-type trace-fibre separation at beta=2,
# fixed-trace profile mode and mean separation, exchangeable fixed-trace pair covariance.
# Run: python -I proposals/091-g-core-induced-pair-correlation/s1_jacobian_v4.py  from repo root.
y1, y2, tau = sp.symbols('y1 y2 tau', positive=True)
u = sp.symbols('u', positive=True)
th, phi = sp.symbols('theta phi', real=True)
params = (th, phi, y1, y2)
# (1) 2x2 Hermitian eigenvalue+fibre map, minimal SU(2)-type fibre chart:
# Z = U diag(y1,y2) U^H, U = [[cos, sin e^{i phi}], [-sin e^{-i phi}, cos]]: 4 real params -> 4 real coords
c, s = sp.cos(th), sp.sin(th)
U = sp.Matrix([[c, s*sp.exp(sp.I*phi)], [-s*sp.exp(-sp.I*phi), c]])
Z = U * sp.diag(y1, y2) * U.H
rl = []
for e in (Z[0, 0], Z[0, 1], Z[1, 1]):
    rr, ii = [sp.simplify(sp.expand_complex(t)) for t in e.as_real_imag()]
    rl.append((rr, ii))
assert sp.simplify(rl[0][1]) == 0 and sp.simplify(rl[2][1]) == 0   # z11, z22 real on the chart
coords = (rl[0][0], rl[1][0], rl[1][1], rl[2][0])                   # Re z11, Re z12, Im z12, Re z22
Jm = sp.Matrix([[sp.diff(rd, p) for p in params] for rd in coords])
Js = sp.simplify(Jm.det())
print("(1) det J factored:", sp.factor(Js))
e = sp.symbols('eps', positive=True)
lead = sp.simplify(sp.expand_trig(sp.series(Js.subs(y2, y1 + e), e, 0, 4).removeO()))
d2 = sp.simplify(sp.diff(lead, (e, 2)).subs(e, 0))
print("(1b) y2 = y1+eps: det J vanishes like eps^2 (beta=2 Vandermonde exponent 2):",
      sp.simplify(lead.subs(e, 0)) == 0 and sp.simplify(sp.diff(lead, e).subs(e, 0)) == 0 and d2 != 0,
      " ; d^2/de^2 at 0 =", sp.simplify(d2))
# (2) trace-fibre separation of the Wishart joint eigenvalue density at beta=2 (090 tau-separation, D=2)
a = sp.symbols('a', positive=True)   # a = m - n + 1
joint = (y1*y2)**(a-1)*sp.exp(-(y1+y2)) * (y1-y2)**2
sep = tau**(2*a+1)*sp.exp(-tau)*u**2*(1-u**2)**(a-1)
print("(2) joint(y1,y2)*|jac(y->tau,u)| == sep(tau,u): zero =",
      sp.simplify(sep - joint.subs({y1: tau*(1+u)/2, y2: tau*(1-u)/2})*tau/2) == 0)
# (3) fixed-trace profile marginal, mode, curvature, mean separation
f = u**2*(1-u**2)**(a-1)
print("(3a) int_0^1 u^2 (1-u^2)^(a-1) du =", sp.simplify(sp.integrate(f, (u, 0, 1))), "( = Beta(3/2,a) )")
print("(3b) f'(u)=0 roots:", sp.solve(sp.Eq(sp.simplify(sp.diff(f, u)), 0), u))
curv = sp.simplify(sp.diff(f, (u, 2)).subs(u, 1/sp.sqrt(a)))
print("(3c) u* = 1/sqrt(a); f''(u*) =", curv, "; < 0:", sp.simplify(curv) < 0)
g1 = sp.symbols('g1', positive=True)   # integrable generic range: a = g1 + 1
mu = sp.simplify(sp.integrate(u*u**2*(1-u**2)**g1, (u, 0, 1)) /
                 sp.integrate(u**2*(1-u**2)**g1, (u, 0, 1)))
print("(3d) a = g1+1: E|u| =", mu, "; lim E|u|*sqrt(a) =", sp.limit(mu*sp.sqrt(g1+1), g1, sp.oo))
# (4) exact pair covariance of any exchangeable fixed-trace D=2 law, at test value E[x1^2] = 1/3
Exx = (1 - 2*sp.Rational(1, 3))/2          # from 1 = E[(x1+x2)^2] = 2 E[x1^2] + 2 E[x1 x2]
Cov = Exx - sp.Rational(1, 4)              # E[x1] = E[x2] = 1/2
Var = sp.Rational(1, 3) - sp.Rational(1, 4)
print("(4) E[x1x2] =", Exx, "; Cov(x1,x2) =", Cov, "= -Var(x1):", Cov == -Var, "; negative:", Cov < 0)
print("S1v4 DONE")
