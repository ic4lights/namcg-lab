#!/usr/bin/env python3
"""054-055 r3: independent symbolic checks of the claims carried by the corrected inserts.
Run: python -I proposals/local-gpu/054-055-r2/check_r3.py
Each block prints PASS/FAIL; the last line is OVERALL."""
import sympy as sp

ok = []
def rep(name, cond):
    ok.append(bool(cond)); print(('PASS ' if cond else 'FAIL ') + name)

# (1) N=2 eigenvalue identity: k.A = sum_a w_a sigma^a/2, w_a = k^mu A^a_mu.
w1, w2, w3, lam = sp.symbols('w1 w2 w3 lam')
s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]])
M = (w1*s1 + w2*s2 + w3*s3)/2
rep('(1a) charpoly(k.A) = lam^2 - (w1^2+w2^2+w3^2)/4',
    sp.expand(M.charpoly(lam).as_expr() - (lam**2 - (w1**2 + w2**2 + w3**2)/4)) == 0)
rep('(1b) -4 det(k.A) = sum_a w_a^2 (rho_X^2), truncation a=1..2 differs',
    sp.expand(-4*M.det() - (w1**2 + w2**2 + w3**2)) == 0 and sp.expand(-4*M.det() - (w1**2 + w2**2)) != 0)
# trace of exponential: Tr exp(i M) = 2 cos(rho/2), test numerically at a complex point
import mpmath as mp
mp.mp.dps = 30
wv = [mp.mpc(0.3, 0.7), mp.mpc(-1.1, 0.2), mp.mpc(0.5, -0.4)]
Mn = mp.matrix([[wv[2]/2, (wv[0] - 1j*wv[1])/2], [(wv[0] + 1j*wv[1])/2, -wv[2]/2]])
lhs = sum(mp.expm(1j*Mn)[i, i] for i in range(2))
rho = mp.sqrt(sum(x**2 for x in wv))
rep('(1c) Tr e^{i k.A} = 2 cos(rho_X/2) (complex test point, 30 dps)', abs(lhs - 2*mp.cos(rho/2)) < mp.mpf(10)**-25)

# (2) one-dimensional branch model on R_u in the normalisation of Definition (A).
# A_0 = e^{-3 pi i u/8} At0, At0 = a sigma^3/2, so Tr At0^2 = a^2/2 (derived below, not assumed).
# Regulator -eps Tr A_0^2 and mass i S_gamma (eta^{00} = -1) give e^{-Q a^2} with
# Q = (1/2) e^{-3 pi i u/4}(eps - i gamma/(2 g^2)); gc = e^{i phi} r0/2.
u, eps, r0, g, G = sp.symbols('u epsilon r0 g Gamma', positive=True)  # G = |gamma| > 0, gamma = -G
aa = sp.symbols('a', real=True)
gam = sp.symbols('gamma', real=True)
pi = sp.pi
At0 = aa*s3/2
A0m = sp.exp(-3*pi*sp.I*u/8)*At0
expo_reg = -eps*(A0m*A0m).trace()
expo_mass = sp.I*(-gam/(2*g**2))*(-(A0m*A0m).trace())      # i S_gamma, Tr A_mu A^mu -> -Tr A_0^2
Qder = sp.simplify(-(expo_reg + expo_mass)/aa**2)
Qtrue = lambda gm: sp.exp(-3*pi*sp.I*u/4)*(eps - sp.I*gm/(2*g**2))/2
rep('(2g) Tr(a sigma^3/2)^2 = a^2/2 and Q = (1/2) e^{-3 pi i u/4}(eps - i gamma/(2 g^2)) from Definition (A)',
    sp.simplify((At0*At0).trace() - aa**2/2) == 0 and sp.simplify(Qder - Qtrue(gam)) == 0)
def expo(phi, Q):
    return -(sp.exp(sp.I*phi)*r0/2)**2/(4*Q)
Q0 = Qtrue(0)                                                   # gamma = 0
Qm = sp.exp(-3*pi*sp.I*u/4)*(sp.I*G/(2*g**2))/2                 # gamma = -G, eps -> 0
frozen, contour = 3*pi/8, 3*pi*(1 - u)/8
def re(e):
    return sp.simplify(sp.re(sp.expand_complex(e)))
e_f0, e_c0 = re(expo(frozen, Q0)), re(expo(contour, Q0))
e_fm, e_cm = re(expo(frozen, Qm)), re(expo(contour, Qm))
rep('(2a) frozen, gamma=0: r0^2 cos(3 pi u/4 - pi/4)/(8 eps)',
    sp.simplify(e_f0 - r0**2*sp.cos(3*pi*u/4 - pi/4)/(8*eps)) == 0)
rep('(2b) frozen, fixed gamma<0, eps->0: g^2 r0^2 sin(3 pi u/4 - pi/4)/(4|gamma|)',
    sp.simplify(e_fm - g**2*r0**2*sp.sin(3*pi*u/4 - pi/4)/(4*G)) == 0)
rep('(2c) contour coefficient, gamma=0: r0^2/(8 sqrt2 eps), independent of u',
    sp.simplify(e_c0 - r0**2/(8*sp.sqrt(2)*eps)) == 0)
rep('(2d) contour coefficient, fixed gamma<0: -g^2 r0^2/(4 sqrt2 |gamma|), independent of u',
    sp.simplify(e_cm + g**2*r0**2/(4*sp.sqrt(2)*G)) == 0)
rep('(2e) coefficient of tilde A_0 in k.A on R_u at k^0 = e^{3 pi i/8} r0 is e^{3 pi i (1-u)/8} r0',
    sp.simplify(sp.exp(3*pi*sp.I/8)*sp.exp(-3*pi*sp.I*u/8) - sp.exp(3*pi*sp.I*(1 - u)/8)) == 0)
rep('(2f) frozen and contour models agree at u=0 (corner value 0.0883883/eps at r0=1)',
    sp.simplify((e_f0 - e_c0).subs(u, 0)) == 0 and abs(float((e_c0*eps).subs(r0, 1)) - 0.0883883) < 1e-6)
# (2h) direct quadrature of the branch integral with the trace normalisation, against the closed form
import mpmath as mp
mp.mp.dps = 30
okq = True
for (uv, ev, gv, rv) in ((0.0, 0.7, 0.0, 1.3), (0.4, 0.5, 0.0, 1.0), (0.4, 0.3, -0.3, 1.0), (0.6, 0.2, -0.2, 1.0)):
    Qn = mp.e**(-3j*mp.pi*uv/4)*(ev - 1j*gv/2)/2
    coefn = mp.e**(3j*mp.pi*(1 - uv)/8)*rv
    f = lambda x: mp.e**(-Qn*x**2)*2*mp.cos(coefn*x/2)
    num = mp.quad(f, [-mp.inf, 0, mp.inf])
    clo = 2*mp.sqrt(mp.pi/Qn)*mp.e**(-(coefn/2)**2/(4*Qn))
    okq &= abs(num - clo) < mp.mpf(10)**-15*abs(clo)
    print('     u=%.1f eps=%.1f gamma=%+.1f r0=%.1f: |quad - closed|/|closed| = %.2e'
          % (uv, ev, gv, rv, float(abs(num - clo)/abs(clo))))
rep('(2h) quadrature of int e^{-Q a^2} 2cos(gc a) da equals 2 sqrt(pi/Q) e^{-gc^2/(4Q)} (contour gc, g=1)', okq)
# (2i) signed exponent below the modulus exponent at u=0: r0^2/(8 sqrt2 eps) <= sin^2(3pi/8) r0^2/(8 eps)
rep('(2i) u=0: signed exponent 1/(8 sqrt2) = 0.08839 <= modulus exponent sin^2(3 pi/8)/8 = 0.10669',
    float(1/(8*sp.sqrt(2))) <= float(sp.sin(3*pi/8)**2/8))
for uu in (0, sp.Rational(3, 10), sp.Rational(1, 3), sp.Rational(3, 5)):
    print('     frozen saturation sign sin(3 pi u/4 - pi/4) at u=%s: %+.4f' % (uu, float(sp.sin(3*pi*uu/4 - pi/4))))
print('     frozen saturation factors at u=0.6, r0=1, g^2=1/2: gamma=-0.2 -> %.4f, gamma=-0.05 -> %.4f'
      % (float(sp.exp(sp.sin(3*pi*sp.Rational(3, 5)/4 - pi/4)/(8*sp.Rational(1, 5)))),
         float(sp.exp(sp.sin(3*pi*sp.Rational(3, 5)/4 - pi/4)/(8*sp.Rational(1, 20))))))

# (3) commuting-ray growth form at u=0: B = v v^T - u u^T on span{e0, rhat}
R, x0 = sp.symbols('R x0', real=True)
uu_ = sp.Matrix([sp.cos(3*pi/8)*x0, sp.cos(pi/8)*R]); vv_ = sp.Matrix([sp.sin(3*pi/8)*x0, -sp.sin(pi/8)*R])
B = sp.simplify(vv_*vv_.T - uu_*uu_.T)
rep('(3a) B = (1/sqrt2) [[r0^2, -r0 R], [-r0 R, -R^2]]',
    sp.simplify(B - sp.Matrix([[x0**2, -x0*R], [-x0*R, -R**2]])/sp.sqrt(2)) == sp.zeros(2))
lmax = (x0**2 - R**2 + sp.sqrt(x0**4 + 6*x0**2*R**2 + R**4))/(2*sp.sqrt(2))
rep('(3b) lambda_max formula is an eigenvalue of B', sp.simplify((B - lmax*sp.eye(2)).det()) == 0)
rep('(3c) det B = -r0^2 R^2 (one positive eigenvalue iff r0 R != 0); r0=0: lambda_max = 0',
    sp.simplify(B.det() + x0**2*R**2) == 0 and sp.simplify(lmax.subs(x0, 0)) == 0)

# (4) rank-one corner maximisation: max_rho [b rho/2 - A rho^2] = b^2/(16 A)
b, A, rr = sp.symbols('b A rho', positive=True)
f = b*rr/2 - A*rr**2
rs = sp.solve(sp.diff(f, rr), rr)[0]
rep('(4a) max of b rho/2 - A rho^2 is b^2/(16 A)', sp.simplify(f.subs(rr, rs) - b**2/(16*A)) == 0)
c0 = sp.sin(3*pi*(1 - u)/8)**2*r0**2/(16*sp.cos(3*pi*u/4))
rep('(4b) c0(u) = sin^2(3pi(1-u)/8) r0^2/(16 cos(3 pi u/4)) > 0 at u=0.3 and r0=1',
    float(c0.subs({u: sp.Rational(3, 10), r0: 1})) > 0)
# lower bound |2cos(z/sqrt2)| >= 2 sinh(|Im z|/2): rank-one H with Tr H^2 = 1 has eigenvalues +-1/sqrt2
ok_lb = True
for z in (mp.mpc(0.3, 2.0), mp.mpc(-1.7, 0.4), mp.mpc(5, -3), mp.mpc(0, 0.01)):
    ok_lb &= abs(2*mp.cos(z/mp.sqrt(2))) >= 2*mp.sinh(abs(z.imag)/2)
rep('(4c) |O_k| >= 2 sinh(b rho/2) on rank-one rays (Tr H^2 = 1; valid, not sharp)', ok_lb)

# (5) R_{u'} as a linear contour: Re Lambda^T Lambda = diag(cos(3 pi u'/4), cos(pi u'/4),...) > 0 iff u' < 2/3
up = sp.symbols('up', positive=True)
rep('(5a) temporal entry cos(3 pi u/4) vanishes at u=2/3 and is positive below',
    sp.simplify(sp.cos(3*pi*sp.Rational(2, 3)/4)) == 0 and float(sp.cos(3*pi*sp.Rational(65, 100)/4)) > 0)
rep('(5b) path tau -> R_{tau up} keeps Re Lambda^T Lambda positive definite for up<2/3 (sampled)',
    all(float(sp.cos(3*pi*t*sp.Rational(13, 20)/4)) > 0 and float(sp.cos(pi*t*sp.Rational(13, 20)/4)) > 0
        for t in [sp.Rational(i, 20) for i in range(21)]))

# (6) 057, mass side: beta(eps,gamma) = eps cos(3 pi u/4) + |gamma| sin(3 pi u/4)/(2 g^2)
bu = sp.symbols('b_u', positive=True)
beta = eps*sp.cos(3*pi*u/4) + G*sp.sin(3*pi*u/4)/(2*g**2)
lim = sp.limit(bu**2/(16*beta), eps, 0)
rep('(6a) b_u^2/(16 beta) -> g^2 b_u^2/(8 |gamma| sin(3 pi u/4)) as eps -> 0+ (Gamma_0/|gamma|)',
    sp.simplify(lim - g**2*bu**2/(8*G*sp.sin(3*pi*u/4))) == 0)
vals = {u: sp.Rational(3, 10), G: sp.Rational(1, 5), g: 1, bu: 1, eps: sp.Rational(1, 100)}
rep('(6b) at eps>0 (u<2/3) beta exceeds its limit, so b_u^2/(16 beta) < Gamma_0/|gamma|: the old ">=" gives no lower bound',
    float((bu**2/(16*beta)).subs(vals)) < float(lim.subs(vals)))

print('OVERALL: ' + ('ALL CHECKS PASS' if all(ok) else 'SOME CHECK FAILED'))
