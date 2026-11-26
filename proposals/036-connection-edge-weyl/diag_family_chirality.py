"""Exact delta content of the vector bundle curvature for the diagonal family Theta^{12} = exp(-l1), Theta^{34} = s*exp(-l2), s = +1 (background Theta-bar self-dual,
Theta-bar^{12} = Theta-bar^{34}) and s = -1 (anti-self-dual), l_i = eps c_i ln r.  Same conventions as 035 diag_family_holonomy.py (Vassilevich data of the vector operator).
Output: the delta part of Omega_12 (Hessian-linear part, Hess l_i -> pi eps c_i delta_ab) for s = +-1, i.e. the holonomy H = c_a J_12 + s c_b J_34 for the family with |Theta^{34}| = r^{-eps c_b}."""
import sympy as sp
x = sp.symbols('x1:5', real=True)
l1 = sp.Function('l1')(x[0], x[1]); l2 = sp.Function('l2')(x[0], x[1])
def holonomy(s):
    Th = sp.zeros(4, 4); Th[0, 1] = sp.exp(-l1); Th[1, 0] = -sp.exp(-l1); Th[2, 3] = s*sp.exp(-l2); Th[3, 2] = -s*sp.exp(-l2)
    Ginv = sp.simplify(Th.T*Th); G = sp.simplify(Ginv.inv()); rho = sp.exp(l1+l2)
    Gam = [[[sp.simplify(sum(Ginv[a, d]*(sp.diff(G[d, b], x[c])+sp.diff(G[d, c], x[b])-sp.diff(G[b, c], x[d])) for d in range(4))/2) for c in range(4)] for b in range(4)] for a in range(4)]
    A_s = [sp.simplify(sum(sp.diff(rho*Ginv[m, n], x[m]) for m in range(4))/rho) for n in range(4)]
    Av = []
    for sidx in range(4):
        M = sp.zeros(4, 4)
        for mu in range(4):
            for nu in range(4):
                M[mu, nu] += 2*sum(Th[r, sidx]*sp.diff(Th[mu, nu], x[r]) for r in range(4))
            M[mu, mu] += A_s[sidx]
        Av.append(M)
    C = [sum(Ginv[m, q]*Gam[nu][m][q] for m in range(4) for q in range(4)) for nu in range(4)]
    om = [sp.simplify(sum((G[sidx, nu]*(Av[nu] + C[nu]*sp.eye(4)) for nu in range(4)), sp.zeros(4, 4))/2) for sidx in range(4)]
    Om12 = sp.simplify(sp.diff(om[1], x[0]) - sp.diff(om[0], x[1]) + om[0]*om[1] - om[1]*om[0])
    a11, a12, a22, b11, b12, b22 = sp.symbols('a11 a12 a22 b11 b12 b22')
    rep = {sp.Derivative(l1, (x[0], 2)): a11, sp.Derivative(l1, x[0], x[1]): a12, sp.Derivative(l1, (x[1], 2)): a22,
           sp.Derivative(l2, (x[0], 2)): b11, sp.Derivative(l2, x[0], x[1]): b12, sp.Derivative(l2, (x[1], 2)): b22}
    Om12h = Om12.subs(rep)
    z = {sp.Derivative(l1, x[0]): 0, sp.Derivative(l1, x[1]): 0, sp.Derivative(l2, x[0]): 0, sp.Derivative(l2, x[1]): 0}
    lin = Om12h.applyfunc(lambda e: sp.simplify(sp.expand(e).subs(z)))
    La, Lb = sp.symbols('La Lb')
    delta = lin.subs({a11: La, a22: La, a12: 0, b11: Lb, b22: Lb, b12: 0}).applyfunc(sp.simplify)
    # evaluate at l1=l2=0 (the profile is l_i = eps c_i ln r, regular normalisation at |x|=1)
    delta0 = delta.subs({l1: 0, l2: 0}).doit().applyfunc(sp.simplify)
    return delta0
La, Lb = sp.symbols('La Lb')
J12 = sp.zeros(4, 4); J12[0, 1] = 1; J12[1, 0] = -1
J34 = sp.zeros(4, 4); J34[2, 3] = 1; J34[3, 2] = -1
for s in (1, -1):
    d = holonomy(s)
    # d = -2 La J12 - 2 s Lb J34 (Omega_12 = d/dx1 omega_2 - d/dx2 omega_1 ; delta^2 coefficient)
    h12 = sp.simplify(d[0, 1] / (-2*La)); h34 = sp.simplify(d[2, 3] / (-2*Lb))
    print('s = %+d (%s): delta part of Omega_12 = %s' % (s, 'SD' if s == 1 else 'ASD', d.tolist()))
    print('   holonomy coefficients  H = %s * c_a J_12 + %s * c_b J_34' % (h12, h34))
