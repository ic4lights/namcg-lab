"""050 s8 (r2): measure, Hermiticity shift and the |det e|^{-1/2} conjugation for general frames, exact rational arithmetic.

An actual chart on the fibre is used, so the Haar statement is tested and not assumed: Cayley coordinates
u = (1-A)^{-1}(1+A), with A in so(p,q), so that du = u Omega reads dA = (1/2)(1+A) Omega (1-A), and
du = L u reads dA = (1/2)(1-A) L (1+A). Haar density in this chart: det(1-A)^{-(d-1)}.

V_a = u_a^b e_b^mu (d_mu - u_f^g w_mu^c_g d/du_f^c), D_a = V_a + t_a - i A_a.
Reference measure d^dy dHaar; mu = |det e|^{-1} d^dy dHaar.

Part 0  Haar density: both invariant families are divergence free in the chart, boosts included.
Part A  div_mu V_a = T_ac^c. It involves only the first jet of e and the value of w, and is linear in them at fixed
        (e, u), so symbolic first jets at a fixed rational (e, u) cover every jet there: d = 2, 3, 4. d = 2 also has
        (e, u) symbolic. Frames are neither triangular nor unimodular.
Part B  polynomial e, w, order two: t_a = (1/2) T_ac^c; the conjugated t~_a = (1/2) div_ref V_a = t_a + (1/2) V_a ln|det e|;
        the order-zero part of [D_a, D_b] is the same in the two pictures with the same T: d = 3 and 4.
Part C  d = 3: L_a = V_a + (1/2) div_ref V_a is formally anti-symmetric in the reference measure; S_cd has no y part,
        no divergence and the stated commutator with V_a; Lambda-type field xi^mu d_mu + (1/2) d_mu xi^mu closes on the
        class in the reference measure.
Limits are stated in proposal-r2.md: pointwise identities in a chart with formal adjoints; no domains, no boundary terms,
no integrals over the non-compact fibre."""
import random
import sys
import time
import sympy as sp


def eta_list(d):
    return [-1] + [1] * (d - 1)


class Chart:
    def __init__(self, d):
        self.d = d
        self.eta = eta_list(d)
        self.y = sp.symbols("y0:%d" % d)
        self.idx = [(g, c) for g in range(d) for c in range(g + 1, d)]
        self.th = sp.symbols("th0:%d" % len(self.idx))
        self.coords = list(self.y) + list(self.th)
        A = sp.zeros(d, d)
        for k, (g, c) in enumerate(self.idx):
            A[g, c] += self.th[k] * self.eta[c]
            A[c, g] += -self.th[k] * self.eta[g]
        self.A = A
        M = sp.eye(d) - A
        self.detm = sp.factor(M.det(method="berkowitz"))
        self.u = (M.adjugate() * (sp.eye(d) + A) / self.detm).applyfunc(sp.cancel)
        self.dlnH = [sp.S.Zero] * d + [-(d - 1) * sp.diff(self.detm, t) / self.detm for t in self.th]

    def read(self, dA):
        return [dA[g, c] * self.eta[c] for (g, c) in self.idx]

    def lie_element(self, k):
        g, c = self.idx[k]
        X = sp.zeros(self.d, self.d)
        X[g, c] = self.eta[c]
        X[c, g] = -self.eta[g]
        return X

    def right_field(self, Om):
        d = self.d
        return [sp.S.Zero] * d + self.read(sp.Rational(1, 2) * (sp.eye(d) + self.A) * Om * (sp.eye(d) - self.A))

    def left_field(self, L):
        d = self.d
        return [sp.S.Zero] * d + self.read(sp.Rational(1, 2) * (sp.eye(d) - self.A) * L * (sp.eye(d) + self.A))

    def div_ref(self, V):
        return sum(sp.diff(V[k], self.coords[k]) + V[k] * self.dlnH[k] for k in range(len(self.coords)) if V[k] != 0)

    def apply(self, V, f):
        return sum(V[k] * sp.diff(f, self.coords[k]) for k in range(len(self.coords)) if V[k] != 0)

    def bracket(self, V, W):
        return [self.apply(V, W[k]) - self.apply(W, V[k]) for k in range(len(self.coords))]

    def frame_fields(self, e, w):
        """e rows b, columns mu; w[mu] = matrix w^c_g, rows c, columns g, lowered antisymmetric."""
        d = self.d
        out = []
        for a in range(d):
            co = [sum(self.u[a, b] * e[b, m] for b in range(d)) for m in range(d)]
            V = list(co) + [sp.S.Zero] * len(self.idx)
            for m in range(d):
                R = self.right_field(-w[m].T)
                for k in range(d, len(self.coords)):
                    V[k] += co[m] * R[k]
            out.append(V)
        return out


def lower_antisym(chart, vals):
    d = chart.d
    m = sp.zeros(d, d)
    for k, (c, g) in enumerate(chart.idx):
        m[c, g] = vals[k] * chart.eta[c]
        m[g, c] = -vals[k] * chart.eta[g]
    return m


def randrat(lim=5):
    return sp.Rational(random.randint(-lim, lim), random.randint(1, 4))


def part0(ch):
    d = ch.d
    pt = {t: sp.Rational(random.randint(-3, 3), 11) for t in ch.th}
    okR, okL, group = True, True, True
    uval = ch.u.subs(pt)
    eta = sp.diag(*ch.eta)
    group = uval * eta * uval.T == eta
    for k in range(len(ch.idx)):
        X = ch.lie_element(k)
        okR &= sp.cancel(ch.div_ref(ch.right_field(X)).subs(pt)) == 0
        okL &= sp.cancel(ch.div_ref(ch.left_field(X)).subs(pt)) == 0
    # the chart formulas reproduce du = u Omega at the point
    X = ch.lie_element(0)
    R = ch.right_field(X)
    du = ch.u.applyfunc(lambda f: ch.apply(R, f)).subs(pt).applyfunc(sp.nsimplify)
    formula = du == (ch.u * X).subs(pt)
    print(f"d={d} part 0: u in the group {group}; right fields divergence free {okR}; left fields divergence free {okL}; dA formula gives du = u X {formula}", flush=True)
    assert group and okR and okL and formula


def torsion_at(ch, Vs, pt):
    """T_ab^c at the point, from the y part of the bracket: [V_a,V_b]^mu = -T_ab^c V_c^mu."""
    d = ch.d
    co = sp.Matrix(d, d, lambda c, m: Vs[c][m].subs(pt))
    coi = co.inv()
    T = {}
    for a in range(d):
        for b in range(a + 1, d):
            br = sp.Matrix([[(ch.apply(Vs[a], Vs[b][m]) - ch.apply(Vs[b], Vs[a][m])).subs(pt) for m in range(d)]])
            t = (-br * coi)
            T[(a, b)] = [sp.expand(t[0, c]) for c in range(d)]
    def get(a, b, c):
        if a == b:
            return sp.S.Zero
        return T[(a, b)][c] if a < b else -T[(b, a)][c]
    return get


def part_A(ch):
    d = ch.d
    E = sp.Matrix(d, d, lambda i, j: randrat() + (3 if i == j else 0))
    while E.det() == 0 or abs(E.det()) == 1:
        E = sp.Matrix(d, d, lambda i, j: randrat() + (3 if i == j else 0))
    J = [[[sp.Symbol(f"J{b}_{m}_{n}") for n in range(d)] for m in range(d)] for b in range(d)]
    Wv = [[sp.Symbol(f"W{m}_{k}") for k in range(len(ch.idx))] for m in range(d)]
    e = sp.Matrix(d, d, lambda b, m: E[b, m] + sum(J[b][m][n] * ch.y[n] for n in range(d)))
    w = [lower_antisym(ch, Wv[m]) for m in range(d)]
    Vs = ch.frame_fields(e, w)
    pt = {t: sp.Rational(random.randint(-3, 3), 11) for t in ch.th}
    pt.update({y: 0 for y in ch.y})
    Ei = E.inv()
    dlnE = [sum(Ei[m, b] * J[b][m][n] for b in range(d) for m in range(d)) for n in range(d)]
    get = torsion_at(ch, Vs, pt)
    ok, plus = True, True
    for a in range(d):
        dv_ref = sp.expand(ch.div_ref(Vs[a]).subs(pt))
        dv = sp.expand(dv_ref - sum(Vs[a][n].subs(pt) * dlnE[n] for n in range(d)))
        tr = sp.expand(sum(get(a, c, c) for c in range(d)))
        ok &= sp.expand(dv - tr) == 0
        plus &= sp.expand(dv + tr) == 0
    print(f"d={d} part A: det e = {E.det()} at the point, entries off the diagonal nonzero {any(E[i, j] != 0 for i in range(d) for j in range(d) if i != j)}; "
          f"symbolic first jets {d**3} and connection values {d*len(ch.idx)}: div_mu V_a = T_ac^c for all a: {ok}; with the opposite sign: {plus}", flush=True)
    assert ok


def part_A_d2():
    ch = Chart(2)
    d = 2
    Es = sp.Matrix(2, 2, lambda i, j: sp.Symbol(f"E{i}{j}"))
    J = [[[sp.Symbol(f"J{b}_{m}_{n}") for n in range(d)] for m in range(d)] for b in range(d)]
    Wv = [[sp.Symbol(f"W{m}")] for m in range(d)]
    e = sp.Matrix(2, 2, lambda b, m: Es[b, m] + sum(J[b][m][n] * ch.y[n] for n in range(d)))
    w = [lower_antisym(ch, Wv[m]) for m in range(d)]
    Vs = ch.frame_fields(e, w)
    pt = {y: 0 for y in ch.y}
    Ei = Es.inv()
    dlnE = [sum(Ei[m, b] * J[b][m][n] for b in range(d) for m in range(d)) for n in range(d)]
    co = sp.Matrix(2, 2, lambda c, m: Vs[c][m].subs(pt))
    br = sp.Matrix([[(ch.apply(Vs[0], Vs[1][m]) - ch.apply(Vs[1], Vs[0][m])).subs(pt) for m in range(2)]])
    T01 = (-br * co.inv()).applyfunc(sp.cancel)
    trs = [T01[0, 1], -T01[0, 0]]
    ok = True
    for a in range(2):
        dv = ch.div_ref(Vs[a]).subs(pt) - sum(Vs[a][n].subs(pt) * dlnE[n] for n in range(d))
        ok &= sp.cancel(sp.together(dv - trs[a])) == 0
    print(f"d=2 part A, all of e, its first jet, w and the fibre coordinate symbolic: div_mu V_a = T_ac^c: {ok}", flush=True)
    assert ok


def poly_data(ch):
    d = ch.d
    y = ch.y
    lin = lambda: randrat(3) + sum(randrat(3) * y[i] for i in range(d))
    quad = lambda: lin() + sum(randrat(2) * y[i] * y[j] for i in range(d) for j in range(i, d))
    e = sp.Matrix(d, d, lambda i, j: (3 if i == j else 0) + quad())
    w = [lower_antisym(ch, [lin() for _ in ch.idx]) for _ in range(d)]
    return e, w


def part_B(ch, pairs_max):
    d = ch.d
    e, w = poly_data(ch)
    dete = e.det(method="berkowitz")
    pt = {y: sp.Rational(i + 1, 7) for i, y in enumerate(ch.y)}
    pt.update({t: sp.Rational(random.randint(-3, 3), 11) for t in ch.th})
    Vs = ch.frame_fields(e, w)
    lnE = [sp.S.Zero if k >= d else sp.diff(dete, ch.coords[k]) / dete for k in range(len(ch.coords))]
    print(f"d={d} part B: det e at the point = {dete.subs(pt)}", flush=True)
    get = torsion_at(ch, Vs, pt)
    tref = [sp.Rational(1, 2) * ch.div_ref(Vs[a]) for a in range(d)]
    delta = [sp.Rational(1, 2) * sum(Vs[a][k] * lnE[k] for k in range(d)) for a in range(d)]
    tmu = [tref[a] - delta[a] for a in range(d)]
    ok_half = all(sp.nsimplify(tmu[a].subs(pt)) == sp.Rational(1, 2) * sum(get(a, c, c) for c in range(d)) for a in range(d))
    print(f"   t_a = (1/2) div_mu V_a = (1/2) T_ac^c at the point: {ok_half}", flush=True)
    assert ok_half
    ok_zero, cnt, nonzero = True, 0, False
    for a in range(d):
        for b in range(a + 1, d):
            if cnt >= pairs_max:
                continue
            cnt += 1
            G_mu = ch.apply(Vs[a], tmu[b]).subs(pt) - ch.apply(Vs[b], tmu[a]).subs(pt) + sum(get(a, b, c) * tmu[c].subs(pt) for c in range(d))
            G_ref = ch.apply(Vs[a], tref[b]).subs(pt) - ch.apply(Vs[b], tref[a]).subs(pt) + sum(get(a, b, c) * tref[c].subs(pt) for c in range(d))
            ok_zero &= sp.nsimplify(G_mu - G_ref) == 0
            nonzero |= sp.nsimplify(G_mu) != 0
            print(f"   pair ({a},{b}): order-zero part of [D_a,D_b] + T^c D_c, picture mu = {sp.nsimplify(G_mu)}, reference = {sp.nsimplify(G_ref)}", flush=True)
    print(f"   same order-zero coefficient in both pictures, with the same T: {ok_zero}; full comparison on {cnt} pairs; nonzero at T != 0: {nonzero}", flush=True)
    ok_diff = True
    if d <= 3:
        ok_diff = all(sp.nsimplify((ch.apply(Vs[a], delta[b]) - ch.apply(Vs[b], delta[a])).subs(pt) + sum(get(a, b, c) * delta[c].subs(pt) for c in range(d))) == 0
                      for a in range(d) for b in range(a + 1, d))
        print(f"   the difference of the two, V_a delta_b - V_b delta_a + T_ab^c delta_c with delta_a = (1/2) V_a ln|det e|, vanishes on all {d*(d-1)//2} pairs: {ok_diff}", flush=True)
    else:
        print("   the all-pairs difference test is not run at this d, for run time", flush=True)
    assert ok_zero and ok_diff


def part_C():
    ch = Chart(3)
    d = 3
    e, w = poly_data(ch)
    Vs = ch.frame_fields(e, w)
    pt = {y: sp.Rational(i + 1, 7) for i, y in enumerate(ch.y)}
    pt.update({t: sp.Rational(random.randint(-3, 3), 11) for t in ch.th})
    y0, y1, y2 = ch.y
    t0, t1, t2 = ch.th
    f = 1 + y0 * y1 + t0 * y2 + t1 * t2
    g = y2 - y1 ** 2 + t2 * y0 + t0 ** 2
    H = ch.detm ** (-(d - 1))
    ok = True
    for a in range(d):
        c = sp.Rational(1, 2) * ch.div_ref(Vs[a])
        lhs = f * (ch.apply(Vs[a], g) + c * g) + g * (ch.apply(Vs[a], f) + c * f)
        flux = sum(sp.diff(H * f * g * Vs[a][k], ch.coords[k]) for k in range(len(ch.coords))) / H
        ok &= sp.nsimplify((lhs - flux).subs(pt)) == 0
    print(f"d=3 part C: f L_a g + g L_a f is a total divergence in the reference measure, so L_a is formally anti-symmetric: {ok}", flush=True)
    assert ok
    eta = ch.eta
    okS = True
    for (c_, d_) in ch.idx:
        L = sp.zeros(d, d)
        for a in range(d):
            for x in range(d):
                L[a, x] = (eta[a] if a == d_ else 0) * (1 if x == c_ else 0) - (eta[a] if a == c_ else 0) * (1 if x == d_ else 0)
        S = ch.left_field(L)
        okS &= sp.cancel(ch.div_ref(S).subs(pt)) == 0
        okS &= all(S[k] == 0 for k in range(d))
        for a in range(d):
            br = ch.bracket(S, Vs[a])
            tgt = [(eta[a] if a == d_ else 0) * Vs[c_][k] - (eta[a] if a == c_ else 0) * Vs[d_][k] for k in range(len(ch.coords))]
            okS &= all(sp.nsimplify((br[k] - tgt[k]).subs(pt)) == 0 for k in range(len(ch.coords)))
    print(f"   S_cd: no y part, no divergence, [S_cd,V_a] = eta_ad V_c - eta_ac V_d on all coordinates: {okS}", flush=True)
    assert okS
    xi = [y0 * y1 + 1, y2 ** 2 - y0, y0 * y1 * y2]
    Xi = list(xi) + [sp.S.Zero] * 3
    cX = sp.Rational(1, 2) * sum(sp.diff(xi[m], ch.y[m]) for m in range(d))
    okL = True
    for a in range(d):
        ca = sp.Rational(1, 2) * ch.div_ref(Vs[a])
        Br = ch.bracket(Xi, Vs[a])
        order0 = ch.apply(Xi, ca) - ch.apply(Vs[a], cX)
        okL &= sp.nsimplify((order0 - sp.Rational(1, 2) * ch.div_ref(Br)).subs(pt)) == 0
    print(f"   [xi + (1/2) div xi, L_a] = W + (1/2) div_ref W with W = [xi, V_a], so the diffeomorphism generator of the reference picture stays in the class: {okL}", flush=True)
    assert okL


random.seed(50)
t0_ = time.time()
part_A_d2()
for d in (2, 3, 4):
    ch = Chart(d)
    part0(ch)
    part_A(ch)
    print(f"   elapsed {time.time()-t0_:.0f} s", flush=True)
part_C()
print(f"   elapsed {time.time()-t0_:.0f} s", flush=True)
part_B(Chart(3), 3)
print(f"   elapsed {time.time()-t0_:.0f} s", flush=True)
part_B(Chart(4), int(sys.argv[1]) if len(sys.argv) > 1 else 1)
print(f"   elapsed {time.time()-t0_:.0f} s", flush=True)
print("ALL ASSERTIONS PASSED")
