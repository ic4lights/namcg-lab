# sym101.py -- item 101: identify the exact piecewise-linear rho(d1,d2|p) for the Haar-fibre D=3
# diagonal law as a signed Kostant-partition-function sum, and test it against (a) the MC grid
# dens101.npy, (b) the established 096 d1-marginal, (c) HCIZ Laplace transform (checked in sym102).
# Run: python -I sym101.py
import numpy as np, itertools, sympy as sp
lam = [sp.Rational(6,10), sp.Rational(3,10), sp.Rational(1,10)]
def kwv(g1, g2):                      # type-A2 continuous partition fn, coords c1=g1, c2=g1+g2... see note
    c1, c2 = g1, g1 + g2              # c1 = gamma_1, c2 = -gamma_3 for gamma=(g1,g2,-g1-g2)
    return min(c1, c2) if c1 >= 0 and c2 >= 0 else 0
perms = list(itertools.permutations(range(3)))
def sgn(p):
    s = 0
    for i in range(3):
        for j in range(i+1, 3):
            if p[i] > p[j]: s += 1
    return -1 if s % 2 else 1
def variant(d1, d2, mode):
    tot = 0
    for w in perms:
        wl = [lam[w[0]], lam[w[1]], lam[w[2]]]
        g = [wl[0]-d1, wl[1]-d2]                       # w lam - d
        if mode == 0: tot += sgn(w) * kwv(*g)
        elif mode == 1: tot += sgn(w) * kwv(*[-x for x in g])
        elif mode == 2:
            wd = [d1*1, d2*1]
            wd3 = 1 - d1 - d2
            wd3p = [d1, d2, wd3]
            wd_l = [wd3p[w[0]], wd3p[w[1]], wd3p[w[2]]]
            tot += sgn(w) * kwv(lam[0]-wd_l[0], lam[1]-wd_l[1])
        elif mode == 3:
            wd3p = [d1, d2, 1-d1-d2]
            wd_l = [wd3p[w[0]], wd3p[w[1]], wd3p[w[2]]]
            tot += sgn(w) * kwv(wd_l[0]-lam[0], wd_l[1]-lam[1])
    return tot
# MC grid
h = 0.005
H = np.load("dens101.npy"); xc = (np.arange(140)+0.5)*h
best = None
for mode in range(4):
    vals = np.zeros((140,140)); pos = 0; tot = 0
    for i in range(140):
        for j in range(140):
            v = float(variant(float(xc[i]), float(xc[j]), mode))
            vals[i,j] = v
            if v > 1e-12: pos += 1
    sup = H > 1.0
    if sup.sum() == 0: continue
    # scale: match integral of vals over its support to 1, compare shape on MC support region
    m = np.abs(vals) > 1e-12
    print("mode %d: nonzero cells %d, MC-support cells %d, neg-on-support %d"
          % (mode, m.sum(), sup.sum(), int(((vals < -1e-12) & sup).sum())))
    if mode == 0 and m.sum() > 0:
        Cfit = 1.0/ (np.abs(vals[m]).sum())            # placeholder shape corr below
        sel = sup & (np.abs(vals) > 1e-12)
        cf = np.corrcoef(vals[sel].ravel(), H[sel].ravel())[0,1]
        print("   shape corr on MC support (mode0): %.4f" % cf)
print("done sym101")
