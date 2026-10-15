"""Round-2 checks (proposal 003).
(A) Finite infrared limit s_max = mu^-2 (eq:s-limits) for the local (d sigma)^2 coefficient of the
    flat-scaffold one-loop action, A_mu = 0 fixed.  With
      B(p) = (1/16 pi^2) int_0^1 dx [E1(M/L^2) - E1(M/mu^2)],  M = m^2 + x(1-x)p^2,
    check  dB/dp^2|0 (massive)  = -(exp(-m^2/L^2) - exp(-m^2/mu^2))/(96 pi^2 m^2),
           dB/dp^2|0 (massless) = (1/L^2 - 1/mu^2)/(96 pi^2)   (for p^2 << mu^2),
    and the totals  Delta Z_H = (3 lam/4pi^2)(e^{-lam v^2/L^2} - e^{-lam v^2/mu^2}),
                    Delta Z_K = (lam^2 v^2/12 pi^2)(1/mu^2 - 1/L^2).
(B) psi-T orthogonality at Phi_bar = v I: with delta = (psi/4) I + eta T (T symmetric, eta^{mu nu}T_{mu nu}=0)
    the cross terms of the kinetic form Tr(d delta^dag d delta) and of the second variation of V vanish.
"""
import sympy as sp, mpmath as mp, itertools

p2, m2, L, mu, x = sp.symbols('p2 m2 Lambda mu x', positive=True)
lam, v = sp.symbols('lambda v', positive=True)

M = m2 + x*(1 - x)*p2
dB = sp.integrate((sp.diff(M, p2)*(-sp.exp(-M/L**2) + sp.exp(-M/mu**2))/M).subs(p2, 0), (x, 0, 1))/(16*sp.pi**2)
dB = sp.simplify(dB)
print('(A) massive dB/dp2(0):', dB)
print('    equals -(e^{-m2/L^2}-e^{-m2/mu^2})/(96 pi^2 m2):',
      sp.simplify(dB + (sp.exp(-m2/L**2) - sp.exp(-m2/mu**2))/(96*sp.pi**2*m2)) == 0)

# massless: series of E1 difference in z = x(1-x)p2
z = sp.symbols('z', positive=True)
E1ser = lambda zz: -sp.EulerGamma - sp.log(zz) + zz
diff0 = sp.expand(E1ser(x*(1-x)*p2/L**2) - E1ser(x*(1-x)*p2/mu**2))
coef = sp.integrate(sp.diff(diff0, p2), (x, 0, 1))/(16*sp.pi**2)
print('    massless dB/dp2(0):', sp.simplify(coef), ' target (1/L^2-1/mu^2)/(96 pi^2): ',
      sp.simplify(coef - (1/L**2 - 1/mu**2)/(96*sp.pi**2)) == 0)

dZH = sp.simplify(-8*9*lam**2*v**2*dB.subs(m2, lam*v**2))
dZK = sp.simplify(-8*lam**2*v**2*coef)
print('    Delta Z_H =', dZH)
print('    Delta Z_K =', dZK, ' target (lam^2 v^2/12pi^2)(1/mu^2-1/L^2):',
      sp.simplify(dZK - lam**2*v**2/(12*sp.pi**2)*(1/mu**2 - 1/L**2)) == 0)
print('    mu -> 0 (s_max -> oo) limit of Delta Z_H:', sp.limit(dZH, mu, 0, '+'), ' (K term diverges ~ 1/mu^2: IR-regulator dependent)')

mp.mp.dps = 30
def Bf(p2v, m2v, Lv, muv):
    return mp.quad(lambda xx: mp.e1((m2v + xx*(1-xx)*p2v)/Lv**2) - mp.e1((m2v + xx*(1-xx)*p2v)/muv**2), [0, 1])/(16*mp.pi**2)
for (Lv, muv) in ((100, 0.1), (100, 0.01), (1000, 0.05)):
    h = mp.mpf('1e-9')*muv**2
    # massless B(0) is finite: x-integrand E1(0+) diverges individually but the difference is ln(mu^2/L^2); use small m2 instead
    m2s = mp.mpf('1e-14')
    d = (Bf(h, m2s, Lv, muv) - Bf(0, m2s, Lv, muv))/h
    print(f'    L={Lv}, mu={muv}: numeric massless dB/dp2 = {mp.nstr(d, 9)}  formula = '
          f'{mp.nstr((1/mp.mpf(Lv)**2 - 1/mp.mpf(muv)**2)/(96*mp.pi**2), 9)}')
for (Lv, muv, mm) in ((100, 0.1, 1), (100, 0.5, 1)):
    h = mp.mpf('1e-7')
    d = (Bf(h, mm, Lv, muv) - Bf(0, mm, Lv, muv))/h
    f = -(mp.exp(-mp.mpf(mm)/Lv**2) - mp.exp(-mp.mpf(mm)/muv**2))/(96*mp.pi**2*mm)
    print(f'    massive m^2={mm}, L={Lv}, mu={muv}: numeric {mp.nstr(d, 9)}  formula {mp.nstr(f, 9)}')

# (B) psi-T orthogonality
eta = sp.diag(-1, 1, 1, 1)
t = sp.symbols('t0:10', real=True)
Tm = sp.zeros(4)
idx = list(itertools.combinations_with_replacement(range(4), 2))
for c, (i, j) in zip(t, idx):
    Tm[i, j] = c; Tm[j, i] = c
# impose eta^{mu nu} T_{mu nu} = 0 by solving for T_00
T00 = sp.solve(sum(eta[i, i]*Tm[i, i] for i in range(4)), Tm[0, 0])[0]
Tm = Tm.subs(Tm[0, 0], T00)
psi = sp.symbols('psi', real=True)
d1 = sp.eye(4)/4
d2 = eta*Tm
print('(B) Tr(eta T) =', sp.simplify((eta*Tm).trace()))
kin_cross = sp.simplify((d1.H*d2 + d2.H*d1).trace())
print('    kinetic cross term Tr(d1^dag d2 + d2^dag d1) =', kin_cross)
a, b = sp.symbols('a b', real=True)
lamv, vv, ph = lam, v, v
Phi = vv*sp.eye(4) + a*d1 + b*d2
X = Phi.H*Phi - vv**2*sp.eye(4)
V = lamv/4*(X*X).trace()
print('    d^2V/da db at (0,0) =', sp.simplify(sp.diff(V, a, b).subs({a: 0, b: 0})))
