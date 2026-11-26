"""025 script 1: classical fibre spin radius on the CP^{1,2} orbit (Poisson limit of the local cutoff s<=m of Manta-Steinacker 2502.02498 eq (70)).
At a point with y^A=M^{A5} (A<=4, y.y=-ell^2) the stabiliser SO(4)_y rotates the eta5-orthogonal complement of y. The fibre S^2 is a coadjoint orbit of SU(2)_L
with moment map = self-dual part of M restricted to that complement; its radius |L_L| is the classical spin bound (area=4 pi |L_L|). Compare with y^0, y^4, ell."""
import sys, numpy as np
sys.path.insert(0, r'../023-casimir-regulator')
from cp12_realisation import *
rng = np.random.default_rng(5)
e5 = np.diag([-1., 1, 1, 1, 1])
def eps4():
    import itertools
    e = np.zeros((4,4,4,4))
    for p in itertools.permutations(range(4)): e[p] = np.linalg.det(np.eye(4)[list(p)])
    return e
E4 = eps4()
print("   y0        y4       ell     |L+|     |L-|    |L+|/y0   |L+|/ell   |L+|^2-|L-|^2")
for t in range(10):
    z = rand_z_pos(rng, rng.uniform(0.5, 4)); M = Mfun(z)
    y = M[:5, 5]; ell = np.sqrt(-(y @ e5 @ y))
    yl = e5 @ y
    # eta5-orthonormal basis of the complement of y: vectors v with v.eta.y=0
    ns = np.linalg.svd(yl.reshape(1,5))[2][1:]            # rows v with yl.v=0
    G = ns @ e5 @ ns.T; w, V = np.linalg.eigh(G); B = (ns.T @ V / np.sqrt(w)).T  # eta-orthonormal (positive)
    Mup = M[:5,:5]
    Mp = B @ e5 @ Mup @ e5 @ B.T                            # components of M^{AB} on complement, lowered with eta
    # self-dual / anti-self-dual parts of 4x4 antisymmetric Mp
    D = 0.5*np.einsum('abcd,cd->ab', E4, Mp)
    Pp, Pm = 0.5*(Mp+D), 0.5*(Mp-D)
    Lp = 0.5*np.sqrt(np.sum(Pp**2)); Lm = 0.5*np.sqrt(np.sum(Pm**2))
    print("%8.4f %8.4f %8.4f %8.4f %8.4f %8.4f %8.4f %10.2e" % (y[0], y[4], ell, Lp, Lm, Lp/abs(y[0]), Lp/ell, Lp**2-Lm**2))
