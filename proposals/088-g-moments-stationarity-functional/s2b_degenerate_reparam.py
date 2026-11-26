# s2b_degenerate_reparam.py -- strictly-monotone-with-Phi'=0 level-set mechanism (F1 evidence).
# D=3, slice sum g = 3, coords g=(1+a,1+b,1-a-b). TRUE convention Sigma=(I-J/3)/4;
# scaled cross-check Sigma'=I-J/3=4*Sigma. Phi(u)=int_0^u (t-1/4)^2 dt: C^inf, strictly
# increasing on [0,inf), Phi'(1/4)=0. Exact sympy; deterministic. Run: python -I s2b_degenerate_reparam.py
import sys, sympy as sp
ok = True
def chk(name, cond, extra=""):
    global ok
    print("%-52s %s %s" % (name, "OK" if cond else "FAIL", extra)); ok = ok and cond
a, b, u, tt = sp.symbols("a b u t", real=True)
g = sp.Matrix([1+a, 1+b, 1-a-b])
SIG = (sp.eye(3) - sp.ones(3,3)/3)/4
SIGs = sp.eye(3) - sp.ones(3,3)/3
Q  = sp.expand((g.T*SIG*g)[0]);  Qs = sp.expand((g.T*SIGs*g)[0])
chk("true Q = (a^2+ab+b^2)/2", Q == (a**2+a*b+b**2)/2, str(Q))
chk("scaled Qs = 2(a^2+ab+b^2)", Qs == 2*(a**2+a*b+b**2), str(Qs))
chk("Qs = 4*Q (conventions rescale)", sp.simplify(Qs - 4*Q) == 0)
chk("SIG annihilates constants", (SIG*sp.ones(3,1)) == sp.zeros(3,1))
PhiP = (u - sp.Rational(1,4))**2
Phi  = sp.integrate((tt - sp.Rational(1,4))**2, (tt, 0, u))
chk("Phi' = (u-1/4)^2 >= 0, zero only at u=1/4",
    sp.simplify(sp.diff(Phi,u) - PhiP) == 0 and sp.solve(PhiP, u) == [sp.Rational(1,4)])
Cmp = sp.expand(Phi.subs(u, Q))
ga, gb = sp.diff(Cmp,a), sp.diff(Cmp,b)
chk("chain rule exact: d(Phi o Q)/da = Phi'(Q) dQ/da", sp.simplify(ga - PhiP.subs(u,Q)*sp.diff(Q,a)) == 0)
chk("chain rule exact: d(Phi o Q)/db = Phi'(Q) dQ/db", sp.simplify(gb - PhiP.subs(u,Q)*sp.diff(Q,b)) == 0)
# ellipse a^2+ab+b^2 = 1/2 (i.e. Q = 1/4 true, Qs = 1 scaled); parametrize b(a) = (-a+sqrt(2-3a^2))/2
bp = (-a + sp.sqrt(2 - 3*a**2))/2
chk("parametrisation lies on ellipse", sp.simplify((a**2+a*bp+bp**2) - sp.Rational(1,2)) == 0)
gaE = sp.simplify(ga.subs(b, bp)); gbE = sp.simplify(gb.subs(b, bp))
chk("grad(Phi o Q) = 0 on WHOLE ellipse (identically in a)", gaE == 0 and gbE == 0)
# none of these are stationary for Q: restricted grad Q != 0 on the ellipse
qga = sp.diff(Q,a).subs(b, bp); qgb = sp.diff(Q,b).subs(b, bp)
chk("grad Q != 0 at a=0 ellipse point", sp.simplify(qga.subs(a,0)) != 0 and sp.simplify(qgb.subs(a,0)) != 0)
chk("grad Q != 0 at a=1/2 ellipse point", not (sp.simplify(qga.subs(a,sp.Rational(1,2))) == 0 and sp.simplify(qgb.subs(a,sp.Rational(1,2))) == 0))
chk("ellipse avoids ker SIG on slice (Q=1/4 != 0 there)", sp.simplify((Q - sp.Rational(1,4)).subs(b, bp)) == 0)
# continuum: two distinct ellipse points give distinct non-uniform profiles
p1 = [1, 1+bp.subs(a,0), 1-bp.subs(a,0)]; p2 = [sp.Rational(1,2)+0, 0, 0]
p2 = [1+sp.Rational(1,2), 1+bp.subs(a,sp.Rational(1,2)), 1-sp.Rational(1,2)-bp.subs(a,sp.Rational(1,2))]
chk("two distinct ellipse profiles (continuum, dim 1 = D-2)", [sp.simplify(x) for x in p1] != [sp.simplify(x) for x in p2])
# gatekeeper point in scaled convention: g=(1+sqrt(1/2), 1-sqrt(1/2), 1) -> Qs = 1
gp = {a: sp.sqrt(sp.Rational(1,2)), b: -sp.sqrt(sp.Rational(1,2))}
chk("scaled circle: Qs(g)=1 and Qs=2(a^2+ab+b^2) at gatekeeper point", Qs.subs(gp) == 1)
chk("true convention: Q(g)=1/4 at gatekeeper point", Q.subs(gp) == sp.Rational(1,4))
# contrast: nowhere-vanishing-derivative reparam Psi=exp keeps locus = ker SIG on slice
E = sp.exp(Q); sol = sp.solve([sp.diff(E,a), sp.diff(E,b)], [a, b], dict=True)
chk("exp (Psi'>0 everywhere): stationary locus = {uniform} = ker SIG on slice", sol == [{a: 0, b: 0}])
# scaled-convention equivalent reparam: Phis(u)=Phi(u/4) strictly increasing, Phis'(1)=0; same level set
Phis = Phi.subs(u, u/4)
chk("scaled Phis'(u)=0 only at u=1; same level set Qs=1",
    sp.solve(sp.diff(Phis,u), u) == [1] and sp.simplify((Qs - 1).subs(b, bp)) == 0)
print("s2b SUMMARY: strictly monotone C^inf Phi with Phi'(1/4)=0 -> whole ellipse Q=1/4")
print("(=Qs=1 scaled, a^2+ab+b^2=1/2, 1-dim continuum) becomes stationary for Phi o Q;")
print("none stationary for Q; nowhere-vanishing-derivative class locus unchanged.")
print("OVERALL", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
