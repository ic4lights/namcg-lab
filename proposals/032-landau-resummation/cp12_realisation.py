"""
Shared realisation of the coadjoint orbit CP^{1,2} of SO(4,2) (same construction as proposals/011-fuzzy-leaf/check_covariant_leaf.py).
z in C^4, Hermitian form H of signature (2,2), constraint z^dag H z = n > 0, U(1) quotient.
M^{AB}(z) = z^dag H Sigma^{AB} z, eta = diag(-1,1,1,1,1,-1), A = 0..5.  Poisson bracket {z^a, zbar^b} = -i (H^{-1})^{ab}.
Matrices: T^a = M^{a4} (R=1);  base functions y^mu = M^{mu5}.
"""
import numpy as np
from scipy.linalg import expm

s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]], complex); s3 = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2, dtype=complex)
def kron(*ms):
    out = np.array([[1]], complex)
    for m in ms:
        out = np.kron(out, m)
    return out
g = [kron(s1, I2, I2), kron(s2, I2, I2), kron(s3, s1, I2), kron(s3, s2, I2), kron(s3, s3, s1), kron(s3, s3, s2)]
Gam = [1j*g[0], g[1], g[2], g[3], g[4], 1j*g[5]]
eta6 = np.diag([-1., 1, 1, 1, 1, -1])
chir = np.eye(8, dtype=complex)
for A in range(6):
    chir = chir @ Gam[A]
w, v = np.linalg.eig(chir)
lam = w[0]
sel = np.where(np.abs(w - lam) < 1e-9)[0]
Vc, _ = np.linalg.qr(v[:, sel])
Sig = np.zeros((6, 6, 4, 4), complex)
for A in range(6):
    for B in range(6):
        S8 = 0.25j*(Gam[A] @ Gam[B] - Gam[B] @ Gam[A])
        Sig[A, B] = Vc.conj().T @ S8 @ Vc
basis = []
for i in range(4):
    for j in range(i, 4):
        if i == j:
            Bm = np.zeros((4, 4), complex); Bm[i, i] = 1; basis.append(Bm)
        else:
            Bm = np.zeros((4, 4), complex); Bm[i, j] = 1; Bm[j, i] = 1; basis.append(Bm)
            Bm = np.zeros((4, 4), complex); Bm[i, j] = 1j; Bm[j, i] = -1j; basis.append(Bm)
cols = []
for Bm in basis:
    cols.append(np.concatenate([(Sig[A, B].conj().T @ Bm - Bm @ Sig[A, B]).flatten() for A in range(6) for B in range(A+1, 6)]))
Mall = np.array(cols).T
Mall = np.vstack([Mall.real, Mall.imag])
u, sv, vh = np.linalg.svd(Mall)
cvec = vh[-1]
H = sum(c*Bm for c, Bm in zip(cvec, basis))
H = H/np.max(np.abs(H))
Hi = np.linalg.inv(H)
P = np.array([[H @ Sig[A, B] for B in range(6)] for A in range(6)])

def Mfun(z):
    return np.array([[np.real(z.conj() @ P[A, B] @ z) for B in range(6)] for A in range(6)])

def br_mat(Pm, Qm, z):
    zb = z.conj()
    return np.real(-1j*(((zb @ Pm) @ Hi @ (Qm @ z)) - ((zb @ Qm) @ Hi @ (Pm @ z))))

def PB(A, B, C, D, z):
    return br_mat(P[A, B], P[C, D], z)

def lie(A, B, C, D, M):
    return eta6[A, C]*M[B, D] - eta6[A, D]*M[B, C] - eta6[B, C]*M[A, D] + eta6[B, D]*M[A, C]

def rand_z_pos(rng, n=1.0):
    while True:
        z = rng.normal(size=4) + 1j*rng.normal(size=4)
        q = np.real(z.conj() @ H @ z)
        if q > 0.1:
            return z*np.sqrt(n/q)

def point_at_rest(n=1.0, seed=0):
    """z0 on the orbit with y^a = M^{a5} = (-n/2, 0,0,0,0)."""
    from scipy.optimize import minimize
    rng = np.random.default_rng(seed)
    def obj(p):
        zz = p[:4] + 1j*p[4:]
        q = np.real(zz.conj() @ H @ zz)
        if q < 1e-6:
            return 1e6
        zz = zz*np.sqrt(n/q)
        M = Mfun(zz)
        return sum(M[a, 5]**2 for a in range(1, 5))
    best = None
    for t in range(20):
        r = minimize(obj, rng.normal(size=8), method='Nelder-Mead', options={'xatol': 1e-12, 'fatol': 1e-18, 'maxiter': 40000})
        if best is None or r.fun < best.fun:
            best = r
    zz = best.x[:4] + 1j*best.x[4:]
    zz = zz*np.sqrt(n/np.real(zz.conj() @ H @ zz))
    return zz, best.fun
