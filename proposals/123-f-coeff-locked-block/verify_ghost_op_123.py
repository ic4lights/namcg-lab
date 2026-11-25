# -*- coding: ascii -*-
# Item 123 script 1: symbolic derivation of the harmonic-gauge (de Donder)
# diffeomorphism Faddeev-Popov operator in the curvature conventions of the
# manuscript (ch02 eq:christoffel and eq:riemann), and of the Hodge-de Rham
# Weitzenbock sign in the same conventions, plus the sphere sign calibration.
#
# Conventions implemented EXACTLY as displayed in the manuscript:
#   eq:christoffel:  Gamma^r_{mn} = 1/2 g^{rs}(d_m g_{ns} + d_n g_{ms} - d_s g_{mn})
#   eq:riemann:      R^r_{smn}  = d_m Gamma^r_{ns} - d_n Gamma^r_{ms}
#                              + Gamma^r_{ml} Gamma^l_{ns} - Gamma^r_{nl} Gamma^l_{ms}
#                    R_{mn} = R^r_{mrn},  R = g^{mn} R_{mn}
# These imply [d_m, d_n] v^r = R^r_{smn} v^s (Wald convention; sphere has
# positive sectional curvature; the sphere calibration below checks this).
#
# Quantities computed:
#   M^mu_nu xi^nu := dF^mu[g + eps L_xi g]/deps|0,  F^mu = g^{ab} Gamma^mu_{ab}
#     (harmonic/de Donder gauge functional; L_xi g = Lie derivative);
#   (lap xi)^mu := g^{ab} nabla_a nabla_b xi^mu (connection Laplacian);
#   (Ric xi)^mu := g^{mu k} R_{k sigma} xi^sigma;
#   result tested: M xi = lap xi + c_g * Ric xi with c_g = +1 on a family of
#     block metrics with 5 generic functions of (x0,x1), xi generic in all
#     four coordinates, coefficients of every jet of xi extracted as a poly;
#   principal symbol of M;
#   Hodge-de Rham Laplacian on 1-forms: (d delta + delta d) omega vs
#     -lap omega + c_h * Ric omega: result c_h extracted the same way;
#   2-sphere scalar curvature (expect +2, fixing the sign of "R" itself).
#
# Invariant expected outputs (checked and printed):
#   CG_GHOST = +1  (M = laplacian + Ricci endomorphism)
#   O_GHOST_EG = -Ricci  (positive Laplace-type operator O = -M has E = -R^mu_nu)
#   CH_HODGE = +1
#   SPHERE_R = +2
#   PRINCIPAL_SYMBOL_OK = PASS  (symbol of M is g^{ab} identity on vectors)
# All checks are exact (rational + generic-function arithmetic, no floats).

import sympy as sp

x = sp.symbols('x0 x1 x2 x3', real=True)
n = 4

# ---------------- generic block metric: 5 generic functions of (x0,x1) -----
u, v = x[0], x[1]
Afun = sp.Function('A')(u, v)
Bfun = sp.Function('B')(u, v)
Cfun = sp.Function('C')(u, v)
Dfun = sp.Function('D')(u, v)
Efun = sp.Function('E')(u, v)

def build_metric(A, B, Cc, Dd, Ee):
    g = sp.zeros(4, 4)
    g[0, 0] = A; g[0, 1] = B; g[1, 0] = B
    g[1, 1] = Cc
    g[2, 2] = Dd
    g[3, 3] = Ee
    return g

G0 = build_metric(Afun, Bfun, Cfun, Dfun, Efun)
GI0 = G0.inv()

def christoffel(g, gi):
    # Gamma[r, m, n] symmetric in m,n
    Gam = {}
    for r in range(n):
        for m in range(n):
            for mm in range(n):
                s = 0
                for sig in range(n):
                    s += sp.Rational(1, 2) * gi[r, sig] * (
                        sp.diff(g[mm, sig], x[m]) +
                        sp.diff(g[m, sig], x[mm]) -
                        sp.diff(g[m, mm], x[sig]))
                Gam[(r, m, mm)] = sp.expand(s)
    return Gam

def riemann(gi, Gam):
    # Riem[r,s,m,nn] = d_m Gam[r,nn,s] - d_nn Gam[r,m,s] + Gam*Gam - Gam*Gam
    Rie = {}
    for r in range(n):
        for s in range(n):
            for m in range(n):
                for nn in range(n):
                    t = sp.diff(Gam[(r, nn, s)], x[m]) - sp.diff(Gam[(r, m, s)], x[nn])
                    for l in range(n):
                        t += Gam[(r, m, l)] * Gam[(l, nn, s)] - Gam[(r, nn, l)] * Gam[(l, m, s)]
                    Rie[(r, s, m, nn)] = sp.expand(t)
    return Rie

def ricci(gi, Rie):
    # R_{mn} = R^r_{m r n}
    Rc = sp.zeros(4, 4)
    for m in range(n):
        for nn in range(n):
            t = 0
            for r in range(n):
                t += Rie[(r, m, r, nn)]
            Rc[m, nn] = sp.expand(t)
    return Rc

def scalar_r(gi, Rc):
    t = 0
    for a in range(n):
        for b in range(n):
            t += gi[a, b] * Rc[a, b]
    return sp.expand(t)

# ---------------- F^mu[g] = g^{ab} Gamma^mu_{ab} ----------------------------
def Fvec(g, gi):
    Gam = christoffel(g, gi)
    F = []
    for mu in range(n):
        t = 0
        for a in range(n):
            for b in range(n):
                t += gi[a, b] * Gam[(mu, a, b)]
        F.append(sp.expand(t))
    return F

# Lie derivative of g_{mu nu} along xi (xi given as CONTRAVARIANT components)
def lie_g(g, xi):
    h = sp.zeros(4, 4)
    for mu in range(n):
        for nu in range(n):
            t = 0
            for l in range(n):
                t += xi[l] * sp.diff(g[mu, nu], x[l])
                t += g[l, nu] * sp.diff(xi[l], x[mu])
                t += g[mu, l] * sp.diff(xi[l], x[nu])
            h[mu, nu] = sp.expand(t)
    return h

# connection Laplacian on vectors
def lap_vec(gi, Gam):
    out = []
    for mu in range(n):
        acc = 0
        for a in range(n):
            for b in range(n):
                # nabla_b xi^mu needs xi; built as operator application below
                pass
        out.append(acc)
    return out

def nabla_vec_mu(gam_xi, Gam):
    # (nabla_b xi)^mu = gam_xi[(mu,b)] + Gam[mu,b,s] xi^s
    pass

def build_xi(generic_in_all=True):
    xis = []
    for i in range(n):
        f = sp.Function('xi%d' % i)
        if generic_in_all:
            xis.append(f(*x))
        else:
            xis.append(f(u, v))
    return xis

def ric_xi(gi, Rc, xi):
    out = []
    for mu in range(n):
        t = 0
        for s in range(n):
            t += gi[mu, s] * sum(Rc[s, k] * xi[k] for k in range(n))
        out.append(sp.expand(t))
    return out

def laplacian_of(gi, Gam, xiu):
    # xiu: list of contravariant components (functions); returns g^{ab} nabla_a nabla_b xi
    out = []
    # first covariant derivative
    Dxi = {}
    for mu in range(n):
        for b in range(n):
            Dxi[(mu, b)] = sp.diff(xiu[mu], x[b]) + sum(Gam[(mu, b, s)] * xiu[s] for s in range(n))
    for mu in range(n):
        acc = 0
        for a in range(n):
            for b in range(n):
                # nabla_a (nabla_b xi)^mu
                term = sp.diff(Dxi[(mu, b)], x[a])
                for l in range(n):
                    term += Gam[(mu, a, l)] * Dxi[(l, b)]
                    term -= Gam[(l, a, b)] * Dxi[(mu, l)]
                acc += gi[a, b] * sp.expand(term)
        out.append(sp.expand(acc))
    return out

def poly_coeffs_zero(exprs, atoms, name):
    """Extract polynomial coefficients in the derivative atoms of xi; all must vanish."""
    ok = True
    bad = []
    for i, e in enumerate(exprs):
        p = sp.Poly(sp.expand(e), *atoms)
        for mon, c in zip(p.monoms(), p.coeffs()):
            if not c.is_zero:
                cs = sp.simplify(c)
                if not cs.is_zero:
                    ok = False
                    bad.append((i, mon, str(cs)[:120]))
    print("%s: %s (%d residual coefficients checked)" % (name, "PASS" if ok else "FAIL",
          sum(len(sp.Poly(sp.expand(e), *atoms).coeffs()) for e in exprs)))
    for b in bad[:6]:
        print("   BAD", b)
    return ok

print("=== item 123 script 1: conventions, ghost operator, Weitzenbock, sphere ===")

# ---------- sphere calibration (2D, but same convention code path) ---------
th, ph = sp.symbols('theta phi', real=True)
gS = sp.Matrix([[1, 0], [0, sp.sin(th)**2]])
giS = gS.inv()
# temporarily reuse code with a 2-index coordinate list via manual derivatives
def christoffel2(g, gi, xx):
    Gam = {}
    for r in range(2):
        for m in range(2):
            for mm in range(2):
                s = 0
                for sig in range(2):
                    s += sp.Rational(1, 2) * gi[r, sig] * (
                        sp.diff(g[mm, sig], xx[m]) +
                        sp.diff(g[m, sig], xx[mm]) -
                        sp.diff(g[m, mm], xx[sig]))
                Gam[(r, m, mm)] = sp.expand(s)
    return Gam

GamS = christoffel2(gS, giS, [th, ph])
RieS = {}
for r in range(2):
    for s in range(2):
        for m in range(2):
            for nn in range(2):
                t = sp.diff(GamS[(r, nn, s)], [th, ph][m]) - sp.diff(GamS[(r, m, s)], [th, ph][nn])
                for l in range(2):
                    t += GamS[(r, m, l)] * GamS[(l, nn, s)] - GamS[(r, nn, l)] * GamS[(l, m, s)]
                RieS[(r, s, m, nn)] = sp.expand(t)
RcS = sp.zeros(2, 2)
for m in range(2):
    for nn in range(2):
        RcS[m, nn] = sp.expand(sum(RieS[(r, m, r, nn)] for r in range(2)))
RS = sp.expand(sum(giS[a, b] * RcS[a, b] for a in range(2) for b in range(2)))
print("SPHERE_R =", RS, "(expected +2; convention = Wald / sphere-positive)")

# ---------- main 4D family ----------------------------------------------
Gam = christoffel(G0, GI0)
xi = build_xi(True)

# M xi = d/deps F[g + eps L_xi g] at eps=0
eps = sp.Symbol('eps')
Ge = G0 + eps * lie_g(G0, xi)
GIe = Ge.inv()
Feps = Fvec(Ge, GIe)
Mxi = [sp.simplify(sp.diff(Feps[mu], eps).subs(eps, 0)) for mu in range(n)]
Mxi = [sp.expand(sp.simplify(m)) for m in Mxi]

Rie = riemann(GI0, Gam)
Rc = ricci(GI0, Rie)
lapxi = laplacian_of(GI0, Gam, xi)
ricxi = ric_xi(GI0, Rc, xi)

res_c1 = [sp.expand(Mxi[mu] - lapxi[mu] - ricxi[mu]) for mu in range(n)]

# derivative atoms of xi up to second order
atoms = []
for mu in range(n):
    f = xi[mu]
    atoms.append(f)
    for a in range(n):
        atoms.append(sp.Derivative(f, x[a]))
    for a in range(n):
        for b in range(a, n):
            atoms.append(sp.Derivative(f, x[a], x[b]))
atoms = list(sp.Add.make_args(sp.Add(*atoms)))

ok_cg = poly_coeffs_zero(res_c1, atoms, "CG_GHOST residual M-xi-lap-Ric (c=+1)")

# uniqueness of c on the family: residual must NOT vanish for c=0
res_c0 = [sp.expand(Mxi[mu] - lapxi[mu]) for mu in range(n)]
nonzero_c0 = any((not sp.simplify(e).is_zero) for e in res_c0)
print("RICCI_TERM_NONTRIVIAL (c=0 fails on family):", "PASS" if nonzero_c0 else "FAIL")

# principal symbol of M: coefficient of d_a d_b xi^mu equals g^{ab} delta
psym_ok = True
for mu in range(n):
    p = sp.Poly(sp.expand(Mxi[mu]), *atoms)
    for mon, c in zip(p.monoms(), p.coeffs()):
        deg = sum(mon)
        if deg == 2:
            # identify which second derivative
            idx = [i for i, m2 in enumerate(mon) if m2]
            if len(idx) == 1:
                ai = idx[0]
                afun = atoms[ai]
                dvars = list(afun.expr.args[1:]) if hasattr(afun, 'expr') else []
                # map atom back
                found = False
                for nu in range(n):
                    for a2 in range(n):
                        for b2 in range(a2, n):
                            if afun == sp.Derivative(xi[nu], x[a2], x[b2]):
                                found = True
                                expected = GI0[a2, b2] * (1 if nu == mu else 0)
                                if sp.simplify(c - expected) != 0:
                                    psym_ok = False
                                    print("   PSYMBAD", mu, a2, b2, nu, c)
                if not found:
                    psym_ok = False
                    print("   PSYMUNK", afun)
print("PRINCIPAL_SYMBOL_OK:", "PASS" if psym_ok else "FAIL")

# ---------- Hodge-de Rham on 1-forms --------------------------------------
om = [sp.Function('om%d' % i)(*x) for i in range(n)]
# covariant derivative of a 1-form: D_a om_m = d_a om_m - Gam[l,a,m] om_l
Dom = {}
for a in range(n):
    for m in range(n):
        Dom[(a, m)] = sp.diff(om[m], x[a]) - sum(Gam[(l, a, m)] * om[l] for l in range(n))
# d omega: (d om)_{mn} = D_m om_n - D_n om_m
dom = {}
for m in range(n):
    for nn in range(n):
        dom[(m, nn)] = sp.expand(Dom[(m, nn)] - Dom[(nn, m)])
# delta omega = - g^{ab} D_a om_b
delom = sp.expand(-sum(GI0[a, b] * Dom[(a, b)] for a in range(n) for b in range(n)))
# d(delta omega)_m = partial_m (delta omega)
ddel = [sp.diff(delom, x[m]) for m in range(n)]
# delta(d omega)_m = - g^{a l} D_l (d om)_{a m}   with D on a 2-form
ddom = []
for m in range(n):
    acc = 0
    for a in range(n):
        for l in range(n):
            t = sp.diff(dom[(a, m)], x[l])
            for p in range(n):
                t -= Gam[(p, l, a)] * dom[(p, m)]
                t -= Gam[(p, l, m)] * dom[(a, p)]
            acc -= GI0[a, l] * t
    ddom.append(sp.expand(acc))
delR = [sp.expand(ddel[m] + ddom[m]) for m in range(n)]

# connection Laplacian on 1-forms: g^{ab} nabla_a nabla_b om_m
lapom = []
DD = {}
for a in range(n):
    for m in range(n):
        DD[(a, m)] = Dom[(a, m)]
for m in range(n):
    acc = 0
    for a in range(n):
        for b in range(n):
            t = sp.diff(DD[(b, m)], x[a])
            for l in range(n):
                t += Gam[(l, a, b)] * DD[(l, m)]   # careful: nabla_a acts, index down: - Gam
                t -= Gam[(l, a, b)] * DD[(l, m)]
                t -= Gam[(l, a, m)] * DD[(b, l)]
            acc += GI0[a, b] * sp.expand(t)
    # fix: the two Gam terms above cancel; rewrite cleanly below
    lapom.append(sp.expand(acc))
# clean rewrite (lower-index connection Laplacian):
lapom2 = []
D1 = {}
for a in range(n):
    for m in range(n):
        D1[(a, m)] = Dom[(a, m)]
D2 = {}
for a in range(n):
    for b in range(n):
        for m in range(n):
            t = sp.diff(D1[(b, m)], x[a])
            for l in range(n):
                t -= Gam[(l, a, m)] * D1[(b, l)]
                t -= Gam[(l, a, b)] * D1[(l, m)]
            D2[(a, b, m)] = sp.expand(t)
lapom2 = [sp.expand(sum(GI0[a, b] * D2[(a, b, m)] for a in range(n) for b in range(n)))
          for m in range(n)]

# Ric lowered on 1-forms: Ric_{m nu} om^nu with om^nu = g^{nu k} om_k
ricom = []
for m in range(n):
    t = 0
    for nu in range(n):
        t += Rc[m, nu] * sum(GI0[nu, k] * om[k] for k in range(n))
    ricom.append(sp.expand(t))

res_h = [sp.expand(delR[m] - (-lapom2[m]) - ricom[m]) for m in range(n)]
atoms_h = []
for m in range(n):
    atoms_h.append(om[m])
    for a in range(n):
        atoms_h.append(sp.Derivative(om[m], x[a]))
    for a in range(n):
        for b in range(a, n):
            atoms_h.append(sp.Derivative(om[m], x[a], x[b]))
atoms_h = list(sp.Add.make_args(sp.Add(*atoms_h)))
ok_ch = poly_coeffs_zero(res_h, atoms_h, "CH_HODGE residual (d delta+delta d) om + lap om - Ric om (c=+1)")

# uniqueness: c=0 fails
res_h0 = [sp.expand(delR[m] + lapom2[m]) for m in range(n)]
nonzero_h0 = any((not sp.simplify(e).is_zero) for e in res_h0)
print("HODGE_RICCI_NONTRIVIAL (c=0 fails on family):", "PASS" if nonzero_h0 else "FAIL")

# ---------- verdict on the Laplace-type endomorphism -----------------------
# M = lap + Ric (c=+1). The ghost determinant is det M; the positive
# Laplace-type operator is O_g = -M = -lap - Ric, i.e. eq:appA-O form with
# E_ghost{}^mu_nu = -R^mu_nu.  Then a_1(ghost fibre) = tr(R/6 - E)
#   = 4R/6 - tr(-Ric)/R * R = (4/6 + 1) R = (5/3) R  (unit trace E coefficient -1).
print("CG_GHOST = +1 (M = laplacian + Ricci endomorphism)")
print("O_GHOST_EG = -Ricci (E_ghost^mu_nu = -R^mu_nu, a_1 = (4/6+1) R = (5/3) R)")
print("CH_HODGE = +1 (d delta + delta d = -lap + Ric on 1-forms)")
print("SPHERE_R_CHECK =", "PASS" if RS == 2 else "FAIL")
allok = ok_cg and psym_ok and ok_ch and RS == 2 and nonzero_c0 and nonzero_h0
print("SCRIPT1 VERDICT:", "PASS" if allok else "FAIL")
raise SystemExit(0 if allok else 1)
