"""023 script 5: pencil of the SO(4,1)-invariant symbols K41, K42 (and K31, Box4) on the leaf: generalised eigenvalues, definite interval for R_kappa = C41 - kappa*C42,
and the invariance of the splitting (independence of the orbit point)."""
import numpy as np, scipy.linalg as sl
from symbol_tools import *
from sym_signatures import forms, sig
rng = np.random.default_rng(23)
rows = []
for t in range(30):
    z = rand_z_pos(rng, rng.uniform(0.3, 5)); M0 = Mfun(z)
    y = M0[:5, 5]; e5 = np.diag([-1., 1, 1, 1, 1]); ell2 = -(y @ e5 @ y)
    rk, F = forms(M0)
    # pencil K41 v = lam K42 v   (K42 nondegenerate)
    lam = np.sort(np.real(sl.eig(F['C41'], F['C42'])[0]))
    # ratios relative to the scale: K42 base coefficient is proportional to ell2 : normalise by ell2
    w42 = np.linalg.eigvalsh(F['C42'])
    rows.append((ell2, lam, w42))
lams = np.array([r[1] for r in rows]); ell = np.array([r[0] for r in rows])
print("pencil K41 v = lam K42 v : generalised eigenvalues (sorted), over 30 random orbit points")
print("  min over points:", lams.min(axis=0)); print("  max over points:", lams.max(axis=0))
print("  max deviation from (1/2 x4, 1 x2):", np.max(np.abs(lams-np.array([0.5,0.5,0.5,0.5,1,1]))))
print("  => alpha'/alpha (4-fold) and beta'/beta (2-fold):", np.round(np.median(lams, axis=0), 12))
# definite interval
a_ratio = [x for x in np.median(lams, axis=0) if abs(x - 1) > 1e-6]
print("  distinct generalised eigenvalues:", sorted(set(np.round(np.median(lams, axis=0), 8))))
# test R_kappa
for kappa in [0.2, 0.45, 0.5, 0.55, 0.75, 0.95, 0.999, 1.0, 1.05]:
    sigs = set()
    for t in range(15):
        z = rand_z_pos(rng, rng.uniform(0.3, 5)); M0 = Mfun(z); rk, F = forms(M0)
        sigs.add(sig(F['C41'] - kappa * F['C42']))
    print("  kappa = %.3f : signature(n+,n-,n0) of K41 - kappa K42 over 15 points:" % kappa, sigs)
