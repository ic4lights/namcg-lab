"""s11: analytic a_1 of the covariant Maxwell-dilaton operator (b = 0): a_1 = -R/3 + box ln rho - V^2   (Hodge on 1-forms, rho-weighted Lorenz gauge)
versus the numerical a_1 of the operator built from H = 2*Maxwell_G only, at generic Poisson-class jets (no J=0 condition: the operator is covariant for any G, rho)."""
import sys, io, contextlib
import numpy as np
sys.path.insert(0, '.')
with contextlib.redirect_stdout(io.StringIO()):
    import s3_operator_identity as s3
    import s6b_covariant_a1_fit as m6
from geom import *

def a1_Mx(bg, with_axion):
    H, bjet = s3.H_jets(bg)
    if not with_axion:
        for I, (a, b) in enumerate(s3.pairs):
            for Jx, (c_, d) in enumerate(s3.pairs):
                if len({a, b, c_, d}) == 4:
                    pass
        # rebuild without axion: subtract axion part
        K, rho = bg['K'], bg['rho']
        H = np.zeros_like(H)
        for I, (a, b) in enumerate(s3.pairs):
            for Jx, (c_, d) in enumerate(s3.pairs):
                H[I, Jx] = 4*J.mul(rho, J.mul(K[a, c_], K[b, d]) - J.mul(K[a, d], K[b, c_]))
    G, rhoi = bg['G'], bg['rhoi']
    def op(A):
        P = s3.P_apply(bg, H, 4.0, A); out = np.zeros_like(P)
        for lam in range(D):
            for nu in range(D):
                out[lam] += J.mul(J.mul(G[lam, nu], rhoi), P[nu])/4.0
        return out
    a, b = apply_to_jets(op, 4)
    return gilkey_a1(a, b, bg['G'], 4)[0]

for etad in [(1, 1, 1, 1), (-1, 1, 1, 1)]:
    for seed in (1, 2, 3):
        bg = s3.setup(seed, etad)
        inv = m6.invariants(bg)
        pred = -inv["R"]/3 + inv["box"] - inv["V2"]
        print(f'eta={etad} seed={seed}: a1(Maxwell-dilaton only) = {a1_Mx(bg, False):+.8f}   -R/3+box-V2 = {pred:+.8f}   [R={inv["R"]:+.4f} V2={inv["V2"]:+.4f} box={inv["box"]:+.4f}]', flush=True)
