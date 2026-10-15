"""
Fibre second moment <M^{ab} M^{cd}> (a,b,c,d = 0..4) over the S^2 fibre of the boosted base point y^a = (-5,0,0,0,-3), n = 8,
compared with kappa * sum_i S_i^{ab} S_i^{cd}, S_i = e_i ^ vhat + e_j ^ e_k (5D, chirality +1, vhat = (y^4,0,0,0,y^0)/ell).
This fixes the leading-order fibre average of the first-order response for fluctuations A^nu = c^nu_i(y) e^i(fibre), in particular for
the frame-type fluctuation A^nu = kappa^nu_sigma(y) T^sigma, where  <T^sigma M^{mu rho}>  is the (sigma 4) component of the same tensor.
"""
import numpy as np
from cp12_realisation import *
np.set_printoptions(precision=6, suppress=True, linewidth=150)
rng = np.random.default_rng(5)
eta5 = np.diag([-1., 1, 1, 1, 1])
n = 8.0
z0, resid = point_at_rest(n=n, seed=3)
beta = np.arctanh(3.0/5.0)
Ub = expm(1j*beta*Sig[0, 4])
yb = Mfun(Ub @ z0)[:5, 5]
assert abs(abs(yb[4]) - 3) < 1e-6
gens = [(a, b) for a in range(1, 5) for b in range(a+1, 5)]
def rand_rot():
    U = np.eye(4, dtype=complex)
    for k in range(8):
        for (a, b) in gens:
            U = expm(1j*rng.uniform(0, 2*np.pi)*Sig[a, b]) @ U
    return U
Nf = 6000
acc = np.zeros((5, 5, 5, 5)); mean = np.zeros((5, 5))
for t in range(Nf):
    M = Mfun(Ub @ rand_rot() @ z0)[:5, :5]
    acc += np.einsum('ab,cd->abcd', M, M); mean += M
acc /= Nf; mean /= Nf
v = np.array([yb[4], 0, 0, 0, yb[0]]); v = v/np.sqrt(v @ eta5 @ v)
e = [np.eye(5)[i] for i in (1, 2, 3)]
def wedge(a, b): return np.outer(a, b) - np.outer(b, a)
S = [wedge(e[i], v) + wedge(e[(i+1) % 3], e[(i+2) % 3]) for i in range(3)]
model = sum(np.einsum('ab,cd->abcd', Si, Si) for Si in S)
kappa = np.sum(acc*model)/np.sum(model*model)
print("y^a =", yb, " fibre mean max |<M^ab>| = %.3f (Monte Carlo, %d samples)" % (np.abs(mean).max(), Nf))
print("fitted kappa = %.4f" % kappa)
print("relative deviation ||<MM> - kappa*model|| / ||<MM>|| = %.3e  (Monte Carlo noise ~ %.1e)" % (np.linalg.norm(acc - kappa*model)/np.linalg.norm(acc), 1/np.sqrt(Nf)))
