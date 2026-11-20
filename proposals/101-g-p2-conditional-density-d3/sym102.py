# sym102.py -- item 101: exact checks of rho_hat(d) = sum_w eps(w) kw(w lam - d), D=3, lam=(6,3,1)/10.
# (1) exact normalization; (2) d1-marginal == 096 formula; (3) HCIZ Laplace match (mpmath);
# (4) E[P2] == (1+sum p^2)/4; (5) f(P2) circle formula vs MC hist p2_hist_101.npy. Run: python -I sym102.py
import numpy as np, itertools
import sympy as sp
from mpmath import mp, mpf, sqrt, exp, det, matrix
mp.dps = 30
L = [mpf(6)/10, mpf(3)/10, mpf(1)/10]
perms = list(itertools.permutations(range(3)))
def sg(p):
    return -1 if sum(1 for i in range(3) for j in range(i+1,3) if p[i]>p[j]) % 2 else 1
def kwf(g1, g2):
    c1, c2 = g1, g1 + g2
    return min(c1, c2) if (c1 > 0 and c2 > 0) else mpf(0)
def rhoh(d1, d2):
    return mpf(sum(sg(w) * float(0)) if False else
               sum(sg(w) * kwf(L[w[0]]-d1, L[w[1]]-d2) for w in perms))
d1, d2 = sp.symbols("d1 d2", real=True)
Ls = [sp.Rational(6,10), sp.Rational(3,10), sp.Rational(1,10)]
def kws(a, b):
    c1, c2 = a, a + b
    return sp.Piecewise((sp.Min(c1,c2), (c1>=0)&(c2>=0)), (0, True))
rhos = sum(sp.sign(sp.factorial(0)) if False else sp.sympify(sg(w))*kws(Ls[w[0]]-d1, Ls[w[1]]-d2) for w in perms)
# chamber polygon = hexagon |d - centroid| etc; instead integrate over triangle fan of hexagon vertices
VH = [(sp.Rational(6,10),sp.Rational(3,10)),(sp.Rational(6,10),sp.Rational(1,10)),
      (sp.Rational(3,10),sp.Rational(1,10)),(sp.Rational(1,10),sp.Rational(3,10)),
      (sp.Rational(1,10),sp.Rational(6,10)),(sp.Rational(3,10),sp.Rational(6,10))]
cC = sp.Rational(1,3)
tris = [(sp.Tuple(cC,cC), VH[k], VH[(k+1)%6]) for k in range(6)]
Z = 0
for (a,b,c,dv) in tris:
    s,t = sp.symbols("s t", positive=True)
    P = (1-s)*b + s*dv; Q = (1-s-t)*a + (s+t)*c   # a=(1/3,1/3) apex: P on edge a->dv? use apex fan:
    X = a*(1-s) + s*( (1-t)*b + t*dv )
    J = sp.simplify(sp.Matrix(X).jacobian([s,t]).det())
    Z += sp.integrate(sp.simplify(rhos.subs({d1:X[0], d2:X[1]}))*sp.Abs(J), (t,0,1),(s,0,1))
print("Z exact =", sp.nsimplify(Z), "=", sp.N(Z,12))
