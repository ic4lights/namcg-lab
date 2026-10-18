"""034 engine (corrected): central Y with the P P insertion at the seam, with the full two-time Duhamel integral.
Correction relative to engine_c/engine_d: the seam P^2 sits between the last and the first propagator, so the two end propagators cannot be merged and the time-translation reduction
  int_0^1 du (1-u) <V(su) V(0)>  is NOT available.  The exact second-order term is
  T2/Theta = -i s <C> <P^2> - s^2 int_{0<u2<u1<1} du1 du2 <V(s u1) V(s u2) P^2>,
with P^2 at the far right, V(tau) = e^{i tau H0} V e^{-i tau H0}.  Exponential handling for general times (tau1 > tau2): E1 = e^{i sig phi(tau1)}, E2 = e^{-i sig phi(tau2)},
 [omega_a(t), phi(t')] = -i (M(t-t') kappa)_a,  E1 E2 = exp(i sig (phi(tau1)-phi(tau2))) exp([A,B]/2),  [phi(t1),phi(t2)] = i (a2-a1).kappa + i a1 F a2^T,  a_i = 2 kappa^T eta Phi(tau_i).
Items: V1 (time tau1): vec = 2 a_lo M(tau1), const = sig a.kappa - 2 sig a.M(tau1-tau2) kappa;  V2 (time tau2): vec = 2 a_lo M(tau2), const = -sig a.kappa;  P, P: vec = y, const = c0."""
import numpy as np, scipy.linalg as sl
GL = {}
def gl_nodes(n):
    if n not in GL:
        x, w = np.polynomial.legendre.leggauss(n); GL[n] = ((x + 1) / 2, w / 2)
    return GL[n]
def expm_pair(F, eta, t):
    d = F.shape[0]; K = 2 * F @ eta
    big = np.zeros((2 * d, 2 * d), complex); big[:d, :d] = K; big[:d, d:] = np.eye(d)
    E = sl.expm(t * big); return E[:d, :d], E[:d, d:]
def wick4(mu, P):
    m1, m2, m3, m4 = mu
    return (m1*m2*m3*m4 + P[(1,2)]*m3*m4 + P[(1,3)]*m2*m4 + P[(1,4)]*m2*m3 + P[(2,3)]*m1*m4 + P[(2,4)]*m1*m3 + P[(3,4)]*m1*m2
            + P[(1,2)]*P[(3,4)] + P[(1,3)]*P[(2,4)] + P[(1,4)]*P[(2,3)])
def second_order_e(F, eta, kappa, alpha_num, y, c0, s, nquad=16):
    F = np.array(F, float); eta = np.array(eta, float); kappa = np.array(kappa, float); alpha_num = np.array(alpha_num, float); y = np.array(y, float)
    d = F.shape[0]
    a_lo = eta @ alpha_num; kup = eta @ kappa
    K = 2 * F @ eta
    Ms = sl.expm(s * K)
    G = -1j * F @ Ms.T @ np.linalg.inv(np.eye(d) - Ms.T)
    PP = c0 ** 2 + y @ G @ y
    total = -1j * s * 0.5 * float(a_lo @ alpha_num) * PP
    us, ws = gl_nodes(nquad)
    acc = 0j
    cache = {}
    def MP(t):
        key = complex(t)
        if key not in cache: cache[key] = expm_pair(F, eta, t)
        return cache[key]
    for u1, w1 in zip(us, ws):
        for u2n, w2 in zip(us, ws):
            u2 = u1 * u2n; w = w1 * w2 * u1               # int_0^{u1} du2
            t1, t2 = s * u1, s * u2
            M1, Ph1 = MP(t1); M2, Ph2 = MP(t2); M12, _ = MP(t1 - t2)
            a1 = 2 * kup @ Ph1; a2 = 2 * kup @ Ph2      # a_i = 2 kappa^T eta Phi(tau_i)  (row vectors)
            comm = 1j * (a2 - a1) @ kappa + 1j * a1 @ F @ a2
            dPhi = Ph1 - Ph2
            for sig in (1, -1):
                l = 2j * sig * (dPhi.T @ kup)
                pref = np.exp(0.5 * sig ** 2 * comm) * np.exp(0.5 * l @ G @ l)
                v1 = 2 * a_lo @ M1; c1 = sig * (a_lo @ kappa) - 2 * sig * (a_lo @ M12 @ kappa)
                v2 = 2 * a_lo @ M2; c2 = -sig * (a_lo @ kappa)
                items = [(v1, c1), (v2, c2), (y, c0), (y, c0)]
                mu = [c + v @ G.T @ l for v, c in items]
                Pm = {(i + 1, j + 1): items[i][0] @ G @ items[j][0] for i in range(4) for j in range(i + 1, 4)}
                acc += w * pref * wick4(mu, Pm) * 0.25
    return total - s ** 2 * acc
