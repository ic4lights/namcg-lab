# verify_ehsum_128.py  (item 128, script 3)
#
# Self-contained re-derivation of the item-123 Alternate-scope sector algebra
# (weighted a1 sums and N0) with e_h carried as a SYMBOL, followed by
# substitution of the e_h value derived in script 2 (passed as argv[1], a
# rational), the condition-(iv) comparison, and the sigma translation.
# Item-123 scripts are NOT run (author kill-order for verify_ghost_op_123.py
# honored; no 123 script is executed here).
#
# Conventions: a1 = tr(R/6 - E) (eq:appA-a1); weights w_s per eq:appA-sector-sum
# with the Grassmann ghost weight -2; per-component scalar record
# E = lambda v^2 + Q R_E per the appH Hermitian-block paragraph; tensor block
# defined by the TOTAL fibre trace tr E_ten = e_h R_E (review-r1 finding 1 of
# item 123: script-2-of-123 definition, which is the clause integrated at r2).
#
# Usage: python -I verify_ehsum_128.py <e_h-rational>   (e.g. 6 or -5/3)
# Expected outputs: A1_MATCH_123 = True, N0_MATCH_123 = True,
#   COND_IV_EH = -5/3 (the unique e_h with A1_trunk = 0 at Q=1/6, nK=0),
#   A1_derived_Q16nK0, SIGMA_for_cond_iv, PASS3.
import sys
import sympy as sp

Q, QK, nK, eh = sp.symbols('Q QK n_K e_h')
J, Lam2, mu2 = sp.symbols('J Lambda2 mu2', positive=True)

a1_sc16 = 16*(sp.Rational(1, 6) - Q)          # 16 scalars, E = lambda v^2 + Q R_E
a1_ten = 10*sp.Rational(1, 6) - eh            # tensor block, total-trace reading
a1_gh = sp.Rational(4, 6) + 1                 # 4-vector fibre, E_gh = -Ric
w_gh = -2                                     # eq:appA-sector-sum ghost weight

A1 = a1_sc16 + nK*(sp.Rational(1, 6) - QK) + a1_ten + w_gh*a1_gh
rec = 16*(sp.Rational(1, 6) - Q) + nK*(sp.Rational(1, 6) - QK) - sp.Rational(5, 3) - eh
print("A1_MATCH_123 =", sp.simplify(A1 - rec) == 0)

N0 = 16 + 10 + w_gh*4 + nK
print("N0_MATCH_123 =", sp.simplify(N0 - (18 + nK)) == 0)

# windowed bracket of the 123 record:
#   -1/(32 pi^2) [ 16(1/6-Q) J + (n_K(1/6-Q_K) - 5/3 - e_h)(Lambda^2 - mu^2) ]
br = 16*(sp.Rational(1, 6) - Q)*J + (nK*(sp.Rational(1, 6) - QK) - sp.Rational(5, 3) - eh)*(Lam2 - mu2)
br2 = 16*(sp.Rational(1, 6) - Q)*J + (nK*(sp.Rational(1, 6) - QK) + sp.simplify(a1_ten + w_gh*a1_gh))*(Lam2 - mu2)
print("WINDOW_MATCH =", sp.simplify(br - br2) == 0)

sol = sp.solve(A1.subs({Q: sp.Rational(1, 6), nK: 0}), eh)
print("COND_IV_EH =", sol)

if len(sys.argv) > 1:
    v = sp.Rational(sys.argv[1])
    print("E_H_INPUT =", v)
    A1v = sp.simplify(A1.subs({Q: sp.Rational(1, 6), nK: 0, eh: v}))
    print("A1_derived_Q16nK0 =", A1v)
    print("SIGMA_for_cond_iv =", sp.Rational(-5, 3) - v)
    print("COND_IV_HOLDS =", A1v == 0)
print("PASS3")
