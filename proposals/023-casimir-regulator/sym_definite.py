"""023 script 2: (a) base/vertical decomposition of the C42 symbol; (b) existence of a definite combination of Casimir-type symbols,
restricted to operator families that commute with H_V: {C42, C41} (both commute with all J^{AB}, A,B<=4, hence with H_V),
and larger families that do not commute."""
import numpy as np
from scipy.optimize import minimize
from symbol_tools import *
from sym_signatures import forms, sig
rng = np.random.default_rng(11)
def best_lmin(F, names, tries=8):
    def f(c):
        c = c / np.linalg.norm(c)
        return -np.linalg.eigvalsh(sum(ci * F[n] for ci, n in zip(c, names)))[0]
    r = min((minimize(f, rng.normal(size=len(names)), method='Nelder-Mead', options={'xatol': 1e-12, 'fatol': 1e-14, 'maxiter': 6000}) for _ in range(tries)), key=lambda r: r.fun)
    c = r.x / np.linalg.norm(r.x)
    return -r.fun, c
fam = {'C42,C41': ['C42', 'C41'], 'C42,C41,C31': ['C42', 'C41', 'C31'], 'C42,C41,Box4(Lorentz)': ['C42', 'C41', 'Box4'],
       'C42,C41,Box4E': ['C42', 'C41', 'Box4E'], 'C42,C41,C31,Box4E': ['C42', 'C41', 'C31', 'Box4E']}
res = {k: [] for k in fam}
split = []
for t in range(25):
    z = rand_z_pos(rng, rng.uniform(0.5, 4)); M0 = Mfun(z)
    rk, F = forms(M0)
    for k, names in fam.items():
        v, c = best_lmin(F, names); res[k].append(v)
    # base/vertical: base covectors = d y^C (C=0..4 span 4-dim cotangent subspace of the 6); vertical vectors = kernel of dy.
    V = {p: vec(M0, *p) for p in pairs}
    T = np.array([V[p] for p in pairs]); u, sv, vh = np.linalg.svd(T); E = vh[:6]
    # coordinates of d y^C (functional M^{C5}) on tangent space: row of E in the pair-index (C,5)
    dy = np.array([E[:, pidx[(C, 5)]] for C in range(5)])      # (5,6) covectors in tangent coords
    ub, sb, vb = np.linalg.svd(dy); base = vb[:4]             # 4-dim span of base covectors
    vert = vb[4:]                                             # orthogonal complement (vertical-ish covectors, 2 dim)
    Kc = F['C42']
    split.append((sig(base @ Kc @ base.T), sig(vert @ Kc @ vert.T)))
print("C42 symbol: (signature on span of base covectors dy^C, signature on the euclidean-orthogonal 2-plane):", set(split))
for k, v in res.items():
    print("%-24s max_c lambda_min(sum c K) over 25 points: min %.4g, max %.4g  -> definite combination exists at all points: %s" % (k, min(v), max(v), min(v) > 1e-9))
