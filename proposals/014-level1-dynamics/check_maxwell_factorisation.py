"""
Leading-symbol tree-level sector: three Maxwell fields c_i^nu (i in W_y) and the induced h = H c.
Questions checked (exact, sympy, base point y=(y0,y4), symbolic q):
 (a) Sum_i S_i^{mu rho}S_i^{alpha sigma} q_rho q_sigma = Q^{mu alpha}(q) closed form (self-dual identity in y^perp).
 (b) Does E[h(c)] factor polynomially through the Maxwell operator, E H = P M ?  (entries of E H divisible by q^2 ?)
 (c) On-shell (M c = 0, q^2 = 0) is E[h(c)] = 0 ?   dimension of the kernel.
 (d) Source J = H^T T (T conserved):  c = J/q^2 (transverse), h = H c : closed form  h = (2/q^2)(Q T + T Q).  Degree-0 homogeneity.
"""
import sympy as sp, itertools, os
eta = sp.diag(-1, 1, 1, 1)
y0, y4 = int(os.environ.get('Y0', 5)), int(os.environ.get('Y4', 3))
ell2 = y0**2 - y4**2; ell = sp.sqrt(ell2)
q = sp.Matrix(sp.symbols('q0:4'))            # covector q_mu
qu = eta*q                                    # q^mu
q2 = sp.expand((q.T*qu)[0])

def Smats(chi=1):
    v = sp.Matrix([y4, 0, 0, 0, y0])/ell
    e = [sp.Matrix([0]*(i+1)+[1]+[0]*(3-i)) for i in range(3)]
    wedge = lambda a, b: a*b.T - b*a.T
    out = []
    for i in range(3):
        j, k = (i+1) % 3, (i+2) % 3
        W5 = wedge(e[i], v) + chi*wedge(e[j], e[k])
        out.append(W5[:4, :4])
    return out
S = Smats()

# (0) Gram matrix of the S_i (Frobenius), equal norm 2(1+y4^2/ell^2) and orthogonal
Gram = sp.Matrix(3, 3, lambda i, j: sum(S[i][a, b]*S[j][a, b] for a in range(4) for b in range(4)))
print('(0) Gram of S_i =', Gram.tolist(), ' expected diag', 2*(1 + sp.Rational(y4**2)/ell2))
# (a) Q^{mu alpha}
Q = sp.zeros(4, 4)
for i in range(3):
    s = S[i]*q            # s^mu = S^{mu rho} q_rho
    Q += s*s.T
Q = Q.applyfunc(sp.expand)
# closed form: 5D, q5 = (q^mu, 0); projector onto y^perp: P^{ab} = eta^{ab} + y^a y^b/ell2 (y upper)
y5 = sp.Matrix([y0, 0, 0, 0, y4])
eta5 = sp.diag(-1, 1, 1, 1, 1)
q5u = sp.Matrix(list(qu) + [0])
q5l = sp.Matrix(list(q) + [0])
Pperp = eta5.inv() + y5*y5.T/ell2
qperp = Pperp*eta5*q5u                  # q_perp^a (upper)  = P^a_b q^b
qperp2 = sp.expand((qperp.T*eta5*qperp)[0])
Qclosed = (qperp2*Pperp - qperp*qperp.T)[:4, :4].applyfunc(sp.expand)
print("(a) Q = q_perp^2 P_perp - q_perp q_perp^T  (4x4 block):", sp.simplify(Q - Qclosed) == sp.zeros(4, 4))

# H : c (12) -> h^{mu nu} (10 comps)
idx = [(i, j) for i in range(4) for j in range(i, 4)]
cs = [[sp.Symbol('c%d_%d' % (nu, i)) for i in range(3)] for nu in range(4)]   # c[nu][i] = c^nu_i
def hup_of(c):
    h = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            h[mu, nu] = sum(c[nu][i]*(S[i]*q)[mu] + c[mu][i]*(S[i]*q)[nu] for i in range(3))
    return h
def lin_einstein(h, p):
    gb = eta; gi = gb.inv(); hu = gi*h; tr = hu.trace(); pu = gi*p; p2 = (p.T*pu)[0]; ph = h*pu; pph = (pu.T*h*pu)[0]
    Ric = sp.Matrix(4, 4, lambda a, b: sp.Rational(1, 2)*(-ph[b]*p[a] - ph[a]*p[b] + p2*h[a, b] + p[a]*p[b]*tr))
    return Ric - sp.Rational(1, 2)*gb*(-pph + p2*tr)
flat = [x for row in cs for x in row]
hup = hup_of(cs); hlow = (eta*hup*eta).applyfunc(sp.expand)
EH = lin_einstein(hlow, q).applyfunc(sp.expand)         # 4x4, entries cubic in q, linear in c
# Maxwell operator: (M c_i)^b = q_a (q^a c^b - q^b c^a) = q2 c^b - q^b (q.c)   (upper b)
def Mc(c):
    return [[sp.expand(q2*c[b][i] - qu[b]*sum(q[a]*c[a][i] for a in range(4))) for i in range(3)] for b in range(4)]
Mcs = Mc(cs)

# (b) divisibility of E H by q2 : polynomial remainder in q0 (q2 is monic-degree 2 in q0 up to sign)
bad = 0
for (i, j) in idx:
    ent = sp.expand(EH[i, j])
    r = sp.rem(sp.Poly(ent, q[0]), sp.Poly(q2, q[0]))
    if r.as_expr() != 0: bad += 1
print("(b) number of the 10 entries of E[h(c)] NOT divisible by q^2 (as polynomials):", bad)

# polynomial factorisation EH = P M with P linear in q: unknown P^{(mu nu)}_{b i}{}^{rho} q_rho
unk = []
Pent = {}
eqs = []
for (a, b) in idx:
    expr = 0
    for bb in range(4):
        for i in range(3):
            for rho in range(4):
                u = sp.Symbol('p_%d%d_%d%d_%d' % (a, b, bb, i, rho)); unk.append(u)
                expr += u*q[rho]*Mcs[bb][i]
    diff = sp.expand(EH[a, b] - expr)
    eqs += sp.Poly(diff, *(list(q)+flat)).coeffs()
sol = sp.linsolve(eqs, unk)
print("(b') polynomial P (linear in q) with E H = P M exists:", sol != sp.EmptySet)

# (c) on-shell null waves: q null, c with q.c_i = 0 (Lorenz)  -> rank/kernel of E H
qnull = {q[0]: 1, q[1]: 1, q[2]: 0, q[3]: 0}
Lor = [sum(q[a]*cs[a][i] for a in range(4)).subs(qnull) for i in range(3)]
EHn = [[EH[i, j].subs(qnull) for (i, j) in idx]]
# linear map c -> E[h] at null q restricted to Lorenz condition
cols = []
sub = sp.solve(Lor, [cs[0][i] for i in range(3)], dict=True)[0]       # solve c^0_i from q.c=0 (q_0=1)
free = [cs[nu][i] for nu in range(1, 4) for i in range(3)]
Ecomp = [EH[i, j].subs(qnull).subs(sub) for (i, j) in idx]
Mat = sp.Matrix([[sp.diff(e, f) for f in free] for e in Ecomp])
print("(c) null q=(1,1,0,0): Lorenz-gauge Maxwell solutions: 9 free amplitudes (3 colours x 3), rank of c->E[h]:", Mat.rank())
# modulo gauge c ~ c + q lambda (3 dims inside), physical 6 polarisations
print("    => E[h(c)] vanishes only on a subspace of dimension", 9 - Mat.rank(), "of the 9; gauge directions (3) are in that subspace; physical polarisations annihilated:", 9 - Mat.rank() - 3, "of 6")

# (d) source and closed-form response
Tsym = sp.Matrix(4, 4, lambda a, b: sp.Symbol('T%d%d' % (min(a, b), max(a, b))))
# conserved T: q^mu T_{mu nu} = 0 : parametrize T_{mu nu} = (transverse projector) X (transverse projector) with generic X, numerically rational q
import random
random.seed(1)
def rr(): return sp.Rational(random.randint(-5, 5), random.randint(1, 3))
for trial in range(3):
    qv = sp.Matrix([rr() for _ in range(4)])
    sub = dict(zip(q, qv))
    quv = eta*qv; qq2 = (qv.T*quv)[0]
    if qq2 == 0: continue
    Pi = sp.eye(4) - quv*qv.T/qq2          # Pi^mu_nu acting on lower index objects: (T_{mu nu}) -> need q^mu T_{mu nu} = 0
    X = sp.Matrix(4, 4, lambda a, b: rr()); X = X + X.T
    Tl = (Pi.T*X*Pi)                       # lower indices; q^mu T_{mu nu}: (quv.T*Tl)=0
    assert (quv.T*Tl).applyfunc(sp.simplify) == sp.zeros(1, 4)
    Tu = eta*Tl*eta
    # J_{i nu} = 2 s_i^mu T_{mu nu}  (coupling int h_{mu nu}T^{mu nu}... use upper-index h and lower T): J_i^nu raised
    Qv = Q.subs(sub); Sv = [Si for Si in S]
    J = [ (2*(Sv[i]*qv).T*Tl).T for i in range(3)]       # J_{i, nu} lower index
    # M c = J (as vectors with upper index): M c_i^b = q2 c^b - q^b q.c  ->  c_i^b = eta^{bn} J_n / q2 (transverse)
    c = [[ (eta*J[i])[nu]/qq2 for i in range(3)] for nu in range(4)]
    assert all(sp.simplify(q2.subs(sub)*c[b][i] - quv[b]*sum(qv[a]*c[a][i] for a in range(4)) - (eta*J[i])[b]) == 0 for b in range(4) for i in range(3))
    h = hup_of(c).subs(sub)
    hclosed = 2*((Qv*Tl*eta) + (Qv*Tl*eta).T)/qq2    # (2/q^2)(Q^{mu a} T_a^nu + (mu nu))
    # note Q is upper-index; h upper
    yh = sp.Matrix([y0, 0, 0, 0])/ell                      # yhat^mu (4D part, upper)
    qpar = (qv.T*yh)[0]                                    # q_mu yhat^mu
    tau = (yh.T*Tl*eta)                                    # tau^nu = yhat^alpha T_alpha^nu  (row)
    QTclosed = (qq2 + qpar**2)*(eta*Tl*eta) + qq2*yh*tau - qpar*quv*tau
    print("(d') Q^{mu a}T_a^nu = (q^2+q_par^2) T + q^2 yhat tau - q_par q tau :", (Qv*Tl*eta - QTclosed).applyfunc(sp.simplify) == sp.zeros(4, 4))
    print("(d) trial", trial, ": h = (2/q^2)(Q T + T Q) closed form matches:", (h - hclosed).applyfunc(sp.simplify) == sp.zeros(4, 4))
    # E[h] vs T : is G[h] proportional to T ? compare ranks / explicit
    Gh = lin_einstein((eta*h*eta), qv)
    print("    E[h] (lower) first row:", list(Gh[0, :]), " ; q^2 T_{0 nu}:", [qq2*Tl[0, n] for n in range(4)])
