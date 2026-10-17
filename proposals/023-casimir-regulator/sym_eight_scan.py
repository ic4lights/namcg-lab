"""023 script 8: scan of the contraction weight lambda for the eight-matrix set {T^a, y^a}: K = K_T + lam*K_y (K_T = sum eta_a v_{a4}^2, K_y = sum eta_a v_{a5}^2, eta=diag(-1,1,1,1))."""
import numpy as np
from symbol_tools import *
from sym_signatures import sig
rng = np.random.default_rng(8)
eta4 = [-1, 1, 1, 1]
lams = [-100, -10, -3, -1, -0.3, -0.1, -0.01, 0.01, 0.1, 1, 10]
tab = {l: {} for l in lams}; sy = {}
for t in range(30):
    z = rand_z_pos(rng, rng.uniform(0.5, 4)); M0 = Mfun(z)
    V = {p: vec(M0, *p) for p in pairs}
    allT = np.array([V[p] for p in pairs]); u, sv, vh = np.linalg.svd(allT); E = vh[:6]
    c = {p: E @ V[p] for p in pairs}
    Kt = sum(eta4[a] * np.outer(c[(a, 4)], c[(a, 4)]) for a in range(4)); Ky = sum(eta4[a] * np.outer(c[(a, 5)], c[(a, 5)]) for a in range(4))
    s0 = sig(Ky); sy[s0] = sy.get(s0, 0) + 1
    for l in lams:
        s_ = sig(Kt + l * Ky); tab[l][s_] = tab[l].get(s_, 0) + 1
print("signature of K_y alone:", sy)
for l in lams: print("lam = %7.2f :" % l, tab[l])
