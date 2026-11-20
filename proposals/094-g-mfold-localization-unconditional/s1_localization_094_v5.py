# 094 s1 v5: exact face bookkeeping, exponent identities, numeric divergence witnesses
# (v2 mpf import; v3 quad endpoints; v4 mpmath quad accuracy on singular 2D cuts;
#  v5: Part D by numpy log-grid for the smooth interior corner + exact radial/angular split
#  for the zero cluster; Parts A-C unchanged; all quadrature deterministic, no RNG)
from fractions import Fraction as F
from math import comb
import itertools
import numpy as np
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

def Im3(p, L, N=3000):  # int_{[e^-L,1]^2} (y1 y2 (y1+y2))^-p dy via log-grid trapz, smooth integrand
    s = np.linspace(0.0, L, N)
    Ss, Tt = np.meshgrid(s, s, indexing='ij')
    H = np.exp((2 * p - 2) * (Ss + Tt) / 1) * (np.exp(-Ss) + np.exp(-Tt)) ** (-p) * 1.0
    H = np.exp((p - 1) * Ss + (p - 1) * Tt) * (np.exp(-Ss) + np.exp(-Tt)) ** (-p)
    return np.trapezoid(np.trapezoid(H, s, axis=1), s)
def lslope(p, Ls):
    v = [np.log(Im3(p, L)) for L in Ls]
    return (v[-1] - v[0]) / (Ls[0] - Ls[-1]) * -1.0
sl_div = lslope(0.8, (4.0, 16.0))              # expect 3p-2 = 0.4 (divergent corner)
sl_fin = lslope(0.6, (4.0, 16.0))              # expect -> 0 (p = 0.6 < 2/3: bounded)
cD1 = abs(sl_div - 0.4) < 0.01 and abs(sl_fin) < 0.02
print('PART D1 log-grid slopes (eta=e^-L): m=3 p=0.8 slope %.4f (pred +0.400); p=0.6 slope %.4f (pred 0)' % (sl_div, sl_fin), cD1)

mp.dps = 15
angB = quad(lambda v: abs(2 * v - 1) ** (-mpf('0.25')) * (v * (1 - v)) ** (mpf('0.125') - 1), [0, mpf('0.5'), 1])
radE = 2 * mpf('0.125') - (1 - mpf('0.75')) * 1  # r=2, a=1/8, beta=3/4: E = 2a - (1-b)binom(2,2)
cD2 = angB < mpf('100') and radE < 0
print('PART D2 zero cluster r=2,a=1/8,beta=3/4: angular integral %.4f finite; radial E = %s < 0 (divergence eta^E, eta^-E = %s)' % (angB, radE, (mpf('1e-6') ** radE)))
print('S1 OVERALL:', 'PASS' if (okA and okB and okC and tab and cD1 and cD2) else 'FAIL')
