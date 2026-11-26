"""
s4_all_harmonic_response.py (proposal 048). Prints to stdout only; writes nothing.

Equal-weight fibre trace (V_i = V, T_i = T, all fibre transitions with the same proper-time weight), amplitudes alpha(n) with
ALL fibre harmonics, q.alpha = 0 modulo gauge.  Pointwise form (s1):
   S_E = <Q_n(alpha,alpha)> ,  Q_n = (q^2/(32 pi^2 m^4)) [ A (v.v)(alpha.alpha) + B (alpha.v)^2 ] + tree (q^2 m^2 rho_M/(4 g^2)) (alpha.alpha),
   A = (V+2T)/24,  A+B = V/8,  rho := A/(A+B) = (V+2T)/(3V).
Source: S_int = T_mu nu hbar^{mu nu} = <2 m alpha^mu T_mu nu v^nu>, hbar = fibre average of h_n = m(alpha v + v alpha).
Response: R = -(1/4) <J Q^{-1} J>, J = 2m T.v.  With u := T.v and no tree,
   <J Q^-1 J> = (4 m^2 / C) I[T],  C = q^2 A/(32 pi^2 m^4),  I[T] = < u.u/(v.v) > + (rho-1) < (v.T.v)^2/(v.v)^2 >.

Parts: (A) exact algebra; (B) null q, TT source; (C) static dust, sources S1, S2, closed forms and PV test;
(D) Galerkin truncation at fibre order N (N=1 is level one, compared with s3 and with the merged c_TT);
(E) tree term: fibre-resolved crossover factor; (F) off-shell helicity-two source.
"""
import numpy as np, sympy as sp, random
from scipy import integrate
sp_R = sp.Rational
random.seed(4804)

print("(A) exact algebra")
# trace-reversed dust squares to eta/4
eta = sp.diag(-1, 1, 1, 1)
for u3 in [(0, 0, 0), (sp_R(3, 5), 0, sp_R(4, 5) * 0), (sp_R(1, 3), sp_R(2, 3), sp_R(2, 3) * 0)]:
    uv = sp.Matrix([0, *u3]);
    u0 = sp.sqrt(1 + sum(x ** 2 for x in u3)); ul = sp.Matrix([-u0, *u3])  # lower components, u.u=-1
    Tt = ul * ul.T + eta / 2
    print("   u_i=%s: Ttilde eta^-1 Ttilde - eta/4 = 0 : %s" % (u3, (Tt * eta.inv() * Tt - eta / 4).applyfunc(sp.simplify).is_zero_matrix))
# pointwise inverse on the three-space, exact rational draws
def rrat(): return sp_R(random.randint(-9, 9), random.randint(1, 7))
ok = True
for trial in range(6):
    a_, b_ = sp_R(random.randint(1, 9), random.randint(1, 5)), sp_R(random.randint(-9, 9) or 1, random.randint(1, 5))
    G = sp.diag(a_, a_, b_)
    n = sp.Matrix([rrat(), rrat(), rrat()])                    # homogeneous in n is enough for the algebra
    Aa, Bb = sp_R(random.randint(1, 5), 7), sp_R(random.randint(-3, 5), 7)
    v2 = (n.T * G * n)[0]
    Q = Aa * v2 * G + Bb * (G * n) * (G * n).T
    if Q.det() == 0: continue
    Th = sp.Matrix(3, 3, lambda i, j: 0);
    for i in range(3):
        for j in range(i, 3): Th[i, j] = Th[j, i] = rrat()
    J = Th * n                                                  # J_i = s_i.T.v in the s-basis
    lhs = (J.T * Q.inv() * J)[0]
    u2 = (J.T * G.inv() * J)[0]; vTv = (n.T * J)[0]
    rho = Aa / (Aa + Bb)
    rhs = (u2 / v2 + (rho - 1) * vTv ** 2 / v2 ** 2) / Aa
    ok = ok and sp.simplify(lhs - rhs) == 0
print("   J Q^-1 J = [u.u/v.v + (rho-1)(v.T.v)^2/(v.v)^2]/A exactly at the sampled draws:", ok)

print("\n(B) null q: v = sqrt(a)(n1 e1 + n2 e2); T transverse traceless, T.T = 2 tau0^2/a^2 in the merged units")
th, ph = sp.symbols('theta phi', positive=True); rho = sp.Symbol('rho', positive=True)
sinth = sp.sin(th)
integrand1 = sp.Integer(1) / 2          # [u.u/v.v] = tau0^2 / a^2 on every fibre point with sin theta != 0, written per (T.T): (1/2)
# <cos^2 2phi> = 1/2 : (v.T.v)^2/(v.v)^2 = (tau0/a)^2 cos^2 2phi -> (T.T/2) cos^2 2phi
I_null = sp.integrate(sp.Integer(1) / 2 + (rho - 1) * sp.cos(2 * ph) ** 2 / 2, (ph, 0, 2 * sp.pi)) / (2 * sp.pi)
print("   I[T]/T.T =", sp.simplify(I_null), " ; (1+rho)/4 =", sp.simplify((1 + rho) / 4))
Vs, Ts = sp.symbols('V T', positive=True)
Ax = (Vs + 2 * Ts) / 24; rx = Ax / (Vs / 8)
c_eff = 8 * Ax / (1 + rx)
print("   c_TT^all = 8A/(1+rho) =", sp.factor(sp.simplify(c_eff)), " ; V=T:", sp.simplify(c_eff.subs(Vs, Ts)), " ; level-one value (2V+T)/5 ; level-one/all-harmonic at V=T:", sp.simplify(((2 * Vs + Ts) / 5).subs(Vs, Ts) / c_eff.subs(Vs, Ts)))
print("   variational inequality c_TT^level-one >= c_TT^all (2V+T)/5 - c_eff = ", sp.factor(sp.simplify((2 * Vs + Ts) / 5 - c_eff)))

print("\n(C) static dust at rest, q=(0,0,0,k), c = cos theta, r = 1/s^2, theta_ = 1+r, c0 = sqrt(r/theta_) = 1/cosh tau")
def g_closed(s2):
    r = 1 / s2; thet = 1 + r; c0 = np.sqrt(r / thet)
    return (1 - c0 * np.arctanh(c0)) / thet
def g_pv(s2, eps=1e-6):
    """principal value of int_0^1 c^2/(theta c^2 - r) dc by subtraction, numerically (not using the closed form)"""
    r = 1 / s2; thet = 1 + r; c0 = np.sqrt(r / thet)
    f = lambda c: (c ** 2 - c0 ** 2) / ((c - c0) * (c + c0)) / thet   # =1/theta : trivial part
    # c^2/(theta(c^2-c0^2)) = (1/theta)[1 + c0^2/(c^2-c0^2)]; 1/(c^2-c0^2) = (1/(2 c0)) [1/(c-c0) - 1/(c+c0)]
    pv = integrate.quad(lambda c: 1.0, 0, 1, )[0]
    w = integrate.quad(lambda c: 1.0 / (c + c0), 0, 1)[0]
    pv1 = integrate.quad(lambda c: 1.0, 0, 1, weight='cauchy', wvar=c0)[0]
    return (1 + c0 ** 2 * (pv1 - w) / (2 * c0)) / thet
for s2 in [0.5625, 1, 4, 9, 100, 1e4, 1e6]:
    print("   s^2=%-9g g(tau)=%.10f (PV numeric %.10f) ; tanh^4 tau = %.10f ; 1-g = %.3e ; 2/s^2=%.3e" % (s2, g_closed(s2), g_pv(s2), (s2 / (1 + s2)) ** 2, 1 - g_closed(s2), 2 / s2))
print("   S1, rho=1: u.u = (1/4) T00^2 v.v exactly, I = T00^2/4, G_stat/G_TT = 1 for every tau; gamma = g(tau)")
print("   S2, rho=1: u.u = -T00^2 (v^0)^2, I = T00^2 g(tau), G_stat/G_TT = 4 g(tau); hbar^{ab} = 0, gamma_PPN = 0")
# root of g
from scipy.optimize import brentq
s2star = brentq(lambda s: g_closed(s), 0.05, 5)
print("   g(tau) changes sign at s^2 = %.6f (cosh tau = %.6f, c0 = %.6f, root of c0 arctanh c0 = 1)" % (s2star, np.sqrt(1 + s2star), 1 / np.sqrt(1 + s2star)))
print("   Cassini-size check, |gamma-1| < 2.3e-5 under S1, rho=1: s^2 > about", 2 / 2.3e-5)

print("\n(D) Galerkin truncation on odd fibre orders J <= N, real spherical harmonics, Gauss-Legendre x trapezoid quadrature")
from scipy.special import sph_harm_y
def real_harmonics(N, ct, phi):
    th_ = np.arccos(ct); out = []
    for J in range(1, N + 1, 2):
        for M_ in range(-J, J + 1):
            Y = sph_harm_y(J, abs(M_), th_, phi)
            if M_ == 0: out.append(Y.real)
            elif M_ > 0: out.append(np.sqrt(2) * Y.real)
            else: out.append(np.sqrt(2) * Y.imag)
    return np.array(out)
def galerkin(N, G, Tfun, rho_, eps=0.0, nth=None, nph=None, jdim=3, vscale=1.0):
    """returns I_N defined so that I_oo = <J Q^-1 J> with Q = v.v G + (1/rho-1) (Gn)(Gn)^T (A=1), J_i = s_i.T.v = Tfun(n)_i.
       eps: v.v -> v.v + i eps vscale"""
    nth = nth or (4 * N + 60); nph = nph or (4 * N + 40)
    ct, wt = np.polynomial.legendre.leggauss(nth)
    phi = 2 * np.pi * np.arange(nph) / nph
    CT, PH = np.meshgrid(ct, phi, indexing='ij'); WT = np.outer(wt, np.ones(nph)) / (2 * nph)  # <1> = 1
    ST = np.sqrt(1 - CT ** 2)
    nx = np.array([ST * np.cos(PH), ST * np.sin(PH), CT])[:jdim if jdim == 3 else 3]
    Y = real_harmonics(N, CT.ravel(), PH.ravel()) * np.sqrt(4 * np.pi)   # normalised to <Y^2> = 1
    w = WT.ravel()
    gv = np.diag(G)
    nv = nx.reshape(3, -1)
    v2 = (gv[None, :].T * nv ** 2).sum(0) + 1j * eps * vscale
    Gn = gv[:, None] * nv
    nb = Y.shape[0]; dim = jdim * nb
    Q = np.zeros((dim, dim), complex); Jv = np.zeros(dim, complex)
    Tn = Tfun(nv)
    for i in range(jdim):
        Jv[i * nb:(i + 1) * nb] = (Y * w * Tn[i]).sum(1)
        for j in range(jdim):
            coeff = v2 * (G[i, j]) + (1 / rho_ - 1) * Gn[i] * Gn[j]
            Q[i * nb:(i + 1) * nb, j * nb:(j + 1) * nb] = (Y * (w * coeff)) @ Y.T
    sol = np.linalg.solve(Q, Jv)
    return Jv @ sol

print("   null q, a=1, TT source T^=diag(1,-1) on (s1,s2); restrict to j=1,2 (s3 is the gauge direction q). c_N in units A: c_N/A = 2 T.T/I_N, T.T = 2")
Gn0 = np.diag([1.0, 1.0, 0.0])
Tnull = lambda n: np.array([n[0], -n[1], 0 * n[0]])
for rho_ in (1.0, 0.75):
    vals = []
    for N in (1, 3, 5, 7, 9, 13, 17, 25):
        I = galerkin(N, Gn0, Tnull, rho_, jdim=2).real
        vals.append((N, 2 * 2 / I))
    print("   rho=%.2f: (N, c_N/A):" % rho_, [(n_, round(v, 5)) for n_, v in vals], " exact N=oo 8/(1+rho) =", 8 / (1 + rho_))
print("   check N=1, rho=1: c_1/A = 24/5 means c_1 = (3/5) T at A = T/8, the merged c_TT at V_i=T_i=T: printed value above")

print("\n   static dust, S1 and S2, m=k=1, r=1/s^2, axisymmetric reduction beta_1=n1 f(c), beta_2=n2 f(c), beta_3=p(c), f even, p odd, orders <= N (same space as J <= N by the symmetry)")
from numpy.polynomial import legendre as LG
def static_axial(s2, N, src, rho_, eps):
    r = 1 / s2
    nq = 3 * N + 400
    c, w = LG.leggauss(nq); w = w / 2
    def P(J):
        cf = np.zeros(J + 1); cf[J] = 1
        return LG.legval(c, cf) * np.sqrt(2 * J + 1)
    Pp = np.array([P(J) for J in range(1, N + 1, 2)]); Pf = np.array([P(J) for J in range(0, N, 2)])
    v2 = r * (1 - c ** 2) - c ** 2 + 1j * eps
    S2 = (1 - c ** 2)
    nf, np_ = Pf.shape[0], Pp.shape[0]
    Q = np.zeros((nf + np_, nf + np_), complex)
    kap_ = (1 / rho_ - 1)
    # form: v2 ( r S2 f^2 - p^2 ) + kap_ ( r S2 f - c p )^2
    Q[:nf, :nf] = (Pf * (w * (v2 * r * S2 + kap_ * (r * S2) ** 2))) @ Pf.T
    Q[nf:, nf:] = (Pp * (w * (-v2 + kap_ * c ** 2))) @ Pp.T
    Q[:nf, nf:] = (Pf * (w * (-kap_ * r * S2 * c))) @ Pp.T
    Q[nf:, :nf] = Q[:nf, nf:].T
    if src == 'S1':
        Jf = (Pf * (w * 0.5 * r * S2)).sum(1); Jp = (Pp * (w * 0.5 * c)).sum(1)
    else:
        Jf = 0 * (Pf * w).sum(1); Jp = (Pp * (w * c)).sum(1)
    Jv = np.concatenate([Jf, Jp])
    return Jv @ np.linalg.solve(Q, Jv)
def reg_exact(s2, src, eps):
    """N=oo value at rho=1 with the regulator, by quadrature of u.u/(v.v+i eps)"""
    r = 1 / s2
    if src == 'S1':
        num = lambda c: 0.25 * (r * (1 - c * c) - c * c)
    else:
        num = lambda c: -c * c
    d = lambda c: r * (1 - c * c) - c * c
    c0_ = np.sqrt(r / (1 + r))
    return integrate.quad(lambda c: num(c) * d(c) / (d(c) ** 2 + eps ** 2), 0, 1, points=[c0_], limit=4000)[0]
for s2 in (1e4, 100.0):
    for src, exact in (('S1', 0.25), ('S2', g_closed(s2))):
        row = []; eps = 0.02
        for N in (1, 3, 9, 33, 129, 513):
            row.append((N, round(float(static_axial(s2, N, src, 1.0, eps).real), 5)))
        print("   s^2=%g %s rho=1 eps=%g: I_N real part %s ; regulated N=oo %.5f ; eps->0 exact %.5f" % (s2, src, eps, row, reg_exact(s2, src, eps), exact))
def static_case(s2, N, src, rho_, eps): return static_axial(s2, N, src, rho_, eps)
print("   level one comparison: ratio G_stat/G_TT at N=1 = I_1/I_GR * c_oo/c_1 with I_GR = 1/4 at c = c_oo: s3 gives 2/3 (S1) and 8/3 (S2) at late times")
I1 = static_case(1e4, 1, 'S1', 1.0, 0.0).real; I1s = static_case(1e4, 1, 'S2', 1.0, 0.0).real
print("   N=1, s^2=1e4: I_1(S1) = %.6f -> ratio %.5f ; I_1(S2) = %.6f -> ratio %.5f (s3: 0.666311 and 2.666844)" % (I1, I1 / 0.25 * (0.6 / 0.5), I1s, I1s / 0.25 * (0.6 / 0.5)))
print("   V != T, late time limit S1: I -> rho/4 and c_stat = 4(A+B) = V/2; rho=0.75, s^2=1e6, N=513, eps=0.002 real part:", round(static_axial(1e6, 513, 'S1', 0.75, 0.002).real, 4), " rho/4 =", 0.75 / 4)

print("\n(E) tree term, rho=1 dust S1: factor <v.v/(v.v + tau)>, tau = 8 pi^2 rho_M m^6/(g^2 A) (units m k): closed form with PV, against the J=0 reading")
def crossover(s2, tp):
    """<v2/(v2+tp)> at q0=0, m=k=1: v2 = r(1-c^2) - c^2; = 1 - tp <1/(v2+tp)>, PV for P<1"""
    r = 1 / s2; thet = 1 + r; P = (r + tp) / thet
    if P < 1:
        pvint = np.arctanh(np.sqrt(P)) / np.sqrt(P)      # PV int_0^1 dc/(P - c^2)
    else:
        pvint = np.arctanh(1 / np.sqrt(P)) / np.sqrt(P)
    return 1 - tp * pvint / thet
def crossover_num(s2, tp, eps=1e-5):
    r = 1 / s2
    f = lambda c: ((r * (1 - c * c) - c * c) * (r * (1 - c * c) - c * c + tp) ) / ((r * (1 - c * c) - c * c + tp) ** 2 + eps ** 2)
    pts = None
    P = (r + tp) / (1 + r)
    if P < 1: pts = [np.sqrt(P)]
    return integrate.quad(f, 0, 1, points=pts, limit=2000)[0]
for s2, tp in [(1e4, 0.01), (1e4, 0.1), (1e4, 0.5), (1e4, 2.0), (1e4, 20.0), (100.0, 0.1), (1e4, 1e-3)]:
    # J=0 reading of (3.25): <v2>/(<v2>+tp) with <v2> = (2 r - 1)/3 ... at q0=0
    r = 1 / s2; v2m = (2 * r - 1) / 3
    print("   s^2=%-8g tau/(mk)^2=%-6g fibre-resolved=%.6f (Lorentz-regulated numeric %.6f) ; J=0 reading <v.v>/(<v.v>+tau)=%.6f" % (s2, tp, crossover(s2, tp), crossover_num(s2, tp), v2m / (v2m + tp)))
print("   IR limit tp->oo: fibre-resolved ->", round(crossover(1e4, 1e6), 8), "(screening, as in the published k->0 statement)")

print("\n(F) off-shell helicity-two source, rho=1: I[T]/T.T = (1/2) h(x), h = <x(1-c^2)/(x(1-c^2)+c^2)>, x = a/b")
def h_closed(x):
    """x>1 timelike: h = (x/(x-1)) [ 1 - arctanh(sqrt((x-1)/x))/sqrt(x(x-1)) ]"""
    return (x / (x - 1)) * (1 - np.arctanh(np.sqrt((x - 1) / x)) / np.sqrt(x * (x - 1)))
def h_num(x):
    return integrate.quad(lambda c: x * (1 - c * c) / (x * (1 - c * c) + c * c), 0, 1)[0]
for x in (1.0001, 1.5, 3.0, 10.0, 100.0, 1e4, 1e6):
    print("   x=%-8g h=%.8f numeric %.8f" % (x, h_closed(x), h_num(x)))
print("   static (x=-r): h = 1 - g(tau); late times h ~ 2/s^2 >0 . So one coefficient on helicity two holds at x = infinity only; dust is a different channel.")

print("\n(G) checks added: regulator sequence, stress entries, gamma from the pointwise solution")
for eps in (0.02, 0.002, 0.0002, 0.00002):
    print("   s^2=1e4 eps=%g: regulated N=oo I(S1) = %.6f, I(S2) = %.6f" % (eps, reg_exact(1e4, 'S1', eps), reg_exact(1e4, 'S2', eps)))
rh, pp, gs, v00, v2s = sp.symbols('rho0 p g v00 v2')
X = sp.diag(rh / 2 + pp, rh / 2, rh / 2)          # X on (time, e1, e2): T = rho0 u u + p (e1 e1 + e2 e2), Ttilde = T - eta (tr T)/2
# X v . X v = -(X00 v0)^2 + (rh/2)^2 v_a^2, with v_a^2 = v2 + v0^2
XvXv = -(rh / 2 + pp) ** 2 * v00 + (rh / 2) ** 2 * (v2s + v00)
print("   X v . X v - [ (rho0^2/4) v.v - (rho0 p + p^2) (v^0)^2 ] =", sp.expand(XvXv - (rh ** 2 / 4 * v2s - (rh * pp + pp ** 2) * v00)))
print("   so I = rho0^2/4 + g (rho0 p + p^2); GR value (1/2)(T.T - T^2/2) =", sp.expand(sp.Rational(1, 2) * (rh ** 2 + 2 * pp ** 2 - sp.Rational(1, 2) * (-rh + 2 * pp) ** 2)))
# gamma from pointwise solution, regulated average, S1 rho=1
def gamma_point(s2, eps):
    r = 1 / s2
    d = lambda c: r * (1 - c * c) - c * c
    pts = [np.sqrt(r / (1 + r))]
    f = integrate.quad(lambda c: c * c * d(c) / (d(c) ** 2 + eps ** 2), 0, 1, points=pts, limit=4000)[0]
    fa = integrate.quad(lambda c: r * (1 - c * c) * d(c) / (d(c) ** 2 + eps ** 2), 0, 1, points=pts, limit=4000)[0]
    h00 = f / 2; B = -fa / 4
    tr = -h00 + 2 * B
    E = h00 + 0.5 * tr; Ff = B - 0.5 * tr
    return E, Ff, Ff / E
for s2, eps in [(100.0, 1e-5), (9.0, 1e-5), (1e4, 1e-6)]:
    E, Ff, gm = gamma_point(s2, eps)
    print("   s^2=%g eps=%g: dhat^00 = %.6f (exact -1/4 at eps=0), dhat^11 = %.6f, gamma = %.6f, g(tau) = %.6f" % (s2, eps, E, Ff, gm, g_closed(s2)))
