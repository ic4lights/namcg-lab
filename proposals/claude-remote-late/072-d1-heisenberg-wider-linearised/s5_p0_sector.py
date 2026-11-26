"""S5 (numerical).  The sector p = 0 of the wider Heisenberg family: there E_2 acts as zero, E_1 and E_3
commute, and the modes are characters q = (q0, q1, 0, q3) (core068.M_of_q; q_c c_ab^c = 0 holds since
q_2 = 0).  Along lines q = (t, q1, 0, q3) every characteristic root of the forty equations and of Q is
fitted to (q - alpha k)^2 = 0, i.e. alpha = q^2 / (2 k^a q_a), k^a = (-1, 0, 1, 0), and compared with
alpha = -i c chi / 2, c in {-1, 1, 3} (the p -> 0 limit of the Landau-sector relation with l-term absent).
Run: python -I -B s5_p0_sector.py"""
import os, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
import numpy as np

KUP = np.array([-1.0, 0, 1.0, 0])


def qsq(q):
    return -q[0] ** 2 + q[1] ** 2 + q[2] ** 2 + q[3] ** 2


for par in [(1.0, 0.5, 0.0, 0.0), (1.0, 0.5, 0.7, -0.2), (1.3, -0.8, 0.3, 0.5)]:
    C, W = wider(*par); chi = par[1]
    for kv in ([0.6, 0, -0.9], [1.3, 0, 0.4]):
        for name, op in [('forty', lambda t: K.M_of_q(C, W, [t, kv[0], 0.0, kv[2]])),
                         ('Q', lambda t: lin.Qop(C, W, K.chars([t, kv[0], 0.0, kv[2]])))]:
            r = K.rank(op(0.37 + 0.1j)); rt = Tl.char_roots(op, r)
            al = []
            for t in rt:
                qv = np.array([t, kv[0], 0.0, kv[2]], dtype=complex)
                kq = KUP @ qv
                if abs(kq) > 1e-6:
                    al.append(qsq(qv) / (2 * kq) / (-0.5j * chi))
            g = Tl.grouped(np.array(al), 4, 1e-3)
            print('%s q=(t,%s) %-5s rank %d roots %d; alpha / (-i chi/2):' % (par, kv, name, r, len(rt)),
                  ', '.join('%.4f%+.4fi x%d' % (z[0], z[1], c) for z, c in g))
