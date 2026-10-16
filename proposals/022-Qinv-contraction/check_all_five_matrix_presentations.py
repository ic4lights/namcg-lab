"""022 script 6: all six 5-matrix presentations X^A = M^{A c0}, A != c0 (contraction eta_AA of the SO(4,2) form), c0 = 0..5, plus the 4-matrix ones.
Reports for each: rank of H, centre rank, signature of the induced horizontal contraction h = c^T eta c, y.y (y^A = M^{A c0}) sign, and the flux ratio f2/f1
when h is definite (Euclidean) or the Lorentz invariants (I1,I2) when h is Lorentzian (1,3)/(3,1), split (2,2) otherwise.
"""
import numpy as np
from symbol_tools import *
rng = np.random.default_rng(21)
res = {}
for c0 in range(6):
    idx = [A for A in range(6) if A != c0]
    fields = [(A, c0) for A in idx]
    etas = [float(eta6[A,A]) for A in idx]
    sg = {}; rat = []; I1 = []; I2 = []; yy = []
    for t in range(25):
        z = rand_z_pos(rng, rng.uniform(0.5, 4))
        M0 = Mfun(z)
        yv = np.array([M0[A, c0] for A in idx]); yy.append(float(np.sum(np.array(etas) * yv ** 2)))
        r = symbol(M0, fields, etas)
        w, V = np.linalg.eigh(r['h'])
        key = (int(np.sum(w < -1e-9)), int(np.sum(w > 1e-9)), r['rank'], r['zrank'])
        sg[key] = sg.get(key, 0) + 1
        if key[0] == 0:
            hs = sqrtm_sym(r['h'])
            for ph in np.linspace(0, np.pi, 31):
                zeta = np.array([np.cos(ph), np.sin(ph)])
                F = np.einsum('ijk,k->ij', r['F'], zeta)
                f1, f2, p, rr = planes(hs @ F @ hs)
                rat.append(f2 / f1)
        elif key[0] in (1, 3):
            o = np.argsort(w) if key[0] == 1 else np.argsort(-w)
            Vo = V[:, o]; wo = w[o]; S = np.diag(np.sqrt(np.abs(wo)))
            for ph in np.linspace(0, np.pi, 11):
                zeta = np.array([np.cos(ph), np.sin(ph)])
                F = np.einsum('ijk,k->ij', r['F'], zeta)
                Ft = S @ Vo.T @ F @ Vo @ S
                E = Ft[0, 1:]; B = np.array([Ft[2, 3], Ft[3, 1], Ft[1, 2]])
                I1.append(B @ B - E @ E); I2.append(E @ B)
    print(f"c0={c0} (eta_c0c0={eta6[c0,c0]:+.0f}): (n_neg,n_pos,rank H,rank centre)->count {sg}; y.y in [{min(yy):.3f},{max(yy):.3f}]", end="")
    if rat: print(f"; Euclid h: f2/f1 in [{min(rat):.6f},{max(rat):.6f}]")
    elif I1: print(f"; Lorentz h: I1 range [{min(I1):.3g},{max(I1):.3g}], I2 range [{min(I2):.3g},{max(I2):.3g}]")
    else: print("")
