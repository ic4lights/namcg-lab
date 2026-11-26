"""V4 (round 2). Null-rotation background in the gauge with constant frame and
omega_a^{12} = vartheta k_a, k_a = (1,0,0,1) (k null for eta = diag(-1,1,1,1)).
Characteristic roots of the forty equations along the line q(t) = q0 + t n of s2, for
vartheta = -1/2 (the value with the torsion of the left-invariant gauge), 1/2, 1, 2.

Since k is null, (q + j vartheta k)^2 = q^2 + 2 j vartheta (k.q), so a root lies on the cone of
weight j iff x := -q^2 / (2 vartheta k.q) equals j.  For every root cluster the script prints
x itself (complex, unrounded), its distance to the nearest integer, and the direct residual
|(q + j vartheta k)^2| / |q|^2.  No rounding is used to decide membership: a root is accepted
on cone j only if |x - j| < 1e-8.  Second, independent check: exact rational ranks of M(q) at
rational points q = nvec - j vartheta k ON each cone (nvec = (13,3,4,12), nvec^2 = 0) and at a
generic rational point, for vartheta = -1/2.
Run: python -I v4_null_rotation_vartheta_r2.py
"""
import os
import sys
from fractions import Fraction
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import M_of_q, M_coeffs, null_rotation_g2, rank, NF   # noqa: E402
from tools import char_roots, grouped                            # noqa: E402

ETA = np.diag([-1.0, 1.0, 1.0, 1.0])
k = np.array([1.0, 0.0, 0.0, 1.0])
q0 = np.array([0.31, 0.42, -0.45, -0.72])
n = np.array([2.5, -0.57, -0.22, -0.23])


def sq(q):
    return q @ ETA @ q


TOL = 1e-8
allok = True
for th in (-0.5, 0.5, 1.0, 2.0):
    c, w = null_rotation_g2(th)
    roots = char_roots(lambda t: M_of_q(c, w, q0 + t * n), 30)
    mult = {}
    worst_x = worst_cone = worst_im = 0.0
    for (re, im), cnt in grouped(roots):
        q = q0 + (re + 1j * im) * n
        x = -sq(q) / (2 * th * (k @ ETA @ q))
        j = int(np.floor(x.real + 0.5))
        dx = abs(x - j)
        cone = abs(sq(q + j * th * k)) / float(np.vdot(q, q).real)
        ok = dx < TOL
        allok &= ok
        worst_x = max(worst_x, dx); worst_cone = max(worst_cone, cone); worst_im = max(worst_im, abs(im))
        mult.setdefault(j if ok else ('OFF', round(x.real, 6)), []).append(cnt)
        print('  vartheta=%+.1f root t=%+.12f%+.1ei  x=%+.12f%+.1ei  |x-j|=%.1e  |(q+j vartheta k)^2|/|q|^2=%.1e  j=%d  mult %d'
              % (th, re, im, x.real, x.imag, dx, cone, j, cnt))
    print('vartheta = %+.1f: total roots %d; max |Im t| %.1e; max |x - j| %.1e; max cone residual %.1e; '
          'all on cones: %s; j -> multiplicities per crossing %s'
          % (th, len(roots), worst_im, worst_x, worst_cone, all(isinstance(j, int) for j in mult),
             dict(sorted((kk, v) for kk, v in mult.items() if isinstance(kk, int)))))

print('== exact rational ranks at vartheta = -1/2 (generic rank 30 = 40 - 10 gauge)')
c, w = null_rotation_g2(-0.5)
M0, M1, M2 = M_coeffs(c, w)


def frac(X):
    out = [[Fraction(float(x)).limit_denominator(64) for x in row] for row in X]
    assert max(abs(float(out[i][jj]) - X[i, jj]) for i in range(X.shape[0]) for jj in range(X.shape[1])) < 1e-12
    return out


M0f, M1f, M2f = frac(M0), {kk: frac(v) for kk, v in M1.items()}, {kk: frac(v) for kk, v in M2.items()}


def exact_rank(q):
    X = [[M0f[i][jj] - sum(q[m] * q[n2] * v[i][jj] for (m, n2), v in M2f.items()) for jj in range(NF)] for i in range(NF)]
    Y = [[sum(q[m] * M1f[m][i][jj] for m in range(4)) for jj in range(NF)] for i in range(NF)]
    A = [X[i] + [-y for y in Y[i]] for i in range(NF)] + [Y[i] + X[i] for i in range(NF)]
    r = 0
    for col in range(2 * NF):
        piv = next((i for i in range(r, len(A)) if A[i][col] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        for i in range(r + 1, len(A)):
            if A[i][col] != 0:
                f = A[i][col] / A[r][col]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        r += 1
    assert r % 2 == 0
    return r // 2


th = Fraction(-1, 2)
qg = [Fraction(3, 7), Fraction(-2, 5), Fraction(1, 3), Fraction(5, 11)]
print('generic rational q: exact rank', exact_rank(qg), '(floating rank',
      rank(M_of_q(c, w, np.array([float(x) for x in qg]))), ')')
nvec = [Fraction(13), Fraction(3), Fraction(4), Fraction(12)]
for j in (-2, -1, 0, 1, 2):
    q = [nvec[0] - j * th, nvec[1], nvec[2], nvec[3] - j * th]     # q + j vartheta k = nvec, null
    qq = -q[0] ** 2 + q[1] ** 2 + q[2] ** 2 + q[3] ** 2
    kq = -q[0] + q[3]
    print('q = %s: (q + j vartheta k)^2 = 0 exactly for j = %+d (x = %s); exact rank %d'
          % ([str(x) for x in q], j, -qq / (2 * th * kq), exact_rank(q)))
print('ALL ROOTS ON CONES WITHOUT ROUNDING:', allok)
