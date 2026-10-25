"""043 / s1: the rigid eta-rotation as a Poisson-limit matrix gauge transformation, and its charge.

Conventions: script indices 0..3 are the manuscript x^1..x^4; Sigma = {x^1 = x^2 = 0}.
{f,g} = Theta^{mu nu} d_mu f d_nu g, Theta = omega^{-1} (omega_{mu rho} Theta^{rho nu} = delta).
(iota_xi omega)_l = xi^n omega_{n l}.  Hamiltonian field of eps: zeta^n = Theta^{m n} d_m eps.
Euclidean: xi = rotation of the (x^1,x^2) plane.  Lorentzian (x^1 time): xi = boost of that plane.

Checks, for omega = omega_bar + dA with omega_bar constant in span{e12,e34} and A a generic polynomial
1-form invariant under xi (so that omega is closed, xi-invariant and NOT of the diagonal family):
 (a) L_xi omega = 0 (tensorial Lie derivative).
 (b) eps := radial integral of iota_xi omega satisfies d eps = iota_xi omega exactly.
 (c) zeta = xi, i.e. {eps, f} = xi^n d_n f for every f (numerical at random points, f generic).
 (d) eps = 0 and d eps = 0 on Sigma; the Hessian of eps on Sigma equals B^T omega (B^n_k = d_k xi^n),
     is symmetric (equivalent to L_xi omega = 0 at Sigma) and nonzero.
 (e) in the matrix chart {eps, x^a} = xi^a = B^a_b x^b (the rigid eta-rotation).
 (f) linearised gauge transformation da^mu = {lam, x^mu} gives dA_nu = d_nu lam for A_nu = a^mu omega_{mu nu}.
 (g) gauge charge of a curvature density: for L = sqrt(G) R_G and zeta = xi on a constant background,
     the Komar/Iyer-Wald density sqrt(G)(G^{ma} d_a zeta^n - G^{na} d_a zeta^m) on Sigma is nonzero
     although eps and d eps vanish there: the charge depends on second derivatives of eps.
"""
import random
import sympy as sp

x = sp.symbols('x1:5', real=True)
X = sp.Matrix(x)
random.seed(43)


def lie_two_form(xi, om):
    n = 4
    L = sp.zeros(n, n)
    for a in range(n):
        for b in range(n):
            L[a, b] = sum(xi[c] * sp.diff(om[a, b], x[c]) for c in range(n)) \
                + sum(om[c, b] * sp.diff(xi[c], x[a]) for c in range(n)) \
                + sum(om[a, c] * sp.diff(xi[c], x[b]) for c in range(n))
    return L.applyfunc(sp.expand)


def lie_one_form(xi, A):
    return [sp.expand(sum(xi[c] * sp.diff(A[b], x[c]) for c in range(4)) +
                      sum(A[c] * sp.diff(xi[c], x[b]) for c in range(4))) for b in range(4)]


def rpoly(vars_, deg):
    terms = [sp.Integer(1)]
    for d in range(1, deg + 1):
        for v in vars_:
            terms.append(v ** d)
    terms += [vars_[i] * vars_[j] for i in range(len(vars_)) for j in range(i + 1, len(vars_))]
    return sum(sp.Rational(random.randint(-3, 3), random.randint(1, 3)) * t for t in terms)


cases = {
    'Euclidean rotation': ([-x[1], x[0], 0, 0], x[0] ** 2 + x[1] ** 2,
                           [-x[1], x[0], 0, 0]),          # alpha = x1 dx2 - x2 dx1
    'Lorentzian boost': ([x[1], x[0], 0, 0], x[1] ** 2 - x[0] ** 2,
                         [x[1], -x[0], 0, 0]),             # alpha = x2 dx1 - x1 dx2
}
allok = True
for name, (xi, u, alpha) in cases.items():
    xi = [sp.sympify(c) for c in xi]
    du = [sp.diff(u, v) for v in x]
    inv = [u, x[2], x[3]]
    a_, b_, c_, d_ = (rpoly(inv, 2) for _ in range(4))
    A = [sp.expand(a_ * alpha[i] + b_ * du[i] + c_ * (1 if i == 2 else 0) + d_ * (1 if i == 3 else 0))
         for i in range(4)]
    LA = lie_one_form(xi, A)
    omb = sp.zeros(4, 4)
    abar, cbar = sp.Rational(3, 2), sp.Rational(-2, 1)
    omb[0, 1], omb[1, 0], omb[2, 3], omb[3, 2] = abar, -abar, cbar, -cbar
    dA = sp.Matrix(4, 4, lambda i, j: sp.expand(sp.diff(A[j], x[i]) - sp.diff(A[i], x[j])))
    om = omb + dA
    ok_a = lie_two_form(xi, om) == sp.zeros(4, 4) and all(t == 0 for t in LA)
    iota = [sp.expand(sum(xi[n] * om[n, l] for n in range(4))) for l in range(4)]
    t = sp.symbols('t')
    eps = sp.integrate(sum(iota[l].subs({x[k]: t * x[k] for k in range(4)}, simultaneous=True) * x[l]
                           for l in range(4)), (t, 0, 1))
    eps = sp.expand(eps)
    ok_b = all(sp.expand(sp.diff(eps, x[l]) - iota[l]) == 0 for l in range(4))
    # (c) numerical: zeta = Theta^T d eps equals xi at random points; generic f
    errs = []
    for _ in range(5):
        pt = {v: sp.Rational(random.randint(-9, 9), random.randint(2, 7)) for v in x}
        omn = om.subs(pt)
        if omn.det() == 0:
            continue
        Th = omn.inv()
        grad = sp.Matrix([sp.diff(eps, v).subs(pt) for v in x])
        zeta = Th.T * grad                       # zeta^n = Theta^{m n} d_m eps
        errs.append(max(abs(zeta[n] - sp.sympify(xi[n]).subs(pt)) for n in range(4)))
    ok_c = len(errs) > 0 and max(errs) == 0
    on_sigma = {x[0]: 0, x[1]: 0}
    ok_d0 = sp.simplify(eps.subs(on_sigma)) == 0 and all(sp.simplify(sp.diff(eps, v).subs(on_sigma)) == 0 for v in x)
    B = sp.Matrix(4, 4, lambda n, k: sp.diff(xi[n], x[k]))
    H = sp.Matrix(4, 4, lambda k, l: sp.diff(eps, x[k], x[l])).subs(on_sigma)
    BTom = (B.T * om).subs(on_sigma)
    ok_d1 = (H - BTom).applyfunc(sp.expand) == sp.zeros(4, 4)
    ok_d2 = (BTom - BTom.T).applyfunc(sp.expand) == sp.zeros(4, 4) and H != sp.zeros(4, 4)
    # (e) matrix chart: {eps, x^a} = zeta^a = xi^a = B^a_b x^b (xi linear)
    ok_e = all(sp.expand(xi[a] - sum(B[a, b] * x[b] for b in range(4))) == 0 for a in range(4))
    print(f"[{name}] (a) L_xi omega=0, L_xi A=0: {ok_a}; (b) d eps = iota_xi omega: {ok_b}; "
          f"(c) zeta = xi at {len(errs)} random points (max err {max(errs) if errs else None}): {ok_c}")
    print(f"   (d) eps, d eps = 0 on Sigma: {ok_d0}; Hess eps|Sigma = B^T omega: {ok_d1}; symmetric and nonzero: {ok_d2}")
    print(f"   Hess eps on Sigma (rows 1,2): {[list(H.row(i)) for i in range(2)]}")
    print(f"   (e) xi^a = B^a_b x^b (rigid eta-rotation in the matrix chart): {ok_e}")
    allok &= all([ok_a, ok_b, ok_c, ok_d0, ok_d1, ok_d2, ok_e])

# (f) linearised gauge transformation on A_nu = a^mu omega_{mu nu}, constant omega
lam = sp.Function('lam')(*x)
om = sp.Matrix([[0, 2, 0, 1], [-2, 0, 3, 0], [0, -3, 0, 5], [-1, 0, -5, 0]])
Th = om.inv()
da = [sum(Th[r, m] * sp.diff(lam, x[r]) for r in range(4)) for m in range(4)]   # {lam, x^m}
dA = [sp.simplify(sum(da[m] * om[m, n] for m in range(4))) for n in range(4)]
ok_f = all(sp.simplify(dA[n] - sp.diff(lam, x[n])) == 0 for n in range(4))
print(f"(f) da^mu = {{lam, x^mu}} gives dA = d lam on A_nu = a^mu omega_mu_nu (U(1) at linear order): {ok_f}")

# (g) Komar density of sqrt(G) R_G for zeta = xi, constant omega in span{e12,e34}, both signatures
for name, eta, xi in [('Euclidean', sp.diag(1, 1, 1, 1), [-x[1], x[0], 0, 0]),
                      ('Lorentzian', sp.diag(-1, 1, 1, 1), [x[1], x[0], 0, 0])]:
    om = sp.zeros(4, 4)
    om[0, 1], om[1, 0], om[2, 3], om[3, 2] = sp.Rational(3, 2), -sp.Rational(3, 2), -2, 2
    G = om * eta.inv() * om.T                      # G = omega gamma^{-1} omega^T, gamma = eta
    Gi = G.inv()
    sq = sp.sqrt(abs(G.det()))
    dz = sp.Matrix(4, 4, lambda a, n: sp.diff(xi[n], x[a]))     # d_a zeta^n (constant: Christoffels vanish)
    Q = sp.Matrix(4, 4, lambda m, n: sq * (sum(Gi[m, a] * dz[a, n] for a in range(4)) -
                                           sum(Gi[n, a] * dz[a, m] for a in range(4))))
    print(f"(g) [{name}] Komar density of sqrt(G)R_G on Sigma for the gauge field zeta = xi: "
          f"Q^12 = {sp.nsimplify(Q[0, 1])}, nonzero: {Q[0, 1] != 0}")
    allok &= Q[0, 1] != 0
allok &= ok_f
print("ALL CHECKS PASSED" if allok else "SOME CHECK FAILED")
