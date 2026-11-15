"""S2. Characteristic roots and partial multiplicities in the character sectors.
Run from this folder: python s2_spectrum.py > s2_spectrum_output.txt"""
import numpy as np, sympy as sp
from core import *
from tools import char_roots, grouped, partial_mult

rng = np.random.default_rng(5)
KLOW = np.array([1.0, 0.0, 0.0, 1.0])            # k_a ; k^a = (-1,0,0,1), null


def line(c, w, q0, n):
    return lambda t: M_of_q(c, w, q0 + t * n)


def null_point(shift, plane=None):
    v = rng.normal(size=3)
    if plane is not None:
        v = v * np.array(plane)
    n = np.array([np.linalg.norm(v), *v])
    return n - shift * KLOW


print('== characteristic roots along a line q0 + t n (numerical; roots common to two random compressions)')
q0 = np.array([0.31, 0.42, -0.45, -0.72]); n = np.array([2.5, -0.57, -0.22, -0.23])
for name, (c, w), mask in [('flat', flat(), [1, 1, 1, 1]),
                           ('null rotation, constant-connection gauge', null_rotation_g2(), [1, 1, 1, 1]),
                           ('Heisenberg, q_2 = 0', heisenberg(), [1, 1, 0, 1]),
                           ('second algebra, q_2 = q_3 = 0', second_algebra(), [1, 1, 0, 0])]:
    m = np.array(mask, dtype=float)
    a, b = q0 * m, n * m
    roots = char_roots(line(c, w, a, b), 30)
    print('--', name, ': number of roots', len(roots))
    for (re, im), cnt in grouped(roots):
        q = a + (re + 1j * im) * b
        qq = -q[0] ** 2 + q[1] ** 2 + q[2] ** 2 + q[3] ** 2
        kq = -q[0] + q[3]                         # k^a q_a
        extra = ''
        if name.startswith('null'):
            extra = '  j with (q + j k)^2 = 0: %s' % (np.round((-qq / (2 * kq)).real, 2))
        if name.startswith('second'):
            qs = q - np.array([2j, 0, 0, 0])
            extra = '  (q - i tau)^2 with tau_a = (2,0,0,0): %s' % np.round(-qs[0] ** 2 + qs[1] ** 2, 4)
        print('   t = %8.4f %+8.4fi  x %2d   q^2 = %s%s' % (re, im, cnt, np.round(qq, 4), extra))

print('== partial multiplicities at a root: cumulative sum_i min(m_i, L), L = 1..4, gauge chains removed')
nn = np.array([1.0, 0.3, -0.2, 0.5])
print('flat, q^2 = 0                        ', partial_mult(line(*flat(), null_point(0), nn), 10))
for j in (-2, -1, 0, 1, 2):
    print('null rotation (flat frame), (q%+dk)^2 = 0 ' % j, partial_mult(line(*null_rotation_g2(), null_point(j), nn), 10))
print('Heisenberg, q_2 = 0, q^2 = 0         ', partial_mult(line(*heisenberg(), null_point(0, [1, 0, 1]), nn * np.array([1, 1, 0, 1])), 10))
print('null rotation, left-invariant gauge, q_0 = q_3  ', partial_mult(line(*null_rotation_g1(), np.array([1.3, 0, 0, 1.3]), np.array([1.0, 0, 0, 0.4])), 10))
print('null rotation, left-invariant gauge, q_0 = -q_3 ', partial_mult(line(*null_rotation_g1(), np.array([1.3, 0, 0, -1.3]), np.array([1.0, 0, 0, 0.4])), 10))

print('== exact ranks (rational arithmetic) on the null-rotation background, flat frame')
from fractions import Fraction
c, w = null_rotation_g2()
M0, M1, M2 = M_coeffs(c, w)


def frac(X):
    out = [[Fraction(float(x)).limit_denominator(64) for x in row] for row in X]
    assert max(abs(float(out[i][j]) - X[i, j]) for i in range(X.shape[0]) for j in range(X.shape[1])) < 1e-12
    return out


M0f, M1f, M2f = frac(M0), {k: frac(v) for k, v in M1.items()}, {k: frac(v) for k, v in M2.items()}


def exact_rank(q):
    """rank over C of M(q) = X + iY, computed as half the rank over Q of [[X,-Y],[Y,X]]."""
    n = NF
    X = [[M0f[i][j] - sum(q[m] * q[n2] * v[i][j] for (m, n2), v in M2f.items()) for j in range(n)] for i in range(n)]
    Y = [[sum(q[m] * M1f[m][i][j] for m in range(4)) for j in range(n)] for i in range(n)]
    A = [X[i] + [-y for y in Y[i]] for i in range(n)] + [Y[i] + X[i] for i in range(n)]
    r = 0
    rows = len(A)
    for col in range(2 * n):
        piv = next((i for i in range(r, rows) if A[i][col] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pr = A[r]
        for i in range(r + 1, rows):
            if A[i][col] != 0:
                f = A[i][col] / pr[col]
                A[i] = [a - f * b for a, b in zip(A[i], pr)]
        r += 1
    assert r % 2 == 0
    return r // 2


qg = [Fraction(3, 7), Fraction(-2, 5), Fraction(1, 3), Fraction(5, 11)]
print('generic rational q: rank', exact_rank(qg), '(floating rank', rank(M_of_q(c, w, np.array([float(x) for x in qg]))), ')')
for j in (-2, -1, 0, 1, 2):
    nvec = [Fraction(13), Fraction(3), Fraction(4), Fraction(12)]                   # 13^2 = 3^2 + 4^2 + 12^2
    q = [nvec[0] - j, nvec[1], nvec[2], nvec[3] - j]                                # q + j k = nvec
    print('q = %s on (q%+dk)^2 = 0: rank %d' % ([int(x) for x in q], j, exact_rank(q)))
print('flat, q = (13,3,4,12):', end=' ')
c, w = flat(); M0, M1, M2 = M_coeffs(c, w)
M0f, M1f, M2f = frac(M0), {k: frac(v) for k, v in M1.items()}, {k: frac(v) for k, v in M2.items()}
print('rank', exact_rank([Fraction(13), Fraction(3), Fraction(4), Fraction(12)]))
