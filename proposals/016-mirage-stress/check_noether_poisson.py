"""
Exact checks in the Lie-Poisson algebra of so(4,2) (polynomial ring in M^{AB}, no orbit constraint needed; the
identities below are consequences of the Jacobi identity and the Leibniz rule and hold for arbitrary functions X^a).
Notation: F^{ab}={X^a,X^b}, E_c = -{X^b,{X_b,X_c}} + mu2 X_c  (field equation of S = (1/4g^2) int [F_ab F^ab + 2 mu2 X_a X^a]).
 (N1) off-shell Noether identity  {X^a, E_a} = 0   for arbitrary polynomial X^a and any mu2.
 (N2) divergence of the eta-variation stress  T^{ab} = F^{ac}F^b_c + mu2 X^a X^b :
          {X_a, T^{ab}} = - F^b_c E^c + (1/4) {X^b, F_cd F^cd}
      and for the trace-subtracted stress  T~^{ab} = T^{ab} - (1/4) eta^{ab} F^2 :   {X_a, T~^{ab}} = - F^b_c E^c   (exact).
 (N3) linear level about X^a = T^a = M^{a4}:  D^a L(A)_a = -(3+mu2)... i.e. {T^a, L(A)_a} = -(3+mu2) {T^a, A_a}... checked as
          {T^a, L(A)_a} + (3+mu2) {A^a, T_a} = 0   for random A, any mu2   (zero for mu2 = -3).
Both sign conventions s=+1,-1 of the Lie-Poisson bracket.
"""
import sympy as sp, random, sys
eta6 = [-1, 1, 1, 1, 1, -1]
pairs = [(A, B) for A in range(6) for B in range(A+1, 6)]
Msym = {p: sp.Symbol('M%d%d' % p) for p in pairs}
def M(A, B):
    if A == B: return 0
    return Msym[(A, B)] if A < B else -Msym[(B, A)]
vars_ = [Msym[p] for p in pairs]
e4 = [-1, 1, 1, 1]

def run(s, seed):
    random.seed(seed)
    def lie(A, B, C, D):
        e = lambda X, Y: eta6[X] if X == Y else 0
        return s*(e(A, C)*M(B, D) - e(A, D)*M(B, C) - e(B, C)*M(A, D) + e(B, D)*M(A, C))
    brM = {(p, r): sp.expand(lie(p[0], p[1], r[0], r[1])) for p in pairs for r in pairs}
    def PB(f, g):
        f = sp.sympify(f); g = sp.sympify(g)
        df = {p: sp.diff(f, Msym[p]) for p in pairs}; dg = {p: sp.diff(g, Msym[p]) for p in pairs}
        out = 0
        for p in pairs:
            if df[p] == 0: continue
            for r in pairs:
                if dg[r] == 0: continue
                out += df[p]*dg[r]*brM[(p, r)]
        return sp.expand(out)
    def rpoly(nl=3, nq=2):
        t = sum(random.randint(-3, 3)*random.choice(vars_) for _ in range(nl))
        t += sum(random.randint(-2, 2)*random.choice(vars_)*random.choice(vars_) for _ in range(nq))
        return sp.expand(t)
    mu2 = sp.Symbol('mu2')
    # ---- (N1),(N2) for arbitrary polynomial X^a (upper index) ----
    X = [rpoly() for _ in range(4)]
    Xl = [e4[a]*X[a] for a in range(4)]
    F = [[PB(X[a], X[b]) for b in range(4)] for a in range(4)]            # F^{ab}
    Fl = [[e4[a]*e4[b]*F[a][b] for b in range(4)] for a in range(4)]       # F_{ab}
    # F^b_c = F^{bd} eta_{dc}
    Fmix = [[e4[c]*F[b][c] for c in range(4)] for b in range(4)]           # F^b_c
    J = [sum(e4[b]*PB(X[b], PB(X[b], X[c])) for b in range(4)) for c in range(4)]   # {X_b,{X^b,X^c}} (upper c)  (X_b {.} = eta_bb X^b)
    E = [sp.expand(-J[c] + mu2*X[c]) for c in range(4)]                    # E^c (upper)
    El = [e4[c]*E[c] for c in range(4)]
    # (N1)
    n1 = sp.expand(sum(PB(X[a], El[a]) for a in range(4)))
    print("s=%+d (N1) {X^a,E_a} = 0 off-shell, arbitrary X, symbolic mu2:" % s, n1 == 0)
    # (N2)
    F2 = sp.expand(sum(F[a][b]*Fl[a][b] for a in range(4) for b in range(4)))
    ok2 = True; ok2b = True
    for b in range(4):
        Tup = [sp.expand(sum(F[a][c]*Fmix[b][c] for c in range(4)) + mu2*X[a]*X[b]) for a in range(4)]       # T^{ab}, a running
        div = sp.expand(sum(PB(Xl[a], Tup[a]) for a in range(4)))
        rhs = sp.expand(-sum(Fmix[b][c]*E[c] for c in range(4)) + sp.Rational(1, 4)*PB(X[b], F2))
        ok2 = ok2 and sp.expand(div - rhs) == 0
        # trace-subtracted: T~^{ab} = T^{ab} - 1/4 eta^{ab} F2   -> {X_a, eta^{ab} F2} = {X^b,F2}
        div2 = sp.expand(div - sp.Rational(1, 4)*PB(X[b], F2))
        rhs2 = sp.expand(-sum(Fmix[b][c]*E[c] for c in range(4)))
        ok2b = ok2b and sp.expand(div2 - rhs2) == 0
    print("s=%+d (N2) {X_a,T^{ab}} = -F^b_c E^c + 1/4 {X^b,F^2}:" % s, ok2, "; trace-subtracted exact:", ok2b)
    # ---- (N3) linear identity about T^a = M^{a4}, A^a random ----
    T = [M(a, 4) for a in range(4)]; Tl = [e4[a]*T[a] for a in range(4)]
    A = [rpoly(3, 2) for _ in range(4)]; Al = [e4[a]*A[a] for a in range(4)]
    ok3 = True
    for mu2v in (-3, 0, 2):
        Lc = []
        for a in range(4):
            L = -sum(e4[b]*PB(T[b], PB(T[b], Al[a])) for b in range(4))
            L -= sum(PB(T[b], PB(Al[b], Tl[a])) for b in range(4))
            L -= sum(PB(A[b], PB(Tl[b], Tl[a])) for b in range(4))
            L += mu2v*Al[a]
            Lc.append(sp.expand(L))
        lhs = sp.expand(sum(PB(T[a], Lc[a]) for a in range(4)) + (3 + mu2v)*sum(PB(A[a], Tl[a]) for a in range(4)))
        div = sp.expand(sum(PB(T[a], Lc[a]) for a in range(4)))
        print("s=%+d (N3) mu2=%d: {T^a,L(A)_a} + (3+mu2){A^a,T_a} = 0:" % (s, mu2v), lhs == 0, "; {T^a,L(A)_a}==0:", div == 0)
for s in (1, -1):
    run(s, 5)
