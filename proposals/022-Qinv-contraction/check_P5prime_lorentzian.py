"""022 script 5: Lorentzian-base variant of the 5-matrix presentation: X^A = M^{A4}, A in {0,1,2,3,5} (stabiliser SO(3,2); base = AdS_4-type quadric),
contraction eta_AB = diag(-1,1,1,1,-1).  Reports the signature of the induced horizontal contraction h and the Lorentz invariants of the vertical flux
(E,B in an h-orthonormal frame): I1 = B^2 - E^2, I2 = E.B.  A real flux with f1=f2 Landau structure needs a Euclidean h; a Lorentzian h gives E/B-type fields."""
import numpy as np
from symbol_tools import *
rng = np.random.default_rng(8)
idx = [0, 1, 2, 3, 5]
fields = [(A, 4) for A in idx]
etas = [-1., 1, 1, 1, -1]
sigs = {}
inv = []
for t in range(40):
    z = rand_z_pos(rng, rng.uniform(0.5, 4))
    M0 = Mfun(z)
    r = symbol(M0, fields, etas)
    h = r['h']
    w, V = np.linalg.eigh(h)
    key = (int(np.sum(w < -1e-9)), int(np.sum(w > 1e-9)))
    sigs[(key, r['rank'], r['zrank'])] = sigs.get((key, r['rank'], r['zrank']), 0) + 1
    if key == (1, 3) or key == (3, 1):
        # order: timelike first
        o = np.argsort(w) if key == (1, 3) else np.argsort(-w)
        Vo = V[:, o]; wo = w[o]
        S = np.diag(np.sqrt(np.abs(wo)))
        for ph in np.linspace(0, np.pi, 7):
            zeta = np.array([np.cos(ph), np.sin(ph)])
            F = np.einsum('ijk,k->ij', r['F'], zeta[:r['zrank']])
            Ft = S @ Vo.T @ F @ Vo @ S                       # components in h-orthonormal frame (index 0 timelike)
            E = Ft[0, 1:]; B = np.array([Ft[2, 3], Ft[3, 1], Ft[1, 2]])
            inv.append((B @ B - E @ E, E @ B, np.linalg.norm(E), np.linalg.norm(B)))
print("signature (n_neg,n_pos) of h, rank H, rank centre ->count:", sigs)
inv = np.array(inv)
if len(inv):
    print("Lorentz invariants over samples: I1=B^2-E^2 range", inv[:, 0].min(), inv[:, 0].max(), " I2=E.B range", inv[:, 1].min(), inv[:, 1].max())
    print("relative |I1|/(E^2+B^2) max:", np.max(np.abs(inv[:, 0]) / (inv[:, 2] ** 2 + inv[:, 3] ** 2)), " |I2|/(|E||B|) max:", np.max(np.abs(inv[:, 1]) / (inv[:, 2] * inv[:, 3])))
