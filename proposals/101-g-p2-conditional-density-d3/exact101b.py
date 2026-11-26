# exact101b.py -- item 101 (fixes exact101: moments() returns int x dA already, so centroid = ix/A not ix/(3A); (replaces failed sympy-integrate sym103): EXACT rational computation of
# Z = int rho_hat, int d1, int sum d_i^2 over the plane, via the arrangement of the 9 wall lines
# d_i = lam_a (rho_hat is affine on each cell; integral of an affine function over a polygon is done
# exactly with Fractions via the boundary formulas int x dA = (1/6)sum (x_i+x_{i+1}) cross_i).
# Also prints rho_hat(centroid) and the P2 breakpoint values (circles centred at the centroid through
# centroid cells also now deduped; breakpoints via explicit linear solve). Run: python -I exact101b.py
from fractions import Fraction as F
import itertools
L = [F(6,10), F(3,10), F(1,10)]
perms = list(itertools.permutations(range(3)))
def sg(p): return -1 if sum(1 for i in range(3) for j in range(i+1,3) if p[i]>p[j]) % 2 else 1
def coord(pt, k): return pt[k] if k < 2 else 1 - pt[0] - pt[1]
def kwf(g1, g2):
    c1, c2 = g1, g1 + g2
    return min(c1, c2) if (c1 > 0 and c2 > 0) else F(0)
def rho(d1, d2): return sum(sg(w) * kwf(L[w[0]] - d1, L[w[1]] - d2) for w in perms)
Hex = [(F(6,10),F(3,10)),(F(6,10),F(1,10)),(F(3,10),F(1,10)),(F(1,10),F(3,10)),(F(1,10),F(6,10)),(F(3,10),F(6,10))]
walls = [(i, L[a]) for i in range(3) for a in range(3)]
def clip(poly, i, cval, keepge):
    out = []
    n = len(poly)
    for k in range(n):
        P, Q = poly[k], poly[(k+1) % n]
        vp = coord(P, i) - cval; vq = coord(Q, i) - cval
        if (vp >= 0) == keepge:
            out.append(P)
            if (vq >= 0) != keepge and vp != vq:
                t = vp / (vp - vq); out.append((P[0] + t*(Q[0]-P[0]), P[1] + t*(Q[1]-P[1])))
        elif (vq >= 0) == keepge and vp != vq:
            t = vp / (vp - vq); out.append((P[0] + t*(Q[0]-P[0]), P[1] + t*(Q[1]-P[1])))
    return out
def moments(poly):
    A = ix = iy = F(0)
    n = len(poly)
    for k in range(n):
        x1, y1 = poly[k]; x2, y2 = poly[(k+1) % n]
        cr = x1*y2 - x2*y1
        A += cr; ix += (x1+x2)*cr; iy += (y1+y2)*cr
    A = A/2
    if A < 0: return -A, -ix/6, -iy/6
    return A, ix/6, iy/6
seen = set(); Z = Md1 = Md2 = Mq = F(0)
for pat in itertools.product([True, False], repeat=len(walls)):
    poly = Hex
    for w, keep in zip(walls, pat):
        poly = clip(poly, w[0], w[1], keep)
        if len(poly) < 3: break
    if len(poly) < 3: continue
    A, ix, iy = moments(poly)
    if A == 0: continue
    cx = ix/A; cy = iy/A
    rv = rho(cx, cy)
    Z += A * rv; Md1 += A * rv * cx; Md2 += A * rv * cy; Mq += A * rv * (cx*cx + cy*cy + (1-cx-cy)**2)
print("Z =", Z, "| C = 1/Z =", 1/Z if Z else "inf")
Zc = Z
print("E[d1] =", Md1/Zc, "E[d2] =", Md2/Zc, "E[sum d^2] =", Mq/Zc, "target (1+sum p^2)/4 =", (1+sum(l*l for l in L))/4)
print("rho(centroid) =", rho(F(1,3), F(1,3)), "C*rho =", (1/Zc)*rho(F(1,3), F(1,3)))
pts = set()
def solve2(i, c1, j, c2):
    # coord_i(p)=c1, coord_j(p)=c2 as linear equations in (d1,d2): a*d1+b*d2=e
    M = {}
    M[0] = (1, 0, c1); M[1] = (0, 1, c2); M[2] = (-1, -1, c1 - 1)
    (a1, b1, e1), (a2, b2, e2) = M[i], M[j]
    det = a1*b2 - a2*b1
    if det == 0: return None
    return ((e1*b2 - e2*b1)/det, (a1*e2 - a2*e1)/det)
for (i, c1), (j, c2) in itertools.combinations(walls, 2):
    if i == j: continue
    sol = solve2(i, c1, j, c2)
    if sol: pts.add(sol)
c = (F(1,3), F(1,3))
E = F(1, 1000)
def inhex(p):
    d3 = 1 - p[0] - p[1]
    return all(F(1,10)-E <= v <= F(6,10)+E for v in (p[0], p[1], d3))
bp = sorted({(p[0]-c[0])**2 + (p[1]-c[1])**2 + ((1-p[0]-p[1])-F(1,3))**2 for p in pts if inhex(p)})
print("P2 breakpoints (dist^2 to centroid, sorted):")
print([float(v) for v in sorted(bp)])
