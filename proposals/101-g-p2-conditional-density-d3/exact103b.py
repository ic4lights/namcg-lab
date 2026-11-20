# exact103b.py -- item 101, SECOND spectrum lam=(7,25,5)/100 (independent check that the int rho*x needs full barycentric product mul(Rh,lin),
# alternating truncated-power formula is spectrum-generic, not tuned to lam=(6,3,1)/10.
# exact via fan triangulation of each arrangement cell and barycentric
# monomial integration: int_T L0^a L1^b L2^c dA = 2A a!b!c!/(2+a+b+c)!. Run: python -I exact103.py
from fractions import Fraction as F
import itertools
from math import factorial
src = open("exact101b.py").read().split("seen = set()")[0].replace('L = [F(6,10), F(3,10), F(1,10)]','L = [F(7,100)*0+F(7,10), F(25,100), F(5,100)]')
src = src.replace('Hex = [(F(6,10),F(3,10)),(F(6,10),F(1,10)),(F(3,10),F(1,10)),(F(1,10),F(3,10)),(F(1,10),F(6,10)),(F(3,10),F(6,10))]',
                  'Hex = [(F(70,100),F(25,100)),(F(70,100),F(5,100)),(F(25,100),F(5,100)),(F(5,100),F(25,100)),(F(5,100),F(70,100)),(F(25,100),F(70,100))]')
exec(src)  # L, perms, sg, kwf, rho, Hex, walls, clip, moments
def mul(p1, p2):
    o = {}
    for e1, c1 in p1.items():
        for e2, c2 in p2.items():
            e = tuple(a + b for a, b in zip(e1, e2)); o[e] = o.get(e, F(0)) + c1 * c2
    return {e: c for e, c in o.items() if c}
def lin(cs):
    return {(1,0,0): cs[0], (0,1,0): cs[1], (0,0,1): cs[2]}
def sq(cs):
    o = {}
    for i in range(3):
        for j in range(3):
            e = tuple((1 if m == i else 0) + (1 if m == j else 0) for m in range(3))
            o[e] = o.get(e, F(0)) + cs[i] * cs[j]
    return {e: c for e, c in o.items() if c}
Z = Md1 = Md2 = Mq = F(0)
for pat in itertools.product([True, False], repeat=len(walls)):
    poly = Hex
    for w, keep in zip(walls, pat):
        poly = clip(poly, w[0], w[1], keep)
        if len(poly) < 3: break
    if len(poly) < 3: continue
    v0 = poly[0]
    for k in range(1, len(poly) - 1):
        T = [v0, poly[k], poly[k + 1]]
        A, _, _ = moments(T); A = abs(A)
        if A == 0: continue
        xs = [p[0] for p in T]; ys = [p[1] for p in T]; rs = [rho(p[0], p[1]) for p in T]
        Rh = {}
        for i in range(3):
            e = tuple(1 if m == i else 0 for m in range(3))
            Rh[e] = rs[i]
        x2 = sq(xs); y2 = sq(ys)
        z = [1 - x - y for x, y in zip(xs, ys)]
        z2 = sq(z)
        for mono, key in ((x2, 'x'), (y2, 'y'), (z2, 'z')):
            P = mul(Rh, mono)
            I = sum(c * 2 * A * F(factorial(a) * factorial(b) * factorial(cc), factorial(2 + a + b + cc))
                    for (a, b, cc), c in P.items())
            Mq += I
        Ix = sum(c * 2 * A * F(factorial(a) * factorial(b) * factorial(cc), factorial(2 + a + b + cc))
                 for (a, b, cc), c in Rh.items())
        Z += Ix
        def bint(P):
            return sum(c * 2 * A * F(factorial(a) * factorial(b) * factorial(cc), factorial(2 + a + b + cc))
                       for (a, b, cc), c in P.items())
        Md1 += bint(mul(Rh, lin(xs)))
        Md2 += bint(mul(Rh, lin(ys)))
print("Z =", Z, " (spectrum-2 lam=(0.7,0.25,0.05))  C =", 1 / Z)
print("E[d1] =", Md1 / Z, "E[d2] =", Md2 / Z, " (target 1/3 each)")
print("E[sum d^2] =", Mq / Z, " (target (1+sum p^2)/4 =", (1 + sum(l * l for l in L)) / 4, ")")
