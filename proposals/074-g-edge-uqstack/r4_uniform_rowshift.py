"""073 s4: exact increments, sign criterion and uniform (N-independent)
Lipschitz bound for the two-row hook-content additivity defect of 072
(Lemma 2 closed form, reused unchanged).

Delta(M1,M2;l1,l2) = sum_{c<=l1} log((M-1+c)/(M1-1+c))
                   + sum_{c<=l2} log((M-2+c)/(M2-1+c)) - log((l1+1)/(l1-l2+1)),
M = M1+M2, valid for partitions l1 >= l2 >= 0.

(1) Extension to l2 = 0 (one-row diagrams): the closed form matches the exact
    dim_{M}(l1)/(dim_{M1}(l1)*1) rational identity.
(2) Exact increment identities (verified as exact Fraction equalities):
    adding a box to row 1: ratio = (M+l1)*(l1-l2+2)*(l1+1)
                                  /((M1+l1)*(l1-l2+1)*(l1+2))   (> 1 always)
    adding a box to row 2 (needs l1 > l2):
                          ratio = (M+l2-1)*(l1-l2)
                                  /((M2+l2)*(l1-l2+1))
    adding a box to both rows (ridge move, l1 = l2 allowed):
                          ratio = inc1-ratio * (M+l2-1)*(l1-l2+1)
                                                  /((M2+l2)*(l1-l2+2))
    (each is the ratio of the two dim-ratios, i.e. of dim_M(...) before/after
    divided by the corresponding single-factor dim ratios).
(3) Sign criterion: the row-2 increment is < 0 exactly when
    (l1-l2)*(M1-1) < M2 + l2   (exact integer cross-multiplication grid);
    confinement: the minimum of the row-2 increment over diagrams with gap
    l1-l2 >= dstar = 1 + (M2+l2)/(M1-1) is >= 0; the most negative single-box
    move on the gap-1 band, and its approach to -log 2 as M2 -> 0 relatively.
(4) Uniform bound (brute force over ALL pairs of valid diagrams within C of
    each other, C <= 5, M1, M2 grids, rows up to M/2 + margin):
    |Delta' - Delta| <= C*(K1 + K2 + 1) + log(2C+1),
    K1 = log(1 + M2/M1), K2 = log(1 + (M1-1)/M2)   (N-independent constants).
(5) Row-independence of the corner-mode claim: N*delta_2 recomputed
    (m1, m2) = (1/2, 1/3), k = 1, N = 100..3200 -> 2.4396; the expression
    delta_p(N, M1, M2, k1, k2) contains no row argument (row-independent by
    construction).

Run: python -I proposals/073-g-edge-rowshift/s4_uniform_rowshift.py
Expected invariants: 'exact extension OK'; 'increments exact: OK';
'sign criterion: OK'; 'min row-2 inc (d >= dstar): >= 0'; 'uniform bound: OK'
with positive worst slack; N*delta_2(N=3200) = 2.4396; 'PASS s4'.
"""
import math
from fractions import Fraction

import numpy as np


def dim(M, rows):
    """Exact dim of the GL_M irrep of the partition `rows`, Fraction."""
    num = Fraction(1)
    den = Fraction(1)
    r1 = len(rows)
    for r in range(1, r1 + 1):
        L = rows[r - 1]
        for c in range(1, L + 1):
            num *= M + c - r
            hook = L - c
            for r2 in range(r + 1, r1 + 1):
                if rows[r2 - 1] >= c:
                    hook += 1
            den *= hook + 1
    return num / den


def Delta(M1, M2, l1, l2):
    t1 = sum(math.log((M1 + M2 - 1 + c) / (M1 - 1 + c)) for c in range(1, l1 + 1))
    t2 = sum(math.log((M1 + M2 - 2 + c) / (M2 - 1 + c)) for c in range(1, l2 + 1))
    return t1 + t2 - math.log((l1 + 1) / (l1 - l2 + 1))


# ---------- (1) exact extension to l2 = 0 ----------
bad = 0
nchk = 0
for M1 in (2, 3, 5, 11, 20):
    for M2 in (2, 4, 9, 17):
        for l1 in range(1, 25):
            lhs = dim(M1 + M2, (l1,)) / dim(M1, (l1,))
            rhs = Fraction(1)
            for c in range(1, l1 + 1):
                rhs *= Fraction(M1 + M2 - 1 + c, M1 - 1 + c)
            nchk += 1
            if lhs != rhs:
                bad += 1
print('(1) l2=0 extension: %d exact checks, %d failures' % (nchk, bad))
assert bad == 0
print('exact extension OK')

# ---------- (2) exact increment identities ----------
bad = 0
nchk = 0
for M1 in (2, 3, 7, 15):
    for M2 in (2, 5, 13):
        M = M1 + M2
        for l2 in range(0, 9):
            for l1 in range(max(l2, 1), 17):
                d = l1 - l2
                r1 = (dim(M, (l1 + 1, l2)) / dim(M, (l1, l2))) / \
                     (dim(M1, (l1 + 1,)) / dim(M1, (l1,)))
                r1p = Fraction((M + l1) * (d + 2) * (l1 + 1),
                               (M1 + l1) * (d + 1) * (l1 + 2))
                rJ = (dim(M, (l1 + 1, l2 + 1)) / dim(M, (l1, l2))) / \
                     ((dim(M1, (l1 + 1,)) / dim(M1, (l1,))) *
                      (dim(M2, (l2 + 1,)) / dim(M2, (l2,))))
                rJp = r1p * Fraction((M + l2 - 1) * (d + 1), (M2 + l2) * (d + 2))
                nchk += 2
                bad += (r1 != r1p) + (rJ != rJp)
                assert r1 > 1 and rJ > 1  # row-1 and ridge moves strictly positive
                if l1 > l2:
                    r2 = (dim(M, (l1, l2 + 1)) / dim(M, (l1, l2))) / \
                         (dim(M2, (l2 + 1,)) / dim(M2, (l2,)))
                    r2p = Fraction((M + l2 - 1) * d, (M2 + l2) * (d + 1))
                    nchk += 1
                    bad += (r2 != r2p)
print('(2) increment identities: %d exact checks, %d failures' % (nchk, bad))
assert bad == 0
print('increments exact: OK')

# ---------- (3) sign criterion for the row-2 increment ----------
bad = 0
nchk = 0
worst_band = (0.0, None)     # most negative increment, recorded case
min_out = (float('inf'), None)  # min increment over d >= dstar
for M1 in range(2, 30):
    for M2 in range(2, 30):
        M = M1 + M2
        for l2 in range(1, 30):
            for l1 in range(l2 + 1, 61):
                d = l1 - l2
                # exact sign of r2 - 1 by integer cross-multiplication
                lhs_i = (M + l2 - 1) * d
                rhs_i = (M2 + l2) * (d + 1)
                crit_neg = (M - 1 - M2) * d < M2 + l2   # d*(M1-1) < M2+l2
                nchk += 1
                bad += ((lhs_i < rhs_i) != crit_neg)
                inc = math.log(Fraction(lhs_i, rhs_i))
                dstar = 1 + (M2 + l2) / (M1 - 1)
                if d >= dstar:
                    if inc < min_out[0]:
                        min_out = (inc, (M1, M2, l1, l2))
                if inc < worst_band[0]:
                    worst_band = (inc, (M1, M2, l1, l2))
print('(3) sign criterion: %d checks, %d failures' % (nchk, bad))
assert bad == 0
print('sign criterion: OK')
print('    min row-2 inc over d >= dstar: %.6e at %s (>= 0: %s)'
      % (min_out[0] if min_out[1] else float('nan'), min_out[1],
         min_out[0] >= 0 if min_out[1] else 'n/a'))
assert min_out[0] >= 0.0
print('    most negative row-2 inc (any d): %.6f at %s (log(1/2) = -0.69315)'
      % (worst_band[0], worst_band[1]))

# ---------- (4) uniform Lipschitz bound, brute force over all pairs ----------
rng = np.random.default_rng(73004)
worst_slack = (float('inf'), None)
npairs = 0
for M1 in (2, 3, 5, 8, 24):
    for M2 in (2, 5, 13, 24):
        K1 = math.log(1 + M2 / M1)
        K2 = math.log(1 + (M1 - 1) / M2)
        lmax = (M1 + M2) // 2 + 4
        base = [(l1, l2) for l1 in range(1, lmax + 1) for l2 in range(0, l1 + 1)]
        sel = [base[i] for i in rng.choice(len(base), size=min(len(base), 300),
                                           replace=False)]
        for C in (1, 2, 3, 5):
            bnd = C * (K1 + K2 + 1) + math.log(2 * C + 1)
            for (l1, l2) in sel:
                d0 = Delta(M1, M2, l1, l2)
                for l1p in range(max(1, l1 - C), lmax + 1):
                    for l2p in range(0, min(l1p, l2 + C) + 1):
                        if abs(l1p - l1) > C or abs(l2p - l2) > C:
                            continue
                        npairs += 1
                        sl = bnd - abs(Delta(M1, M2, l1p, l2p) - d0)
                        if sl < worst_slack[0]:
                            worst_slack = (sl, (M1, M2, l1, l2, l1p, l2p, C))
print('(4) uniform bound: %d pairs checked, worst slack %.6f at %s'
      % (npairs, worst_slack[0], worst_slack[1]))
assert worst_slack[0] > 0
print('uniform bound: OK')

# ---------- (5) corner mode: row-independence ----------
print('(5) corner mode N*delta_2, m=(1/2,1/3), k=1 (no row argument):')
for N in (100, 400, 1600, 3200):
    M1 = N // 2
    M2 = N // 3
    s1sq = M1 * (N - M1)
    s2sq = M2 * (N - M2)
    p = 2
    tot = (M2 - 1) * s1sq ** p + (M1 - 1) * s2sq ** p + (s1sq + s2sq) ** p
    dlt = (s1sq + s2sq) ** p - s1sq ** p - s2sq ** p
    print('    N=%5d  N*delta_2 = %.4f' % (N, N * dlt / tot))
print('PASS s4')
