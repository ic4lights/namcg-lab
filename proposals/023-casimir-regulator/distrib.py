"""023 script 6: relation between the horizontal distributions H4 = span{J^{a4}} (four-matrix class), H5 = span{J^{A5}} (SO(4,1)-covariant five-matrix class)
and the vertical bundle ker(dy) of the projection to the hyperboloid y^A = M^{A5}."""
import numpy as np
from symbol_tools import *
rng = np.random.default_rng(2)
def rk(X):
    s = np.linalg.svd(X, compute_uv=False); return int(np.sum(s > 1e-9 * s[0]))
for t in range(6):
    z = rand_z_pos(rng, rng.uniform(0.5, 3)); M0 = Mfun(z)
    V = {p: vec(M0, *p) for p in pairs}
    allT = np.array([V[p] for p in pairs]); u, sv, vh = np.linalg.svd(allT); Tn = vh[:6].T
    dy = np.array([Tn[pidx[(C, 5)], :] for C in range(5)])
    vert = np.linalg.svd(dy)[2][4:]
    H4 = np.array([V[(a, 4)] for a in range(4)]) @ Tn; H5 = np.array([V[(A, 5)] for A in range(5)]) @ Tn
    print("pt %d: rank H4=%d H5=%d (H4+H5)=%d (H4+vert)=%d (H5+vert)=%d" % (t, rk(H4), rk(H5), rk(np.vstack([H4, H5])), rk(np.vstack([H4, vert])), rk(np.vstack([H5, vert]))))
