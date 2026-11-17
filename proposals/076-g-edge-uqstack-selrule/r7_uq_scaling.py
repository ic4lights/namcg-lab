"""074 s2: scaling of the U(q)-stack defect at fixed fractions.

Delta_{q1,q2}(l1,l2; M1,M2) from the closed form verified in s1 (float log-sums).
Continuum limit at u_f = l_f/N fixed, depths q_f fixed as N -> infinity:
  Delta/N -> q1*[G(m1+m2,u1)-G(m1,u1)] + q2*[G(m1+m2,u2)-G(m2,u2)],
  G(m,u) = (m+u)log(m+u) - m log m - u.
Equal-depth q1=q2=q at the symmetric saddle gives q*Lambda(u1,u2), Lambda as in the
integrated 073 paragraph (Lambda(1/2,1/2) = 0.523248144...).

Checks: q=1,N=3200,t=1 reproduces the 072/073 shipped value 0.520906 (see r3.out line
't=1.0 N= 3200 l= 1600 Delta/N=0.520906'); monotone increase in N and in q; unequal-depth
limits; row-block-removal limit. Deterministic.
"""
import math


def G(m, u):
    return (m + u) * math.log(m + u) - m * math.log(m) - u if m > 0 else (m + u) * math.log(m + u) - u


def Delta(M1, M2, l1, l2, q1, q2):
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


def limit_value(M1, M2, l1, l2, q1, q2):
    N = M1 + M2  # per-073: fractions taken w.r.t. N; here pass N explicitly below
    raise RuntimeError('unused')


def main():
    # ---- symmetric saddle m1=m2=1/2, k1=k2=1, t=1: s=N/2, l1=l2=N/2 ----
    Lam = 2.0 * (G(1.0, 0.5) - G(0.5, 0.5))
    print('Lambda(1/2,1/2) = %.9f' % Lam)
    assert abs(Lam - 0.523248144) < 1e-8
    prev = {}
    for N in (400, 800, 1600, 3200):
        M1 = M2 = N // 2
        l = N // 2
        row = []
        for q in (1, 2, 3):
            dN = Delta(M1, M2, l, l, q, q) / N
            row.append(dN)
            assert abs(dN - q * Lam) < abs(prev[q] - q * Lam) if q in prev else True
            assert 0 < dN < q * Lam
            print('sym t=1 N=%5d q=%d Delta_q/N=%.6f  q*Lambda=%.6f  N(resid)=%7.2f'
                  % (N, q, dN, q * Lam, N * (q * Lam - dN)))
            prev[q] = dN
        assert row[0] < row[1] < row[2], 'monotone in q failed'
        # consistency with the shipped 072/073 value at q=1, N=3200 (r3.out)
        if N == 3200:
            assert abs(row[0] - 0.520906) < 5e-7, 'q=1 N=3200 does not reproduce 072 s3'
    # ---- unequal depths at the symmetric fractions ----
    N = 3200
    M1 = M2 = N // 2
    l = N // 2
    g1 = G(1.0, 0.5) - G(0.5, 0.5)
    for (q1, q2) in ((2, 1), (1, 3), (3, 1)):
        dN = Delta(M1, M2, l, l, q1, q2) / N
        pred = (q1 + q2) * g1
        print('unequal N=3200 (q1,q2)=(%d,%d) Delta/N=%.6f pred=(q1+q2)*g=%.6f diff=%.5f'
              % (q1, q2, dN, pred, dN - pred))
        assert abs(dN - pred) < 0.02
    # ---- asymmetric m=(1/2,1/3): row-block-2 removal, Delta_{q,0}/N -> q*g1 ----
    N = 1600
    M1 = 800
    M2 = 533
    m = N - M1 - M2
    s1 = math.sqrt(M1 * (N - M1))
    s2 = math.sqrt(M2 * (N - M2))
    l1 = int(round(s1))
    l2 = int(round(s2))
    Ntot = float(N)
    mm1 = M1 / Ntot
    mm2 = M2 / Ntot
    g1a = G(mm1 + mm2, l1 / Ntot) - G(mm1, l1 / Ntot)
    print('asym N=1600 M=(800,533) l=(%d,%d) g1=%.6f' % (l1, l2, g1a))
    base = Delta(M1, M2, l1, 0, 1, 0) / Ntot
    print('Delta_{1,0}/N = %.6f (073 two-row Delta(l1,0)/N reference 0.188909)' % base)
    assert abs(base - 0.188909) < 5e-5
    for q in (2, 3):
        dN = Delta(M1, M2, l1, 0, q, 0) / Ntot
        print('Delta_{%d,0}/N = %.6f  ratio-to-q = %.6f' % (q, dN, dN / q))
        assert abs(dN / q - base) < 2e-4  # finite-N per-layer O(log N/N) correction
    print('PASS s2')


if __name__ == '__main__':
    main()
