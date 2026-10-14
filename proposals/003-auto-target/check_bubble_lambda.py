"""Check 2 (proposal 003): Lambda_UV dependence of the one-loop two-derivative term
for the radial singlet sigma, displayed action on the flat scaffold, A_mu = 0 held fixed.

Background Phi_bar = (v + sigma) I.  From check_scaffold_hessian.py:
  16 Hermitian components with E_H(sigma), E_H(0) = m_H^2 = lam v^2, E_H'(0) = 3 lam v;
  16 anti-Hermitian components with E_K(sigma), E_K(0) = 0,          E_K'(0) = lam v.
Euclidean one-loop Gamma = (1/2) Tr ln(-d^2 + E), proper-time cutoff s_min = Lambda^-2 as in eq:W-again
(the regulator uses the scaffold Laplacian).  At second order in sigma:
  Gamma^(1) > -(1/4) sum_b n_b E_b'^2 int d^4p/(2pi)^4 sigma(p) sigma(-p) B_b(p) + (p-independent tadpoles),
  B(p) = int d^4k/(2pi)^4 [ (k^2+m^2)((k+p)^2+m^2) ]^-1  (regulated)
       = (1/16 pi^2) int_0^1 dx int_{Lambda^-2}^infty ds/s exp(-s(m^2 + x(1-x)p^2))
       = (1/16 pi^2) int_0^1 dx E1((m^2 + x(1-x) p^2)/Lambda^2).
We check: the p^2 coefficient of B is -exp(-m^2/Lambda^2)/(96 pi^2 m^2) (no Lambda^2, no log Lambda),
and the resulting local (d sigma)^2 coefficient of Gamma_E from the Hermitian block,
Delta(Z/2) = 3 lam/(8 pi^2) * exp(-lam v^2/Lambda^2), i.e. Delta Z = 3 lam/(4 pi^2) up to O(lam v^2/Lambda^2).
Also a numerical check of the proper-time-regulated B against direct quadrature.
"""
import sympy as sp
import mpmath as mp

p2, m2, L, x, s = sp.symbols('p2 m2 Lambda x s', positive=True)
lam, v = sp.symbols('lambda v', positive=True)

# p^2-derivative of the integrand at p^2 = 0: d/dp2 E1(M/L^2) = -exp(-M/L^2)/M * dM/dp2, M = m2 + x(1-x)p2
M = m2 + x*(1 - x)*p2
dE1 = -sp.exp(-M/L**2)/M*sp.diff(M, p2)
coef = sp.integrate(dE1.subs(p2, 0), (x, 0, 1))/(16*sp.pi**2)
coef = sp.simplify(coef)
print('p^2 coefficient of B:', coef)
print('  equals -exp(-m2/L^2)/(96 pi^2 m2):', sp.simplify(coef + sp.exp(-m2/L**2)/(96*sp.pi**2*m2)) == 0)
print('  large-Lambda series:', sp.series(coef, L, sp.oo, 3))

# sanity: E1 representation of the proper-time integral
z = sp.symbols('z', positive=True)
print('  int_{L^-2}^oo ds/s e^{-s z} == E1(z/L^2) (numeric, z=0.7, L=3):',
      mp.almosteq(mp.quad(lambda ss: mp.exp(-ss*mp.mpf('0.7'))/ss, [mp.mpf(1)/9, mp.inf]), mp.e1(mp.mpf('0.7')/9)))

# local (d sigma)^2 coefficient from the Hermitian block
nH, EHp = 16, 3*lam*v
dGamma = sp.Rational(-1, 4)*nH*EHp**2*coef.subs(m2, lam*v**2)   # coefficient of p^2 sigma sigma
print('Gamma_E (d sigma)^2 coefficient from H block:', sp.simplify(dGamma))
print('  Delta Z = 2*that =', sp.simplify(2*dGamma), ' -> leading', sp.limit(2*dGamma, L, sp.oo))
print('  tree Z = 2N = 8; relative correction (leading):', sp.limit(2*dGamma, L, sp.oo)/8)

# massless block: p^2 term of B0 is O(p^2/Lambda^2) plus non-analytic log p^2
B0_series = sp.series(-sp.EulerGamma - sp.log(x*(1 - x)*p2/L**2) + x*(1 - x)*p2/L**2, p2, 0, 2)
print('massless integrand small-z expansion (E1(z) = -gamma - ln z + z + ...):', B0_series)
print('  analytic p^2 coefficient after x-integration:',
      sp.integrate(x*(1 - x), (x, 0, 1))/(16*sp.pi**2), '/ Lambda^2')

# numeric cross-check of B(p) with direct 4D Euclidean quadrature of the proper-time-regulated bubble
mp.mp.dps = 30
def B_formula(p2v, m2v, Lv):
    return mp.quad(lambda xx: mp.e1((m2v + xx*(1 - xx)*p2v)/Lv**2), [0, 1])/(16*mp.pi**2)
def B_direct(p2v, m2v, Lv):
    # int d^4k/(2pi)^4 int_0^1 dx int_{L^-2}^oo ds s e^{-s[(k+xp)^2 + m^2 + x(1-x)p^2]}; k-integral done exactly
    f = lambda xx, ss: ss*mp.exp(-ss*(m2v + xx*(1 - xx)*p2v))/(16*mp.pi**2*ss**2)
    return mp.quad(lambda xx: mp.quad(lambda ss: f(xx, ss), [1/Lv**2, 1, mp.inf]), [0, 1])
for Lv in (10, 100, 1000):
    a, b = B_formula(mp.mpf('0.3'), 1, Lv), B_direct(mp.mpf('0.3'), 1, Lv)
    h = mp.mpf('1e-6')
    d = (B_formula(h, 1, Lv) - B_formula(0, 1, Lv))/h
    print(f'Lambda/m = {Lv:5d}:  B formula {mp.nstr(a, 12)}  direct {mp.nstr(b, 12)}  '
          f'dB/dp2(0) {mp.nstr(d, 10)}  vs -exp(-1/L^2)/(96 pi^2) = {mp.nstr(-mp.exp(-1/mp.mpf(Lv)**2)/(96*mp.pi**2), 10)}')
