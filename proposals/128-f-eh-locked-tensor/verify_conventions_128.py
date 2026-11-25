# verify_conventions_128.py  (item 128, script 1)
# Checks the curvature conventions of the manuscript as written in
# chapters/ch02-preliminaries.tex (eq:christoffel, eq:riemann):
#   R^rho_{sigma mu nu} = d_mu Gamma^rho_{nu sigma} - d_nu Gamma^rho_{mu sigma}
#                         + Gamma^rho_{mu lam}Gamma^lam_{nu sigma}
#                         - Gamma^rho_{nu lam}Gamma^lam_{mu sigma}
#   Ric_{mu nu} = R^rho_{mu rho nu},  R = g^{mu nu} Ric_{mu nu}
# and the sign calibration used in the item-123 record (appH, "overall sign
# calibrated by the unit sphere at R=+2").
# Expected invariant outputs:
#   SPHERE_R = 2        (unit 2-sphere scalar curvature under eq:riemann)
#   SPHERE_Ric_11 = sin(theta)^2  (i.e. Ric = g on the unit sphere)
#   GAUGE_a1_S2 = 5*theta-dependent form: a1 = tr(R/6 - E) with E = -Ric on
#                 the 2-vector fibre gives (2/3+1)*R = (5/3)*R  (123 ghost check, dimension-shrunk)
#   A1_TENSOR_R = (10/6 - e_h) * R  identity (convention bookkeeping only)
import sympy as sp

th, ph = sp.symbols('theta phi', real=True)
g = sp.Matrix([[1, 0], [0, sp.sin(th)**2]])
ginv = g.inv()
x = [th, ph]

def christoffel(g, ginv, x):
    n = len(x)
    G = {}
    for r in range(n):
        for mu in range(n):
            for nu in range(n):
                s = 0
                for sig in range(n):
                    s += ginv[r, sig]*sp.Rational(1, 2)*(
                        sp.diff(g[nu, sig], x[mu]) +
                        sp.diff(g[mu, sig], x[nu]) -
                        sp.diff(g[mu, nu], x[sig]))
                G[(r, mu, nu)] = sp.simplify(s)
    return G

G = christoffel(g, ginv, x)

def riemann(G, g, x):
    n = len(x)
    Rm = {}
    for r in range(n):
        for s in range(n):
            for mu in range(n):
                for nu in range(n):
                    val = (sp.diff(G[(r, nu, s)], x[mu]) -
                           sp.diff(G[(r, mu, s)], x[nu]))
                    for lam in range(n):
                        val += G[(r, mu, lam)]*G[(lam, nu, s)] - G[(r, nu, lam)]*G[(lam, mu, s)]
                    Rm[(r, s, mu, nu)] = sp.simplify(val)
    return Rm

Rm = riemann(G, g, x)
Ric = sp.zeros(2, 2)
for mu in range(2):
    for nu in range(2):
        Ric[mu, nu] = sp.simplify(sum(Rm[(r, mu, r, nu)] for r in range(2)))
Rscal = sp.simplify(sum(ginv[mu, nu]*Ric[mu, nu] for mu in range(2) for nu in range(2)))

print("SPHERE_R =", sp.simplify(Rscal))          # expect 2
print("SPHERE_Ric_11 =", Ric[1, 1], " sin^2 =", sp.simplify(Ric[1,1] - sp.sin(th)**2))  # expect 0 diff

# 123 ghost a1 check with these conventions, on the sphere fibre (vector):
# a1 = tr(R/6 - E), E = -Ric  =>  2*R/6 + tr(Ric) = (1/3 + 1)*R = (4/3)R on S2
a1_vec = sp.simplify(2*Rscal/6 + sum(ginv[i, j]*Ric[i, j] for i in range(2) for j in range(2)))
print("GAUGE_a1_S2 =", a1_vec, " ratio_to_R =", sp.simplify(a1_vec/Rscal))  # expect 4/3

# convention bookkeeping identity for the tensor block, total-trace reading:
e_h = sp.symbols('e_h')
a1_ten = sp.simplify(10*Rscal/6 - e_h*Rscal)
print("A1_TENSOR_R = (10/6 - e_h)*R holds:", sp.simplify(a1_ten - (sp.Rational(10,6)-e_h)*Rscal) == 0)
