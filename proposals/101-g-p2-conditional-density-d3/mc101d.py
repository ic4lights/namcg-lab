# mc101d.py -- item 101: density-shape check at the SECOND spectrum lam=(0.7,0.25,0.05):
# 800k-sample Haar MC diagonal grid vs exact rho_hat (C = 2/117... C = 1/Z = 4000/117), grid 120x120
# over [0,1]^2 restricted to support cells. Reports E[P2], negative cells on MC support, shape corr.
# Run: python -I mc101d.py
import numpy as np, itertools
L = np.array([0.7, 0.25, 0.05]); C = 4000.0/117.0
perms = list(itertools.permutations(range(3)))
SG = np.array([-1 if sum(1 for i in range(3) for j in range(i+1,3) if p[i]>p[j]) % 2 else 1 for p in perms])
WL = np.array([[L[p[0]], L[p[1]]] for p in perms])
def rho_vec(d1, d2):
    tot = np.zeros(np.broadcast(d1, d2).shape)
    for k in range(6):
        g1 = WL[k,0] - d1; g2 = WL[k,1] - d2
        tot = tot + SG[k] * np.where((g1 > 0) & (g1 + g2 > 0), np.minimum(g1, g1 + g2), 0.0)
    return C * tot
rng = np.random.default_rng(101202617)
N = 800_000
A = (rng.standard_normal((N,3,3)) + 1j*rng.standard_normal((N,3,3)))/np.sqrt(2)
Q, Rr = np.linalg.qr(A); dr = np.diagonal(Rr, axis1=1, axis2=2)
b = np.abs(Q * (dr/np.abs(dr))[:, None, :])**2
d = b @ L
print("mean d_i:", d.mean(0), " exact 0.3333; E[P2] = %.6f exact %.6f +-%.6f" %
      ((d**2).sum(1).mean(), (1+ (L**2).sum())/4, (d**2).sum(1).std()/np.sqrt(N)))
M = 120; ed = np.linspace(0, 1, M+1); cc = 0.5*(ed[1:]+ed[:-1])
D1, D2 = np.meshgrid(cc, cc, indexing="ij")
H, _, _ = np.histogram2d(d[:,0], d[:,1], bins=[ed, ed])
H = H/N/(ed[1]-ed[0])**2
ex = rho_vec(D1, D2)
msk = H > 50/(N*(ed[1]-ed[0])**2)
print("cells with MC support:", msk.sum(), " negative exact cells on support:", int((ex[msk] < -1e-9).sum()))
print("min exact on support: %.3e" % ex[msk].min())
v1 = H[msk].ravel(); v2 = ex[msk].ravel()
print("shape corr: %.4f" % np.corrcoef(v1, v2)[0,1])
w = np.trapezoid(np.trapezoid(np.clip(ex,0,None), cc, axis=1), cc)
print("C*rho trapz over plane: %.5f  (target 1.0)" % w)
print("done mc101d")
