"""040 t4: continuation prescription check on the leading-symbol Zeeman integral
   J = int_0^infty ds  a b /( sinh(a s) sin(b s) ) * ( chi_V(s) - 4 ),  chi_V = e^{2as} + e^{-2as} + e^{2ibs} + e^{-2ibs},
which has no convergent ray (E+ grows for theta < theta*, B+ grows for theta > theta*, theta* = arctan(a/b)).
(1) branch-wise: each exponential branch integrated on its own ray (E+ on theta_E > theta*, B+ on theta_B < theta*, the rest anywhere; the -4 term and the
    1/s^2 UV behaviour are split between branches by the regulated-at-zero form  -4 + 2... : we integrate the full integrand pieces on the same ray as the branch they multiply,
    splitting the '-4' equally  (all branches carry -1) );
(2) Abel/regulator: multiply by exp(-i s m2) (positive m2 opens a common window around theta*), integrate on theta*, extrapolate m2 -> 0+.
Agreement shows (2) = (1) = analytic continuation, and that the value is not ray dependent."""
import sys, mpmath as mp
sys.dont_write_bytecode = True
mp.mp.dps = 25
a = mp.mpf('1.6'); b = mp.mpf('0.9')
ths = mp.atan(a / b)
def Th(s):
    return a * b / (mp.sinh(a * s) * mp.sin(b * s))
def ray_int(f, th, rmax):
    ph = mp.expj(-th)
    g = lambda r: f(r * ph) * ph
    pts = [mp.mpf(rmax) * k / 160 for k in range(161)]
    return mp.quad(g, pts)
branches = {'E+': 2 * a, 'E-': -2 * a, 'B+': 2j * b, 'B-': -2j * b}
def f_branch(mu, m2=0):
    return lambda s: Th(s) * (mp.exp(mu * s) - 1) * mp.exp(-1j * s * m2)
# (1) branch-wise: group E+ with E- (cancelling 1/s at s->0) on a ray theta_E>theta*, B+ with B- on a ray theta_B<theta*
def grp(mus, th):
    rate = a * mp.cos(th) + b * mp.sin(th)
    return ray_int(lambda s: Th(s) * sum(mp.exp(mu * s) - 1 for mu in mus), th, 45 / rate)
tot1 = 0
for thE, thB in ((ths + mp.mpf('0.25'), ths - mp.mpf('0.5')), (ths + mp.mpf('0.1'), ths - mp.mpf('0.3'))):
    vE = grp([2 * a, -2 * a], thE); vB = grp([2j * b, -2j * b], thB)
    print('thetaE %s thetaB %s  E-group %s  B-group %s  total %s' % (mp.nstr(thE, 4), mp.nstr(thB, 4), mp.nstr(vE, 12), mp.nstr(vB, 12), mp.nstr(vE + vB, 12)))
# (2) regulator
vals = []
for m2 in (mp.mpf('0.8'), mp.mpf('0.6'), mp.mpf('0.4'), mp.mpf('0.3'), mp.mpf('0.2'), mp.mpf('0.15'), mp.mpf('0.1')):
    f = lambda s: sum(Th(s) * (mp.exp(mu * s) - 1) for mu in branches.values()) * mp.exp(-1j * s * m2)
    rate = m2 * mp.sin(ths)
    v = ray_int(f, ths, 40 / rate)
    vals.append((m2, v)); print('m2', mp.nstr(m2, 3), mp.nstr(v, 12))
# polynomial (Richardson) extrapolation in m2
xs = [x for x, _ in vals]; ys = [y for _, y in vals]
for n in (3, 4, 5, 6):
    pts = list(zip(xs[-n:], ys[-n:]))
    # Neville at 0
    P = [y for _, y in pts]
    for k in range(1, n):
        P = [(-pts[i + k][0] * P[i] + pts[i][0] * P[i + 1]) / (pts[i][0] - pts[i + k][0]) for i in range(n - k)]
    print('extrapolation (last %d points) to m2=0:' % n, mp.nstr(P[0], 12))
