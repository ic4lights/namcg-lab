"""
067 e5 (round 2, finding F1): Weyl dimension of the U(M) highest weight (ell^r, 0^{M-2r}, (-ell)^r) over a full grid
of (r, ell), M = 4000 and 16000, to replace range statements by the bounds actually found.

Reported per grid point: slope = dlog d/dlog M /(2 r ell) (finite difference M -> 1.02 M),
c = log d/(2 r ell) - log(M/(r+ell)), ratio = log d(r) / (r log d(1)).
Then (a) the extrema over the whole grid, with the points where they occur;
     (b) the extrema over the seven pairs quoted in the manuscript text (the sampled pairs of e4);
     (c) the extrema of the slope over the six quoted pairs with ell <= 40.
Output to stdout only.
"""
import numpy as np
from math import log

def logdim_weyl(lam):
    lam = np.asarray(lam, dtype=np.int64); M = len(lam)
    vals, starts = np.unique(-lam, return_index=True)
    starts = list(starts) + [M]
    tot = 0.0
    for g in range(len(vals)):
        for h in range(g + 1, len(vals)):
            i = np.arange(starts[g], starts[g + 1])[:, None]; j = np.arange(starts[h], starts[h + 1])[None, :]
            d = float(lam[starts[g]] - lam[starts[h]])
            tot += (np.log(d + (j - i)) - np.log(j - i)).sum()
    return tot

def two_sided(r, ell, M):
    assert 2 * r <= M
    return logdim_weyl([ell] * r + [0] * (M - 2 * r) + [-ell] * r)

assert abs(two_sided(1, 1, 7) - log(48)) < 1e-10          # adjoint of U(7)

RS = (1, 2, 4, 8, 16, 40, 80, 160); LS = (4, 8, 16, 40, 100, 200, 400); MS = (4000, 16000)
QUOTED = ((1, 40), (4, 40), (16, 40), (40, 40), (160, 40), (40, 4), (40, 400))
rows = []
print('   r   ell      M     slope        c    ratio')
for r in RS:
    for ell in LS:
        for M in MS:
            L = two_sided(r, ell, M); M2 = int(M * 1.02); Lp = two_sided(r, ell, M2)
            slope = (Lp - L) / log(M2 / M) / (2 * r * ell)
            c = L / (2 * r * ell) - log(M / (r + ell))
            ratio = L / (r * two_sided(1, ell, M))
            rows.append((r, ell, M, slope, c, ratio))
            print('%4d %5d %6d  %8.5f %8.5f %8.5f' % (r, ell, M, slope, c, ratio))

def ext(sel, col, name):
    lo = min(sel, key=lambda t: t[col]); hi = max(sel, key=lambda t: t[col])
    print('  %-6s min %.5f at (r,ell,M)=(%d,%d,%d) ; max %.5f at (%d,%d,%d)' % (name, lo[col], lo[0], lo[1], lo[2], hi[col], hi[0], hi[1], hi[2]))
    return lo[col], hi[col]

print('(a) whole grid r in %s, ell in %s, M in %s' % (RS, LS, MS))
ext(rows, 3, 'slope'); ca = ext(rows, 4, 'c'); ra = ext([t for t in rows if t[0] > 1], 5, 'ratio')
print('(b) the seven quoted pairs, both M')
q = [t for t in rows if (t[0], t[1]) in QUOTED]
assert len(q) == 14
cq = ext(q, 4, 'c'); rq = ext([t for t in q if t[0] > 1], 5, 'ratio')
print('(c) slope, the six quoted pairs with ell <= 40, both M')
sq = ext([t for t in q if t[1] <= 40], 3, 'slope')
# the statements made in the manuscript text (sampled values)
assert 0.80 < cq[0] and cq[1] < 0.97
assert 0.69 < rq[0] and rq[1] < 0.99
assert abs(sq[0] - 1) < 0.02 and abs(sq[1] - 1) < 0.02
# the r1 range statement fails on the grid (finding F1): record it
print('(d) r1 range statement "0.80 < c < 0.97, ratio in [0.69, 0.98]" on the grid: c in [%.4f, %.4f], ratio in [%.4f, %.4f] -> %s'
      % (ca[0], ca[1], ra[0], ra[1], 'holds' if (0.80 < ca[0] and ca[1] < 0.97 and 0.69 <= ra[0] and ra[1] <= 0.98) else 'FAILS as a range statement'))
assert all(t[5] < 1 for t in rows if t[0] > 1)             # sub-additivity in r at the same M holds at every grid point
print('sub-additivity log d(r) < r log d(1) at the same M: holds at all %d grid points with r > 1' % len([t for t in rows if t[0] > 1]))
print('PASS e5')
