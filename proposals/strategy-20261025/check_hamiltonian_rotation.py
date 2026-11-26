"""Lead check for candidate 1: on joint-flow-stationary backgrounds the rotation xi of the normal
plane is Hamiltonian for omega (iota_xi omega = d eps), so the rigid eta-rotation of the matrix
coordinates equals the Poisson (matrix-gauge) transformation {eps, X^a}.  eps vanishes to second
order on Sigma = {x1 = x2 = 0}.  Euclidean, constant omega in span{e12,e34} and the cone family."""
import sympy as sp
x = sp.symbols('x1:5', real=True)
a, c = sp.symbols('a c', nonzero=True)
f = sp.Function('f')
r2 = x[0]**2 + x[1]**2
xi = [-x[1], x[0], 0, 0]
for name, w12, w34 in [('constant span', a, c), ('cone family f(u)=1+u+u^2/3', -(1 + r2 + r2**2/3), -1), ('cone family f(u)=exp(u)', -sp.exp(r2), -1)]:
    om = sp.zeros(4, 4); om[0, 1] = w12; om[1, 0] = -w12; om[2, 3] = w34; om[3, 2] = -w34
    iota = [sp.simplify(sum(xi[m] * om[m, n] for m in range(4))) for n in range(4)]   # (iota_xi om)_n
    # eps with d eps = iota: integrate along radius for the (x1,x2) part
    s = sp.symbols('s', positive=True)
    eps = sp.integrate((iota[0].subs({x[0]: s*x[0], x[1]: s*x[1]})*x[0] + iota[1].subs({x[0]: s*x[0], x[1]: s*x[1]})*x[1]), (s, 0, 1))
    ok = all(sp.simplify(sp.diff(eps, x[n]) - iota[n]) == 0 for n in range(4))
    Th = om.inv()
    pb = [sp.simplify(sum(Th[m, n] * sp.diff(eps, x[m]) * sp.diff(x[k], x[n]) for m in range(4) for n in range(4))) for k in range(4)]
    print(f"[{name}] iota_xi omega = d eps: {ok}; eps = {sp.simplify(eps)}")
    print(f"   {{eps, X^a}} - xi^a = {[sp.simplify(pb[k] - xi[k]) for k in range(4)]}  (or + xi: {[sp.simplify(pb[k] + xi[k]) for k in range(4)]})")
    on_sigma = [sp.simplify(e.subs({x[0]: 0, x[1]: 0})) for e in [eps] + [sp.diff(eps, v) for v in x]]
    print(f"   eps and d eps on Sigma: {on_sigma}")
