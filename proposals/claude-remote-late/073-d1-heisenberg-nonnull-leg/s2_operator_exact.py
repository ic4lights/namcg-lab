"""S2 (exact, sympy).  Operator-level check on the bundle, following the construction of the gatekeeper's
071 r2 script (proposals/071-.../gk071r2_exact.py), re-written here for a general constant connection:
  D_a = u_a^b (E_b - u_f^g om_b^c_g d/du_f^c) + t_a,  om_b = -w_b (normalisation of 071), t_a = (1/2) divergence
in the measure dy dHaar(u), on time x Heisenberg with E_1 = d_1 + (kappa/2) y^3 d_2, E_3 = d_3 - (kappa/2) y^1 d_2.
For the connection of common073.family at exact parameter points, with symbolic kappa and symbolic y and an exact
rational Lorentz u (Cayley transform), it checks
  (1) [S_cd, D_a] = eta_ad D_c - eta_ac D_d;
  (2) the matrix equation [D^a, [D_a, D_b]] = 0, all components including the order-zero (multiplication) part;
  (3) the section values T, R and F read off at u = 1 agree with the formulas of S1 (T = tau k-trace, F_13).
Points: U2 (s = 0, chi = 0, th = 1, al = 3/5, be = 0, ga = 4/5, zeta = 1/2, x = -1/3; tau = 7/5) and
        T1 (s = 3/5, chi = 0, th = 1, al = -1/sqrt2, be = 0, ga = 1/sqrt2, zeta = 1/2, x = -1/3; tau = 0).
Run: python -I -B s2_operator_exact.py   (a few minutes)"""
import itertools, time
import sympy as sp

t0 = time.time()
eta = sp.diag(-1, 1, 1, 1); r4 = range(4)
y = sp.symbols('y0:4'); U = sp.Matrix(4, 4, lambda i, j: sp.Symbol('u%d%d' % (i, j))); coords = list(y) + list(U)
kap = sp.Symbol('kappa', positive=True)


class VF:
    def __init__(s, c, f=0):
        s.c = [sp.sympify(t) for t in c]; s.f = sp.sympify(f)

    def act(s, g):
        return sp.expand(sum(s.c[i] * sp.diff(g, coords[i]) for i in range(20)))


def comm(A, Bv):
    return VF([A.act(Bv.c[i]) - Bv.act(A.c[i]) for i in range(20)], A.act(Bv.f) - Bv.act(A.f))


def lin(ts):
    return VF([sp.expand(sum(c * t.c[i] for c, t in ts)) for i in range(20)], sp.expand(sum(c * t.f for c, t in ts)))


def wedge(u, v):
    return sp.Matrix(4, 4, lambda c, d: u[c] * v[d] - u[d] * v[c])


def connection(s, chi, th, zeta, x, al, be, ga):
    c = sp.sqrt(1 - s ** 2)
    n = [1, s, -c, 0]; e = [0, c, s, 0]; f = [0, 0, 0, 1]; mnh = [0, -s, c, 0]; e0 = [1, 0, 0, 0]
    low = lambda v: [sum(eta[a, b] * v[b] for b in r4) for a in r4]
    k = [-z for z in low(n)]; eL = low(e); fL = low(f)
    Bn, Jn, Ne, Nf = wedge(e0, mnh), wedge(e, f), wedge(n, e), wedge(n, f)
    P = [zeta * k[a] + al * eL[a] + (be + th) * fL[a] for a in r4]
    Q = [x * k[a] + be * eL[a] + ga * fL[a] for a in r4]
    return [k[a] * (chi * Bn + th * Jn) + P[a] * Ne + Q[a] * Nf for a in r4], k


Ey = [[1, 0, 0, 0], [0, 1, kap * y[3] / 2, 0], [0, 0, 1, 0], [0, 0, -kap * y[1] / 2, 1]]
S = {}
for c, d in itertools.combinations(range(4), 2):
    comp = [0] * 20
    for A_ in range(4):
        for b in range(4):
            comp[4 + 4 * A_ + b] = eta[A_, d] * U[c, b] - eta[A_, c] * U[d, b]
    S[(c, d)] = VF(comp)
Aa = sp.Matrix([[0, sp.Rational(1, 3), sp.Rational(-1, 5), sp.Rational(2, 7)], [0, 0, sp.Rational(1, 4), sp.Rational(-1, 6)],
                [0, 0, 0, sp.Rational(3, 8)], [0, 0, 0, 0]]); Aa = Aa - Aa.T
X = eta * Aa; Lc = (sp.eye(4) - X).inv() * (sp.eye(4) + X)
assert sp.simplify(Lc.T * eta * Lc - eta) == sp.zeros(4, 4)
subU = {U[i, j]: Lc[i, j] for i in range(4) for j in range(4)}
sub1 = {U[i, j]: (1 if i == j else 0) for i in range(4) for j in range(4)}


def ev(V, sub):
    return [sp.simplify(t.subs(sub)) for t in V.c] + [sp.simplify(V.f.subs(sub))]


r2 = sp.sqrt(2)
points = {'U2': dict(s=0, chi=0, th=1, zeta=sp.Rational(1, 2), x=sp.Rational(-1, 3), al=sp.Rational(3, 5), be=0, ga=sp.Rational(4, 5)),
          'T1': dict(s=sp.Rational(3, 5), chi=0, th=1, zeta=sp.Rational(1, 2), x=sp.Rational(-1, 3), al=-1 / r2, be=0, ga=1 / r2)}
for name, pt in points.items():
    con = pt['th'] ** 2 - 2 * pt['th'] * pt['be'] - 2 * pt['be'] ** 2 - pt['al'] ** 2 - pt['ga'] ** 2 + 2 * pt['chi'] * (pt['al'] + pt['ga'])
    tau = pt['chi'] + pt['al'] + pt['ga']
    Wm, k = connection(**pt)
    om = [-Wm[b] for b in range(4)]
    D = []
    for A_ in range(4):
        comp = [0] * 20; dv = 0
        for b in range(4):
            omg = om[b] * eta
            Yb = list(Ey[b]) + [-sum(U[f_, g] * omg[c, g] for g in range(4)) for f_ in range(4) for c in range(4)]
            for i in range(20):
                comp[i] += U[A_, b] * Yb[i]
            dv += VF(Yb).act(U[A_, b]) + U[A_, b] * sum(sp.diff(Ey[b][i], y[i]) for i in range(4))
        D.append(VF(comp, sp.expand(dv / 2)))
    r1 = set()
    for (c, d), Sv in S.items():
        for A_ in range(4):
            lhs = comm(Sv, D[A_]); rhs = lin([(eta[A_, d], D[c]), (-eta[A_, c], D[d])])
            r1 |= set(sp.simplify(p - q) for p, q in zip(ev(lhs, subU), ev(rhs, subU)))
    F = {(p, q): comm(D[p], D[q]) for p in range(4) for q in range(4) if p != q}
    res = set()
    for b in range(4):
        tot = lin([(eta[A_, A_], comm(D[A_], F[(A_, b)])) for A_ in range(4) if A_ != b])
        res |= set(ev(tot, subU))
    cs_ = sp.symbols('c0:10'); keys = list(S.keys()); Tt = {}; FF = {}
    tc = [D[i].f.subs(sub1) for i in range(4)]
    for p in range(4):
        for q in range(p + 1, 4):
            V = comm(D[p], D[q]); comb = lin([(-cs_[i], D[i]) for i in range(4)] + [(cs_[4 + j], S[keys[j]]) for j in range(6)])
            eqs = [sp.expand((V.c[i] - comb.c[i]).subs(sub1)) for i in range(20)]
            sol = sp.solve(eqs, cs_, dict=True); assert len(sol) == 1; sol = sol[0]
            Tt[(p, q)] = [sp.simplify(sol[cs_[i]]) for i in range(4)]
            FF[(p, q)] = sp.simplify(V.f.subs(sub1) + sum(Tt[(p, q)][i] * tc[i] for i in range(4)))
    Tf = [[[0] * 4 for _ in r4] for _ in r4]
    for (p, q), v in Tt.items():
        for c in r4:
            Tf[p][q][c] = v[c]; Tf[q][p][c] = -v[c]
    trT = [sp.simplify(sum(Tf[a][c][c] for c in r4)) for a in r4]
    print('== %s: constraint %s, tau = %s' % (name, sp.simplify(con), sp.nsimplify(tau)))
    print('   (1) first relation at Cayley u, symbolic y, kappa: residual set', r1)
    print('   (2) [D^a,[D_a,D_b]] at Cayley u, all components incl. multiplication part:', res)
    print('   (3) read-off at u = 1: T_ac^c - tau k_a =', [sp.simplify(trT[a] - tau * k[a]) for a in r4],
          '; nonzero F pairs', {kk: v for kk, v in FF.items() if v != 0}, '[%.0fs]' % (time.time() - t0), flush=True)
