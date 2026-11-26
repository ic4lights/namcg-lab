"""
074 / s2.  Exact checks in the polynomial Lie-Poisson algebra of so(4,2), both signs s of the bracket.

Setting (conjugate-coordinate class, Poisson limit, units R=1): eta6 = diag(-1,1,1,1,1,-1),
{M^AB, M^CD} = s(eta^AC M^BD - eta^AD M^BC - eta^BC M^AD + eta^BD M^AC),
T^a = M^{a4} (a=0..3), D^a = {T^a, .}, Box = eta_ab D^a D^b, J_ab = {M_ab, .},
E_a(X) = -{X^b,{X_b,X_a}} + mu^2 X_a  (field equation of (4g^2)^{-1} Int (F_ab F^ab + 2 mu^2 X_a X^a)),
L(A)_a = linearisation of E at X = T  (the Hessian; S^(2) = (2g^2)^{-1} Int A.L(A)).

Checks:
 (a) E(T) = 0 exactly for mu^2 = -3;
 (b) L(A) = -Box A_a + D_a(D_b A^b) - 2 s J_ab A^b + mu^2 A_a  (the recorded form) for random polynomial A;
 (c) for constant kappa (A^a = kappa^a_b T^b): symmetric kappa gives L(kappa T) = -2 kappa T + 2 tr(kappa) T,
     antisymmetric kappa gives L(kappa T) = 0;
 (d) for a constant non-null u and P_u = u u^T eta/(u.u): L(P_u T) = 2 (1-P_u) T, L(T) = 6 T, and on the span
     {P_u T, (1-P_u) T} the matrix [[0,6],[2,4]] with eigenvalues 6 (kappa = 1) and -2 (kappa = 1-4P_u);
 (e) the one-component rescaling X = (1+eps P_u) T: F_ab F^ab + 2 mu^2 X.X depends on eps only through
     (1+eps)^2 (exact polynomial identity on the leaf, any u).
Run:  python -I s2_liepoisson_q0_hessian.py
"""
import itertools
import sympy as sp

eta6 = [-1, 1, 1, 1, 1, -1]
pairs = [(A, B) for A in range(6) for B in range(A + 1, 6)]
Msym = {p: sp.Symbol("M%d%d" % p) for p in pairs}
gens = list(Msym.values())


def M(A, B):
    if A == B:
        return sp.Integer(0)
    return Msym[(A, B)] if A < B else -Msym[(B, A)]


def make_bracket(s):
    table = {}
    for (A, B) in pairs:
        for (C, D) in pairs:
            val = 0
            if A == C: val += eta6[A] * M(B, D)
            if A == D: val -= eta6[A] * M(B, C)
            if B == C: val -= eta6[B] * M(A, D)
            if B == D: val += eta6[B] * M(A, C)
            table[(Msym[(A, B)], Msym[(C, D)])] = s * val

    def br(f, g):
        f = sp.expand(f); g = sp.expand(g)
        df = {x: sp.diff(f, x) for x in gens}
        dg = {x: sp.diff(g, x) for x in gens}
        out = 0
        for x in gens:
            if df[x] == 0: continue
            for y in gens:
                if dg[y] == 0: continue
                t = table[(x, y)]
                if t != 0:
                    out += df[x] * dg[y] * t
        return sp.expand(out)
    return br


eta4 = [-1, 1, 1, 1]
T = [M(a, 4) for a in range(4)]


def lower(v):
    return [eta4[a] * v[a] for a in range(4)]


def Efield(X, br, mu2):
    Xl = lower(X)
    out = []
    for a in range(4):
        e = mu2 * Xl[a]
        for b in range(4):
            e -= br(X[b], br(Xl[b], Xl[a]))
        out.append(sp.expand(e))
    return out  # lower index a


def Lrecorded(A, br, s, mu2):
    Al = lower(A)
    Tl = lower(T)
    divA = sum(br(T[b], Al[b]) for b in range(4))  # D_b A^b = {T_b, A^b} = {T^b, A_b}
    out = []
    for a in range(4):
        boxA = sum(eta4[b] * br(T[b], br(T[b], Al[a])) for b in range(4))
        val = -boxA + br(Tl[a], divA) + mu2 * Al[a]
        for b in range(4):
            Mab_low = eta4[a] * eta4[b] * M(a, b)
            val += -2 * s * br(Mab_low, A[b])
        out.append(sp.expand(val))
    return out


eps = sp.Symbol("eps")
mu2 = -3
for s in (1, -1):
    br = make_bracket(s)
    # (a)
    E0 = Efield(T, br, mu2)
    print(f"s={s}: (a) E(T) = 0 for mu^2=-3:", all(e == 0 for e in E0))
    assert all(e == 0 for e in E0)
    # (b) random polynomial A (quadratic in the generators)
    import random
    random.seed(3 + s)
    A = [sum(random.randint(-2, 2) * gens[random.randrange(15)] * gens[random.randrange(15)] for _ in range(3))
         + random.randint(-2, 2) * gens[random.randrange(15)] for _ in range(4)]
    lin = Efield([T[a] + eps * A[a] for a in range(4)], br, mu2)
    Lin = [sp.expand(sp.diff(e, eps).subs(eps, 0)) for e in lin]
    Lrec = Lrecorded(A, br, s, mu2)
    okb = all(sp.expand(Lin[a] - Lrec[a]) == 0 for a in range(4))
    print(f"s={s}: (b) linearised field equation = recorded L(A):", okb)
    assert okb
    # (c) constant kappa
    k = sp.Matrix(4, 4, lambda i, j: sp.Symbol("k%d%d" % (i, j)))
    G = sp.diag(*eta4)
    ks = sp.Matrix(4, 4, lambda i, j: sp.Symbol("ks%d%d" % (min(i, j), max(i, j))))  # symmetric kappa_{ab}
    kup = G * ks  # kappa^a_b = eta^ac kappa_cb
    A = [sp.expand(sum(kup[a, b] * T[b] for b in range(4))) for a in range(4)]
    LA = Lrecorded(A, br, s, mu2)  # lower index
    tr = sum(kup[a, a] for a in range(4))
    target = [sp.expand(eta4[a] * (-2 * A[a] + 2 * tr * T[a])) for a in range(4)]
    okc1 = all(sp.expand(LA[a] - target[a]) == 0 for a in range(4))
    ka = sp.Matrix(4, 4, lambda i, j: 0 if i == j else (sp.Symbol("ka%d%d" % (min(i, j), max(i, j))) * (1 if i < j else -1)))
    kupa = G * ka
    Aa = [sp.expand(sum(kupa[a, b] * T[b] for b in range(4))) for a in range(4)]
    LAa = Lrecorded(Aa, br, s, mu2)
    okc2 = all(e == 0 for e in LAa)
    print(f"s={s}: (c) symmetric kappa: L(kappa T) = -2 kappa T + 2 tr(kappa) T: {okc1}; antisymmetric kappa: L = 0: {okc2}")
    assert okc1 and okc2
    # (d) rank-one projector along a symbolic constant u
    u = sp.symbols("u0:4")
    uu = sum(eta4[a] * u[a] ** 2 for a in range(4))
    P = sp.Matrix(4, 4, lambda a, b: u[a] * eta4[b] * u[b] / uu)  # P^a_b
    PT = [sp.together(sum(P[a, b] * T[b] for b in range(4))) for a in range(4)]
    LPT = Lrecorded([sp.expand(x * uu) for x in PT], br, s, mu2)  # times uu to stay polynomial
    LPT = [sp.expand(x / uu) for x in LPT]
    target = [sp.simplify(eta4[a] * 2 * (T[a] - PT[a])) for a in range(4)]
    okd1 = all(sp.simplify(LPT[a] - target[a]) == 0 for a in range(4))
    LT = Lrecorded(T, br, s, mu2)
    okd2 = all(sp.expand(LT[a] - 6 * eta4[a] * T[a]) == 0 for a in range(4))
    Mspan = sp.Matrix([[0, 6], [2, 4]])  # columns: L(P T) = 0 P T + 2 (1-P) T ; L((1-P) T) = 6 P T + 4 (1-P) T
    print(f"s={s}: (d) L(P_u T) = 2(1-P_u)T: {okd1}; L(T) = 6T: {okd2}; span matrix eigenvalues {Mspan.eigenvals()}")
    assert okd1 and okd2 and Mspan.eigenvals() == {6: 1, -2: 1}
    # (e) one-component rescaling: density depends on eps only through (1+eps)^2
    Lam = sp.eye(4) + eps * P
    X = [sp.together(sum(Lam[a, b] * T[b] for b in range(4))) for a in range(4)]
    Xn = [sp.expand(x * uu) for x in X]  # uu*X, polynomial
    Xl = lower(Xn)
    FF = sum(br(Xl[a], Xl[b]) * br(Xn[a], Xn[b]) for a in range(4) for b in range(4))
    XX = sum(Xl[a] * Xn[a] for a in range(4))
    dens = sp.expand(FF / uu**4 + 2 * mu2 * XX / uu**2)
    d0 = dens.subs(eps, 0)
    poly = sp.Poly(sp.expand((dens - d0) * uu**4), eps)
    c = poly.all_coeffs()[::-1]  # c[0]=eps^0 ...
    c = c + [0] * (5 - len(c))
    oke = sp.expand(c[0]) == 0 and sp.expand(c[2] - c[1] / 2) == 0 and sp.expand(c[3]) == 0 and sp.expand(c[4]) == 0
    print(f"s={s}: (e) density along X=(1+eps P_u)T = d0 + ((1+eps)^2-1) * d_u exactly: {oke}")
    assert oke
print("all exact checks passed")
