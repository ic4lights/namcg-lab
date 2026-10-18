"""omega = d(h(r) Lambda^3), Lambda^3 = x1 dx2 - x2 dx1 + x3 dx4 - x4 dx3, r^2 = sum x^2: invariant under both plane rotations.
Jets of omega at a point (Taylor in y to the jet order) for a given radial profile h(r) (sympy expression in r)."""
import sympy as sp
import jetlib as jl
from jetlib import Jet
from common import QQ_I
X = sp.symbols('x1:5', real=True)
r = sp.symbols('r', positive=True)

def omega_from_h(hexpr):
    rr = sp.sqrt(sum(x**2 for x in X))
    h = hexpr.subs(r, rr)
    Lam = [-X[1], X[0], -X[3], X[2]]
    A = [h * L for L in Lam]
    return sp.Matrix(4, 4, lambda m, n: sp.diff(A[n], X[m]) - sp.diff(A[m], X[n]))

def omega_jets(hexpr, x0):
    W = omega_from_h(hexpr)
    Y = sp.symbols('y1:5')
    res = [[Jet() for _ in range(4)] for _ in range(4)]
    for m in range(4):
        for n in range(4):
            e = W[m, n]
            if e == 0: continue
            d = {}
            import itertools
            for mon in itertools.product(range(jl.N + 1), repeat=4):
                if sum(mon) > jl.N: continue
                t = e
                for i, k in enumerate(mon):
                    if k: t = sp.diff(t, X[i], k)
                val = sp.nsimplify(sp.simplify(t.subs({X[i]: x0[i] for i in range(4)})))
                val = val / sp.prod([sp.factorial(k) for k in mon])
                if val != 0:
                    d[mon] = QQ_I.from_sympy(sp.Rational(val))
            res[m][n] = Jet(d)
    return res
