"""Delta content of the connection-sector and Dirac data on the 021 smooth family  Theta^{12} = 1/f(x1,x2), Theta^{34} = 1,
f = e^{l(x1,x2)},  rho = f,  G = diag(f^2, f^2, 1, 1).  For l = eps*ln r the distribution identities are
    Lap_0 l = 2 pi eps delta^2(x),   d_i d_j l = pi eps delta_ij delta^2(x) + (principal value part) ,
so every term linear in the second derivatives l_ij carries the delta  pi eps delta_ij delta^2 (trace part) and terms quadratic in l_i are O(eps^2).
We extract the coefficients of l_ij in  E_V  and in  Omega_12  (Vassilevich data of the vector and Dirac operators, Euclidean eta = delta),
with  O = -(G^{mn} d_m d_n + A^s d_s + B)  ->  omega_s = (1/2) G_{sn}(A^n + G^{ml} Gamma^n_{ml}),  E_V = B - G^{nm}(d_n omega_m + omega_n omega_m - omega_s Gamma^s_{nm}),  Omega_{mk} = d_m omega_k - d_k omega_m + [omega_m, omega_k]."""
import sympy as sp
x = sp.symbols('x1:5', real=True)
l = sp.Function('l')(x[0], x[1])
f = sp.exp(l)
Th = sp.zeros(4, 4); Th[0, 1] = 1/f; Th[1, 0] = -1/f; Th[2, 3] = 1; Th[3, 2] = -1
Ginv = sp.simplify(Th.T*Th)            # G^{mn} = eta_ab Th^{am} Th^{bn}
G = sp.simplify(Ginv.inv())
rho = f                                # 1/|Pf Theta| = f
sqrtG = sp.sqrt(G.det())
def christoffel(G, Gi):
    Gam = [[[0]*4 for _ in range(4)] for _ in range(4)]
    for a in range(4):
        for b in range(4):
            for c in range(4):
                Gam[a][b][c] = sp.simplify(sum(Gi[a, d]*(sp.diff(G[d, b], x[c]) + sp.diff(G[d, c], x[b]) - sp.diff(G[b, c], x[d])) for d in range(4))/2)
    return Gam
Gam = christoffel(G, Ginv)
# scalar drift: O_s = -rho^{-1} d_mu (rho K^{mu nu} d_nu .) = -(K^{mn} d_m d_n + A^n d_n),  A^n = rho^{-1} d_m (rho K^{mn})
A_s = [sp.simplify(sum(sp.diff(rho*Ginv[m, n], x[m]) for m in range(4))/rho) for n in range(4)]
def omega_E_Omega(A, B, nfib):
    C = [sum(Ginv[m, ll]*Gam[nu][m][ll] for m in range(4) for ll in range(4)) for nu in range(4)]
    om = []
    for s in range(4):
        M = sp.zeros(nfib, nfib)
        for nu in range(4):
            M += G[s, nu]*(A[nu] + C[nu]*sp.eye(nfib))
        om.append(sp.simplify(M/2))
    E = B.copy()
    for nu in range(4):
        for m in range(4):
            T = sp.diff(om[m], x[nu]) + om[nu]*om[m]
            T -= sum((om[sg]*Gam[sg][nu][m] for sg in range(4)), sp.zeros(nfib, nfib))
            E -= Ginv[nu, m]*T
    Om = [[sp.diff(om[k], x[m]) - sp.diff(om[m], x[k]) + om[m]*om[k] - om[k]*om[m] for k in range(4)] for m in range(4)]
    return om, sp.simplify(E), Om
# vector:  O_v a^mu = O_s a^mu - 2 eta^{mu alpha} {Theta_{alpha nu}, a^nu},  {Th_{an}, a^n} = Th^{rs} d_r Th_{an} d_s a^n  (Theta_{an}=Theta^{an}, eta = delta)
Av = []
for s in range(4):
    M = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            M[mu, nu] += 2*sum(Th[r, s]*sp.diff(Th[mu, nu], x[r]) for r in range(4))        # from -(A^s d_s): O contains -2 Th^{rs} d_r Th_{mu nu} d_s
        M[mu, mu] += A_s[s]
    Av.append(M)
omv, Ev, Omv = omega_E_Omega(Av, sp.zeros(4, 4), 4)
# Dirac: O_f = O_s - (1/2) gamma^{mk} {Theta_{mk}, .}
I = sp.I
s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -I], [I, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]])
Z = sp.zeros(2, 2); E2 = sp.eye(2)
gam = [sp.Matrix(sp.BlockMatrix([[Z, -I*sg], [I*sg, Z]])) for sg in (s1, s2, s3)] + [sp.Matrix(sp.BlockMatrix([[Z, E2], [E2, Z]]))]
gmn = lambda m, k: (gam[m]*gam[k] - gam[k]*gam[m])/2
Af = []
for s in range(4):
    M = sp.zeros(4, 4)
    for m in range(4):
        for k in range(4):
            coef = sum(Th[r, s]*sp.diff(Th[m, k], x[r]) for r in range(4))
            if coef != 0:
                M += coef*gmn(m, k)/2
    M += A_s[s]*sp.eye(4)
    Af.append(M)
omf, Ef, Omf = omega_E_Omega(Af, sp.zeros(4, 4), 4)
# scalar
oms, Es, Oms = omega_E_Omega([sp.Matrix([[a]]) for a in A_s], sp.zeros(1, 1), 1)
l11, l22, l12 = sp.symbols('l11 l22 l12')
def hess_coeff(M):
    M = sp.simplify(M)
    # replace second derivatives by symbols (l is only a function of x1,x2)
    rep = {sp.Derivative(l, (x[0], 2)): l11, sp.Derivative(l, (x[1], 2)): l22, sp.Derivative(l, x[0], x[1]): l12}
    M = M.subs(rep)
    return M
for name, E_, Om_ in (('scalar', Es, Oms), ('vector', Ev, Omv), ('Dirac', Ef, Omf)):
    Eh = hess_coeff(E_)
    # trace over x1,x2 hessian: delta part:  l_ij -> (1/2) delta_ij (l11 + l22)  (delta content of the Hessian of eps ln r)
    Edelta = sp.simplify(Eh.subs({l11: 1, l22: 1, l12: 0}) - Eh.subs({l11: 0, l22: 0, l12: 0}))/1
    Edelta = sp.simplify((Eh.diff(l11) + Eh.diff(l22))/2)           # coefficient of (1/2) Lap l, i.e. delta part = coeff * (pi eps) * 2 ... see below
    print(name, ': coefficient matrix c with E_G containing  c * (l11 + l22)/2 -> delta part  c * (pi eps delta^2) * [G-normalisation factor f^-2]:')
    print(sp.simplify(Eh.diff(l11)), '|', sp.simplify(Eh.diff(l22)), '|', sp.simplify(Eh.diff(l12)))
    Omh = hess_coeff(Om_[0][1])
    print(name, ' Omega_12 : d/dl11, d/dl22, d/dl12 (should vanish for second derivs; third derivatives enter):')
    print(sp.simplify(Omh))
    sp.pprint(sp.simplify(Om_[0][1]))
