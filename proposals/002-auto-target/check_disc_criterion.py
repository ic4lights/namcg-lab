"""Principal-sheet zeros of F(x) = 1 - (1/a) x (ln(1/x) + c), x = k^2/Lam^2,
with the principal logarithm (cut along x < 0, the timelike axis in (-,+,+,+)).

Checks:
 1. Only Lambert branches W_0 and W_{-1} give principal-sheet zeros
    (Im ln x in (-pi, pi]); other branches are tested and rejected.
 2. min |x| over principal-sheet zeros is increasing in a at fixed c, so
    'no zero in the disc |x|<1' is equivalent to a > a*(c).
 3. a*(c) at several c, and a*(0) = pi/2 (unit-circle crossing at x = +-i).
 4. Independent check by the argument principle: number of zeros of F in
    the disc |x| < 1 (contour |x| = 1 - 1e-9 avoiding the cut by small
    indentation is unnecessary: F is analytic in the slit disc, and we
    count zeros in the slit disc by integrating F'/F around a keyhole).
"""
import mpmath as mp
mp.mp.dps = 30

def principal_zeros(a, c):
    b = a * mp.e**(-c)
    zs = []
    for k in range(-6, 7):
        W = mp.lambertw(-b, k)
        if -mp.pi < mp.im(W) <= mp.pi:
            x = mp.e**c * mp.e**W  # y = e^W solves y ln(1/y) = b, x = e^c y
            res = x * (-mp.log(x) + c) - a
            if abs(res) < 1e-20:
                zs.append((k, x))
    return zs

print('branches giving principal-sheet zeros:')
for a, c in [(10, 0), (1, 0), (0.2, 0), (10, -10), (1.5, 1.42)]:
    print(f'  a={a}, c={c}:', [(k, mp.nstr(x, 6)) for k, x in principal_zeros(a, c)])

def minabs(a, c):
    zs = principal_zeros(a, c)
    return min(abs(x) for _, x in zs) if zs else mp.inf

print('\nmonotonicity scan of min|x| in a:')
for c in (-4, -2, 0, 2 - mp.euler, 3):
    prev = None
    mono = True
    for i in range(1, 400):
        a = mp.mpf(i) / 20
        m = minabs(a, c)
        if prev is not None and m < prev - mp.mpf('1e-20'):
            mono = False
        prev = m
    astar = mp.findroot(lambda a: minabs(a, c) - 1, 1.5)
    print(f'  c={mp.nstr(c,5):>7}: monotone increasing = {mono};  a*(c) = {mp.nstr(astar, 10)}')
print('  pi/2 =', mp.nstr(mp.pi / 2, 10))

# argument-principle count in the slit unit disc (keyhole around cut on x<0)
def count_zeros(a, c, r=mp.mpf('0.999999'), eps=mp.mpf('1e-12'), rho=mp.mpf('1e-8')):
    F = lambda x: 1 - x * (-mp.log(x) + c) / a
    dF = lambda x: -(-mp.log(x) + c - 1) / a
    g = lambda x: dF(x) / F(x)
    # outer circle from angle -pi+eps to pi-eps
    I = mp.quad(lambda t: g(r * mp.e**(1j * t)) * 1j * r * mp.e**(1j * t), [-mp.pi + eps, 0, mp.pi - eps])
    # upper edge of cut from -r to -rho (x = s e^{i(pi-eps)}), inner small circle, lower edge back
    I += mp.quad(lambda s: g(s * mp.e**(1j * (mp.pi - eps))) * (-mp.e**(1j * (mp.pi - eps))), [rho, r])
    I += mp.quad(lambda t: g(rho * mp.e**(1j * t)) * 1j * rho * mp.e**(1j * t), [mp.pi - eps, 0, -mp.pi + eps])
    I += mp.quad(lambda s: g(s * mp.e**(-1j * (mp.pi - eps))) * mp.e**(-1j * (mp.pi - eps)), [rho, r])
    return I / (2j * mp.pi)

print('\nargument-principle zero counts in slit disc |x|<1:')
for a, c in [(10, 0), (2, 0), (1.4, 0), (1, 0), (0.2, 0), (10, -11), (10, -9)]:
    n = count_zeros(a, c)
    print(f'  a={a}, c={c}: N = {mp.nstr(mp.re(n), 6)} (imag {mp.nstr(mp.im(n), 3)});  Lambert zeros inside:',
          sum(1 for _, x in principal_zeros(a, c) if abs(x) < 1))

# ---- threshold curve Upsilon_*(delta) and the window for Upsilon = 10
print('\nthreshold Upsilon_*(delta) (no zero in |x|<1 iff Upsilon > Upsilon_*):')
for d in (-10, -9.5845785, -6, -4, -2, -1, 0, 0.5, 0.9, 1, 1.5, 2, 5, 10):
    d = mp.mpf(d)
    # bracket scan in Upsilon on (0.01, 40) for crossing of min|x| = 1
    grid = [mp.mpf(i) / 100 for i in range(1, 4001)]
    prev_inside = None
    ups = None
    for U in grid:
        inside = minabs(U, d) < 1
        if prev_inside is True and inside is False:
            ups = U
        prev_inside = inside
    # after last change from inside->outside, check no re-entry
    reentry = any(minabs(U, d) < 1 for U in grid if ups is not None and U > ups)
    print(f'  delta={mp.nstr(d,6):>9}: Upsilon_* ~ {mp.nstr(ups,4):>6} (grid 0.01), re-entry above = {reentry}')

print('\nUpsilon=10 window in delta (no zero in slit unit disc):')
for d in (-9.7, -9.5, 0, 5, 9.9, 10.1, 12):
    n = count_zeros(10, d)
    print(f'  delta={d}: N = {mp.nstr(mp.re(n), 4)};  Lambert zeros inside:',
          sum(1 for _, x in principal_zeros(10, d) if abs(x) < 1))
