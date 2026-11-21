"""075 s3: frame average of the stacked-row (depth q) saddle excess.

Class: as in s2 (072 (H1)-(H4) product testbed + cap frames) with the 074
stacked-row diagrams (l1^q, l2^q), equal depths q fixed as N -> infinity, on the
mean-preserving axial family B = diag((3-g)/2, (3-g)/2, g).

Continuum limit (074, integrated): Delta_q/N -> q * Lambda(u1,u2),
Lambda = R(m1,.,u1) + R(m2,.,u2), so the frame average of the stacked excess is
q times the frame-averaged two-row profile of s2.

Exact finite-N form (074 closed form, verified there against Weyl dimension):
Delta_q = sum_{r=1..q} sum_{c=1..l1} log((M+c-r)/(M1+c-r))
        + sum_{r=1..q} sum_{c=1..l2} log((M-q+c-r)/(M2+c-r))
        - sum_{r=1..q} sum_{c=1..l2} log((l1-c+2q-r+1)/(l1-c+q-r+1)),
evaluated here with prefix sums at equal rows l1 = l2 = l (symmetric family).

Sections:
(1) anchors: g = 1 (round frame), N = 3200, q = 1, 2, 3 reproduces the shipped
    074 sequence 0.520906 / 1.037902 / 1.551490 (r7.out).
(2) continuum frame averages q * bar_Lambda(g) and lower bounds q * Lambda_min,
    g in {1.0, 1.6, 2.2}: assert q*Lambda_min < q*bar <= q*0.523248144.
(3) finite N (GL64 frames): g in {1.0, 1.6, 2.2}, q in {1,2,3},
    N in {1600, 3200}: bar/N, min-frame/N, max per-frame residual
    |Delta_q - N*q*Lambda(u(z))|; assert positivity at every node,
    |bar/N - q*bar_Lambda| <= 20*q/N, min/N >= q*Lambda_min - 20*q/N.

Deterministic. Run:
  python -I proposals/075-g-edge-frameavg/s3_frame_stacked.py
Expected invariants: shipped 074 anchors reproduced; positivity asserts; last
line 'PASS s3'.
"""
import math

import numpy as np


def G(m, u):
    return (m + u) * math.log(m + u) - m * math.log(m) - u


def R(m, a, u):
    return G(a, u) - G(m, u)


def Lam(u1, u2, m1=0.5, m2=0.5):
    a = m1 + m2
    return R(m1, a, u1) + R(m2, a, u2)


def rho(z, g):
    x = g * z * z + 0.5 * (3.0 - g) * (1.0 - z * z)
    return 0.5 * (3.0 - x)


def gl(n):
    xg, wg = np.polynomial.legendre.leggauss(n)
    return 0.5 * (xg + 1.0), 0.5 * wg


def make_stacked(M1, M2, q, L):
    M = M1 + M2
    A1 = [np.zeros(L + 1) for _ in range(q + 1)]
    A2 = [np.zeros(L + 1) for _ in range(q + 1)]
    H = [np.zeros(L + 1) for _ in range(q + 1)]
    for r in range(1, q + 1):
        for c in range(1, L + 1):
            A1[r][c] = A1[r][c - 1] + math.log((M + c - r) / (M1 + c - r))
        for c in range(1, L + 1):
            A2[r][c] = A2[r][c - 1] + math.log((M - q + c - r) / (M2 + c - r))
        for x in range(0, L):
            H[r][x + 1] = H[r][x] + math.log((x + 2 * q - r + 1) / (x + q - r + 1))
    return A1, A2, H


def Dstack(A1, A2, H, l):
    q = len(A1) - 1
    return sum(A1[r][l] + A2[r][l] - H[r][l] for r in range(1, q + 1))


# ---------- (1) anchors: g = 1 reproduces the shipped 074 sequence ----------
print('(1) anchors: round frame g=1, N=3200')
Lam0 = Lam(0.5, 0.5)
assert abs(Lam0 - 0.523248144) < 1e-8
N = 3200
M1 = M2 = N // 2
shipped = {1: 0.520906, 2: 1.037902, 3: 1.551490}
for q in (1, 2, 3):
    A1, A2, H = make_stacked(M1, M2, q, N // 2 + 2)
    dN = Dstack(A1, A2, H, N // 2) / N
    print('    q=%d Delta_q/N=%.6f shipped=%.6f diff=%.1e' % (q, dN, shipped[q],
                                                               abs(dN - shipped[q])))
    assert abs(dN - shipped[q]) < 5e-7
print('(1) PASS s3(1)')

# ---------- (2) continuum frame averages ----------
print('(2) continuum: q*bar_Lambda and q*Lambda_min, m1=m2=1/2, t=1')
zz, ww = gl(200)
for g in (1.0, 1.6, 2.2):
    uv = 0.5 * np.sqrt([rho(x, g) for x in zz])
    bar = 2.0 * sum(wi * R(0.5, 1.0, ui) for wi, ui in zip(ww, uv))
    rmin = min(rho(0.0, g), rho(1.0, g))
    Lmin = Lam(0.5 * math.sqrt(rmin), 0.5 * math.sqrt(rmin))
    print('    g=%.1f  bar_Lambda=%.6f  Lambda_min=%.6f' % (g, bar, Lmin))
    assert Lmin < bar + 1e-12
    assert bar <= Lam0 + 1e-12
    if g != 1.0:
        assert bar < Lam0 - 1e-6
    for q in (2, 3):
        assert Lmin * q < bar * q <= q * Lam0 + 1e-12
print('(2) PASS s3(2)')

# ---------- (3) finite N ----------
print('(3) finite N stacked (GL64 frames), m1=m2=1/2, t=1')
for g in (1.0, 1.6, 2.2):
    zz64, ww64 = gl(64)
    uv = 0.5 * np.sqrt([rho(x, g) for x in zz64])
    zz2, ww2 = gl(200)
    uv2 = 0.5 * np.sqrt([rho(x, g) for x in zz2])
    barlim = 2.0 * sum(wi * R(0.5, 1.0, ui) for wi, ui in zip(ww2, uv2))
    rmin = min(rho(0.0, g), rho(1.0, g))
    Lmin = Lam(0.5 * math.sqrt(rmin), 0.5 * math.sqrt(rmin))
    for N in (1600, 3200):
        rowsN = [max(1, int(round(N * ui))) for ui in uv]
        lmax = max(rowsN) + 2
        for q in (1, 2, 3):
            A1, A2, H = make_stacked(N // 2, N // 2, q, lmax)
            d = [Dstack(A1, A2, H, l) for l in rowsN]
            bar = sum(wi * di for wi, di in zip(ww64, d)) / N
            dmin = min(d) / N
            resid = max(abs(di - N * q * Lam(l * 1.0 / N, l * 1.0 / N))
                        for l, di in zip(rowsN, d))
            assert all(di > 0 for di in d)
            assert abs(bar - q * barlim) <= 20.0 * q / N
            assert dmin >= q * Lmin - 20.0 * q / N
            print('    g=%.1f N=%5d q=%d  bar/N=%.6f  min-frame/N=%.6f  residmax=%.2f'
                  % (g, N, q, bar, dmin, resid))
print('(3) PASS s3(3)')

print('PASS s3')
