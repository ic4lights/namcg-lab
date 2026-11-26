"""079 s1 (repaired, r1): exact (integer/rational arithmetic) verification of the
lemmas behind the frame-uniform residual bound, plus the full chain inequality on
exhaustive small grids. Deterministic, no random numbers.

REPAIR LINEAGE: the dead-predecessor draft of this file had a disclosed WIP zone
(a degenerate symmetric-grid prefix sum, a placeholder guard, Iint defined inside
the loop). This file is a clean pre-.out rewrite executed BEFORE any .out existed:
the dead lines were removed, Iint was hoisted to module level, and the draft's
asymmetric tiny-grid choice (row-1 block rank M1 = M-3) was ADOPTED; the check was
strengthened to the exact stacked (depth-q) defect functional and the clean
theorem-level frame-free bound.

Lemma R (Riemann bracketing, general A,B >= 1). For integers A,B >= 1, ell >= 1,
  S(A,B,ell) = sum_{c=1}^{ell} log((A+c)/(B+c)),
  I(A,B,ell) = (A+ell)log(A+ell) - A log A - (B+ell)log(B+ell) + B log B
               ( = int_0^ell log((A+y)/(B+y)) dy ),
one has |I - S| <= |log(A/B)|.
Proof: f(y)=log((A+y)/(B+y)) is monotone (decreasing iff A>B), so for A>B
int_1^{ell+1} f <= sum <= int_0^{ell} f gives 0 <= f(ell)-... , explicitly
I-S <= f(0)-f(ell) <= log(A/B) and I-S >= -f(0)+f(ell) >= -log(A/B);
the case A<B follows by swapping (I and S are antisymmetric in A,B).
Checked here EXACTLY by integer exponentiation of exp(I-S) (check_expR).

Lemma H (hook telescoping). For integers q >= 1, 1 <= r <= q, ell >= 1,
  prod_{x=0}^{ell-1} (x+2q-r+1)/(x+q-r+1) = prod_{i=0}^{q-1} (ell+q-r+1+i)/(q-r+1+i)
as exact Fractions, and more generally, for a >= 1, q2 >= 1,
  prod_{x=0}^{ell-1} (x+a)/(x+a+q2) = prod_{i=0}^{q2-1} (a+i)/(ell+a+i),
so |sum_x log((x+a)/(x+a+q2))| <= q2*log(ell+a+q2-1) (each factor <= 1,
each numerator <= ell+a+q2-1, each denominator >= 1 after clearing).

Multiplicative defect identity. For the stacked two-diagram class (rows
(l1^q1,l2^q2) of U(M), M=M1+M2, vs (l1^q1) of U(M1) and (l2^q2) of U(M2)),
with the guard M1-q1 >= 1, M2-q2 >= 1, M-q1-q2+1 >= 1, l1 >= l2 >= 0,
l1 <= min(M1,M)-q1-q2, the hook-content (Weyl) dimension ratio equals EXACTLY the
product of content factors and hook ratios displayed in the integrated Problem G
stacked-row paragraph (checked as exact Fraction identities, with hook lengths
h(r,c)=(l_r-c)+(l'_c-r)+1).

Chain inequality. For every valid small tuple, with the exact stacked defect
Delta_q (float logs of the exact product functional), the continuum target
T_q = sum_f q_f * I(M,M_f,l_f) and the frame-free bound
  B_q = sum_f sum_r |log((M-a_f-r+1)/(M_f-r+1))|                    (Lemma R)
      + l1 sum_r [(r-1)/(M-r+1) + (r-1)/(M1-r+1)]                   (shift, stack 1)
      + l2 sum_r [(q1+r-1)/(M-q1-r+1) + (r-1)/(M2-r+1)]             (shift, stack 2)
      + q1*q2*log(l1+q1+q2)                                         (hooks),
(mean-value bound on I: |dI/dA| <= ell/A, |dI/dB| <= ell/B, sup on the shifted
interval; guards M1-q1>=1, M2-q2>=1, M-q1-q2+1>=1 keep denominators >= 1,)
one has |Delta_q - T_q| <= B_q.

Run:  python -I proposals/079-g-frameavg-residual/s1_exact_lemma.py
Expected final line: PASS s1
"""
import math
from fractions import Fraction

def Iint(A, B, ell):
    """int_0^ell log((A+y)/(B+y)) dy for A,B >= 1, ell >= 0."""
    if ell == 0:
        return 0.0
    return ((A + ell) * math.log(A + ell) - A * math.log(A)
            - (B + ell) * math.log(B + ell) + B * math.log(B))

def check_expR(A, B, ell):
    """Exact integer check of |I-S| <= |log(A/B)| via exp of both sides."""
    num = pow(A + ell, A + ell) * pow(B, B) * math.factorial(A) * math.factorial(B + ell)
    den = pow(A, A) * pow(B + ell, B + ell) * math.factorial(A + ell) * math.factorial(B)
    # exp(I-S) = num/den; require min(A/B,B/A) <= num/den <= max(A/B,B/A)
    if A >= B:
        return (A * num >= B * den) and (B * num <= A * den)
    return (B * num >= A * den) and (A * num <= B * den)

bad = 0
tests = 0
for Bv in (1, 2, 3, 7, 40):
    for d in (0, 1, 5, 97):          # A = B + d
        Av = Bv + d
        for ell in (1, 2, 3, 7, 41, 133):
            tests += 1
            if not check_expR(Av, Bv, ell):
                bad += 1; print('FAIL R', Av, Bv, ell)
            if d != 0:               # swapped case A < B
                tests += 1
                if not check_expR(Bv, Av, ell):
                    bad += 1; print('FAIL R swapped', Bv, Av, ell)
print('Lemma R: %d exact integer checks, %d failures' % (tests, bad))
assert bad == 0

bad = 0
tests = 0
for q in (1, 2, 3, 4):
    for r in range(1, q + 1):
        for ell in (1, 2, 5, 60, 201):
            lhs = Fraction(1)
            for x in range(ell):
                lhs *= Fraction(x + 2 * q - r + 1, x + q - r + 1)
            rhs = Fraction(1)
            for i in range(q):
                rhs *= Fraction(ell + q - r + 1 + i, q - r + 1 + i)
            tests += 1
            if lhs != rhs:
                bad += 1; print('FAIL H', q, r, ell)
            if lhs > Fraction((ell + 2 * q) ** q, 1):
                bad += 1; print('FAIL Hbound', q, r, ell)
for a in (1, 2, 5):
    for q2 in (1, 2, 3):
        for ell in (1, 3, 44):
            lhs = Fraction(1)
            for x in range(ell):
                lhs *= Fraction(x + a, x + a + q2)
            rhs = Fraction(1)
            for i in range(q2):
                rhs *= Fraction(a + i, ell + a + i)
            tests += 1
            if lhs != rhs:
                bad += 1; print('FAIL H2', a, q2, ell)
            hookb = -math.log(float(lhs))
            if hookb > q2 * math.log(ell + a + q2 - 1) + 1e-12:
                bad += 1; print('FAIL H2bound', a, q2, ell)
print('Lemma H: %d exact Fraction checks, %d failures' % (tests, bad))
assert bad == 0

def wdim_exact(M, rows):
    """Exact hook-content dimension ratio (up to overall scale) of U(M), rows a
    nonincreasing list of nonnegative ints; dim = prod_boxes (M+c-r)/h(r,c),
    h(r,c) = (l_r-c)+(l'_c-r)+1. Only ratios of such are used (scale cancels)."""
    num = 1
    den = 1
    q = len(rows)
    for r in range(1, q + 1):
        lr = rows[r - 1]
        for c in range(1, lr + 1):
            num *= M + c - r
            lc = sum(1 for x in rows if x >= c)
            den *= (lr - c) + (lc - r) + 1
    return Fraction(num, den)

def product_formula_exact(M, M1, M2, q1, q2, l1, l2):
    """Exact multiplicative defect of the integrated stacked-row identity:
    content factors on both stacks times the first-stack hook ratios."""
    f = Fraction(1)
    for r in range(1, q1 + 1):
        for c in range(1, l1 + 1):
            f *= Fraction(M + c - r, M1 + c - r)
    for r in range(1, q2 + 1):
        for c in range(1, l2 + 1):
            f *= Fraction(M - q1 + c - r, M2 + c - r)
    for r in range(1, q1 + 1):
        for c in range(1, l2 + 1):
            f *= Fraction(l1 - c + q1 - r + 1, l1 - c + q1 + q2 - r + 1)
    return f

def product_formula_log(M, M1, M2, q1, q2, l1, l2):
    """Float log of the same exact functional (chain input)."""
    s = 0.0
    for r in range(1, q1 + 1):
        for c in range(1, l1 + 1):
            s += math.log(M + c - r) - math.log(M1 + c - r)
    for r in range(1, q2 + 1):
        for c in range(1, l2 + 1):
            s += math.log(M - q1 + c - r) - math.log(M2 + c - r)
    for r in range(1, q1 + 1):
        for c in range(1, l2 + 1):
            s += math.log(l1 - c + q1 - r + 1) - math.log(l1 - c + q1 + q2 - r + 1)
    return s

bad = 0
tests = 0
for M1 in (2, 3, 5):
    for M2 in (2, 3, 5):
        M = M1 + M2
        for q1 in (1, 2, 3):
            for q2 in (1, 2, 3):
                if not (M1 - q1 >= 1 and M2 - q2 >= 1 and M - q1 - q2 + 1 >= 1):
                    continue
                for l1 in range(1, M1 - q1 - q2 + 1):
                    for l2 in range(0, l1 + 1):
                        rows = [l1] * q1 + ([l2] * q2 if l2 >= 1 else [])
                        lhs = (wdim_exact(M, rows)
                               / (wdim_exact(M1, [l1] * q1)
                                  * wdim_exact(M2, [l2] * q2 if l2 >= 1 else [])))
                        rhs = product_formula_exact(M, M1, M2, q1, q2, l1, l2)
                        tests += 1
                        if lhs != rhs:
                            bad += 1
                            print('FAIL prodID', M1, M2, q1, q2, l1, l2)
print('multiplicative defect identity: %d exact Fraction checks, %d failures' % (tests, bad))
assert bad == 0

def chain_bound(M1, M2, q1, q2, l1, l2):
    """Frame-free bound B_q of the proposal (Lemma R + shift + hooks)."""
    M = M1 + M2
    b = 0.0
    for r in range(1, q1 + 1):
        b += abs(math.log((M - r + 1) / (M1 - r + 1)))
        b += l1 * ((r - 1) / (M - r + 1) + (r - 1) / (M1 - r + 1))
    for r in range(1, q2 + 1):
        b += abs(math.log((M - q1 - r + 1) / (M2 - r + 1)))
        b += l2 * ((q1 + r - 1) / (M - q1 - r + 1) + (r - 1) / (M2 - r + 1))
    b += q1 * q2 * math.log(l1 + q1 + q2)
    return b

def chain_case(M1, M2, q1, q2, l1, l2):
    M = M1 + M2
    delta = product_formula_log(M, M1, M2, q1, q2, l1, l2)
    T = q1 * Iint(M, M1, l1) + q2 * Iint(M, M2, l2)
    return delta, T, chain_bound(M1, M2, q1, q2, l1, l2)

bad = 0
tests = 0
worst = 0.0
for N in (24, 50, 101):
    M = N // 2
    M1 = M - 3                      # draft's asymmetric tiny-grid choice (adopted)
    M2 = N - M1
    if M1 < 4:
        continue
    for l1 in range(1, min(M1, M) // 2 + 1):
        for l2 in range(0, l1 + 1):
            for (q1, q2) in ((1, 1), (2, 1), (1, 2), (2, 2)):
                if q1 > M1 - 1 or q2 > M2 - 1:
                    continue
                if l1 > min(M1, M) - q1 - q2:
                    continue
                dlt, T, Bnd = chain_case(M1, M2, q1, q2, l1, l2)
                tests += 1
                r = abs(dlt - T) / Bnd
                worst = max(worst, r)
                if abs(dlt - T) > Bnd + 1e-12:
                    bad += 1
                    print('FAIL chain', N, M1, q1, q2, l1, l2, abs(dlt - T), Bnd)
print('chain cross-check: %d cases, %d failures, worst |residual|/bound = %.4f'
      % (tests, bad, worst))
assert bad == 0

# two-row closed form consistency with the integrated selection-independence
# paragraph: Delta(l1,l2) at q=(1,1) equals the displayed closed form
bad = 0
for M1 in (5, 9):
    M2 = M1 + 4
    M = M1 + M2
    for l1 in range(1, 7):
        for l2 in range(0, l1 + 1):
            cf = (sum(math.log((M - 1 + c) / (M1 - 1 + c)) for c in range(1, l1 + 1))
                  + sum(math.log((M - 2 + c) / (M2 - 1 + c)) for c in range(1, l2 + 1))
                  - (math.log(l1 + 1) - math.log(l1 - l2 + 1)))
            dlt, T, Bnd = chain_case(M1, M2, 1, 1, l1, l2)
            if abs(dlt - cf) > 1e-9:
                bad += 1; print('FAIL tworow', M1, M2, l1, l2, dlt, cf)
print('two-row closed-form match: %d failures' % bad)
assert bad == 0

print('PASS s1')
