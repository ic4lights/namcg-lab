"""040: spin-block decomposition of the Zeeman-dressed vector response (kappa^2 coefficient) in the canonical frame.
Eigenbasis of K_F = 2 F eta:  E+ : (1,+1,0,0), mu=+2a ;  E- : (1,-1,0,0), mu=-2a ;  B+ : (0,0,1,+i), mu=+2ib ;  B- : (0,0,1,-i), mu=-2ib.
M(t) = sum_k e^{t mu_k} R_k L_k.  e^{-i s Z0} = M(s): the factor e^{+2 s a} (E+) is the unbounded branch on the real s axis, e^{+-2 i b s} the magnetic Zeeman phases.
Blocks of the order-eps^2 response (T2/Theta units):
   diagonal 'D_k' : e^{s mu_k} [ T_C + (-s^2) sum_nodes w nVV ]  +  e^{s mu_k} N_kk (-s^2) sum_nodes w (nVd+ndV)
   pair 'P_kl'    : (-s^2) sum_nodes w ndd  e^{(s-tau) mu_k + tau mu_l} N_kl N_lk
sum over (k) and (k,l) equals T2_total for the vector species."""
import mpmath as mp, numpy as np
from engine_z import *

NAMES = ['E+', 'E-', 'B+', 'B-']
def eig_data(a, b):
    a = mp.mpf(a); b = mp.mpf(b)
    R = np.array([[1, 1, 0, 0], [1, -1, 0, 0], [0, 0, 1, 1], [0, 0, 1j, -1j]], dtype=object).T  # columns = eigenvectors? build explicitly
    cols = [[1, 1, 0, 0], [1, -1, 0, 0], [0, 0, 1, 1j], [0, 0, 1, -1j]]
    R = np.array([[mp.mpc(cols[k][i]) for k in range(4)] for i in range(4)], dtype=object)
    mat = mp.matrix(4, 4)
    for i in range(4):
        for j in range(4):
            mat[i, j] = R[i, j]
    inv = mat ** -1
    L = np.array([[inv[i, j] for j in range(4)] for i in range(4)], dtype=object)
    mus = [2 * a, -2 * a, 2j * b, -2j * b]
    return R, L, mus

def block_terms(a, b, kappa_s, alpha, y, c0, s, nquad=8):
    """dict name -> block value for a given (scaled) kappa."""
    TC, nodes = orbital_nodes(a, b, kappa_s, alpha, y, c0, s, nquad)
    R, L, mus = eig_data(a, b)
    sp = vector_species(a, b, kappa_s, alpha)
    N = sp.N
    Nk = L.dot(N).dot(R)
    sVV = sum(w * nVV for (w, tau, nVV, nVd, ndV, ndd) in nodes)
    sVd = sum(w * (nVd + ndV) for (w, tau, nVV, nVd, ndV, ndd) in nodes)
    out = {}
    for k in range(4):
        e = mp.exp(s * mus[k])
        out['D' + NAMES[k]] = e * (TC - s ** 2 * sVV) + e * Nk[k, k] * (-s ** 2) * sVd
    for k in range(4):
        for l in range(4):
            coef = Nk[k, l] * Nk[l, k]
            acc = mp.mpc(0)
            for (w, tau, nVV, nVd, ndV, ndd) in nodes:
                acc += w * ndd * mp.exp((s - tau) * mus[k] + tau * mus[l])
            out['P' + NAMES[k] + NAMES[l]] = coef * (-s ** 2) * acc
    return out

def k2_blocks(a, b, kappa, alpha, y, c0, s, nquad=8, lam=mp.mpf('1e-8')):
    ka = np.array([mp.mpf(x) for x in kappa], dtype=object)
    al = np.array([mp.mpf(x) for x in alpha], dtype=object)
    yy = np.array([mp.mpf(x) for x in y], dtype=object)
    c0 = mp.mpf(c0)
    res = []
    for f in (lam, -lam, 0):
        res.append(block_terms(a, b, scale_kappa(ka, f), al, yy, c0, s, nquad))
    return {k: (res[0][k] + res[1][k] - 2 * res[2][k]) / (2 * lam ** 2) for k in res[0]}
