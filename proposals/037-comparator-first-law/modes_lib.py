"""Plane-wave test modes about constant (A)SD Theta-bar with delta-rho = 0 (033/036 conventions); returns first-order data incl. full Omega_{st} and Riemann as so(4)-valued 2-forms."""
import random, sympy as sp
from sympy import Rational as Q
import lin_lib as L, lib

def modes(Thb, n, seed):
    random.seed(seed); out = []
    rnd = lambda: Q(random.randint(-4, 4), random.randint(1, 3))
    while len(out) < n:
        p = [rnd() for _ in range(4)]
        if all(x == 0 for x in p): continue
        v = sp.symbols('v0:4'); S, w = L.hat_S(p, list(v))
        cond = sp.expand((Thb*w).trace()); vv = [rnd() for _ in range(3)]
        sol = sp.solve(cond.subs(dict(zip(v[:3], vv))), v[3], dict=True)
        if not sol: continue
        vals = dict(zip(v[:3], vv)); vals[v[3]] = sol[0][v[3]]
        S, w = L.hat_S(p, [x.subs(vals) for x in v])
        d = L.linear_data(Thb, S)
        if d['C2'] == 0: continue
        D2Th = {k: -Thb * S[k] * Thb for k in S}
        g0 = d['g0']
        def Om(s, t):
            return g0 * sum((Thb[r, t]*D2Th[(s, r)] - Thb[r, s]*D2Th[(t, r)] for r in range(4)), sp.zeros(4, 4))
        d['Om'] = {(s, t): Om(s, t) for s in range(4) for t in range(4)}
        d['Rmat'] = {(s, t): sp.Matrix(4, 4, lambda m, n_: d['Rt'][(m, n_, s, t)] / g0) for s in range(4) for t in range(4)}
        d['S'] = S
        out.append(d)
    return out

def gen(a, b):
    J = sp.zeros(4, 4); J[a, b] = 1; J[b, a] = -1; return J

def ip(X, Y, g0):
    """<X,Y> = G^{ss'}G^{tt'} tr(X_st Y_s't') with G = g0*delta, X,Y dicts (s,t)->4x4."""
    return sum(((X[(s, t)]*Y[(s, t)]).trace() for s in range(4) for t in range(4)), 0) / g0**2

def backgrounds():
    return (('SD', lib.eta3()[2].inv()), ('ASD', lib.etabar()[2].inv()))
