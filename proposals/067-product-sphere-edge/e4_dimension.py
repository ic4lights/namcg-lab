"""
067 e4: dimension of the U(M) irreducible representation with r equal rows on each side,
highest weight (ell^r, 0^{M-2r}, (-ell)^r), from the Weyl dimension formula (exact products, evaluated in logs),
and of the one-sided rectangle (ell^r, 0^{M-r}) from the hook-content formula (cross-check of the two formulas).

Reported:
 (i)   d log d / d log M  ->  |mu| = 2 r ell          (rank dependence at fixed diagram; 065 for general diagrams);
 (ii)  c(r, ell, M) := log d / (2 r ell) - log( M / (r + ell) ), which stays O(1): the rank enters through M/(r+ell);
 (iii) log d(r rows) / ( r * log d(1 row) ) < 1: the r-row value is below r times the one-row value
       2 ell log(e M / ell) of arXiv:2408.05274 Eq. (3.14), by about 2 r ell [ log((r+ell)/ell) + O(1) ];
 (iv)  block cap x whole sphere: M = M1 N, r = N: dependence on N at fixed depth M1 and fixed ell.
Output to stdout only.
"""
import numpy as np
from math import lgamma, log

def logdim_weyl(lam):
    lam = np.asarray(lam, dtype=np.int64); M = len(lam)
    # only pairs with lam_i != lam_j contribute; group by value
    vals, starts = np.unique(-lam, return_index=True)           # descending lam
    starts = list(starts) + [M]
    tot = 0.0
    for g in range(len(vals)):
        for h in range(g + 1, len(vals)):
            i = np.arange(starts[g], starts[g + 1])[:, None]; j = np.arange(starts[h], starts[h + 1])[None, :]
            d = float(lam[starts[g]] - lam[starts[h]])
            tot += (np.log(d + (j - i)) - np.log(j - i)).sum()
    return tot

def logdim_hook(r, ell, M):                                      # one-sided rectangle r x ell
    tot = 0.0
    for i in range(r):
        for j in range(ell):
            tot += log(M + j - i) - log((r - i) + (ell - j) - 1)
    return tot

def two_sided(r, ell, M):
    assert 2 * r <= M
    return logdim_weyl([ell] * r + [0] * (M - 2 * r) + [-ell] * r)

# cross-check Weyl against hook-content for one-sided rectangles
dev = 0.0
for (r, ell, M) in ((1, 5, 9), (3, 4, 11), (6, 2, 40), (5, 17, 60)):
    a = logdim_weyl([ell] * r + [0] * (M - r)); b = logdim_hook(r, ell, M); dev = max(dev, abs(a - b))
print('Weyl vs hook-content, one-sided rectangles: max |difference of logs| = %.1e' % dev)
assert dev < 1e-8
# small exact case: adjoint of U(M), weight (1,0,...,0,-1), dim M^2 - 1
assert abs(two_sided(1, 1, 7) - log(48)) < 1e-10

print('(i),(ii)  two-sided rectangle (ell^r, 0, (-ell)^r) in U(M)')
print('    r   ell      M    log d      dlogd/dlogM /(2 r ell)   c = logd/(2 r ell) - log(M/(r+ell))   logd(r)/(r logd(1))   deficit/(2 r ell log((r+ell)/ell))')
for (r, ell) in ((1, 40), (4, 40), (16, 40), (40, 40), (160, 40), (40, 4), (40, 400)):
    for M in (4000, 16000):
        if 2 * r + 2 > M: continue
        L = two_sided(r, ell, M); Lp = two_sided(r, ell, int(M * 1.02))
        slope = (Lp - L) / log(int(M * 1.02) / M) / (2 * r * ell)
        c = L / (2 * r * ell) - log(M / (r + ell))
        L1 = two_sided(1, ell, M)
        deficit = r * L1 - L
        dn = 2 * r * ell * log((r + ell) / ell)
        print('  %4d %4d %6d  %10.2f   %8.4f                 %8.4f                              %8.4f              %s'
              % (r, ell, M, L, slope, c, L / (r * L1), ('%8.4f' % (deficit / dn)) if r > 1 else '   -'))
        assert 0.7 < c < 1.1 and (r == 1 or L < r * L1)

print('(iv)  block cap x whole sphere: M = M1 N, r = N, fixed depth M1 = 50 and ell = 30')
print('     N      M    log d / (2 N ell)    log(M1) = %.4f' % log(50))
for N in (10, 20, 40, 80, 160):
    M = 50 * N
    L = two_sided(N, 30, M)
    print('  %4d %6d    %8.4f     [log(M/(N+ell)) = %.4f, log(e M/ell) = %.4f]' % (N, M, L / (2 * N * 30), log(M / (N + 30)), log(np.e * M / 30)))
print('PASS e4')
