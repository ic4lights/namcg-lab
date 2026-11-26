"""
s1_exact_structure.py  (proposal 047)  --  prints to stdout only; writes nothing.

Exact algebra of the background operators of the conjugate-coordinate class, polynomial Lie-Poisson algebra so(4,2),
T^a = M^{a4}, y^mu = M^{mu5}, m = M^{45}, D^a = {T^a,.}, J^{AB} = {M^{AB},.}, Box = eta_ab D^a D^b, both bracket signs.

(E1) F^{ab} = {T^a,T^b} = c M^{ab} with c = +-1, so the flux operator of the background is c J^{ab}.
(E2) [Box, J^{ab}] = 0 on test polynomials, hence e^{s Box} commutes with every species' Zeeman term.
(E3) For the vector and the Dirac index, with Sigma_V, Sigma_D of s3 of proposal 046, kappa = -1:
     H_i^0 := -Box + kappa Sigma_i^{ab} Zbar_ab  equals  C_31^{tot,i} - C_41 - C_{Sigma_i}, tested on random
     polynomial index-valued functions; the sign of the index action in C^{tot} is reported.
(E4) On functions of y: Tbar^{ab mu} = {F^{ab}, y^mu} = eta^{a mu} y^b - eta^{b mu} y^a.
Chart statements (exact symbolic, m^2 = -y.y - l^2, rho = 1/m, frame E^{a mu} = m eta^{a mu}):
(C1) rho-divergence of the frame and of Tbar vanish; Tbar^{ab mu} = +-[E^a, E^b]^mu  (Lie bracket).
(C2) Tbar_{ab mu} is +- the Levi-Civita spin connection of G_{mu nu} = eta/m^2 in the frame E.
(C3) Scalar coefficient: e = R/6 - Box_G phi - |d phi|^2, phi = (1/2) ln(rho/sqrt|G|), sqrt|G| e = (5m^2-3l^2)/(4m^6),
     the value stated in Appendix H; at y^i = 0 in units of Box: e/m^... = 2 - (3/4) coth^2 tau (see output).
(C4) Lichnerowicz identity on the background: index density (1/4) G tr_D Zbar Zbar = -R + 4 Box_G phi + 4 |d phi|^2.
"""
import sys
sys.dont_write_bytecode = True
import sympy as sp, itertools, random
from sympy.physics.quantum import TensorProduct as TP
random.seed(47)

syms = {(A, B): sp.Symbol('M%d%d' % (A, B)) for A in range(6) for B in range(A + 1, 6)}
def Ms(A, B):
    if A == B: return sp.Integer(0)
    return syms[(A, B)] if A < B else -syms[(B, A)]
eta6 = [-1, 1, 1, 1, 1, -1]
pairs = sorted(syms)
def struct(sb):
    e = lambda X, Y: eta6[X] if X == Y else 0
    return {(p1, p2): sb * (e(p1[0], p2[0]) * Ms(p1[1], p2[1]) - e(p1[0], p2[1]) * Ms(p1[1], p2[0])
                            - e(p1[1], p2[0]) * Ms(p1[0], p2[1]) + e(p1[1], p2[1]) * Ms(p1[0], p2[0]))
            for p1 in pairs for p2 in pairs}
def br(f, g, ST):
    df = {p: sp.diff(f, syms[p]) for p in pairs}; dg = {p: sp.diff(g, syms[p]) for p in pairs}
    tot = 0
    for p1 in pairs:
        if df[p1] == 0: continue
        for p2 in pairs:
            if dg[p2] == 0: continue
            st = ST[(p1, p2)]
            if st != 0: tot += df[p1] * dg[p2] * st
    return sp.expand(tot)
eta4 = [-1, 1, 1, 1]
def Box(f, ST):
    return sp.expand(sum(eta4[a] * br(Ms(a, 4), br(Ms(a, 4), f, ST), ST) for a in range(4)))
def rand_poly():
    vs = [syms[p] for p in pairs]
    return sum(random.randint(-3, 3) * random.choice(vs) * random.choice(vs) for _ in range(3)) + random.randint(-3, 3) * random.choice(vs)
def Jop(A, B, f, ST): return br(Ms(A, B), f, ST)
def C41(f, ST):
    tot = 0
    for A in range(5):
        for B in range(5):
            if A != B: tot += eta6[A] * eta6[B] * Jop(A, B, Jop(A, B, f, ST), ST)
    return sp.expand(tot / 2)
def C31(f, ST):
    tot = 0
    for a in range(4):
        for b in range(4):
            if a != b: tot += eta4[a] * eta4[b] * Jop(a, b, Jop(a, b, f, ST), ST)
    return sp.expand(tot / 2)

I2 = sp.eye(2); sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -sp.I], [sp.I, 0]]); sz = sp.Matrix([[1, 0], [0, -1]])
gE = [TP(sx, I2), TP(sy, I2), TP(sz, sx), TP(sz, sy)]
Gam = [sp.I * gE[0], gE[1], gE[2], gE[3]]
def SigD(a, b): return (Gam[a] * Gam[b] - Gam[b] * Gam[a]) / 4
def SigV(a, b):
    M = sp.zeros(4, 4)
    for c_ in range(4):
        for d in range(4):
            M[c_, d] = (eta4[a] if a == c_ else 0) * (1 if b == d else 0) - (eta4[b] if b == c_ else 0) * (1 if a == d else 0)
    return M

print("(E) polynomial Lie-Poisson identities")
for sb in (1, -1):
    ST = struct(sb)
    cvals = set()
    for a in range(4):
        for b in range(a + 1, 4):
            cvals.add(sp.simplify(br(Ms(a, 4), Ms(b, 4), ST) / Ms(a, b)))
    print("  bracket %+d: {T^a,T^b} = c M^{ab}, c values %s" % (sb, sorted(cvals, key=str)))
    c = list(cvals)[0]
    okT = True
    for a, b, mu in itertools.product(range(4), repeat=3):
        lhs = br(c * Ms(a, b), Ms(mu, 5), ST)
        rhs = (eta4[a] if a == mu else 0) * Ms(b, 5) - (eta4[b] if b == mu else 0) * Ms(a, 5)
        okT &= sp.expand(lhs - rhs) == 0
    okTm = True
    for a, b, mu in itertools.product(range(4), repeat=3):
        lhs = br(c * Ms(a, b), Ms(mu, 5), ST)
        rhs = -(eta4[a] if a == mu else 0) * Ms(b, 5) + (eta4[b] if b == mu else 0) * Ms(a, 5)
        okTm &= sp.expand(lhs - rhs) == 0
    print("     (E4) {F^{ab},y^mu} = +(eta^{a mu} y^b - eta^{b mu} y^a): %s; = -(...): %s" % (okT, okTm))
    ok2 = True
    for k in range(3):
        f = rand_poly()
        for (a, b) in [(0, 1), (1, 2), (2, 3)]:
            ok2 &= sp.expand(Box(Jop(a, b, f, ST), ST) - Jop(a, b, Box(f, ST), ST)) == 0
    print("     (E2) [Box, J^{ab}] = 0 on 3 random polynomials, 3 generators: %s" % ok2)
    f = rand_poly()
    print("     Box = C41 - C31 on a random polynomial: %s" % (sp.expand(Box(f, ST) - C41(f, ST) + C31(f, ST)) == 0))
    for name, Sg in (('V', SigV), ('D', SigD)):
        dim = 4
        psi = sp.Matrix([rand_poly() for _ in range(dim)])
        def Jv(a, b, v): return v.applyfunc(lambda g: Jop(a, b, g, ST))
        Zee = sp.zeros(dim, 1)
        for a in range(4):
            for b in range(4):
                if a != b:
                    Zee += -1 * Sg(a, b) * (c * eta4[a] * eta4[b] * Jv(a, b, psi))
        Zee = Zee.applyfunc(sp.expand)
        H0 = (-psi.applyfunc(lambda g: Box(g, ST))) + Zee
        CS = sp.zeros(dim, dim)
        for a in range(4):
            for b in range(4):
                if a != b: CS += eta4[a] * eta4[b] * Sg(a, b) * Sg(a, b)
        CS = (CS / 2).applyfunc(sp.simplify)
        results = {}
        for rho in (1, -1):
            tot = sp.zeros(dim, 1)
            for a in range(4):
                for b in range(4):
                    if a == b: continue
                    Gv = lambda w: Jv(a, b, w) + rho * Sg(a, b) * w
                    tot += eta4[a] * eta4[b] * Gv(Gv(psi))
            Ctot = (tot / 2).applyfunc(sp.expand)
            rhs = Ctot - psi.applyfunc(lambda g: C41(g, ST)) - CS * psi
            results[rho] = all(v == 0 for v in (H0 - rhs).applyfunc(sp.expand))
        print("     (E3) species %s: C_Sigma = %s x identity (is scalar: %s); H^0 = C31tot - C41 - C_Sigma with index sign +1: %s, -1: %s"
              % (name, CS[0, 0], CS == CS[0, 0] * sp.eye(dim), results[1], results[-1]))

print("\n(C) chart statements, symbolic in y^mu, l")
Y = sp.symbols('y0:4', real=True); l = sp.Symbol('l', positive=True)
etaM = sp.diag(-1, 1, 1, 1)
yl = etaM * sp.Matrix(Y)
yy = sum(Y[i] * yl[i] for i in range(4))
m2 = -yy - l ** 2
m = sp.sqrt(m2)
Eup = [[m * etaM[a, mu] for mu in range(4)] for a in range(4)]
rho = 1 / m
Tbar = [[[etaM[a, mu] * Y[b] - etaM[b, mu] * Y[a] for mu in range(4)] for b in range(4)] for a in range(4)]
okdiv = all(sp.simplify(sum(sp.diff(rho * Eup[a][mu], Y[mu]) for mu in range(4))) == 0 for a in range(4))
okdivT = all(sp.simplify(sum(sp.diff(rho * Tbar[a][b][mu], Y[mu]) for mu in range(4))) == 0 for a in range(4) for b in range(4))
def lie(a, b, mu):
    return sum(Eup[a][nu] * sp.diff(Eup[b][mu], Y[nu]) - Eup[b][nu] * sp.diff(Eup[a][mu], Y[nu]) for nu in range(4))
oklie = all(sp.simplify(lie(a, b, mu) - Tbar[a][b][mu]) == 0 for a in range(4) for b in range(4) for mu in range(4))
oklie2 = all(sp.simplify(lie(a, b, mu) + Tbar[a][b][mu]) == 0 for a in range(4) for b in range(4) for mu in range(4))
print("  (C1) rho-divergence of E^a vanishes: %s; of Tbar^{ab}: %s; [E^a,E^b] = +Tbar: %s, = -Tbar: %s" % (okdiv, okdivT, oklie, oklie2))

G = etaM / m2; Gi = etaM * m2
Gam_ = [[[sum(Gi[l_, s] * (sp.diff(G[s, n], Y[k]) + sp.diff(G[s, k], Y[n]) - sp.diff(G[k, n], Y[s])) for s in range(4)) / 2
          for n in range(4)] for k in range(4)] for l_ in range(4)]
def omega(mu, a, b):
    # omega_mu^a_b = e^a_nu (d_mu E_b^nu + Gamma^nu_{mu rho} E_b^rho), E_b^nu = m delta_b^nu, e^a_nu = delta^a_nu / m
    t = (sp.diff(m, Y[mu]) if a == b else 0) + Gam_[a][mu][b] * m
    return t / m
okom = {}
for sgn in (1, -1):
    okom[sgn] = True
    for mu in range(4):
        for a in range(4):
            for b in range(4):
                om_up = omega(mu, a, b) * etaM[b, b]
                Tl = sum(G[mu, nu] * Tbar[a][b][nu] for nu in range(4))
                if sp.simplify(om_up - sgn * Tl) != 0: okom[sgn] = False
print("  (C2) omega_LC mu^{ab} = + G_{mu nu} Tbar^{ab nu}: %s ; = - G_{mu nu} Tbar^{ab nu}: %s" % (okom[1], okom[-1]))

R_ = 0
for mu in range(4):
    for nu in range(4):
        t = 0
        for l_ in range(4):
            t += sp.diff(Gam_[l_][mu][nu], Y[l_]) - sp.diff(Gam_[l_][mu][l_], Y[nu])
            for s in range(4):
                t += Gam_[l_][l_][s] * Gam_[s][mu][nu] - Gam_[l_][nu][s] * Gam_[s][mu][l_]
        R_ += Gi[mu, nu] * t
sqrtG = 1 / m2 ** 2
phi = sp.log(rho / sqrtG) / 2
dphi = [sp.diff(phi, Y[i]) for i in range(4)]
boxphi = sum(sp.diff(sqrtG * Gi[i, j] * dphi[j], Y[i]) for i in range(4) for j in range(4)) / sqrtG
dphi2 = sum(Gi[i, j] * dphi[i] * dphi[j] for i in range(4) for j in range(4))
e = R_ / 6 - boxphi - dphi2
closed = (5 * m2 - 3 * l ** 2) / (4 * m2 ** 3)
test_pts = [{Y[0]: sp.Rational(5), Y[1]: 0, Y[2]: 0, Y[3]: 0, l: 4},
            {Y[0]: sp.Rational(13), Y[1]: sp.Rational(3), Y[2]: sp.Rational(-2), Y[3]: sp.Rational(1), l: 5},
            {Y[0]: sp.Rational(7), Y[1]: sp.Rational(1), Y[2]: sp.Rational(1, 2), Y[3]: sp.Rational(-1, 3), l: 3}]
print("  (C3) sqrt|G| e - (5m^2-3l^2)/(4m^6) at 3 rational points:", [sp.nsimplify(sp.simplify((sqrtG * e - closed).subs(p))) for p in test_pts])
for p, lab in ((test_pts[0], '(y0,l)=(5,4), m=3'),):
    ev = sp.nsimplify(sp.simplify(e.subs(p)))
    print("       e at %s: %s ; 2 - (3/4) coth^2 tau = %s" % (lab, ev, sp.Rational(2) - sp.Rational(3, 4) * sp.Rational(25, 9)))

SD = {(a, b): SigD(a, b) for a in range(4) for b in range(4)}
def Zmu(mu):
    tot = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            if a != b:
                tot += -sp.I * SD[(a, b)] * (etaM[a, a] * etaM[b, b] * Tbar[a][b][mu])
    return tot
Zs = [Zmu(mu) for mu in range(4)]
idx = sum(G[i, j] * (Zs[i] * Zs[j]).trace() for i in range(4) for j in range(4)) / 4
identity = idx - (-R_ + 4 * boxphi + 4 * dphi2)
print("  (C4) (1/4) G tr_D Z Z + R - 4 Box phi - 4 |d phi|^2 at 3 rational points:", [sp.nsimplify(sp.simplify(identity.subs(p))) for p in test_pts])
