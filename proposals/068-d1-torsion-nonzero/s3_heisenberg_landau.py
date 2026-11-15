"""S3. Heisenberg background [E_3, E_1] = kappa E_2: sectors with central momentum p.
Run from this folder: python s3_heisenberg_landau.py > s3_heisenberg_landau_output.txt

Part A: the 40 fields (h, w) in the Schroedinger representation.  Columns are
restricted to oscillator levels <= L, rows are kept on all N levels, so no
truncation defect enters; a root is a value of q_0 at which the rank drops
below its generic value (gauge directions are in the kernel for every q_0).
Part B: the order-zero field A_a of the class, third bracket
D^a F_ab - T_ab^c F^a_c = 0 with T = -c, by direct matrices.
Part C: the same with the contraction delta."""
import numpy as np
import core
from core import *
from tools import char_roots, grouped


def part_A(p, kappa, N=14, L=5):
    c, w = heisenberg(kappa)
    cols = [i * N + n for i in range(40) for n in range(L + 1)]
    Mfun = lambda q0: M_op(c, w, heisenberg_modes(p, q0, N, kappa))[:, cols]
    r = rank(Mfun(0.37))
    roots = char_roots(Mfun, r)
    lev = (roots ** 2 * (1 if core.ETA[0, 0] < 0 else -1) - p * p) / (kappa * p)
    print('  p = %.2f kappa = %.2f: generic rank %d of %d; roots %d' % (p, kappa, r, len(cols), len(roots)))
    for (re, im), cnt in grouped(lev, 3):
        j = (re - 1) / 2
        note = '' if j <= L - 3 else '   (level reaches the column cut; count incomplete)'
        print('     (s q_0^2 - p^2)/(kappa p) = %7.3f %+.3fi   x %3d%s' % (re, im, cnt, note))


def part_B(p, kappa, N=14, L=5):
    """Unknowns A_b (4 components x levels <= L); equations b = 0..3 on all levels."""
    eta = core.ETA
    c = heisenberg(kappa)[0]

    def Mfun(q0):
        E = heisenberg_modes(p, q0, N, kappa)
        I = np.eye(N, dtype=complex)
        # F_ab = E_a A_b - E_b A_a - c_ab^d A_d ; eq_b = eta^{aa'} E_a' F_ab + c_ab^c eta^{aa'} F_a'c
        F = np.zeros((4, 4, N, 4, N), dtype=complex)       # F[a,b,:, comp, :]
        for a in range(4):
            for b in range(4):
                F[a, b, :, b, :] += E[a]
                F[a, b, :, a, :] -= E[b]
                for d in range(4):
                    F[a, b, :, d, :] -= c[a, b, d] * I
        eq = np.zeros((4, N, 4, N), dtype=complex)
        for b in range(4):
            for a in range(4):
                eq[b] += eta[a, a] * np.einsum('nm,mxk->nxk', E[a], F[a, b])
                for cc in range(4):
                    eq[b] += c[a, b, cc] * eta[a, a] * F[a, cc]
        M = eq.reshape(4 * N, 4 * N)
        cols = [i * N + n for i in range(4) for n in range(L + 1)]
        return M[:, cols]
    r = rank(Mfun(0.37))
    roots = char_roots(Mfun, r)
    lev = (roots ** 2 * (1 if eta[0, 0] < 0 else -1) - p * p) / (kappa * p)
    print('  p = %.2f kappa = %.2f: generic rank %d of %d (one gauge parameter per level)' % (p, kappa, r, 4 * (L + 1)))
    for (re, im), cnt in grouped(lev, 3):
        print('     (s q_0^2 - p^2)/(kappa p) = %7.3f %+.3fi   x %3d' % (re, im, cnt))


print('== A. fields (h, w), contraction eta; s = +1.  Prediction: levels 2j+1, j = -1, 0, 1, ...')
for p, kappa in [(0.3, 1.0), (2.0, 1.0), (0.3, 0.5)]:
    part_A(p, kappa)
print('== B. order-zero field A_a, contraction eta.  By hand: q_0^2 = p^2 + kappa p (2n+1 -+ 2)')
for p, kappa in [(0.3, 1.0), (2.0, 1.0)]:
    part_B(p, kappa)
print('== growth rate of the lowest level: q_0^2 = p (p - kappa) < 0 for 0 < p < kappa; minimum -kappa^2/4 at p = kappa/2')
core.set_eta([1, 1, 1, 1])
print('== C. contraction delta; s = -1: a real root q_0 is a zero of the Euclidean operator')
part_A(0.3, 1.0)
part_B(0.3, 1.0)
