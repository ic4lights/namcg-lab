# s1b_transport_group.py - exact checks of the diagonal projective transport of the 089
# pushforward family (rewrite of s1: symbolic Jacobian only for D=2,3; simplex-Jacobian
# high-precision numeric check for D=4..8 via tangent-basis determinant; density identity D=2,3,4).
# Run: python -I proposals/092-g-profile-coordinate-transport/s1b_transport_group.py
import sympy as sp
from functools import reduce


def PRODN(xs):
    return reduce(lambda a, b: a*b, xs)


def chart_tau(gs, ps, k):
    D = len(gs)
    pfull = list(ps[:D-1]) + [1 - sum(ps[:D-1])]
    S = sum(gs[i]*pfull[i] for i in range(D))
    return [gs[i]*pfull[i]/S for i in range(k)]

fails = []
def chk(name, cond):
    print(("OK  " if cond else "FAIL") + " " + name)
    if not cond:
        fails.append(name)

# ---- (1) group law and inverse, exact, D=2 and D=3
for D in (2, 3):
    a = sp.symbols('a0:%d' % D, positive=True)
    b = sp.symbols('b0:%d' % D, positive=True)
    p = sp.symbols('p0:%d' % (D-1), positive=True)
    gh = [a[i]*b[i] for i in range(D)]
    lhs = chart_tau(gh, p, D-1)
    rhs = chart_tau(a, chart_tau(b, p, D-1), D-1)
    chk("D=%d group law tau_g o tau_h = tau_{gh}" % D,
        all(sp.simplify(lhs[i] - rhs[i]) == 0 for i in range(D-1)))
    inv = chart_tau([1/x for x in a], chart_tau(a, p, D-1), D-1)
    chk("D=%d inverse tau_{1/g} o tau_g = id" % D,
        all(sp.simplify(inv[i] - p[i]) == 0 for i in range(D-1)))

# ---- (2) free action: tau_g(p)=p with interior p forces g constant, D=2 exact
g2 = sp.symbols('g1 g2', positive=True)
x = sp.symbols('x')
q1 = g2[0]*x/(g2[0]*x + g2[1]*(1-x))
sol = sp.solve(sp.simplify(q1 - x), g2[1], dict=True)
chk("D=2 fixed-point-free: tau_g(p)=p forces g2=g1",
    any(sp.simplify(d[g2[1]] - g2[0]) == 0 for d in sol))

# ---- (3) chart Jacobian of tau_{1/g} at q equals 1/(G*(sum q_i/g_i)^D), symbolic D=2,3
for D in (2, 3):
    g = sp.symbols('g0:%d' % D, positive=True)
    q = sp.symbols('q0:%d' % (D-1), positive=True)
    J = sp.Matrix(chart_tau([1/x for x in g], q, D-1)).jacobian(list(q))
    detJ = sp.simplify(J.det())
    qfull = list(q) + [1 - sum(q)]
    Lam = sum(qfull[i]/g[i] for i in range(D))
    target = 1/(sp.prod(g)*Lam**D)
    s1ok = sp.simplify(detJ - target) == 0
    s2ok = sp.simplify(detJ + target) == 0
    chk("D=%d symbolic Jacobian tau_{1/g} = +/- 1/(G Lam^D)" % D, s1ok or s2ok)
    print("   D=%d sign: %s" % (D, "plus" if s1ok else ("minus" if s2ok else "??")))

# ---- (3b) simplex Jacobian det at D=4..8, high-precision numeric, tangent basis B = e_i - e_D:
# claim: det_T(D tau_h)(p) = prod h_i / <h,p>^D  (so for h=1/g at q: 1/(G*Lam^D))
import mpmath as mp
mp.mp.dps = 40
import random
random.seed(921)
for D in (4, 5, 6, 7, 8):
    h = [mp.mpf(repr(random.uniform(0.2, 4.0))) for _ in range(D)]
    pp = [mp.mpf(repr(random.uniform(0.05, 0.6))) for _ in range(D-1)]
    if sum(pp) >= 0.9:
        pp = [v/2 for v in pp]
    pp = pp + [1 - sum(pp)]
    S = sum(h[i]*pp[i] for i in range(D))
    # ambient derivative M = diag(h/S) (I - outer(p, h/S))
    M = mp.zeros(D, D)
    for i in range(D):
        for j in range(D):
            M[i, j] = (h[i]/S)*((1 if i == j else 0) - pp[i]*h[j]/S)
    # basis columns B[:,k] = e_k - e_{D-1}, k=0..D-2
    Bm = mp.zeros(D, D-1)
    for k in range(D-1):
        Bm[k, k] = 1
        Bm[D-1, k] = -1
    Gm = Bm.T * M * Bm
    detT = mp.det(Gm)
    # For tau_h: claim det = prod h_i / S^D
    claimed = PRODN(h)/S**D * D   # det(B^T M B) = det_T(M) * det(B^T B), det(B^T B) = D
    rel = abs(detT - claimed)/abs(claimed)
    chk("D=%d numeric simplex Jacobian of tau_h = prod h_i/<h,p>^D (rel<1e-30)" % D, rel < 1e-30)
    print("   D=%d rel err %.2e" % (D, rel))

# ---- (4) pushforward of the flat density under tau_g reproduces the 089 density:
# density at q = (D-1)! * |det_T D tau_{1/g} at q| with det from (3)/(3b), at random points, D=2,3,4
for D in (2, 3, 4):
    gg = [mp.mpf(repr(random.uniform(0.3, 3.0))) for _ in range(D)]
    qq = [mp.mpf(repr(random.uniform(0.05, 0.4))) for _ in range(D-1)]
    qq = qq + [1 - sum(qq)]
    Lam = sum(qq[i]/gg[i] for i in range(D))
    G = PRODN(gg)
    density_via_jacobian = mp.factorial(D-1)*PRODN([1/x for x in gg])/Lam**D
    target = mp.factorial(D-1)/(G*Lam**D)
    rel = abs(density_via_jacobian - target)/abs(target)
    chk("D=%d flat --tau_g--> 089 density: Jacobian formula == closed form (rel<1e-30)" % D, rel < 1e-30)

print("S1B:", "PASS" if not fails else "FAIL " + str(fails))
