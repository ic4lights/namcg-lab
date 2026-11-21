#!/usr/bin/env python3
"""054-055 r2: independent symbolic checks of the claims carried by the corrected inserts.
Run: python -I proposals/local-gpu/054-055-r2/check_r2.py
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

# (2) one-dimensional branch model on R_u: Q = e^{-3 pi i u/4}(eps - i gam/(2 g^2)), gc = c e^{i phi} r0/2.
u, eps, r0, g, G = sp.symbols('u epsilon r0 g Gamma', positive=True)  # G = |gamma| > 0, gamma = -G
pi = sp.pi
def expo(phi, Q):
    return -(sp.exp(sp.I*phi)*r0/2)**2/(4*Q)
Q0 = sp.exp(-3*pi*sp.I*u/4)*eps                      # gamma = 0
Qm = sp.exp(-3*pi*sp.I*u/4)*(sp.I*G/(2*g**2))        # gamma = -G, eps -> 0
frozen, contour = 3*pi/8, 3*pi*(1 - u)/8
def re(e):
    return sp.simplify(sp.re(sp.expand_complex(e)))
e_f0, e_c0 = re(expo(frozen, Q0)), re(expo(contour, Q0))
e_fm, e_cm = re(expo(frozen, Qm)), re(expo(contour, Qm))
rep('(2a) frozen, gamma=0: r0^2 cos(3 pi u/4 - pi/4)/(16 eps)',
    sp.simplify(e_f0 - r0**2*sp.cos(3*pi*u/4 - pi/4)/(16*eps)) == 0)
rep('(2b) frozen, fixed gamma<0, eps->0 (g=1): r0^2 sin(3 pi u/4 - pi/4)/(8|gamma|)',
    sp.simplify((e_fm - r0**2*sp.sin(3*pi*u/4 - pi/4)/(8*G)).subs(g, 1)) == 0)
rep('(2c) contour coefficient, gamma=0: r0^2/(16 sqrt2 eps), independent of u',
    sp.simplify(e_c0 - r0**2/(16*sp.sqrt(2)*eps)) == 0)
rep('(2d) contour coefficient, fixed gamma<0: -g^2 r0^2/(8 sqrt2 |gamma|), independent of u',
    sp.simplify(e_cm + g**2*r0**2/(8*sp.sqrt(2)*G)) == 0)
rep('(2e) coefficient of tilde A_0 in k.A on R_u at k^0 = e^{3 pi i/8} r0 is e^{3 pi i (1-u)/8} r0',
    sp.simplify(sp.exp(3*pi*sp.I/8)*sp.exp(-3*pi*sp.I*u/8) - sp.exp(3*pi*sp.I*(1 - u)/8)) == 0)
rep('(2f) frozen and contour models agree at u=0 (corner value 0.0441942/eps at r0=1)',
    sp.simplify((e_f0 - e_c0).subs(u, 0)) == 0 and abs(float((e_c0*eps).subs(r0, 1)) - 0.0441942) < 1e-6)
for uu in (0, sp.Rational(3, 10), sp.Rational(1, 3), sp.Rational(3, 5)):
    print('     frozen saturation sign sin(3 pi u/4 - pi/4) at u=%s: %+.4f' % (uu, float(sp.sin(3*pi*uu/4 - pi/4))))
print('     frozen saturation factors at u=0.6, r0=1: gamma=-0.2 -> %.4f, gamma=-0.05 -> %.4f'
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

print('OVERALL: ' + ('ALL CHECKS PASS' if all(ok) else 'SOME CHECK FAILED'))
