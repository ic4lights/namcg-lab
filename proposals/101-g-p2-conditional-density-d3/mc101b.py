# mc101b.py -- item 101 probe (clean; supersedes broken-patch mc101a.py). Haar-fibre MC for the
# D=3 conditional law of P2 = sum (G_ii/tau)^2 given the spectrum (constant-variance class:
# conditional eigenbasis law is Haar, established 097). Gates: (1) 096 D=3 linear-form marginal;
# (2) exact E[P2] = (1+sum p^2)/4 from Dirichlet(1,1,1) row moments. Run: python -I mc101b.py
import numpy as np
rng = np.random.default_rng(101202603)
lam = np.array([6.0, 3.0, 1.0]); tau = lam.sum(); p = lam / tau; s2 = (p**2).sum()
def haarU(n, N):
    A = (rng.standard_normal((N, n, n)) + 1j * rng.standard_normal((N, n, n))) / np.sqrt(2)
    Q, R = np.linalg.qr(A)
    d = np.diagonal(R, axis1=1, axis2=2)
    return Q * (d / np.abs(d))[:, None, :]        # Q @ diag(phases): standard Haar fix
U = haarU(3, 600_000)
b = np.abs(U) ** 2                                  # rows: |u_ik|^2
dd = b @ lam                                        # d_i * tau = (U lam U^dag)_ii
t = (dd[:, 0] - lam[2]) / (lam[0] - lam[2])         # scaled G_11 in (0,1), density 2min(t/mu,(1-t)/(1-mu))
mu = (lam[1] - lam[2]) / (lam[0] - lam[2])
ed = np.linspace(0.01, 0.99, 26)
ht, et = np.histogram(t, bins=ed, density=True)
tc = 0.5 * (ed[:-1] + ed[1:])
ex = 2 * np.minimum(tc / mu, (1 - tc) / (1 - mu))
zc = tc / mu + (1 - tc) / (1 - mu)                  # second moment of the mixture indicator
se = np.sqrt(zc / (len(t) * np.diff(ed)))
print("gate1 096-marginal: max z = %.2f (expect <4)" % np.max(np.abs(ht - ex) / se))
P2 = (dd ** 2).sum(1) / tau ** 2
Ep2 = 3 * (2 * s2 + (1.0 - s2)) / 12
print("gate2 E[P2]: sim %.6f exact %.6f (sd %.5f over %.0f samples -> z=%.2f)"
      % (P2.mean(), Ep2, P2.std(), len(P2), abs(P2.mean() - Ep2) / (P2.std() / np.sqrt(len(P2)))))
bd = np.linspace(1 / 3 + 1e-9, s2 - 1e-9, 25)
h2, e2 = np.histogram(P2, bins=bd, density=True)
np.save("p2_hist_101.npy", np.vstack([0.5 * (e2[1:] + e2[:-1]), h2]))
print("P2 density (center dens):")
print(np.array2string(np.vstack([0.5 * (e2[1:] + e2[:-1]), h2]).T, precision=4, max_line_width=140))
d12 = dd / tau
g = np.linspace(0.0, 0.75, 31)
H, xe, ye = np.histogram2d(d12[:, 0], d12[:, 1], bins=[g, g], density=True)
np.save("d12_hist_101.npy", np.column_stack([0.5 * (xe[1:] + xe[:-1]), 0.5 * (ye[1:] + ye[:-1]), H.T]))
print("joint (d1,d2) saved to d12_hist_101.npy; d1 range sim (%.4f,%.4f)" % (d12[:, 0].min(), d12[:, 0].max()))
print("done mc101b")
