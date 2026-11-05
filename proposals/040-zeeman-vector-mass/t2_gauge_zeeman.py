"""040 t2: gauge invariance alpha -> alpha + lam*kappa of the full order-eps^2 response (finite kappa, all orders) with the Zeeman-dressed species.
Vector alone (chi, t1, D) and vector+Dirac+scalars (massless supertrace combination).  The delta (Zeeman) terms must be invariant by themselves together with V:
only the correct relative sign/normalisation of the Zeeman insertion passes.  Also reports the failure when the sign of N is flipped."""
import sys, numpy as np, mpmath as mp
sys.dont_write_bytecode = True
from engine_z import *
mp.mp.dps = 30
rng = np.random.default_rng(5)
kappa = rng.normal(size=4)
y = rng.normal(size=4); y = y - kappa * (y @ kappa) / (kappa @ kappa)
alpha = rng.normal(size=4); c0 = 0.8; lam = 0.37
def full(a, b, al, s, which, signN=1, nquad=8):
    ka = np.array([mp.mpf(x) for x in kappa], dtype=object); alm = np.array([mp.mpf(x) for x in al], dtype=object)
    yy = np.array([mp.mpf(x) for x in y], dtype=object)
    TC, nodes = orbital_nodes(a, b, ka, alm, yy, mp.mpf(c0), s, nquad)
    sp = []
    if which in ('vec', 'str'):
        v = vector_species(a, b, ka, alm, w=1)
        v.N = v.N * signN
        sp.append(v)
    if which == 'str':
        d = dirac_species(a, b, ka, alm)
        d.N = d.N * signN
        sp.append(d)
        sp.append(Species('scal', mp.mpf(4), None, None))   # n_ex - 2 = 4 scalar-type components (6 scalars + ghost -2)
    if which == 'scal':
        sp.append(scalar_species())
    return T2_total(sp, TC, nodes, s)
for (a, b) in ((mp.mpf('0.7'), mp.mpf('1.3')), (mp.mpf('1.9'), mp.mpf('1.0'))):
    for s in (mp.mpf('0.4'), mp.mpf('0.9') * mp.expj(-0.3)):
        for which in ('scal', 'vec', 'str'):
            for signN in ((1,) if which == 'scal' else (1, -1)):
                t0 = full(a, b, alpha, s, which, signN); t1 = full(a, b, alpha + lam * kappa, s, which, signN)
                print('(a,b)=(%s,%s) s=%s %-4s signN=%+d  T2=%s  rel.change under alpha->alpha+lam kappa: %s' % (mp.nstr(a, 3), mp.nstr(b, 3), mp.nstr(s, 4), which, signN, mp.nstr(t0, 8), mp.nstr(abs(t1 - t0) / abs(t0), 3)))
