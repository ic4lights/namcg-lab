"""
Reduce the gauge-invariant quartic forms Mh(p), Mx(p) (from check_quadratic_form_sym.py) to the 3-dim gauge quotient
and compare with the tree-level Maxwell kernel  M_Max = q^2 eta - q q  (q^mu = Tbar^{mu r} p_r, q_a = eta_{am} q^m).
Prints the generalized eigenvalues lambda of  det(Q_red - lambda M_red)=0 for Q = Mh and Q = Mx, at sample momenta.
Usage: python analyze_quadratic_forms.py s0 a0 b0
"""
import sympy as sp, sys
from sympy import Symbol
s0, a0, b0 = [sp.Rational(v) for v in sys.argv[1:4]]
fn = 'quadratic_forms_s%s_a%s_b%s.srepr' % (s0, a0, b0)
data = sp.sympify(open(fn).read(), locals={}) if False else eval(open(fn).read(), sp.__dict__)
Mh, Mx = data['Lh'], data['Lx']
p = sp.symbols('p0:4')
eta = sp.diag(s0, 1, 1, 1)
Tb = sp.zeros(4, 4); Tb[0, 1] = a0; Tb[1, 0] = -a0; Tb[2, 3] = b0; Tb[3, 2] = -b0
q = Tb*sp.Matrix(p); ql = eta*q
q2 = (q.T*eta*q)[0]
MMax = q2*eta - ql*ql.T       # quadratic form on upper-index u:  u^T M u
# forms act on upper-index u; M_Max,ab u^a u^b with M_ab = q2 eta_ab - q_a q_b
def reduce(Q, pnum, label):
    sub = dict(zip(p, pnum))
    qn = q.subs(sub)
    # complement basis: pick 3 standard basis vectors independent of qn
    for drop in range(4):
        if qn[drop] != 0: break
    idx = [i for i in range(4) if i != drop]
    E = sp.zeros(4, 3)
    for c, i in enumerate(idx): E[i, c] = 1
    Qr = E.T*Q.subs(sub)*E; Mr = E.T*MMax.subs(sub)*E
    lam = sp.symbols('lam')
    cp = sp.factor((Qr - lam*Mr).det())
    roots = sp.solve(cp, lam)
    return roots, q2.subs(sub), sub
for pnum in [(1, 2, 0, 0), (0, 0, 1, 3), (1, 2, 3, 5), (2, -1, 1, 1), (3, 1, 2, 7)]:
    P1 = pnum[0]**2 + pnum[1]**2; P2 = pnum[2]**2 + pnum[3]**2
    print("p =", pnum, " (p0,p1)^2=%s (p2,p3)^2=%s" % (P1, P2), " q^2 =", q2.subs(dict(zip(p, pnum))))
    for name, Q in (('Mh', Mh), ('Mx', Mx)):
        roots, qq, _ = reduce(Q, pnum, name)
        print("   ", name, "generalized eigenvalues:", [sp.nsimplify(r) for r in roots])
