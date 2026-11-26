"""079 s2 (r1): frame scan for the frame-uniform residual bound.

For the exact stacked defect functional (the closed form of the integrated
Problem G block) and the frame-free bound B_q of the proposal, this script
(1) scans random positive-definite Gram frames B (tr B = 3) with saddle-class
rows l_f = round(t*s_f(B)), t the saddle parameter, and verifies
|Delta_q - T_q| <= B_q with the SAME bound formula for every frame;
(2) records that the bound evaluated at fixed rows is literally frame-
independent (one distinct value over all frames);
(3) sweeps t at fixed N to show the growth of residual and bound;
(4) compares the bound at the shipped scale N=3200 against the integrated
numerical residuals 7.7 (two-row) and 59.8 (depth three) recorded in
appH-microscopic-proofs.tex L3165 (quoted; the bound dominates them).

s_f = (1/2) sqrt(M_f(N-M_f)(tr B - n^T B n)) is the edge-datum norm of the
integrated edge-datum paragraph (its s^2 = (1/4)M(N-M)(sigma_1^2+sigma_2^2),
trace-3 normalisation).

Deterministic: rng.seed(79), printed. Defect values are float logs of the exact
product functional; the inequality margin is never of float-error order.

Run:  python -I proposals/079-g-frameavg-residual/s2_frame_uniform_check.py
Expected final line: PASS s2
"""
import math
import random

def Iint(A, B, ell):
    if ell == 0:
        return 0.0
    return ((A + ell) * math.log(A + ell) - A * math.log(A)
            - (B + ell) * math.log(B + ell) + B * math.log(B))

def delta_log(M, M1, M2, q1, q2, l1, l2):
    s = 0.0
    for r in range(1, q1 + 1):
        for c in range(1, l1 + 1):
            s += math.log((M + c - r) / (M1 + c - r))
    for r in range(1, q2 + 1):
        for c in range(1, l2 + 1):
            s += math.log((M - q1 + c - r) / (M2 + c - r))
    for r in range(1, q1 + 1):
        for c in range(1, l2 + 1):
            s += math.log((l1 - c + q1 - r + 1) / (l1 - c + q1 + q2 - r + 1))
    return s

def chain_bound(M1, M2, q1, q2, l1, l2):
    M = M1 + M2
    b = 0.0
    for r in range(1, q1 + 1):
        b += abs(math.log((M - r + 1) / (M1 - r + 1)))
        b += l1 * ((r - 1) / (M - r + 1) + (r - 1) / (M1 - r + 1))
    for r in range(1, q2 + 1):
        b += abs(math.log((M - q1 - r + 1) / (M2 - r + 1)))
        b += l2 * ((q1 + r - 1) / (M - q1 - r + 1) + (r - 1) / (M2 - r + 1))
    b += q1 * q2 * math.log(l1 + q1 + q2)
    return b

def nBn(n, B):
    return sum(n[i] * B[i][j] * n[j] for i in range(3) for j in range(3))

def s_edge(B, n, Mf, N):
    """edge-datum norm s = sqrt( (1/4) M(N-M) (tr B - n^T B n) ), tr B = 3."""
    return 0.5 * math.sqrt(Mf * (N - Mf) * (3.0 - nBn(n, B)))

rng = random.Random(79)
print('rng.seed(79)')

def rand_B():
    X = [[rng.gauss(0, 1) for _ in range(3)] for _ in range(3)]
    B = [[sum(X[i][k] * X[j][k] for k in range(3)) for j in range(3)] for i in range(3)]
    tr = B[0][0] + B[1][1] + B[2][2]
    return [[v * 3.0 / tr for v in row] for row in B]

frames = [[[1.0, 0, 0], [0, 1.0, 0], [0, 0, 1.0]]]
for _ in range(149):
    frames.append(rand_B())

n1 = (1.0, 0.0, 0.0)
n2 = (0.0, 1.0, 0.0)

def rows_for(B, t, M1, M2, N):
    la = int(round(t * s_edge(B, n1, M1, N)))
    lb = int(round(t * s_edge(B, n2, M2, N)))
    return max(1, max(la, lb)), max(0, min(la, lb))

print('scan 1: symmetric ranks m_f=1/2, N in {400,1600,3200}, t=1, q=(1,1) and (3,3)')
for N in (400, 1600, 3200):
    M = 2 * (N // 2)
    M1 = M2 = N // 2
    for (q1, q2) in ((1, 1), (3, 3)):
        worst_res = 0.0
        minb = None
        maxb = 0.0
        fails = 0
        for B in frames:
            l1, l2 = rows_for(B, 1.0, M1, M2, N)
            dlt = delta_log(M, M1, M2, q1, q2, l1, l2)
            T = q1 * Iint(M, M1, l1) + q2 * Iint(M, M2, l2)
            bnd = chain_bound(M1, M2, q1, q2, l1, l2)
            res = abs(dlt - T)
            worst_res = max(worst_res, res)
            maxb = max(maxb, bnd)
            minb = bnd if minb is None else min(minb, bnd)
            if res > bnd + 1e-9:
                fails += 1
                print('FAIL scan1', N, q1, q2, res, bnd)
        print('  N=%4d q=(%d,%d): frames=150 fails=%d  worst residual=%9.3f  bound in [%.3f, %.3f]'
              % (N, q1, q2, fails, worst_res, minb, maxb))
        assert fails == 0

print('scan 2: bound at fixed rows is frame-independent (rows from identity frame)')
N = 1600
M1 = M2 = 800
l1, l2 = rows_for(frames[0], 1.0, M1, M2, N)
vals = set()
for B in frames:
    vals.add(round(chain_bound(M1, M2, 3, 3, l1, l2), 12))
print('  rows=(%d,%d)  distinct depth-3 bound values over 150 frames: %d (expected 1)'
      % (l1, l2, len(vals)))
assert len(vals) == 1

print('scan 3: t sweep at N=3200, symmetric ranks, q=(1,1): growth of residual and bound')
N = 3200
M1 = M2 = 1600
for t in (0.25, 0.5, 1.0, 2.0):
    worst_res = 0.0
    maxb = 0.0
    for B in frames[:50]:
        l1, l2 = rows_for(B, t, M1, M2, N)
        dlt = delta_log(3200, M1, M2, 1, 1, l1, l2)
        T = Iint(3200, M1, l1) + Iint(3200, M2, l2)
        bnd = chain_bound(M1, M2, 1, 1, l1, l2)
        res = abs(dlt - T)
        if res > bnd + 1e-9:
            print('FAIL scan3', t, res, bnd); raise AssertionError
        worst_res = max(worst_res, res)
        maxb = max(maxb, bnd)
    print('  t=%5.2f: worst residual=%9.3f  max bound=%9.3f' % (t, worst_res, maxb))

print('check: bound vs integrated residuals (appH L3165: 7.7 two-row, 59.8 depth 3, N up to 3200)')
l1, l2 = rows_for(frames[0], 1.0, 1600, 1600, 3200)
b1 = chain_bound(1600, 1600, 1, 1, l1, l2)
b3 = chain_bound(1600, 1600, 3, 3, l1, l2)
res1 = abs(delta_log(3200, 1600, 1600, 1, 1, l1, l2) - Iint(3200, 1600, l1) - Iint(3200, 1600, l2))
print('  N=3200 round frame t=1: rows=(%d,%d)  two-row bound=%.3f (vs shipped 7.7)  depth-3 bound=%.3f (vs shipped 59.8)  this-scan two-row residual=%.3f'
      % (l1, l2, b1, b3, res1))
assert b1 > 7.7 and b3 > 59.8

print('PASS s2')
