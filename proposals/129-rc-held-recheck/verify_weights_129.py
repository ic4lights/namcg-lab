# verify_weights_129.py -- item 129, held block 48 one-loop weight bookkeeping (F cubic branch).
# Run:  python -I proposals/129-rc-held-recheck/verify_weights_129.py
# Expected invariant output: last line  WEIGHTS_129 PASS
#
# (1) Multiplicities of the three branches over l=1..N-1 sum to 3(N^2-1) (adjoint content).
# (2) SECOND MOMENT: with naive +1 weights on the vector content,
#     sum_{l=1}^{N-1} [(2l+3) l^2 + (2l+1)(-1)^2 + (2l-1)(l+1)^2] = N^2(N^2-1)  (sympy).
#     This is EXACTLY the factor multiplying (kappa3^2-4) chi^4 in the held identity, so the
#     vector-sector factor is reproduced; the cross term per l,
#     sum over branches of l(l+1)*mu, mu in {l,-1,-(l+1)}: (2l+3)l^2(l+1)-(2l+1)l(l+1)
#     -(2l-1)l(l+1)^2 = 0 identically.
#     The FULL held identity sum w lambda^2 = (kappa3^2-4) chi^4 N^2(N^2-1) also involves the
#     spinor/ghost supertrace bookkeeping of the product-backgrounds paragraph, which is NOT
#     reverified here; the identity is carried as CONDITIONAL and downstream U-sign claims are
#     NOT payloaded. (A previous journal note claiming non-reproduction was an arithmetic
#     error, corrected here.)
# (3) Algebra that DOES hold: (kappa3^2-4) chi^4 = c3^2 chi^2 - 4 c3 chi^3 (kappa3 = 2-c3/chi),
#     vanishing at kappa3 = 2 (the c3=0 index-part agreement point).
import sympy as sp

N, l = sp.symbols('N l', positive=True, integer=True)
chi, c3 = sp.symbols('chi c3', positive=True)

# (1)
msum = sp.summation((2 * l + 3) + (2 * l + 1) + (2 * l - 1), (l, 1, N - 1))
assert sp.simplify(msum - 3 * (N ** 2 - 1)) == 0, msum
# (2)
m2 = sp.summation((2 * l + 3) * l ** 2 + (2 * l + 1) + (2 * l - 1) * (l + 1) ** 2, (l, 1, N - 1))
m2 = sp.simplify(sp.expand(m2))
assert sp.simplify(m2 - N ** 2 * (N ** 2 - 1)) == 0, m2
print(f"sum (S.L)^2 over vector content = {m2} = N^2(N^2-1): matches the held factor")
cross = sp.simplify((2 * l + 3) * l ** 2 * (l + 1) - (2 * l + 1) * l * (l + 1) - (2 * l - 1) * l * (l + 1) ** 2)
assert cross == 0, cross
print("per-l cross term of L^2 and S.L in the second moment vanishes identically")
# (3)
e3 = sp.simplify(((2 - c3 / chi) ** 2 - 4) * chi ** 4 - (c3 ** 2 * chi ** 2 - 4 * c3 * chi ** 3))
assert e3 == 0, e3
assert sp.simplify(((2 - c3 / chi) ** 2 - 4) * chi ** 4).subs(c3, 0) == 0
print("WEIGHTS_129 PASS (vector factor N^2(N^2-1) reproduced; (k3^2-4)chi^4 algebra holds; full weighted identity conditional)")
