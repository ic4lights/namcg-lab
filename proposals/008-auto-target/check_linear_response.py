"""
Linear response of the Poisson-limit metrics to the matrix gauge potential, about a constant nondegenerate Theta_bar
(four matrix coordinates, Lorentzian eta = diag(-1,1,1,1) and Euclidean eta = 1).

Conventions (appH Presentation-A paragraph): K^{rs} = Theta^{ar} eta_{ab} Theta^{bs}, G = K^{-1}, rho = 1/|Pf Theta|, g_rho^{mu nu} = rho K^{mu nu}.
Fluctuation: Theta = Theta_bar + eps * T,  T^{mu nu} = Theta_bar^{mu r} d_r a^nu - Theta_bar^{nu r} d_r a^mu,  a^mu = u^mu cos(p.x)
  => T = -sin(p.x) (q u^T - u q^T),  q = Theta_bar p.   Amplitude of sin(p.x) in dX/d eps used below.

Claims checked (exact rational arithmetic, random Theta_bar, p, u):
 (a) dG/d eps = (G u) (.) p + n (.) m,  with a (.) b := a b^T + b a^T, n := G Theta_bar p, m := G Theta_bar eta u   [up to the factor -sin(p.x)... see code]
 (b) d ln rho / d eps  proportional to  p.u ;  u = q gives dTheta = 0, dG = 0, drho = 0.
 (c) <n,p>_K = 0 (K-orthogonality) and <n,n>_K = p^T eta^{-1} p  (so n is spacelike/transverse for K-null p unless p is eta-null).
 (d) the map u -> (dG, drho) has rank 3 (kernel spanned by q).
 (e) linearised Einstein operator about the constant background metric Gbar (and about g_rho-bar) restricted to the 3-dim image:
     rank 3, image lies in the 6-dim space of conserved symmetric tensors; so a codimension-3 subspace of conserved sources is reachable.
"""
import sympy as sp, random, itertools
random.seed(11)
def rnd_theta():
    while True:
        t = [sp.Rational(random.randint(-5, 5), random.randint(1, 3)) for _ in range(6)]
        T = sp.Matrix([[0, t[0], t[1], t[2]], [-t[0], 0, t[3], t[4]], [-t[1], -t[3], 0, t[5]], [-t[2], -t[4], -t[5], 0]])
        if T[0, 1]*T[2, 3] - T[0, 2]*T[1, 3] + T[0, 3]*T[1, 2] != 0:
            return T
def odot(a, b):
    return a*b.T + b*a.T
def run(sig):
    eta = sp.diag(sig, 1, 1, 1)
    T0 = rnd_theta()
    p = sp.Matrix([sp.Rational(random.randint(-4, 4), random.randint(1, 3)) for _ in range(4)])   # covector p_mu
    K0 = T0.T*eta*T0; G0 = K0.inv()
    Pf0 = T0[0, 1]*T0[2, 3] - T0[0, 2]*T0[1, 3] + T0[0, 3]*T0[1, 2]
    q = T0*p                                   # q^mu = Theta^{mu r} p_r
    eps = sp.symbols('eps')
    def resp(u):
        D = -(q*u.T - u*q.T)                   # coefficient of sin(p.x) in T
        Th = T0 + eps*D
        K = Th.T*eta*Th
        Gm = K.inv()
        Pf = Th[0, 1]*Th[2, 3] - Th[0, 2]*Th[1, 3] + Th[0, 3]*Th[1, 2]
        rho = 1/sp.Abs(Pf)
        sgn = sp.sign(Pf0)
        rho = sgn/Pf
        grho_up = rho*K                         # g_rho^{mu nu}
        grho = grho_up.inv()
        d = lambda M: M.applyfunc(lambda e: sp.diff(e, eps).subs(eps, 0))
        return d(Gm), sp.diff(rho, eps).subs(eps, 0), d(grho), rho.subs(eps, 0)
    u = sp.Matrix([sp.Rational(random.randint(-4, 4), random.randint(1, 3)) for _ in range(4)])
    dG, drho, dgr, rho0 = resp(u)
    n = G0*q; m = G0*T0*eta*u
    # sign: dTheta = D = -(q u^T - u q^T); formula derived for dTheta = -(...) gives dG = -[ (G u)(.)p + n (.) m ] ?  test both signs
    form = odot(G0*u, p) + odot(n, m)
    ok_plus = sp.simplify(dG - form) == sp.zeros(4, 4)
    ok_minus = sp.simplify(dG + form) == sp.zeros(4, 4)
    print("[sig=%d] (a) dG = +[(Gu)(.)p + n(.)m] : %s ;  dG = -[...] : %s" % (sig, ok_plus, ok_minus))
    print("        (b) d ln rho = %s * (p.u)" % sp.nsimplify((drho/rho0)/ (p.dot(u)) if p.dot(u) != 0 else 'NA'))
    dG_q, drho_q, dgr_q, _ = resp(q)
    print("        u = q : dG = 0:", dG_q == sp.zeros(4, 4), " drho = 0:", drho_q == 0)
    print("        (c) <n,p>_K =", sp.simplify((n.T*K0*p)[0]), "; <n,n>_K - p^T eta^{-1} p =", sp.simplify((n.T*K0*n)[0] - (p.T*eta.inv()*p)[0]))
    # (d) rank of u -> (dG, drho)
    cols = []
    cols_gr = []
    for k in range(4):
        e = sp.zeros(4, 1); e[k] = 1
        a, b, c, r0 = resp(e)
        cols.append(list(a[i, j] for i in range(4) for j in range(i, 4)) + [b])
        cols_gr.append(list(c[i, j] for i in range(4) for j in range(i, 4)) + [b])
    M = sp.Matrix(cols).T
    Mg = sp.Matrix(cols_gr).T
    print("        (d) rank of u -> (dG, drho):", M.rank(), "; rank of u -> (dg_rho, drho):", Mg.rank())
    # (e) linearised Einstein operator
    def lin_einstein(h, gb):
        gi = gb.inv()
        hu = gi*h                                        # h^a_b
        tr = sum(hu[i, i] for i in range(4))
        pu = gi*p                                        # p^a
        p2 = (p.T*pu)[0]
        ph = h*pu                                        # (h_{ab} p^b)
        pph = (pu.T*h*pu)[0]
        Ric = sp.Matrix(4, 4, lambda a, b: sp.Rational(1, 2)*(-ph[b]*p[a] - ph[a]*p[b] + p2*h[a, b] + p[a]*p[b]*tr))
        R = -pph + p2*tr
        return Ric - sp.Rational(1, 2)*gb*R
    for name, Hs, gb in (("G", [M[:10, k] for k in range(4)], G0), ("g_rho", [Mg[:10, k] for k in range(4)], (rho0*K0).inv())):
        idx = [(i, j) for i in range(4) for j in range(i, 4)]
        def tomat(v):
            h = sp.zeros(4, 4)
            for c_, (i, j) in enumerate(idx):
                h[i, j] = v[c_]; h[j, i] = v[c_]
            return h
        Es = []
        for v in Hs:
            Ev = lin_einstein(tomat(v), gb)
            # conservation: p^a E_ab = 0
            cons = (gb.inv()*p).T*Ev
            assert cons == sp.zeros(1, 4), "Bianchi identity failed"
            Es.append([Ev[i, j] for (i, j) in idx])
        rkE = sp.Matrix(Es).rank()
        # space of conserved symmetric T: p^a T_ab = 0
        syms = sp.symbols('t0:10')
        Tm = tomat(syms)
        eqs = list((gb.inv()*p).T*Tm)
        sol = sp.linsolve(eqs, syms)
        dimC = 10 - sp.Matrix([[sp.diff(e, s) for s in syms] for e in eqs]).rank()
        print("        (e) background %-5s : rank of Einstein operator on image = %d ; dim of conserved symmetric sources = %d" % (name, rkE, dimC))
for sig in (-1, 1):
    run(sig)
