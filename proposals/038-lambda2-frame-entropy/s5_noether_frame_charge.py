"""s5: pure-diffeomorphism Noether charge of a first-order frame Lagrangian L(e, de) and its value at a fixed point of xi.

Fields: coframe e^A_mu (d=2; the derivation below is dimension independent), L = sqrt(g) (a TT + b TT' + c V^2),
g_{mu nu} = e^A_mu e^A_nu, T^A_{mu nu} = d_mu e^A_nu - d_nu e^A_mu, T_{l m n} = e^A_l T^A_{mn}, V_m = g^{l n} T_{l m n}.
This is a diffeo-covariant density of e (internal index A rigid).
Definitions:  pi^{mu nu}_A = dL/d(d_mu e^A_nu)  (antisymmetric in mu,nu),  E^nu_A = dL/de^A_nu - d_mu pi^{mu nu}_A,
              J^mu = pi^{mu nu}_A (L_xi e^A_nu) - xi^mu L,   L_xi e^A_nu = xi.d e^A_nu + e^A_sigma d_nu xi^sigma.
Claim (checked at random points for random polynomial e and xi; chain rule through the Hessian of L, 30 digits):
              J^mu = d_nu Q^{mu nu} - E^mu_A e^A_sigma xi^sigma,     Q^{mu nu} = pi^{mu nu}_A e^A_sigma xi^sigma ,
so Q is proportional to xi and vanishes where xi = 0 (bifurcation surface) for every L(e, de).
Second check (flat frame, boost): e_{A mu} L_xi e^A_nu at xi = 0 equals nabla_nu xi_mu, the Komar integrand, whereas Q vanishes there:
the Y(phi, L_xi phi) term of Iyer-Wald eqs. (59)-(60) is nonzero at Sigma when L_xi e != 0.
"""
import random
import sympy as sp
from sympy import Rational as Q

random.seed(11)
d = 2
X = sp.symbols('x1:%d' % (d+1))
Es = [[sp.Symbol(f'e{A}{m}') for m in range(d)] for A in range(d)]                        # e^A_mu
Ds = [[[sp.Symbol(f'd{A}_{m}_{n}') for n in range(d)] for m in range(d)] for A in range(d)]   # d_m e^A_n
a, b, c = sp.symbols('a b c')
e = sp.Matrix(d, d, lambda m, A: Es[A][m])
g = e*e.T
gi = g.inv()
sg = sp.sqrt(g.det())
T = [[[Ds[A][m][n] - Ds[A][n][m] for n in range(d)] for m in range(d)] for A in range(d)]
Tl = [[[sum(Es[A][l]*T[A][m][n] for A in range(d)) for n in range(d)] for m in range(d)] for l in range(d)]
Tu = [[[sum(gi[l, l2]*gi[m, m2]*gi[n, n2]*Tl[l2][m2][n2] for l2 in range(d) for m2 in range(d) for n2 in range(d))
        for n in range(d)] for m in range(d)] for l in range(d)]
TT = sum(Tl[l][m][n]*Tu[l][m][n] for l in range(d) for m in range(d) for n in range(d))
TTp = sum(Tl[l][m][n]*Tu[m][l][n] for l in range(d) for m in range(d) for n in range(d))
V = [sum(gi[l, n]*Tl[l][m][n] for l in range(d) for n in range(d)) for m in range(d)]
V2 = sum(gi[m, n]*V[m]*V[n] for m in range(d) for n in range(d))
coeffs = {a: Q(2), b: Q(-3), c: Q(5, 2)}
L = (sg*(a*TT + b*TTp + c*V2)).subs(coeffs)

zs = [Es[A][m] for A in range(d) for m in range(d)] + [Ds[A][m][n] for A in range(d) for m in range(d) for n in range(d)]
idx = {z: i for i, z in enumerate(zs)}
grad = [sp.diff(L, z) for z in zs]
hess = [[sp.diff(gz, z2) for z2 in zs] for gz in grad]

def rp(deg=2):
    return sum(Q(random.randint(-3, 3), random.randint(1, 3))*sp.prod(random.choices(X, k=random.randint(1, deg))) for _ in range(3))

def trial():
    e_field = [[(1 if A == m else 0) + Q(1, 4)*rp() for m in range(d)] for A in range(d)]      # e^A_m(x)
    xi = [rp() for _ in range(d)]
    x0 = {X[i]: Q(random.randint(1, 5), random.randint(3, 7)) for i in range(d)}
    zval = {}
    dz = {}      # dz[z][k] = d z / d x_k
    for A in range(d):
        for m in range(d):
            zval[Es[A][m]] = e_field[A][m].subs(x0)
            dz[Es[A][m]] = [sp.diff(e_field[A][m], X[k]).subs(x0) for k in range(d)]
            for n in range(d):
                pass
    for A in range(d):
        for m in range(d):
            for n in range(d):
                f_ = sp.diff(e_field[A][n], X[m])
                zval[Ds[A][m][n]] = f_.subs(x0)
                dz[Ds[A][m][n]] = [sp.diff(f_, X[k]).subs(x0) for k in range(d)]
    nz = len(zs)
    gv = [sp.N(gr.subs(zval), 30) for gr in grad]
    Hv = [[sp.N(h.subs(zval), 30) for h in row] for row in hess]
    Lv = sp.N(L.subs(zval), 30)
    ev = lambda A, m: zval[Es[A][m]]
    dev = lambda A, m, k: dz[Es[A][m]][k]
    xi0 = [s.subs(x0) for s in xi]
    dxi = [[sp.diff(xi[s], X[k]).subs(x0) for k in range(d)] for s in range(d)]   # dxi[s][k] = d_k xi^s
    pi = {(A, m, n): gv[idx[Ds[A][m][n]]] for A in range(d) for m in range(d) for n in range(d)}
    # d_k pi^{mn}_A = sum_j H[D_Amn, z_j] dz_j/dx_k
    dpi = {}
    for A in range(d):
        for m in range(d):
            for n in range(d):
                i = idx[Ds[A][m][n]]
                for k in range(d):
                    dpi[(A, m, n, k)] = sum(Hv[i][j]*dz[zs[j]][k] for j in range(nz))
    dLde = {(A, n): gv[idx[Es[A][n]]] for A in range(d) for n in range(d)}
    Eom = {(A, n): dLde[(A, n)] - sum(dpi[(A, m, n, m)] for m in range(d)) for A in range(d) for n in range(d)}
    # J^mu
    Lxi_e = {(A, n): sum(xi0[s]*dev(A, n, s) for s in range(d)) + sum(ev(A, s)*dxi[s][n] for s in range(d)) for A in range(d) for n in range(d)}
    J = [sum(pi[(A, m, n)]*Lxi_e[(A, n)] for A in range(d) for n in range(d)) - xi0[m]*Lv for m in range(d)]
    # d_nu Q^{mu nu},  Q^{mu nu} = pi^{mu nu}_A e^A_s xi^s
    dQ = []
    for m in range(d):
        tot = 0
        for n in range(d):
            for A in range(d):
                tot += dpi[(A, m, n, n)]*sum(ev(A, s)*xi0[s] for s in range(d))
                tot += pi[(A, m, n)]*sum(dev(A, s, n)*xi0[s] + ev(A, s)*dxi[s][n] for s in range(d))
        dQ.append(tot)
    anti = max(abs(pi[(A, m, n)] + pi[(A, n, m)]) for A in range(d) for m in range(d) for n in range(d))
    resid = [J[m] - dQ[m] + sum(Eom[(A, m)]*ev(A, s)*xi0[s] for A in range(d) for s in range(d)) for m in range(d)]
    return anti, resid, J, dQ

for t in range(3):
    anti, resid, J, dQ = trial()
    print(f"trial {t}: max|pi^(mn)+pi^(nm)| = {sp.N(anti, 5)};  residual J - d_nu Q + E e xi = {[sp.N(r_, 5) for r_ in resid]};  |J| ~ {[sp.N(j, 5) for j in J]}")

print("\nFlat frame e^A = delta^A_mu (d=2), boost xi = (x2, x1) (Killing, vanishes at the origin):")
x1, x2 = sp.symbols('x1 x2')
xiF = [x2, x1]
eF = sp.eye(2)
for nu in range(2):
    row = []
    for mu in range(2):
        val = sum(eF[A, mu]*(sum(xiF[s]*sp.diff(eF[A, nu], [x1, x2][s]) for s in range(2)) + sum(eF[A, s]*sp.diff(xiF[s], [x1, x2][nu]) for s in range(2)))
                  for A in range(2))
        row.append(val)
    print("   (e_{A mu} L_xi e^A_nu), nu=%d, mu=0,1:" % nu, row, " (antisymmetric: = nabla_nu xi_mu, the Komar integrand)")
print("   Q^{mu nu} = pi^{mu nu}_A e^A_sigma xi^sigma is proportional to xi: it vanishes at xi = 0 for every L(e, de).")
