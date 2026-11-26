# 094 s1 v6 (FINAL): exact face bookkeeping, exponent identities, numeric divergence witnesses
# (v2 mpf import; v3 quad endpoints; v4 quad accuracy; v5 slope window too early - L in [20,24]
#  is resolution- and window-consistent (checked N=3000/9000); v6: D2 a=1/16 (v5 picked E=0))
from fractions import Fraction as F
from math import comb
import itertools
import numpy as np
import sympy as sp
from mpmath import mp, mpf, quad

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

def Im3(p, L, N=3000):  # int_{[e^-L,1]^2} (y1 y2 (y1+y2))^-p dy via log-grid trapz
    s = np.linspace(0.0, L, N)
    Ss, Tt = np.meshgrid(s, s, indexing='ij')
    H = np.exp((p - 1) * (Ss + Tt)) * (np.exp(-Ss) + np.exp(-Tt)) ** (-p)
    return np.trapezoid(np.trapezoid(H, s, axis=1), s)
def lslope(p, L1, L2):
    return (np.log(Im3(p, L2, 6000)) - np.log(Im3(p, L1, 6000))) / (L2 - L1)
sl_div = lslope(0.8, 20.0, 24.0)   # divergent corner: slope -> 3p-2 = 0.4
sl_fin = lslope(0.6, 20.0, 24.0)   # p = 0.6 < 2/3: bounded, slope -> 0 (rate 2-3p = 0.2)
cD1 = abs(sl_div - 0.4) < 0.005 and abs(sl_fin) < 0.01
print('PART D1 log-grid slope on L in [20,24]: m=3 p=0.8 %.4f (pred +0.400); p=0.6 %.4f (pred 0)' % (sl_div, sl_fin), cD1)

mp.dps = 15
angB = quad(lambda v: abs(2 * v - 1) ** (mpf('-0.25')) * (v * (1 - v)) ** (mpf('0.0625') - 1), [0, mpf('0.5'), 1])
radE = 2 * mpf('0.0625') - (1 - mpf('0.75')) * 1  # r=2, a=1/16, beta=3/4: E = 2a - (1-b)*binom(2,2)
cD2 = angB < mpf('1000') and radE < 0
print('PART D2 zero cluster r=2,a=1/16,beta=3/4: angular integral %.3f finite; radial E = %s < 0: divergence eta^E, eta=1e-6 gives %.1f' % (angB, radE, mpf('1e-6') ** radE))
print('S1 OVERALL:', 'PASS' if (okA and okB and okC and tab and cD1 and cD2) else 'FAIL')
