"""
Symbolic-in-p version of analyze_quadratic_forms.py:  det( Q_red - lam * M_red ) on the gauge quotient, factored, for Q = Mh and Q = Mx.
Reads quadratic_forms_s*_a*_b*.srepr (written by check_quadratic_form_sym.py).  Usage: python analyze_quadratic_forms_symbolic.py s0 a0 b0
Expected: Mx -> (lam - rho0^2 p2_eta)^3 ;  Mh -> (lam + rho0^2 p2_eta/4)^2 (lam + 3 rho0^2 p2_eta/4),  rho0 = 1/(a0 b0),
 p2_eta = eta^{mu nu} p_mu p_nu  (up to an overall p-dependent factor from the det of M_red).
"""
import sympy as sp, sys
s0, a0, b0 = [sp.Rational(v) for v in sys.argv[1:4]]
data = eval(open('quadratic_forms_s%s_a%s_b%s.srepr' % (s0, a0, b0)).read(), sp.__dict__)
Mh, Mx = data['Lh'], data['Lx']
p = sp.symbols('p0:4'); lam = sp.symbols('lam')
eta = sp.diag(s0, 1, 1, 1)
Tb = sp.zeros(4, 4); Tb[0, 1] = a0; Tb[1, 0] = -a0; Tb[2, 3] = b0; Tb[3, 2] = -b0
q = Tb*sp.Matrix(p); ql = eta*q; q2 = (q.T*eta*q)[0]
MMax = q2*eta - ql*ql.T
E = sp.zeros(4, 3)
for c, i in enumerate([1, 2, 3]): E[i, c] = 1          # complement of the e_0 direction (q^0 = a0 p1 != 0 generically)
p2 = (sp.Matrix(p).T*eta.inv()*sp.Matrix(p))[0]
rho0 = 1/(a0*b0)
Mr = E.T*MMax*E
for name, Q in (('Mx', Mx), ('Mh', Mh)):
    cp = sp.factor(sp.expand((E.T*Q*E - lam*Mr).det()))
    print(name, ":", cp)
    sub = {lam: -rho0**2*p2*sp.Symbol('c')}
    # check the claimed roots by substitution
roots = {'Mx': [rho0**2*p2]*3, 'Mh': [-rho0**2*p2/4, -rho0**2*p2/4, -3*rho0**2*p2/4]}
for name, Q in (('Mx', Mx), ('Mh', Mh)):
    expr = sp.expand((E.T*Q*E - lam*Mr).det())
    prod = sp.expand(Mr.det()*(-1)**3*sp.prod([(lam - r) for r in roots[name]]))
    print(name, "det(Q_red - lam M_red) == -det(M_red) * prod(lam - root):", sp.simplify(expr - prod) == 0)
print("p2_eta =", p2, "  rho0 =", rho0)
