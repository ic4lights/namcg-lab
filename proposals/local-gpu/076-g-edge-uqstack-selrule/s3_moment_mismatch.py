"""076 s3: exact moment mismatch between the stacked diagram and the
multiplicity-1 two-cap signature at the saddle (bounded negation arithmetic).

Convention (074 / appH Row length + stacked-rows paragraphs): row length
ell_f = 2 t s_f, s_f^2 = k_f M_f (N - M_f), M_f = m_f N, so
ell_f^2 = 4 t^2 k_f m_f (1 - m_f) N^2 exactly at integer M_f.
Multiplicity-1 signature (two caps, one row per component):
    S_true(p) = ell_1^{2p} + ell_2^{2p}.
Stacked signature with depths (q_1, q_2):
    S_stack(p) = q_1 ell_1^{2p} + q_2 ell_2^{2p}.
Mismatch fraction (excess over true, relative to true)
    rho_p = (S_stack - S_true)/S_true
          = sum_f (q_f - 1) (k_f w_f)^p / sum_f (k_f w_f)^p,  w_f = m_f(1 - m_f),
which is independent of N, t and the overall saddle scale: the mismatch is a
leading-order (O(1) in N) fraction of the moment for any q_f >= 2 - outside
the single-diagram dominance window of the transplanted rule.

Checks:
  (a) symbolic: rho_p after substituting ell_f = 2 t sqrt(k_f m_f (1-m_f)) N
      simplifies to an expression free of N and t (sympy, exact);
  (b) exact rationals: (q1,q2)=(2,1), (m1,m2)=(1/2,1/3), k=1:
      rho_1 = 9/17, rho_2 = 81/145; (q1,q2)=(2,2): rho_p = 1 for all p;
      symmetric saddle m1=m2 with equal depth q: excess/true = q - 1;
  (c) finite-N float check of the exact integer construction
      ell_f^2 = 4 M_f (N - M_f) at N = 600, 1200, 2400 (t=1, k=1; N
      divisible by 6 so M_f = m_f N are exact integers):
      rho_p identical across N and equal to the exact rationals.

Run: python -I proposals/076-g-edge-uqstack-selrule/s3_moment_mismatch.py
Expected invariants: (a) free(N)=True, free(t)=True for p=1..4;
(b) rho_1 = 9/17, rho_2 = 81/145, rho_p = 1 for (2,2), q-1 symmetric;
(c) max spread across N < 1e-12 and floats match 9/17, 81/145; last line 'PASS s3'.
"""
import sympy as sp

N, t = sp.symbols('N t', positive=True)
k1, k2, m1, m2, q1, q2 = sp.symbols('k1 k2 m1 m2 q1 q2', positive=True)

w1 = m1 * (1 - m1)
w2 = m2 * (1 - m2)
l1sq = 4 * t**2 * k1 * w1 * N**2
l2sq = 4 * t**2 * k2 * w2 * N**2


def rho(pv):
    true_ = l1sq**pv + l2sq**pv
    stack_ = q1 * l1sq**pv + q2 * l2sq**pv
    return sp.simplify((stack_ - true_) / true_)


print('(a) N- and t-independence of rho_p at the saddle:')
ok_a = True
for pv in range(1, 5):
    r = sp.simplify(sp.cancel(sp.together(rho(pv))))
    fN = r.free_symbols.isdisjoint({N})
    ft = r.free_symbols.isdisjoint({t})
    ok_a = ok_a and fN and ft
    print('  p=%d  free(N)=%s free(t)=%s' % (pv, fN, ft))

print('(b) exact rational values:')
subs = {q1: 2, q2: 1, m1: sp.Rational(1, 2), m2: sp.Rational(1, 3),
        k1: 1, k2: 1}
r1v = rho(1).subs(subs)
r2v = rho(2).subs(subs)
print('  (q1,q2)=(2,1), (m1,m2)=(1/2,1/3): rho_1 = %s  rho_2 = %s' % (r1v, r2v))
ok_b1 = (r1v == sp.Rational(9, 17)) and (r2v == sp.Rational(81, 145))
ok_b2 = True
for pv in range(1, 6):
    v = sp.simplify(rho(pv).subs({q1: 2, q2: 2}))
    ok_b2 = ok_b2 and (v == 1)
print('  (q1,q2)=(2,2), generic m: rho_p == 1 for p=1..5: %s' % ok_b2)
ms = sp.symbols('ms', positive=True)
qq = sp.symbols('q', positive=True)
lsq = 4 * t**2 * ms * (1 - ms) * N**2
rsym = sp.simplify(((qq * lsq + qq * lsq) - 2 * lsq) / (2 * lsq))
ok_b3 = (rsym == qq - 1)
print('  symmetric saddle, equal depth q: excess/true = q-1 (p-independent): %s'
      % ok_b3)

print('(c) finite-N float check, ell_f^2 = 4 M_f (N - M_f), m=(1/2,1/3), q=(2,1):')
print('    (N divisible by 6 so M_f = m_f N are exact integers)')
vals = []
for NN in (600, 1200, 2400):
    M1, M2 = NN // 2, NN // 3
    l1s = 4.0 * M1 * (NN - M1)
    l2s = 4.0 * M2 * (NN - M2)
    row = []
    for pv in (1, 2, 3):
        true_ = l1s**pv + l2s**pv
        stack_ = 2.0 * l1s**pv + 1.0 * l2s**pv
        row.append((stack_ - true_) / true_)
    vals.append(row)
    print('  N=%4d rho_1=%.15f rho_2=%.15f rho_3=%.15f' % (NN, row[0], row[1], row[2]))
spread = max(max(abs(v[j] - vals[0][j]) for v in vals) for j in range(3))
print('  max spread across N: %.3e' % spread)
ok_c = spread < 1e-12
ok_close = abs(vals[0][0] - 9 / 17) < 1e-12 and abs(vals[0][1] - 81 / 145) < 1e-12
print('  float values match exact rationals 9/17, 81/145: %s' % ok_close)

ok = ok_a and ok_b1 and ok_b2 and ok_b3 and ok_c and ok_close
print('all checks inside thresholds:', ok)
assert ok
print('PASS s3')
