# s2f_dirichlet_var.py - exact D=2 Dirichlet(a,a) variance, the beta=0 comparator of the insert.
# Also: for the flat member (a=1) u=|2x-1| has density 1 on (0,1), so P(u<eps)=eps by inspection;
# the beta=2 member gives eps^3 (s2b_exact_d2_stats_v2.py (3e)).
# Run: python -I proposals/091-g-core-induced-pair-correlation/s2f_dirichlet_var.py
import sympy as sp
a = sp.symbols('a', positive=True)
x = sp.symbols('x', positive=True)
dens = x**(a-1)*(1-x)**(a-1)
Zn = sp.integrate(dens, (x, 0, 1))
m1 = sp.simplify(sp.integrate(x*dens, (x, 0, 1))/Zn)
m2 = sp.simplify(sp.integrate(x**2*dens, (x, 0, 1))/Zn)
V = sp.simplify(m2 - m1**2)
print("(f) Dirichlet(a,a) D=2: E[x] =", m1, " Var(x) =", V, " ; == 1/(4(2a+1)):",
      bool(sp.simplify(V - 1/(4*(2*a+1))) == 0))
print("S2F DONE")
