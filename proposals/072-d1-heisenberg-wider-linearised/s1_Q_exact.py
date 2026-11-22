"""S1 (exact, sympy).  Order-zero operator Q on the wider Heisenberg family
   [E_3, E_1] = kappa E_2,  w_a^{cd} = k_a (chi B + zeta N + x N')^{cd},  k_a = (1,0,1,0),
in the normalisation of 071 (first-order part E_a + 1/2 w S at u = 1; literal L1519 omega = -w).
Part A: Q_b[A] = nabla^a F_ab[A] - T_ab^c F^a_c[A], F_ab[A] = nabla_a A_b - nabla_b A_a + T_ab^c A_c, with
        nabla_a V_b = E_a V_b + Om_ab^c V_c, Om_ab^c = w_a^{cd} eta_db (lin.Qop convention), as differential
        operators in the coordinates of L1623.  On A = (0, phi, 0, i phi),
        phi = exp(i q0 y0 + i p y2 - kappa p ((y1)^2 + (y3)^2) / 4):
        Q_b[A] = (q0^2 - p^2 + kappa p + i chi (q0 - p)) A_b  for all kappa, chi, zeta, x (symbolic);
        F_32[A] = p phi (not a gauge direction).
Part B: the literal operators on the bundle (vector fields on (y, u), L1519 form with t_a = half the
        divergence and an order-zero fluctuation -i eps u_a^b A_b(y)): the O(eps) multiplication part of
        sum_a eta^{aa} [D_a, [D_a, D_b]] equals -i eps Q_b[A] at u = 1, for polynomial test functions A
        (numerical evaluation of exact sympy expressions at a sample point, two parameter sets).
Part C: roots and growth.  Q[A] = 0 at q0 = -i chi/2 +- sqrt((p + i chi/2)^2 - kappa p); the largest
        |Im q0| over p > 0 is |chi|/2 + kappa/4 + sqrt(kappa^2/16 + chi^2/4), attained at
        p = kappa/4 + sqrt(kappa^2/16 + chi^2/4) (closed form checked symbolically at the stationary point
        and numerically on a grid); at chi = 0 this is kappa/2 at p = kappa/2.
Part D: for arbitrary functions A_b(y) (sympy Functions), Q_b[A] - Q_b[A]|_{w=0} + chi k^a F_ab[A] = 0 for all
        kappa, chi, zeta, x (exact; k^a = (-1,0,1,0)); so Q does not depend on zeta, x, and chi enters only
        through the gauge-invariant first-order term -chi k^a F_ab[A].
Run: python -I -B s1_Q_exact.py"""
import itertools
import numpy as np
import sympy as sp

y = sp.symbols('y0:4')
kap, chi, zeta, xx, p, q0 = sp.symbols('kappa chi zeta x p q0')
eta = sp.diag(-1, 1, 1, 1)


def gen(d):
    M = sp.zeros(4, 4)
    for (c, e), v in d.items():
        M[c, e] = v; M[e, c] = -v
    return M


B = gen({(0, 2): 1}); N = gen({(0, 1): 1, (1, 2): 1}); Np = gen({(0, 3): 1, (2, 3): -1}); k = [1, 0, 1, 0]


def setup(kv, cv, zv, xv):
    Mw = cv * B + zv * N + xv * Np
    W = [[[k[a] * Mw[c, d] for d in range(4)] for c in range(4)] for a in range(4)]
    Om = [[[sum(W[a][c][d] * eta[d, b] for d in range(4)) for c in range(4)] for b in range(4)] for a in range(4)]
    C = [[[0] * 4 for _ in range(4)] for _ in range(4)]; C[3][1][2] = kv; C[1][3][2] = -kv
    T = [[[-C[a][b][c] - Om[a][b][c] + Om[b][a][c] for c in range(4)] for b in range(4)] for a in range(4)]
    return W, Om, T


def E(a, f, kv):
    if a == 0: return sp.diff(f, y[0])
    if a == 1: return sp.diff(f, y[1]) + kv * y[3] / 2 * sp.diff(f, y[2])
    if a == 2: return sp.diff(f, y[2])
    return sp.diff(f, y[3]) - kv * y[1] / 2 * sp.diff(f, y[2])


def Q(A, kv, cv, zv, xv):
    W, Om, T = setup(kv, cv, zv, xv)
    nA = [[E(a, A[b], kv) + sum(Om[a][b][z] * A[z] for z in range(4)) for b in range(4)] for a in range(4)]
    F = [[nA[a][b] - nA[b][a] + sum(T[a][b][c] * A[c] for c in range(4)) for b in range(4)] for a in range(4)]
    nF = lambda x_, a, b: E(x_, F[a][b], kv) + sum(Om[x_][a][z] * F[z][b] + Om[x_][b][z] * F[a][z] for z in range(4))
    return [sp.expand(sum(eta[x_, x_] * nF(x_, x_, b) for x_ in range(4))
                      - sum(T[a][b][c] * eta[a, a] * F[a][c] for a in range(4) for c in range(4))) for b in range(4)], F


print('== A. Q on the Heisenberg ground mode, symbolic kappa, chi, zeta, x')
phi = sp.exp(sp.I * q0 * y[0] + sp.I * p * y[2] - kap * p * (y[1] ** 2 + y[3] ** 2) / 4)
A = [0, phi, 0, sp.I * phi]
QA, F = Q(A, kap, chi, zeta, xx)
lam = q0 ** 2 - p ** 2 + kap * p + sp.I * chi * (q0 - p)
print('  Q_b[A] - lambda A_b, lambda = q0^2 - p^2 + kappa p + i chi (q0 - p):',
      [sp.simplify((QA[b] - lam * A[b]) / phi) for b in range(4)])
print('  F_32[A] / phi =', sp.simplify(F[3][2] / phi))

print('== B. literal bundle operators: O(eps) order-zero part of sum_a eta^aa [D_a,[D_a,D_b]] vs -i eps Q_b[A]')
U = sp.Matrix(4, 4, lambda i, j: sp.Symbol('u%d%d' % (i, j)))
coords = list(y) + list(U)
eps = sp.Symbol('eps')


class VF:
    def __init__(s, comp, f=0):
        s.c = [sp.sympify(v) for v in comp]; s.f = sp.sympify(f)

    def act(s, g):
        return sum(s.c[i] * sp.diff(g, coords[i]) for i in range(20))


def comm(P_, R_):
    c = [sp.expand(P_.act(R_.c[i]) - R_.act(P_.c[i])) for i in range(20)]
    return VF(c, sp.expand(P_.act(R_.f) - R_.act(P_.f)))


def build(kv, W, Atil):
    Ey = [[1, 0, 0, 0], [0, 1, kv * y[3] / 2, 0], [0, 0, 1, 0], [0, 0, -kv * y[1] / 2, 1]]
    om = [-sp.Matrix(4, 4, lambda c, d: W[b][c][d]) for b in range(4)]       # literal omega = -w
    D = []
    for a in range(4):
        comp = [0] * 20
        for b in range(4):
            for i in range(4):
                comp[i] += U[a, b] * Ey[b][i]
            omg = om[b] * eta
            for f_ in range(4):
                for c in range(4):
                    comp[4 + 4 * f_ + c] += U[a, b] * (-sum(U[f_, g] * omg[c, g] for g in range(4)))
        D.append(VF(comp))
    for a in range(4):
        dv = 0
        for b in range(4):
            omg = om[b] * eta
            Yb = VF(list(Ey[b]) + [-sum(U[f_, g] * omg[c, g] for g in range(4)) for f_ in range(4) for c in range(4)])
            dv += Yb.act(U[a, b]) + U[a, b] * sum(sp.diff(Ey[b][i], y[i]) for i in range(4))
        D[a].f = sp.expand(dv / 2 - sp.I * eps * sum(U[a, b] * Atil[b] for b in range(4)))
    return D


pt = {y[0]: sp.Rational(3, 10), y[1]: -sp.Rational(7, 10), y[2]: sp.Rational(1, 5), y[3]: sp.Rational(11, 10)}
one = {U[i, j]: (1 if i == j else 0) for i in range(4) for j in range(4)}
Atil = [y[1] * y[3] + 2 * y[0], y[2] ** 2 - y[0] * y[1], 3 * y[3] + y[0] * y[2], y[1] ** 2 - y[2] * y[3]]
for kv, cv, zv, xv in [(1, sp.Rational(1, 2), 1, -sp.Rational(1, 3)), (2, -sp.Rational(3, 2), sp.Rational(1, 2), 1)]:
    W, Om, T = setup(kv, cv, zv, xv)
    D = build(kv, W, Atil)
    Fab = {(a, b): comm(D[a], D[b]) for a in range(4) for b in range(4) if a != b}
    Qs, _ = Q(Atil, kv, cv, zv, xv)
    err = 0; err0 = 0
    for b in range(4):
        tot = sum((eta[a, a] * comm(D[a], Fab[(a, b)]).f for a in range(4) if a != b), sp.Integer(0))
        f0 = tot.subs(eps, 0).subs(one).subs(pt)
        f1 = sp.diff(tot, eps).subs(eps, 0).subs(one).subs(pt)
        err0 = max(err0, abs(complex(sp.N(f0))))
        err = max(err, abs(complex(sp.N(f1 - (-sp.I) * Qs[b].subs(pt)))))
    print('  (kappa, chi, zeta, x) = (%s, %s, %s, %s): background order-zero part %.1e ; |O(eps) part + i Q_b[A]| = %.1e'
          % (kv, cv, zv, xv, err0, err))

print('== C. roots and the largest |Im q0| of the ground mode')
S, g, kp = sp.symbols('S gamma kappa', positive=True)
pp = sp.Symbol('p', positive=True)
# sqrt((p + i g)^2 - kappa p) = X + i S with X S = g p, X^2 - S^2 = p^2 - g^2 - kappa p
f = g ** 2 * pp ** 2 / S ** 2 - S ** 2 - pp ** 2 + g ** 2 + kp * pp
Sstar = kp / 4 + sp.sqrt(kp ** 2 / 16 + g ** 2)
print('  constraint f(p, S) = 0 and df/dp = 0 at p = S = kappa/4 + sqrt(kappa^2/16 + gamma^2):',
      sp.simplify(f.subs({pp: Sstar, S: Sstar})), sp.simplify(sp.diff(f, pp).subs({pp: Sstar, S: Sstar})))
for kv, cv in [(1.0, 0.5), (1.0, -0.5), (1.3, 0.8), (1.0, 0.0)]:
    ps = np.linspace(1e-5, 40, 400001)
    gm = cv / 2
    sq = np.sqrt((ps + 1j * gm) ** 2 - kv * ps)
    im = np.maximum(np.abs((-1j * gm + sq).imag), np.abs((-1j * gm - sq).imag))
    pred = abs(gm) + kv / 4 + np.sqrt(kv ** 2 / 16 + gm ** 2)
    print('  kappa = %.2f chi = %+.2f: grid max |Im q0| = %.6f at p = %.4f ; closed form %.6f at p = %.4f'
          % (kv, cv, im.max(), ps[im.argmax()], pred, kv / 4 + np.sqrt(kv ** 2 / 16 + gm ** 2)))

print('== D. Q for arbitrary A_b(y): Q_b - Q_b|_{w=0} + chi k^a F_ab')
Af = [sp.Function('A%d' % b)(*y) for b in range(4)]
Qa, Fa = Q(Af, kap, chi, zeta, xx)
Q0, _ = Q(Af, kap, 0, 0, 0)
kup = [-1, 0, 1, 0]
print('  ', [sp.expand(Qa[b] - Q0[b] + chi * sum(kup[a] * Fa[a][b] for a in range(4))) for b in range(4)])
print('   F_ab[A] contains no w:', all(sp.expand(Fa[a][b] - Q(Af, kap, 0, 0, 0)[1][a][b]) == 0 for a in range(4) for b in range(4)))
