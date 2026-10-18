"""027 script 6: structural identities in whitened coordinates at 60 random orbit points of CP^{1,2}:
 (i) eig(S_uu) = (-c, a, a, a) with c = 1/2 (kappa-independent normalisation of this script's whitening: |u|^2 = alpha q_b) and c/a = ell^2/(y4)^2;
 (ii) w = S_uu^{-1} S_uz maps R^2 conformally (both singular values equal) with |w|^2 = 1 + c/a = coth^2(tau);   (iii) image(w) is orthogonal to the time eigenvector of S_uu (q purely spatial);
 (iv) the inner ball B(w z, |z|) of the window is therefore tangent to the null cone of Q_L: distance from the apex to the cone ridge equals r*sqrt(1+c/a)."""
import numpy as np
from cone_window_geometry import *
rng = np.random.default_rng(101)
e5 = np.diag([-1., 1, 1, 1, 1])
mx = np.zeros(6)
for t in range(60):
    z = rand_z_pos(rng, rng.uniform(0.3, 6)); M0 = Mfun(z); y = M0[:5, 5]
    ell2 = -(y @ e5 @ y); m2 = y[4]**2
    r = analyse(M0)
    ev, O = np.linalg.eigh(r['S'][:4, :4])
    c = -ev[0]; a = ev[1:]
    sv = np.linalg.svd(r['w'], compute_uv=False)
    q = O.T @ r['w']
    mx[0] = max(mx[0], abs(c - 0.5)); mx[1] = max(mx[1], np.ptp(a)/a.mean()); mx[2] = max(mx[2], abs(c/a.mean() - ell2/m2)/(ell2/m2))
    mx[3] = max(mx[3], abs(sv[0] - sv[1])); mx[4] = max(mx[4], abs(sv[0]**2 - 1 - ell2/m2)); mx[5] = max(mx[5], np.max(np.abs(q[0]))/np.max(np.abs(q)))
print("max deviations over 60 points: |c-1/2| %.2e | spread of a_k %.2e | rel. dev. of c/a from ell^2/y4^2 %.2e | |sv1-sv2| %.2e | | |w|^2-1-ell^2/y4^2 | %.2e | time component of image(w) (relative) %.2e" % tuple(mx))
