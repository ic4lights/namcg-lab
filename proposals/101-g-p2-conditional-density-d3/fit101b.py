# fit101b.py -- item 101 (replaces fit101.py per two-touch rule; loads saved dens101.npy).
# Horizontal-scanline kink detection on rho(d1,d2) + symbolic wall-line predictions.
# Run: python -I fit101b.py
import numpy as np
h = 0.005
H = np.load("dens101.npy")           # H[i,j] density at (x_i,y_j), x_i=y_j=(i+0.5)*h
xc = (np.arange(140) + 0.5) * h
for yv in [0.12, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50]:
    k = int(yv / h)
    row = H[:, k]
    w = (row > 5) & (np.convolve(row, np.ones(9) / 9, mode="same") > 5)
    xs = xc[w]
    if len(xs) < 20:
        print("y=%.2f: too few" % yv); continue
    sm = np.convolve(row, np.ones(9) / 9, mode="same")
    d1_ = np.gradient(sm, h)[w]
    d2_ = np.gradient(d1_, h)
    flips = np.where(np.diff(np.sign(d2_)) != 0)[0]
    jumps = np.abs(np.diff(d1_))
    kk = xs[flips][jumps[flips] > 0.35 * np.median(jumps)]
    print("y=%.2f: support x=(%.3f,%.3f) kinks=%s" % (yv, xs.min(), xs.max(),
          np.array2string(np.round(kk, 3), max_line_width=110)))
import sympy as sp
Y = sp.Rational(3, 10)
V = [(sp.Rational(a, 10), sp.Rational(c, 10)) for a, c in [(6,3),(6,1),(3,6),(3,1),(1,6),(1,3)]]
dirs = [(1,-1),(1,0),(1,-2),(2,-1),(1,1),(0,1)]
for (vx, vy) in V:
    for (ax, ay) in dirs:
        if ay == 0: continue
        xi = sp.simplify(vx + ax * (Y - vy) / ay)
        if 0 < xi < 1: print("vert(%s,%s) dir(%d,%d) x@0.3=%s" % (vx, vy, ax, ay, xi))
print("done fit101b")
