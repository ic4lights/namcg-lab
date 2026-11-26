"""075 s5: closed forms (sympy, exact) for the one-form operator of the cubic term about the flat point,
   M_b^d = -(q^2 delta_b^d - q_b q^d) + i eps_b^{cd}_f (c w)^f q_c ,
 (1) exact identity det(M - q_b q^d) = (q^2)^2 [ (q^2)^2 - c^2((q.w)^2 - q^2 w^2) ], and M q = 0 (gauge);
     the product of the three nonzero eigenvalues of M is -q^2 [ ... ] (numerical, s3 (4)); the rank of M
     drops below 3 only on the bracket (at null q the zero eigenvalue is defective), as found for the
     28-field system in s3 (3);
 (2) branches for unit spacelike, unit timelike and null w, and their limits;
 (3) the S^3 levels of s4: (q0/kappa)^2 = l(l+1).
"""
import sympy as sp

q0, q1, q2_, q3, c = sp.symbols('q0 q1 q2 q3 c', real=True)
w = sp.symbols('w0:4', real=True)
eta = sp.diag(-1, 1, 1, 1)
q = sp.Matrix([q0, q1, q2_, q3])               # lower components
qu = eta * q
Q2 = sp.expand((q.T * qu)[0])
wl = eta * sp.Matrix(w)
W2 = sp.expand((sp.Matrix(w).T * wl)[0])
QW = sp.expand((q.T * sp.Matrix(w))[0])
epsU = lambda a, b, cc, d: sp.LeviCivita(a, b, cc, d)          # eps^{abcd}, eps^{0123} = 1
# eps_b^{cd}_f = eta_bb' eta_ff' eps^{b' c d f'}
M = sp.zeros(4, 4)
for b in range(4):
    for d in range(4):
        s = -(Q2 * (1 if b == d else 0) - q[b] * qu[d])
        s += sp.I * c * sum(eta[b, b] * eta[f, f] * epsU(b, cc, d, f) * q[cc] * w[f] for cc in range(4) for f in range(4))
        M[b, d] = s
Mg = M - q * qu.T
target = sp.expand(Q2 ** 2 * (Q2 ** 2 - c ** 2 * (QW ** 2 - Q2 * W2)))
print('(1) det(M - q q^T) - (q^2)^2[(q^2)^2 - c^2((q.w)^2 - q^2 w^2)] =', sp.simplify(sp.expand(Mg.det()) - target))
# gauge direction
print('    M q^gauge (A_d = q_d) =', sp.simplify(M * q).T)

k, kw, kp = sp.symbols('k k_w k_perp', positive=True)
X = sp.symbols('X')                              # X = q^2
print('(2) unit spacelike w: X^2 + c^2 X - c^2 (q.w)^2 = 0 ->', sp.solve(sp.Eq(X ** 2 + c ** 2 * X - c ** 2 * kw ** 2, 0), X))
Xm = -c ** 2 / 2 - sp.sqrt(c ** 4 / 4 + c ** 2 * kw ** 2)
Xp = -c ** 2 / 2 + sp.sqrt(c ** 4 / 4 + c ** 2 * kw ** 2)
om2_m = kp ** 2 + kw ** 2 - Xm
om2_p = kp ** 2 + kw ** 2 - Xp
print('    gapped branch q0^2 - (k^2 + c^2) =', sp.simplify(om2_m - kp ** 2 - kw ** 2 - c ** 2), ' (>= 0)')
print('    gapped branch at k = 0: q0^2 =', sp.simplify(om2_m.subs({kp: 0, kw: 0})))
print('    gapless branch q0^2, series in k_w:', sp.series(om2_p.subs(c, sp.Symbol('C', positive=True)), kw, 0, 7))
print('    gapless branch q0^2 - k_perp^2 >= 0:', sp.simplify((om2_p - kp ** 2) * (kw ** 2 + c ** 2 / 2 + sp.sqrt(c ** 4 / 4 + c ** 2 * kw ** 2))), '(numerator after rationalising, = k_w^4)')
print('    momenta with q.w = 0: q^2 in', sp.solve(sp.Eq(X ** 2 + c ** 2 * X, 0), X))
print('    unit timelike w (w^2 = -1, q.w = q0): bracket - (q0^2 - k^2 - c k)(q0^2 - k^2 + c k) =', sp.expand(((-q0 ** 2 + k ** 2) ** 2 - c ** 2 * (q0 ** 2 + (-q0 ** 2 + k ** 2))) - (q0 ** 2 - k ** 2 - c * k) * (q0 ** 2 - k ** 2 + c * k)))
qq0 = sp.sqrt(k ** 2 - sp.Abs(c) * k)
print('    timelike: q0^2 = k^2 - |c| k < 0 for 0 < k < |c|; max of |c| k - k^2 at k = |c|/2:',
      sp.simplify((sp.Abs(c) * k - k ** 2).subs(k, sp.Abs(c) / 2)), '-> max |Im q0| = |c|/2')
n = sp.Matrix([1, 0, 0, 1])
QWn = sp.expand((q.T * n)[0])
shift = sp.expand(((q + c * (eta * n) / 2).T * eta.inv() * (q + c * (eta * n) / 2))[0])
print('    null w: q^2 + c q.w - (q + c w_flat/2)^2 =', sp.simplify(Q2 + c * QWn - shift), ' (w null)')
print('(3) l(l+1) for l = 1/2, 1, 3/2, 2, 5/2:', [sp.Rational(l2, 2) * (sp.Rational(l2, 2) + 1) for l2 in range(1, 6)],
      ' sqrt:', [round(float(sp.sqrt(sp.Rational(l2, 2) * (sp.Rational(l2, 2) + 1))), 4) for l2 in range(1, 6)])
