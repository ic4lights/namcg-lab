"""023 script 3: contraction forms of the extended matrix sets on the leaf (cf. 022 'eight-matrix -eta set'): signature of the horizontal quadratic form
K = sum_I e_I v_I v_I^T for  {T^a} (rank 4), {T^a, y^a} with y-block contracted by +eta or -eta (eight matrices), and ratios of C42/C41 symbol components."""
import numpy as np
from symbol_tools import *
from sym_signatures import forms, sig
rng = np.random.default_rng(3)
eta4 = [-1, 1, 1, 1]
out = {}
rat = []
for t in range(40):
    z = rand_z_pos(rng, rng.uniform(0.5, 4)); M0 = Mfun(z)
    V = {p: vec(M0, *p) for p in pairs}
    T = np.array([V[p] for p in pairs]); u, sv, vh = np.linalg.svd(T); E = vh[:6]
    c = {p: E @ V[p] for p in pairs}
    Kt = sum(eta4[a] * np.outer(c[(a, 4)], c[(a, 4)]) for a in range(4))
    Ky = sum(eta4[a] * np.outer(c[(a, 5)], c[(a, 5)]) for a in range(4))
    for name, Kf in [('T only (eta)', Kt), ('T eta + y eta', Kt + Ky), ('T eta + y (-eta)', Kt - Ky), ('T delta + y delta', sum(np.outer(c[(a, 4)], c[(a, 4)]) + np.outer(c[(a, 5)], c[(a, 5)]) for a in range(4)))]:
        s_ = sig(Kf); out.setdefault(name, {}); out[name][s_] = out[name].get(s_, 0) + 1
print("signature (n+, n-, n0) of the contraction form on the 6-dim tangent space at 40 random points:")
for k, v in out.items(): print("  %-22s" % k, v)
