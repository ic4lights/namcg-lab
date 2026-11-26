"""
Lie--Poisson algebra of so(4,2) on the polynomial ring in M^{AB} (no orbit constraint needed).
Checks (exact, sympy), for both sign conventions s = +1, -1:
 (1) {T_a,{T^a,T^b}} = -3 T^b          (background stationarity requires the bilinear coefficient mu^2 = -3/R^2, R=1)
 (2) linearised EOM operator  L(A)_a = -{T^b,{T_b,A_a}} - {T^b,{A_b,T_a}} - {A^b,{T_b,T_a}} + mu^2 A_a
     equals  -Box A_a + D_a (D.A) - 2 s J_{ab} A^b + mu^2 A_a ,  D^a = {T^a,.}, J_{ab} = {M_{ab},.}, Box = D_b D^b
     for random polynomial A^a (degree 2).
 (3) gauge zero mode: L({Lambda,T}) = 0 for random polynomial Lambda iff mu^2 = -3 (two-line proof by Jacobi; here an explicit check).
 (4) [D^a,D^b] = s J^{ab}.
Signature: eta4 = diag(-1,1,1,1) for a,b=0..3; eta6 = diag(-1,1,1,1,1,-1).
"""
import sympy as sp, itertools, random
eta6 = [-1, 1, 1, 1, 1, -1]
pairs = [(A, B) for A in range(6) for B in range(A+1, 6)]
Msym = {p: sp.Symbol('M%d%d' % p) for p in pairs}
def M(A, B):
    if A == B: return 0
    return Msym[(A, B)] if A < B else -Msym[(B, A)]
vars_ = [Msym[p] for p in pairs]
def run(s):
    def lie(A, B, C, D):
        e = lambda X, Y: eta6[X] if X == Y else 0
        return s*(e(A, C)*M(B, D) - e(A, D)*M(B, C) - e(B, C)*M(A, D) + e(B, D)*M(A, C))
    brM = {}
    for p in pairs:
        for r in pairs:
            brM[(p, r)] = sp.expand(lie(p[0], p[1], r[0], r[1]))
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
    e4 = [-1, 1, 1, 1]
    T = [M(a, 4) for a in range(4)]                     # T^a (upper index)
    Tl = [e4[a]*T[a] for a in range(4)]                  # T_a
    # (1)
    ok1 = True
    for b in range(4):
        tot = sum(e4[a]*PB(T[a], PB(T[a], T[b])) for a in range(4))   # {T_a,{T^a,T^b}} = sum_a eta_aa {T^a,{T^a,T^b}}
        ok1 = ok1 and sp.expand(tot + 3*T[b]) == 0
    print("s=%+d (1) Box T^b = -3 T^b:" % s, ok1)
    # (4)
    ok4 = True
    f = M(0, 5)*M(1, 2) + M(3, 4)**2
    for a, b in [(0, 1), (1, 2), (0, 3)]:
        lhs = PB(T[a], PB(T[b], f)) - PB(T[b], PB(T[a], f))
        rhs = s*PB(M(a, b), f)         # J^{ab} with upper indices: M^{ab}
        ok4 = ok4 and sp.expand(lhs - rhs) == 0
    print("s=%+d (4) [D^a,D^b] = s J^{ab}:" % s, ok4)
    random.seed(11)
    def rpoly(deg=2, n=4):
        mons = [sp.Mul(*random.sample(vars_, k)) for k in (1, 2) for _ in range(n)]
        return sum(random.randint(-3, 3)*m for m in mons)
    mu2 = -3
    A = [rpoly() for _ in range(4)]                      # A^a upper
    Al = [e4[a]*A[a] for a in range(4)]
    D = lambda a, f: PB(T[a], f)                        # D^a
    Dl = lambda a, f: e4[a]*PB(T[a], f)                 # D_a
    def Jl(a, b, f): return PB(e4[a]*e4[b]*M(a, b), f)  # J_{ab} f = {M_{ab}, f}
    Box = lambda f: sp.expand(sum(e4[b]*PB(T[b], PB(T[b], f)) for b in range(4)))
    # L(A)_a (lower index a)
    ok2 = True
    for a in range(4):
        L = 0
        L -= sum(e4[b]*PB(T[b], PB(T[b], Al[a])) for b in range(4))                 # -{T^b,{T_b,A_a}}
        L -= sum(PB(T[b], PB(Al[b], Tl[a])) for b in range(4))                      # -{T^b,{A_b,T_a}}
        L -= sum(PB(A[b], PB(Tl[b], Tl[a])) for b in range(4))                      # -{A^b,{T_b,T_a}}
        L += mu2*Al[a]
        L = sp.expand(L)
        divA = sum(Dl(b, A[b]) for b in range(4))                                  # D_b A^b
        R = -Box(Al[a]) + Dl(a, divA) - 2*s*sum(Jl(a, b, A[b]) for b in range(4)) + mu2*Al[a]
        ok2 = ok2 and sp.expand(L - sp.expand(R)) == 0
    print("s=%+d (2) L(A)_a = -Box A_a + D_a(D.A) - 2 s J_ab A^b + mu^2 A_a:" % s, ok2)
    # (3) gauge zero mode
    Lam = rpoly()
    Ag = [PB(Lam, T[a]) for a in range(4)]
    Agl = [e4[a]*Ag[a] for a in range(4)]
    for mu2v in (-3, 0, 1):
        ok3 = True
        for a in range(4):
            L = -sum(e4[b]*PB(T[b], PB(T[b], Agl[a])) for b in range(4))
            L -= sum(PB(T[b], PB(Agl[b], Tl[a])) for b in range(4))
            L -= sum(PB(Ag[b], PB(Tl[b], Tl[a])) for b in range(4))
            L += mu2v*Agl[a]
            ok3 = ok3 and sp.expand(L) == 0
        print("s=%+d (3) L({Lambda,T}) = 0 with mu^2 = %d:" % (s, mu2v), ok3)
for s in (1, -1):
    run(s)
