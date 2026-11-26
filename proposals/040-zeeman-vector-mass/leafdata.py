"""034 library: leaf-consistent data of the nilpotent (Landau) model on CP^{1,2}, built from the actual vector fields.

Frame at an orbit point: W_a = Ham(T^a), T^a = M^{a4};  Z_k (k=1,2) a basis of the vertical space V' = common kernel of dy^mu, y^mu = M^{mu5}.
Operators: omega_a = -i W_a,  zeta_k = -i Z_k  (Hermitian), so that
   [omega_a, omega_b] = -[W_a,W_b] = -S_ab^k Z_k + (horizontal, dropped) = i F_ab,   F_ab = -S_ab^k zeta_k      ([W_a,W_b] = S_ab^k Z_k + h^c_ab W_c),
   [omega_a, phi]     = -i W_a(phi) = -i kappa_a,
   zeta_Y := -i Y = y^c omega_c + y^k zeta_k      (Y = Ham(phi) = q_mu {y^mu, .} = y^c W_c + y^k Z_k),
   D^X_a = W_a - eps alpha_a sin(phi) Y  ->  H = eta^{ab} Omega_a Omega_b,  Omega_a = omega_a - eps alpha_a sin(phi) zeta_Y = omega_a + eps sin(phi)(m_a^c omega_c + n_a),
   m_a^c = -alpha_a y^c,  n_a = -alpha_a y^k zeta_k.
Index placement as in 030/032: W_a, kappa_a, alpha_a, F_ab, q_mu lower; y^c, t^mu upper; eta = diag(-1,1,1,1).
"""
import sys, numpy as np
sys.dont_write_bytecode = True
from scipy.linalg import null_space
from geom28 import *

eta_a = np.array([-1., 1, 1, 1])
etan = np.diag(eta_a)

def to_tangent(E, v15):
    return E @ v15

def leaf_frame(M0):
    """returns dict with tangent-space frame data at the orbit point M0."""
    Pi, c, E = poisson_bivector(M0)
    W = np.array([c[pidx[(a, 4)]] for a in range(4)])                      # (4,6)
    b = np.array([E[:, pidx[(m, 5)]] for m in range(4)])                    # (4,6) covectors dy^mu
    Zs = null_space(b).T                                                    # (2,6) vertical vectors
    assert Zs.shape[0] == 2
    Lam = np.vstack([W, Zs])                                                # rows = frame vectors
    LamT_inv = np.linalg.inv(Lam.T)
    def comps(t6):
        x = LamT_inv @ t6
        return x[:4], x[4:]                                                 # horizontal coefficients t^c, vertical t^k
    return dict(Pi=Pi, c=c, E=E, W=W, b=b, Z=Zs, Lam=Lam, comps=comps)

def bracket_field(M0, E, f1, f2):
    """Lie bracket [Ham f1, Ham f2] = Ham({f1,f2}) for f = M^{CD}; returns tangent 6-vector."""
    L = lin_coeffs(*f1, *f2)
    return E @ ham_of_lin(M0, L)

def leaf_data(M0, q):
    """q: lower-index covector q_mu of the plane wave phi = q_mu y^mu.  Returns frame, F tensor S (S[a,b,k]), Y comps, V comps, kappa."""
    fr = leaf_frame(M0)
    E, c, W, comps = fr['E'], fr['c'], fr['W'], fr['comps']
    # structure constants of the horizontal frame
    S = np.zeros((4, 4, 2)); Hh = np.zeros((4, 4, 4))
    for a in range(4):
        for bb in range(4):
            if a == bb: continue
            t6 = bracket_field(M0, E, (a, 4), (bb, 4))
            hc, vc = comps(t6)
            S[a, bb] = vc; Hh[a, bb] = hc
    Yv = sum(q[m] * c[pidx[(m, 5)]] for m in range(4))                     # Y = q_mu Ham(y^mu)
    ycomp, ykomp = comps(Yv)                                               # y^c, y^k
    Vv = c[pidx[(4, 5)]]                                                   # V = Ham(M^{45})
    vc, vk = comps(Vv)
    dphi = sum(q[m] * fr['b'][m] for m in range(4))
    kappa = np.array([dphi @ W[a] for a in range(4)])                      # kappa_a = W_a(phi)
    # [W_a, Y] directly (tangent coordinates)
    WY = np.array([sum(q[m] * bracket_field(M0, E, (a, 4), (m, 5)) for m in range(4)) for a in range(4)])
    WYc = [comps(WY[a]) for a in range(4)]
    return dict(fr=fr, S=S, Hh=Hh, y=ycomp, yk=ykomp, v=vc, vk=vk, kappa=kappa, WY=WYc, Yv=Yv, Vv=Vv, dphi=dphi, W=W, E=E, c=c, b=fr['b'])

def rand_point(rng, lo=0.6, hi=3.0):
    z = rand_z_pos(rng, rng.uniform(lo, hi)); return Mfun(z)
