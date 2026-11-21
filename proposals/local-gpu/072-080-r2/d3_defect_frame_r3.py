"""072-080 r3, d3 (r2 checks (a)-(f) unchanged, plus (g)): independent checks of the defect numbers and of the frame average.

 (a) two-row closed form against a from-scratch hook-content dimension (Fractions),
     all M1, M2 in 2..7, l1 >= l2, l1 <= 8;
 (b) exact increment Delta(l1,l2+1) - Delta(l1,l2) = log(37/72) at (2,24,13,12);
 (c) symmetric saddle M1 = M2 = N/2, l = N/2: Delta/N at N = 3200 and the
     continuum value 2[G(1,1/2) - G(1/2,1/2)] = log(27/16);
     rank ratio sum M/(M+c-r)/|mu| at block rank M = N and its limit 2 log(3/2);
 (d) stacked residual Delta_{q,q} - N q Lambda at N = 400..3200, q = 1,2,3:
     increments per doubling of N against q^2 log 2 (residual ~ q1 q2 log N);
 (e) frame average for B = diag((3-g)/2, (3-g)/2, g): averaged continuum limit and
     frame minimum at g = 1.4, 2, 2.6 (m_f = 1/2, round rows N/2, q = 1),
     by Gauss-Legendre quadrature in cos(theta);
 (f) concavity of the per-summand profile in rho (sympy) and Jensen at tr B = 3;
 (g) equal against unequal row fractions (review r2, M1):
     (g1) exact telescoping of the hook ratios (Fractions):
          prod_{c=1}^{l2} (a-c)/(a+q2-c) = prod_{j=0}^{q2-1} (a-l2+j)/(a+j),
          a = l1+q1-r+1, so the hook part is
          Hk = sum_{r=1}^{q1} sum_{j=0}^{q2-1} log((l1-l2+q1-r+1+j)/(l1+q1-r+1+j));
     (g2) residual N Lambda - Delta_{q,q} at equal fractions (u1 = u2 = 1/2, m = 1/2)
          and at unequal fractions (m,u) = (1/2,1/2; 1/2,3/10), (1/2,1/3; 2/5,1/4),
          (1/2,1/2; 9/20,3/10), q = 1,2,3, N = 480..3840 (Lambda at the exact
          integer fractions): unequal residuals bounded, increments -> 0;
     (g3) the content (row-sum) part of the residual, N Lambda - (Delta - Hk), is
          bounded in N at equal fractions as well: the q1 q2 log N growth is
          entirely the hook part, -Hk = q1 q2 log N + O(1) at u1 = u2, while at
          u1 > u2, -Hk -> q1 q2 log(u1/(u1-u2)).

Run: python -I proposals/local-gpu/072-080-r2/d3_defect_frame_r3.py
Expected: (a) 0 failures; (b) exact; (c) 0.520906, log(27/16) = 0.523248144,
0.8111, 0.810930; (d) increments increase towards q^2 log 2 from below, within 0.08; (e) averaged
0.522655 0.519217 0.511350, minimum 0.479485 0.396700 0.268892 (6 decimals);
(g1) 0 failures; (g2) unequal: |increment| < 0.1 at the last doubling, residuals < 12;
equal: increments within 0.08 of q^2 log 2; (g3) content-part increments < 0.05 in
all cases; unequal -Hk within 0.05 of q1 q2 log(u1/(u1-u2)) at N = 3840, approaching it in N;
last line 'PASS d3'.
"""
import math
from fractions import Fraction
import numpy as np
import sympy as sp

ok = True


def dim_u(M, rows):
    rows = [r for r in rows if r > 0]
    if len(rows) > M:
        return Fraction(0)
    cols = [sum(1 for r in rows if r > c) for c in range(rows[0])] if rows else []
    num = Fraction(1)
    for i, r in enumerate(rows):
        for c in range(r):
            hook = (r - c - 1) + (cols[c] - i - 1) + 1
            num *= Fraction(M + c - i, hook)
    return num


def closed(M1, M2, l1, l2):
    M = M1 + M2
    s = Fraction(1)
    for c in range(1, l1 + 1):
        s *= Fraction(M - 1 + c, M1 - 1 + c)
    for c in range(1, l2 + 1):
        s *= Fraction(M - 2 + c, M2 - 1 + c)
    return s * Fraction(l1 - l2 + 1, l1 + 1)


fails = 0
n = 0
for M1 in range(2, 8):
    for M2 in range(2, 8):
        for l1 in range(0, 9):
            for l2 in range(0, l1 + 1):
                lhs = dim_u(M1 + M2, [l1, l2]) / (dim_u(M1, [l1]) * dim_u(M2, [l2]))
                n += 1
                fails += lhs != closed(M1, M2, l1, l2)
print('(a) two-row closed form: %d cases, %d failures' % (n, fails))
ok &= fails == 0

inc = closed(2, 24, 13, 13) / closed(2, 24, 13, 12)
print('(b) exp increment at (2,24,13,12) =', inc)
ok &= inc == Fraction(37, 72)


def delta_log(M1, M2, q1, q2, l1, l2):
    M = M1 + M2
    s = 0.0
    for r in range(1, q1 + 1):
        s += sum(math.log((M + c - r) / (M1 + c - r)) for c in range(1, l1 + 1))
    for r in range(1, q2 + 1):
        s += sum(math.log((M - q1 + c - r) / (M2 + c - r)) for c in range(1, l2 + 1))
    for r in range(1, q1 + 1):
        s += sum(math.log((l1 - c + q1 - r + 1) / (l1 - c + q1 + q2 - r + 1)) for c in range(1, l2 + 1))
    return s


def G(m, u):
    return (m + u) * math.log(m + u) - m * math.log(m) - u


N = 3200
d = delta_log(N // 2, N // 2, 1, 1, N // 2, N // 2) / N
lim = 2 * (G(1.0, 0.5) - G(0.5, 0.5))
print('(c) Delta/N at N=3200: %.6f ; limit %.9f ; log(27/16) = %.9f' % (d, lim, math.log(27 / 16)))
ok &= abs(d - 0.520906) < 1e-6 and abs(lim - math.log(27 / 16)) < 1e-12
M = N
rat = sum(M / (M + c - r) for r in (1, 2) for c in range(1, N // 2 + 1)) / N
print('(c) rank ratio at N=3200: %.4f ; limit 2 log(3/2) = %.6f' % (rat, 2 * math.log(1.5)))
ok &= abs(rat - 0.8111) < 5e-5

for q in (1, 2, 3):
    res = []
    for N in (400, 800, 1600, 3200):
        res.append(delta_log(N // 2, N // 2, q, q, N // 2, N // 2) - N * q * lim)
    incs = [res[i] - res[i + 1] for i in range(3)]
    print('(d) q=%d residual N(Lambda q) - Delta: %s ; increments %s ; q^2 log 2 = %.4f'
          % (q, ['%.2f' % (-x) for x in res], ['%.3f' % x for x in incs], q * q * math.log(2)))
    ok &= all(abs(x - q * q * math.log(2)) < 0.08 for x in incs) and incs[0] < incs[1] < incs[2] < q * q * math.log(2)


def phi(rho):
    u = 0.5 * math.sqrt(rho)
    return G(1.0, u) - G(0.5, u)


x, w = np.polynomial.legendre.leggauss(200)
for g, avg_exp, min_exp in [(1.4, 0.522655, 0.479485), (2.0, 0.519217, 0.396700), (2.6, 0.511350, 0.268892)]:
    a = (3 - g) / 2
    rhos = [0.5 * (3 - (a + (g - a) * t * t)) for t in x]
    mean = sum(wi * phi(r) for wi, r in zip(w, rhos)) / 2
    avg = 2 * mean
    rmin = 0.5 * (3 - max(a, g))
    mn = 2 * phi(rmin)
    print('(e) gamma=%.1f averaged %.6f frame minimum %.6f' % (g, avg, mn))
    ok &= abs(avg - avg_exp) < 1e-6 and abs(mn - min_exp) < 1e-6

r_, u0 = sp.symbols('rho u0', positive=True)
Mm, mm = sp.symbols('M m', positive=True)
uu = u0 * sp.sqrt(r_)
Gs = lambda m, u: (m + u) * sp.log(m + u) - m * sp.log(m) - u
prof = Gs(Mm, uu) - Gs(mm, uu)
d1 = sp.simplify(sp.diff(prof, r_))
d2 = sp.simplify(sp.diff(prof, r_, 2))
print('(f) d profile/d rho =', d1)
print('(f) d2 profile/d rho2 =', d2)
num = [d2.subs({Mm: 1.0, mm: 0.5, u0: 0.5, r_: rv}) for rv in (0.05, 0.5, 1.0, 2.0, 5.0)]
num1 = [d1.subs({Mm: 1.0, mm: 0.5, u0: 0.5, r_: rv}) for rv in (0.05, 0.5, 1.0, 2.0, 5.0)]
print('(f) samples d1 > 0:', all(v > 0 for v in num1), ' d2 < 0:', all(v < 0 for v in num))
ok &= all(v > 0 for v in num1) and all(v < 0 for v in num)

# (g) equal against unequal row fractions
import itertools
f1 = 0
n1 = 0
for l1, l2, q1, q2, r in itertools.product(range(0, 9), range(0, 9), range(1, 4), range(1, 4), range(1, 4)):
    if l2 > l1 or r > q1:
        continue
    a = l1 + q1 - r + 1
    lhs = Fraction(1)
    for c in range(1, l2 + 1):
        lhs *= Fraction(a - c, a + q2 - c)
    rhs = Fraction(1)
    for j in range(q2):
        rhs *= Fraction(a - l2 + j, a + j)
    n1 += 1
    f1 += lhs != rhs
print('(g1) hook telescoping: %d cases, %d failures' % (n1, f1))
ok &= f1 == 0


def hookpart(q1, q2, l1, l2):
    return sum(math.log((l1 - l2 + q1 - r + 1 + j) / (l1 + q1 - r + 1 + j))
               for r in range(1, q1 + 1) for j in range(q2))


def Lam(M1, M2, l1, l2, q1, q2, N):
    m1, m2, u1, u2 = M1 / N, M2 / N, l1 / N, l2 / N
    return q1 * (G(m1 + m2, u1) - G(m1, u1)) + q2 * (G(m1 + m2, u2) - G(m2, u2))


Ns = (480, 960, 1920, 3840)
cases = [((Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2)), 'equal'),
         ((Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(3, 10)), 'unequal'),
         ((Fraction(1, 2), Fraction(1, 3), Fraction(2, 5), Fraction(1, 4)), 'unequal'),
         ((Fraction(1, 2), Fraction(1, 2), Fraction(9, 20), Fraction(3, 10)), 'unequal')]
for (m1, m2, u1, u2), kind in cases:
    for q in (1, 2, 3):
        res, cres, hk = [], [], []
        for N in Ns:
            M1, M2, l1, l2 = int(m1 * N), int(m2 * N), int(u1 * N), int(u2 * N)
            D = delta_log(M1, M2, q, q, l1, l2)
            Hk = hookpart(q, q, l1, l2)
            L = N * Lam(M1, M2, l1, l2, q, q, N)
            res.append(L - D)
            cres.append(L - (D - Hk))
            hk.append(-Hk)
        inc = [res[i + 1] - res[i] for i in range(3)]
        cinc = [cres[i + 1] - cres[i] for i in range(3)]
        print('(g2) %-7s (m1,m2,u1,u2)=(%s,%s,%s,%s) q=%d residual %s incr %s | content-part incr %s | -Hk %s'
              % (kind, m1, m2, u1, u2, q, ['%.3f' % x for x in res], ['%.3f' % x for x in inc],
                 ['%.4f' % x for x in cinc], ['%.3f' % x for x in hk]))
        ok &= all(abs(x) < 0.05 for x in cinc)
        if kind == 'equal':
            ok &= all(abs(x - q * q * math.log(2)) < 0.08 for x in inc)
        else:
            lim_h = q * q * math.log(float(u1 / (u1 - u2)))
            print('(g3) unequal: -Hk at N=3840 %.4f against q1 q2 log(u1/(u1-u2)) = %.4f' % (hk[-1], lim_h))
            ok &= abs(inc[-1]) < 0.1 and max(abs(x) for x in res) < 12 and abs(hk[-1] - lim_h) < 0.05 and abs(hk[-1] - lim_h) < abs(hk[0] - lim_h)
print('all checks inside thresholds:', ok)
assert ok
print('PASS d3')
