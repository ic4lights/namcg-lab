"""
s2_axial_torsion_4coord.py  (proposal 044)

Four-coordinate Poisson class, constant background theta_bar, plane-wave matrix fluctuation
a^mu = u^mu cos(p.x):  T^{mu nu} = q^mu u^nu - q^nu u^mu (times -sin(p.x)), q = theta_bar p.
Coframe e^A_mu = eta^{AB} omega_{mu B}, omega = Theta^{-1}; first-order torsion
T^A_{mu nu} = d_mu e^A_nu - d_nu e^A_mu.  All quadratic invariants carry the same phase factor,
so their ratios are exact rational numbers computed from the amplitudes (exact sympy arithmetic).

Checks (Euclidean eta = delta, off shell, the two modes with delta rho = 0, i.e. p.u = 0 modulo u ~ q):
  (a) V_mu = G^{lam nu} T_{lam mu nu} = 0 on these modes;
  (b) the identity X = 2 calT + (3/2) S_{lmn}S^{lmn} + 2 V^2  (X = T_{lmn}T^{lmn},
      calT = 1/4 T T + 1/2 T_{lmn}T^{mln} - V^2, S = totally antisymmetric part);
  (c) the quadratic forms of S^2 and of calT relative to X on the 2-dim mode space:
      calT = X/4 (so <R> = -<calT> = -X/4, r = -4 on the modes) and (3/2) S^2 = X/2:
      the axial torsion carries half of X on every mode (no axion-free tensor mode);
  (d) Lorentzian eta = diag(-1,1,1,1), on-shell null q (Maxwell equation at first order) with
      eta(q,u) = 0 and p.u = 0: value of the axial torsion and of X there.
"""
import sympy as sp, random
from itertools import permutations
random.seed(44)
Rr = lambda: sp.Rational(random.randint(-6, 6), random.randint(1, 4))

def antisym(vals):
    a, b, c, d, e, f = vals
    return sp.Matrix([[0, a, b, c], [-a, 0, d, e], [-b, -d, 0, f], [-c, -e, -f, 0]])

def torsion_data(th, eta, p, u):
    om = th.inv()                                 # omega_{mu B}: om[mu, B]
    etai = eta.inv()
    e = etai * om.T                               # e[A, mu] = eta^{AB} om[mu, B]
    G = e.T * eta * e                             # G_{mu nu}
    Gi = G.inv()
    q = th * p
    Th = q * u.T - u * q.T                        # T^{mu nu} amplitude
    om1 = -om * Th * om                           # first-order omega (amplitude)
    e1 = etai * om1.T
    # torsion T^A_{mu nu} = p_mu e1^A_nu - p_nu e1^A_mu (common phase factor dropped)
    TA = [[[p[m] * e1[A, n] - p[n] * e1[A, m] for n in range(4)] for m in range(4)] for A in range(4)]
    # T_{lam mu nu} = eta_{AB} e^A_lam T^B_{mu nu}
    T = [[[sum(eta[A, B] * e[A, l] * TA[B][m][n] for A in range(4) for B in range(4)) for n in range(4)] for m in range(4)] for l in range(4)]
    def up(l, m, n):  # T^{lam mu nu}
        return sum(Gi[l, a] * Gi[m, b] * Gi[n, c] * T[a][b][c] for a in range(4) for b in range(4) for c in range(4))
    Tup = [[[up(l, m, n) for n in range(4)] for m in range(4)] for l in range(4)]
    X = sp.simplify(sum(T[l][m][n] * Tup[l][m][n] for l in range(4) for m in range(4) for n in range(4)))
    TTp = sp.simplify(sum(T[l][m][n] * Tup[m][l][n] for l in range(4) for m in range(4) for n in range(4)))
    V = [sp.simplify(sum(Gi[l, n] * T[l][m][n] for l in range(4) for n in range(4))) for m in range(4)]
    V2 = sp.simplify(sum(Gi[a, b] * V[a] * V[b] for a in range(4) for b in range(4)))
    def S(l, m, n): return sp.Rational(1, 3) * (T[l][m][n] + T[m][n][l] + T[n][l][m])
    Sl = [[[S(l, m, n) for n in range(4)] for m in range(4)] for l in range(4)]
    def Sup(l, m, n):
        return sum(Gi[l, a] * Gi[m, b] * Gi[n, c] * Sl[a][b][c] for a in range(4) for b in range(4) for c in range(4))
    SS = sp.simplify(sum(Sl[l][m][n] * Sup(l, m, n) for l in range(4) for m in range(4) for n in range(4)))
    calT = sp.simplify(sp.Rational(1, 4) * X + sp.Rational(1, 2) * TTp - V2)
    Snonzero = any(sp.simplify(Sl[l][m][n]) != 0 for l in range(4) for m in range(4) for n in range(4))
    Tnonzero = any(sp.simplify(T[l][m][n]) != 0 for l in range(4) for m in range(4) for n in range(4))
    return dict(X=X, TTp=TTp, V=V, V2=V2, SS=SS, calT=calT, q=q, G=G, Snonzero=Snonzero, Tnonzero=Tnonzero)

out = []
def P(*a):
    line = " ".join(str(x) for x in a); print(line); out.append(line)

P("=== Euclidean eta = delta, off shell, delta rho = 0 modes ===")
eta = sp.eye(4)
for trial in range(4):
    while True:
        th = antisym([Rr() for _ in range(6)])
        if th.det() != 0: break
    p = sp.Matrix([Rr() for _ in range(4)])
    q = th * p
    # basis of {u : p.u = 0}: contains q; pick two further vectors
    ns = sp.Matrix([list(p)]).nullspace()           # 3 vectors with p.u = 0
    basis = [v for v in ns]
    # remove q-direction: choose two vectors independent of q
    w = []
    for v in basis:
        if sp.Matrix.hstack(q, *w, v).rank() == len(w) + 2: w.append(v)
        if len(w) == 2: break
    c1, c2 = sp.symbols('c1 c2')
    u = c1 * w[0] + c2 * w[1]
    d = torsion_data(th, eta, p, u)
    QX = sp.Poly(sp.expand(d['X']), c1, c2); QS = sp.Poly(sp.expand(d['SS']), c1, c2); QT = sp.Poly(sp.expand(d['calT']), c1, c2)
    Vzero = all(sp.simplify(v) == 0 for v in d['V'])
    ident = sp.simplify(d['X'] - (2 * d['calT'] + sp.Rational(3, 2) * d['SS'] + 2 * d['V2'])) == 0
    ratioS = sp.simplify(sp.Rational(3, 2) * d['SS'] / d['X'])
    ratioT = sp.simplify(d['calT'] / d['X'])
    detX = sp.Matrix([[QX.coeff_monomial(c1**2), QX.coeff_monomial(c1*c2) / 2], [QX.coeff_monomial(c1*c2) / 2, QX.coeff_monomial(c2**2)]]).det()
    P(f"trial {trial}: theta_bar entries {list(th[0,1:])+[th[1,2],th[1,3],th[2,3]]}, p = {list(p)}")
    P(f"   V = 0 on modes: {Vzero} ; identity X = 2calT + 3/2 S^2 + 2V^2: {ident}")
    P(f"   (3/2)S^2 / X = {ratioS}  ;  calT / X = {ratioT}   (as functions of the polarisation (c1,c2))")
    P(f"   det of the X form on the 2-dim mode space = {sp.nsimplify(detX)} (nonzero: X definite there)")

P("")
P("=== Lorentzian eta = diag(-1,1,1,1), on-shell null q, eta(q,u) = 0, p.u = 0 ===")
eta = sp.diag(-1, 1, 1, 1)
ok = 0
for trial in range(40):
    if ok == 3: break
    while True:
        th = antisym([Rr() for _ in range(6)])
        if th.det() != 0: break
    K = th.T * eta * th
    p1, p2, p3 = Rr(), Rr(), Rr(); p0 = sp.symbols('p0')
    pv = sp.Matrix([p0, p1, p2, p3])
    sols = sp.solve(sp.expand((pv.T * K * pv)[0]), p0)
    sols = [s_ for s_ in sols if s_.is_real]
    if not sols: continue
    ok += 1
    p = pv.subs(p0, sols[0])
    q = th * p
    A = sp.Matrix([list(p), list((eta * q).T)])     # conditions p.u = 0, eta(q,u) = 0
    ns = A.nullspace()
    w = [v for v in ns if sp.Matrix.hstack(q, v).rank() == 2]
    u = sp.simplify(w[0])
    d = torsion_data(th, eta, p, u)
    P(f"trial {trial}: K(p,p) = {sp.simplify((p.T*K*p)[0])}, eta(q,q) = {sp.simplify((q.T*eta*q)[0])}")
    P(f"   X = {sp.nsimplify(sp.simplify(d['X']))}, S^2 = {sp.nsimplify(sp.simplify(d['SS']))}, calT = {sp.nsimplify(sp.simplify(d['calT']))}, V2 = {sp.nsimplify(sp.simplify(d['V2']))}")
    P(f"   torsion tensor nonzero: {d['Tnonzero']} ; axial (totally antisymmetric) part nonzero: {d['Snonzero']}")

open(__file__.replace('.py', '.out.txt'), 'w').write("\n".join(out) + "\n")
