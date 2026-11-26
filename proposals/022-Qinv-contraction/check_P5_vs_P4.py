"""022 script 2: contraction induced on the horizontal space and flux eigenvalues f1,f2 for
  P4: matrices T^a = M^{a4}, a=0..3, contraction eta_ab   (manuscript's CP^{1,2} class)
  P5: matrices X^A = M^{A5}, A=0..4, contraction eta_AB = diag(-1,1,1,1,1) (SO(4,1)-covariant presentation, 'fifth field' included)
For each: rank of H, centre rank, signature of h = c^T eta c, flux of the operator sum eta_I D^I D^I in an h-orthonormal frame,
ratio f2/f1 over zeta directions, and SD/ASD content.  Euclidean continuation eta->delta also reported for P4.
"""
import numpy as np
from symbol_tools import *
np.set_printoptions(precision=6, suppress=True, linewidth=170)
eta4 = [-1., 1, 1, 1]; eta5 = [-1., 1, 1, 1, 1]
rng = np.random.default_rng(3)
P4f = [(a, 4) for a in range(4)]
P5f = [(A, 5) for A in range(5)]
rows = []
worst = dict(P5_ratio=0, P5_signdef=0, P5_resid=0, P4E_min=9, P4E_max=0, P4_lorentz=0)
for t in range(60):
    z = rand_z_pos(rng, rng.uniform(0.5, 4))
    M0 = Mfun(z)
    y = M0[:5, 5]; yl = np.diag(eta5) @ y; ell2 = -(y @ yl)
    # ---- P5
    r5 = symbol(M0, P5f, eta5)
    h5 = r5['h']; ev5 = np.linalg.eigvalsh(h5)
    # y . D = 0 relation
    rel = sum(eta5[A] * M0[A, 5] * vec(M0, A, 5) for A in range(5))
    worst['P5_resid'] = max(worst['P5_resid'], r5['resid'], np.max(np.abs(rel)))
    worst['P5_signdef'] = max(worst['P5_signdef'], 0 if ev5.min() > 0 else 1)
    hs = sqrtm_sym(h5)
    rat = []
    for ph in np.linspace(0, np.pi, 61):
        zeta = np.array([np.cos(ph), np.sin(ph)])
        F = np.einsum('ijk,k->ij', r5['F'], zeta[:r5['zrank']])
        Ft = hs @ F @ hs
        f1, f2, p, r = planes(Ft)
        rat.append(f2 / f1 if f1 > 0 else 1.0)
    worst['P5_ratio'] = max(worst['P5_ratio'], 1 - min(rat))
    # ---- P4 with Euclid delta and Lorentz eta
    r4 = symbol(M0, P4f, [1., 1, 1, 1])
    rat4 = []
    for ph in np.linspace(0, np.pi, 61):
        zeta = np.array([np.cos(ph), np.sin(ph)])
        F = np.einsum('ijk,k->ij', r4['F'], zeta)
        hs4 = sqrtm_sym(r4['h'])
        f1, f2, p, r = planes(hs4 @ F @ hs4)
        rat4.append(f2 / f1)
    worst['P4E_min'] = min(worst['P4E_min'], min(rat4)); worst['P4E_max'] = max(worst['P4E_max'], max(rat4))
    rows.append((r5['rank'], r5['zrank'], ev5, r4['rank'], r4['zrank']))
print("P5: ranks (H, centre) over sample:", set((r[0], r[1]) for r in rows))
print("P5: h = c^T eta c eigenvalues (first 3 samples):"); [print("   ", r[2]) for r in rows[:3]]
print("P5: min over sample of smallest eigenvalue of h:", min(r[2].min() for r in rows), "(>0 means Euclidean horizontal contraction)")
print("P5: max residual of  S = c F c^T and of y_A D^A = 0:", worst['P5_resid'])
print("P5: max over points,zeta of (1 - f2/f1):", worst['P5_ratio'])
print("P4: ranks (H,centre):", set((r[3], r[4]) for r in rows))
print("P4 (eta->delta): f2/f1 range over sample:", worst['P4E_min'], worst['P4E_max'])
