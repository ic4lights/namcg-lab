"""
s3_static_level_one.py (proposal 048). Prints to stdout only; writes nothing.

Static channel q.y = 0 at level one: 2x2 block (d_q, d_perp), D = diag(d_perp, d_perp, d_q) with index 3 along qhat.
This block contains helicity 0 and the trace polarisation.  Forms IX1, IX2, SC1, L1, L2, EH are computed exactly with the
routines of 045/046 at symbolic (l, m, k) with q = (0,0,0,k), and the forms in the block are closed-formed.

Sources (matter coupling is NOT derived; both are recorded):
  (S1) T_mu nu dhat^{mu nu}, dhat = hbar - (1/2) eta tr hbar: the coupling of Eq. (3.8)-type of 2601.08031 to the metric
       G^{mu nu} = rho^-2 gamma^{mu nu}; on dust at rest it acts on hbar with Ttilde = T_00 diag(1,1,1,1)/2.
  (S2) T_mu nu hbar^{mu nu}: the canonical Poisson-limit source of a mode with action int rho_M (gamma dphi dphi + M^2 phi^2),
       M rigid; dust at rest: T_00 only.
Response R = -(1/4) J^T F^{-1} J for S_E = D^T F D + J^T D.  Reference, for both S1 and S2 (round 2 wording): the one-coefficient value
R_GR = -64 pi^2 m^6 (T.T - T^2/2)/(c q^2) = -32 pi^2 m^6 T_00^2/(c q^2).  It is not the response of the form c EH to the source S2 itself.
The ratio r = R/R_GR at c = c_TT is the quantity printed as G_stat/G_TT.  Section R2 at the end was added in round 2; everything before it prints as in round 1.
Weights: V_0,T_0 with D; V_1,T_1 with B_1; V_2,T_2 with B_0; V_3 - T_3 =: W_R^(2) with B_2 (weight 3(1-2a)^2), which enters on the trace only.
"""
import sys, os
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '046-fibre-regime-interpolation'))
from forms_lib import *

l, m, k, q0sym = sp.symbols('l m k q0', positive=True)
dq, dp = sp.symbols('d_q d_p', real=True)
pi = sp.pi
eta = ETA

def wedge(a, b): return a * b.T - b * a.T
e = [sp.eye(4)[:, i] for i in range(4)]

def block_forms(q0_val):
    S = []
    for i in (1, 2, 3):
        j = i % 3 + 1; h = (i + 1) % 3 + 1
        S.append(m * wedge(e[i], e[0]) + l * wedge(e[j], e[h]))
    q = sp.Matrix([q0_val, 0, 0, k]); qu = eta * q
    s = [Si * q for Si in S]
    D = sp.diag(dp, dp, dq)
    c = [sum((D[i, j] * s[j] for j in range(3)), sp.zeros(4, 1)) for i in range(3)]
    n = sp.Matrix(NSYM); NN = n * n.T
    dE = sp.zeros(4, 4)
    for i in range(3):
        for j in range(3): dE += NN[i, j] * c[i] * s[j].T
    gb = m ** 2 * eta.inv(); Eb = m * eta.inv()
    dg = Eb.T * eta * dE + dE.T * eta * Eb
    K = [qu * c[i].T - c[i] * qu.T for i in range(3)]
    dT = [[[-m * sum(NN[i, j] * s[j][mu] * K[i][a, b] for i in range(3) for j in range(3)) for mu in range(4)] for b in range(4)] for a in range(4)]
    sc_pt, eh_pt = scalar_form(gb, dg, q)
    ix_pt = index_form(gb, dT, eta)
    SC2 = fibre_avg(sc_pt); IX2 = fibre_avg(ix_pt)
    dgbar = dg.applyfunc(fibre_avg)
    dTbar = [[[fibre_avg(dT[a][b][mu]) for mu in range(4)] for b in range(4)] for a in range(4)]
    SC1, EH1 = scalar_form(gb, dgbar, q)
    IX1 = index_form(gb, dTbar, eta)
    # L1, L2 of 046
    h2 = (dg - dgbar).applyfunc(sp.expand)
    G = gb.inv()
    qgq = (q.T * gb * q)[0]; qhq = (q.T * h2 * q)[0]; trhG = (h2 * G).trace()
    T1 = trhG ** 2 + 2 * (h2 * G * h2 * G).trace(); f1 = -qgq * T1 / 4 - qhq * trhG; f2 = (q.T * h2 * G * h2 * q)[0] / 2
    pref = R(1, 4) / sp.sqrt(sp.Abs(gb.det()))
    L1 = fibre_avg(sp.expand(pref * f1 / 6)); L2 = fibre_avg(sp.expand(pref * f2 / 3))
    hb = dgbar / m if False else None
    # hbar of the merged definition: (2m/3) D_ij s_i s_j; equals dgbar for symmetric D, gauge zero
    hbar = (2 * m / 3) * sum((D[i, j] * s[i] * s[j].T for i in range(3) for j in range(3)), sp.zeros(4, 4))
    return dict(SC1=SC1, SC2=SC2, IX1=IX1, IX2=IX2, EH=EH1, L1=L1, L2=L2, hbar=hbar, dgbar=dgbar, s=s, q=q)

F = block_forms(sp.Integer(0))
print("Consistency: hbar = fibre average of delta gamma:", (F['hbar'] - F['dgbar']).applyfunc(sp.simplify).is_zero_matrix)
print("L1 + L2 - (SC2 - SC1) =", sp.simplify(F['L1'] + F['L2'] - (F['SC2'] - F['SC1'])))
for key in ('EH', 'IX1', 'IX2', 'SC1', 'SC2', 'L1', 'L2'):
    print("  %-4s = %s" % (key, sp.factor(sp.simplify(F[key]))))
q2 = k ** 2
a = l ** 2 * k ** 2; b = -m ** 2 * k ** 2
print("\nClosed-form check of IX2, SC2 with G = diag(a,a,b):")
P = sp.diag(a * dp ** 2, a * dp ** 2, b * dq ** 2); Gm = sp.diag(a, a, b); A = sp.diag(a * dp, a * dp, b * dq)
base = Gm.trace() * P.trace() + 2 * (Gm * P).trace()
print("   IX2 residual:", sp.simplify(F['IX2'] - q2 * base / (15 * m ** 4)))
print("   SC2 residual:", sp.simplify(F['SC2'] + q2 * (base + 2 * (A.trace() ** 2 + 2 * (A * A).trace())) / (360 * m ** 4)))

# total level-one form
V0, V1, T0, T1, T2, W3 = sp.symbols('V0 V1 T0 T1 T2 W3', real=True)
Tt = sp.Symbol('T', positive=True); Vv = sp.Symbol('V', positive=True)
WR0, WR1, WR2, WX0, WX2 = V0 - T0, V1 - T1, W3, -T0 / 8, -T2 / 8
ind = -(1 / (32 * pi ** 2)) * (WR0 * F['SC1'] + WR1 * F['L1'] + WR2 * F['L2'] + WX0 * F['IX1'] + WX2 * (F['IX2'] - F['IX1']))
tree_c = sp.Symbol('tree', nonnegative=True)   # rho_M m^2/(4 g^2)
Pc = (sp.diag(1, 1, 1))  # c_i.c_i contribution
ccsum = 2 * a * dp ** 2 + b * dq ** 2
treeF = tree_c * q2 * ccsum / 3
FF = sp.Matrix(2, 2, lambda i, j: sp.Rational(1, 2) * sp.diff(ind + treeF, (dq, dp)[i], (dq, dp)[j]))
FF = FF.applyfunc(sp.simplify)
print("\nTotal block (S_E = D^T F D, basis d_q, d_p), general weights:")
for (i, j) in [(0, 0), (0, 1), (1, 1)]:
    print("   F[%d,%d] = %s" % (i, j, sp.factor(FF[i, j].subs(tree_c, 0))))
print("   tree part: F_qq = tree q^2 b/3, F_pp = 2 tree q^2 a/3 (time component has the indefinite sign of alpha^0)")

# sources
hb = F['hbar']
hbdq, hbdp = sp.simplify(sp.diff(hb, dq)), sp.simplify(sp.diff(hb, dp))
print("\nhbar images: d/d d_q:", hbdq.tolist(), "\n             d/d d_p:", hbdp.tolist())
T00 = sp.Symbol('T00', positive=True)
Tlow_S2 = sp.zeros(4, 4); Tlow_S2[0, 0] = T00
Tlow_S1 = T00 * sp.eye(4) / 2
Js = {}
for name, Tl in (('S1', Tlow_S1), ('S2', Tlow_S2)):
    Js[name] = sp.Matrix([sum(Tl[i, j] * hbdq[i, j] for i in range(4) for j in range(4)), sum(Tl[i, j] * hbdp[i, j] for i in range(4) for j in range(4))]).applyfunc(sp.simplify)
    print("   J[%s] =" % name, Js[name].tolist())
s2 = sp.Symbol('s2', positive=True)      # s^2 = m^2/l^2
def response(Fm, J):
    return sp.simplify(-sp.Rational(1, 4) * (J.T * Fm.inv() * J)[0])
RGR = lambda c: -32 * pi ** 2 * m ** 6 * T00 ** 2 / (c * q2)

print("\nEqual weights (V_i=V, T_i=T, W3=V-T), no tree: closed response")
eqw = {V0: Vv, V1: Vv, T0: Tt, T1: Tt, T2: Tt, W3: Vv - Tt, tree_c: 0}
F_eq = FF.subs(eqw).applyfunc(sp.simplify)
print("   F_eq =", F_eq.applyfunc(sp.factor).tolist())
cTT_eq = sp.Rational(2, 5) * (Vv - Tt) + sp.Rational(3, 5) * Tt
print("   c_TT (equal weights) =", sp.simplify(Vv / 6 + Tt / 12 + sp.Rational(7, 30) * (Vv - Tt) + sp.Rational(7, 20) * Tt), " check:", sp.simplify(Vv / 6 + Tt / 12 + sp.Rational(7, 30) * (Vv - Tt) + sp.Rational(7, 20) * Tt - cTT_eq))
for name in ('S1', 'S2'):
    Rr = response(F_eq, Js[name])
    ratio = sp.simplify((Rr / RGR(cTT_eq)).subs(l, m / sp.sqrt(s2)))
    print("   %s: G_stat/G_TT (level one, equal weights) = %s" % (name, sp.factor(ratio)))
    print("       V=T: %s ; late s->oo, V=T: %s ; late s->oo, V general: %s" % (sp.factor(ratio.subs(Vv, Tt)), sp.limit(ratio.subs(Vv, Tt), s2, sp.oo), sp.simplify(sp.limit(ratio, s2, sp.oo))))
    rr = sp.factor(ratio.subs(Vv, Tt))
    num, den = sp.fraction(rr)
    print("       V=T: zeros of the numerator in s^2:", sp.nroots(sp.Poly(num, s2)), " zeros of the denominator:", sp.nroots(sp.Poly(den, s2)))
    for sv in [R(9, 16), R(1), R(3), R(5), R(9), R(10), R(100), R(10 ** 4)]:
        print("         s^2=%-8s ratio(V=T)=%.6f" % (sv, float(rr.subs(s2, sv))))

print("\nSolution direction, V=T, S1: spatial/time amplitudes of hbar and PPN-type ratio, level one")
sol = -sp.Rational(1, 2) * F_eq.subs(Vv, Tt).inv() * Js['S1']
hsol = (hbdq * sol[0] + hbdp * sol[1]).applyfunc(sp.simplify)
tr = sum(eta[i, i] * hsol[i, i] for i in range(4))   # eta_mu nu h^{mu nu}
E = hsol[0, 0] - sp.Rational(1, 2) * eta[0, 0] * tr
Ff = hsol[1, 1] - sp.Rational(1, 2) * eta[1, 1] * tr
gam = sp.simplify((Ff / E).subs(l, m / sp.sqrt(s2)))
print("   gamma_level-one(S1, V=T) = delta g^{11}/delta g^{00} =", sp.factor(gam), " ; late:", sp.limit(gam, s2, sp.oo))

print("\nSign of the helicity-zero eigenvalue and of the source channel, weights V_i,T_i generic: the two are different quantities")
print("   F_qq (no tree), general weights, at s->oo per l^2 -> 0:", sp.factor(sp.limit(FF[0, 0].subs(tree_c, 0), l, 0)))
print("   F_pp (no tree), general weights, leading in l^2:", sp.factor(sp.limit(FF[1, 1].subs(tree_c, 0) / l ** 2, l, 0)))
print("   F_qp (no tree), general weights, leading in l^2:", sp.factor(sp.limit(FF[0, 1].subs(tree_c, 0) / l ** 2, l, 0)))

print("\nGeneral weights, late limit l -> 0 at fixed V_i, T_i: G_stat/G_TT at level one")
cTTg = V0 / 6 + T0 / 12 + sp.Rational(7, 30) * (V1 - T1) + sp.Rational(7, 20) * T2
Fg = FF.subs(tree_c, 0).applyfunc(sp.simplify)
for name, pred in (('S1', 10 * cTTg / (5 * V0 + 4 * (V1 - T1) + 4 * T2)), ('S2', 40 * cTTg / (5 * V0 + 4 * (V1 - T1) + 4 * T2))):
    Rg = response(Fg, Js[name])
    ratio = sp.simplify(Rg / RGR(cTTg))
    lim = sp.simplify(sp.limit(ratio, l, 0))
    print("   %s: limit = %s ; minus predicted = %s" % (name, sp.factor(lim), sp.simplify(lim - pred)))
print("   sum check with equal weights S1: 2(2V+T)/(9V):", sp.simplify((10 * cTTg / (5 * V0 + 4 * (V1 - T1) + 4 * T2)).subs({V0: Vv, V1: Vv, T0: Tt, T1: Tt, T2: Tt}, simultaneous=True) - 2 * (2 * Vv + Tt) / (9 * Vv)))

print("\n=== R2: checks added in round 2 ===")
print("\n(R2.1) Calibration on the three-space orthogonal to q, indices 0,1,2 with eta_3 = diag(-1,1,1)")
eta3 = sp.diag(-1, 1, 1)
tt = sp.symbols('t00 t01 t02 t11 t12 t22', real=True)
Tg = sp.Matrix([[tt[0], tt[1], tt[2]], [tt[1], tt[3], tt[4]], [tt[2], tt[4], tt[5]]])
dot3 = lambda P, Q: (eta3 * P * eta3 * Q).trace()
tr3 = lambda P: (eta3 * P).trace()
X3g = Tg - eta3 * tr3(Tg) / 2
print("   any symmetric T on the three-space, X_3 = T - (1/2) eta_3 trT: X_3.X_3 - (tr X_3)^2 - (T.T - (1/2)(trT)^2) =", sp.expand(dot3(X3g, X3g) - tr3(X3g) ** 2 - dot3(Tg, Tg) + tr3(Tg) ** 2 / 2))
rho0, bst = sp.symbols('rho0 b', positive=True)
u3 = sp.Matrix([sp.cosh(bst), sp.sinh(bst), 0])
Td3 = rho0 * u3 * u3.T
print("   dust, boosted in the three-space, u.u =", sp.simplify((u3.T * eta3 * u3)[0]))
X3d = Td3 - eta3 * tr3(Td3) / 2
print("   dust: T.T - (1/2)(trT)^2 =", sp.simplify(dot3(Td3, Td3) - tr3(Td3) ** 2 / 2), "; X_3.X_3 - (tr X_3)^2 =", sp.simplify(dot3(X3d, X3d) - tr3(X3d) ** 2))
eta4 = sp.diag(-1, 1, 1, 1)
u4 = sp.Matrix([1, 0, 0, 0])
Td4 = rho0 * u4 * u4.T
X4 = Td4 - eta4 * (eta4 * Td4).trace() / 2
print("   the round-1 form with the four-dimensional X, at rest: X.X =", (eta4 * X4 * eta4 * X4).trace(), "; tr_3 X =", tr3(X4[:3, :3]), "; X.X - (tr_3 X)^2 =", (eta4 * X4 * eta4 * X4).trace() - tr3(X4[:3, :3]) ** 2, " (not rho0^2/2)")
Td3r = Td3.subs(bst, 0)
print("   the round-1 form with X = T (S2), at rest: T.T - (trT)^2 =", dot3(Td3r, Td3r) - tr3(Td3r) ** 2, " (so it cannot be the reference of S2)")
TT_, mm_, qq_ = sp.symbols('T m q2', positive=True)
A_VT = (TT_ + 2 * TT_) / 24
print("   V=T: -32 pi^2 m^6 I/(q^2 A) at I = rho0^2/4, minus the one-coefficient value at c = T/2 =", sp.simplify(-32 * pi ** 2 * mm_ ** 6 * (rho0 ** 2 / 4) / (qq_ * A_VT) + 64 * pi ** 2 * mm_ ** 6 * (rho0 ** 2 / 2) / ((TT_ / 2) * qq_)))
print("   RGR(c) of this script minus -64 pi^2 m^6 (T00^2/2)/(c q^2):", sp.simplify(RGR(Tt) + 64 * pi ** 2 * m ** 6 * (T00 ** 2 / 2) / (Tt * q2)))

print("\n(R2.2) S1, V_i = T_i = T, level one: signs as exact roots, s2 = sinh^2 tau > 0")
r_S1 = sp.factor(sp.simplify((response(F_eq, Js['S1']) / RGR(cTT_eq)).subs(l, m / sp.sqrt(s2)).subs(Vv, Tt)))
pred_S1 = 2 * (s2 ** 2 - 10 * s2 + 4) / ((s2 - 4) * (3 * s2 - 2))
print("   ratio =", r_S1, "; minus the formula of the text:", sp.simplify(r_S1 - pred_S1))
nS1, dS1 = sp.fraction(sp.together(pred_S1))
zeros = sorted(sp.roots(sp.Poly(nS1, s2)).keys(), key=lambda z: float(z))
poles = sorted(sp.roots(sp.Poly(dS1, s2)).keys(), key=lambda z: float(z))
print("   zeros:", zeros, "; poles:", poles)
neg = sp.solve_univariate_inequality(pred_S1 < 0, s2, relational=False, domain=sp.Interval.open(0, sp.oo))
corrected = sp.Union(sp.Interval.open(5 - sp.sqrt(21), sp.Rational(2, 3)), sp.Interval.open(4, 5 + sp.sqrt(21)))
print("   negative set:", neg, "; equals (5-sqrt 21, 2/3) U (4, 5+sqrt 21):", neg == corrected)
pts = sorted(set([sp.Integer(0)] + zeros + poles), key=lambda z: float(z))
for i in range(len(pts)):
    lo = pts[i]; hi = pts[i + 1] if i + 1 < len(pts) else lo + 10
    mid = sp.nsimplify((lo + hi) / 2)
    print("     (%s, %s): at the midpoint the sign is %+d" % (lo, hi if i + 1 < len(pts) else 'oo', sp.sign(pred_S1.subs(s2, mid))))
print("   exact samples: s^2=1/2:", pred_S1.subs(s2, R(1, 2)), "; s^2=9/16:", pred_S1.subs(s2, R(9, 16)), "; limit:", sp.limit(pred_S1, s2, sp.oo))

print("\n(R2.3) The formula needs V_i = T_i = T: V_i = T_i with T_0 = 1, T_1 = T_2 = 2, S1, s^2 = 100, against the formula")
wt = {V0: 1, T0: 1, V1: 2, T1: 2, T2: 2}
Fw = Fg.subs(wt).applyfunc(sp.simplify)
cw = cTTg.subs(wt)
rw = sp.simplify((response(Fw, Js['S1']) / RGR(cw)).subs(l, m / sp.sqrt(sp.Integer(100))))
print("   ratio:", rw, "; formula:", pred_S1.subs(s2, 100))

print("\n(R2.4) v^2 -> 1/5 at large tau means c_TT = 4 kappa, one linear condition on the weights")
kap = (V1 - T1) / 20 + sp.Rational(3, 20) * T2
cond = sp.expand(cTTg - 4 * kap)
print("   c_TT - 4 kappa =", cond, "; minus V0/6 + T0/12 + (V1-T1)/30 - T2/4:", sp.expand(cond - (V0 / 6 + T0 / 12 + (V1 - T1) / 30 - T2 / 4)))
print("   equal weights V_i=V, T_i=T:", sp.factor(cond.subs({V0: Vv, V1: Vv, T0: Tt, T1: Tt, T2: Tt})), " ; V_i=T_i:", sp.factor(cond.subs({V0: T0, V1: T1})))

print("\n(R2.5) Which variable carries the ratio 0: (S2) solution hbar^00 = H, hbar^11 = hbar^22 = 0, at rest")
H = sp.Symbol('H', real=True)
hb5 = sp.diag(H, 0, 0, 0)
t5 = (eta4 * hb5).trace()
hh5 = hb5 - eta4.inv() * t5 / 2
print("   hbar^11/hbar^00 =", hb5[1, 1] / hb5[0, 0], "; hhat^11/hhat^00 =", sp.simplify(hh5[1, 1] / hh5[0, 0]), "; (hbar^00+hbar^11) - (hhat^00+hhat^11) =", sp.simplify(hb5[0, 0] + hb5[1, 1] - hh5[0, 0] - hh5[1, 1]))
