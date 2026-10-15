"""
Tree-level Maxwell form W0 = K*M(q) (12x12, M = oplus_i (q^2 eta - q q) acting on c_i^nu) plus an ASSUMED induced linearised
Einstein-Hilbert form  W1 = g * H^T Eh H  (Eh = quadratic form of the linearised EH action on h, h = H c).
Exact rational / sympy checks:
 (a) Euler-Lagrange form of linearised EH: Eh h = - (linearised Einstein tensor) up to the standard normalisation; symmetric.
 (b) generalised eigenvalues of W1 relative to W0 on the 9-dimensional quotient by the Maxwell gauge c ~ c + q lambda_i:
     poles of the combined propagator.
 (c) matter exchange amplitude  T.H W^{-1} H^T.T  at tree level only, static source in the base-point rest frame: contact.
"""
import sympy as sp, random
exec(open('check_maxwell_factorisation.py').read().split("# (b) divisibility")[0].replace('print(', 'pass; (lambda *a, **k: None)('))
random.seed(7)
def rr(): return sp.Rational(random.randint(-5, 5), random.randint(1, 3))
# matrix of H (10 x 12) in symbols
cols = []
Hmat = sp.zeros(10, 12)
for col, (nu, i) in enumerate([(nu, i) for nu in range(4) for i in range(3)]):
    c = [[0]*3 for _ in range(4)]; c[nu][i] = 1
    h = hup_of(c)
    for r, (a, b) in enumerate(idx): Hmat[r, col] = h[a, b]
# symmetric-tensor <-> vector map: quadratic form of linearised EH:  L2 = -1/2 h^{mu nu} G_{mu nu}[h]  (sign convention immaterial here)
def Gof(hvec, qv):
    h = sp.zeros(4, 4)
    for r, (a, b) in enumerate(idx): h[a, b] = h[b, a] = hvec[r]
    G = lin_einstein((eta*h*eta), qv)
    return G
def Emat(qv):
    # bilinear form  h . G[h'] with h upper indices contracted against lower G: sum_{mu nu} h^{mu nu} G_{mu nu}
    Em = sp.zeros(10, 10)
    for c2 in range(10):
        e2 = sp.zeros(10, 1); e2[c2] = 1
        G = Gof(e2, qv)
        for r, (a, b) in enumerate(idx):
            w = 1 if a == b else 2
            Em[r, c2] = w*G[a, b]
    return Em
qlist = [sp.Matrix([0, sp.Rational(1,3), -5, 3]), sp.Matrix([7, 1, 2, -1]), sp.Matrix([3, 1, 0, 0]), sp.Matrix([2, 5, 1, 1])]
for trial in range(len(qlist)):
    qv = qlist[trial]; sub = dict(zip(q, qv))
    q2v = q2.subs(sub); quv = eta*qv
    if q2v == 0: continue
    # raw H at this q: Hmat computed with symbolic q -> substitute; note Hmat built from hup_of(c) uses symbolic q
    Hq = Hmat.subs(sub)
    Eq = Emat(qv)
    print("trial", trial, "q=", list(qv), "q^2=", q2v)
    print(" (a) Eh symmetric:", (Eq - Eq.T).applyfunc(sp.simplify) == sp.zeros(10, 10), " rank of Eh on all h:", Eq.rank())
    # Maxwell form M (12x12), c ordering (nu,i): (Mc)^b = q2 c^b - q^b q.c  with q_a contraction
    Mm = sp.zeros(12, 12)
    for (b, i) in [(b, i) for b in range(4) for i in range(3)]:
        for (nu, j) in [(nu, j) for nu in range(4) for j in range(3)]:
            if i != j: continue
            val = (q2v if b == nu else 0) - quv[b]*qv[nu]
            Mm[b*3+i, nu*3+j] = val
    # to make the form symmetric use lowered index on the equation: Mlow_{b nu} = eta_{b b'} M^{b'}_nu
    Mlow = sp.zeros(12, 12)
    for (b, i) in [(b, i) for b in range(4) for i in range(3)]:
        for (nu, j) in [(nu, j) for nu in range(4) for j in range(3)]:
            if i != j: continue
            Mlow[b*3+i, nu*3+j] = eta[b, b]*Mm[b*3+i, nu*3+j]
    print(" Maxwell form symmetric:", (Mlow - Mlow.T).applyfunc(sp.simplify) == sp.zeros(12, 12), " rank:", Mlow.rank())
    # gauge vectors c_i^nu = q^nu * l_i  (upper index)
    Gv = sp.zeros(12, 3)
    for i in range(3):
        for nu in range(4): Gv[nu*3+i, i] = quv[nu]
    W1 = Hq.T*Eq*Hq
    print(" W1 gauge-invariant (W1*gauge=0):", (W1*Gv).applyfunc(sp.simplify) == sp.zeros(12, 3), " rank W1:", W1.rank())
    # Quotient: choose complement basis of gauge in 12-space
    ns = Gv.T.nullspace()  # vectors v with Gv^T v = 0 : not a complement; use projector onto quotient via basis completion
    # complete to a basis of R^12 using standard vectors
    full = Gv
    for k in range(12):
        e = sp.zeros(12, 1); e[k] = 1
        trial_m = full.row_join(e)
        if trial_m.rank() > full.rank(): full = trial_m
    Cm = full[:, 3:]                     # complement, 12 x 9
    M9 = (Cm.T*Mlow*Cm); W9 = (Cm.T*W1*Cm)
    print(" quotient dims: rank M9 =", M9.rank(), " rank W9 =", W9.rank())
    lam = sp.symbols('lam')
    cp = sp.factor((W9 - lam*M9).det())
    print(" det(W1 - lam M) on quotient =", cp)
    print(" ratio to q^2:", [sp.nsimplify(s/q2v) for s in sp.roots(sp.Poly(sp.numer(sp.together((W9 - lam*M9).det())), lam)).keys()])
