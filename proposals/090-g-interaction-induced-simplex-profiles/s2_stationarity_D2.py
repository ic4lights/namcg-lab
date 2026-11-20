import sympy as sp
# D=2 profile-simplex stationary point of L = (a-1)*(log p1 + log p2) + b*log|p1-p2|, p1+p2=1.
# Chamber p1 > p2: p1 = (1+u)/2, p2 = (1-u)/2, 0 < u < 1.
a, b, u = sp.symbols('a beta u', positive=True)
p1 = (1+u)/2
p2 = (1-u)/2
L = (a-1)*(sp.log(p1)+sp.log(p2)) + b*sp.log(p1-p2)
dL = sp.simplify(sp.diff(L, u))
print('dL_du:', sp.factor(sp.together(dL)))
sol = sp.solve(sp.numer(sp.numer(dL)*u if False else sp.numer(dL)), u)
print('critical_u:', [sp.simplify(s) for s in sol])
ustar = sp.sqrt(b/(b+2*(a-1)))
res = sp.simplify(sp.together(dL.subs({u: ustar})))
print('residual_at_ustar:', res)
d2 = sp.simplify(sp.diff(L, u, 2).subs({u: ustar}))
print('d2L_at_ustar_sgneg_form:', sp.simplify(d2), ' is_negative:', sp.simplify(d2 < 0))
onset = sp.limit(ustar/sp.sqrt(b), b, 0)
print('ONSET_slope_u_over_sqrtbeta_as_beta0:', onset, ' i.e. u ~ sqrt(beta/(2(a-1)))')
tail = sp.limit((1-ustar)*b, b, sp.oo)
print('TAIL_(1-u)*beta_as_beta_inf:', tail)
u_a1 = sp.simplify(ustar.subs({a: 1}))
print('a1_u:', u_a1, ' -> u==1: vertex-only maximizer, no interior point at a=1')
# check the a=1 vertex claim directly: max of (2t-1)^b * (t(1-t))^0 on (1/2,1) is at t=1 for any b>0
t = sp.symbols('t', positive=True)
g = (2*t-1)**b
print('a1_interior_critical_count:', len(sp.solve(sp.diff(sp.log(g), t), t)))
print('S2_D2 OK')
