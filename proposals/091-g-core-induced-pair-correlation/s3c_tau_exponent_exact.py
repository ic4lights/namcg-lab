# s3c_tau_exponent_exact.py - EXACT check of the tau = tr G exponent (the MC fit of s3b is
# unresolvable at attainable n: Gamma(8)-CDF at the fit window's left edge is ~1e-11).
# I(tau) = int_0^tau [lambda(tau-lambda)]^2 (tau-2 lambda)^2 dlambda = C tau^7:
# substitution lambda = tau*x shows the power 7 = 4+2+1 exactly, and C is computed.
# Consistency: sum of 8 iid Exp(1) is Gamma(8): pdf ~ t^7 near 0 (shape 8), matching 2a+2 for a=3.
# Run: python -I proposals/091-g-core-induced-pair-correlation/s3c_tau_exponent_exact.py
import sympy as sp
tau, x = sp.symbols('tau x', positive=True)
inner = sp.integrate(x**2*(1-x)**2*(1-2*x)**2, (x, 0, 1))
print("(c1) int_0^1 x^2(1-x)^2(1-2x)^2 dx =", inner, "(= 1/210:", inner == sp.Rational(1, 210), ")")
lam = sp.symbols('lam', positive=True)
I = sp.integrate((lam*(tau-lam))**2*(tau-2*lam)**2, (lam, 0, tau))
I = sp.expand(sp.simplify(I))
print("(c2) int_0^tau (lam(tau-lam))^2 (tau-2 lam)^2 dlam =", I, " ; == tau^7/210:", I == tau**7/210)
t = sp.symbols('t', positive=True)
pdf8 = sp.gamma(8)**(-1)*t**7*sp.exp(-t)
cdf8 = sp.integrate(pdf8, (t, 0, x))
print("(c3) Gamma(8) pdf ~ t^7 e^{-t}; its CDF =", sp.simplify(cdf8),
      "; leading term t^8/40320:", sp.simplify(sp.series(cdf8, x, 0, 9).removeO() - x**8/sp.factorial(8)) == 0)
print("S3C DONE")
