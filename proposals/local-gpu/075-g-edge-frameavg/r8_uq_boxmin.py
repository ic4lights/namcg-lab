"""074 s3: uniform residual bound, box minima and breakdown for the U(q)-stack class.

Uses the closed form of s1 (validated there in exact rational arithmetic), evaluated via
prefix arrays so box minima over large boxes are cheap:

Delta(l1,l2) = sum_r A_r(l1) + sum_r B_r(l2) - sum_r [F_r(l1) - F_r(l1-l2)],
  A_r(l1) = sum_{c<=l1} log((M+c-r)/(M1+c-r)),            r = 1..q1
  B_r(l2) = sum_{c<=l2} log((M-q1+c-r)/(M2+c-r)),         r = 1..q2
  F_r(j)  = sum_{x<=j} log((x+q1+q2-r+1)/(x+q1-r+1)),     r = 1..q1  (hook correction,
            column height of the union diagram exceeds that of (l1^q1) by q2 for c <= l2)

Section 1: uniform residual bound |Delta - N*(q1*g1+q2*g2)| <= B on random stacks
           (g_f = G(m1+m2,u_f)-G(m_f,u_f), B as printed; worst slack reported).
Section 2: exhaustive box minima at the symmetric saddle N=400, q in {1,2,3}, bounded C:
           min > 0, Theta(N), attained at the far corner, converging up to q*Lambda.
Section 3: linear breakdown C = cN at the symmetric saddle: min > 0 for c < 1/2 and the
           minimum vanishes exactly at C = l1 = N/2, where the trivial stacked diagram
           (all rows zero) enters the box (exhaustive at N=400).
Deterministic (fixed seed).
"""
import math
import random


def G(m, u):
    return (m + u) * math.log(m + u) - m * math.log(m) - u


def make_delta(M1, M2, q1, q2, lmax):
    M = M1 + M2
    A = [[0.0] * (lmax + 1) for _ in range(q1)]
    B = [[0.0] * (lmax + 1) for _ in range(q2)]
    F = [[0.0] * (lmax + 2) for _ in range(q1)]
    for r in range(1, q1 + 1):
        acc = 0.0
        for c in range(1, lmax + 1):
            acc += math.log((M + c - r) / (M1 + c - r))
            A[r - 1][c] = acc
        acc = 0.0
        # F[r-1][j+1] = sum_{x=1}^{j} log((x+q1+q2-r+1)/(x+q1-r+1)); hook sum over
        # c=1..l2 has x=l1-c in [l1-l2, l1-1], i.e. F[l1] - F[l1-l2] in shifted indexing
        for j in range(0, lmax + 1):
            acc += math.log((j + q1 + q2 - r + 1) / (j + q1 - r + 1))  # includes x = 0
            F[r - 1][j + 1] = acc
    for r in range(1, q2 + 1):
        acc = 0.0
        for c in range(1, lmax + 1):
            acc += math.log((M - q1 + c - r) / (M2 + c - r))
            B[r - 1][c] = acc

    def delta(l1, l2):
        s = sum(a[l1] for a in A) + sum(b[l2] for b in B)
        s -= sum(f[l1] - f[l1 - l2] for f in F)  # F[j] = sum_{x=1}^{j-1} g(x)
        return s
    return delta


def delta_ref(M1, M2, l1, l2, q1, q2):
    """direct log-sum (cross-check of the prefix implementation)."""
    M = M1 + M2
    s = 0.0
    for r in range(1, q1 + 1):
        for c in range(1, l1 + 1):
            s += math.log((M + c - r) / (M1 + c - r))
    for r in range(1, q2 + 1):
        for c in range(1, l2 + 1):
            s += math.log((M - q1 + c - r) / (M2 + c - r))
    for r in range(1, q1 + 1):
        for c in range(1, l2 + 1):
            s -= math.log((l1 - c + q1 + q2 - r + 1) / (l1 - c + q1 - r + 1))
    return s


def boxmin(delta, l1, l2, C, lmax):
    lo1 = max(0, l1 - C)
    hi1 = min(lmax, l1 + C)
    best = float('inf')
    arg = None
    for a in range(lo1, hi1 + 1):
        lo2 = max(0, l2 - C)
        hi2 = min(a, l2 + C)
        for b in range(lo2, hi2 + 1):
            v = delta(a, b)
            if v < best:
                best = v
                arg = (a, b)
    return best, arg


def main():
    # ---------- section 1: uniform residual bound on random stacks ----------
    rnd = random.Random(20261115)
    worst_slack = -float('inf')
    worst_arg = None
    n = 0
    for _ in range(400):
        M1 = rnd.randint(100, 2000)
        M2 = rnd.randint(100, 2000)
        q1 = rnd.randint(1, 3)
        q2 = rnd.randint(0, 3)
        if M1 < 4 * q1 + 4 or M2 < 4 * q2 + 4:
            continue
        M = M1 + M2
        l1 = rnd.randint(M // 20, min(M1, 3 * M // 4))
        l2 = rnd.randint(0, l1)
        N = M
        g1 = G(M / N, l1 / N) - G(M1 / N, l1 / N)
        g2 = G(M / N, l2 / N) - G(M2 / N, l2 / N)
        if q2 == 0:
            g2 = 0.0
        d = delta_ref(M1, M2, l1, l2, q1, q2)
        K1c = math.log(M / (M1 - q1))
        K2c = math.log((M - q1) / max(M2 - q2, 1))
        B = (q1 * (2 * K1c + math.log(l1 + 1) + 2) + q2 * (2 * K2c + 2)
             + q1 * q2 * (math.log(l1 + 2) + 2) + q1 * (q1 + q2))
        slack = abs(d - N * (q1 * g1 + q2 * g2)) - B
        n += 1
        if slack > worst_slack:
            worst_slack = slack
            worst_arg = (M1, M2, l1, l2, q1, q2)
    print('residual bound: samples %d  worst (|resid|-bound) %.6f at %s'
          % (n, worst_slack, worst_arg))
    assert worst_slack < 0, 'residual bound violated'

    # ---------- sections 2-3: symmetric saddle N=400 ----------
    Lam = 2.0 * (G(1.0, 0.5) - G(0.5, 0.5))
    N = 400
    M1 = M2 = N // 2
    l = N // 2
    Cmax = N
    for q in (1, 2, 3):
        delta = make_delta(M1, M2, q, q, Cmax)
        # cross-check prefix vs direct at a few points
        for (a, b) in ((l, l), (l - 3, l - 7), (l - 40, l - 40), (2 * l, l), (2 * l, 0)):
            assert abs(delta(a, b) - delta_ref(M1, M2, a, b, q, q)) < 1e-10
        sec2 = []
        for C in (1, 5, 10, 20, 40, 80):
            best, arg = boxmin(delta, l, l, C, Cmax)
            corner = 2 * q * (G(1.0, (l - C) / N) - G(0.5, (l - C) / N)) * N  # q*N*Lambda((l-C)/N)
            sec2.append((C, best, best / N, corner / N, arg))
            assert arg == (l - C, l - C), ('far-corner argmin failed', q, C, arg)
            assert best > 0.3 * q * N
        for row in sec2:
            print('q=%d boxmin C=%3d min/N=%.6f corner/N=%.6f arg=%s'
                  % (q, row[0], row[1] / N, row[3] / N, row[4]))
        print('q=%d q*Lambda=%.6f' % (q, q * Lam))
        for C in (40, 80, 120, 160, 199):
            best, arg = boxmin(delta, l, l, C, Cmax)
            print('q=%d breakdown C=%3d (c=%.4f) min/N=%.6f arg=%s'
                  % (q, C, C / N, best / N, arg))
            assert best > 0.0
        best, arg = boxmin(delta, l, l, 200, Cmax)
        print('q=%d breakdown C=200 (c=0.5000) min/N=%.6f arg=%s' % (q, best / N, arg))
        assert best == 0.0 and arg == (0, 0)
    print('PASS s3')


if __name__ == '__main__':
    main()
