"""Rotation-invariant SD Poisson bivectors with J=0 and a fixed plane Sigma={x1=x2=0}.
Find polynomial b_i(x) (degree <= D) with  d(b_i eta^i)=0  and invariance of omega under the (12)-plane rotation
R_alpha: omega(R x) = R omega(x) R^T, i.e. L_{x1 d2 - x2 d1} omega = 0 (Lie derivative of the 2-form)."""
import itertools, random
import sympy as sp
from sympy import Rational
import lib
X = sp.symbols('x1:5')

def lie_rot(w):
    """Lie derivative of the 2-form w (matrix w_{mn}) along the rotation vector field v = x1 d2 - x2 d1."""
    v = [-X[1], X[0], 0, 0]
    out = sp.zeros(4, 4)
    for m in range(4):
        for n in range(4):
            t = sum(v[k]*sp.diff(w[m, n], X[k]) for k in range(4))
            t += sum(sp.diff(v[k], X[m])*w[k, n] for k in range(4))
            t += sum(sp.diff(v[k], X[n])*w[m, k] for k in range(4))
            out[m, n] = t
    return out

def solve(deg=4, seed=0, anti=False):
    random.seed(seed)
    mons = [m for m in itertools.product(range(deg+1), repeat=4) if sum(m) <= deg]
    syms = sp.symbols('c0:%d' % (3*len(mons)))
    b = [sum(syms[i*len(mons)+k]*sp.prod([X[a]**mons[k][a] for a in range(4)]) for k in range(len(mons))) for i in range(3)]
    eta = lib.etabar() if anti else lib.eta3()
    w = sum((b[i]*eta[i] for i in range(3)), sp.zeros(4, 4))
    eqs = []
    for a, bb, c in itertools.combinations(range(4), 3):
        eqs.append(sp.expand(sp.diff(w[bb, c], X[a]) + sp.diff(w[c, a], X[bb]) + sp.diff(w[a, bb], X[c])))
    L = lie_rot(w)
    for m in range(4):
        for n in range(m+1, 4):
            eqs.append(sp.expand(L[m, n]))
    lin = []
    for e in eqs:
        if e == 0: continue
        lin += list(sp.Poly(e, *X).coeffs())
    zero_idx = mons.index((0, 0, 0, 0))
    # b(0) = (0,0,1): nondegenerate and invariant on Sigma
    cons = [syms[0*len(mons)+zero_idx], syms[1*len(mons)+zero_idx], syms[2*len(mons)+zero_idx] - 1]
    sol = list(sp.linsolve(lin + cons, *syms))[0]
    free = sorted(set().union(*[s.free_symbols for s in sol]), key=str)
    return b, syms, sol, free, mons

if __name__ == '__main__':
    b, syms, sol, free, mons = solve(deg=4, seed=0)
    print('free parameters:', len(free))
    random.seed(5)
    sub = {f: Rational(random.randint(-3, 3), random.randint(1, 3)) for f in free}
    vals = [s.subs(sub) for s in sol]
    bs = [sp.expand(bi.subs(dict(zip(syms, vals)))) for bi in b]
    for i in range(3): print('b%d =' % (i+1), bs[i])
