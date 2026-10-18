"""Shared geometry for 028: Hamiltonian fields, Poisson bivector, symbol data at points of CP^{1,2}; fibre points by the stabiliser SO(4) of y."""
import numpy as np, scipy.linalg as sl
from symbol_tools import *            # vec, pairs, pidx, s, eta6, lie, Mfun, rand_z_pos ...
from sym_signatures import forms
eta4 = np.diag([-1., 1, 1, 1])

def geometry(M0):
    V = np.array([vec(M0, *p) for p in pairs])             # (15,15) row p = components of Ham field of M^p in R^15
    u, sv, vh = np.linalg.svd(V)
    E = vh[:6]                                             # (6,15)
    assert sv[5] > 1e-9*sv[0] and sv[6] < 1e-9*sv[0]
    c = V @ E.T                                            # (15,6): Ham field of M^p in tangent coordinates
    return V, E, c

def poisson_bivector(M0):
    V, E, c = geometry(M0)
    # covector of dM^p is E[:,p]; Ham field Pi e_p = c[p]  ->  Pi = C E^T with C = c.T (6x15)
    Pi = c.T @ E.T
    return Pi, c, E

def window_forms(M0, kappa=0.75):
    rk, Fm = forms(M0)
    # forms() uses its own SVD basis; recompute in OUR basis to keep coordinates consistent
    V, E, c = geometry(M0)
    def K(sel, wfun):
        return sum(wfun(p)*np.outer(c[pidx[p]], c[pidx[p]]) for p in pairs if sel(p))
    eta = lambda p: eta6[p[0], p[0]]*eta6[p[1], p[1]]
    K42 = K(lambda p: True, eta); K41 = K(lambda p: p[1] <= 4, eta)
    Box = K(lambda p: p[1] == 4 and p[0] <= 3, eta)
    P = K41 - kappa*K42                                     # -sigma(Delta_kappa) = K41 - kappa K42
    return dict(K42=K42, K41=K41, Box=Box, P=P)

def fields(M0):
    Pi, c, E = poisson_bivector(M0)
    W = np.array([c[pidx[(a, 4)]] for a in range(4)])      # W_a = Ham field of T^a = M^{a4}   (4,6)
    Yb = np.array([c[pidx[(m, 5)]] for m in range(4)])     # Ham field of y^mu = M^{mu5}
    return Pi, W, Yb, c, E

def orbit_point_rest(a_target=None, seed=0):
    z, res = point_at_rest(1.0, seed)
    return z

# ---- fibre points: Ad action of the stabiliser of y inside SO(4,1) on the 6x6 matrix M^{AB} (indices up, eta6 metric)
def stab_algebra(M0):
    y = M0[:5, 5].copy()
    eta5 = np.diag([-1., 1, 1, 1, 1])
    basis = []
    for A in range(5):
        for B in range(A+1, 5):
            L = np.zeros((5, 5)); L[A, B] = 1; L[B, A] = -1          # generator acting on vector index: (L y)^A = L^A_B y^B, L eta-skew requires L = Omega eta ; use Omega antisym then L = Omega @ eta5
            basis.append(L @ eta5)
    # keep combos with L y = 0
    Mtx = np.array([b @ y for b in basis]).T                            # (5, 10)
    u, sv, vh = np.linalg.svd(Mtx)
    null = vh[np.sum(sv > 1e-9):]
    gens = [sum(c_*b for c_, b in zip(v, basis)) for v in null]
    return gens, y

def fibre_point(M0, gens, rng):
    # random element of SO(4) (Haar on the compact group generated; the stabiliser of a timelike vector in R^{4,1} is compact SO(4))
    coef = rng.normal(size=len(gens))
    L5 = sum(c_*g for c_, g in zip(coef, gens))
    # make it a random group element: scale to large angle
    g5 = sl.expm(3.0*L5)
    g6 = np.eye(6); g6[:5, :5] = g5
    return g6 @ M0 @ g6.T

def point_y_spatial_zero(seed=0, n=1.0):
    """orbit point with y^i = M^{i5} = 0 (i=1..3) but y^4 != 0 (generic a): minimise sum_i (y^i)^2 from random starts; reject y^4 ~ 0."""
    from scipy.optimize import minimize
    rng = np.random.default_rng(seed)
    best = None
    for t in range(60):
        p0 = rng.normal(size=8)
        def obj(p):
            zz = p[:4] + 1j*p[4:]
            q_ = np.real(zz.conj() @ H @ zz)
            if q_ < 1e-3: return 1e6
            zz = zz*np.sqrt(n/q_)
            M = Mfun(zz)
            return sum(M[i, 5]**2 for i in range(1, 4)) + 1e-3*max(0, 0.3 - abs(M[4, 5]))**2
        r = minimize(obj, p0, method='Nelder-Mead', options={'xatol': 1e-12, 'fatol': 1e-20, 'maxiter': 20000})
        zz = r.x[:4] + 1j*r.x[4:]; zz = zz*np.sqrt(n/np.real(zz.conj() @ H @ zz))
        M = Mfun(zz)
        if r.fun < 1e-14 and abs(M[4, 5]) > 0.2:
            return zz
    raise RuntimeError("no point found")
