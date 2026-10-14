"""
Check of the weighted (Poisson-trace) scalar operator of rem:ch3-varying-theta,
    L phi = rho^{-1} d_mu ( rho K^{mu nu} d_nu phi ),   g_rho^{mu nu} = rho K^{mu nu},  det g_rho = 1,
written as Laplace type for the metric G = rho * g_rho (sqrt(G) = rho^2, G^{mu nu} = K^{mu nu}):
    L = Lap_G - G^{mu nu} d_mu ln(rho) d_nu = D^2 - E,  D = nabla + omega, omega = -1/2 d ln rho,
    E = -1/2 Box_G ln rho + 1/4 (grad ln rho)^2,  a_1 = R_G/6 - E.
Claim checked: integral sqrt(G) a_1 = integral sqrt(g_rho) rho R[g_rho]/6   (up to total derivatives)
(Brans-Dicke omega=0 form).  Test with a unimodular metric diag(e^u, e^-u, e^v, e^-v), u,v,rho functions of (x0,x1).
Euclidean signature used for the algebra (signature does not enter the identity).
"""
import sympy as sp
from sympy.calculus.euler import euler_equations

x = sp.symbols('x0:4')
u = sp.Function('u')(x[0], x[1]); v = sp.Function('v')(x[0], x[1]); rho = sp.Function('rho')(x[0], x[1])
phi = sp.Function('phi')(*x)

def geometry(g):
    n = 4
    gi = g.inv()
    Gam = [[[sum(gi[a, d]*(sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d])) for d in range(n))/2
             for c in range(n)] for b in range(n)] for a in range(n)]
    def Riem(a, b, c, d):
        return (sp.diff(Gam[a][b][d], x[c]) - sp.diff(Gam[a][b][c], x[d])
                + sum(Gam[a][c][e]*Gam[e][b][d] - Gam[a][d][e]*Gam[e][b][c] for e in range(n)))
    Ric = sp.Matrix(n, n, lambda b, d: sum(Riem(a, b, a, d) for a in range(n)))
    R = sum(gi[b, d]*Ric[b, d] for b in range(n) for d in range(n))
    return gi, Gam, sp.simplify(R)

g_rho = sp.diag(sp.exp(u), sp.exp(-u), sp.exp(v), sp.exp(-v))     # det = 1
assert sp.simplify(g_rho.det()) == 1
G = rho*g_rho
sqrtG = rho**2
Ginv = G.inv()
K = Ginv                                                           # K^{mu nu} = G^{mu nu}
# operator identity (part 1), applied to a generic phi
L_phi = sum(sp.diff(rho*sum(K[m, n]*sp.diff(phi, x[n]) for n in range(4)), x[m]) for m in range(4))/rho
gi, Gam, RG = geometry(G)
def box(f):
    return sum(sp.diff(sqrtG*sum(Ginv[m, n]*sp.diff(f, x[n]) for n in range(4)), x[m]) for m in range(4))/sqrtG
lnr = sp.log(rho)
grad2 = sum(Ginv[m, n]*sp.diff(lnr, x[m])*sp.diff(lnr, x[n]) for m in range(4) for n in range(4))
drift = sum(Ginv[m, n]*sp.diff(lnr, x[m])*sp.diff(phi, x[n]) for m in range(4) for n in range(4))
print("part 1: L phi - (Box_G phi - drift) =", sp.simplify(L_phi - (box(phi) - drift)))
# D^2 phi with omega_mu = -1/2 d_mu ln rho acting on a scalar: D^2 = Box + 2 omega.grad + (div omega) + omega^2
om = [-sp.diff(lnr, x[m])/2 for m in range(4)]
div_om = box_om = sum(sp.diff(sqrtG*sum(Ginv[m, n]*om[n] for n in range(4)), x[m]) for m in range(4))/sqrtG
om2 = sum(Ginv[m, n]*om[m]*om[n] for m in range(4) for n in range(4))
D2phi = box(phi) + 2*sum(Ginv[m, n]*om[m]*sp.diff(phi, x[n]) for m in range(4) for n in range(4)) + (div_om + om2)*phi
E = -box(lnr)/2 + grad2/4
print("part 1b: L phi - (D^2 phi - E phi) =", sp.simplify(L_phi - (D2phi - E*phi)))

# part 2: integrated a_1
a1_density = sqrtG*(RG/6 - E)
gi0, Gam0, Rg = geometry(g_rho)
target = rho*Rg/6                      # sqrt(g_rho) = 1
diff = sp.simplify(a1_density - target)
eqs = euler_equations(diff, [u, v, rho], [x[0], x[1]])
print("part 2: Euler-Lagrange operators of (a1 density - rho R[g_rho]/6):")
for e in eqs:
    print("  ", sp.simplify(e.lhs - e.rhs))
print("diff identically zero pointwise:", diff == 0)
if diff != 0:
    print("diff =", diff)
