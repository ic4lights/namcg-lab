"""
Exact kinematics of the SO(4,2)-covariant six-dimensional leaf (a coadjoint orbit CP^{1,2}), D = 4 matrices, in NAMCG notation.
Realisation: z in C^4, Hermitian form H of signature (2,2), constraint z^dagger H z = n (>0), U(1) quotient.
   M^{AB}(z) = z^dagger H Sigma^{AB} z   (15 real functions),  Sigma^{AB} = (i/4)[Gamma^A, Gamma^B] on a chiral 4-block,
   eta = diag(-1,1,1,1,1,-1)  (A = 0..5; 0..3 Lorentz, 4 spacelike, 5 timelike).
Poisson bracket {z^a, zbar^b} = -i (H^{-1})^{ab}.   Matrices (background): T^a = M^{a4}/R, a = 0..3.
Base (position) functions: x^mu = M^{mu 5}/R, mu = 0..3.     R = 1 below (scale).
Frame  E^{a mu} = {T^a, x^mu},   K^{mu nu} = eta_{ab} E^{a mu} E^{b nu}   (operator tensor for functions of x^mu).
Checks:  (1) Lie-Poisson algebra holds with a constant s = +-1;  (2) E^{a mu} = s eta^{a mu} M^{45}/R^2 exactly, hence
K^{mu nu} = (M^{45})^2 eta^{mu nu} / R^4 pointwise (no fibre average needed);  (3) x^mu are four independent functions on the
six-dimensional leaf (rank of {x^mu, M^{AB}} is 4; rank of the Poisson matrix of the 15 generators is 6);  (4) x^4 := M^{45}/R
is a function of x^mu alone on the leaf (x_a x^a constant);  (5) the 6x6 operator tensor K_L^{ij} = eta_{ab}{T^a,f^i}{T^b,f^j}
for local coordinates f = (x^mu, 2 fibre functions) has rank 4;  (6) the fibre average (Haar average over the SO(4) stabiliser
of a point of H^4) of the Lorentz generators M^{mu nu} vanishes.
"""
import numpy as np
from itertools import product

np.set_printoptions(precision=6, suppress=True, linewidth=140)
rng = np.random.default_rng(5)

# ---- gamma matrices for signature (4,2): euclidean 8x8 gammas, two of them multiplied by i
s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]], complex); s3 = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2, dtype=complex)
def kron(*ms):
    out = np.array([[1]], complex)
    for m in ms:
        out = np.kron(out, m)
    return out
g = [kron(s1, I2, I2), kron(s2, I2, I2), kron(s3, s1, I2), kron(s3, s2, I2), kron(s3, s3, s1), kron(s3, s3, s2)]
for i in range(6):
    for j in range(6):
        ac = g[i] @ g[j] + g[j] @ g[i]
        assert np.allclose(ac, 2*np.eye(8)*(i == j))
Gam = [1j*g[0], g[1], g[2], g[3], g[4], 1j*g[5]]     # A = 0..5, squares (-1,+1,+1,+1,+1,-1)
eta = np.diag([-1., 1, 1, 1, 1, -1])
for A in range(6):
    for B in range(6):
        assert np.allclose(Gam[A] @ Gam[B] + Gam[B] @ Gam[A], 2*eta[A, B]*np.eye(8))
chir = np.eye(8, dtype=complex)
for A in range(6):
    chir = chir @ Gam[A]
w, v = np.linalg.eig(chir)
# chir^2 = +-1; pick eigenvalue with positive imaginary/real part to define a chiral 4-block
lam = w[0]
sel = np.where(np.abs(w - lam) < 1e-9)[0]
Vc, _ = np.linalg.qr(v[:, sel])
assert Vc.shape[1] == 4
Sig = np.zeros((6, 6, 4, 4), complex)
for A in range(6):
    for B in range(6):
        S8 = 0.25j*(Gam[A] @ Gam[B] - Gam[B] @ Gam[A])
        Sig[A, B] = Vc.conj().T @ S8 @ Vc
        assert np.allclose(S8 @ Vc, Vc @ Sig[A, B])     # chiral block is invariant
# invariant Hermitian form H:  Sigma^dagger H = H Sigma  for all A,B
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
    cols.append(np.concatenate([ (Sig[A, B].conj().T @ Bm - Bm @ Sig[A, B]).flatten() for A in range(6) for B in range(A+1, 6)]))
Mall = np.array(cols).T
Mall = np.vstack([Mall.real, Mall.imag])
u, sv, vh = np.linalg.svd(Mall)
print('smallest singular values of the H-equation:', np.round(sv[-3:], 12))
cvec = vh[-1]
H = sum(c*Bm for c, Bm in zip(cvec, basis))
H = H/np.max(np.abs(H))
ev = np.linalg.eigvalsh(H)
print('smallest singular values of the H-equation:', np.round(sv[-3:], 12), ' eigenvalues of H:', np.round(ev, 6))
assert np.allclose(H.conj().T, H) and np.sum(ev > 0) == 2 and np.sum(ev < 0) == 2
for A in range(6):
    for B in range(6):
        assert np.allclose(Sig[A, B].conj().T @ H, H @ Sig[A, B])
Hi = np.linalg.inv(H)
P = np.array([[H @ Sig[A, B] for B in range(6)] for A in range(6)])   # M^{AB} = z^dag P z

def Mfun(z):
    return np.array([[np.real(z.conj() @ P[A, B] @ z) for B in range(6)] for A in range(6)])

def br_mat(Pm, Qm, z):
    # {F,G}, F = zbar P z, G = zbar Q z;  {z^a, zbar^b} = -i Hi^{ab}
    zb = z.conj()
    return np.real(-1j*((zb @ Pm) @ Hi @ (Qm @ z) - (zb @ Qm) @ Hi @ (Pm @ z)).item()) if False else \
        np.real(-1j*(((zb @ Pm) @ Hi @ (Qm @ z)) - ((zb @ Qm) @ Hi @ (Pm @ z))))

def PB(A, B, C, D, z):
    return br_mat(P[A, B], P[C, D], z)

def lie(A, B, C, D, M):
    return eta[A, C]*M[B, D] - eta[A, D]*M[B, C] - eta[B, C]*M[A, D] + eta[B, D]*M[A, C]

def rand_z(n=1.0):
    z = rng.normal(size=4) + 1j*rng.normal(size=4)
    q = np.real(z.conj() @ H @ z)
    if q < 0:
        z = np.array([z[0], z[1], z[2], z[3]])
        z = Hi @ z.conj()*0 + z   # placeholder, replaced below
    return z

def rand_z_pos(n=1.0):
    while True:
        z = rng.normal(size=4) + 1j*rng.normal(size=4)
        q = np.real(z.conj() @ H @ z)
        if q > 0.1:
            return z*np.sqrt(n/q)

# (1) Lie-Poisson algebra with constant s
ratios = []
for t in range(30):
    z = rand_z_pos()
    M = Mfun(z)
    for (A, B, C, D) in [(0, 4, 1, 5), (2, 4, 2, 5), (0, 1, 1, 2), (3, 4, 3, 5), (1, 2, 2, 5), (0, 5, 0, 4)]:
        lhs = PB(A, B, C, D, z); rhs = lie(A, B, C, D, M)
        if abs(rhs) > 1e-6:
            ratios.append(lhs/rhs)
ratios = np.array(ratios)
print('(1) {M^AB,M^CD} / (Lie-structure expression): min %.6f max %.6f over %d samples' % (ratios.min(), ratios.max(), len(ratios)))
s = np.sign(ratios.mean())*round(abs(ratios.mean()))
print('    constant s =', s)

# (2) frame and operator tensor at random leaf points
maxdev = 0; maxdevK = 0
etam = np.diag([-1., 1, 1, 1])
for t in range(40):
    z = rand_z_pos(rng.uniform(0.5, 3.0))
    M = Mfun(z)
    E = np.array([[PB(a, 4, mu, 5, z) for mu in range(4)] for a in range(4)])    # E^{a mu} (R = 1)
    pred = s*np.diag([-1., 1, 1, 1])*M[4, 5]                                      # s eta^{a mu} M^{45}
    maxdev = max(maxdev, np.abs(E - pred).max())
    Kmn = E.T @ etam @ E
    maxdevK = max(maxdevK, np.abs(Kmn - (M[4, 5]**2)*np.diag([-1., 1, 1, 1])).max())
print('(2) max |E^{a mu} - s eta^{a mu} M^{45}| = %.2e ;  max |K^{mu nu} - (M^{45})^2 eta^{mu nu}| = %.2e' % (maxdev, maxdevK))

# (3) independence of x^mu and rank of the Poisson matrix of the 15 generators
pairs = [(A, B) for A in range(6) for B in range(A+1, 6)]
z = rand_z_pos()
Pm = np.array([[PB(a[0], a[1], b[0], b[1], z) for b in pairs] for a in pairs])
print('(3) rank of the 15x15 Poisson matrix of the generators:', np.linalg.matrix_rank(Pm, tol=1e-9))
xi = [pairs.index((mu, 5)) for mu in range(4)]
print('    rank of {x^mu, M^AB} (4 x 15):', np.linalg.matrix_rank(Pm[xi, :], tol=1e-9))

# (4) x^4 = M^{45} as a function of x^mu: x_a x^a (a = 0..4, eta_{ab}) on the leaf
vals = []
for t in range(10):
    n = 1.0
    z = rand_z_pos(n)
    M = Mfun(z)
    xs = np.array([M[a, 5] for a in range(5)])
    vals.append(np.sum(np.diag([-1., 1, 1, 1, 1])*np.outer(xs, xs)*np.eye(5)))
print('(4) x_a x^a (a=0..4) at n=1, 10 samples:', np.round(vals, 8))
for n in (0.5, 2.0):
    z = rand_z_pos(n); M = Mfun(z); xs = np.array([M[a, 5] for a in range(5)])
    print('    n = %.1f: x_a x^a = %.8f' % (n, np.sum(np.diag([-1., 1, 1, 1, 1])*xs**2)))

# (5) six-dimensional operator tensor with local coordinates f = (x^0..x^3, two fibre functions)
z = rand_z_pos()
fidx = [pairs.index((mu, 5)) for mu in range(4)]
# add two generators giving independent differentials: choose from remaining pairs by rank test
dP = Pm[fidx, :]
cand = [p for p in pairs if p not in [(mu, 5) for mu in range(4)]]
chosen = []
for c in cand:
    trial = fidx + [pairs.index(c) for c in chosen] + [pairs.index(c)]
    # the generators' differentials d f restricted to the leaf: rank of Poisson rows
    if np.linalg.matrix_rank(Pm[trial, :], tol=1e-9) == len(trial):
        chosen.append(c)
    if len(chosen) == 2:
        break
f_all = fidx + [pairs.index(c) for c in chosen]
print('(5) local coordinates: x^0..x^3 and generators', chosen, ' rank of their Poisson rows:', np.linalg.matrix_rank(Pm[f_all, :], tol=1e-9))
V = np.array([[PB(a, 4, pairs[fi][0], pairs[fi][1], z) for fi in f_all] for a in range(4)])   # {T^a, f^i} (4 x 6)
KL = V.T @ etam @ V
print('    6x6 operator tensor K_L^{ij} = eta_ab {T^a,f^i}{T^b,f^j}: rank', np.linalg.matrix_rank(KL, tol=1e-9))
print('    its 4x4 base block equals (M^45)^2 eta^{-1}:', np.allclose(KL[:4, :4], (Mfun(z)[4, 5]**2)*np.diag([-1., 1, 1, 1])))

# (6) Haar average over the SO(4) stabiliser of a point of H^4: M^{mu nu} averages to zero
# find z0 with x^a = (x0, 0,0,0,0)
def stabiliser_average(nsamp=4000):
    # choose z0 by minimising sum_{a=1..4} x_a^2 over the orbit
    from scipy.optimize import minimize
    def obj(p):
        zz = p[:4] + 1j*p[4:]
        q = np.real(zz.conj() @ H @ zz)
        if q < 1e-6:
            return 1e6
        zz = zz*np.sqrt(1.0/q)
        M = Mfun(zz)
        return sum(M[a, 5]**2 for a in range(1, 5))
    best = None
    for t in range(20):
        r = minimize(obj, rng.normal(size=8), method='Nelder-Mead', options={'xatol': 1e-10, 'fatol': 1e-14, 'maxiter': 20000})
        if best is None or r.fun < best.fun:
            best = r
    zz = best.x[:4] + 1j*best.x[4:]
    zz = zz*np.sqrt(1.0/np.real(zz.conj() @ H @ zz))
    return zz, best.fun
z0, resid = stabiliser_average()
M0 = Mfun(z0)
print('(6) point with x^a ~ (x0,0,0,0,0): residual', resid, ' x^a =', np.round([M0[a, 5] for a in range(5)], 5))
from scipy.linalg import expm
gens = [(a, b) for a in range(1, 5) for b in range(a+1, 5)]   # so(4) on indices 1..4
acc = np.zeros((6, 6)); N = 6000
for t in range(N):
    # random SO(4) element: product of exponentials with random angles (approximate Haar by many random compositions)
    U = np.eye(4, dtype=complex)
    for k in range(6):
        for (a, b) in gens:
            U = expm(1j*rng.uniform(0, 2*np.pi)*Sig[a, b]) @ U
    zz = U @ z0
    acc += Mfun(zz)
acc /= N
print('    fibre average of M^{AB} over the SO(4) orbit (max |entry| outside the M^{a5} block):',
      np.abs(acc[:5, :5]).max(), '  M^{a5} block (x^a):', np.round(acc[:5, 5], 4), ' unaveraged x^a:', np.round([M0[a, 5] for a in range(5)], 4))
