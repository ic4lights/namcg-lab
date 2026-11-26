# mc101a.py -- item 101 probe: Haar-fibre MC for the D=3 conditional law of P2 = sum (G_ii/tau)^2
# given the spectrum, complex Wishart constant-variance class (Haar fibre of the 097 paragraph).
# Gate: the D=3 linear-form marginal of 096 (integrated, appH L3205) must match. Run: python -I mc101a.py
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
t = (dd[:, 0] - lam[2]) / (lam[0] - lam[2])         # scaled G_11, exact density 2 min(t/mu,(1-t)/(1-mu))
mu = (lam[1] - lam[2]) / (lam[0] - lam[2])
ed = np.linspace(0.01, 0.99, 26)
ht, et = np.histogram(t, bins=ed, density=True)
ex = 2 * np.minimum(ht[0:1] / mu, (1 - ht[0:1]) / (1 - mu))
zc = ht[0:1] / mu + (1 - ht[0:1]) / (1 - mu)        # var of indicator mixture for SE
se = np.sqrt(zc / (len(t) * np.diff(ed)))
gate = np.max(np.abs(ht - ex) / se)
print("gate 096-marginal: max z = %.2f (expect <4)" % gate)
P2 = (dd ** 2).sum(1) / tau ** 2
print("P2 mean sim %.6f vs moment mean (check below)" % P2.mean())
# E[P2] over Haar fibre: rows of |U|^2 are Dirichlet(1,1,1): E b_k^2=2/12, E b_k b_l=1/12
Ep2 = 3 * (2 * (p**2).sum() + ((p.sum()**2) - (p**2).sum())) / 12
print("E[P2] exact (1+sum p^2)/4 = %.6f" % ((1 + s2) / 4))
print("P2 mean sim %.6f vs moment mean (check below)" % P2.mean())
Ep2 = 0.0
# E[P2] over Haar fibre = E[sum d_i^2]: d_i = sum_k p_k b_ik, E b_ik=1/3, E b_ik^2 = 2/(3*4)=1/6,
# E b_ik b_il (k!=l) = (1/3)(1/(3+1))=1/12? Dirichlet(1,1,1): E b_k b_l = 1/(3*4) k!=l, E b_k^2=2/12
Ep2 = (( (p**2).sum() * (1/6 + 1/12) + 2 * (p.sum()**2 - (p**2).sum()) / 12 ) if True else 0)
Ep2 = ((p**2).sum() * (2/12 + 1/12) * 0 + sum(p[k]*p[l]*(2/12 if k == l else 1/12) for k in range(3) for l in range(3)) for i in range(1)).__iter__()
Ep2 = list(Ep2)[0]
print("P2 mean sim %.6f vs exact %.6f" % (P2.mean(), Ep2))
bd = np.linspace(1/3 + 1e-9, s2 - 1e-9, 25)
h2, e2 = np.histogram(P2, bins=bd, density=True)
np.save("p2_hist_101.npy", np.vstack([0.5*(e2[1:]+e2[:-1]), h2]))
print("P2 density table (center, dens):")
print(np.array2string(np.vstack([0.5*(e2[1:]+e2[:-1]), h2]).T, precision=4, max_line_width=140))
d12 = np.column_stack([dd[:, 0], dd[:, 1]]) / tau
g = np.linspace(0, 0.75, 26)
H, xe, ye = np.histogram2d(d12[:, 0], d12[:, 1], bins=[g, g], density=True)
np.save("d12_hist_101.npy", np.column_stack([0.5*(xe[1:]+xe[:-1]), 0.5*(ye[1:]+ye[:-1]), H.T]))
print("joint (d1,d2) saved; support box d1,d2 in (0, %.3f), d1+d2>1/3? min sum %.4f" % (g[-1], (d12.sum(1)).min()))
print("done mc101a")
