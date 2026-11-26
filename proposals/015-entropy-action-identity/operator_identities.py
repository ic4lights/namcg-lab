"""
Algebraic identities used in proposal 015 (Poisson limit, Euclidean or Lorentzian eta).

(a) Scalar operator  O_s f = -rho^{-1} d_mu( rho K^{mu nu} d_nu f ),  K = G^{-1},  sqrt|G| = rho^2,  g_rho^{mu nu} = rho K^{mu nu}:
        O_s = -D^2 + E,  D = nabla + omega,  omega_mu = -(1/2) d_mu ln rho,  E = -(1/2) box_G ln rho + (1/4)|d ln rho|^2_G,
    and  sqrt|G| ( R_G/6 - E ) = rho R[g_rho] / 6.   Tested at a random point for a unimodular diagonal g_rho depending on (x0,x1).
(b) Connection sector:  tr(B_sigma B^sigma) = -X  pointwise, X = eta^{rl} d_r Theta^{mn} d_l Theta_{mn},
    (B^sigma)^mu_nu = eta^{mu a} Theta^{r sigma} d_r Theta_{a nu},  G = (Theta^T eta Theta)^{-1};  tr B = 0.
    Hence  sqrt|G| tr(R_G/6 - E_v) = (4/6) rho R[g_rho] + rho^2 X.
(c) No explicit curvature of G appears in E_s, E_v (they are built from d ln rho and d Theta only).
"""
import sympy as sp
import numpy as np

x = sp.symbols('x0:4')
rng = np.random.default_rng(7)

# ---------- (a) ----------
a = 1 + x[0] ** 2 / 3 + x[1] / 5
b = 2 + sp.sin(x[0] * x[1]) / 4
c = 1 + x[1] ** 2 / 7 + x[0] / 4
d = 1 / (a * b * c)
rho = 2 + x[0] * x[1] / 3 + x[1] ** 2 / 5
f = sp.exp(x[0] / 2) * (1 + x[1] ** 2) + x[1] * x[0] ** 3
gdiag_up = [a, b, c, d]                      # g_rho^{mu nu} = diag
gr_lo = sp.diag(*[1 / v for v in gdiag_up])  # g_rho,mu nu
G_lo = rho * gr_lo
G_up = G_lo.inv()
sqrtG = rho ** 2
assert sp.simplify(G_lo.det() - rho ** 4) == 0


def christoffel(g, gi):
    n = 4
    return [[[sum(gi[l, s] * (sp.diff(g[s, m], x[nn]) + sp.diff(g[s, nn], x[m]) - sp.diff(g[m, nn], x[s])) for s in range(n)) / 2
              for nn in range(n)] for m in range(n)] for l in range(n)]


def ricci_scalar(g):
    n = 4
    gi = g.inv()
    Gm = christoffel(g, gi)
    Ric = sp.zeros(n, n)
    for s in range(n):
        for nn in range(n):
            Ric[s, nn] = sum(sp.diff(Gm[r][nn][s], x[r]) - sp.diff(Gm[r][r][s], x[nn])
                             + sum(Gm[r][r][l] * Gm[l][nn][s] - Gm[r][nn][l] * Gm[l][r][s] for l in range(n)) for r in range(n))
    return sum(gi[s, nn] * Ric[s, nn] for s in range(n) for nn in range(n))


pt = {x[0]: 0.37, x[1]: 0.61, x[2]: 0.2, x[3]: -0.4}
num = lambda e: complex(sp.N(e.subs(pt), 20)).real

Gi = G_up
box = lambda u: sum(sp.diff(sqrtG * Gi[m, nn] * sp.diff(u, x[nn]), x[m]) for m in range(4) for nn in range(4)) / sqrtG
lnrho = sp.log(rho)
Os_f = -sum(sp.diff(sum(rho * G_up[m, nn] * sp.diff(f, x[nn]) for nn in range(4)), x[m]) for m in range(4)) / rho
E = -box(lnrho) / 2 + sum(Gi[m, nn] * sp.diff(lnrho, x[m]) * sp.diff(lnrho, x[nn]) for m in range(4) for nn in range(4)) / 4
om_up = [-sum(Gi[m, nn] * sp.diff(lnrho, x[nn]) for nn in range(4)) / 2 for m in range(4)]
om_lo = [-sp.diff(lnrho, x[m]) / 2 for m in range(4)]
Df = box(f) + 2 * sum(om_up[m] * sp.diff(f, x[m]) for m in range(4)) + (sum(sp.diff(sqrtG * om_up[m], x[m]) for m in range(4)) / sqrtG + sum(om_up[m] * om_lo[m] for m in range(4))) * f
res1 = num(Os_f - (-Df + E * f))
print("(a) O_s f - (-D^2 f + E f) at a random point:", f"{res1:.2e}")
RG = ricci_scalar(G_lo)
Rg = ricci_scalar(gr_lo)
res2 = num(sqrtG * (RG / 6 - E) - rho * Rg / 6)
print("(a) sqrt|G|(R_G/6 - E) - rho R[g_rho]/6 at a random point:", f"{res2:.2e}", " (values", f"{num(sqrtG*(RG/6-E)):.6f}, {num(rho*Rg/6):.6f})")

# ---------- (b) ----------
for sig, eta in (("Euclid", np.diag([1., 1, 1, 1])), ("Lorentz", np.diag([-1., 1, 1, 1]))):
    A = rng.normal(size=(4, 4))
    Th = A - A.T
    D = rng.normal(size=(4, 4, 4))
    D = D - D.transpose(0, 2, 1)             # D[r, m, n] = d_r Theta^{mn}, antisymmetric in (m,n)
    etai = np.linalg.inv(eta)
    K = Th.T @ eta @ Th
    G = np.linalg.inv(K)
    Th_lo = eta @ Th @ eta
    D_lo = np.einsum('ma,rab,bn->rmn', eta, D, eta)
    # B^sigma[mu,nu] = eta^{mu a} Theta^{r sigma} d_r Theta_{a nu}
    B = np.einsum('ma,rs,ran->smn', etai, Th, D_lo)
    trB = np.einsum('smm->s', B)
    trBB = np.einsum('st,smn,tnm->', G, B, B)
    X = np.einsum('rl,rmn,lab,ma,nb->', etai, D, D, eta, eta)
    print(f"(b) {sig}: tr B_sigma = {np.abs(trB).max():.1e};  tr(B_s B^s) = {trBB:.8f},  -X = {-X:.8f}")
