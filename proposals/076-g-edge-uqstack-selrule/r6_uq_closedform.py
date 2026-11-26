"""074 s1: exact rational verification of the U(q)-stack repeated-row additivity defect.

Class: diagrams lambda = (l1 repeated q1 times, l2 repeated q2 times) of U(M), M = M1+M2,
with l1 >= l2 >= 0, compared against the per-factor stacked rows (l1^q1) of U(M1) and
(l2^q2) of U(M2). The defect is Delta = log dim_U(M)(lambda) - log dim_U(M1)(l1^q1)
- log dim_U(M2)(l2^q2).

Verified closed form (as the multiplicative defect D = exp(Delta)):
  D = prod_{r=1}^{q1} prod_{c=1}^{l1} (M+c-r)/(M1+c-r)
    * prod_{r=1}^{q2} prod_{c=1}^{l2} (M-q1+c-r)/(M2+c-r)
    * prod_{r=1}^{q1} prod_{c=1}^{l2} (l1-c+q1-r+1)/(l1-c+q1+q2-r+1)

Reference dims are computed independently from the hook-content product
dim_{U(M)}(rows) = prod_{(r,c)} (M+c-r)/hook(r,c),  hook(r,c) = rows[r]-c + #{rows >= c} - r + 1.
Cross-checked on the q1=q2=1 subgrid against the integrated 072 two-row closed form
  D_072 = prod_{c=1}^{l1} (M-1+c)/(M1-1+c) * prod_{c=1}^{l2} (M-2+c)/(M2-1+c) * (l1-l2+1)/(l1+1).

Deterministic; exact Fractions. Prints a PASS line per section.
"""
import math
from fractions import Fraction


def dim_exact(M, rows):
    """Hook-content dimension, exact Fraction. rows: nonincreasing tuple of >=0 ints.

    Zero-length rows are inert (they shift no row index and raise no column height),
    so the stacked tuples may carry them freely."""
    num = 1
    den = 1
    for r, L in enumerate(rows, start=1):
        for c in range(1, L + 1):
            colh = sum(1 for L2 in rows if L2 >= c)
            hook = (L - c) + (colh - r) + 1
            num *= (M + c - r)
            den *= hook
    return Fraction(num, den)


def closedform_D(M, M1, M2, l1, l2, q1, q2):
    D = Fraction(1)
    for r in range(1, q1 + 1):
        for c in range(1, l1 + 1):
            D *= Fraction(M + c - r, M1 + c - r)
    for r in range(1, q2 + 1):
        for c in range(1, l2 + 1):
            D *= Fraction(M - q1 + c - r, M2 + c - r)
    # hook correction: row block 1, columns c <= l2, where the column height of the
    # union diagram exceeds that of the separate diagram (l1^q1) by q2
    for r in range(1, q1 + 1):
        for c in range(1, l2 + 1):
            D *= Fraction(l1 - c + q1 - r + 1, l1 - c + q1 + q2 - r + 1)
    return D


def closedform_D_072(M, M1, M2, l1, l2):
    D = Fraction(1)
    for c in range(1, l1 + 1):
        D *= Fraction(M - 1 + c, M1 - 1 + c)
    for c in range(1, l2 + 1):
        D *= Fraction(M - 2 + c, M2 - 1 + c)
    D *= Fraction(l1 - l2 + 1, l1 + 1)
    return D


def main():
    fails = 0
    cases = 0
    cross_fails = 0
    cross_cases = 0
    min_delta = float('inf')
    min_arg = None
    min_delta_gen = float('inf')
    min_delta_gen_arg = None
    neg_count = 0
    for M1 in range(1, 10):
        for M2 in range(1, 10):
            M = M1 + M2
            for q1 in range(0, 4):
                if q1 > M1:
                    continue
                for q2 in range(0, 4):
                    if q2 > M2 or q1 + q2 == 0:
                        continue
                    for l1 in range(0, 7):
                        for l2 in range(0, l1 + 1):
                            if q1 == 0 and (l1 > 0 or l2 > 0):
                                continue
                            if q2 == 0 and l2 > 0:
                                continue
                            if l1 == 0 and l2 > 0:
                                continue
                            comb = tuple([l1] * q1 + [l2] * q2)
                            ref1 = tuple([l1] * q1)
                            ref2 = tuple([l2] * q2)
                            lhs = dim_exact(M, comb)
                            rhs = dim_exact(M1, ref1) * dim_exact(M2, ref2) * \
                                closedform_D(M, M1, M2, l1, l2, q1, q2)
                            cases += 1
                            if lhs != rhs:
                                fails += 1
                            if q1 == 1 and q2 == 1:
                                cross_cases += 1
                                if closedform_D(M, M1, M2, l1, l2, 1, 1) != \
                                        closedform_D_072(M, M1, M2, l1, l2):
                                    cross_fails += 1
                            if l1 >= 1 and q1 >= 1:
                                d = math.log(float(
                                    lhs / (dim_exact(M1, ref1) * dim_exact(M2, ref2))))
                                if d < min_delta:
                                    min_delta = d
                                    min_arg = (M1, M2, l1, l2, q1, q2)
                                if M1 >= 2 and M2 >= 2 and q1 + q2 < M:
                                    if d < min_delta_gen:
                                        min_delta_gen = d
                                        min_delta_gen_arg = (M1, M2, l1, l2, q1, q2)
                                if d < -1e-12:
                                    neg_count += 1
    print('cases %d  exact-identity failures %d' % (cases, fails))
    assert fails == 0, 'closed form failed'
    print('cross-check vs integrated 072 two-row closed form: cases %d  failures %d'
          % (cross_cases, cross_fails))
    assert cross_fails == 0, 'q1=q2=1 reduction differs from 072 closed form'
    print('nontrivial cases: min Delta = %.9f at (M1,M2,l1,l2,q1,q2)=%s; negative-count %d'
          % (min_delta, min_arg, neg_count))
    print('strict-positivity subset (M1,M2 >= 2, q1+q2 < M1+M2): min Delta = %.9f at %s'
          % (min_delta_gen, min_delta_gen_arg))
    assert min_delta >= 0.0, 'positivity grid failed (all)'
    assert min_delta_gen > 0.0, 'positivity grid failed (generic ranks)'
    assert neg_count == 0
    print('PASS s1')


if __name__ == '__main__':
    main()
