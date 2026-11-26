# 094 spot: independent re-check of the 094 localization claims (different code path from s1_v6)
# (1) exponent identity e+1 = C(m,2)(b-(1-2/m)); (2) s=3 (m=4) model-integral two-sided numeric;
# (3) boundary r=2 zero-cluster divergence rate at (a,b)=(1/16,3/4); (4) face pair-count bookkeeping.
import numpy as np
import sympy as sp
from math import comb
bb = sp.Symbol('b')
ok1 = True
thr = []
for m in (2, 3, 4, 6):
    e = (m - 2) - (1 - bb) * comb(m, 2)
    ok1 = ok1 and sp.simplify((e + 1) - comb(m, 2) * (bb - (1 - sp.Rational(2, m)))) == 0
    r = sp.solve(sp.Eq(e + 1, 0), bb)
    if m <= 4:
        thr.append(r[0])
print('1 identity+thresholds', ok1, 'm=2,3,4 thresholds:', thr)

def runsum(S, D):  # independent pair-count: pairs whose gap-interval lies in S
    return sum(1 for i in range(1, D) for j in range(i + 1, D + 1) if set(range(i, j)) <= S)
def lensum(S):
    S = sorted(S); tot = 0; L = 0; prev = None
    for k in S:
        L = L + 1 if prev is not None and k == prev + 1 else 1
        tot += comb(L + 1, 2)
        prev = k
    return tot
ok4 = all(runsum(set(C), 7) == lensum(set(C)) for n in range(7) for C in __import__('itertools').combinations(range(1, 7), n))
print('4 pair-count sum binom(l+1,2) over runs (all subsets, D=7):', ok4)

def I3(p, L, N=140):  # s=3 model integral over [e^-L,1]^3, log-grid trapz, 6 consecutive-sum factors
    u = np.linspace(0.0, L, N)
    y = np.exp(-u)
    a1 = y[:, None, None]
    a2 = y[None, :, None]
    a3 = y[None, None, :]
    prod = a1 * a2 * a3 * (a1 + a2) * (a2 + a3) * (a1 + a2 + a3)
    H = prod ** (-p) * a1 * a2 * a3
    return np.trapezoid(np.trapezoid(np.trapezoid(H, u, 0), u, 1), u, 2)
def slope(f, p, L1, L2, N=140):
    return (np.log(f(p, L2, N)) - np.log(f(p, L1, N))) / (L2 - L1)
d1 = slope(I3, 0.55, 12.0, 15.0)
f1 = slope(I3, 0.45, 12.0, 15.0)
print('2 s=3 slope L in [12,15]: p=0.55 %.4f (pred 6p-3=0.300 div); p=0.45 %.4f (pred ~0 conv) ok %s' % (d1, f1, abs(d1 - 0.30) < 0.01 and abs(f1) < 0.03))

def I2b(a, p, L, N=1500):  # r=2 zero cluster: int (xy)^(a-1)|x-y|^(p-1) over [e^-L,1]^2, log-grid
    u = np.linspace(0.0, L, N)
    y = np.exp(-u)
    X = y[:, None]
    Y = y[None, :]
    W = X ** (a - 1) * Y ** (a - 1) * np.abs(X - Y + 0.0) ** (p - 1) * X * Y
    np.fill_diagonal(np.asarray(W), 0.0) if np.ndim(W) == 2 and W.shape[0] == W.shape[1] else None
    return np.trapezoid(np.trapezoid(W, u, 0), u, 1)
# diagonal singular |x-y|^(p-1) with p-1=-1/4: set diagonal to cell-average surrogate by epsilon shift
def I2c(a, p, L, N=1500):
    u = np.linspace(0.0, L, N)
    y = np.exp(-u)
    X = y[:, None]
    Y = y[None, :]
    dif = np.abs(X - Y) + y[:, None] * (u[1] - u[0])  # cell-scale diagonal cutoff
    W = X ** (a - 1) * Y ** (a - 1) * dif ** (p - 1) * X * Y
    return np.trapezoid(np.trapezoid(W, u, 0), u, 1)
d2 = slope(I2c, 0, 10.0, 12.0, 0) if False else (np.log(I2c(1/16, 3/4, 12.0)) - np.log(I2c(1/16, 3/4, 10.0))) / 2.0
print('3 r=2 cluster (a,b)=(1/16,3/4) slope L in [10,12]: %.4f (pred 1/8=0.125 div since b<1-2a=7/8) ok %s' % (d2, abs(d2 - 0.125) < 0.015))
print('SPOT OVERALL:', 'PASS' if (ok1 and ok4 and abs(d1 - 0.30) < 0.01 and abs(f1) < 0.03 and abs(d2 - 0.125) < 0.015) else 'FAIL')
