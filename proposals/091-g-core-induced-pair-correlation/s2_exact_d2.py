# s2_exact_d2.py - exact D=2 identities for proposal 091 (route A).
# Run from repo root:  python -I proposals/091-g-core-induced-pair-correlation/s2_exact_d2.py
# (1) Hermitian 2x2 eigenvalue-fibre chart: det J = (1/2)(y1-y2)^2 sin(2 theta)  -> Vandermonde exponent 2.
# (2) Fixed-trace separation of the Laguerre beta=2 joint density, EXACT up to a constant
#     (ratio check, superseding the dead-pass s1_jacobian_v4 check (2) which asserted constant 1).
# (3) Exact D=2 pair statistics of the a-member at beta=2: mode, E[u], Var(p1), coincidence tail.
# (4) Cross-check of the integrated 089 D=2 slot-pushforward density by direct fibre integration.
import sympy as sp

y1, y2, tau, u, a, eps = sp.symbols('y1 y2 tau u a eps', positive=True)
th, phi = sp.symbols('theta phi', real=True)
# ---- (1) chart Z = U diag(y1,y2) U^H, U = [[c, s e^{i phi}],[-s e^{-i phi}, c]]
c, s = sp.cos(th), sp.sin(th)
U = sp.Matrix([[c, s*sp.exp(sp.I*phi)], [-s*sp.exp(-sp.I*phi), c]])
Z = U * sp.diag(y1, y2) * U.H
rows = []
for e in (Z[0, 0], Z[0, 1], Z[1, 1]):
    rows.append([sp.simplify(sp.expand_complex(t)) for t in e.as_real_imag()])
assert rows[0][1] == 0 and rows[2][1] == 0
coords = (rows[0][0], rows[1][0], rows[1][1], rows[2][0])
params = (th, phi, y1, y2)
Jm = sp.Matrix([[sp.diff(rd, p) for p in params] for rd in coords])
detJ = sp.factor(sp.simplify(Jm.det()))
target = sp.Rational(1, 2)*(y1 - y2)**2*sp.sin(2*th)
print("(1) det J == (1/2)(y1-y2)^2 sin(2 theta):", sp.simplify(detJ - target) == 0)
# ---- (2) fixed-trace separation: joint = (y1 y2)^(a-1) e^{-(y1+y2)} (y1-y2)^2
joint = (y1*y2)**(a-1)*sp.exp(-(y1+y2))*(y1-y2)**2
sub = joint.subs({y1: tau*(1+u)/2, y2: tau*(1-u)/2})*tau/2   # |jac (tau,u)->(y1,y2)| = tau/2
ratio = sp.simplify(sp.powsimp(sp.expand_log(sub/((tau**(2*a+1))*sp.exp(-tau)*u**2*(1-u**2)**(a-1)),
                                             force=True), force=True))
print("(2) joint*|jac| / [tau^(2a+1) e^-tau u^2 (1-u^2)^(a-1)] is constant:",
      sp.simplify(sp.diff(ratio, tau)) == 0 and sp.simplify(sp.diff(ratio, u)) == 0,
      "; ratio =", sp.simplify(ratio.subs({tau: 3, u: sp.Rational(2, 5)})))
