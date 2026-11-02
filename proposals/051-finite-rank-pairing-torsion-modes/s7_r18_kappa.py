"""051 s7: check of R18 (review-r2.md), independent of the helper functions of s3.  Read-only.

Claim checked: on the Gaussian w of variance P^2 per component and phi^2 = exp(-t^2/sigma^2)/(sigma sqrt(pi)),
   kappa = -sqrt2 sigma P exp(+sigma^2/4) for the boost, -sqrt2 sigma P exp(-sigma^2/4) for the rotation,
so kappa = -sqrt2 sigma P (1 + O(sigma^2)), and the bare -sqrt2 sigma P is the leading term and not the exact value.

 A  the part of Q2 odd in t is sinh(t) v.p (boost) or sin(t) v.p (rotation), exact.
 B  kappa = <O1, Q2 O2> by direct exact integration of the full Q2, with no use of A or of integration by parts.
 C  series of kappa in sigma: relative correction +-sigma^2/4.
 D  floating-point quadrature of the same integral, and comparison with the values printed by s3 (r1 output).
"""
import os
import re

import mpmath as mp
import sympy as sp

here = os.path.dirname(os.path.abspath(__file__))
d = 4
eta = sp.diag(-1, 1, 1, 1)
sig, P = sp.symbols('sigma P', positive=True)
t = sp.Symbol('t', real=True)
ps = sp.symbols('p0:4', real=True)
pv = sp.Matrix(ps)
k = sp.Matrix([-1, 1, 0, 0])
phi2 = sp.exp(-t ** 2 / sig ** 2) / (sig * sp.sqrt(sp.pi))
psi1psi2 = sig / sp.sqrt(2) * sp.diff(phi2, t)  # psi1 psi2 = phi sqrt2 sigma phi'


def gauss_p(expr):
    out = sp.S.Zero
    for mon, co in sp.Poly(sp.expand(expr), *ps).terms():
        f = co
        for m_ in mon:
            f = f * (0 if m_ % 2 else (sp.factorial2(m_ - 1) * P ** m_ if m_ > 0 else 1))
        out += f
    return out


def case(name, Lam, odd, sign):
    print('---', name)
    assert sp.simplify(Lam.T * eta * Lam - eta) == sp.zeros(4) or sp.simplify(Lam * eta * Lam.T - eta) == sp.zeros(4)
    vec = k + (sp.eye(d) - Lam) * pv
    Q2 = sp.expand((vec.T * eta * vec)[0])
    dQ0 = sp.expand(sp.diff(Q2, t).subs(t, 0))
    v = sp.Matrix([sp.diff(dQ0, x) for x in ps])
    vp = (v.T * pv)[0]
    print('A  v =', list(v), ', |v|^2 =', (v.T * v)[0])
    assert (v.T * v)[0] == 4
    oddpart = sp.simplify((Q2 - Q2.subs(t, -t)) / 2 - odd * vp)
    print('A  (Q2(t)-Q2(-t))/2 minus %s(t) v.p =' % odd.func.__name__, oddpart)
    assert oddpart == 0
    a = gauss_p(vp ** 2)
    assert sp.simplify(a - 4 * P ** 2) == 0
    # p-integral first, for fixed t; then the t-integral of the whole function
    Ft = gauss_p(vp * Q2) / sp.sqrt(a)
    integrand = sp.expand((psi1psi2 * Ft).rewrite(sp.exp))
    kappa = sp.simplify(sp.integrate(integrand, (t, -sp.oo, sp.oo)).rewrite(sp.erf))  # sympy leaves erf + erfc unreduced otherwise
    predicted = -sp.sqrt(2) * sig * P * sp.exp(sign * sig ** 2 / 4)
    print('B  kappa by direct integration =', kappa)
    print('B  kappa - predicted =', sp.simplify(kappa - predicted))
    assert sp.simplify(kappa - predicted) == 0
    rel = sp.series(kappa / (-sp.sqrt(2) * sig * P), sig, 0, 4).removeO()
    print('C  kappa / (-sqrt2 sigma P) =', rel, '+ O(sigma^4)')
    assert sp.expand(rel - (1 + sign * sig ** 2 / 4)) == 0
    assert sp.simplify(kappa / (-sp.sqrt(2) * sig * P)) != 1
    # D: floating point, full Q2, weight phi^2, using the derivative of the weight as written
    Ff = sp.lambdify(t, Ft.subs(P, 1), 'mpmath')
    out = []
    for s_ in (mp.mpf(1) / 10, mp.mpf(1) / 20, mp.mpf(1) / 100):
        w12 = lambda x: (s_ / mp.sqrt(2)) * (-2 * x / s_ ** 2) * mp.exp(-x ** 2 / s_ ** 2) / (s_ * mp.sqrt(mp.pi))
        val = mp.quad(lambda x: w12(x) * Ff(x), [-12 * s_, 0, 12 * s_])
        ex = -mp.sqrt(2) * s_ * mp.exp(sign * s_ ** 2 / 4)
        bare = -mp.sqrt(2) * s_
        print('D  sigma=%s quadrature %s closed form %s bare leading term %s' % (mp.nstr(s_, 3), mp.nstr(val, 10), mp.nstr(ex, 10), mp.nstr(bare, 10)))
        assert abs(val - ex) < mp.mpf(10) ** (-12)
        out.append((s_, ex))
    return kappa


mp.mp.dps = 30
ch, sh = sp.cosh(t), sp.sinh(t)
Lb = sp.Matrix([[ch, 0, sh, 0], [0, 1, 0, 0], [sh, 0, ch, 0], [0, 0, 0, 1]])
c_, s_ = sp.cos(t), sp.sin(t)
Lr = sp.Matrix([[1, 0, 0, 0], [0, c_, -s_, 0], [0, s_, c_, 0], [0, 0, 0, 1]])
kb = case('boost(0,2)', Lb, sh, +1)
kr = case('rotation(1,2)', Lr, s_, -1)

print('--- comparison with the printed values of s3 (r1 output), P = 1')
txt = open(os.path.join(here, 's3_cutoff_pencil.r1.out.txt')).read()
rows = re.findall(r'P=1 eps=1/(\d+)\s+H12=(-?[0-9.e+-]+)', txt)
assert len(rows) == 6
for i, (den, val) in enumerate(rows):
    s_v = mp.mpf(1) / int(den)
    sign = 1 if i < 3 else -1
    ex = -mp.sqrt(2) * s_v * mp.exp(sign * s_v ** 2 / 4)
    print('  %-8s sigma=1/%-4s s3 %s closed form %s' % ('boost' if sign > 0 else 'rotation', den, val, mp.nstr(ex, 7)))
    assert '%.6e' % float(ex) == val

print('--- the bytes of R18 state the form that was checked')
review = open(os.path.join(here, 'review-r2.md'), 'rb').read()
assert review.count(rb'(\(\varkappa=-\sqrt2\sigma P\,(1+O(\sigma^2))\) for the Gaussian') == 1
assert review.count(rb'The entries of this compression are evaluated exactly on a Gaussian') == 1
print('  new string of R18 contains the (1+O(sigma^2)) form and "The entries of this compression"')
print('ALL ASSERTIONS PASSED')
