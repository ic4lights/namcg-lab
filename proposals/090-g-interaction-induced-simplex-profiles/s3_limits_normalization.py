import sympy as sp
import mpmath as mp
b = sp.symbols('beta', positive=True)
p = sp.symbols('p', positive=True)
Z2a1 = sp.simplify(2*sp.integrate((2*p-1)**b, (p, sp.Rational(1,2), 1)))
print('Z2_a1_closed:', Z2a1, 'beta0_limit:', sp.limit(Z2a1, b, 0), flush=True)
mp.mp.dps = 12
for av, bv in [(mp.mpf(2), mp.mpf('0.5')), (mp.mpf(3), mp.mpf(2)), (mp.mpf('1.3'), mp.mpf('0.25'))]:
    num = 2*mp.quad(lambda pp: (pp*(1-pp))**(av-1)*abs(2*pp-1)**bv, [mp.mpf('0.5'), 1])
    closed = 4**(1-av)*mp.beta((bv+1)/2, av)/2
    print('Z2_betaform_check a=%s beta=%s num=%s closed=%s' % (av, bv, mp.nstr(num, 12), mp.nstr(closed, 12)), flush=True)
t = sp.symbols('t', positive=True)
f = t*(1-t)*(2*t-1)
rts = [r for r in sp.solve(sp.diff(f, t), t) if r.is_real and (r > sp.Rational(1,2)) and (r < 1)]
print('A1_D3_FACE_MAX_t:', [sp.simplify(r) for r in rts], [sp.N(r, 10) for r in rts], flush=True)
k1 = t*(1-t)*(2*t-1)**b
lim = sp.limit((k1/(t*(1-t)) - 1)/b, b, 0)
print('KERNEL_EXPANSION_slope_a2_D2:', sp.simplify(lim), flush=True)
# Z3: integral of prod|pi-pj|^beta over the ordered simplex (a=1 flat base), inner x2 in (0, min(x1, 1-x1))
# (v3 had a bug: it integrated x2 up to x1 even for x1 > 1/2, letting x3 = 1-x1-x2 go negative; fixed here (upper limit 1-x1 plus cusp breakpoints).)
def Zft3(bv, av):
    def inner(x1):
        hi = 1-x1  # full simplex: x3 > 0 iff x2 < 1-x1
        bps = [mp.mpf(0)]
        for c in [(1-x1)/2, 1-2*x1, x1/2]:
            if 0 < c < hi:
                bps.append(c)
        bps.append(hi)
        bps = sorted(set(bps))
        def g(x2):
            x3 = 1-x1-x2
            v = 1
            if av != 1:
                v = (x1*x2*x3)**(av-1)
            return v*abs(x1-x2)**bv*abs(x1-x3)**bv*abs(x2-x3)**bv
        s = mp.mpf(0)
        for lo, h2 in zip(bps[:-1], bps[1:]):
            s += mp.quad(g, [lo, h2])
        return s
    return mp.quad(inner, [0, mp.mpf('0.25'), mp.mpf('0.5'), mp.mpf('0.75'), 1])
for bv in ['0.5', '0.05']:
    print('Z3_a1_beta=%s:' % bv, mp.nstr(Zft3(mp.mpf(bv), 1), 10), 'target_flat=0.5', flush=True)
pm = mp.mpf
def kernD3(x, av, bv):
    v = pm(1)
    for xi in x:
        v *= xi**(av-1)
    for i in range(3):
        for j in range(i+1, 3):
            v *= abs(x[i]-x[j])**bv
    return v
A = [pm('0.8'), pm('0.15'), pm('0.05')]
B = [pm('0.6465642069'), pm('0.2754506074'), pm('0.0779851856')]
print('NONFLAT_ratio_a2b1:', mp.nstr(kernD3(A, 2, 1)/kernD3(B, 2, 1), 8), flush=True)
print('AT_BARYCENTER:', kernD3([pm(1)/3]*3, 2, 1), 'AT_STAR:', mp.nstr(kernD3(B, 2, 1), 8), flush=True)
print('S3 OK', flush=True)
