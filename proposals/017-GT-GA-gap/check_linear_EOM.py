"""
Linearisation of the Poisson-limit tree-level equation of motion E_nu = Theta^{mu r} d_r Theta^{mu nu} about constant Thetabar
for Theta = Thetabar + eps*T, T^{mu nu} = -(q^mu u^nu - u^mu q^nu) sin(p.x), q = Thetabar p (eta = delta):
    E_nu = -eps cos(p.x) [ q^2 u_nu - (q.u) q_nu ] = -eps cos(p.x) (M u)_nu ,  M = q^2 delta - q q   (kernel of Remark rem:ch3-trace-quadratic).
Also: rho^2 E.E = eps^2 cos^2 rho^2 u M^2 u = eps^2 cos^2 rho^2 q^2 (u M u)  (M^2 = q^2 M on the quotient u ~ q).
"""
import sympy as sp
x = sp.symbols('x1:5'); eps = sp.Symbol('eps')
a0, b0 = sp.symbols('a0 b0', positive=True)
p = sp.Matrix(sp.symbols('p1:5')); u = sp.Matrix(sp.symbols('u1:5'))
Tb = sp.zeros(4, 4); Tb[0, 1], Tb[1, 0], Tb[2, 3], Tb[3, 2] = a0, -a0, b0, -b0
q = Tb * p
th = sum(p[i] * x[i] for i in range(4))
T = -(q * u.T - u * q.T) * sp.sin(th)
Th = Tb + eps * T
E = [sum(Th[m, r] * sp.diff(Th[m, n], x[r]) for m in range(4) for r in range(4)) for n in range(4)]
E1 = [sp.expand(e).coeff(eps, 1) for e in E]
M = (q.T * q)[0] * sp.eye(4) - q * q.T
Mu = M * u
print('E^(1)_nu + cos(p.x) (M u)_nu :', [sp.simplify(E1[n] + sp.cos(th) * Mu[n]) for n in range(4)])
print('(M u).q =', sp.simplify((Mu.T * q)[0]))
