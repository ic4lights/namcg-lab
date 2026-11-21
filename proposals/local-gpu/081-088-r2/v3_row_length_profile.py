"""081-088 r2, v3: the slot law of the Gaussian state of the Row length paragraph itself.

Basis |k), k=0..N-1, eigenvalue (N-1)/2-k of J^3 (cap axis n = e_3); block = k<M, edge vectors
u=|M-1), v=|M). Momenta Pi = sum_{l<=lc,m} pi_lm T_lm, T_lm the trace-normalised irreducible tensor
operators, E|pi_lm|^2 = f(l), pi_{l,-m} fixed by hermiticity, pi_lm (m>0) circular.
Checks:
 A  T_lm has entries only on the diagonal k' - k = m (offset), Sum_m T_lm T_lm^+ = (2l+1)/N (exact
    to roundoff): full row sums of <|Pi_ij|^2> are N^-1 sum (2l+1) f(l);
 B  covariance of the boundary row w_j = Pi_{vj}, j<M: E w_j w_k^* = delta_jk g_j and E w_j w_k = 0
    (distinct offsets, same sign), so u = |M-1) is a slot basis vector: Gamma = 0, a independent of r,
    and r = sum_{j<M-1} |w_j|^2 is the exponential slot sum with weights g_j, j != M-1 (structural; the
    covariance matrix is built explicitly from the T_lm and its off-diagonal part is checked to vanish);
 C  g_j = 0 for M-1-j >= lc, so D <= lc - 1 slots carry r and D_eff <= D <= lc - 1 (Cauchy-Schwarz);
    numbers at N=400, M=200, lc=20, 40 for f = l/2 and f = l(l+1)/4;
 D  comparison with the 081 mode-count proxy (g = f(l) with multiplicity 2l+1): D_eff 1488 at lc=40.
Run: python -I proposals/local-gpu/081-088-r2/v3_row_length_profile.py   Last line: PASS v3
"""
from fractions import Fraction

import numpy as np

ok = True


def spin_ops(N):
    j = (N - 1)/2
    mk = j - np.arange(N)
    cp = np.sqrt(j*(j + 1) - mk[1:]*(mk[1:] + 1))   # (J+)_{k-1,k}
    Jp = np.diag(cp, 1)
    return Jp, Jp.T.copy()


def tensors(N, lc):
    Jp, Jm = spin_ops(N)
    out = {}
    P = np.eye(N)
    for l in range(1, lc + 1):
        P = Jp @ P
        P /= np.linalg.norm(P)
        T = P.copy()
        out[(l, l)] = T
        for m in range(l, -l, -1):
            T = Jm @ T - T @ Jm
            T /= np.linalg.norm(T)
            out[(l, m - 1)] = T
    return out


def offsets_ok(T, m):
    # T_lm raises J^3 by m: entries at (k-m, k), i.e. column minus row = m
    idx = np.argwhere(np.abs(T) > 1e-13)
    return np.all(idx[:, 1] - idx[:, 0] == m)


# A on a small case
N0, lc0 = 12, 5
T0 = tensors(N0, lc0)
offA = all(offsets_ok(T0[(l, m)], m) for l in range(1, lc0 + 1) for m in range(-l, l + 1))
casA = max(np.max(np.abs(sum(T0[(l, m)] @ T0[(l, m)].conj().T for m in range(-l, l + 1)) - (2*l + 1)/N0*np.eye(N0)))
           for l in range(1, lc0 + 1))
print('A offsets:', offA, '| Casimir-type sum dev %.1e' % casA); ok &= offA and casA < 1e-10


def row_cov(N, M, lc, f):
    T = tensors(N, lc)
    v = M
    C = np.zeros((M, M), complex)   # E w_j w_k^*
    Pc = np.zeros((M, M), complex)  # E w_j w_k
    for l in range(1, lc + 1):
        for m in range(1, l + 1):
            # independent circular pi_lm (m>0); pi_{l,-m} = (-1)^m conj(pi_lm); Pi = sum_m>0 (pi T_lm + conj(pi)(-1)^m T_l,-m) + pi_l0 T_l0
            A = T[(l, m)][v, :M]; B = ((-1)**m)*T[(l, -m)][v, :M]
            C += f(l)*(np.outer(A, A.conj()) + np.outer(B, B.conj()))
            Pc += f(l)*(np.outer(A, B) + np.outer(B, A))
        A0 = T[(l, 0)][v, :M]
        C += f(l)*np.outer(A0, A0.conj()); Pc += f(l)*np.outer(A0, A0)
    return C, Pc


for N, M, lc, name, f in [(60, 30, 8, 'l/2', lambda l: l/2), (400, 200, 20, 'l/2', lambda l: l/2),
                          (400, 200, 40, 'l/2', lambda l: l/2), (400, 200, 40, 'l(l+1)/4', lambda l: l*(l + 1)/4)]:
    C, Pc = row_cov(N, M, lc, f)
    gdiag = np.real(np.diag(C))
    offd = np.max(np.abs(C - np.diag(np.diag(C))))/np.max(gdiag)
    pse = np.max(np.abs(Pc))/np.max(gdiag)
    gr = gdiag[:M - 1]                     # slots of r: j != M-1
    nz = int(np.sum(gr > 1e-12*gr.max()))
    far = np.max(gdiag[:M - lc]) if M - lc > 0 else 0.0
    Deff = gr.sum()**2/np.sum(gr**2)
    Wblock = gdiag.sum()
    print('B/C N=%d M=%d lc=%d f=%s: offdiag %.1e pseudo %.1e | slots of r with g>0: %d (<= lc-1=%d) | '
          'max g at distance >= lc: %.1e | D_eff(r) = %.2f | W_block = %.4f' % (N, M, lc, name, offd, pse, nz, lc - 1, far, Deff, Wblock))
    ok &= offd < 1e-10 and pse < 1e-10 and nz <= lc - 1 and far < 1e-12*gdiag.max() and Deff <= lc - 1


def deff_proxy(L):
    W = sum(Fraction(2*l + 1)*Fraction(l, 2) for l in range(1, L + 1))
    S2 = sum(Fraction(2*l + 1)*Fraction(l, 2)**2 for l in range(1, L + 1))
    return W*W/S2


d40, d160 = deff_proxy(40), deff_proxy(160)
print('D proxy D_eff (081 mode-count convention): lc=40 %.3f, lc=160 %.3f' % (float(d40), float(d160)))
ok &= round(float(d40)) == 1488 and round(float(d160)) == 23017
print('PASS v3' if ok else 'FAIL v3')
