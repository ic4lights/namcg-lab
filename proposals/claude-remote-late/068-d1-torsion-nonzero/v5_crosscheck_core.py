"""V5. Cross-check of the independent symbolic linearisation of v1 against core.py (numerical, characters).
For a character q (q_c c_ab^c = 0) and random constant amplitudes (h0, w0), v1's brackets applied to
(h0, w0) e^{i q.y}, divided by e^{i q.y}, must equal core.M_of_q(q) applied to the packed amplitudes.
Run: python -I v5_crosscheck_core.py
"""
import itertools
import os
import sys
import numpy as np
import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v1_reduction_symbolic as v1                      # noqa: E402
import core                                             # noqa: E402

rng = np.random.default_rng(7)
cases = [('flat', core.flat(), [0.3, -0.7, 0.4, 0.9]), ('Heisenberg', core.heisenberg(1.0), [0.3, -0.7, 0.0, 0.9])]
for name, (cn, wn), q in cases:
    E, _ = v1.BGS[name]
    E = [[sp.sympify(x).subs(v1.kap, 1) for x in V] for V in E]
    c = v1.struct(E)
    vec = rng.normal(size=core.NF)
    hn, wv = core.unpack(vec, 1)
    phase = sp.exp(sp.I * sum(sp.nsimplify(q[m]) * v1.Y[m] for m in range(4)))
    h = [[sp.nsimplify(float(hn[b, d, 0].real), rational=False) * phase for d in range(4)] for b in range(4)]
    w = [[[float(wv[b, x, d, 0].real) * phase for d in range(4)] for x in range(4)] for b in range(4)]
    B1, B2 = v1.brackets_lin(E, c, v1.ETA, h, w)
    sym = np.zeros(core.NF, dtype=complex)
    sym[:16] = [complex(sp.N(sp.simplify(B1[b][e] / phase))) for b in range(4) for e in range(4)]
    for b in range(4):
        for k, (d, e) in enumerate(core.PAIRS):
            sym[16 + 6 * b + k] = complex(sp.N(sp.simplify(B2[b][d][e] / phase)))
    num = core.M_of_q(cn, wn, np.array(q)) @ vec
    print('%s: max |v1 - core| = %.1e (max |core| = %.2f)' % (name, np.abs(sym - num).max(), np.abs(num).max()))
