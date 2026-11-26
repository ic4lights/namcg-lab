import sympy as sp

# S2: frame average of Gamma over Haar unit frames == average over the
# Dirichlet(1,...,1) weight simplex w_i = |u_i|^2, sum w_i = 1.
# Claim: E_u Gamma = (D*sum g_i^2 - W^2) / (D*(D+1)) = W^2*(1/Deff - 1/D)/(D+1),
# Deff = (sum g)^2/(sum g^2).  Uses only E[w_i] = 1/D and
# E[w_i w_j] = (1+delta_ij)/(D(D+1)).

for D in (2, 3):
    g = sp.symbols('g0:%d' % D, real=True)
    w = sp.symbols('w0:%d' % D, positive=True)
    mu = sum(g[i]*w[i] for i in range(D))
    Gam = sum(w[i]*(g[i]-mu)**2 for i in range(D))
    GamE = sp.expand(Gam)
    # Dirichlet(1,...,1) = uniform on simplex: integrate with w_{D-1}=1-sum others.
    ind = sp.symbols('t0:%d' % (D-1), positive=True)
    sub = {w[i]: ind[i] for i in range(D-1)}
    sub[w[D-1]] = 1 - sum(ind)
    ex = GamE.subs(sub)
    # normalize: volume 1/(D-1)!
    integr = ex
    for k in range(D-2, -1, -1):
        integr = sp.integrate(integr, (ind[k], 0, 1 - sum(ind[:k])))
    integr = sp.simplify(integr*sp.factorial(D-1))
    Wsym = sum(g)
    target = (D*sum(gi**2 for gi in g) - Wsym**2)/(D*(D+1))
    print("D=%d exact Dirichlet average == target:" % D, sp.simplify(integr - target) == 0)
    # also express target through Deff
    Deff = Wsym**2/sum(gi**2 for gi in g)
    t2 = Wsym**2*(1/Deff - sp.Rational(1, D))/(D+1)
    print("D=%d target == W^2(1/Deff-1/D)/(D+1):" % D, sp.simplify(target - t2) == 0)

# (2) Monte Carlo for D=5,8 with random profiles: Haar frames via complex gaussians.
import numpy as np
rng = np.random.default_rng(20261118)
for D in (5, 8):
    for trial in range(3):
        gg = rng.random(D)
        Wv = gg.sum()
        Deff = Wv*Wv/(gg*gg).sum()
        pred = Wv*Wv*(1/Deff - 1/D)/(D+1)
        M = 400000
        z = (rng.standard_normal((M, D)) + 1j*rng.standard_normal((M, D)))/np.sqrt(2)
        u = z/np.linalg.norm(z, axis=1, keepdims=True)
        w = np.abs(u)**2
        mu_m = w @ gg
        Gam_m = (w*(gg[None, :] - mu_m[:, None])**2).sum(axis=1)
        em, es = Gam_m.mean(), Gam_m.std(ddof=1)/np.sqrt(M)
        print("D=%d trial%d: MC %.6g +- %.2g  target %.6g  |z|=%.2f"
              % (D, trial, em, es, pred, abs(em-pred)/es))
print("S2 DONE")
