# s2e_d3_jacobian_num.py - numerical check, D=3 Hermitian eigenvalue-fibre map:
# exponent of det J at pairwise coincidence is 2 per pair (kinematic repulsion exponent).
# Run: python -I proposals/091-g-core-induced-pair-correlation/s2e_d3_jacobian_num.py
import numpy as np
rng = np.random.default_rng(91)

def givens(p, q, ang, ph):
    Uu = np.eye(3, dtype=complex); cc, ss = np.cos(ang), np.sin(ang)
    Uu[p, p] = cc; Uu[q, q] = cc; Uu[p, q] = np.exp(1j*ph)*ss; Uu[q, p] = -np.exp(-1j*ph)*ss
    return Uu

def coords(lam, angs, phs):
    Uu = givens(1, 2, angs[0], phs[0]) @ givens(0, 2, angs[1], phs[1]) @ givens(0, 1, angs[2], phs[2])
    Z = Uu @ np.diag(lam) @ Uu.conj().T
    return np.array([Z[0, 0].real, Z[1, 1].real, Z[2, 2].real,
                     Z[0, 1].real, Z[0, 1].imag, Z[0, 2].real, Z[0, 2].imag,
                     Z[1, 2].real, Z[1, 2].imag], dtype=float)

def detJ(lam, angs, phs, h=1e-5):
    pars = np.concatenate([lam, angs, phs])
    J = np.zeros((9, 9))
    for k in range(9):
        pp = pars.copy(); pp[k] += h
        pm = pars.copy(); pm[k] -= h
        J[:, k] = (coords(pp[:3], pp[3:6], pp[6:]) - coords(pm[:3], pm[3:6], pm[6:]))/(2*h)
    return np.linalg.det(J)

sl = []
for trial in range(5):
    lam = np.sort(rng.uniform(0.5, 3.0, 3)); angs = rng.uniform(0.1, 1.2, 3); phs = rng.uniform(0.1, 2.0, 3)
    vs = []
    for eps in np.logspace(-2, -5, 8):
        lm = lam.copy(); lm[0] = lm[1] + eps
        vs.append([np.log(abs(detJ(lm.copy(), angs, phs)) + 1e-300), np.log(eps)])
    sl.append(np.polyfit([v[1] for v in vs], [v[0] for v in vs], 1)[0])
print("D=3 slope of log|det J| vs log(eps) at lam1->lam2 (expect ~2):", np.round(sl, 3))
sl2 = []
for trial in range(3):
    lam3 = rng.uniform(1.0, 3.0); angs = rng.uniform(0.1, 1.2, 3); phs = rng.uniform(0.1, 2.0, 3)
    vs = []
    for eps in np.logspace(-2, -4, 6):
        lm = np.array([lam3 + 2*eps, lam3 + eps, lam3])
        vs.append([np.log(abs(detJ(lm.copy(), angs, phs)) + 1e-300), np.log(eps)])
    sl2.append(np.polyfit([v[1] for v in vs], [v[0] for v in vs], 1)[0])
print("D=3 triple-collision slope (expect ~6):", np.round(sl2, 3))
print("S2E DONE")
