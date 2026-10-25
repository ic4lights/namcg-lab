"""s11b: axion contribution to a_1 of the covariant operator at generic Poisson-class jets (no J=0 condition):
   a1(Maxwell-dilaton + axion) - a1(Maxwell-dilaton) versus  s*6*|d theta~ - theta~ V|^2_G  (s = +1 Euclid, -1 Lorentz; analytic estimate)"""
import sys, io, contextlib
import numpy as np
sys.path.insert(0, '.')
with contextlib.redirect_stdout(io.StringIO()):
    import s3_operator_identity as s3
    import s6b_covariant_a1_fit as m6
    import s11_hodge_check as m11
from geom import *
for etad in [(1, 1, 1, 1), (-1, 1, 1, 1)]:
    for seed in (1, 2, 3):
        bg = s3.setup(seed, etad)
        inv = m6.invariants(bg)
        full = m6.a1_M(bg); md = m11.a1_Mx(bg, False)
        U2 = inv['th2'] - 2*inv['vth'] + inv['t2V2']
        print(f'eta={etad} seed={seed}: a1(M) = {full:+.6f}; a1(MD) = {md:+.6f}; axion part = {full-md:+.6f};  6|U|^2 = {6*U2:+.6f}   ratio {(full-md)/(6*U2):+.4f}', flush=True)
