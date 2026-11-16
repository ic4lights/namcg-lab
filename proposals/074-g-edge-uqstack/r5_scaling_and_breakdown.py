"""073 s5: uniform scaling of the two-row defect under row perturbations.

Reuses the 072 Lemma-2 closed form (prefix sums). Classes: M_f = m_f N,
saddle rows l_i = t*s_i, s_f = sqrt(k_f M_f (N-M_f)) (k = 1); perturbed
diagrams l' with |l_i' - l_i| <= C.

Limit profile (derived in the proposal): with u_i = l_i/N,
    Delta(N u1, N u2)/N -> Lambda(u1,u2)
      = R(m1,u1) + R(m2,u2),  R(m,u) = G(m1+m2,u) - G(m,u),
      G(a,u) = (a+u)log(a+u) - a log a - u,
uniformly (error O(log N)); Lambda > 0 iff (u1,u2) != (0,0), strictly
increasing in each argument. Consequences checked here:
(1) uniform error bound |Delta - N*Lambda| <= 2 K1' + 2 K2' + log(l1+1) + 2
    (K1' = log(M/(M1-1)), K2' = log((M-1)/(M2-1))) on random diagrams, N up
    to 3200;
(2) bounded-class uniform lower bound: min of Delta over the box
    max(l_i - C, 0) <= l_i' <= l_i + C (valid partitions), C in {1,10,100},
    N up to 3200: min/N -> Lambda(u1,u2); the deficit N*(Lambda - min/N)
    grows linearly in C with slope ~ dLambda/du1 + dLambda/du2; the bound
    min >= Delta(l) - C(K1+K2+1) - log(2C+1) holds with slack;
(3) o(N)-perturbation class C = round(sqrt(N)): min/N still -> Lambda;
(4) linear breakdown: C = c*N, c up to 0.5 (symmetric saddle, t=1):
    min/N tracks Lambda(0.5-c, 0.5-c) and hits the trivial diagram exactly
    at c = 0.5 (min = 0 there; exact box minima vs corner at N <= 800);
    asymmetric fractions: killing only row 2 leaves Lambda(u1, 0) > 0;
(5) sharp trade: worst-case loss for a budget removed from one row is the
    row paired with the larger other-factor rank (check at (1/2,1/3));
(6) rank ratio rho = (sum_{(r,c)} M/(M+c-r))/|mu| off the saddle: 0.8111
    is a saddle-fraction value; rho stays bounded in (0,1) and rho -> 1 as
    u -> 0, so the Theta(|mu|) rank dependence is fraction-uniform but the
    constant 0.8111 is not.

Run: python -I proposals/073-g-edge-rowshift/s5_scaling_and_breakdown.py
Expected invariants: max residual in (1) < the stated bound; min/N in (2)-(3)
-> Lambda with the linear-C deficit; min = 0 at c = 0.5 in (4); rho table in
(6); 'PASS s5'.
"""
import math

import numpy as np


def prefix(M1, M2, lmax):
    M = M1 + M2
    p1 = [0.0] * (lmax + 1)
    p2 = [0.0] * (lmax + 1)
    for c in range(1, lmax + 1):
        p1[c] = p1[c - 1] + math.log((M - 1 + c) / (M1 - 1 + c))
        p2[c] = p2[c - 1] + math.log((M - 2 + c) / (M2 - 1 + c))
    return p1, p2


def DeltaP(p1, p2, l1, l2):
    return p1[l1] + p2[l2] - math.log((l1 + 1) / (l1 - l2 + 1))


def Delta(M1, M2, l1, l2):
    p1, p2 = prefix(M1, M2, max(l1, l2))
    return DeltaP(p1, p2, l1, l2)


def G(a, u):
    return (a + u) * math.log(a + u) - a * math.log(a) - u


def Lam(m1, m2, u1, u2):
    a = m1 + m2
    return G(a, u1) - G(m1, u1) + G(a, u2) - G(m2, u2)


def dLam(m1, m2, ui, which):
    mo = m2 if which == 1 else m1
    return math.log((m1 + m2 + ui) / ((m1 if which == 1 else m2) + ui))


def boxmin(p1, p2, l1, l2, C):
    best = (float('inf'), None)
    for l1p in range(max(0, l1 - C), l1 + C + 1):
        lo = max(0, l2 - C)
        for l2p in range(lo, min(l1p, l2 + C) + 1):
            d = DeltaP(p1, p2, l1p, l2p)
            if d < best[0]:
                best = (d, (l1p, l2p))
    return best


# ---------- (1) uniform error bound against N*Lambda ----------
print('(1) uniform error bound, random diagrams, k=1:')
worst = (-float('inf'), None)
rng = np.random.default_rng(73005)
for (m1, m2) in ((0.5, 0.5), (0.5, 1 / 3), (0.5, 1 / 6)):
    for N in (400, 1600, 3200):
        M1 = int(round(m1 * N))
        M2 = int(round(m2 * N))
        M = M1 + M2
        K1p = math.log(M / (M1 - 1))
        K2p = math.log((M - 1) / (M2 - 1))
        for trial in range(25):
            u1 = rng.uniform(0.02, 0.7)
            u2 = rng.uniform(0.0, u1)
            l1 = max(1, int(round(u1 * N)))
            l2 = int(round(u2 * N))
            l2 = min(l2, l1)
            e = abs(Delta(M1, M2, l1, l2) - N * Lam(m1, m2, l1 / N, l2 / N))
            eb = 2 * K1p + 2 * K2p + math.log(l1 + 1) + 2
            if e - eb > worst[0]:
                worst = (e - eb, (m1, m2, N, l1, l2, e, eb))
print('    worst (residual - bound): %.3e at %s' % (worst[0], worst[1]))
assert worst[0] < 0
print('    bound holds on all cases')

# ---------- (2) bounded-class uniform lower bound ----------
print('(2) box minima at the saddle, k=1 (min/N -> Lambda):')
for (m1, m2, t) in ((0.5, 0.5, 1.0), (0.5, 1 / 3, 1.0), (0.5, 0.5, 0.5)):
    for N in (400, 1600, 3200):
        M1 = int(round(m1 * N))
        M2 = int(round(m2 * N))
        M = M1 + M2
        s1 = math.sqrt(M1 * (N - M1))
        s2 = math.sqrt(M2 * (N - M2))
        l1 = int(round(t * max(s1, s2)))
        l2 = int(round(t * min(s1, s2)))
        p1, p2 = prefix(M1, M2, l1 + 100)
        d0 = DeltaP(p1, p2, l1, l2)
        L = Lam(m1, m2, l1 / N, l2 / N)
        row = '    m=(%.3f,%.3f) t=%.1f N=%4d:' % (m1, m2, t, N)
        K1 = math.log(1 + M2 / M1)
        K2 = math.log(1 + (M1 - 1) / M2)
        K1p = math.log(M / (M1 - 1))
        K2p = math.log((M - 1) / (M2 - 1))
        for C in (1, 10, 100):
            ebound = 2 * K1p + 2 * K2p + math.log(l1 + C + 2) + 2
            dm, arg = boxmin(p1, p2, l1, l2, C)
            bnd = d0 - C * (K1 + K2 + 1) - math.log(2 * C + 1)
            assert dm >= bnd                       # uniform Lipschitz bound
            cc = DeltaP(p1, p2, max(l1 - C, 0), max(l2 - C, 0))
            assert dm <= cc + 1e-9                 # corner is in the box
            lam_c = Lam(m1, m2, max(l1 - C, 0) / N, max(l2 - C, 0) / N)
            assert dm >= N * lam_c - 2 * ebound    # min >= corner Lambda - err
            row += '  C=%3d min/N=%.6f (L=%.6f, N(L-min)=%8.2f pred1st=%6.2f)' % (
                C, dm / N, L, N * (L - dm / N),
                C * (dLam(m1, m2, l1 / N, 1) + dLam(m1, m2, l2 / N, 2)))
            if C == 10 and N == 3200:
                # finite-N Delta/N approaches Lambda with a constant O(log N)/N
                # offset (072 gatekeeper note); test the C-derivative (slope),
                # which is free of that offset
                slope = (d0 - dm) / (C * N)
                sl_pred = (dLam(m1, m2, l1 / N, 1)
                           + dLam(m1, m2, l2 / N, 2)) / N
                assert abs(slope - sl_pred) < 0.05 * sl_pred
        print(row)
        if m1 == 0.5 and m2 == 0.5 and N == 3200:
            print('      argmin at C=100: %s, corner=(%d,%d)'
                  % (arg, l1 - 100, l2 - 100))

# ---------- (3) o(N)-perturbation class ----------
print('(3) C = round(sqrt(N)), symmetric t=1:')
for N in (400, 1600, 3200):
    M1 = M2 = N // 2
    l = int(round(0.5 * N))
    p1, p2 = prefix(M1, M2, l + 100)
    C = int(round(math.sqrt(N)))
    dm, arg = boxmin(p1, p2, l, l, C)
    print('    N=%4d C=%3d  min/N=%.6f  Lambda=%.6f' % (N, C, dm / N,
                                                        Lam(.5, .5, .5, .5)))

# ---------- (4) linear breakdown ----------
print('(4) linear perturbation C = c*N, symmetric saddle t=1:')
for c in (0.1, 0.3, 0.45):
    for N in (400, 1600):
        M1 = M2 = N // 2
        l = int(round(0.5 * N))
        C = int(round(c * N))
        p1, p2 = prefix(M1, M2, l + C + 2)
        if N <= 400:
            dm, arg = boxmin(p1, p2, l, l, C)
            print('    c=%.2f N=%4d exact box min/N=%.6f  corner/N=%.6f '
                  'Lambda(0.5-c)=%.6f  argmin=%s'
                  % (c, N, dm / N,
                     DeltaP(p1, p2, max(l - C, 0), max(l - C, 0)) / N,
                     Lam(.5, .5, max(.5 - c, 0), max(.5 - c, 0)), arg))
        else:
            cc = DeltaP(p1, p2, max(l - C, 1), max(l - C, 0)) / N
            print('    c=%.2f N=%4d corner/N=%.6f  Lambda(0.5-c)=%.6f'
                  % (c, N, cc, Lam(.5, .5, max(.5 - c, 0), max(.5 - c, 0))))
for N in (400, 1600):
    M1 = M2 = N // 2
    l = N // 2
    p1, p2 = prefix(M1, M2, 2 * l + 2)
    dm, arg = boxmin(p1, p2, l, l, l)  # C = l = 0.5*N: full collapse
    print('    c=0.50 N=%4d exact box min = %.1e at %s (trivial diagram)'
          % (N, dm, arg))
    assert dm < 1e-12
print('    asymmetric, N=1600, m=(0.5,1/3), t=1: kill row 2 only (C2 = l2):')
N = 1600
M1 = N // 2
M2 = N // 3
s1 = math.sqrt(M1 * (N - M1))
s2 = math.sqrt(M2 * (N - M2))
l1, l2 = int(round(max(s1, s2))), int(round(min(s1, s2)))
p1, p2 = prefix(M1, M2, l1 + 10)
d_row2gone = DeltaP(p1, p2, l1, 0) / N
print('    Delta(l1,0)/N = %.6f  Lambda(u1,0) = %.6f  (both > 0)'
      % (d_row2gone, Lam(0.5, 1 / 3, l1 / N, 0.0)))
assert abs(d_row2gone - Lam(0.5, 1 / 3, l1 / N, 0.0)) * N < 5.0

# ---------- (5) sharp trade ----------
print('(5) worst one-row removal of budget B vs half-half, m=(0.5,1/3), '
      'N=1600 (B < row gap %d, so row order is preserved):' % (l1 - l2))
B = 40
d0 = DeltaP(p1, p2, l1, l2)
lR1 = d0 - DeltaP(p1, p2, l1 - B, l2)
lR2 = d0 - DeltaP(p1, p2, l1, l2 - B)
lHH = d0 - DeltaP(p1, p2, l1 - B // 2, l2 - B // 2)
print('    loss(row1)=%.4f  loss(row2)=%.4f  loss(half-half)=%.4f' % (lR1, lR2, lHH))
print('    predictions B*dLambda/du: row1=%.4f row2=%.4f'
      % (B * dLam(0.5, 1 / 3, l1 / N, 1), B * dLam(0.5, 1 / 3, l2 / N, 2)))
assert lR2 > lR1

# ---------- (6) rank ratio off the saddle ----------
print('(6) rho = (sum M/(M+c-r))/|mu| at N=3200, block rank M=N:')


def rho(M, l1v, l2v):
    ssum = sum(M / (M + c - r) for r, L in ((1, l1v), (2, l2v))
               for c in range(1, L + 1))
    return ssum / (l1v + l2v)


cases = [('saddle t=1', 1600, 1600), ('saddle C=+100', 1700, 1600),
         ('saddle C=-100', 1500, 1500), ('u=(0.4,0.4)', 1280, 1280),
         ('u=(0.5,0)', 1600, 0), ('u=(0.2,0.05)', 640, 160),
         ('u=(0.8,0.8)', 2560, 2560)]
MM = 3200
for name, a, b in cases:
    print('    %-16s rows=(%4d,%4d) rho=%.4f' % (name, a, b, rho(MM, a, b)))

print('PASS s5')
