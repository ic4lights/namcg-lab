# 094 spot v2 (independent of s1_v6, different code paths; v1's own bugs: wrong run-sum accumulation,
# too-coarse 3D log grid (du~0.1 biases slopes), too-early boundary window - all fixed here)
# (1) exponent identity e+1 = C(m,2)(b-(1-2/m)) + thresholds; (2) face pair-count bookkeeping;
# (3) s=2 (m=3) model integral via nested EXACT 1D quadrature (no 2D grid): divergence slope 3p-2;
# (4) boundary r=2 zero cluster, two-sided in a at window L in [24,28]: slope -> 1-2a-b ... rate.
import numpy as np
import sympy as sp
from itertools import combinations
from math import comb
bb = sp.Symbol('b')
ok1 = True; thr = []
for m in (2, 3, 4, 6):
    e = (m - 2) - (1 - bb) * comb(m, 2)
    ok1 = ok1 and sp.simplify((e + 1) - comb(m, 2) * (bb - (1 - sp.Rational(2, m)))) == 0
    if m <= 4:
        thr.append(sp.solve(sp.Eq(e + 1, 0), bb)[0])
def runsum(S):
    S = sorted(S); tot = 0; L = 0; prev = None
    for k in S:
        if prev is not None and k == prev + 1:
            L += 1
        else:
            tot += comb(L + 1, 2); L = 1
        prev = k
    return tot + comb(L + 1, 2)
ok2 = all(sum(1 for i in range(1, 7) for j in range(i + 1, 8) if set(range(i, j)) <= set(C)) == runsum(C)
          for n in range(7) for C in combinations(range(1, 7), n))
print('1 identity+thresholds', ok1, 'm=2,3,4:', thr, '| 2 pair-count all subsets D=7:', ok2)

def Im2(p, Ls, M=120001, N=48001):  # int_[e^-L,1]^2 (y z (y+z))^-p via 1D+1D, exact inner via global cumtrapz
    Lmax = max(Ls) + 2.0
    v = np.linspace(-(Lmax + 2.0), Lmax + 2.0, M)
    g = np.exp(v * (1 - p) - p * np.logaddexp(0.0, v))  # t^-p (1+t)^-p dt, t=e^v
    F = np.concatenate(([0.0], np.cumsum((g[1:] + g[:-1]) / 2 * np.diff(v))))
    F = F - np.interp(0.0, v, F)                       # H(e^x) = int_1^{e^x}
    out = []
    for L in Ls:
        u = np.linspace(0.0, L, N)
        dH = np.interp(u, v, F) - np.interp(u - L, v, F)
        out.append(np.trapezoid(np.exp(-u * (2 - 3 * p)) * dH, u))
    return out
r8 = Im2(0.8, [20.0, 24.0]); r6 = Im2(0.6, [20.0, 24.0])
s8 = (np.log(r8[1]) - np.log(r8[0])) / 4.0
s6 = (np.log(r6[1]) - np.log(r6[0])) / 4.0
ok3 = abs(s8 - 0.4) < 0.01 and abs(s6) < 0.03
print('3 m=3 model L in [20,24]: p=0.8 slope %.4f (pred 3p-2=0.400 div); p=0.6 slope %.4f (pred ~0 conv)' % (s8, s6), ok3)

def Ib(a, p, L, N=1200):  # r=2 zero cluster int_[e^-L,1]^2 (xy)^(a-1)|x-y|^(p-1) dxdy, log-grid + cell cutoff
    u = np.linspace(0.0, L, N)
    y = np.exp(-u)
    X = y[:, None]; Y = y[None, :]
    dif = np.abs(X - Y) + X * (u[1] - u[0])
    W = X ** (a - 1) * Y ** (a - 1) * dif ** (p - 1) * X * Y
    return np.trapezoid(np.trapezoid(W, u, 0), u, 1)
def slope2(a, p, L1, L2):
    return (np.log(Ib(a, p, L2)) - np.log(Ib(a, p, L1))) / (L2 - L1)
sb_div = slope2(1 / 16, 3 / 4, 24.0, 28.0)   # beta=3/4 < 1-2a=7/8: diverge, rate lambda=2a+b-1=-1/8 -> slope->~0.131
sb_fin = slope2(1.0, 3 / 4, 24.0, 28.0)      # a=1: beta=3/4 > 1-2a=-1: converge, slope->0
ok4 = 0.115 < sb_div < 0.145 and abs(sb_fin) < 0.03
print('4 r=2 cluster L in [24,28]: (a,b)=(1/16,3/4) slope %.4f (asympt 0.131 div); (1,3/4) slope %.4f (pred ~0 conv)' % (sb_div, sb_fin), ok4)
print('SPOT OVERALL:', 'PASS' if (ok1 and ok2 and ok3 and ok4) else 'FAIL')
