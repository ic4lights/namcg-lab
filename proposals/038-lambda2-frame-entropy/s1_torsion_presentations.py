"""s1: algebra of the quadratic torsion scalars of the coframe e^A = omega_{mu A} (closed, antisymmetric omega)
and the R-coefficient of X = T_{lmn}T^{lmn} in each presentation.

Part A (algebraic, exact rationals): irreducible decomposition T = vector + axial + tensor in d=4, G=delta;
   TT = a_V V^2 + a_S S^2 + a_q q^2,  TEGR scalar  calT = TT/4 + TT'/2 - V^2 = t_V V^2 + t_S S^2 + t_q q^2.
Part B (differential, exact rationals at a random two-jet of a closed omega, Euclidean signature):
   (i)  V_mu = G^{lambda nu} T_{lambda mu nu} equals d_mu ln rho,
   (ii) R[G] = -calT - 2 nabla_mu V^mu,
   (iii) E_s = -1/2 Box ln rho + 1/4 |d ln rho|^2 equals R/4 + TT/16 + TT'/8,
   (iv) rho^2 X = -2 rho R[g_rho] - rho |d ln rho|^2_{g_rho} + 3/2 rho^2 S^2 + 2 d(g_rho^{mu nu} d_nu rho)
        checked through the conformal relation R_G = rho^{-1}[R[g_rho] - 3 Box_{g_rho} ln rho - 3/2 |grad ln rho|^2_{g_rho}].
"""
import itertools, random
import sympy as sp
from sympy import Rational as Q

random.seed(20261024)

# ---------------- Part A: algebra ----------------
d = 4
def rand_T():
    T = [[[sp.Integer(0)]*d for _ in range(d)] for _ in range(d)]
    for l in range(d):
        for m in range(d):
            for n in range(m+1, d):
                v = Q(random.randint(-9, 9), random.randint(1, 5))
                T[l][m][n] = v
                T[l][n][m] = -v
    return T

def contr_TT(T, U):
    return sum(T[l][m][n]*U[l][m][n] for l in range(d) for m in range(d) for n in range(d))
def contr_TTp(T, U):
    return sum(T[l][m][n]*U[m][l][n] for l in range(d) for m in range(d) for n in range(d))
def vec(T):
    return [sum(T[l][m][l] for l in range(d)) for m in range(d)]   # V_mu = T_{l mu l}
def axial(T):
    S = [[[sp.Integer(0)]*d for _ in range(d)] for _ in range(d)]
    for l in range(d):
        for m in range(d):
            for n in range(d):
                s = sp.Integer(0)
                for (a, b, c), sg in [((l, m, n), 1), ((m, n, l), 1), ((n, l, m), 1),
                                       ((m, l, n), -1), ((l, n, m), -1), ((n, m, l), -1)]:
                    s += sg*T[a][b][c]
                S[l][m][n] = s/6
    return S
def vecpart(V):
    # T^V_{lmn} = -(1/3)(delta_{lm} V_n - delta_{ln} V_m)  so that its trace T_{l m l} = V_m
    P = [[[sp.Integer(0)]*d for _ in range(d)] for _ in range(d)]
    for l in range(d):
        for m in range(d):
            for n in range(d):
                P[l][m][n] = -Q(1, 3)*((1 if l == m else 0)*V[n] - (1 if l == n else 0)*V[m])
    return P
def sub(A, B):
    return [[[A[l][m][n]-B[l][m][n] for n in range(d)] for m in range(d)] for l in range(d)]

rows = []
for _ in range(6):
    T = rand_T()
    V = vec(T); S = axial(T); Vp = vecpart(V)
    q = sub(sub(T, Vp), S)
    assert vec(Vp) == V and vec(S) == [0]*d and vec(q) == [0]*d
    V2 = sum(v*v for v in V); S2 = contr_TT(S, S); q2 = contr_TT(q, q)
    assert contr_TT(Vp, S) == 0 and contr_TT(Vp, q) == 0 and contr_TT(S, q) == 0
    TT = contr_TT(T, T); TTp = contr_TTp(T, T)
    calT = TT/4 + TTp/2 - V2
    rows.append((V2, S2, q2, TT, TTp, calT))

aV, aS, aq, tV, tS, tq, bV, bS, bq = sp.symbols('aV aS aq tV tS tq bV bS bq')
eqs_TT = [sp.Eq(aV*r[0]+aS*r[1]+aq*r[2], r[3]) for r in rows]
eqs_T = [sp.Eq(tV*r[0]+tS*r[1]+tq*r[2], r[5]) for r in rows]
eqs_TTp = [sp.Eq(bV*r[0]+bS*r[1]+bq*r[2], r[4]) for r in rows]
sol_TT = sp.solve(eqs_TT, [aV, aS, aq]); sol_T = sp.solve(eqs_T, [tV, tS, tq]); sol_TTp = sp.solve(eqs_TTp, [bV, bS, bq])
print("TT  =", sol_TT, " (V^2, S^2, q^2 coefficients)")
print("TT' =", sol_TTp)
print("calT=", sol_T)
a_V, a_S, a_q = sol_TT[aV], sol_TT[aS], sol_TT[aq]
t_V, t_S, t_q = sol_T[tV], sol_T[tS], sol_T[tq]

# R = -calT - 2 div V  =>  R-coefficient of X after eliminating one irreducible square
print("\nR-coefficient r of X = TT when one of {V^2,S^2,q^2} is eliminated using R = -calT - 2 div V:")
r_q = -a_q/t_q; r_S = -a_S/t_S; r_V = -a_V/t_V
print("  eliminate q^2 (keep R,V^2,S^2): r =", r_q, "; S^2 coefficient =", a_S - a_q*t_S/t_q, "; V^2 coefficient =", a_V - a_q*t_V/t_q)
print("  eliminate S^2 (keep R,V^2,q^2): r =", r_S)
print("  eliminate V^2 (keep R,S^2,q^2): r =", r_V)
print("  R-free presentation (keep V^2,S^2,q^2), TT itself: r = 0")

# ---------------- Part B: differential identities on a random 2-jet ----------------
x = sp.symbols('x1:5')
N = 2
def trunc(expr, n=N):
    expr = sp.expand(expr)
    if expr == 0:
        return sp.Integer(0)
    p = sp.Poly(expr, *x)
    return sum(c*sp.prod([xi**e for xi, e in zip(x, mon)]) for mon, c in p.terms() if sum(mon) <= n)
def mtrunc(M, n=N):
    return M.applyfunc(lambda e: trunc(e, n))
def rr(lo=-3, hi=3):
    return Q(random.randint(lo, hi), random.randint(1, 3))

def random_closed_omega():
    A = [0]*4
    for nu in range(4):
        e = 0
        for a in range(4):
            for b in range(a, 4):
                e += rr()*x[a]*x[b]
        for a in range(4):
            for b in range(a, 4):
                for c in range(b, 4):
                    e += rr()*x[a]*x[b]*x[c]/3
        A[nu] = e
    w = sp.zeros(4, 4)
    for m in range(4):
        for n in range(4):
            w[m, n] = sp.diff(A[n], x[m]) - sp.diff(A[m], x[n])
    w0 = sp.zeros(4, 4)
    while True:
        for m in range(4):
            for n in range(m+1, 4):
                v = rr(-4, 4)
                w0[m, n] = v; w0[n, m] = -v
        pf = w0[0, 1]*w0[2, 3] - w0[0, 2]*w0[1, 3] + w0[0, 3]*w0[1, 2]
        if pf != 0:
            break
    return (w + w0).applyfunc(sp.expand)

def inv_series(M, n=N):
    M0 = M.subs({xi: 0 for xi in x})
    M0i = M0.inv()
    dM = (M - M0).applyfunc(sp.expand)
    out = M0i
    term = M0i
    for _ in range(n):
        term = mtrunc(-term*dM*M0i, n)
        out = out + term
    return mtrunc(out, n)

def at0(e):
    return sp.nsimplify(sp.sympify(e).subs({xi: 0 for xi in x}))

def run_jet():
    w = random_closed_omega()
    E = w.copy()                      # E[mu, A] = omega_{mu A}  (e^A_mu = omega_{mu A})
    G = mtrunc(E*E.T)                 # G_{mu nu} = e^A_mu e^A_nu
    Gi = inv_series(G)
    pf = w[0, 1]*w[2, 3] - w[0, 2]*w[1, 3] + w[0, 3]*w[1, 2]
    pf = trunc(pf)
    rho = pf                          # rho = |Pf omega| up to a sign irrelevant for ln derivatives
    # Gamma
    dG = [[[sp.diff(G[a, b], x[c]) for c in range(4)] for b in range(4)] for a in range(4)]
    Gam = [[[trunc(sum(Gi[l, s]*(dG[s][n][m] + dG[s][m][n] - dG[m][n][s]) for s in range(4))/2, 1)
             for n in range(4)] for m in range(4)] for l in range(4)]   # Gam[l][m][n]
    def Riem_scalar():
        Ric = sp.zeros(4, 4)
        for s in range(4):
            for n in range(4):
                val = 0
                for r in range(4):
                    # R^r_{s r n} = d_r Gam^r_{n s} - d_n Gam^r_{r s} + Gam^r_{r l}Gam^l_{n s} - Gam^r_{n l}Gam^l_{r s}
                    val += sp.diff(Gam[r][n][s], x[r]) - sp.diff(Gam[r][r][s], x[n])
                    for l in range(4):
                        val += Gam[r][r][l]*Gam[l][n][s] - Gam[r][n][l]*Gam[l][r][s]
                Ric[s, n] = val
        return sum(Gi[s, n]*Ric[s, n] for s in range(4) for n in range(4))
    R = at0(Riem_scalar())
    G0i = Gi.subs({xi: 0 for xi in x})
    # ln rho derivatives at 0
    rho0 = rho.subs({xi: 0 for xi in x})
    dlr = [sp.diff(rho, x[m])/rho0 for m in range(4)]
    dlr0 = [at0(v) for v in dlr]
    ddlr = [[sp.diff(rho, x[m], x[n])/rho0 - sp.diff(rho, x[m])*sp.diff(rho, x[n])/rho0**2 for n in range(4)] for m in range(4)]
    ddlr0 = [[at0(ddlr[m][n]) for n in range(4)] for m in range(4)]
    Gam0 = [[[at0(Gam[l][m][n]) for n in range(4)] for m in range(4)] for l in range(4)]
    box = sum(G0i[m, n]*(ddlr0[m][n] - sum(Gam0[l][m][n]*dlr0[l] for l in range(4))) for m in range(4) for n in range(4))
    grad2 = sum(G0i[m, n]*dlr0[m]*dlr0[n] for m in range(4) for n in range(4))
    Es = -box/2 + grad2/4
    # torsion
    Tup = [[[sp.diff(E[n, A], x[m]) - sp.diff(E[m, A], x[n]) for n in range(4)] for m in range(4)] for A in range(4)]  # T^A_{mn}
    # T_{l m n} = e^A_l T^A_{mn}
    Tlmn = [[[sum(E[l, A]*Tup[A][m][n] for A in range(4)) for n in range(4)] for m in range(4)] for l in range(4)]
    def at0T(l, m, n):
        return at0(Tlmn[l][m][n])
    T0 = [[[at0T(l, m, n) for n in range(4)] for m in range(4)] for l in range(4)]
    # raise with G0i
    def raise_all(T):
        return [[[sum(G0i[l, a]*G0i[m, b]*G0i[n, c]*T[a][b][c] for a in range(4) for b in range(4) for c in range(4))
                  for n in range(4)] for m in range(4)] for l in range(4)]
    Tr = raise_all(T0)
    TT = sum(T0[l][m][n]*Tr[l][m][n] for l in range(4) for m in range(4) for n in range(4))
    TTp = sum(T0[l][m][n]*Tr[m][l][n] for l in range(4) for m in range(4) for n in range(4))
    # V_mu(x) = G^{l n}(x) T_{l mu n}(x), need value and derivative at 0
    Vx = [trunc(sum(Gi[l, n]*Tlmn[l][m][n] for l in range(4) for n in range(4)), 1) for m in range(4)]
    V0 = [at0(v) for v in Vx]
    divV = sum(G0i[m, n]*(at0(sp.diff(Vx[m], x[n])) - sum(Gam0[l][m][n]*V0[l] for l in range(4))) for m in range(4) for n in range(4))
    V2 = sum(G0i[m, n]*V0[m]*V0[n] for m in range(4) for n in range(4))
    calT = TT/4 + TTp/2 - V2
    ok_i = all(sp.simplify(V0[m] - dlr0[m]) == 0 for m in range(4))
    ok_ii = sp.simplify(R + calT + 2*divV) == 0
    ok_iii = sp.simplify(Es - (R/4 + TT/16 + TTp/8)) == 0
    # axial part S_{lmn} (indices down), S^2 with G0i
    S0 = [[[sum(sg*T0[a][b][c] for (a, b, c), sg in
                [((l, m, n), 1), ((m, n, l), 1), ((n, l, m), 1), ((m, l, n), -1), ((l, n, m), -1), ((n, m, l), -1)])/6
            for n in range(4)] for m in range(4)] for l in range(4)]
    Sr = raise_all(S0)
    S2 = sum(S0[l][m][n]*Sr[l][m][n] for l in range(4) for m in range(4) for n in range(4))
    # ledger identity (iv): with X = TT and rho^2 = sqrt(G)
    # sqrt(G) = rho^2 (check), g_rho = G/rho  (unimodular), conformal relation for R[g_rho]
    detG = G.subs({xi: 0 for xi in x}).det()
    ok_det = sp.simplify(detG - rho0**4) == 0
    # R[g_rho] from R_G = rho^{-1}[R[g_rho] - 3 Box_{g_rho} ln rho - 3/2 |grad ln rho|^2_{g_rho}]
    # Box_{g_rho} f and |.|^2_{g_rho}: g_rho = G/rho -> g_rho^{mu nu} = rho G^{mu nu}; Gamma_{g_rho} = Gamma_G + conformal shift
    # use the 4d conformal formulas directly: g_rho = e^{2w} G with e^{2w}=1/rho, w=-lnrho/2:
    #   Box_{g}f = e^{-2w}[Box_G f + 2 G^{mn} d_m w d_n f];  |df|^2_g = e^{-2w}|df|^2_G
    w_d = [-dlr0[m]/2 for m in range(4)]
    box_g = rho0*(box + 2*sum(G0i[m, n]*w_d[m]*dlr0[n] for m in range(4) for n in range(4)))
    grad2_g = rho0*grad2
    Rg = rho0*R + 3*box_g + sp.Rational(3, 2)*grad2_g          # from the quoted relation
    # LHS and RHS of the ledger identity (iv); total derivative term 2 d_mu(g_rho^{mu nu} d_nu rho) evaluated explicitly
    # g_rho^{mu nu}(x) = rho(x) G^{mu nu}(x) ; need d_mu of (rho G^{mu nu} d_nu rho) at 0
    div_term = 0
    for m in range(4):
        for n in range(4):
            div_term += sp.diff(trunc(rho*Gi[m, n], 1)*sp.diff(rho, x[n]), x[m])
    div_term = at0(2*div_term)
    lhs = rho0**2*TT
    rhs = -2*rho0*Rg - rho0*grad2_g*rho0**0 + sp.Rational(3, 2)*rho0**2*S2 + div_term
    # note |d ln rho|^2_{g_rho} multiplied by rho (the ledger writes rho g_rho^{mu nu} d ln rho d ln rho)
    rhs = -2*rho0*Rg - rho0*grad2_g + sp.Rational(3, 2)*rho0**2*S2 + div_term
    ok_iv = sp.simplify(lhs - rhs) == 0
    return dict(R=R, TT=TT, TTp=TTp, V2=V2, S2=S2, ok_V_is_dlnrho=ok_i, ok_R_identity=ok_ii, ok_Es_identity=ok_iii,
                ok_sqrtG=ok_det, ok_ledger_X_identity=ok_iv, resid_iv=sp.simplify(lhs-rhs))

print("\nPart B: random two-jets of a closed omega (Euclidean)")
for k in range(3):
    r = run_jet()
    print(" jet", k, {kk: (vv if not isinstance(vv, sp.Expr) else sp.nsimplify(vv)) for kk, vv in r.items()})
