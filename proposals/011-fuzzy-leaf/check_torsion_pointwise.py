"""
Pointwise (not only 'mod total derivative at zero total momentum') test of
    rho^2 X + 2 h + r - (3/2) rho^2 I_S = c * d_mu( g_rho^{mu nu} d_nu rho )
in the exact perturbative Poisson class of check_torsion_decomposition.py, using generic momenta p_j (sum p_j != 0) so that
every mask coefficient of a total derivative is nonzero.  Prints the ratio Res/TD for every nonempty mask, with
Res = rho^2 X + 2 h + r - (3/2) rho^2 I_S, TD = d_a(g_rho^{ab} d_b rho).  A pointwise identity requires one constant c.
(h = rho R[g_rho], r = rho |grad ln rho|^2_{g_rho}, I_S as in check_torsion_decomposition.py.)
"""
import numpy as np
import check_torsion_decomposition as C

rng = np.random.default_rng(2024)
ratios = {}
for s in range(12):
    sig = rng.choice([1.0, -1.0]); ab = rng.uniform(0.5, 2.5, 2)
    ps = [rng.integers(-3, 4, 4).astype(float) for _ in range(3)]
    us = [rng.normal(size=4) for _ in range(3)]
    masks = list(range(1, 8))
    o = C.build(sig, ab, ps, us, masks)
    for mk in masks:
        res = o['x'][mk] + 2*o['h'][mk] + o['r'][mk] - 1.5*o['S'][mk]
        td = o['td'][mk]
        scale = abs(o['x'][mk]) + abs(o['h'][mk]) + abs(o['S'][mk]) + 1e-300
        ratios.setdefault(mk, []).append((res, td, scale))
for mk in sorted(ratios):
    rows = ratios[mk]
    cs = [r[0]/r[1] for r in rows if abs(r[1]) > 1e-8*r[2]]
    nres = max(abs(r[0])/r[2] for r in rows)
    if cs:
        cs = np.array(cs)
        print('mask %d: n=%d  c = Res/TD : mean %s  spread %.2e   max|Res|/scale %.2e' % (mk, len(cs), np.round(cs.mean(), 8), np.abs(cs - cs.mean()).max(), nres))
    else:
        print('mask %d: TD ~ 0 for all samples; max|Res|/scale = %.2e' % (mk, nres))
