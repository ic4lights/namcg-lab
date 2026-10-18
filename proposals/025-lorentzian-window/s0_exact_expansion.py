"""025 script 3: invariant (fibre-constant, s=0) sector, exact harmonic analysis on H^4 = R_tau x H^3 (metric dtau^2 + cosh^2 tau dH3^2).
C41 = Laplacian of H^4, C31 = Laplacian of the unit H^3 slice, Box = C41 - C31 (Lorentzian).  Window exp(t C41); Lorentzian Schwinger factor exp(-i s Box).
Diagonal  D(z,w;tau) = diag of exp(z C41 + w C31) = int_{H3} K_4(z;r) K_3(w;d) dvol,  cosh r = 1 + cosh^2(tau)(cosh d - 1),  z = t - i s,  w = i s.
Small-(z,w) expansion D = D0 (1 + c_z z + c_w w + ...); c_s := c_w - c_z is the Seeley-DeWitt coefficient of Box itself (window independent).
Checks: (i) transport recursion for the H^4 off-diagonal coefficient b_1; (ii) D0 against the Gaussian symbol formula; (iii) c_s against the formal density of the appendix, (5 m^2 - 3 l^2)/(4 m^2) with m = l sinh(tau)."""
import sympy as sp
r, z, w, d, tau, x, e = sp.symbols('r z w d tau x epsilon', positive=True)
# (i) recursion for the H^4 heat kernel: K=(4 pi z)^-2 exp(-r^2/4z) Delta^{1/2} (1 + z b1 + z^2 b2 ...), L = d_r^2 + 3 coth r d_r
Dh = (r/sp.sinh(r))**sp.Rational(3, 2)
L = lambda f: sp.diff(f, r, 2) + 3*sp.coth(r)*sp.diff(f, r)
rhs = sp.simplify(L(Dh)/Dh)                     # = (r b1' + b1)
b1s = sp.Function('b1')
sol = sp.dsolve(sp.Eq(r*b1s(r).diff(r) + b1s(r), rhs), b1s(r))
b1 = sp.simplify(sol.rhs.subs(sp.Symbol('C1'), 0))
print("b1(r) general solution (C1->0):", b1)
b10 = sp.series(rhs, r, 0, 2).removeO().subs(r, 0)
print("b1(0) = value of Delta^{-1/2} L Delta^{1/2} at r=0 (regular solution b1(0)=rhs(0)) =", sp.limit(rhs, r, 0), " (R/6 = -2 for H^4)")
bb1 = sp.limit(rhs, r, 0)
# direct check that K solves the heat equation to O(z^0) in the combination (diagonal): verify with series of exact structure not needed further
# (ii)/(iii) expansion of D
C = sp.cosh(tau)**2
z0, w0 = sp.symbols('z0 w0', positive=True)
dd = sp.sqrt(e)*x
r2 = C*dd**2 + (C - C**2)*dd**4/12
K4 = (4*sp.pi*e*z0)**-2*sp.exp(-C*dd**2/(4*e*z0))*(1 - (C - C**2)*dd**4/(48*e*z0))*(1 - C*dd**2/4)*(1 + e*z0*bb1)
K3 = (4*sp.pi*e*w0)**sp.Rational(-3, 2)*(1 - dd**2/6)*(1 - e*w0)*sp.exp(-dd**2/(4*e*w0))
meas = 4*sp.pi*dd**2*(1 + dd**2/3)*sp.sqrt(e)           # sinh^2 d dd, dd = sqrt(e) dx
integrand = sp.expand(sp.series(meas*K4*K3, e, 0, 0).removeO()) if False else None
# expand in e analytically: factor out the Gaussian
pref = (4*sp.pi*e*z0)**-2*(4*sp.pi*e*w0)**sp.Rational(-3, 2)*4*sp.pi*e*sp.sqrt(e)
gam = C/(4*z0) + 1/(4*w0)
corr = sp.expand((1 - (C - C**2)*e**2*x**4/(48*e*z0))*(1 - C*e*x**2/4)*(1 + e*z0*bb1)*(1 - e*x**2/6)*(1 - e*w0)*(1 + e*x**2/3))
corr = sp.series(corr, e, 0, 2).removeO()
# gaussian moments with weight x^2 exp(-gam x^2): <x^2>=3/(2 gam), <x^4>=15/(4 gam^2)
mom = {0: 1, 2: sp.Rational(3, 2)/gam, 4: sp.Rational(15, 4)/gam**2}
c1 = sp.expand(corr).coeff(e, 1)
c1 = sum(sp.expand(c1).coeff(x, k)*mom[k] for k in (0, 2, 4))
D1 = sp.simplify(c1)                                    # = e^{-1} * ... first-order correction, in terms of z0,w0
cz = sp.simplify(sp.diff(D1, z0)); cw = sp.simplify(sp.diff(D1, w0))
print("D1(z0,w0) =", sp.simplify(D1))
print("check linearity: D1 - (cz*z0+cw*w0) =", sp.simplify(D1 - cz*z0 - cw*w0))
print("c_z =", sp.simplify(cz), "\nc_w =", sp.simplify(cw))
# c_z, c_w may depend on z0/w0 ratio; evaluate in the Lorentzian configuration z0=t-is, w0=is

# pure-Box limit t -> 0: z0=-i s, w0=i s  ->  D1 = i s * cs(tau)
S = sp.symbols('S', positive=True)
Dbox = sp.simplify(D1.subs({z0: -sp.I*S, w0: sp.I*S}))
cs = sp.simplify(sp.trigsimp(Dbox/(sp.I*S)))
print("pure Box limit: D1 = i s * c_s,  c_s(tau) =", cs)
a = sp.symbols('a', positive=True)
cs_a = sp.simplify(cs.rewrite(sp.exp).subs(tau, sp.asinh(a)))
print("c_s in a = sinh(tau):", sp.simplify(cs_a))
print("compare formal appendix density (5 a^2 - 3)/(4 a^2):", sp.simplify(cs_a - (5*a**2 - 3)/(4*a**2)), " ratio:", sp.simplify(cs_a/((5*a**2 - 3)/(4*a**2))))
