# s4_mean_map_d2.py - D=2: closed form of the first moment of the pushforward measure,
# E_{mu_g}(p_1), and injectivity of g/W -> E_{mu_g}(p_1) on the ordered chamber.
# Claimed closed form, with rates lam_i = 1/g_i and L = lam_1/lam_2:
#   E[p_1] = L/(L-1)^2 * ( log L + 1/L - 1 ) ... derived below and verified against direct integration.
# Run: python -I proposals/092-g-profile-coordinate-transport/s4_mean_map_d2.py
import sympy as sp

fails = []
def chk(name, cond):
    print(("OK  " if cond else "FAIL") + " " + name)
    if not cond:
        fails.append(name)

l1, l2, s, u = sp.symbols('lambda1 lambda2 s u', positive=True)
Lam = l1*s + l2*(1-s)
E_direct = sp.integrate(s*l1*l2/Lam**2, (s, 0, 1))
E_direct = sp.simplify(E_direct)
print("   direct integration E[p_1] =", E_direct)

# closed form in ratio L = l1/l2
L = sp.symbols('L', positive=True)
cf = L/(L-1)**2*(sp.log(L) + 1/L - 1)
cf_simpl = sp.simplify(cf)
diff = sp.simplify(E_direct - cf_simpl.subs(L, l1/l2))
chk("closed form matches direct integration (D=2, L != 1)", diff == 0)

# limit L -> 1 is 1/2
chk("limit L->1 equals 1/2", sp.limit(cf, L, 1) == sp.Rational(1, 2))
# limit L -> oo is 1 (g_2 -> 0 : p_1 -> 1)
chk("limit L->oo equals 0 (E[p_1] decreases 1/2 -> 0 as lam1/lam2 -> oo)", sp.limit(cf, L, sp.oo) == 0)

# monotonicity on L in (1, oo): derivative strictly negative
dL = sp.simplify(sp.diff(cf, L))
dL_num = sp.lambdify(L, dL, "mpmath")
import mpmath
mpmath.mp.dps = 30
vals = [dL_num(x) for x in [mpmath.mpf('1.0001'), mpmath.mpf('1.01'), mpmath.mpf('2'),
                            mpmath.mpf('10'), mpmath.mpf('1000'), mpmath.mpf('1e6')]]
print("   d/dL at sample L:", [str(v)[:12] for v in vals])
chk("derivative strictly negative on sampled L in (1,oo)", all(v < 0 for v in vals))
# series sign near L=1: cf = 1/2 - (L-1)/12 + ... ? get series
ser = sp.series(cf, L, 1, 3).removeO()
print("   expansion about L=1:", sp.simplify(ser))
c1 = sp.simplify(sp.diff(cf, L).subs(L, 1)) if sp.diff(cf, L).subs(L, 1).is_finite else sp.limit(sp.diff(cf, L), L, 1)
print("   slope at L=1 (limit):", sp.limit(sp.diff(cf, L), L, 1))
chk("slope at L=1 strictly negative", sp.limit(sp.diff(cf, L), L, 1) < 0)

# second derivative / global negativity of dL: check dL < 0 symbolically via numerator sign after substitution L = e^t, t>0
t = sp.symbols('t', positive=True)
et = sp.exp(t)
dft = sp.simplify(dL.subs(L, et)*et)   # d/dt
num = sp.together(dft)
print("   d/dt form:", sp.simplify(num))
f2 = sp.lambdify(t, num, "mpmath")
neg = all(f2(x) < 0 for x in [mpmath.mpf('0.001'), mpmath.mpf('0.1'), mpmath.mpf('1'),
                              mpmath.mpf('5'), mpmath.mpf('20')])
chk("d/dt of cf at L=exp(t) strictly negative on sampled t>0", neg)

# numeric cross-check: E[p_1] at g=(2,5) vs quadrature of the 089 density
import random, math
random.seed(4)
g1v, g2v = 2.0, 5.0
# quadrature via the 089 density on the interval
import mpmath as mp
mp.mp.dps = 25
dens = lambda p: 1/(g1v*g2v*(p/g1v + (1-p)/g2v)**2)
ref = mp.quad(lambda p: p*dens(p), [0, 1])
got = float(cf.subs(L, g2v and (1/g1v)/(1/g2v)))
print("   g=(2,5): quadrature %.10f closed form %.10f" % (ref, got))
chk("quadrature matches closed form at g=(2,5)", abs(ref-got) < 1e-12)

print("S4:", "PASS" if not fails else "FAIL " + str(fails))
