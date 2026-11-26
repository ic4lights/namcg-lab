# mc101c.py -- item 101: fine structure of the joint density rho(d1,d2) of the diagonal given
# the spectrum, D=3, Haar fibre (cv class). p = (0.6,0.3,0.1). Outputs: breakpoint radii along
# rays from the centre, and the d1-marginal vs the established 096 piecewise-linear formula.
# Run: python -I mc101c.py  (writes fine_hist_101.npy)
import numpy as np
rng = np.random.default_rng(101202604)
lam = np.array([6.0, 3.0, 1.0]); tau = lam.sum(); p = lam / tau
N = 4_000_000
A = (rng.standard_normal((N, 3, 3)) + 1j * rng.standard_normal((N, 3, 3))) / np.sqrt(2)
Q, R = np.linalg.qr(A)
d = np.diagonal(R, axis1=1, axis2=2)
U = Q * (d / np.abs(d))[:, None, :]
b = np.abs(U) ** 2
dd = (b @ lam) / tau
del A, Q, R, U, b
x0, y0 = 1.0 / 3, 1.0 / 3
dx, dy = dd[:, 0] - x0, dd[:, 1] - y0
rad = np.hypot(dx, dy)
ang = np.arctan2(dy, dx)
print("max radius %.5f; per-ray segment counts:" % rad.max())
for adeg in range(0, 360, 30):
    m = np.abs(((ang - np.deg2rad(adeg) + np.pi / 60) % (np.pi / 3)) - np.pi / 60) < 1e-2
    r = np.sort(rad[m])
    n = len(r)
    # local density along ray: histogram in r
    h, e = np.histogram(r, bins=60, range=(0, r.max()), density=True)
    d2 = np.diff(h)
    brs = e[1:-1][np.abs(d2) > 3 * np.sqrt(h[1:] + h[:-1]) / np.sqrt(n * (e[1] - e[0]))]
    print("ray %3d: N=%6d breakpoints(r)=%s" % (adeg, n, np.array2string(brs, precision=3, max_line_width=90)))
ed = np.linspace(0, 1, 201)
h1, _ = np.histogram(dd[:, 0], bins=ed, density=True)
mu = (lam[1] - lam[2]) / (lam[0] - lam[2])
tc = 0.5 * (ed[:-1] + ed[1:])
mask = (tc > p[2]) & (tc < p[0])
ex1 = np.where(tc < mu, 2 * tc / mu, 2 * (1 - tc) / (1 - mu))
zc = np.where(tc < mu, tc / mu, (1 - tc) / (1 - mu))
se = np.sqrt(zc / (N * np.diff(ed)[0]))
zmax = np.max(np.abs(h1[mask] - ex1[mask]) / se[mask])
print("d1 marginal vs 096 exact: max z = %.2f over %d interior bins" % (zmax, mask.sum()))
np.save("fine_hist_101.npy", np.vstack([0.5 * (ed[:-1] + ed[1:]), h1]))
print("done mc101c")
