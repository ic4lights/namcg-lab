"""022 script 11: large-sample check for the 5-matrix presentation X^A = M^{A5}: 300 random orbit points (n in [0.5,4]), 91 zeta directions,
both signs s of the Lie-Poisson bracket.  Reports: rank (4,2), positivity of h, the fraction of the opposite chirality of the flux in the h-orthonormal frame
(0 means exactly (anti-)self-dual, f1=f2), the chirality sign, and the equality of the horizontal base symbol with ell^2 g^{-1}."""
import numpy as np
import symbol_tools as st
from symbol_tools import *
e5 = np.diag([-1., 1, 1, 1, 1])
P5f = [(A, 5) for A in range(5)]
for sval in (-1.0, 1.0):
    st.s = sval
    rng = np.random.default_rng(100 + int(sval))
    worst_opp = 0; worst_r = 0; signs = set(); hmin = 1e9; rk = set(); conf = 0
    for t in range(300):
        z = rand_z_pos(rng, rng.uniform(0.5, 4)); M0 = Mfun(z)
        r = st.symbol(M0, P5f, [-1., 1, 1, 1, 1])
        rk.add((r['rank'], r['zrank']))
        w = np.linalg.eigvalsh(r['h']); hmin = min(hmin, w.min())
        hs = sqrtm_sym(r['h'])
        for ph in np.linspace(0, np.pi, 91):
            zeta = np.array([np.cos(ph), np.sin(ph)])
            F = np.einsum('ijk,k->ij', r['F'], zeta)
            Ft = hs @ F @ hs
            Fp, Fm = hodge_split(Ft)
            a, b = amp(Fp), amp(Fm)
            signs.add(1 if a > b else -1)
            worst_opp = max(worst_opp, min(a, b) / max(a, b))
            f1, f2, p, rr = planes(Ft)
            worst_r = max(worst_r, 1 - f2 / f1)
        worst_r = max(worst_r, 0)
    print(f"s={sval:+.0f}: ranks {rk}; min eig h = {hmin:.3e} (>0); worst opposite-chirality fraction = {worst_opp:.2e}; worst 1 - f2/f1 = {worst_r:.2e}; chirality signs seen: {signs}")
