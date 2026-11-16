"""073 s2 (copy of 072 s2_hook_content.py, review-r1 findings 2
fixed: section (5) label direction; logic and prints unchanged): hook-content additivity defect of two-row U(M1+M2) diagrams.

(1) EXACT rational verification of the closed form
      dim_{M1+M2}(l1,l2) / (dim_{M1}(l1) dim_{M2}(l2))
    = Pi_{c=1}^{l1} (M1+M2-1+c)/(M1-1+c)
      * Pi_{c=1}^{l2} (M1+M2-2+c)/(M2-1+c) * (l1-l2+1)/(l1+1)
    (hook-content formula; the hook products of (l1,l2) vs (l1) and (l2)
    telescope to (l1+1)/(l1-l2+1)). Verified as an exact Fraction identity on a
    grid. dim_M(rows) = prod_{(r,c)} (M+c-r)/hook(r,c).
(2) Symbolic: the telescoping hook ratio
    Product((l1-c+2)/(l1-c+1), (c,1,l2)) = (l1+1)/(l1-l2+1), and
    d log dim / d log M = sum_{(r,c)} M/(M+c-r)  (mismatch 2), sympy.
(3) Sign survey of the defect
      Delta = sum_c1 log((M1+M2-1+c)/(M1-1+c)) + sum_c2 log((M1+M2-2+c)/(M2-1+c))
              - log((l1+1)/(l1-l2+1))
    on grids of bounded row-length ratio, reporting the minimum.
(4) Monotonicity survey: sign of Delta(l1,l2+1)-Delta(l1,l2) on the grids.
(5) Exact rational direction count for T1 vs T2 (the product ratio
      T1/T2 decreases with the base rank: T1 < T2 in all checked cases),
      where
      T1 = sum_c1 log((M1+M2-1+c)/(M1-1+c)),
      T2 = sum_c1 log((M1+M2-2+c)/(M1-2+c)).

Run: python -I proposals/073-g-edge-rowshift/s2_hook_content.py
Expected invariants: 'exact identity: OK'; 'hook-ratio symbolic: OK';
'derivative symbolic: OK'; grid minimum of Delta > 0; 'PASS s2'.
"""
import math
from fractions import Fraction

import sympy as sp


def dim(M, rows):
    """Exact dim of the GL_M irrep of the diagram `rows` (partition), Fraction."""
    num = Fraction(1)
    den = Fraction(1)
    r1 = len(rows)
    for r in range(1, r1 + 1):
        L = rows[r - 1]
        for c in range(1, L + 1):
            num *= M + c - r
            hook = L - c  # boxes to the right
            for r2 in range(r + 1, r1 + 1):
                if rows[r2 - 1] >= c:
                    hook += 1
            den *= hook + 1
    return num / den


# ---------- (1) exact rational identity ----------
bad = 0
nchk = 0
for M1 in (2, 3, 5, 7, 11, 20, 41):
    for M2 in (2, 3, 5, 9, 17):
        for l2 in range(1, 12):
            for l1 in range(l2, l2 + 8, 3):
                lhs = dim(M1 + M2, (l1, l2)) / (dim(M1, (l1,)) * dim(M2, (l2,)))
                rhs = Fraction(1)
                for c in range(1, l1 + 1):
                    rhs *= Fraction(M1 + M2 - 1 + c, M1 - 1 + c)
                for c in range(1, l2 + 1):
                    rhs *= Fraction(M1 + M2 - 2 + c, M2 - 1 + c)
                rhs *= Fraction(l1 - l2 + 1, l1 + 1)
                nchk += 1
                if lhs != rhs:
                    bad += 1
print('exact rational identity: %d checks, %d failures' % (nchk, bad))
assert bad == 0
print('exact identity: OK')

# ---------- (2) symbolic checks ----------
l1, l2, c, M = sp.symbols('l1 l2 c M', positive=True, integer=True)
hookratio = sp.product((l1 - c + 2) / (l1 - c + 1), (c, 1, l2)).doit()
sr = sp.simplify(hookratio - (l1 + 1) / (l1 - l2 + 1))
print('hook-ratio symbolic: OK' if sr == 0 else 'hook-ratio symbolic: FAIL %s' % sr)
assert sr == 0
# derivative check on a fixed two-row diagram by explicit sums
l1v, l2v = 5, 3
expr = sum(sp.log(M + cc - r) for r, L in ((1, l1v), (2, l2v)) for cc in range(1, L + 1))
lhs = sp.simplify(sp.diff(expr, M) * M)
rhs = sum(M / (M + cc - r) for r, L in ((1, l1v), (2, l2v)) for cc in range(1, L + 1))
dv = sp.simplify(lhs - rhs)
print('derivative symbolic: OK' if dv == 0 else 'derivative symbolic: FAIL %s' % dv)
assert dv == 0


def Delta(M1, M2, l1v, l2v):
    t1 = sum(math.log((M1 + M2 - 1 + c) / (M1 - 1 + c)) for c in range(1, l1v + 1))
    t2 = sum(math.log((M1 + M2 - 2 + c) / (M2 - 1 + c)) for c in range(1, l2v + 1))
    return t1 + t2 - math.log((l1v + 1) / (l1v - l2v + 1))


# ---------- (3) sign survey, bounded ratios ----------
best = (float('inf'), None)
for M1 in range(2, 41):
    for M2 in range(2, 41):
        cap = (M1 + M2) // 2  # class bound: row length <= half the block rank
        step = 1 if cap < 30 else 3
        for l2 in range(1, cap + 1):
            for l1 in range(l2, cap + 1, step):
                d = Delta(M1, M2, l1, l2)
                if d < best[0]:
                    best = (d, (M1, M2, l1, l2))
print('grid min Delta (M<=40, l <= (M1+M2)/2): %.6e at %s' % best)
assert best[0] > 0

# ---------- (4) monotonicity in l2 ----------
worst_inc = (float('inf'), None)
for M1 in range(2, 25):
    for M2 in range(2, 25):
        cap = (M1 + M2) // 2
        step = 1 if cap < 30 else 3
        for l2 in range(1, cap):
            for l1 in range(l2 + 1, cap + 1, step):
                inc = Delta(M1, M2, l1, l2 + 1) - Delta(M1, M2, l1, l2)
                if inc < worst_inc[0]:
                    worst_inc = (inc, (M1, M2, l1, l2))
print('grid min Delta(l1,l2+1)-Delta(l1,l2): %.6e at %s' % worst_inc)

# ---------- (5) exact rational T1 vs T2 direction count ----------
bad5 = 0
n5 = 0
for M1 in range(2, 25, 3):
    for M2 in (2, 5, 13):
        for l1 in range(1, 25):
            t1 = Fraction(1)
            t2 = Fraction(1)
            for c in range(1, l1 + 1):
                t1 *= Fraction(M1 + M2 - 1 + c, M1 - 1 + c)
                t2 *= Fraction(M1 + M2 - 2 + c, M1 - 2 + c)
            n5 += 1
            if t1 < t2:
                bad5 += 1
print("T1 vs T2 (ratio decreasing in base rank): %d of %d with T1<T2 (informational)" % (bad5, n5))
print('PASS s2')
