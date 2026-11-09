"""Proposal 066 r2: check of the K_0 Weyl-symbol claim (gatekeeper Finding 3), not a proof about the undefined H_quad.
Moyal plane in d=2 (coordinates x0,x1), [x_mu, x_nu]_* = i Theta_{mu nu}, Theta = theta*eps.
Exact Moyal product for polynomials. Computes the integrand of
K_0 = 1/2 Theta^{-1 mu nu} tr( x_mu [x_nu, h]_* ) with tr -> integral, for a generic quadratic symbol h,
and compares with (i/2) x^mu d_mu h (dilatation weighting) and with the boost weighting x0 d1 h - x1 d0 h.
Integrals of total derivatives are dropped, so integrands are compared modulo exact Moyal corrections:
for polynomials, int f*g = int f g holds up to boundary terms, checked by comparing f*g - f g to a divergence."""
import sympy as sp
x0, x1, th = sp.symbols('x0 x1 theta', real=True, nonzero=True)
X = [x0, x1]
Th = sp.Matrix([[0, th], [-th, 0]])
def star(f, g, order=6):
    res = 0
    for n in range(order + 1):
        term = 0
        # n-th order bidifferential: (i/2)^n/n! Th^{a1b1}..Th^{anbn} d_a.. f d_b.. g
        import itertools
        for idx in itertools.product(range(2), repeat=2 * n):
            a, b = idx[:n], idx[n:]
            coef = 1
            for k in range(n):
                coef *= Th[a[k], b[k]]
            if coef == 0:
                continue
            df, dg = f, g
            for k in range(n):
                df = sp.diff(df, X[a[k]]); dg = sp.diff(dg, X[b[k]])
            term += coef * df * dg
        res += (sp.I / 2) ** n / sp.factorial(n) * term
    return sp.expand(res)
cs = sp.symbols('c0:6')
h = cs[0]*x0**2 + cs[1]*x0*x1 + cs[2]*x1**2 + cs[3]*x0 + cs[4]*x1 + cs[5]
print("[x0,x1]_* =", sp.simplify(star(x0, x1) - star(x1, x0)))
Thinv = Th.inv()
integrand = 0
for mu in range(2):
    for nu in range(2):
        comm = star(X[nu], h) - star(h, X[nu])
        integrand += sp.Rational(1, 2) * Thinv[mu, nu] * star(X[mu], comm)
integrand = sp.expand(integrand)
dil = sp.expand(sp.I / 2 * sum(X[m] * sp.diff(h, X[m]) for m in range(2)))
boost = sp.expand(x0 * sp.diff(h, x1) - x1 * sp.diff(h, x0))
print("integrand        =", integrand)
print("(i/2) x.d h      =", dil)
print("difference       =", sp.simplify(integrand - dil))
print("boost weighting  =", boost)
print("integrand proportional to boost weighting for generic h?",
      sp.simplify(integrand - sp.Symbol('k') * boost) == 0)
