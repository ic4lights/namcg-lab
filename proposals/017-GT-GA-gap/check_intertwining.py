"""
Exact symbolic check (nonlinear Poisson bivector) of the intertwining identity of proposal 017:

   O_0 (G phi) = G (O_s phi) - { E_nu , phi },      E_nu := D_mu Theta_{mu nu},

with  D_mu f = {x_mu, f} = Theta^{mu r} d_r f,   G phi = (D_nu phi)_nu,   O_s = -D_mu D_mu,
O_0 a_nu = -D_mu D_mu a_nu - 2 {Theta_{nu l}, a_l}  (Feynman-gauge connection operator of the Poisson-limit paragraph).
Consequently  G^dagger G = O_s  (w.r.t. rho d^4x) and, on E = 0,  O_kappa G = (1-kappa) G O_s  for O_kappa = O_0 - kappa G G^dagger.

Theta = (psi^* omega_bar)^{-1} = J^{-1} Thetabar J^{-T},  psi = x + w(x) (a Poisson bivector, Jacobi exact), Euclidean eta = delta.
The identity is checked at a rational point for polynomial phi, with exact rational arithmetic.
"""
import sympy as sp

x = sp.symbols('x1:5')
a0, b0 = sp.Integer(2), sp.Rational(3, 2)
Tb = sp.zeros(4, 4)
Tb[0, 1], Tb[1, 0], Tb[2, 3], Tb[3, 2] = a0, -a0, b0, -b0
w = [x[1] * x[2] / 5 + x[3] ** 2 / 7, x[0] * x[3] / 6 - x[2] ** 2 / 9, x[0] * x[1] / 8 + x[0] * x[3] / 11, x[2] * x[1] / 10 - x[0] ** 2 / 13]
J = sp.Matrix(4, 4, lambda i, j: sp.KroneckerDelta(i, j) + sp.diff(w[i], x[j]))
Jinv = J.adjugate() / J.det()
Th = (Jinv * Tb * Jinv.T)
pt = {x[0]: sp.Rational(1, 3), x[1]: sp.Rational(-1, 4), x[2]: sp.Rational(1, 5), x[3]: sp.Rational(1, 2)}

# Jacobi identity check at the point (numerical-exact)
def br(f, g):
    return sum(Th[m, n] * sp.diff(f, x[m]) * sp.diff(g, x[n]) for m in range(4) for n in range(4))

jac = 0
for (i, j, k) in [(0, 1, 2), (0, 2, 3), (1, 2, 3), (0, 1, 3)]:
    xi, xj, xk = x[i], x[j], x[k]
    jac += abs(sp.nsimplify((br(xi, br(xj, xk)) + br(xj, br(xk, xi)) + br(xk, br(xi, xj))).subs(pt)))
print('Jacobi residual (4 triples, exact):', jac)

def D(m, f):
    return sum(Th[m, r] * sp.diff(f, x[r]) for r in range(4))

phi = x[0] ** 2 * x[2] + 3 * x[1] * x[3] ** 2 - x[0] * x[1] * x[3] + x[2] ** 3
Gphi = [D(n, phi) for n in range(4)]
Os = lambda f: -sum(D(m, D(m, f)) for m in range(4))
E = [sum(D(m, Th[m, n]) for m in range(4)) for n in range(4)]

def O0(a):
    out = []
    for n in range(4):
        t = -sum(D(m, D(m, a[n])) for m in range(4))
        Y = sum(br(Th[n, l], a[l]) for l in range(4))
        out.append(t - 2 * Y)
    return out

lhs = O0(Gphi)
rhs = [D(n, Os(phi)) - br(E[n], phi) for n in range(4)]
res = [sp.nsimplify((lhs[n] - rhs[n]).subs(pt)) for n in range(4)]
print('residual O0 G phi - G Os phi + {E,phi} at the point:', res)
print('magnitudes at the point: |O0 G phi| =', [sp.N(sp.nsimplify(lhs[n].subs(pt)), 6) for n in range(4)])
print('E at the point:', [sp.N(sp.nsimplify(E[n].subs(pt)), 6) for n in range(4)], ' (nonzero: background is off shell)')
# rho-weighted divergence-free property: d_r(rho Theta^{n r}) = 0  (so D_mu is anti-self-adjoint on L^2(rho d^4x), G^dagger G = O_s)
rho = 1 / (Th[0, 1] * Th[2, 3] - Th[0, 2] * Th[1, 3] + Th[0, 3] * Th[1, 2])
print('d_r(rho Theta^{n r}) at the point:', [sp.nsimplify(sum(sp.diff(rho * Th[n, r], x[r]) for r in range(4)).subs(pt)) for n in range(4)])
