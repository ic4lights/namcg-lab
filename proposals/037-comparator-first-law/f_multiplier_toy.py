"""037-f: composite constraint omega = F[theta] = theta*theta' (1-D toy of omega = Theta dTheta).  Extended Lagrangian L_ext = (1/2) omega'^2 + lam (omega - theta theta')
versus the composite Lagrangian L_c = (1/2) ((theta theta')')^2.  The omega-equation fixes lam = omega''; substituting it, the theta-equation of L_ext equals the chain-rule Euler-Lagrange expression of L_c."""
import sympy as sp
from sympy.calculus.euler import euler_equations
x = sp.symbols('x'); th = sp.Function('th')(x); om = sp.Function('om')(x); lam = sp.Function('lam')(x)
Lext = om.diff(x)**2/2 + lam*(om - th*th.diff(x))
eqs = euler_equations(Lext, [th, om, lam], x)
e_th, e_om, e_lam = [e.lhs - e.rhs for e in eqs]
Lc = ((th*th.diff(x)).diff(x))**2/2
e_c = euler_equations(Lc, [th], x)[0]; e_c = e_c.lhs - e_c.rhs
lam_sol = sp.solve(e_om, lam)[0]
sub = e_th.subs(lam, lam_sol).subs(om, th*th.diff(x)).doit()
print('lambda =', lam_sol)
print('theta-equation of L_ext with lambda eliminated and omega = F[theta]:', sp.simplify(sub))
print('Euler-Lagrange of composite L_c                                    :', sp.simplify(e_c))
print('difference:', sp.simplify(sub - e_c), ' or sum:', sp.simplify(sub + e_c))
