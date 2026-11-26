"""
Proposal 021, script 2: first-order Weitzenboeck identity in the Poisson-limit class (exact, symbolic).

Class: omega = Theta^{-1} closed, omega = omega_bar + eps d A  with an ARBITRARY constant antisymmetric invertible omega_bar and
four arbitrary functions A_nu(x0..x3);  G = omega omega^T,  rho = |Pf omega|,  g_rho = G / rho (det g_rho = const).
To first order in eps:
   (1)  R_G^{(1)}  =  - 2 box_{G0} (delta ln rho)                      (so a first-order curvature delta forces a singular rho)
   (2)  R[g_rho]^{(1)} (with g_rho,0 = G0/rho0) = rho0 * box_{G0} (delta ln rho)  ... printed as a ratio
   (3)  E_s^{(1)} = -1/2 box delta ln rho = + 1/4 R_G^{(1)}  and  rho R[g_rho]^{(1)} = -1/2 R_G^{(1)}  (the factor -1/2 between the two readings)
Linearised scalar curvature: R^{(1)}[g0,h] = g0^{ma} g0^{nb} d_m d_n h_{ab} - g0^{mn} g0^{ab} d_m d_n h_{ab}.
"""
import sympy as sp

x = sp.symbols('x0:4')
eps = sp.symbols('eps')
Rat = sp.Rational
A = [sp.Function(f'A{i}')(*x) for i in range(4)]
ob = sp.Matrix([[0, 2, 1, -1], [-2, 0, 3, 1], [-1, -3, 0, 5], [1, -1, -5, 0]]) * Rat(1, 3)       # generic antisymmetric
assert ob.det() != 0
dA = sp.Matrix(4, 4, lambda m, n: sp.diff(A[n], x[m]) - sp.diff(A[m], x[n]))                       # closed: d(dA) = 0


def pf(M):
    return M[0, 1] * M[2, 3] - M[0, 2] * M[1, 3] + M[0, 3] * M[1, 2]


# first-order metric perturbation and density perturbation
h = ob * dA.T + dA * ob.T                        # d/deps (omega omega^T) at eps=0
G0 = ob * ob.T
G0i = G0.inv()
pf0 = pf(ob)
dpf = sp.diff(pf(ob + eps * dA), eps).subs(eps, 0)
dlnrho = sp.simplify(dpf / pf0)                  # delta ln rho (rho = |Pf omega|, sign constant)
rho0 = abs(pf0)


def lin_R(g0i, hh):
    t1 = 0
    t2 = 0
    for m in range(4):
        for n in range(4):
            for a in range(4):
                for b in range(4):
                    d = sp.diff(hh[a, b], x[m], x[n])
                    t1 += g0i[m, a] * g0i[n, b] * d
                    t2 += g0i[m, n] * g0i[a, b] * d
    return sp.expand(t1 - t2)


def box(f):
    return sum(G0i[m, n] * sp.diff(f, x[m], x[n]) for m in range(4) for n in range(4))


R1 = lin_R(G0i, h)
print('(1) R_G^(1) + 2 box_G0 delta ln rho =', sp.simplify(R1 + 2 * sp.expand(box(dlnrho))))
# g_rho = G/rho: g0 = G0/rho0, perturbation h' = h/rho0 - G0 delta rho/rho0^2, delta rho = rho0 delta ln rho
g0i = rho0 * G0i
hp = h / rho0 - G0 * dlnrho / rho0
Rg1 = lin_R(g0i, hp)
print('(2) R[g_rho]^(1) / (rho0 box_G0 delta ln rho) =', sp.simplify(Rg1 / (rho0 * sp.expand(box(dlnrho)))), '   (g_rho inverse metric is rho0 G0^{-1})')
print('    => rho0 R[g_rho]^(1) - rho0^2 box_G0 dlnrho = ', sp.simplify(rho0 * Rg1 - rho0**2 * sp.expand(box(dlnrho))))
print('    ratio  R[g_rho]^(1) * (1/rho0) / R_G^(1)  [with R[g_rho] in the g_rho-units]:', sp.simplify(Rg1 / rho0 / R1) if R1 != 0 else None)
print('(3) E_s^(1) = -1/2 box dlnrho ; E_s^(1) - R_G^(1)/4 =', sp.simplify(-sp.Rational(1, 2) * sp.expand(box(dlnrho)) - R1 / 4))
