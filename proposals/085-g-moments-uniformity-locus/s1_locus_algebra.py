import sympy as sp

# S1: consistency-locus algebra for Gamma(u) = sum_i w_i (g_i - mu)^2,
# w_i = |u_i|^2 >= 0, sum w_i = 1, mu = sum_i g_i w_i (084 definitions).

# (1) D=2 exact closed form and pair bound.
p, q, g1, g2 = sp.symbols('p q g1 g2', nonnegative=True)
mu = (p*g1 + q*g2)/(p + q)
G2 = sp.simplify(p*(g1-mu)**2 + q*(g2-mu)**2)
lb = p*q*(g1-g2)**2/(p+q)
print("(1) D2 closed form Gamma == p*q*(g1-g2)^2/(p+q):", sp.simplify(G2-lb) == 0)
# on unit frames p+q=1: Gamma = p q (g1-g2)^2 -> zero with p,q>0 iff g1=g2.
th = sp.symbols('theta', real=True)
Gth = sp.simplify(G2.subs({p: sp.cos(th)**2, q: sp.sin(th)**2}))
print("(1b) Gamma(theta) == cos^2 sin^2 (g1-g2)^2:",
      sp.simplify(Gth - sp.cos(th)**2*sp.sin(th)**2*(g1-g2)**2) == 0)

# (2) full-support frame D=3: work in weight variables W_i, eliminate W2 = 1-W0-W1.
g = sp.symbols('g0:3', real=True)
U0, U1 = sp.symbols('U0 U1', real=True)
mu3 = g[0]*U0 + g[1]*U1 + g[2]*(1-U0-U1)
Gsub = sp.expand(U0*(g[0]-mu3)**2 + U1*(g[1]-mu3)**2 + (1-U0-U1)*(g[2]-mu3)**2)
poly = sp.Poly(Gsub, U0, U1)
sols = sp.solve([sp.Eq(cf, 0) for cf in poly.coeffs()], [g[1], g[2]], dict=True)
print("(2) full-support Gamma identically 0 in (U0,U1) forces:", sols)
# witness: nonuniform g gives a nonzero coefficient
c0 = [cf for cf in poly.coeffs() if cf != 0]
print("(2b) number of nonzero coefficient polynomials:", len(c0))

# (3) universality over pair frames D=4: pair (i,j) frame => factor (gi-gj)^2.
g4 = sp.symbols('g0:4', real=True)
def pair_gamma(i, j, t=sp.Rational(1, 2)):
    mu4 = t*g4[i] + t*g4[j]
    return sp.factor(sp.expand(t*(g4[i]-mu4)**2 + t*(g4[j]-mu4)**2))
pf = [(i, j, pair_gamma(i, j)) for i in range(4) for j in range(i+1, 4)]
print("(3) all six pair-frame Gammas are (gi-gj)^2/4:",
      all(f == (g4[i]-g4[j])**2/4 for i, j, f in pf))

# (4) affine-slice sum-of-squares range (equal-rest family), exact.
for (D, m) in [(4, 2), (5, 3), (6, 1), (6, 4)]:
    Ubar, Ws = sp.symbols('Ubar Wsym', positive=True)
    b = (Ws - m*Ubar)/(D - m)
    Smin = m*Ubar**2 + (D - m)*b**2
    usol = sp.solve(sp.Eq(sp.diff(Smin, Ubar), 0), Ubar)[0]
    print("(4) D=%d m=%d: stationary Ubar = %s (equals W/D: %s), Smin(Ubar*) = %s, "
          "Smin(0) = %s, Smin(W/m) = %s, max on slice = %s" % (
        D, m, usol, sp.simplify(usol - Ws/D) == 0,
        sp.simplify(Smin.subs(Ubar, usol)), sp.simplify(Smin.subs(Ubar, 0)),
        sp.simplify(Smin.subs(Ubar, Ws/m)),
        max([sp.simplify(Smin.subs(Ubar, 0)), sp.simplify(Smin.subs(Ubar, Ws/m))])))

# (5) numeric check of full-locus rho2-1 range endpoints (free rest off support).
import numpy as np
rng = np.random.default_rng(5)
for (D, m) in [(6, 2), (6, 4)]:
    best, worst = 1e9, -1e9
    for _ in range(200000):
        Ubar = rng.uniform(0, 1/m)
        x = rng.random(D-m); x /= x.sum()
        gg = np.array([Ubar]*m + list((1-m*Ubar)*x))
        s2 = (gg*gg).sum()
        best = min(best, s2); worst = max(worst, s2)
    print("(5) D=%d m=%d: rho2-1 grid min %.6f (exact 1/D = %.6f) max %.6f (single-row 1.0)"
          % (D, m, best, 1/D, worst))
print("S1 DONE")
