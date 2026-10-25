"""s7: exact Casimir structure of the Zeeman-dressed vector operator in the conjugate-coordinate class (Lie-Poisson algebra so(4,2)).

Setting (appH, paragraph 'Conjugate-coordinate class: the Theta-built heat kernel ...'): functions on the coadjoint orbit are polynomials in M^{AB};
{M^{AB}, M^{CD}} = eta^{BC} M^{AD} - eta^{AC} M^{BD} - eta^{BD} M^{AC} + eta^{AD} M^{BC},  eta_6 = diag(-,+,+,+,+,-).
T^a = M^{a4}, D^a = {T^a, .}, J^{AB} = {M^{AB}, .}, F_{ab} = {T_a, T_b}, Box = eta_{ab} D^a D^b.
Vector operator (massless part):  (H eps)_a = -Box eps_a - 2 {F_{ab}, eps^b}.

Tests (exact polynomial arithmetic, sympy):
  (1) Box = C41 - C31 with C41 = 1/2 J^{AB}J_{AB} (A,B<=4, eta_5 = diag(-,+,+,+,+)), C31 = 1/2 J^{ab}J_{ab}.
  (2) with Sigma^{ab} the generators of the vector representation normalised by [J^{ab}, J^{cd}] (same structure constants), the operator
      H + kappa_s * (Zeeman) is a total-spin Casimir:  H = -C41 + C31_tot - C_V   for the sign/normalisation fixed by the data;
      the script solves for the constants (alpha, beta, gamma) in  H = alpha*(-C41) + beta*C31_tot + gamma  on random vector-valued polynomials.
"""
import itertools, random
import sympy as sp

eta6 = [-1, 1, 1, 1, 1, -1]
idx = [(A, B) for A in range(6) for B in range(A+1, 6)]
M = {}
for (A, B) in idx:
    M[(A, B)] = sp.Symbol(f'M{A}{B}')


def Mf(A, B):
    if A == B: return sp.Integer(0)
    if A < B: return M[(A, B)]
    return -M[(B, A)]


def Mup(A, B):
    return Mf(A, B)   # components M^{AB} (upper) used as the symbols


def eta(A, B):
    return eta6[A] if A == B else 0


def PB_gen(A, B, C, Dd):
    """{M^{AB}, M^{CD}} = eta^{BC} M^{AD} - eta^{AC} M^{BD} - eta^{BD} M^{AC} + eta^{AD} M^{BC}"""
    return (eta(B, C)*Mup(A, Dd) - eta(A, C)*Mup(B, Dd) - eta(B, Dd)*Mup(A, C) + eta(A, Dd)*Mup(B, C))


def Jop(A, B, f):
    """J^{AB} f = {M^{AB}, f} = sum_{CD} dM^{AB}/... : {M^{AB}, f} = sum_{C<D} {M^{AB},M^{CD}} df/dM^{CD}"""
    if A == B: return sp.Integer(0)
    s = sp.Integer(0)
    for (C, Dd) in idx:
        s += PB_gen(A, B, C, Dd)*sp.diff(f, M[(C, Dd)])
    return sp.expand(s)


def low(A):  # eta_{AA}
    return eta6[A]


def Dop(a, f):          # D^a = J^{a4}
    return Jop(a, 4, f)


def Box(f):
    return sp.expand(sum(low(a)*Dop(a, Dop(a, f)) for a in range(4)))


def C41(f):
    s = 0
    for A in range(5):
        for B in range(5):
            if A == B: continue
            s += sp.Rational(1, 2)*low(A)*low(B)*Jop(A, B, Jop(A, B, f))
    return sp.expand(s)


def C31(f):
    s = 0
    for A in range(4):
        for B in range(4):
            if A == B: continue
            s += sp.Rational(1, 2)*low(A)*low(B)*Jop(A, B, Jop(A, B, f))
    return sp.expand(s)


random.seed(4)
def randpoly(deg=3, nterms=6):
    f = 0
    gens = list(M.values())
    for _ in range(nterms):
        mon = 1
        for _ in range(random.randint(1, deg)):
            mon *= random.choice(gens)
        f += random.randint(-3, 3)*mon
    return sp.expand(f)


print('test (1): Box - (C41 - C31) on random polynomials')
for t in range(3):
    f = randpoly()
    print('   residual:', sp.expand(Box(f) - (C41(f) - C31(f))))

# vector representation: (Sigma^{ab} eps)^c = eta^{b c} delta... ; use matrices (Sigma^{ab})^c_d = eta^{ac}... choose such that
# [J^{ab}, J^{cd}] acts like the Lie-Poisson bracket: J^{AB} acts on functions as {M^{AB}, .}; for vector fields eps^c we need
# the representation matrices R^{ab} with the same commutation relations as the operators J^{ab}:
#   [J^{AB}, J^{CD}] f = {{M^{AB}, M^{CD}}, f}-type relation. Build R^{ab} by requiring the Lorentz invariance of  eps^a eta_{ab} eps'^b  under J_tot = J + R:
def vec_R(a, b):
    """matrix (R^{ab})^c_d acting on eps^d:  (R^{ab} eps)^c = eta^{bc} delta^a_d eps^d * s - (a<->b), sign s fixed below"""
    R = sp.zeros(4, 4)
    for c in range(4):
        for d in range(4):
            R[c, d] = (eta(b, c) if d == a else 0) - (eta(a, c) if d == b else 0)
    return R


def Jtot(a, b, eps, sgn):
    out = []
    Rm = vec_R(a, b)
    for c in range(4):
        v = Jop(a, b, eps[c]) + sgn*sum(Rm[c, d]*eps[d] for d in range(4))
        out.append(sp.expand(v))
    return out


def F_ab(a, b):         # F_{ab} = {T_a, T_b} with lowered indices: T_a = eta_{aa} T^a, {T^a,T^b} = {M^{a4},M^{b4}}
    return low(a)*low(b)*PB_gen(a, 4, b, 4)


def Hvec(eps, zee):
    """(H eps)_a = -Box eps_a + zee * 2 {F_{ab}, eps^b};  eps given with UPPER index components eps^c; returns lowered components a"""
    out = []
    for a in range(4):
        z = 0
        for b in range(4):
            Fab = F_ab(a, b)
            z += sum(low(0)*0 for _ in [0])
            # {F_ab, eps^b} = sum_{C<D} dF_ab/dM^{CD} {M^{CD}, eps^b}  -> use J: {F, g} = sum dF/dM^{CD} J^{CD} g
            br = sum(sp.diff(Fab, M[(C, Dd)])*Jop(C, Dd, eps[b]) for (C, Dd) in idx)
            z += br
        out.append(sp.expand(-low(a)*Box(eps[a]) + zee*2*z))
    return out


def invariance_defect(eps, sgn, zee):
    """check [H, J_tot^{ab}] = 0 for a few (a,b)"""
    worst = 0
    for (a, b) in [(0, 1), (1, 2), (0, 3)]:
        He = Hvec(eps, zee)
        # lowered -> upper components: eps^c = eta^{cc} eps_c
        He_up = [low(c)*He[c] for c in range(4)]
        JHe = Jtot(a, b, He_up, sgn)
        Je = Jtot(a, b, eps, sgn)
        HJe = Hvec(Je, zee); HJe_up = [low(c)*HJe[c] for c in range(4)]
        d = [sp.expand(JHe[c] - HJe_up[c]) for c in range(4)]
        worst = max(worst, max(len(str(x)) for x in d) if any(x != 0 for x in d) else 0)
        if any(x != 0 for x in d):
            return (a, b), d[:1]
    return 'invariant'


eps = [randpoly(2, 3) for _ in range(4)]
for sgn in (1, -1):
    for zee in (1, -1):
        print(f'test (2a): [H, J_tot] = 0 ?  sign of R: {sgn:+d}, Zeeman sign {zee:+d}:', invariance_defect(eps, sgn, zee))


def C31_tot(eps, sgn=-1):
    """C31_tot eps = 1/2 sum_{a!=b} eta_aa eta_bb J_tot^{ab} J_tot^{ab} eps"""
    out = [0]*4
    for a in range(4):
        for b in range(4):
            if a == b: continue
            inner = Jtot(a, b, eps, sgn)
            outer = Jtot(a, b, inner, sgn)
            for c in range(4):
                out[c] += sp.Rational(1, 2)*low(a)*low(b)*outer[c]
    return [sp.expand(x) for x in out]


def CV_const(sgn=-1):
    """Casimir of the vector rep alone (matrix)"""
    S = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            if a == b: continue
            Rm = sgn*vec_R(a, b)
            S += sp.Rational(1, 2)*low(a)*low(b)*Rm*Rm
    return S


print('test (2b): fit  H eps = alpha*(-C41 eps) + beta*C31_tot eps + gamma*eps  (upper-index components), sgn(R) = -1')
CVm = CV_const()
print('   C_V (vector rep Casimir) =', CVm.tolist()[0][0], '* identity' if CVm == CVm[0, 0]*sp.eye(4) else CVm)
eps = [randpoly(2, 3) for _ in range(4)]
al, be, ga = sp.symbols('al be ga')
C41e = [C41(e) for e in eps]
C31t = C31_tot(eps)
for zee in (1, -1):
    He = Hvec(eps, zee)
    He_up = [low(c)*He[c] for c in range(4)]
    eqs = []
    for c in range(4):
        expr = sp.expand(He_up[c] - (al*(-C41e[c]) + be*C31t[c] + ga*eps[c]))
        poly = sp.Poly(expr, *M.values())
        eqs += list(poly.coeffs())
    sol = sp.solve(eqs, [al, be, ga], dict=True)
    print(f'   Zeeman sign {zee:+d}: solution', sol)
