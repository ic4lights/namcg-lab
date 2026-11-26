"""
065 s5: form of the edge entropy log dim_{U(M)} mu and its dependence on the rank M.

(a) sympy: the row length of arXiv:2408.05274 Eq. (3.14) [eqn:cap-ee], ell = sqrt(nu^3 Lam^3 N)|dS|/(4 sqrt3 pi),
    with |dS| = 4 pi sqrt(M(N-M))/N [Eq. (3.13)], is ell^2 = nu^3 Lam^3 M(N-M)/(3N).
(b) hook-content formula dim_{U(M)} mu = prod_{boxes} (M + c - r)/hook(r,c) checked against the Weyl formula.
(c) at fixed diagram mu, d log dim / d log M = sum_boxes M/(M+c-r) -> |mu| as M -> infinity (exact formula,
    numerical evaluation): the dimension of the edge irrep depends on the rank M of the block, not only on the
    boundary data (the diagram).
(d) two disjoint caps (rows ell_1, ell_2 of one diagram of U(M1+M2), one-sided diagram): log dim exceeds the sum
    of the single-cap values log dim_{U(M1)}[ell_1] + log dim_{U(M2)}[ell_2] by about
    ell_1 log((M1+M2)/M1) + ell_2 log((M1+M2)/M2) (minus a hook correction of order log): not additive.
(e) flat diagram: 2 ell log(eM/ell) vs exact 2 log binom(M+ell-1, ell) for M >> ell >> 1.
Output to stdout only.
"""
import itertools, math
import sympy as s
from fractions import Fraction

# (a)
nu, Lam, N, M = s.symbols('nu Lambda N M', positive=True)
dS = 4 * s.pi * s.sqrt(M * (N - M)) / N
ell = s.sqrt(nu ** 3 * Lam ** 3 * N) * dS / (4 * s.sqrt(3) * s.pi)
print('(a) ell^2 =', s.simplify(ell ** 2), '; equals nu^3 Lam^3 M(N-M)/(3N):',
      s.simplify(ell ** 2 - nu ** 3 * Lam ** 3 * M * (N - M) / (3 * N)) == 0)

# (b)
def boxes(lam):
    return [(r, c) for r, row in enumerate(lam, 1) for c in range(1, row + 1)]

def hook(lam, r, c):
    conj = [sum(1 for row in lam if row >= cc) for cc in range(1, (lam[0] if lam else 0) + 1)]
    return (lam[r - 1] - c) + (conj[c - 1] - r) + 1

def dim_hook(lam, M):
    v = Fraction(1)
    for r, c in boxes(lam):
        v *= Fraction(M + c - r, hook(lam, r, c))
    return v

def dim_weyl(lam, M):
    l = list(lam) + [0] * (M - len(lam))
    if len(lam) > M:
        return Fraction(0)
    v = Fraction(1)
    for i in range(M):
        for j in range(i + 1, M):
            v *= Fraction(l[i] - l[j] + j - i, j - i)
    return v

ok = True
for lam in ([1], [2], [1, 1], [3, 1], [2, 2], [4, 2, 1], [5], [3, 3, 1]):
    for Mv in range(len(lam), 7):
        ok &= dim_hook(lam, Mv) == dim_weyl(lam, Mv)
print('(b) hook-content = Weyl dimension on the sampled diagrams and ranks:', ok)
assert ok

# (c)
def logdim(lam, Mv):
    return sum(math.log(Mv + c - r) - math.log(hook(lam, r, c)) for r, c in boxes(lam))

print('(c) d log dim / d log M at fixed diagram (exact sum M/(M+c-r)) divided by |mu|:')
for lam in ([40], [40, 25], [30, 30, 10]):
    sz = sum(lam)
    vals = []
    for Mv in (100, 1000, 10000, 100000):
        der = sum(Mv / (Mv + c - r) for r, c in boxes(lam))
        vals.append('M=%d: %.5f' % (Mv, der / sz))
    print('   mu =', lam, ' '.join(vals))

# (d)
print('(d) two caps, rows (ell1, ell2) = (30, 20) of one diagram of U(M1+M2), M1 = 2000:')
lam = [30, 20]
for M2 in (500, 2000, 8000):
    Mtot = 2000 + M2
    joint = logdim(lam, Mtot)
    sep = logdim([30], 2000) + logdim([20], M2)
    est = 30 * math.log(Mtot / 2000) + 20 * math.log(Mtot / M2)
    print('   M2=%5d: log dim (joint) = %.4f, sum of single-cap values = %.4f, difference = %.4f, estimate %.4f' % (M2, joint, sep, joint - sep, est))
    assert joint - sep > 1

# (e)
print('(e) flat diagram, 2 log binom(M+ell-1, ell) vs 2 ell log(e M / ell):')
for Mv, l in ((10 ** 4, 50), (10 ** 5, 100), (10 ** 6, 300)):
    exact = 2 * (math.lgamma(Mv + l) - math.lgamma(l + 1) - math.lgamma(Mv))
    approx = 2 * l * math.log(math.e * Mv / l)
    print('   M=%d ell=%d: exact %.2f, approx %.2f, ratio %.5f' % (Mv, l, exact, approx, exact / approx))
print('PASS s5')
