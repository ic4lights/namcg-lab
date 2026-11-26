"""
Identify the degenerate eigenspaces of  Q_h u = lambda M_Max u  (on the gauge quotient) and test whether the induced
linear metric perturbation h1 = d g_rho/d eps (and rho1) is transverse-traceless with respect to p and the background g_rho.
Usage: python check_tt_content.py s0 a0 b0 p0 p1 p2 p3
"""
import sympy as sp, sys
s0 = sp.Rational(sys.argv[1]); a0 = sp.Rational(sys.argv[2]); b0 = sp.Rational(sys.argv[3])
pv = [sp.Rational(v) for v in sys.argv[4:8]]
fn = 'quadratic_forms_s%s_a%s_b%s.srepr' % (s0, a0, b0)
data = eval(open(fn).read(), sp.__dict__)
Mh, Mx = data['Lh'], data['Lx']
n = 4
p = sp.symbols('p0:4'); sub = dict(zip(p, pv))
eta = sp.diag(s0, 1, 1, 1); etai = eta.inv()
Tb = sp.zeros(4, 4); Tb[0, 1] = a0; Tb[1, 0] = -a0; Tb[2, 3] = b0; Tb[3, 2] = -b0
q = Tb*sp.Matrix(pv); ql = eta*q; q2 = (q.T*eta*q)[0]
MMax = q2*eta - ql*ql.T
Qh = Mh.subs(sub)
# generalized eigenproblem on full space with gauge direction q projected out: use M_Max + c * (eta-dual of q) to fix the null direction
# eigenvectors of  Qh u = lam MMax u  with u defined mod q.   Use sympy: solve (Qh - lam MMax) u = 0 via nullspace for each lam.
lam = sp.symbols('lam')
# characteristic values on quotient
for drop in range(4):
    if q[drop] != 0: break
idx = [i for i in range(4) if i != drop]
E = sp.zeros(4, 3)
for c, i in enumerate(idx): E[i, c] = 1
cp = sp.factor((E.T*Qh*E - lam*E.T*MMax.subs(sub)*E).det())
roots = sp.roots(sp.Poly(cp, lam))
print("eigenvalues (with multiplicity):", roots)
# linear metric perturbation from u:  A = u cos(th):  T^{mn} = i-like; use cos/sin pair -> take real amplitude with A=u*cos, T = -(Tb p)(.)sin ; h1 linear in T
Tm = lambda u_: sp.Matrix(n, n, lambda m, k: -(q[m]*u_[k] - q[k]*u_[m]))    # coefficient of sin(th) in T (dA = -p sin)
def h_of(u_):
    eps = sp.symbols('eps')
    Th = Tb + eps*Tm(u_)
    dual = lambda M: sp.Matrix(n, n, lambda m, k: sum(sp.LeviCivita(m, k, r, s)*M[r, s] for r in range(n) for s in range(n))/2)
    Pf = Th[0, 1]*Th[2, 3] - Th[0, 2]*Th[1, 3] + Th[0, 3]*Th[1, 2]
    Ts = dual(Th)
    g = (Ts*etai*Ts.T)/Pf
    return g.applyfunc(lambda e: sp.diff(e, eps).subs(eps, 0)), g.subs(eps, 0), sp.diff(1/Pf, eps).subs(eps, 0)
g0 = None
for lv, mult in roots.items():
    M0 = (Qh - lv*MMax.subs(sub))
    ns = M0.nullspace()
    # remove the gauge vector q from the nullspace description
    print("lambda =", lv, "mult", mult, "nullspace dim (full space, includes gauge q):", len(ns))
    for v in ns:
        h, g0, rho1 = h_of(list(v))
        g0i = g0.inv()
        trh = sum(g0i[a, b]*h[a, b] for a in range(n) for b in range(n))
        ph = sp.Matrix([sum(g0i[a, b]*pv[a]*h[b, c] for a in range(n) for b in range(n)) for c in range(n)])   # p^b h_bc
        print("   vec", list(v), "  tr h =", sp.simplify(trh), "  p^a h_ac =", list(sp.simplify(ph)), "  rho1 =", sp.simplify(rho1))

# ---- TT projection test: for each eigenvector compare  <FP(h)> with  -1/4 rho0 p^2_g |h_TT|^2   (TT part w.r.t. p and background g0)
def fp_value(h, rho0, rho1, g0):
    g0i = g0.inv()
    th_ = sp.symbols('th_')
    # plane wave h(x)=h sin(p.x)  ->  average of quadratic forms: <d d> = p p /2 ; use direct contraction with amplitude only
    P_ = sp.Matrix(pv)
    hup = g0i*h*g0i
    tr = sum(g0i[a, b]*h[a, b] for a in range(n) for b in range(n))
    dd = sum(g0i[l, k]*pv[l]*pv[k] for l in range(n) for k in range(n))
    contr = sum(g0i[m, a]*g0i[nn, b]*h[m, nn]*h[a, b] for m in range(n) for nn in range(n) for a in range(n) for b in range(n))
    divh = [sum(pv[m]*hup[m, nn] for m in range(n)) for nn in range(n)]
    t2 = sum(g0[nn, k]*divh[nn]*divh[k] for nn in range(n) for k in range(n))
    t3 = tr*sum(pv[nn]*divh[nn] for nn in range(n))
    t4 = dd*tr**2
    # all with the same overall 1/2 from averaging sin^2:  L_FP -> 1/2*[ -1/4 dd*contr + 1/2 t2 - 1/2 t3 + 1/4 t4 ]
    LFP = sp.Rational(1, 2)*(-sp.Rational(1, 4)*dd*contr + sp.Rational(1, 2)*t2 - sp.Rational(1, 2)*t3 + sp.Rational(1, 4)*t4)
    return LFP
def tt_norm(h, g0):
    g0i = g0.inv()
    pu = g0i*sp.Matrix(pv); p2 = (sp.Matrix(pv).T*pu)[0]
    Pr = g0 - sp.Matrix(pv)*sp.Matrix(pv).T/p2          # transverse projector, lower indices
    Pup = g0i*Pr                                         # P^a_b
    hT = Pup.T*h*Pup                                     # (P h P)_{ab}
    trT = sum(g0i[a, b]*hT[a, b] for a in range(n) for b in range(n))
    hTT = hT - Pr*trT/3
    contr = sum(g0i[m, a]*g0i[nn, b]*hTT[m, nn]*hTT[a, b] for m in range(n) for nn in range(n) for a in range(n) for b in range(n))
    return contr, p2
print("TT-projection test (value of FP form vs -1/4*rho0*p2*|h_TT|^2/2):")
for lv, mult in roots.items():
    ns = (Qh - lv*MMax.subs(sub)).nullspace()
    for v in ns:
        h, g0, rho1 = h_of(list(v))
        rho0 = None
        fpv = fp_value(h, None, rho1, g0)
        c, p2 = tt_norm(h, g0)
        print("  lam=", lv, "vec", list(v), " FP(h) =", sp.simplify(fpv), "  -1/4*p2*|hTT|^2/2 =", sp.simplify(-sp.Rational(1, 8)*p2*c), "  ratio-diff =", sp.simplify(fpv + sp.Rational(1, 8)*p2*c))
