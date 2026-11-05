"""052 s3: linear algebra of the label forms and the reflection sign of the Gaussian two-point function.  Exact (sympy) except part D, numerical.

A. Krein relation: a positive form G on the translations with G = P^2 (eta + 2 n n), the second moments of a Gaussian weight in the rest frame n,
   satisfies theta_n G = P^2 eta as a bilinear form, for theta_n = 1 + 2 n n^T eta the reflection along n; both sides covariant under a boost.  A weight with G_00 != G_11 does not give a multiple of eta.
B. so(3,1) with the form kappa(lam,lam) = (1/2) lam_cd lam^cd has signature (3,3); majorant |E|^2+|B|^2 with reflection boost -> -boost.
C. At null q != 0: restrict the forms to q.g = 0 on translations and q_c lam^{cd} = 0 on so(3,1).  Signature on the whole, on the restriction, radical, quotient.
   Count with the two transverse polarisations: 20 = 12 + 8 under the product form; on the restriction 6 positive and 6 null.  Gauge compatibility of the constraints at linear order.
D. Reflection positivity of the scalar kernel D(y,y') = 1/(4 pi^2 |theta y - y'|^2) and of <F_12 F_12> at sampled points with y^0 > 0, and the sign with a theta-odd label.
E. Left-invariant backgrounds: background equation eta^{ac} ad_a ad_c = 0, and the stabiliser of the structure constants inside so(3,1), for two algebras and the Isono-Tomino frame.
Seeded where random.  Requires sympy and numpy."""
import itertools
import numpy as np
import sympy as sp

R = sp.Rational
eta = sp.diag(-1, 1, 1, 1)


def boost(ch, sh):
    """exact rational boost along axis 3, ch^2 - sh^2 = 1."""
    assert ch ** 2 - sh ** 2 == 1
    L = sp.eye(4)
    L[0, 0] = ch
    L[3, 3] = ch
    L[0, 3] = sh
    L[3, 0] = sh
    return L


# A
P = sp.Symbol('P', positive=True)
n_up = sp.Matrix([1, 0, 0, 0])
G_rest = P ** 2 * sp.eye(4)  # second moments p_g p_h of a Gaussian of variance P^2 per component, lower indices
n_low = eta * n_up
assert G_rest == P ** 2 * (eta + 2 * n_low * n_low.T)
theta = sp.eye(4) + 2 * n_up * n_low.T  # acts on upper index: t -> -t, x -> x
assert theta == sp.diag(-1, 1, 1, 1)
# the bilinear form G_gh theta^h_k
assert sp.simplify(G_rest * theta - P ** 2 * eta) == sp.zeros(4)
L = boost(R(5, 4), R(3, 4))
Linv = eta * L.T * eta
assert Linv * L == sp.eye(4)
# the weight is pushed forward: p_low -> L^{-T} p_low, so G -> Linv.T G Linv in lower indices, and theta -> L theta Linv
G_b = Linv.T * G_rest * Linv
theta_b = L * theta * Linv
assert sp.simplify(G_b * theta_b - P ** 2 * eta) == sp.zeros(4)
assert G_b != G_rest
print('A. G theta = P^2 eta in the rest frame and after a boost (ch,sh)=(5/4,3/4); boosted G has G_00 =', G_b[0, 0], ', G_03 =', G_b[0, 3])
G_aniso = sp.diag(3, 1, 1, 1)
m = G_aniso * theta
assert not any(sp.simplify(m - c * eta) == sp.zeros(4) for c in (1, 3))
print('   anisotropic moments diag(3,1,1,1): G theta =', list(m.diagonal()), 'not a multiple of eta')
print('   any positive G: G_00 >= 0 and G_11 >= 0, so G is never a nonzero multiple of eta itself (merged statement).')

# B, C
pairs = list(itertools.combinations(range(4), 2))


def biv(i):
    a, b = pairs[i]
    M = sp.zeros(4)
    M[a, b] = 1
    M[b, a] = -1
    return M  # lam^{ab}, upper indices


def kappa(l1, l2):
    low1 = eta * l1 * eta
    return sum(low1[a, b] * l2[a, b] for a in range(4) for b in range(4)) / 2


K = sp.Matrix(6, 6, lambda i, j: kappa(biv(i), biv(j)))
print('B. pairs', pairs, ' kappa diag', list(K.diagonal()))
assert K == sp.diag(*[(-1 if 0 in pairs[i] else 1) for i in range(6)])
assert sum(1 for i in range(6) if K[i, i] > 0) == 3


def signature(M, tol=0):
    ev = M.eigenvals()
    p = sum(mu for v, mu in ev.items() if sp.N(v) > 1e-12)
    q = sum(mu for v, mu in ev.items() if sp.N(v) < -1e-12)
    z = sum(mu for v, mu in ev.items() if abs(sp.N(v)) <= 1e-12)
    return p, q, z


def restrict(form, basis):
    B = sp.Matrix.hstack(*basis)
    return B.T * form * B


def analyse(q_up):
    q_low = eta * q_up
    assert (q_up.T * q_low)[0] == 0 and q_up != sp.zeros(4, 1)
    # translations: label vector g^mu with form eta; constraint q_low . g = 0
    ker_t = (q_low.T).nullspace()
    Gr = restrict(eta, ker_t)
    sig_t = signature(Gr)
    # so(3,1): lam -> q_c lam^{cd}
    Cm = sp.zeros(4, 6)
    for j in range(6):
        v = biv(j).T * q_low  # q_c lam^{cd}
        for r in range(4):
            Cm[r, j] = v[r]
    rank = Cm.rank()
    ker_l = Cm.nullspace()
    Kr = restrict(K, ker_l)
    sig_l = signature(Kr)
    # image lies in q-perp
    im = Cm.columnspace()
    assert all((q_low.T * v)[0] == 0 for v in im)
    # whole-space
    return dict(sig_eta=signature(eta), sig_kappa=signature(K), ker_t=len(ker_t), sig_t=sig_t, rank=rank, ker_l=len(ker_l), sig_l=sig_l, image_dim=len(im))


for q in (sp.Matrix([1, 0, 0, 1]), sp.Matrix([5, 3, 0, 4]), sp.Matrix([13, 3, 4, 12])):
    res = analyse(q)
    print('C. q =', list(q), res)
    assert res['sig_eta'] == (3, 1, 0) and res['sig_kappa'] == (3, 3, 0)
    assert res['sig_t'] == (2, 0, 1)
    assert res['rank'] == 3 and res['ker_l'] == 3 and res['sig_l'] == (1, 0, 2)
pos_all = 2 * (3 + 3)
neg_all = 2 * (1 + 3)
print('   count on 2 polarisations x (4 + 6) labels: positive', pos_all, ', negative', neg_all, ', total', pos_all + neg_all)
assert pos_all + neg_all == 20
print('   restricted: positive', 2 * (2 + 1), ', null', 2 * (1 + 2), ', removed by the constraints', 2 * (1 + 3))
assert 2 * (2 + 1) + 2 * (1 + 2) + 2 * (1 + 3) == 20
print('   odd number of time indices among h_i^mu, omega_i^{cd}: h_i^0 (2) + omega_i^{0j} (6) =', 2 + 6)
# gauge compatibility: delta f_b^g = q_b eps^g, q_g delta f_b^g = q_b (q.eps): needs q.eps = 0; delta f_b^{cd} = q_b eps^{cd}: needs q_c eps^{cd} = 0.
# free local parameters left in position space: 4 - 1 = 3 for the translations; for the bivector, 6 - 3 = 3, since rank is 3 at null q (generic q: rank?)
q_gen = sp.Matrix([1, 2, 3, 5])
q_low = eta * q_gen
Cm = sp.Matrix(4, 6, lambda r, j: (biv(j).T * q_low)[r])
print('   rank of lam -> q_c lam^{cd} at non-null q:', Cm.rank(), '; so the bivector constraint leaves', 6 - Cm.rank(), 'parameters of six at each momentum')
assert Cm.rank() == 3
# closure of the bivector constraint: two parameters with zero divergence, bracket has a divergence in general
x = sp.symbols('x0:4')
eta_np = eta


def div_biv(L_):
    return [sum(sp.diff(L_[c, d], x[c]) * eta[c, c] for c in range(4)) for d in range(4)]


f1, f2 = x[2], x[3]
e1 = sp.zeros(4)
e1[0, 1] = f1
e1[1, 0] = -f1
e2 = sp.zeros(4)
e2[1, 2] = f2
e2[2, 1] = -f2
assert all(v == 0 for v in div_biv(sp.Matrix(e1))) or True
d1 = div_biv(e1)
d2 = div_biv(e2)
comm = e1 * eta * e2 - e2 * eta * e1
d3 = div_biv(comm)
print('   example: e1 = x2 (0^1), e2 = x3 (1^2): div e1 =', d1, ', div e2 =', d2, ', div [e1,e2] =', d3)
assert all(v == 0 for v in d1) and all(v == 0 for v in d2)
assert any(v != 0 for v in d3)

# D reflection positivity kernels
rng = np.random.default_rng(52003)
n = 60
pts = rng.normal(size=(n, 4))
pts[:, 0] = np.abs(pts[:, 0]) + 0.2
th = np.array([-1.0, 1, 1, 1])
refl = pts * th
D = np.zeros((n, n))
F = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        r = refl[i] - pts[j]
        r2 = r @ r
        D[i, j] = 1.0 / (4 * np.pi ** 2 * r2)
        # <F_12(y) F_12(y')> = -(d_1^2 + d_2^2) D(y-y') with D = 1/(4 pi^2 r^2): d_i^2 D = (8 r_i^2/r2 - 2) / (4 pi^2 r2^2)
        F[i, j] = -((8 * r[1] ** 2 / r2 - 2) + (8 * r[2] ** 2 / r2 - 2)) / (4 * np.pi ** 2 * r2 ** 2)
evD = np.linalg.eigvalsh((D + D.T) / 2)
evF = np.linalg.eigvalsh((F + F.T) / 2)
print('D. min eigenvalue of the reflected kernel: D', evD.min(), ', <F12 F12>', evF.min(), '; relative to max', evD.min() / evD.max(), evF.min() / evF.max())
assert evD.min() > -1e-10 * evD.max() and evF.min() > -1e-10 * evF.max()
print('   with a theta-odd label the reflected kernel is minus this: max eigenvalue of -D', (-evD).max(), ' <= 0; min', (-evD).min(), ' < 0')
assert (-evD).min() < 0

# E left-invariant backgrounds; indices 0,1,2,3 orthonormal; f[a][b] = vector of [E_a, E_b]^c


def bg_check(name, brackets, eta_=eta):
    f = {}
    for a in range(4):
        for b in range(4):
            f[a, b] = sp.zeros(4, 1)
    for (a, b), v in brackets.items():
        v = sp.Matrix(v)
        f[a, b] = v
        f[b, a] = -v
    # ad_a: matrix (ad_a)^c_b = coefficient of E_c in [E_a,E_b]
    ad = [sp.Matrix.hstack(*[f[a, b] for b in range(4)]) for a in range(4)]
    # Jacobi
    for a, b, c in itertools.product(range(4), repeat=3):
        v = ad[a] * f[b, c] + ad[b] * f[c, a] + ad[c] * f[a, b]
        assert v == sp.zeros(4, 1), ('Jacobi', a, b, c)
    cas = sp.zeros(4)
    for a in range(4):
        cas += eta_[a, a] * ad[a] * ad[a]
    # stabiliser in so(3,1) acting on the frame index: lam acts on E_b by (lam_low)_b^c, derivation condition
    unknown = sp.symbols('l0:6')
    M = sp.zeros(4)
    for i, (a, b) in enumerate(pairs):
        M[a, b] = unknown[i]
        M[b, a] = -unknown[i]
    A = M * eta_  # A^a_b = lam^{ac} eta_cb; derivation D(E_b) = A^c_b E_c
    eqs = []
    for a in range(4):
        for b in range(4):
            # D[E_a,E_b] = [D E_a, E_b] + [E_a, D E_b]
            lhs = A * f[a, b]
            rhs = sp.zeros(4, 1)
            for c in range(4):
                rhs += A[c, a] * f[c, b] + A[c, b] * f[a, c]
            eqs += list(lhs - rhs)
    sol = sp.linsolve([e for e in eqs if e != 0], list(unknown)) if any(e != 0 for e in eqs) else None
    if sol is None:
        dim = 6
    else:
        s = list(sol)[0]
        dim = len(set(v for e in s for v in e.free_symbols))
    print('E.', name, ': eta^{ac} ad_a ad_c =', 'zero' if cas == sp.zeros(4) else list(cas), '; dim of stabiliser of f in so(3,1) =', dim)
    return cas, dim


m_ = R(1)
# null rotation: E_+ = (E_0+E_3)/sqrt2 is awkward over Q; use E_p = E_0 + E_3, E_m = (E_3 - E_0)/2 with eta(E_p,E_m) = 1.  In an orthonormal basis the same algebra has
# [E_0 + E_3, E_1] = m E_2, [E_0 + E_3, E_2] = - m E_1: write separately on (E_0, E_3)
br = {(0, 1): [0, 0, m_ / 2, 0], (3, 1): [0, 0, m_ / 2, 0], (0, 2): [0, -m_ / 2, 0, 0], (3, 2): [0, -m_ / 2, 0, 0]}
cas, dim = bg_check('null rotation algebra [E_0+E_3, E_1] = E_2, [E_0+E_3, E_2] = -E_1', br)
assert cas == sp.zeros(4)
cas, dim = bg_check('same algebra, Euclidean contraction', br, sp.eye(4))
print('   (the equation fails for the Euclidean contraction when the result above is not zero)')
# solvable, non-unimodular: [E_0,E_2] = E_2, [E_0,E_3] = E_3, [E_1,E_2] = E_2, [E_1,E_3] = -E_3
br2 = {(0, 2): [0, 0, 1, 0], (0, 3): [0, 0, 0, 1], (1, 2): [0, 0, 1, 0], (1, 3): [0, 0, 0, -1]}
cas, dim = bg_check('solvable algebra with commuting ad_0 = 1, ad_1 = diag(1,-1) on (E_2,E_3)', br2)
assert cas == sp.zeros(4)
# Euclidean contraction solution: ad_0 scale, ad_1 rotation on (E_2,E_3)
br3 = {(0, 2): [0, 0, 1, 0], (0, 3): [0, 0, 0, 1], (1, 2): [0, 0, 0, 1], (1, 3): [0, 0, -1, 0]}
cas, dim = bg_check('solvable algebra with ad_0 = 1, ad_1 = rotation on (E_2,E_3), Euclidean contraction', br3, sp.eye(4))
assert cas == sp.zeros(4)
cas, dim = bg_check('same, Lorentzian contraction', br3)
assert cas != sp.zeros(4)

# Isono-Tomino curvature-less frame, as first-order operators: e_0 = d_t, e_i = (alpha - t) d_i
t, x1, x2, x3, al = sp.symbols('t x1 x2 x3 alpha')
co = (t, x1, x2, x3)


def lie(u, v):
    return [sum(u[j] * sp.diff(v[i], co[j]) - v[j] * sp.diff(u[i], co[j]) for j in range(4)) for i in range(4)]


frame = [[1, 0, 0, 0], [0, al - t, 0, 0], [0, 0, al - t, 0], [0, 0, 0, al - t]]
for name, sig in (('Lorentzian', (-1, 1, 1, 1)), ('Euclidean', (1, 1, 1, 1))):
    res = []
    for b in range(4):
        tot = [0, 0, 0, 0]
        for a in range(4):
            v = lie(frame[a], lie(frame[a], frame[b]))
            tot = [tot[i] + sig[a] * v[i] for i in range(4)]
        res.append([sp.simplify(c) for c in tot])
    print('E. frame e_0 = d_t, e_i = (alpha-t) d_i,', name, 'contraction: [e^a,[e_a,e_b]] =', res)
    assert all(c == 0 for r in res for c in r)
print('ALL ASSERTIONS PASSED')
