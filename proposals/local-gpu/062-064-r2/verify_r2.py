"""Verification for proposal local-gpu/062-064-r2 (run: python -I verify_r2.py).

Sections
 S1  profile identities and parametrisation dependence of the quadratic part at an uncancelled tadpole
 S2  recorded-convention consistency: q_b^2 = -U4 L/(2 m^4), q_*^2|chi = -beta_K U' L/(8 m^4)
 S3  identity at a stationary background: sum C_i = sum (C_i - T_i), invariant under sigma -> sigma + a sigma^2
 S4  q_*^2|chi = -U'^2 L/(4 m^4 U_chichi) <= 0
 S5  rigidity: T y = 0 => T (g + eps y y^T) T^T = T g T^T exactly; y.y in the fluctuated metric moves
 S6  064 density of the first term with a lower limit s_Lambda; its ln(chi) derivative is the Y summand
 S7  extra first-order part under the response hypothesis dln(theta) = p sigma; regulator dependence of its sign
 S8  t-response of Y (finite) and the p = 1/2 value of the contraction reading (metric and inverse metric)
 S9  cross-check against the group4 review numbers (t_064 = 2 sigma, p = 1/2)
"""
import sympy as sp
import mpmath as mp

ok_all = True
def check(name, cond):
    global ok_all
    ok_all = ok_all and bool(cond)
    print(f"{name}: {bool(cond)}")

# ---------------- S1 ----------------
t, e, u, x, s, a = sp.symbols('t e u x sigma a', real=True)
m = sp.symbols('m', positive=True)
# three parametrisations of the same first-order channel, written in sigma = first-order dln sqrt|g|
P_metric = sp.series((1 + s/2)**2, s, 0, 3).removeO()          # g -> (1+u) gbar, u = sigma/2
P_inverse = sp.series((1 - s/2)**(-2), s, 0, 3).removeO()      # gamma -> (1+e) gammabar, e = -sigma/2
P_rank1 = sp.series(1/(1 - s), s, 0, 3).removeO()               # frame rank one, sqrt|g_n| ~ (1+x)^-1, x = -sigma
P_conf = sp.series(sp.exp(s), s, 0, 3).removeO()                # conformal field phi
for nm, P in [('metric', P_metric), ('inverse', P_inverse), ('rank1(recorded)', P_rank1), ('conformal', P_conf)]:
    T1 = sp.expand(P).coeff(s, 1); C1 = sp.expand(P).coeff(s, 2)
    print(f"S1 profile {nm}: T={T1}, C={C1}, C/T={sp.nsimplify(C1/T1)}")
check("S1 first-order part is parametrisation-free (all T=1)",
      all(sp.expand(P).coeff(s, 1) == 1 for P in [P_metric, P_inverse, P_rank1, P_conf]))
check("S1 recorded rank-one profile has C=T (term U4 sigma^2)", sp.expand(P_rank1).coeff(s, 2) == 1)
# redefinition shifts C by a*T
Tg, Cg = sp.symbols('T C')
f = Tg*s + Cg*s**2
f2 = sp.expand(f.subs(s, s + a*s**2))
check("S1 sigma->sigma+a sigma^2 shifts C by a T", sp.simplify(f2.coeff(s, 2) - (Cg + a*Tg)) == 0)

# ---------------- S2 ----------------
F, Uh, Vh, Th, chi, L = sp.symbols('F Uhat Vhat That chi L', positive=True)
A = F*(Vh + 2*Th)*chi**2/24                     # A=(V+2T)/24, V=F Vhat chi^2, T=F That chi^2 (recorded)
Lrec = 32*sp.pi**2*m**6/A
sqrtgbar = m**-4                                # sqrt|g_n| = m^-4 (1+x_n)^-1 at a fibre point (recorded)
U4 = -F/(32*sp.pi**2)*sqrtgbar*Uh*chi**4
qb2_rec = 12*Uh*chi**2/(m**2*(Vh + 2*Th))
# local term C sigma^2 = C t^2/(4 m^4); phase average -> (1/2) C t^2/(4m^4)*... reduced form (q^2/4L) t^2 + (1/2) M t^2, M = C/(4 m^4)
def pole_shift(C):
    M = C/(4*m**4)
    return 2*M*Lrec
check("S2 U4 sigma^2 gives -q_b^2 (recorded q_b^2)", sp.simplify(pole_shift(U4) + qb2_rec) == 0)
beta, Up, Ucc = sp.symbols('beta_K Uprime U_chichi', real=True)
check("S2 chi exchange C=-beta U'/4 gives -beta U' L/(8 m^4) (recorded)",
      sp.simplify(pole_shift(-beta*Up/4) - (-beta*Up*Lrec/(8*m**4))) == 0)
check("S2 recorded q_*^2|chi = beta U'/(4 U4) q_b^2 consistent",
      sp.simplify(-beta*Up*Lrec/(8*m**4) - beta*Up/(4*U4)*qb2_rec) == 0)

# ---------------- S3 ----------------
n = 5
Ts = sp.symbols('T0:%d' % n); Cs = sp.symbols('C0:%d' % n)
lhs = sum(Cs)
rhs = sum(Cs[i] - Ts[i] for i in range(n))
check("S3 sum C = sum (C-T) on sum T = 0",
      sp.simplify((lhs - rhs).subs(Ts[0], -sum(Ts[1:]))) == 0)
# invariance of sum (C - T) at sum T = 0 under the redefinition
rhs_a = sum((Cs[i] + a*Ts[i]) - Ts[i] for i in range(n))
check("S3 invariant under redefinition at sum T = 0",
      sp.simplify((rhs_a - rhs).subs(Ts[0], -sum(Ts[1:]))) == 0)
# U4 + cosmological-type term only: T=C for both, cancellation removes -q_b^2
Lam = -U4
check("S3 U4 + Lambda sqrt|g| with zero tadpole: pole shift 0",
      sp.simplify(pole_shift(U4) + pole_shift(Lam)) == 0)

# ---------------- S4 ----------------
betaK = 2*Up/Ucc
qchi = -betaK*Up*L/(8*m**4)
check("S4 q_*^2|chi = -U'^2 L/(4 m^4 U_chichi)", sp.simplify(qchi + Up**2*L/(4*m**4*Ucc)) == 0)

# ---------------- S5 ----------------
import random
random.seed(7)
def rnd(): return sp.Rational(random.randint(-9, 9), random.randint(1, 5))
y = sp.Matrix([rnd() for _ in range(4)])
# rows of Tb orthogonal to y (Tb y = 0)
rows = []
while len(rows) < 6:
    r = sp.Matrix([[rnd() for _ in range(4)]])
    r = r - (r*y)[0]/(y.T*y)[0]*y.T
    rows.append(r)
Tb = sp.Matrix.vstack(*rows)
B = sp.Matrix(4, 4, lambda i, j: rnd())
gam = B*B.T + 4*sp.eye(4)
eps = sp.symbols('epsilon')
gam_e = gam + eps*y*y.T
check("S5 Tb y = 0", (Tb*y).is_zero_matrix)
check("S5 covariance Tb gamma Tb^T unchanged, all orders in eps", sp.simplify(Tb*gam_e*Tb.T - Tb*gam*Tb.T).is_zero_matrix)
gmet = gam.inv(); gmet_e = gam_e.inv()
yy0 = (y.T*gmet*y)[0]; yy1 = sp.simplify((y.T*gmet_e*y)[0])
d1 = sp.simplify(sp.diff(yy1, eps).subs(eps, 0))
check("S5 y.y in fluctuated metric moves: d(y.y)/d eps = -(y.y)^2", sp.simplify(d1 + yy0**2) == 0)
print("S5 dln(y.y)/d eps =", sp.simplify(d1/yy0), " (= -y.y, nonzero)")

# ---------------- S6 ----------------
th, c, D, sL, sv, MA2, muJ = sp.symbols('vartheta c_J D s_Lambda s M_A2 mu_J', positive=True)
integrand = sp.Rational(15, 4)*th**2 - sv*th*c + sv**2*c**2       # recorded level average (over s^2)
G_exact = sp.integrate(sp.exp(-sv*D)*integrand/sv, (sv, sL, sp.oo), conds='none')
G_claim = sp.Rational(15, 4)*th**2*sp.expint(1, sL*D) - th*c*sp.exp(-sL*D)/D + c**2*sp.exp(-sL*D)*(1 + sL*D)/D**2
check("S6 regulated density bracket (exact)", sp.simplify(sp.expand_func(G_exact - G_claim).rewrite(sp.Ei)) == 0
      or abs(sp.N((G_exact - G_claim).subs({th: 1.3, c: 2, D: 7, sL: 0.01}))) < 1e-12)
# small s_Lambda form
G_lead = sp.Rational(15, 4)*th**2*sp.expint(1, sL*D) - th*c/D + c**2/D**2
diffG = sp.N((G_claim - G_lead).subs({th: 1.3, c: 2, D: 7, sL: 1e-6}))
check("S6 bracket = 15/4 th^2 E1 - th c/D + c^2/D^2 + O(s_Lambda D)", abs(diffG) < 1e-4)
# derivative in ln chi: D = M_A^2 + mu_J, dD/dln chi = 2 M_A^2
dG = sp.diff(G_claim, D)
Ybr = sp.Rational(15, 4)*th**2/D - th*c/D**2 + 2*c**2/D**3
lim = sp.limit(sp.simplify(dG), sL, 0)
check("S6 dG/dD -> -(Y bracket) as s_Lambda -> 0", sp.simplify(lim + Ybr) == 0)
# density = -(sqrt|g|/32pi^2) sum (2J+1) G ; d/dln chi -> +(sqrt|g|/32pi^2) sum (2J+1) 2 M_A^2 Ybr = Y (recorded display)
sg, Fn, NK = sp.symbols('sqrtg F N_K', positive=True)
Yfibreconst = sg/(32*sp.pi**2)*Fn*NK*2*MA2*(sp.Rational(15, 4)*th**2/MA2)  # c=0, D=M_A^2, sum_J (2J+1) = F
check("S6 fibre-constant limit reproduces Y = 15F th^2 sqrt|g| N_K/64pi^2",
      sp.simplify(Yfibreconst - 15*Fn*th**2*sg*NK/(64*sp.pi**2)) == 0)

# ---------------- S7 ----------------
p = sp.symbols('p', real=True)
dens = lambda S: -sg/(32*sp.pi**2)*sp.exp(S)*G_lead.subs(th, th*sp.exp(p*S))   # sqrt|g| profile e^sigma at first order
first = sp.diff(dens(s), s).subs(s, 0)
profile = dens(0)
extra = sp.simplify(first - profile)
extra_claim = -p*sg/(32*sp.pi**2)*(sp.Rational(15, 2)*th**2*sp.expint(1, sL*D) - th*c/D)
check("S7 extra first-order part = -p sqrt/32pi^2 [15/2 th^2 E1 - th c/D]", sp.simplify(extra - extra_claim) == 0)
# sign depends on s_Lambda: bracket 15/2 th^2 E1(x) - th c/D at th=1, D=10, c=2 (J=1)
br = lambda xx: 7.5*mp.e1(xx) - 2.0/10
vals = [(xx, br(xx)) for xx in [1e-3, 0.1, 1.0, 2.0, 3.0]]
print("S7 bracket(15/2 th^2 E1(s_L D) - th c/D) at th=1,D=10,c=2:", [(xx, float(v)) for xx, v in vals])
check("S7 sign of extra part changes with s_Lambda", min(float(v) for _, v in vals) < 0 < max(float(v) for _, v in vals))
# U2 at V=T is theta-linear: extra p U2
U2 = lambda thv, Vv, Tv: -F/(32*sp.pi**2)*sg*(2*(Vv - Tv) - sp.Rational(3, 4)*thv*(Vv - 2*Tv))*chi**2
U2VT = U2(th, Th, Th)
check("S7 U2 at V=T = -(3F/128pi^2) th That sqrt chi^2 (recorded)", sp.simplify(U2VT + 3*F/(128*sp.pi**2)*th*Th*sg*chi**2) == 0)
U2resp = sp.diff(sp.exp(s)*U2(th*sp.exp(p*s), Th, Th), s).subs(s, 0)
check("S7 U2 first-order part exceeds profile by p U2 at V=T", sp.simplify(U2resp - U2VT - p*U2VT) == 0)

# ---------------- S8 ----------------
Yl = lambda S: sg/(32*sp.pi**2)*2*MA2*sp.exp(S)*Ybr.subs(th, th*sp.exp(p*S))
Yresp = sp.simplify(sp.diff(Yl(s), s).subs(s, 0))
Yresp_claim = sg/(32*sp.pi**2)*2*MA2*((1 + 2*p)*sp.Rational(15, 4)*th**2/D - (1 + p)*th*c/D**2 + 2*c**2/D**3)
check("S8 t-response of Y summand", sp.simplify(Yresp - Yresp_claim) == 0)
check("S8 Y-response = d/dln chi of the first-order density response (s_L->0)",
      sp.simplify(sp.limit(sp.diff(first, D)*2*MA2, sL, 0) - Yresp_claim) == 0)
# contraction reading: theta ~ y.y in fluctuated metric
# metric pure trace: g -> (1+u) gbar: y.y -> (1+u) y.y, sqrt|g| -> (1+u)^2
pm = sp.limit(sp.diff(sp.log(1 + u), u)/sp.diff(sp.log((1 + u)**2), u), u, 0)
# inverse pure trace: gamma -> (1+e) gammabar: g -> gbar/(1+e), y.y -> y.y/(1+e), sqrt|g| -> (1+e)^-2
pi_ = sp.limit(sp.diff(-sp.log(1 + e), e)/sp.diff(-2*sp.log(1 + e), e), e, 0)
check("S8 contraction reading gives p = 1/2 (metric and inverse-metric pure trace)", pm == sp.Rational(1, 2) and pi_ == sp.Rational(1, 2))

# ---------------- S9 ----------------
# group4: with t_064 (sqrt|g| -> (1+t/4)^2, theta -> (1+t/4) theta), density bracket G_lead (sign and prefactor dropped)
E = sp.symbols('E', positive=True)
Gb = sp.Rational(15, 4)*th**2*E - th*c/D + c**2/D**2
t64 = sp.symbols('t64')
resp = sp.expand(sp.series((1 + t64/4)**2*Gb.subs(th, th*(1 + t64/4)), t64, 0, 3).removeO())
tad_extra = sp.simplify(resp.coeff(t64, 1) - Gb/2)
quad_extra = sp.simplify(resp.coeff(t64, 2) - Gb/16)
check("S9 group4 extra tadpole th(15 th D E - 2c)/(8D)", sp.simplify(tad_extra - th*(15*th*D*E - 2*c)/(8*D)) == 0)
check("S9 group4 extra quadratic th(75 th D E - 8c)/(64D)", sp.simplify(quad_extra - th*(75*th*D*E - 8*c)/(64*D)) == 0)
check("S9 tadpole in t_064 = (1/2) x [p-extra at p=1/2] (dsigma/dt_064=1/2)",
      sp.simplify(tad_extra - sp.Rational(1, 2)*sp.Rational(1, 2)*(sp.Rational(15, 2)*th**2*E - th*c/D)) == 0)

print("ALL CHECKS PASS:", ok_all)
