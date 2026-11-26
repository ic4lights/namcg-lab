import sympy as sp
a, b = sp.symbols('a beta', positive=True)
sig = sp.symbols('sigma', positive=True)
t = sp.symbols('tau', positive=True)
p, q1, q2 = sp.symbols('p q1 q2', positive=True)
E2 = [t*p, t*(1-p)]
assert sp.expand(sp.Matrix(E2).jacobian([t, p]).det()) == -t
print('JAC_D2_abs_eq_tau1: True')
L2 = (a-1)*(sp.log(E2[0])+sp.log(E2[1])) + b*sp.log(sp.Abs(E2[0]-E2[1])) - (E2[0]+E2[1])/sig + sp.log(t)
M2 = (a-1)*(sp.log(p)+sp.log(1-p)) + b*sp.log(sp.Abs(2*p-1)) - t/sig + (2*a+b-1)*sp.log(t)
d2 = sp.simplify(sp.expand_log(L2 - M2, force=True))
assert d2 == 0, d2
print('FACTOR_D2_logsplit_zero_general: True')
P3 = [1-q1-q2, q1, q2]
E3 = [t*x for x in P3]
assert sp.expand(sp.Matrix(E3).jacobian([t, q1, q2]).det()) == t**2
print('JAC_D3_abs_eq_tau2: True')
L3 = (a-1)*sum(sp.log(x) for x in E3) + b*(sp.log(sp.Abs(E3[0]-E3[1]))+sp.log(sp.Abs(E3[0]-E3[2]))+sp.log(sp.Abs(E3[1]-E3[2]))) - t/sig + 2*sp.log(t)
M3 = (a-1)*sum(sp.log(x) for x in P3) + b*(sp.log(sp.Abs(P3[0]-P3[1]))+sp.log(sp.Abs(P3[0]-P3[2]))+sp.log(sp.Abs(P3[1]-P3[2]))) - t/sig + (3*a+3*b-1)*sp.log(t)
d3 = sp.simplify(sp.expand_log(L3 - M3, force=True))
assert d3 == 0, d3
print('FACTOR_D3_logsplit_zero_general: True')
I2 = sp.integrate(t**(2*a+b-1)*sp.exp(-t/sig), (t, 0, sp.oo))
I3 = sp.integrate(t**(3*a+3*b-1)*sp.exp(-t/sig), (t, 0, sp.oo))
print('TAU_LAW_D2:', sp.simplify(I2))
print('TAU_LAW_D3:', sp.simplify(I3))
print('CONVENTION tau_exponent = D*a + beta*D*(D-1)/2 - 1')
print('S1 OK')
