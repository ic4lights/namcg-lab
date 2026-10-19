"""034 engine: second-order response of the nilpotent (Landau) problem when the plane-wave coupling is the CENTRAL operator Y (Y commutes with omega_a and phi).

Model (leaf, nilpotent order):  H = eta^{ab} Omega_a Omega_b,   Omega_a = omega_a - eps alpha_a sin(phi) Y,    [omega_a,omega_b] = i F_ab,  [omega_a, phi] = -i kappa_a,
  Y = right-invariant generator:  [Y, omega_a] = 0 = [Y, phi]  (Jacobi: [W_a, Y] = -q_a V, V horizontal, dropped at the nilpotent order),
  its diagonal value at the base point is the polynomial P = y^c omega_c + c0 sitting at the SEAM of the trace:  Tr[ chain * P^2 ]  (chain = ordered product of the left-invariant factors).
Second order in eps (phase averaged):
  T2/Theta = -i s <V2 P^2> - s^2 int_0^1 du (1-u) <V1(su) V1(0) P^2>,   V1 = -(a.omega S + S a.omega),  a_a = eta_aa alpha^a,   V2 = (1/2) (a.alpha) ,
all expectation values in the quasi-free state e^{-isH0}/Theta (Wick, KMS), P^2 = P P at the far right.
This is engine.py with the interleaved factor (u_b+n_b) replaced by the central scalar Y whose two insertions are placed at the seam.  For F = 0 it equals engine.second_order with m_a^c = -alpha_a y^c, n_a = -alpha_a c0.
Conventions: omega_a = xi(D^a) numerically, eta = diag(-1,1,1,1) contracts the field index; alpha_num[a] = coefficient of D^a in the perturbation; y[c] = coefficient of D^c in Y; kappa[a] = D^a(phi)."""
import numpy as np, scipy.linalg as sl
from engine import G_and_M, gl_nodes, eta

def wick4(mu, P):
    m1, m2, m3, m4 = mu
    return (m1 * m2 * m3 * m4
            + P[(1, 2)] * m3 * m4 + P[(1, 3)] * m2 * m4 + P[(1, 4)] * m2 * m3
            + P[(2, 3)] * m1 * m4 + P[(2, 4)] * m1 * m3 + P[(3, 4)] * m1 * m2
            + P[(1, 2)] * P[(3, 4)] + P[(1, 3)] * P[(2, 4)] + P[(1, 4)] * P[(2, 3)])

def second_order_central(F, kappa, alpha_num, y, c0, s, nquad=24, seam=True):
    """returns T2(s)/Theta(s).  F: 4x4 antisymmetric ([omega_a,omega_b]=iF_ab); kappa (4); alpha_num (4); y (4); c0 scalar (charge at the base point).
    seam=False: place the two Y factors inside each V1 (as the interleaved engine does when m != 0) -- not used for the leaf, kept for tests."""
    F = np.array(F, float); kappa = np.array(kappa, float); alpha_num = np.array(alpha_num, float); y = np.array(y, float)
    a_lo = eta @ alpha_num                      # eta_aa alpha^a
    kup = eta @ kappa
    us, ws = gl_nodes(nquad)
    taus = [s * u for u in us]
    G, Ms, Ph = G_and_M(F, s, taus)
    aa = float(a_lo @ alpha_num)                # eta_aa alpha^a alpha^a
    PP = c0 ** 2 + y @ G @ y                    # <P P> in the state (items P1, P2 contracted)
    V2 = 0.5 * aa * PP
    total = -1j * s * V2
    acc = 0j
    for u, wu, tau, M, Phi in zip(us, ws, taus, Ms, Ph):
        for sig in (+1, -1):
            l = 2j * sig * (Phi.T @ kup)
            ph = np.exp(-1j * kup @ Phi @ kappa)
            pref = ph * np.exp(0.5 * l @ G @ l)
            # V1 e^{i sig phi}: coefficient vector a_lo (kinds 1+2): linear form a.(2 omega + sig kappa) -> vec = 2 a_lo, const = sig a_lo.kappa
            v1 = 2 * a_lo; c1 = sig * (a_lo @ kappa)
            v1t = v1 @ M
            c1t = c1 - sig * (v1t @ kappa)          # engine rule: const' = const - sig * vec'.kappa, vec' = M^T vec
            v2 = 2 * a_lo; c2 = -sig * (a_lo @ kappa)
            items = [(v1t, c1t), (v2, c2), (y, c0), (y, c0)]
            mu = [c + v @ G.T @ l for v, c in items]
            P = {}
            for i in range(4):
                for j in range(i + 1, 4):
                    P[(i + 1, j + 1)] = items[i][0] @ G @ items[j][0]
            acc += wu * (1 - u) * pref * wick4(mu, P) * 0.25
    return total - s ** 2 * acc
