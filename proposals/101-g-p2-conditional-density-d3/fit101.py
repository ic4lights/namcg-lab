# fit101.py -- item 101: map the chamber walls of rho(d1,d2): fine bin density, horizontal-scanline
# kink detection, plus symbolic prediction of the intersections of the "root-direction lines through
# the hexagon vertices" (candidate Duistermaat wall lines) with each scanline. p=(0.6,0.3,0.1).
# Run: python -I fit101.py  (kink table printed; density grid saved to dens101.npy)
import numpy as np
rng = np.random.default_rng(101202605)
p = np.array([0.6, 0.3, 0.1])
N = 3_000_000
A = (rng.standard_normal((N, 3, 3)) + 1j * rng.standard_normal((N, 3, 3))) / np.sqrt(2)
Q, R = np.linalg.qr(A)
d = np.diagonal(R, axis1=1, axis2=2)
U = Q * (d / np.abs(d))[:, None, :]
del A, Q, R
b = np.abs(U) ** 2
del U
d12 = (b @ p)
del b
h = 0.005
g = np.arange(0.0, 0.7001, h)
H, xe, ye = np.histogram2d(d12[:, 0], d12[:, 1], bins=[np.arange(141) * h, np.arange(141) * h], density=True)
np.save("dens101.npy", H)
xc = 0.5 * (xe[:-1] + xe[1:])
yc = 0.5 * (ye[:-1] + ye[1:])
print("grid ok; support check d1+d2 min %.4f max %.4f" % ((d12.sum(1)).min(), (d12.sum(1)).max()))
for yv in [0.15, 0.25, 0.30, 0.35, 0.45]:
    k = int(yv / h)
    row = H[:, k]
    w = (row > 5) & (np.convolve(row, np.ones(9) / 9, mode="same") > 5)
    xs = xc[w]
    if len(xs) < 20:
        print("y=%.2f: too few" % yv); continue
    sm = np.convolve(row, np.ones(9) / 9, mode="same")
    d1_ = np.gradient(sm, h)[w]
    d2_ = np.gradient(d1_, h)
    sgn = np.sign(d2_)
    flips = np.where(np.abs(np.diff(sgn)) > 0)[0]
    kk = xs[flips][ (np.abs(d2_[flips]) > 0.05 * (np.abs(sm[flips]) + 1)) ]
    print("y=%.2f: support x=(%.3f,%.3f) kinks=%s" % (yv, xs.min(), xs.max(),
          np.array2string(np.round(kk, 3), max_line_width=110)))
# symbolic prediction: lines through vertices (perms of p in (x,y)) with directions (1,-1),(0,1),(1,-2)-ish
import sympy as sp
x = sp.symbols("x")
verts = [tuple(sorted(q, reverse=r)) for q in [(sp.Rational(6,10), sp.Rational(3,10))] for r in (0,)]
V = [(sp.Rational(a), sp.Rational(c)) for a, c in [(6,3),(6,1),(3,6),(3,1),(1,6),(1,3)]]
dirs = [(1, -1), (1, 0), (1, -2), (2, -1), (1, 1), (0, 1)]
for (vx, vy) in V:
    for (ax, ay) in dirs:
        # line: (x,y) = (vx,vy)+t(ax,ay); x where y=Y:
        Y = sp.Rational(3, 10)
        if ay == 0: continue
        xint = sp.simplify(vx + ax * (Y - vy) / ay)
        print("vert(%s,%s) dir(%d,%d) x@y=0.3: %s" % (vx, vy, ax, ay, xint))
print("done fit101")
