"""
064 / s3: numerical illustrations on the tempered (unitary principal series of SL(2,C), integer k) side.
Units c = 1 (c > 0 drops out of the relative logarithm as eps -> 0, eps/c being the only combination).

 (a) gap: for integer k and c5 <= -9/4, min |lambda| over a grid >= 1/4; for -9/4 < c5 < -2 it is |c5 + 2|.
 (b) local determinant class near a zero: the zero (c5, k, p) = (0, 1, 0) of lambda1. With a bounded
     density in c5 (here uniform) and the Plancherel weight ~ k^2 + p^2 (polynomial, bounded on the box),
       I(eps) = int_box |log|lambda1 - i eps|| (k^2+p^2) dc5 dp
     is finite and converges as eps -> 0; the same for an atom in c5 at the zero value (1-d integral).
 (c) the relative logarithm summed over both chiralities on the same box converges as eps -> 0
     (the reference zeros a = 0 lie on the curve c5 = -p^2 inside the box).
 (d) large p at fixed (c5, k): (k^2 + p^2) * 2 Re F -> 2, so the trace over the Spin(3,1) Plancherel measure
     at a fixed value of C5 diverges linearly in a cut-off on p.
 (e) branch: replacing the principal branch by one continuous across p = 0 changes 2 Re F by
     -4 pi Im w1 = 4 pi p/|z|^2 on {p < 0, Re lambda1 < 0}; the modulus of Pf_rel depends on the branch.
"""
import numpy as np, warnings
from scipy import integrate
warnings.filterwarnings('ignore')

out = []
def log(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)

def lams(c5, k, p):
    z = k + 1j * p
    C4 = k * k - p * p - 1
    A = c5 - C4
    return A + 1 - z, A + 1 + z, A, z

# (a)
P = np.linspace(-40, 40, 8001)
mn = np.inf
for c5 in np.concatenate([np.linspace(-60, -2.25, 400), [-2.25]]):
    for k in range(-25, 26):
        l1, l2, _, _ = lams(c5, k, P)
        mn = min(mn, np.abs(l1).min(), np.abs(l2).min())
log(f'(a) integer |k| <= 25, -60 <= c5 <= -9/4, |p| <= 40: min |lambda| = {mn:.6f}  (bound 1/4)')
assert mn >= 0.25 - 1e-9
for c5 in (-2.2, -2.1, -2.01):
    m = min(min(np.abs(lams(c5, k, P)[0]).min(), np.abs(lams(c5, k, P)[1]).min()) for k in range(-10, 11))
    log(f'    c5 = {c5}: min |lambda| = {m:.6f}  (|c5 + 2| = {abs(c5 + 2):.6f})')

# (b)
k0 = 1
def f_abs(p, c5, eps):
    l1 = lams(c5, k0, p)[0]
    m = abs(l1 - 1j * eps)
    if m == 0.0:          # the single point (0, 0) has measure zero; avoid evaluating log 0 there
        return 0.0
    return abs(np.log(m)) * (k0 * k0 + p * p)
log('(b) zero of lambda1 at (c5, k, p) = (0, 1, 0); box |c5| <= 1, |p| <= 1, uniform density in c5:')
vals = []
for eps in (1e-1, 1e-2, 1e-3, 1e-4, 0.0):
    I, err = integrate.dblquad(f_abs, -1, 1, -1, 1, args=(eps,), epsabs=1e-9, epsrel=1e-9)
    vals.append(I)
    log(f'    eps = {eps:g}: I = {I:.8f} (quadrature error estimate {err:.1e})')
assert abs(vals[-1] - vals[-2]) < 1e-3
log('    atom in c5 at the zero value (c5 = 0):')
for eps in (1e-2, 1e-4, 0.0):
    I, err = integrate.quad(lambda p: f_abs(p, 0.0, eps), -1, 1, points=[0.0, -eps], limit=400)
    log(f'    eps = {eps:g}: int |log|lambda1 - i eps|| (1 + p^2) dp = {I:.8f}')

# (c) relative logarithm, both chiralities (conjugate z), principal branch, Feynman -i eps everywhere
def relF(p, c5, eps, part):
    tot = 0.0
    for sgn in (+1, -1):
        z = k0 + 1j * sgn * p
        C4 = k0 * k0 - p * p - 1
        A = c5 - C4
        w1, w2 = (z + 1) / z, (z - 1) / z
        l1, l2 = A + 1 - z, A + 1 + z
        val = (w1 * np.log(l1 - 1j * eps) + w2 * np.log(l2 - 1j * eps) - 2 * np.log(A - 1j * eps))
        tot += val
    v = tot.real if part == 're' else tot.imag
    return v * (k0 * k0 + p * p)
log('(c) relative log summed over chiralities on the same box (reference zeros on c5 = -p^2):')
prev = None
for eps in (1e-2, 1e-3, 1e-4, 1e-5):
    Ir, er = integrate.dblquad(relF, -1, 1, -1, 1, args=(eps, 're'), epsabs=1e-8, epsrel=1e-8)
    Ii, ei = integrate.dblquad(relF, -1, 1, -1, 1, args=(eps, 'im'), epsabs=1e-8, epsrel=1e-8)
    log(f'    eps = {eps:g}: Re = {Ir:.6f}, Im = {Ii:.6f}')
    prev = (Ir, Ii)
ref_phase = 4 * np.pi * integrate.quad(lambda p: (1 - p**2) * (1 + p * p), -1, 1)[0]   # A = c5 + p^2 < 0 region, weight 1+p^2
log(f'    reference phase 4 pi * int_(A<0) (k^2+p^2) = {ref_phase:.6f}: the imaginary part is the phase of the Feynman reference;')
log('    the fermionic imaginary parts of the two chiralities cancel (conjugate labels, principal branch)')
assert abs(prev[1] - ref_phase) < 1e-3

# (d) large p at fixed (c5, k)
for (c5, k) in ((-3.0, 0), (0.5, 2), (10.0, 3)):
    row = []
    for p in (10., 100., 1000., 10000.):
        l1, l2, A, z = lams(c5, k, p)
        w1, w2 = (z + 1) / z, (z - 1) / z
        Fp = w1 * np.log(l1 / A) + w2 * np.log(l2 / A)
        row.append((k * k + p * p) * 2 * Fp.real)
    log(f'(d) c5 = {c5}, k = {k}: (k^2+p^2) * 2 Re F at p = 1e1..1e4: ' + ', '.join(f'{r:.6f}' for r in row))
    assert abs(row[-1] - 2) < 1e-3

# (e) branch dependence of the modulus
pp = -0.3; kk = 1; c5 = -3.0
l1, l2, A, z = lams(c5, kk, pp)
w1 = (z + 1) / z
delta = (w1 * 2j * np.pi + np.conj(w1) * (-2j * np.pi)).real
log(f'(e) at (c5, k, p) = ({c5}, {kk}, {pp}): Re lambda1 = {l1.real:.3f} < 0; change of 2 Re F under the branch shift = {delta:.6f}; 4 pi p/|z|^2 = {4 * np.pi * pp / abs(z)**2:.6f}')
assert abs(delta - 4 * np.pi * pp / abs(z)**2) < 1e-12
log('All checks passed.')
open(__file__.replace('.py', '.out.txt'), 'w').write('\n'.join(out) + '\n')
