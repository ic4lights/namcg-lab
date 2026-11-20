# 094 s1 v2: exact face bookkeeping, exponent identities, numeric divergence witnesses
# (supersedes s1_localization_094.py: missing mpmath.mpf import in Part D; Parts A-C unchanged)
from fractions import Fraction as F
from math import comb
import itertools
import sympy as sp
from mpmath import mp, mpf, quad, log

def runlens(S):
    S = sorted(S); out = []; cur = 0; prev = None
    for k in S:
        cur = cur + 1 if prev is not None and k == prev + 1 else 1
        if cur == 1:
            out.append(1)
        else:
            out[-1] += 1
        prev = k
    return out

okA = True
for D in range(2, 9):
    gaps = list(range(1, D))
    facecond = []
    for r in range(len(gaps) + 1):
        for Sc in itertools.combinations(gaps, r):
            S = set(Sc)
            direct = sum(1 for i in range(1, D) for j in range(i + 1, D + 1) if all(k in S for k in range(i, j)))
            zero_pairs = sum(comb(l + 1, 2) for l in runlens(S))
            if direct != zero_pairs:
                okA = False
            if S:
                facecond.append(min(F(2, l + 1) for l in runlens(S)))
    if min(facecond) != F(2, D):
        okA = False
print('PART A zero-pair counts = sum binom(l+1,2) over runs; face thresholds 2/(s+1); chamber min = 2/D (D=2..8):', okA)

beta = sp.Symbol('beta', real=True)
okB = True
for m in range(2, 9):
    N = comb(m, 2)
    e = (m - 1) - 1 - (1 - beta) * N            # transverse polar exponent, weight rho^e dr
    okB = okB and sp.simplify((e + 1) - N * (beta - (1 - F(2, m)))) == 0
    okB = okB and sp.solve(sp.Eq(e + 1, 0), beta)[0] == 1 - F(2, m)
    okB = okB and sp.solve(sp.Eq(e, -1), beta)[0] == 1 - F(2, m)
print('PART B identity e+1=binom(m,2)(beta-(1-2/m)); threshold beta=1-2/m; e=-1 iff beta=1-2/m (m=2..8):', okB)

a = sp.Symbol('a', positive=True)
okC = True
for r in range(2, 8):
    radial = (beta - 1) * comb(r, 2) + r * (a - 1) + r - 1   # orthant polar exponent at r-zero cluster
    okC = okC and sp.solve(sp.Eq(radial + 1, 0), beta)[0] == 1 - 2 * a / (r - 1)
tab = all(min(min(F(2, rp), 2 * F(1, 4) / (rp - 1)) for rp in range(2, rr + 1)) == min(F(2, rr), 2 * F(1, 4) / (rr - 1)) for rr in range(2, 9))
print('PART C zero-cluster radial condition beta>1-2a/(r-1) (r=2..7); nested face min attained at r (a=1/4):', okC and tab)

mp.dps = 14
def I2(f, eta):
    return quad(lambda y: quad(lambda x: f(x, y), eta, 1, [y]), eta, 1, [0.5])
def fitslope(f, e_pred):
    v = [(I2(f, eta), log(mpf(eta))) for eta in ('1e-2', '1e-3', '1e-4')]
    s = (log(v[0][0]) - log(v[2][0])) / (v[0][1] - v[2][1])
    return abs(s - e_pred) < mpf('0.03'), s
p8 = mpf('0.8'); p6 = mpf('0.6'); a8 = mpf('0.125')
c3, s3 = fitslope(lambda x, y: (x * y * (x + y)) ** (-p8), mpf('-0.4'))     # interior m=3 corner: 2-3p
c3b = I2(lambda x, y: (x * y * (x + y)) ** (-p6), mpf('1e-8')) < mpf('1e6')  # p=0.6<2/3 stays bounded
cB, sB = fitslope(lambda x, y: abs(x - y) ** (p6 - 1) * (x * y) ** (a8 - 1), mpf('-0.25'))  # r=2,a=1/8,beta=1/2: 2a-(1-b)
print('PART D slopes: m=3 interior p=0.8 -> %.3f (pred -0.400) %s; p=0.6 bounded %s; zero-cluster -> %.3f (pred -0.250) %s' % (s3, c3, c3b, sB, cB))
print('S1 OVERALL:', 'PASS' if (okA and okB and okC and tab and c3 and c3b and cB) else 'FAIL')
