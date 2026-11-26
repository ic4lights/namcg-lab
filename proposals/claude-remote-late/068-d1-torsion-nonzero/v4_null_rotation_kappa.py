"""V4. Null-rotation background in the gauge with constant frame and omega_a^{12} = kappa k_a, k_a = (1,0,0,1):
characteristic roots of the forty equations along the line of s2 lie on (q + j kappa k)^2 = 0 with
j = 0, +-1, +-2 and multiplicities 4, 6, 2 per crossing, for kappa = 1/2, 1, 2; all roots real.
Run: python -I v4_null_rotation_kappa.py
"""
import os
import sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core import M_of_q, null_rotation_g2   # noqa: E402
from tools import char_roots, grouped       # noqa: E402

q0 = np.array([0.31, 0.42, -0.45, -0.72])
n = np.array([2.5, -0.57, -0.22, -0.23])
for kap in (0.5, 1.0, 2.0):
    c, w = null_rotation_g2(kap)
    roots = char_roots(lambda t: M_of_q(c, w, q0 + t * n), 30)
    rows = []
    for (re, im), cnt in grouped(roots):
        q = q0 + (re + 1j * im) * n
        qq = -q[0] ** 2 + q[1] ** 2 + q[2] ** 2 + q[3] ** 2
        kq = -q[0] + q[3]
        rows.append((int(round((-qq / (2 * kq)).real / kap)), cnt, abs(im) < 1e-6))
    mult = {}
    for j, cnt, real in rows:
        mult.setdefault(j, []).append(cnt)
    print('kappa = %.1f: total roots %d; all real: %s; j -> multiplicities per crossing %s'
          % (kap, len(roots), all(r[2] for r in rows), dict(sorted(mult.items()))))
