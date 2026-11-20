# s3_mc_checks_v2.py - Monte Carlo confirmation (numerical, not proof) for proposal 091.
# (1) Wishart W_2(4) edge Gram (M=2, N=6, a=3): u=|p1-p2| coincidence exponent ~2;
#     tau-density exponent near 0 ~ 2a = 6; E[u^2] flat across tau deciles (separation);
#     flat value E[u^2] = 3/(2a+3) = 1/3 at a = 3.
# (2) Kinematic universality: heterogeneous column variances keep coincidence exponent 2.
# (3) Rank-one slot law: normalized squared moduli of 3 iid complex normals = flat Dirichlet moments.
# Run: python -I proposals/091-g-core-induced-pair-correlation/s3_mc_checks_v2.py
import numpy as np
rng = np.random.default_rng(93)
n = 200_000

def block(M, cols, scales):
    A = (rng.standard_normal((n, M, cols)) + 1j*rng.standard_normal((n, M, cols)))/np.sqrt(2)
    return A * np.sqrt(scales)

def eig2(A):
    G = A @ A.conj().transpose(0, 2, 1)
    tr = np.trace(G, axis1=1, axis2=2); dt = np.linalg.det(G)
    rad = np.sqrt(np.maximum(tr**2/4 - dt, 0))
    return tr/2 + rad, tr/2 - rad

def slope_near0(vals, nmax, nb):
    v = vals[vals < nmax]
    edges = np.logspace(-3.0, np.log10(nmax), nb + 1)
    h, _ = np.histogram(v, edges)
    cen = 0.5*(edges[:-1] + edges[1:]); ok = h > 0
    return np.polyfit(np.log(cen[ok]), np.log(h[ok]/v.size/np.diff(edges)[ok]), 1)[0]

A = block(2, 4, np.ones(4)); l1, l2 = eig2(A)
tau = l1 + l2; uu = (l1 - l2)/tau
print("(1a) exponent of u near 0, iid block (expect ~2):", round(slope_near0(uu, 0.25, 30), 3))
print("(1b) exponent of tau near 0 (expect ~2a = 6):", round(slope_near0(tau, 0.3, 25), 3))
order = np.argsort(tau); dec = np.array_split(order, 12)
print("(1c) E[u^2] by tau-decile (expect flat, = 3/(2a+3) = 1/3 at a=3):",
      np.round([np.mean(uu[d]**2) for d in dec], 3))
A = block(2, 4, np.array([1.0, 4.0, 9.0, 16.0])); l1, l2 = eig2(A)
uu2 = (l1 - l2)/(l1 + l2)
print("(2) coincidence exponent, heterogeneous column variances (expect ~2):", round(slope_near0(uu2, 0.2, 28), 3))
w = rng.standard_normal((100_000, 3)) + 1j*rng.standard_normal((100_000, 3))
E = np.abs(w)**2; p = E/E.sum(1, keepdims=True)
print("(3) rank-one slot moments (expect 0.3333, 0.1667, 0.0833):",
      np.round([p[:, 0].mean(), (p[:, 0]**2).mean(), (p[:, 0]*p[:, 1]).mean()], 4))
print("S3-V2 DONE")
