import sympy as sp
r, C, c = sp.symbols('r C c', positive=True)
for sig in (1, -1):
    for Cs in (C, -C):
        h = c*(1 + sig*sp.sqrt(1 - Cs/r**4))
        hp = sp.diff(h, r); hpp = sp.diff(h, r, 2)
        ode = 2*h**2*r*hpp + 10*h**2*hp + 4*h*r*hp**2 + r**2*hp**3
        print('sigma', sig, 'C sign', 'C' if Cs == C else '-C', '-> ODE residual:', sp.simplify(ode))
# alpha, beta, ratio
s = sp.symbols('s', positive=True)
h = c*(1 + sp.sqrt(1 - C/r**4))
alpha = sp.simplify(r*sp.diff(h, r) + 2*h); beta = 2*h
print('alpha/beta =', sp.simplify(alpha/beta), ' ; 1/sqrt(1-C/r^4) =', 1/sp.sqrt(1 - C/r**4))
