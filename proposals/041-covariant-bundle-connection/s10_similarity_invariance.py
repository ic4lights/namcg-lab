"""s10: Lemma S, numerically.  The diagonal heat-kernel density tr K_s(x,x) (hence a_1 = tr(E + R/6) pointwise) is unchanged by a local similarity of the
fluctuation bundle.  Test: O_v in the a variables versus S O_v S^{-1} in the Moser variables A = a.omega (a local invertible matrix function), at generic Poisson-class jets (J != 0)."""
import sys, io, contextlib
import numpy as np
sys.path.insert(0, '.')
with contextlib.redirect_stdout(io.StringIO()):
    import s3_operator_identity as s3
from geom import *
for etad in [(1, 1, 1, 1), (-1, 1, 1, 1)]:
    for seed in (1, 2):
        bg = s3.setup(seed, etad)
        a4, b4 = apply_to_jets(lambda A: s3.Ov_apply(bg, A), 4)
        v1, e1 = gilkey_a1(a4, b4, bg['G'], 4)
        aS, bS = apply_to_jets(lambda A: s3.S_apply(bg, s3.Ov_apply(bg, s3.Sinv_apply(bg, A))), 4)
        v2, e2 = gilkey_a1(aS, bS, bg['G'], 4)
        print(f'eta={etad} seed={seed}: a1(O_v) = {v1:+.10f},  a1(S O_v S^-1) = {v2:+.10f}, diff {abs(v1-v2):.1e}')
