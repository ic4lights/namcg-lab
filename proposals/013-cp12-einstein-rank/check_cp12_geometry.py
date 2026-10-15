"""
Geometry of the fibre of y^mu = M^{mu5} over a base point with y^4 = M^{45} != 0, in the explicit realisation (floats).
Checks:
 (G1) Lie-Poisson algebra constant s; {T^a, y^mu} = s eta^{a mu} M^{45}  (so K = (M^{45})^2 eta^{-1} pointwise).
 (G2) Orbit relations at random points: y_b M^{ab} = 0 (a,b = 0..4, eta_5 = diag(-,+,+,+,+)).
 (G3) Fibre over a boosted base point (SO(4) stabiliser orbit of a boosted point): y^a constant on the fibre,
      the span of the six functions M^{mu rho} (mu<rho) on the fibre has dimension 3, T^mu = M^{mu4} lies in that span,
      the fibre average of M^{mu rho} vanishes; the subspace W_y in Lambda^2 R^4 is saved.
 (G4) Identification of W_y with the (anti-)self-dual 2-forms of y^perp (rational model used in check_cp12_rank_exact.py).
"""
import numpy as np, json, sys, os
from cp12_realisation import *
np.set_printoptions(precision=6, suppress=True, linewidth=150)
rng = np.random.default_rng(11)
eta5 = np.diag([-1., 1, 1, 1, 1])

ratios = []
for t in range(30):
    z = rand_z_pos(rng, rng.uniform(0.5, 3)); M = Mfun(z)
    for (A, B, C, D) in [(0, 4, 1, 5), (2, 4, 2, 5), (0, 1, 1, 2), (3, 4, 3, 5), (1, 2, 2, 5), (0, 5, 0, 4)]:
        rhs = lie(A, B, C, D, M)
        if abs(rhs) > 1e-6:
            ratios.append(PB(A, B, C, D, z)/rhs)
s = float(np.sign(np.mean(ratios)))
print("(G1) Lie-Poisson sign s = %+.0f (spread %.1e)" % (s, np.ptp(ratios)))
dev = 0
for t in range(30):
    z = rand_z_pos(rng, rng.uniform(0.5, 3)); M = Mfun(z)
    E = np.array([[PB(a, 4, mu, 5, z) for mu in range(4)] for a in range(4)])
    dev = max(dev, np.abs(E - s*np.diag([-1., 1, 1, 1])*M[4, 5]).max())
print("     max |{T^a,y^mu} - s eta^{a mu} M^45| = %.2e" % dev)

dev = 0
for t in range(30):
    z = rand_z_pos(rng, rng.uniform(0.5, 3)); M = Mfun(z)
    yv = np.array([M[b, 5] for b in range(5)])
    r = M[:5, :5] @ (eta5 @ yv)
    dev = max(dev, np.abs(r).max())
print("(G2) max |M^{ab} y_b| (a,b=0..4) = %.2e" % dev)

Y0, Y4 = (float(os.environ.get('Y0', 5)), float(os.environ.get('Y4', 3)))
n = 2*np.sqrt(Y0**2 - Y4**2)
z0, resid = point_at_rest(n=n, seed=3)
M0 = Mfun(z0)
print("(G3) rest point y^a =", np.round([M0[a, 5] for a in range(5)], 6), " residual %.1e" % resid)
beta = np.arctanh(Y4/Y0)
Ub = None
for sign in (+1, -1):
    Ubt = expm(1j*sign*beta*Sig[0, 4])
    yb = Mfun(Ubt @ z0)[:5, 5]
    print("     boost sign %+d gives y^a =" % sign, np.round(yb, 6))
    if abs(abs(yb[4]) - Y4) < 1e-6:
        Ub = Ubt
        break
assert Ub is not None
yb = Mfun(Ub @ z0)[:5, 5]
gens = [(a, b) for a in range(1, 5) for b in range(a+1, 5)]
def rand_rot():
    U = np.eye(4, dtype=complex)
    for k in range(8):
        for (a, b) in gens:
            U = expm(1j*rng.uniform(0, 2*np.pi)*Sig[a, b]) @ U
    return U
Nf = 3000
cols = []
ydev = 0
for t in range(Nf):
    zz = Ub @ rand_rot() @ z0
    M = Mfun(zz)
    ydev = max(ydev, np.abs(M[:5, 5] - yb).max())
    cols.append(np.array([M[mu, rho] for mu in range(4) for rho in range(mu+1, 4)] + [M[mu, 4] for mu in range(4)]))
cols = np.array(cols)
print("     fibre samples: %d, max deviation of y^a from base value: %.2e" % (Nf, ydev))
sv = np.linalg.svd(cols, compute_uv=False)
print("     singular values of the 10 functions (M^{mu rho}, mu<rho; T^mu) over the fibre:", np.round(sv[:6], 6))
print("     fibre mean of M^{mu rho}, T^mu:", np.round(cols.mean(axis=0), 4))
Mmr = cols[:, :6]
U6, s6, Vh6 = np.linalg.svd(Mmr, full_matrices=False)
print("     singular values of the 6 functions M^{mu rho} alone:", np.round(s6, 6))
Wbasis = Vh6[:3]
np.save("Wy_numeric.npy", Wbasis)
Tm = cols[:, 6:]
coef, res, rk, svv = np.linalg.lstsq(Mmr, Tm, rcond=None)
print("     max residual expressing T^mu as linear combination of M^{mu rho}: %.2e" % np.abs(Mmr @ coef - Tm).max())
y4 = yb[4]; ysig = yb[:4]
def Mantisym(v):
    A = np.zeros((4, 4)); k = 0
    for mu in range(4):
        for rho in range(mu+1, 4):
            A[mu, rho] = v[k]; A[rho, mu] = -v[k]; k += 1
    return A
dev = 0
for row in cols[:50]:
    A = Mantisym(row[:6])
    pred = -(A @ (np.diag([-1., 1, 1, 1]) @ ysig))/y4
    dev = max(dev, np.abs(pred - row[6:]).max())
print("     max |T^mu + M^{mu sigma} y_sigma / y^4| = %.2e" % dev)

yv = yb.copy()
yl = eta5 @ yv
print("(G4) base point y^a =", np.round(yv, 6), " y.y =", np.round(yv @ yl, 6))
v = np.array([yv[4], 0, 0, 0, yv[0]])
assert abs(v @ eta5 @ yv) < 1e-9, v @ eta5 @ yv
v = v/np.sqrt(v @ eta5 @ v)
e = [np.eye(5)[i] for i in (1, 2, 3)]
def wedge(a, b):
    return np.outer(a, b) - np.outer(b, a)
def proj04(Wm):
    return np.array([Wm[mu, rho] for mu in range(4) for rho in range(mu+1, 4)])
best = None
for chi in (+1, -1):
    S = []
    for i in range(3):
        j, k = (i+1) % 3, (i+2) % 3
        S.append(proj04(wedge(e[i], v) + chi*wedge(e[j], e[k])))
    S = np.array(S)
    Q, _ = np.linalg.qr(S.T)
    resid = np.linalg.norm(Wbasis.T - Q @ (Q.T @ Wbasis.T))
    print("     chirality %+d: ||W_numeric - projection onto model span|| = %.2e" % (chi, resid))
    if best is None or resid < best[1]:
        best = (chi, resid)
print("     matching chirality:", best[0])
json.dump({"y": list(map(float, yv)), "chirality": int(best[0]), "s": s}, open("geometry_summary.json", "w"))

svT = np.linalg.svd(cols[:, 6:], compute_uv=False)
print("(G5) singular values of the four functions T^mu over the fibre:", np.round(svT, 6), "-> span dimension", int(np.sum(svT > 1e-8*svT[0])))
print("     y_mu T^mu over the fibre, max abs: %.2e" % np.abs(cols[:, 6:] @ (np.diag([-1., 1, 1, 1]) @ ysig)).max())
