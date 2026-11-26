import numpy as np, sympy as sp
import an_su2_general as A
from an_su2_general import *
# off-shell: random h' and h'' (J != 0)
import random
random.seed(2)
def data_off(c):
    cc = [[Wrap.convert(sp.Rational(v)) for v in row] for row in c]
    w = SG.build_omega(Wrap, cc)
    geom.SIGN_OVERRIDE = None
    Th = theta_from_omega(w)
    Ginv, G, rho = geom.metric_data(Th)
    f = lambda v: float(getattr(v, 'x', v))
    G0 = np.array([[f(G[i][j].c0()) for j in range(4)] for i in range(4)]); Gi0 = np.linalg.inv(G0)
    B = np.zeros((4, 4, 4))
    for t in range(4):
        for m in range(4):
            for n in range(4):
                B[t, m, n] = f(sum((Th[r][t]*Th[m][n].diff(r) for r in range(4)), Jet()).c0())
    b = np.einsum('st,tmn->smn', G0, B)
    l = np.array([[0.25*np.sum(eta[k]*b[s_]) for k in range(3)] for s_ in range(4)])
    r = np.array([[0.25*np.sum(etab[k]*b[s_]) for k in range(3)] for s_ in range(4)])
    J = [f(sum((Th[m][r_]*Th[m][n].diff(r_) for m in range(4) for r_ in range(4)), Jet()).c0()) for n in range(4)]
    return np.linalg.norm(J), np.sum(l*l), np.sum(r*r)
for t in range(4):
    c = [[random.randint(1, 4), random.randint(-3, 3), random.randint(-3, 3), 0] for _ in range(3)]
    print('off-shell SU(2)-inv  |J| = %.3g  |l|^2 = %.3g  |r|^2 = %.3g' % data_off(c))
