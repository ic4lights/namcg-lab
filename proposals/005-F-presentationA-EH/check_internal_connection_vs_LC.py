"""
Compare the internal-index connection of the Poisson-limit gauge-field operator, omega^{int}_sigma = -1/2 d_sigma ln rho + B_sigma,
with the Levi-Civita spin connection of G in the frame e^alpha_nu = omega_nu^alpha (omega = Theta^{-1}), block family.
Internal index alpha of A^alpha = frame index of the covector a_rho = e_rho^alpha A_alpha  (A^alpha = Theta^{alpha rho} a_rho).
"""
import sympy as sp
x = sp.symbols('x0:4'); n = 4
a = sp.Function('a')(x[0], x[1]); b = sp.Function('b')(x[2], x[3])
eta = sp.diag(-1, 1, 1, 1); etai = eta.inv()
Th = sp.zeros(4, 4); Th[0, 1] = a; Th[1, 0] = -a; Th[2, 3] = b; Th[3, 2] = -b
rho = 1/(a*b)
K = Th.T*eta*Th; G = K.inv(); Gi = K
Thl = eta*Th*eta
Gam = [[[sum(Gi[l, d]*(sp.diff(G[d, bb], x[c]) + sp.diff(G[d, c], x[bb]) - sp.diff(G[bb, c], x[d])) for d in range(n))/2 for c in range(n)] for bb in range(n)] for l in range(n)]
om = Th.inv()                       # omega_{nu B}
e = om*etai                          # e_nu^A  (A upper)  row index nu
ei = e.inv()                         # (e^{-1})^A_nu?  ei[A, nu]:  e_nu^A (e^{-1})_A^rho = delta
# spin connection  w_sigma^A_B = e^A_rho (d_sigma E^rho_B + Gamma^rho_{sigma lam} E^lam_B),  E^rho_B = (e^{-1})[B?]  inverse frame:  E_B^rho with  e_rho^A E_B^rho = delta^A_B
E = e.inv()                          # E[A, rho]  satisfies e*E = 1 -> sum_rho e[nu?]...
# e as matrix e[nu, A]; inverse frame E[A, nu] with sum_nu E[A,nu] e[nu,B] = delta
wLC = []
for s in range(n):
    M = sp.zeros(n, n)
    for A_ in range(n):
        for B_ in range(n):
            M[A_, B_] = sum(e[r, A_]*(sp.diff(E[B_, r], x[s]) + sum(Gam[r][s][l]*E[B_, l] for l in range(n))) for r in range(n))
    wLC.append(M.applyfunc(sp.simplify))
Bs = lambda s_, m, nn: sum(Th[r, s_]*sp.diff(Thl[m, nn], x[r]) for r in range(n))
lnr = sp.log(rho)
for s in range(n):
    Bm = sp.Matrix(n, n, lambda m, nn: sum(etai[m, k]*Bs(s, k, nn) for k in range(n)))
    wint = (-sp.Rational(1, 2)*sp.diff(lnr, x[s])*sp.eye(n) + Bm)
    # drift: Gi-index conventions: omega_sigma lower index = G_{sigma tau} omega^tau ; here B_s defined with sigma upper -> lower with G
    print("sigma=", s)
    print("  LC spin connection w_sigma{}^A_B :", wLC[s].tolist())
print("B^sigma (mixed, upper sigma) matrices  B^sigma{}^mu_nu :")
for s in range(n):
    Bm = sp.Matrix(n, n, lambda m, nn: sum(etai[m, k]*Bs(s, k, nn) for k in range(n))).applyfunc(sp.simplify)
    print("  sigma^", s, Bm.tolist())
print("omega^sigma_lower = G_{sigma tau} B^tau :")
for s in range(n):
    Bl = sum((G[s, t]*sp.Matrix(n, n, lambda m, nn: sum(etai[m, k]*Bs(t, k, nn) for k in range(n))) for t in range(n)), sp.zeros(n, n)).applyfunc(sp.simplify)
    print("  sigma_", s, Bl.tolist())
