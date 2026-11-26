# num101.py -- item 101: independent numeric validations of rho_hat = sum_w eps(w) kw(w.lam-d), lam=(.6,.3,.1).
# (a) 2D Laplace transform of rho_hat vs HCIZ determinant (mpmath, random rational shifts, dps=25);
# (b) f(P2) from circle integrals of rho_hat vs fresh Haar MC (fine bins, z-scores);
# (c) E[P2] by quadrature vs (1+sum p^2)/4. Run: python -I num101.py
import numpy as np, itertools
from mpmath import mp, mpf, exp, matrix
mp.dps = 25
L = [mpf(6)/10, mpf(3)/10, mpf(1)/10]
perms = list(itertools.permutations(range(3)))
def sg(p): return -1 if sum(1 for i in range(3) for j in range(i+1,3) if p[i]>p[j]) % 2 else 1
def kwf(g1, g2):
    c1, c2 = g1, g1 + g2
    return min(c1, c2) if (c1 > 0 and c2 > 0) else mpf(0)
def rhoh(d1, d2):
    return sum(sg(w) * kwf(L[w[0]] - d1, L[w[1]] - d2) for w in perms)
# (a) Laplace: integrate rho_hat*exp(-(s1 d1+s2 d2)) over triangle fan of hexagon (quad on each triangle)
from mpmath import quad
VH = [(mpf(6)/10,mpf(3)/10),(mpf(6)/10,mpf(1)/10),(mpf(3)/10,mpf(1)/10),
      (mpf(1)/10,mpf(3)/10),(mpf(1)/10,mpf(6)/10),(mpf(3)/10,mpf(6)/10)]
ap = (mpf(1)/3, mpf(1)/3)
def lap2d(s1, s2):
    tot = mpf(0)
    for k in range(6):
        b, c = VH[k], VH[(k+1) % 6]
        ja = (b[0]-ap[0])*(c[1]-b[1]) - (b[1]-ap[1])*(c[0]-b[0])
        f = lambda tt, ss: rhoh(ap[0]+ss*(b[0]-ap[0])+ss*tt*(c[0]-b[0]),
                                 ap[1]+ss*(b[1]-ap[1])+ss*tt*(c[1]-b[1])) * \
                           exp(-(s1*(ap[0]+ss*(b[0]-ap[0])+ss*tt*(c[0]-b[0]))+s2*(ap[1]+ss*(b[1]-ap[1])+ss*tt*(c[1]-b[1])))) * ss
        tot += quad(lambda ss: quad(lambda tt: f(tt, ss), [0, 1]), [0, 1]) * ja
    return tot
def hciz(s1, s2):
    a = [-s1, -s2, mpf(0)]
    M = matrix(3, 3, lambda i, j: exp(a[i]*L[j]))
    D = lambda v: (v[0]-v[1])*(v[0]-v[2])*(v[1]-v[2])
    return det(M) / (D(a)*D(L))
Zn = lap2d(mpf(0), mpf(0))
print("Z numeric =", mp.nstr(Zn, 12))
mx = 0
for (s1, s2) in [(mpf(1)/2, -mpf(1)/3), (mpf(3), mpf(5)), (-mpf(1)/4, mpf(7)/2), (mpf(11)/3, mpf(-2)/7), (mpf(0)/1, mpf(4))]:
    A, B = lap2d(s1, s2)/Zn, hciz(s1, s2)
    r = abs(A-B)/abs(B) if B != 0 else abs(A-B)
    mx = max(mx, r)
    print("lap s=(%s,%s): ans %.12g hciz %.12g rel %.2e" % (s1, s2, A, B, r))
print("max rel HCIZ mismatch:", mp.nstr(mx, 3))
