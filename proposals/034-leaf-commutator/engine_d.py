"""034: dimension-general version of engine_c (any metric eta) with selectable placement of the two Y factors, for the 2D toy check.
placement: 'seam' -> <V1(su) V1(0) P P> (P P at the far right);  'left' -> <P P V1(su) V1(0)> with P at time 0 (not cyclically equivalent);  'inter' -> not available here."""
import numpy as np, scipy.linalg as sl
GL = {}
def gl_nodes(n):
    if n not in GL:
        x, w = np.polynomial.legendre.leggauss(n); GL[n] = ((x + 1) / 2, w / 2)
    return GL[n]
def G_and_M(F, eta, s, taus):
    d = F.shape[0]
    K = 2 * F @ eta
    M = sl.expm(s * K)
    G = -1j * F @ M.T @ np.linalg.inv(np.eye(d) - M.T)
    Ms, Ph = [], []
    big = np.zeros((2 * d, 2 * d), complex); big[:d, :d] = K; big[:d, d:] = np.eye(d)
    for t in taus:
        E = sl.expm(t * big); Ms.append(E[:d, :d]); Ph.append(E[:d, d:])
    return G, Ms, Ph
def wick4(mu, P):
    m1, m2, m3, m4 = mu
    return (m1*m2*m3*m4 + P[(1,2)]*m3*m4 + P[(1,3)]*m2*m4 + P[(1,4)]*m2*m3 + P[(2,3)]*m1*m4 + P[(2,4)]*m1*m3 + P[(3,4)]*m1*m2
            + P[(1,2)]*P[(3,4)] + P[(1,3)]*P[(2,4)] + P[(1,4)]*P[(2,3)])
def second_order_gen(F, eta, kappa, alpha_num, y, c0, s, nquad=24, placement='seam'):
    F = np.array(F, float); eta = np.array(eta, float)
    a_lo = eta @ alpha_num; kup = eta @ kappa
    us, ws = gl_nodes(nquad); taus = [s * u for u in us]
    G, Ms, Ph = G_and_M(F, eta, s, taus)
    PP = c0 ** 2 + y @ G @ y
    total = -1j * s * 0.5 * float(a_lo @ alpha_num) * PP
    acc = 0j
    for u, wu, tau, M, Phi in zip(us, ws, taus, Ms, Ph):
        for sig in (1, -1):
            l = 2j * sig * (Phi.T @ kup)
            pref = np.exp(-1j * kup @ Phi @ kappa) * np.exp(0.5 * l @ G @ l)
            v1 = 2 * a_lo; c1 = sig * (a_lo @ kappa); v1t = v1 @ M; c1t = c1 - sig * (v1t @ kappa)
            v2 = 2 * a_lo; c2 = -sig * (a_lo @ kappa)
            if placement == 'seam':
                items = [(v1t, c1t), (v2, c2), (y, c0), (y, c0)]
            else:
                items = [(y, c0), (y, c0), (v1t, c1t), (v2, c2)]
            mu = [c + v @ G.T @ l for v, c in items]
            P = {(i + 1, j + 1): items[i][0] @ G @ items[j][0] for i in range(4) for j in range(i + 1, 4)}
            acc += wu * (1 - u) * pref * wick4(mu, P) * 0.25
    return total - s ** 2 * acc
