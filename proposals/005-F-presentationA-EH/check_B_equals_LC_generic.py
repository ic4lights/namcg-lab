"""
Generic Darboux-pushforward check (same setup as check_vector_sector_generic.py) that the internal-index connection
B_c = G_{cd} B^d  (B^d{}^mu_nu = eta^{mu k} Theta0^{d b} d_b Theta_{k nu})  equals the Levi-Civita spin connection of G in the coframe
e_c{}^A = (Theta0^{-1} J^{-1} eta^{-1})_{cA}   (= omega_{nu B} eta^{BA} pulled to y-coordinates),
    w_c{}^A{}_B = e_d^A ( d_c E_B^d + Gamma^d_{c l} E_B^l ),   E = e^{-1}.
Evaluated at a rational point.
"""
import sympy as sp, random
random.seed(11)
y = sp.symbols('y0:4'); n = 4
eta = sp.diag(-1, 1, 1, 1); etai = eta.inv()
Th0 = sp.zeros(4, 4); Th0[0, 1] = 1; Th0[1, 0] = -1; Th0[2, 3] = 1; Th0[3, 2] = -1
Th0i = Th0.inv()
c = [sp.Rational(random.randint(-4, 4), 10) for _ in range(8)]
phi = [y[0] + c[0]*y[0]**2, y[1] + c[1]*y[0]*y[1] + c[2]*y[0]**2, y[2] + c[3]*y[1]**2 + c[4]*y[0]*y[2],
       y[3] + c[5]*y[2]*y[3] + c[6]*y[0]*y[1] + c[7]*y[3]**2]
J = sp.Matrix(n, n, lambda m, a: sp.diff(phi[m], y[a])); Ji = J.inv()
pt = {y[0]: sp.Rational(1, 7), y[1]: sp.Rational(-1, 5), y[2]: sp.Rational(1, 6), y[3]: sp.Rational(1, 9)}
Thx = J*Th0*J.T; Thl = eta*Thx*eta
G = Th0i*(Ji*etai*Ji.T)*Th0i.T; Gi = (Ji*(Thx.T*eta*Thx)*Ji.T)
Gam = [[[sum(Gi[l, d]*(sp.diff(G[d, a], y[b]) + sp.diff(G[d, b], y[a]) - sp.diff(G[a, b], y[d])) for d in range(n))/2 for b in range(n)] for a in range(n)] for l in range(n)]
e = Th0i*Ji*etai                  # e[c, A]
E = e.inv()                       # E[A, d]
# check orthonormality: G_{cd} = e_c^A eta_AB e_d^B
print("G == e eta e^T at pt:", sp.simplify((G - e*eta*e.T).subs(pt)) == sp.zeros(4, 4))
def wLC(cidx):
    M = sp.zeros(n, n)
    for A_ in range(n):
        for B_ in range(n):
            M[A_, B_] = sum(e[d, A_]*(sp.diff(E[B_, d], y[cidx]) + sum(Gam[d][cidx][l]*E[B_, l] for l in range(n))) for d in range(n))
    return M
Bup = [sp.Matrix(n, n, lambda m, nn, cc=cc: sum(etai[m, k]*Th0[b, cc]*sp.diff(Thl[k, nn], y[b]) for k in range(n) for b in range(n))) for cc in range(n)]
for cidx in range(n):
    Bl = sum((G[cidx, t]*Bup[t] for t in range(n)), sp.zeros(n, n))
    d = (wLC(cidx) - Bl).subs(pt)
    d = d.applyfunc(sp.simplify)
    print("c =", cidx, " (w_LC - B_c) at pt =", d.tolist(), "   |B_c| =", [sp.N(v, 6) for v in Bl.subs(pt)][:6])
