# hciz101b.py -- item 101 (round 2 header fix; code identical to hciz101.py): independent Laplace-transform check. L(s1,s2) = int e^{s.d} rho_hat(d) dd
# computed by 16-point Gauss-Legendre on the 7 arrangement cells (exp x cubic: exact to fp roundoff),
# compared at s=(0,0) (=> Z vs 3/200) and at generic real s to the classical HCIZ integral
# 2*det[e^{t_i lam_j}]/(Delta(t) Delta(lam)), t=(s1,s2,0), evaluated in mpmath at dps=30.
# The numerator factor 2 = (D-1)! is the type-A HCIZ normalization (review r1 finding 1;
# the code already computed the correct side in r1; only this r1 header comment was wrong
# -- it said det/(Delta(a)Delta(lam)) at a=(-s1,-s2,0)). Code body is byte-identical to hciz101.py.
# The identity "Laplace transform of the Kostant-type density = HCIZ" is the claimed bridge; it is
# VERIFIED NUMERICALLY HERE, not derived. Run: python -I hciz101.py
import numpy as np, itertools, mpmath as mp
mp.mp.dps = 30
src = open("exact101b.py").read().split("seen = set()")[0]
exec(src)  # L(list of Fractions), Hex, walls, clip, rho
cells = []
for pat in itertools.product([True, False], repeat=len(walls)):
    poly = Hex
    for w, keep in zip(walls, pat):
        poly = clip(poly, w[0], w[1], keep)
        if len(poly) < 3: break
    if len(poly) < 3: continue
    A, _, _ = moments(poly)
    if A == 0: continue
    key = frozenset(poly)
    if key not in [frozenset(c) for c in cells]: cells.append(poly)
print("cells:", len(cells), "area(quad):", end=" ")
xs_gl, ws_gl = np.polynomial.legendre.leggauss(16)
u = (xs_gl + 1)/2; wu = ws_gl/2
UU, VV = np.meshgrid(u, u, indexing="ij"); WW = np.outer(wu, wu)
tris = []
for poly in cells:
    for k in range(1, len(poly)-1): tris.append((poly[0], poly[k], poly[k+1]))
pts = []; wts = []
for (p0, p1, p2) in tris:
    v1 = np.array([float(p1[0]-p0[0]), float(p1[1]-p0[1])]); v2 = np.array([float(p2[0]-p0[0]), float(p2[1]-p0[1])])
    jac = abs(v1[0]*v2[1]-v1[1]*v2[0])  # parallelogram Jacobian; Duffy u->(xi,eta)=u(1-v),uv, |d|=u
    xi = UU*(1-VV); eta = UU*VV
    d1 = float(p0[0]) + xi*v1[0] + eta*v2[0]; d2 = float(p0[1]) + xi*v1[1] + eta*v2[1]
    pts.append(np.stack([d1.ravel(), d2.ravel()])); wts.append((WW*UU*jac).ravel())
PTS = np.concatenate(pts, axis=1); WT = np.concatenate(wts)
def rho_f(d1, d2):
    d1 = np.asarray(d1); d2 = np.asarray(d2); tot = np.zeros(d1.shape)
    for w in itertools.permutations(range(3)):
        sgn = -1 if sum(1 for i in range(3) for j in range(i+1,3) if w[i]>w[j]) % 2 else 1
        g1 = float(L[w[0]]) - d1; g2 = float(L[w[1]]) - d2
        tot = tot + sgn*np.where((g1 > 0) & (g1+g2 > 0), np.minimum(g1, g1+g2), 0.0)
    return tot
Lam = [mp.mpf(6)/10, mp.mpf(3)/10, mp.mpf(1)/10]
def lap(s1, s2): return float(np.sum(WT*np.exp(s1*PTS[0]+s2*PTS[1])*rho_f(PTS[0], PTS[1])))
def hciz(s1, s2):
    a = [mp.mpf(s1), mp.mpf(s2), mp.mpf(0)]  # lap uses e^{+s.d}: match a to (s1,s2,0)
    E = [[mp.exp(a[i]*Lam[j]) for j in range(3)] for i in range(3)]
    dt = (E[0][0]*(E[1][1]*E[2][2]-E[1][2]*E[2][1]) - E[0][1]*(E[1][0]*E[2][2]-E[1][2]*E[2][0])
          + E[0][2]*(E[1][0]*E[2][1]-E[1][1]*E[2][0]))
    D = lambda v: (v[0]-v[1])*(v[0]-v[2])*(v[1]-v[2])
    return 2*dt/(D(a)*D(Lam))  # IZ normalization: (N-1)! = 2 for U(3); verified below by agreement
Zq = lap(0.0, 0.0)
print("Z(quad) = %.15f  vs exact 3/200 = %.15f  rel %.1e" % (Zq, 0.015, abs(Zq-0.015)/0.015))
mx = 0.0
for (s1, s2) in [(5.0, -7.0), (-3.0, 2.0), (11/3, 4.0), (-1.0, -2.0), (0.5, -1/3)]:
    A = lap(s1, s2)/Zq; B = hciz(str(mp.mpf(s1)), str(mp.mpf(s2)))
    r = abs(mp.mpf(repr(A))-B)/abs(B); mx = max(mx, float(r))
    print("s=(%g,%g): L/Z=%.10f HCIZ=%.10f rel=%.2e" % (s1, s2, A, B, r))
print("max rel HCIZ mismatch = %.2e" % mx)
