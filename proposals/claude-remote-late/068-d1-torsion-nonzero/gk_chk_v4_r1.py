import sys, numpy as np
sys.path.insert(0, r'C:\Users\redgi\Projects\namcg-lab\proposals\068-d1-torsion-nonzero')
from core import M_of_q, null_rotation_g2
from tools import char_roots, grouped
q0 = np.array([0.31, 0.42, -0.45, -0.72]); n = np.array([2.5, -0.57, -0.22, -0.23])
for kap in (-0.5,):
    c, w = null_rotation_g2(kap)
    roots = char_roots(lambda t: M_of_q(c, w, q0 + t * n), 30)
    out=[]
    for (re, im), cnt in grouped(roots):
        q = q0 + (re + 1j*im)*n
        qq = -q[0]**2+q[1]**2+q[2]**2+q[3]**2; kq = -q[0]+q[3]
        x = (-qq/(2*kq)).real/kap
        out.append((round(x,5), cnt, round(abs(im),8)))
    print(kap, len(roots), out)
