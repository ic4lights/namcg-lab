"""Rotation-invariant (x1,x2 plane) self-dual closed omega = b_i eta^i, polynomial solutions with random free data.
b1 + i b2 = z * h(s,x3,x4), b3 = k(s,x3,x4), s = x1^2+x2^2, z = x1 + i x2.  Sigma = {x1=x2=0} is fixed pointwise."""
import itertools, random
import sympy as sp
from sympy import Rational
import lib

X = sp.symbols('x1:5', real=True)

def rot_solution(deg=4, seed=0, b3_0=1):
    random.seed(seed)
    s = X[0]**2 + X[1]**2
    z = X[0] + sp.I*X[1]
    mons = [(a, m, n) for a in range(deg//2 + 1) for m in range(deg + 1) for n in range(deg + 1) if 2*a + m + n <= deg - 1]
    mons_k = [(a, m, n) for a in range(deg//2 + 1) for m in range(deg + 1) for n in range(deg + 1) if 2*a + m + n <= deg]
    hr = sp.symbols('hr0:%d' % len(mons), real=True); hi = sp.symbols('hi0:%d' % len(mons), real=True); kc = sp.symbols('k0:%d' % len(mons_k), real=True)
    h = sum((hr[i] + sp.I*hi[i])*s**mons[i][0]*X[2]**mons[i][1]*X[3]**mons[i][2] for i in range(len(mons)))
    k = sum(kc[i]*s**mons_k[i][0]*X[2]**mons_k[i][1]*X[3]**mons_k[i][2] for i in range(len(mons_k)))
    zh = sp.expand(z*h)
    b1 = sp.expand(sp.re(zh)); b2 = sp.expand(sp.im(zh)); b3 = sp.expand(k)
    b = [b1, b2, b3]
    eta = lib.eta3()
    omega = sum((b[i]*eta[i] for i in range(3)), sp.zeros(4, 4))
    lin = []
    for a, bb, c in itertools.combinations(range(4), 3):
        e = sp.expand(sp.diff(omega[bb, c], X[a]) + sp.diff(omega[c, a], X[bb]) + sp.diff(omega[a, bb], X[c]))
        P = sp.Poly(e, *X)
        lin += list(P.coeffs())
    unknowns = list(hr) + list(hi) + list(kc)
    zero_k = mons_k.index((0, 0, 0))
    cons = [kc[zero_k] - b3_0]
    sol = list(sp.linsolve(lin + cons, *unknowns))[0]
    free = sorted(set().union(*[v.free_symbols for v in sol]), key=str)
    sub = {f: Rational(random.randint(-3, 3), random.randint(1, 3)) for f in free}
    vals = [v.subs(sub) for v in sol]
    d = dict(zip(unknowns, vals))
    import sd_family
    bsol = [sp.expand(bi.subs(d).subs({X[i]: sd_family.X[i] for i in range(4)}, simultaneous=True)) for bi in b]
    return bsol, eta, len(free)

if __name__ == '__main__':
    bs, eta, nf = rot_solution(4, 1)
    print('free params', nf)
    print(bs[2])
