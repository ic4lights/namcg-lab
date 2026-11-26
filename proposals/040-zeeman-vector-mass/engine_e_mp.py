"""034: multiprecision version of engine_e for F in canonical Lorentz-frame form (F_01 = a electric, F_23 = b magnetic), eta = diag(-1,1,1,1).
Same formulas as engine_e.second_order_e (see its docstring).  k2coef_e returns the kappa^2 coefficient (T2(lam kappa) - T2(0))/lam^2 at fixed alpha, y, c0 (y.kappa = 0 is preserved)."""
import mpmath as mp, numpy as np
from engine_mp import blocks, Gmat, ETAM, ETA, zeros, eye4, gl, to_mp_vec, to_mp_mat
mp.mp.dps = 40
def wick4(mu, P):
    m1, m2, m3, m4 = mu
    return (m1*m2*m3*m4 + P[(1,2)]*m3*m4 + P[(1,3)]*m2*m4 + P[(1,4)]*m2*m3 + P[(2,3)]*m1*m4 + P[(2,4)]*m1*m3 + P[(3,4)]*m1*m2
            + P[(1,2)]*P[(3,4)] + P[(1,3)]*P[(2,4)] + P[(1,4)]*P[(2,3)])
def vdot(a, b):
    return sum(a[i] * b[i] for i in range(4))
def vmat(v, M):      # row vector @ matrix
    return np.array([sum(v[i] * M[i, j] for i in range(4)) for j in range(4)], dtype=object)
def matv(M, v):
    return np.array([sum(M[i, j] * v[j] for j in range(4)) for i in range(4)], dtype=object)
def second_order_e_mp(a, b, kappa, alpha, y, c0, s, nquad=10):
    """a,b mpf; kappa, alpha, y : object arrays of mpf (alpha = numeric coefficients; eta applied inside); returns T2/Theta (mpc)."""
    a = mp.mpf(a); b = mp.mpf(b)
    eta = [mp.mpf(e) for e in ETA]
    a_lo = np.array([eta[i] * alpha[i] for i in range(4)], dtype=object)
    kup = np.array([eta[i] * kappa[i] for i in range(4)], dtype=object)
    aa = vdot(a_lo, alpha)
    G = Gmat(a, b, s)
    GT = G.T
    Fm = zeros(4); Fm[0, 1] = a; Fm[1, 0] = -a; Fm[2, 3] = b; Fm[3, 2] = -b
    yG = vmat(y, G); PP = c0 ** 2 + vdot(yG, y)
    total = -1j * s * aa * PP / 2
    us, ws = gl(nquad)
    acc = mp.mpc(0)
    for u1, w1 in zip(us, ws):
        for un, w2 in zip(us, ws):
            u2 = u1 * un; w = w1 * w2 * u1
            t1, t2 = s * u1, s * u2
            M1, Ph1 = blocks(a, b, t1); M2, Ph2 = blocks(a, b, t2); M12, _ = blocks(a, b, t1 - t2)
            a1 = 2 * vmat(kup, Ph1); a2 = 2 * vmat(kup, Ph2)
            comm = 1j * (vdot(a2 - a1, kappa)) + 1j * vdot(vmat(a1, Fm), a2)
            dPhi = Ph1 - Ph2
            l0 = 2j * matv(dPhi.T, kup)
            for sig in (1, -1):
                l = sig * l0
                pref = mp.exp(comm / 2) * mp.exp(vdot(vmat(l, G), l) / 2)
                v1 = 2 * vmat(a_lo, M1); c1 = sig * vdot(a_lo, kappa) - 2 * sig * vdot(vmat(a_lo, M12), kappa)
                v2 = 2 * vmat(a_lo, M2); c2 = -sig * vdot(a_lo, kappa)
                items = [(v1, c1), (v2, c2), (y, c0), (y, c0)]
                mu = [c + vdot(vmat(v, GT), l) for v, c in items]
                Pm = {}
                for i in range(4):
                    for j in range(i + 1, 4):
                        Pm[(i + 1, j + 1)] = vdot(vmat(items[i][0], G), items[j][0])
                acc += w * pref * wick4(mu, Pm) / 4
    return total - s ** 2 * acc
def k2coef_e(a, b, kappa, alpha, y, c0, s, nquad=10, lam=mp.mpf('1e-12')):
    ka = np.array([mp.mpf(x) for x in kappa], dtype=object)
    al = np.array([mp.mpf(x) for x in alpha], dtype=object)
    yy = np.array([mp.mpf(x) for x in y], dtype=object)
    c0 = mp.mpf(c0)
    t1 = second_order_e_mp(a, b, lam * ka, al, yy, c0, s, nquad)
    t0 = second_order_e_mp(a, b, 0 * ka, al, yy, c0, s, nquad)
    return (t1 - t0) / lam ** 2
