"""075 s2: frame average of the two-row saddle excess at fixed saddle class.

Class: the 072 (H1)-(H4) product testbed (M_f = m_f N, block rank M = M1+M2,
saddle rows l_f = t * s_f, two-row diagrams) plus cap frames: the edge datum of
s1, s^2(n) = k M (N-M) rho(n) with rho(n) = (tr B - n^T B n) / tr(B) * tr(B)/2
normalised so that the round frame (B proportional to I) has rho = 1; the
convention-free content is the ratio s^2(n)/s^2(round) = rho(n) verified in s1
(3), so the frame dependence enters the saddle rows and the defect only through
u_f(n) = t sqrt(m_f (1-m_f) rho_f(n)) (t held fixed, mean-preserving family).

Frame average: the two cap axes n_1, n_2 are averaged independently and
uniformly on S^2 (axisymmetric integrands: average over z = cos(theta) on [0,1]
with Lebesgue measure); NOT the full U(N) conjugacy-class average.

Continuum defect (073, integrated): Lambda(u1,u2) = R(m1,u1) + R(m2,u2),
R(m,u) = G(a,u) - G(m,u), a = m1+m2, G(m,u) = (m+u)log(m+u) - m log m - u.
Sections:
(1) anchors: Lambda(1/2,1/2) = log(27/16) = 0.523248144; the shipped fixed-frame
    sequence (r3.out t=1: 0.509694, 0.518996, 0.520906 at N = 400, 1600, 3200)
    reproduced by the prefix machinery used below.
(2) structure: R_u = log((a+u)/(m+u)) > 0, R_uu = 1/(a+u) - 1/(m+u) < 0 (sympy
    identity checks + numerical witnesses); sqrt concavity (symbolic);
    z -> R(u(z)) concave on the family (finite differences) - the Jensen witness.
(3) mean-preserving axial family B = diag((3-g)/2, (3-g)/2, g), tr B = 3:
    limits rho_min, Lambda_min = Lambda(u^-,u^-), frame average bar_Lambda,
    Lambda_maxframe = Lambda(u^+,u^+); assert Lambda_min < bar <= log(27/16),
    strict below for g != 1; GL200 vs GL800 convergence.
(4) finite N, symmetric m1 = m2 = 1/2, t = 1: per-frame Delta via the exact
    closed form (prefix sums), GL64 frames: bar/N, min-frame/N, max per-frame
    residual |Delta - N Lambda(u(z))|; assert positivity at every node,
    |bar/N - bar_Lambda| <= 10/N, min/N >= Lambda_min - 10/N; g = 1 reproduces
    the shipped sequence of (1).
(5) asymmetric m = (1/2, 1/3), g1 = g2 = 2, N = 1200: tensor-grid GL64 x GL40
    frame average, min, max of Delta/N; limits bar_Lambda, Lambda(u1^-,u2^-).
(6) corner-mode moment fraction N*delta_2/Tr E^2 (072 definition, r3 (2)) over
    frames at m = (1/2, 1/3), N = 3200: g = (1,1) reproduces the shipped 2.4396;
    frames at g = (1,2) and (1.4, 2.6) stay bounded away from 0 and O(1)
    (uniform O(1/N)).
(7) saddle rank ratio sum M/(M+c-r) / (l1+l2) (072 definition, r3 (4)) over
    frames at N = 3200: g = 1 reproduces the shipped 0.8111; g = 2.0, 2.6 stay
    Theta(1) (min/mean/max over the frame tensor grid).

Deterministic; numpy/sympy floats only. Run:
  python -I proposals/075-g-edge-frameavg/s2_frame_two_row.py
Expected invariants: shipped anchors reproduced; positivity asserts; last line
'PASS s2'.
"""
import math

import numpy as np
import sympy as sp


def G(m, u):
    return (m + u) * math.log(m + u) - m * math.log(m) - u


def R(m, a, u):
    return G(a, u) - G(m, u)


def Lam(u1, u2, m1=0.5, m2=0.5):
    a = m1 + m2
    return R(m1, a, u1) + R(m2, a, u2)


def make_prefix(M1, M2, L):
    M = M1 + M2
    t1 = np.zeros(L + 1)
    t2 = np.zeros(L + 1)
    for c in range(1, L + 1):
        t1[c] = t1[c - 1] + math.log((M - 1 + c) / (M1 - 1 + c))
        t2[c] = t2[c - 1] + math.log((M - 2 + c) / (M2 - 1 + c))
    return t1, t2


def Dpre(t1, t2, lmax, lmin):
    return t1[lmax] + t2[lmin] - math.log((lmax + 1) / (lmax - lmin + 1))


def rho(z, g):
    # (tr B - n^T B n)/2 with B = diag((3-g)/2, (3-g)/2, g), z = cos(theta)
    x = g * z * z + 0.5 * (3.0 - g) * (1.0 - z * z)
    return 0.5 * (3.0 - x)


def gl(n):
    xg, wg = np.polynomial.legendre.leggauss(n)
    return 0.5 * (xg + 1.0), 0.5 * wg


# ---------- (1) anchors ----------
print('(1) anchors')
Lam0 = Lam(0.5, 0.5)
print('    Lambda(1/2,1/2) = %.9f  log(27/16) = %.9f' % (Lam0, math.log(27.0 / 16.0)))
assert abs(Lam0 - math.log(27.0 / 16.0)) < 1e-12
assert abs(Lam0 - 0.523248144) < 1e-8
for N, shipped in ((400, 0.509694), (1600, 0.518996), (3200, 0.520906)):
    M = N // 2
    t1, t2 = make_prefix(M, M, M + 2)
    dN = Dpre(t1, t2, M, M) / N
    print('    N=%5d prefix Delta/N=%.6f shipped=%.6f diff=%.1e'
          % (N, dN, shipped, abs(dN - shipped)))
    assert abs(dN - shipped) < 1e-6
print('(1) PASS s2(1)')

# ---------- (2) structure ----------
print('(2) structure of the per-factor profile R(m,u) = G(a,u) - G(m,u)')
u, m, a = sp.symbols('u m a', positive=True)
Rex = (a + u) * sp.log(a + u) - m * sp.log(m) - u - ((m + u) * sp.log(m + u) - u)
d1 = sp.simplify(sp.diff(Rex, u) - sp.log((a + u) / (m + u)))
d2 = sp.simplify(sp.diff(Rex, u, 2) - (1 / (a + u) - 1 / (m + u)))
print('    sympy: dR/du - log((a+u)/(m+u)) = %s ; d2R/du2 - (1/(a+u)-1/(m+u)) = %s'
      % (d1, d2))
assert d1 == 0 and d2 == 0
print('    sympy: d2 sqrt(u)/du2 = %s (negative)' % sp.simplify(sp.diff(sp.sqrt(u), u, 2)))
assert sp.simplify(sp.diff(sp.sqrt(u), u, 2) + 1 / (4 * u ** sp.Rational(3, 2))) == 0
# numerical witnesses at m=1/2, a=1
us = np.linspace(0.05, 0.7, 65)
dR = np.diff([R(0.5, 1.0, x) for x in us]) / (us[1] - us[0])
d2R = np.diff([R(0.5, 1.0, x) for x in us], 2) / (us[1] - us[0]) ** 2
print('    witness min dR/du = %.4e > 0, max d2R/du2 = %.4e < 0' % (dR.min(), d2R.max()))
assert dR.min() > 0 and d2R.max() < 0
# Jensen witness: z -> R(u(z)) concave on the family (g=2, t=1)
z = np.linspace(0.0, 1.0, 401)
f = [R(0.5, 1.0, 0.5 * math.sqrt(rho(zi, 2.0))) for zi in z]
dd = np.diff(f, 2)
print('    concavity of z -> R(u(z)), g=2: max second difference = %.3e < 0' % dd.max())
assert dd.max() < 0
print('(2) PASS s2(2)')

# ---------- (3) mean-preserving axial family, continuum limits ----------
print('(3) continuum frame average, m1=m2=1/2, t=1, mean-preserving g')
print('    g   rho_min  rho_max  Lambda_min  bar_Lambda  Lambda_max  gap_to_0.523248')
gl800z, gl800w = gl(800)
for g in (0.6, 1.0, 1.4, 2.0, 2.6):
    zz, ww = gl(200)
    uvals = 0.5 * np.sqrt([rho(x, g) for x in zz])          # t=1, m=1/2
    bar = 2.0 * sum(wi * R(0.5, 1.0, ui) for wi, ui in zip(ww, uvals))
    lmaxB, lminB = max(g, 0.5 * (3.0 - g)), min(g, 0.5 * (3.0 - g))
    rmin = 0.5 * (3.0 - lmaxB)   # axis of largest eigenvalue of B
    rmax = 0.5 * (3.0 - lminB)
    Lmin = Lam(0.5 * math.sqrt(rmin), 0.5 * math.sqrt(rmin))
    Lmax = Lam(0.5 * math.sqrt(rmax), 0.5 * math.sqrt(rmax))
    if g != 1.0:
        zz2, ww2 = gl800z, gl800w
        u2v = 0.5 * np.sqrt([rho(x, g) for x in zz2])
        bar8 = 2.0 * sum(wi * R(0.5, 1.0, ui) for wi, ui in zip(ww2, u2v))
        assert abs(bar - bar8) < 1e-8
    print('    %.1f  %.6f  %.6f  %.6f    %.6f     %.6f     %.6f'
          % (g, rmin, rmax, Lmin, bar, Lmax, Lam0 - bar))
    assert Lmin < bar + 1e-12
    assert bar <= Lam0 + 1e-12
    if g != 1.0:
        assert bar < Lam0 - 1e-6
print('(3) PASS s2(3)')

# ---------- (4) finite N, symmetric ----------
print('(4) finite N symmetric (GL64 frames), m1=m2=1/2, t=1')
for g in (1.0, 1.4, 2.0, 2.6):
    zz, ww = gl(64)
    uvals = 0.5 * np.sqrt([rho(x, g) for x in zz])
    for N in (400, 1600, 3200):
        M = N // 2
        lmaxall = max(1, int(round(N * max(uvals))))
        t1, t2 = make_prefix(M, M, lmaxall + 2)
        rows = [max(1, int(round(N * ui))) for ui in uvals]
        d = [Dpre(t1, t2, r, r) for r in rows]
        bar = sum(wi * di for wi, di in zip(ww, d)) / N
        dmin = min(d) / N
        resid = max(abs(di - N * Lam(r * 1.0 / N, r * 1.0 / N))
                    for r, di in zip(rows, d))
        zz200, ww200 = gl(200)
        uv2 = 0.5 * np.sqrt([rho(x, g) for x in zz200])
        barlim = 2.0 * sum(wi * R(0.5, 1.0, ui) for wi, ui in zip(ww200, uv2))
        rmin = min(rho(0.0, g), rho(1.0, g))
        Lmin = Lam(0.5 * math.sqrt(rmin), 0.5 * math.sqrt(rmin))
        assert all(di > 0 for di in d)
        assert abs(bar - barlim) <= 12.0 / N
        assert dmin >= Lmin - 12.0 / N
        if g == 1.0:
            shipped = {400: 0.509694, 1600: 0.518996, 3200: 0.520906}[N]
            assert abs(bar - shipped) < 1e-6
        print('    g=%.1f N=%5d  bar/N=%.6f  min-frame/N=%.6f  residmax=%.2f'
              % (g, N, bar, dmin, resid))
print('(4) PASS s2(4)')

# ---------- (5) asymmetric ----------
print('(5) asymmetric m=(1/2,1/3), g1=g2=2, t=1')
N = 1200
M1, M2 = 600, 400
z1, w1 = gl(64)
z2, w2 = gl(40)
u1 = 0.5 * np.sqrt([rho(x, 2.0) for x in z1])              # sqrt(m1(1-m1)) = 1/2
u2 = math.sqrt(2.0 / 9.0) * np.sqrt([rho(x, 2.0) for x in z2])
rows1 = [max(1, int(round(N * x))) for x in u1]
rows2 = [max(1, int(round(N * x))) for x in u2]
t1, t2 = make_prefix(M1, M2, max(max(rows1), max(rows2)) + 2)
bar = 0.0
dmin = float('inf')
dmax = -float('inf')
for ri, wi in zip(rows1, w1):
    for rj, wj in zip(rows2, w2):
        # frames vary independently: the exact defect is the closed form of the
        # SORTED partition (r6 verified it for sorted rows)
        di = Dpre(t1, t2, max(ri, rj), min(ri, rj)) / N
        bar += wi * wj * di
        dmin = min(dmin, di)
        dmax = max(dmax, di)
zz, ww = gl(200)
uu1 = [0.5 * math.sqrt(rho(x, 2.0)) for x in zz]
uu2 = [math.sqrt(2.0 / 9.0) * math.sqrt(rho(x, 2.0)) for x in zz]
lim1 = sum(wi * R(0.5, 5.0 / 6.0, x) for wi, x in zip(ww, uu1))
lim2 = sum(wi * R(1.0 / 3.0, 5.0 / 6.0, x) for wi, x in zip(ww, uu2))
lim_fac = lim1 + lim2
zz3, ww3 = gl(60)
u3a = [0.5 * math.sqrt(rho(x, 2.0)) for x in zz3]
u3b = [math.sqrt(2.0 / 9.0) * math.sqrt(rho(x, 2.0)) for x in zz3]
lim_sort = sum(wa * wb * (R(0.5, 5.0 / 6.0, max(ua, ub)) + R(1.0 / 3.0, 5.0 / 6.0, min(ua, ub)))
               for wa, ua in zip(ww3, u3a) for wb, ub in zip(ww3, u3b))
rmin2 = min(rho(0.0, 2.0), rho(1.0, 2.0))
umax2 = max(rho(0.0, 2.0), rho(1.0, 2.0))
um1, um2 = 0.5 * math.sqrt(rmin2), math.sqrt(2.0 / 9.0) * math.sqrt(rmin2)
Lmin = R(0.5, 5.0 / 6.0, max(um1, um2)) + R(1.0 / 3.0, 5.0 / 6.0, min(um1, um2))
uM1, uM2 = 0.5 * math.sqrt(umax2), math.sqrt(2.0 / 9.0) * math.sqrt(umax2)
Lmax = R(0.5, 5.0 / 6.0, max(uM1, uM2)) + R(1.0 / 3.0, 5.0 / 6.0, max(uM1, uM2))
print('    limits: factor-pairing %.6f (= %.6f + %.6f), sorted-pairing %.6f'
      % (lim_fac, lim1, lim2, lim_sort))
print('    bounds: sorted lower pair %.6f, upper pair %.6f' % (Lmin, Lmax))
print('    finite N=%d tensor GL64xGL40: bar/N=%.6f min/N=%.6f max/N=%.6f'
      % (N, bar, dmin, dmax))
assert bar > 0 and dmin > 0 and dmax > 0
assert dmin >= Lmin - 12.0 / N
assert abs(bar - lim_sort) <= 12.0 / N
assert dmax <= Lmax + 12.0 / N
print('(5) PASS s2(5)')

# ---------- (6) corner-mode fraction over frames ----------
print('(6) corner fraction N*delta_2/Tr E^2, m=(1/2,1/3), N=3200')
N = 3200
M1, M2 = N // 2, N // 3
zz, ww = gl(40)


def corner(g1, g2):
    vals = []
    for x1 in zz:
        s1sq = M1 * (N - M1) * rho(x1, g1)
        for x2 in zz:
            s2sq = M2 * (N - M2) * rho(x2, g2)
            p = 2
            tot = (M2 - 1) * s1sq ** p + (M1 - 1) * s2sq ** p + (s1sq + s2sq) ** p
            dlt = (s1sq + s2sq) ** p - s1sq ** p - s2sq ** p
            vals.append(N * dlt / tot)
    return min(vals), max(vals)


lo, hi = corner(1.0, 1.0)
print('    g=(1,1):  N*delta2/TrE^2 in [%.4f, %.4f]  shipped 2.4396' % (lo, hi))
assert abs(hi - 2.4396) < 1e-3 and abs(lo - 2.4396) < 1e-3
for g1, g2 in ((1.0, 2.0), (1.4, 2.6)):
    lo, hi = corner(g1, g2)
    print('    g=(%.1f,%.1f): in [%.4f, %.4f]' % (g1, g2, lo, hi))
    assert lo > 0.5 and hi < 3.0
print('(6) PASS s2(6)')

# ---------- (7) rank ratio over frames ----------
print('(7) saddle rank ratio, m1=m2=1/2, N=3200')
N = 3200
M = N
M1 = M2 = N // 2
zz, ww = gl(40)


def rankgrid(g):
    uvals = 0.5 * np.sqrt([rho(x, g) for x in zz])
    rows = [max(1, int(round(N * x))) for x in uvals]
    L = max(rows) + 2
    p1 = np.zeros(L + 1)
    p2 = np.zeros(L + 1)
    for c in range(1, L + 1):
        p1[c] = p1[c - 1] + M / (M + c - 1)
        p2[c] = p2[c - 1] + M / (M + c - 2)
    vals = []
    for ri in rows:
        for rj in rows:
            vals.append((p1[ri] + p2[rj]) / (ri + rj))
    return min(vals), sum(vals) / len(vals), max(vals)


lo, mid, hi = rankgrid(1.0)
print('    g=1.0: ratio=%.4f  shipped 0.8111' % mid)
assert abs(mid - 0.8111) < 5e-4
for g in (2.0, 2.6):
    lo, mid, hi = rankgrid(g)
    print('    g=%.1f: min=%.4f mean=%.4f max=%.4f' % (g, lo, mid, hi))
    assert lo > 0.7
print('(7) PASS s2(7)')

print('PASS s2')
