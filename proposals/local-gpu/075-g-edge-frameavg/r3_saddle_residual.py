"""073 s3 (copy of 072 s3_saddle_residual.py, review-r1 finding 3 fixed:
stale seed/comment lines and docstring ratio expectation; logic and prints unchanged): dominant-saddle residual on the product testbed, N scaling.

Class: saddle rows l_i = t * s_i with s_f^2 = k_f M_f (N - M_f) (the 065
relation <l^2> = 4 s^2 W with t = 2 sqrt(W)); block rank M = M1 + M2;
entropy defect Delta from s2 with these rows.

(1) N scaling: M_f = m_f N, k=1, t in {0.5,1,2}, N up to 3200: report
    Delta/N and the leading prediction
    [l1 log(1+M2/M1) + l2 log(1+M1/M2)]/N -> positive constant; the ratio
    Delta / leading does NOT tend to 1: it stabilises near 0.75 at t=1 and is
    0.85 at t=0.5, 0.62 at t=2 (072 run; the naive leading form overcounts).
(2) Corner-mode non-additivity of the selection input:
    delta_p = (s1^2+s2^2)^p - s1^{2p} - s2^{2p} (the corner mode, p>=2)
    against Tr E^p; report delta_p/TrE^p at the s1-style finite-N cases
    (N = 6,9,12) and at the m-fraction scaling (N = 100..3200): O(1/N).
(3) The s1 finite-N cases evaluated at t=1: Delta and the leading
    prediction; all positive.
(4) Rank dependence at the saddle: partial logdim / partial logM =
    sum_{(r,c)} M/(M+c-r) evaluated at the saddle diagram of case (1),
    vs |mu| = l1+l2; report the ratio (-> 1 for M >> l, and the value at
    the testbed fractions).

Run: python -I proposals/073-g-edge-rowshift/s3_saddle_residual.py
Expected invariants: Delta/N -> constant (increasing N), Delta/leading
stabilising near 0.75 at t=1 (see docstring (1)), delta_p/TrE^p ~ 1/N;
all Delta > 0; 'PASS s3'.
"""
import math


def Delta(M1, M2, l1v, l2v):
    t1 = sum(math.log((M1 + M2 - 1 + c) / (M1 - 1 + c)) for c in range(1, l1v + 1))
    t2 = sum(math.log((M1 + M2 - 2 + c) / (M2 - 1 + c)) for c in range(1, l2v + 1))
    return t1 + t2 - math.log((l1v + 1) / (l1v - l2v + 1))


def lead(M1, M2, l1v, l2v):
    return l1v * math.log((M1 + M2) / M1) + l2v * math.log((M1 + M2) / M2)


# ---------- (1) N scaling ----------
print('(1) N scaling, m1=m2=0.5, k=1:')
prev = None
for t in (0.5, 1.0, 2.0):
    for N in (100, 200, 400, 800, 1600, 3200):
        M1 = M2 = N // 2
        s = math.sqrt(M1 * (N - M1))
        l = max(1, int(round(t * s)))
        d = Delta(M1, M2, l, l)
        ld = lead(M1, M2, l, l)
        print('  t=%.1f N=%5d l=%5d Delta/N=%.6f leading/N=%.6f ratio=%.6f'
              % (t, N, l, d / N, ld / N, d / ld))
    print('  (t=%.1f leading/N prediction: %.6f)' % (t, 2 * t * math.sqrt(0.25) * math.log(2.0)))

# ---------- (2) corner-mode moment non-additivity ----------
print('(2) corner correction delta_p / TrE^p:')
cases = []  # representative small product cases, k set to 1 (not the s1 random-seed cases)
for N, M1, M2 in ((6, 4, 2), (9, 4, 6), (12, 10, 5)):
    k1 = k2 = 1.0
    s1sq = k1 * M1 * (N - M1)
    s2sq = k2 * M2 * (N - M2)
    for p in (2, 3):
        tot = (M2 - 1) * s1sq ** p + (M1 - 1) * s2sq ** p + (s1sq + s2sq) ** p
        dlt = (s1sq + s2sq) ** p - s1sq ** p - s2sq ** p
        print('  N=%2d M1=%2d M2=%2d p=%d  delta_p/TrE^p = %.4e' % (N, M1, M2, p, dlt / tot))
for N in (100, 400, 1600, 3200):
    M1 = N // 2
    M2 = N // 3
    s1sq = M1 * (N - M1)
    s2sq = M2 * (N - M2)
    p = 2
    tot = (M2 - 1) * s1sq ** p + (M1 - 1) * s2sq ** p + (s1sq + s2sq) ** p
    dlt = (s1sq + s2sq) ** p - s1sq ** p - s2sq ** p
    print('  N=%5d m1=1/2 m2=1/3 p=%d  delta_p/TrE^p = %.4e  (xN = %.4f)'
          % (N, p, dlt / tot, N * dlt / tot))

# ---------- (3) s1-style finite-N cases at t=1 ----------
print('(3) finite-N product cases, t=1, k=1:')
for N, M1, M2 in ((6, 4, 2), (9, 4, 6), (12, 10, 5), (12, 8, 3)):
    s1 = math.sqrt(M1 * (N - M1))
    s2 = math.sqrt(M2 * (N - M2))
    l1v, l2v = int(round(max(s1, s2))), int(round(min(s1, s2)))
    d = Delta(M1, M2, l1v, l2v)
    print('  N=%2d M1=%2d M2=%2d rows=(%d,%d) Delta=%.4f leading=%.4f  positive=%s'
          % (N, M1, M2, l1v, l2v, d, lead(M1, M2, l1v, l2v), d > 0))
    assert d > 0

# ---------- (4) rank dependence at the saddle ----------
print('(4) dlogdim/dlogM at the saddle diagram vs |mu|:')
for N in (200, 800, 3200):
    M1 = M2 = N // 2
    s = math.sqrt(M1 * (N - M1))
    l = int(round(s))
    M = M1 + M2
    dsum = sum(M / (M + c - r) for r, L in ((1, l), (2, l)) for c in range(1, L + 1))
    print('  N=%5d rows=(%d,%d)  sum M/(M+c-r)=%.1f  |mu|=%d  ratio=%.4f'
          % (N, l, l, dsum, 2 * l, dsum / (2 * l)))

print('PASS s3')
