# sym103.py -- item 101 (replaces sym102): exact checks for rho_hat(d1,d2)=sum_w eps(w) kw(w.lam-d),
# kw(g)=min(g1, g1+g2)_+, lam=(6,3,1)/10. Checks: (1) exact Z and C=1/Z; (2) d1-marginal == 096;
# (3) HCIZ Laplace vs mpmath quadrature; (4) E[P2]==(1+sum p^2)/4; (5) f(P2) circle-integral vs MC.
# Run: python -I sym103.py   (prints PASS/FAIL table)
import numpy as np, itertools
import sympy as sp
from mpmath import mp, mpf, exp, matrix, det, quad
mp.dps = 30
perms = list(itertools.permutations(range(3)))
def sg(p): return -1 if sum(1 for i in range(3) for j in range(i+1,3) if p[i]>p[j]) % 2 else 1
# ---- sympy part: exact Z over hexagon fan, exact marginal, E[P2]
d1, d2, s, t = sp.symbols("d1 d2 s t", real=True)
Ls = [sp.Rational(6,10), sp.Rational(3,10), sp.Rational(1,10)]
def kws(a, b):
    return sp.Piecewise((a, (a >= 0) & (a+b >= 0) & (b >= 0)),
                          (a+b, (a >= 0) & (a+b >= 0)), (0, True))
rhoS = sum(sp.sympify(sg(w)) * kws(Ls[w[0]] - d1, Ls[w[1]] - d2) for w in perms)
apex = (sp.Rational(1,3), sp.Rational(1,3))
VH = [(sp.Rational(6,10),sp.Rational(3,10)),(sp.Rational(6,10),sp.Rational(1,10)),
      (sp.Rational(3,10),sp.Rational(1,10)),(sp.Rational(1,10),sp.Rational(3,10)),
      (sp.Rational(1,10),sp.Rational(6,10)),(sp.Rational(3,10),sp.Rational(6,10))]
Z = sum(sp.integrate(sp.integrate((rhoS.subs({d1: apex[0]+s*(b[0]-apex[0])+s*t*(c[0]-b[0]),
        d2: apex[1]+s*(b[1]-apex[1])+s*t*(c[1]-b[1])}) * sp.Abs((b[0]-apex[0])*(c[1]-b[1])-(b[1]-apex[1])*(c[0]-b[0]))*s
        ), (t, 0, 1)), (s, 0, 1)) for (b, c) in zip(VH, VH[1:]+VH[:1]))
print("Z =", sp.nsimplify(Z), "=", sp.N(Z, 15))
C = 1/Z
marg = sp.integrate(rhoS*C, (d2, 0, 1))     # density of d1
margS = sp.simplify(sp.piecewise_fold(marg))
tt = sp.symbols("tt", real=True)                      # 096: t=(d1-1/10)/(6/10-1/10), mu=2/5
mu = sp.Rational(2,5)
ex096 = sp.Piecewise((2*tt/mu, tt <= mu), (2*(1-tt)/(1-mu), True))
ok_marg = [sp.simplify(margS.subs(d1, sp.Rational(1,10)+sp.Rational(1,2)*tv) * sp.Rational(1,2) - ex096.subs(tt, tv)) == 0
           for tv in [sp.Rational(k,40) for k in [4, 8, 12, 16, 24, 30, 36, 39]]]
print("marginal-vs-096 at", len(ok_marg), "exact points:", all(ok_marg))
EP2 = sp.integrate((d1**2 + d2**2 + (1-d1-d2)**2) * rhoS * C, (d2, 0, 1))
EP2 = sp.integrate(EP2, (d1, 0, 1))
print("E[P2] exact:", EP2, "target (1+sum p^2)/4 =", (1+sum(l*l for l in Ls))/4)
