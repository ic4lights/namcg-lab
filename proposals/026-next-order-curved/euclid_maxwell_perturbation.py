"""First-order J = 0 backgrounds about a constant Theta_bar (Euclidean section).
Theta = (psi^* omega_bar)^{-1}, psi = x + eps a(x) exactly Poisson;  Theta1^{mn} = -(Theta_bar^{m r} d_r a^n - Theta_bar^{n r} d_r a^m).
J^{(1)n} = D^m D^m a^n - D^n D^m a^m,  D^m = Theta_bar^{m r} d_r  (Maxwell equation in the flat coordinates y with d/dy^m = D^m).
For quadratic a^n = (1/2) H^n_{rs} x^r x^s:  J1^n = K^{rs} H^n_{rs} - Theta_bar^{n r} Theta_bar^{m s} H^m_{rs}.
Step 1: validate J1 and b^{(1)} against exact jets of the Poisson bivector at small eps.
Step 2: solve J1 = 0 (nullspace), compute b^{(1)}_s = G_{st} Theta_bar^{r t} d_r Theta1^{mn} and S = 8 tr a tr b + 16 tr(c c^T) (>=0)."""
import numpy as np, sympy as sp, itertools
import jetlib as jl
from jetlib import Jet
from common import *
import lib
rng = np.random.default_rng(11)
eta = [np.array(e.tolist(), float) for e in lib.eta3()]
etab = [np.array(e.tolist(), float) for e in lib.etabar()]
Tb = np.array([[0, 1.0, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 2.0], [0, 0, -2.0, 0]])
Tb = Tb + 0.3*np.array([[0, 0, 1.0, 0], [0, 0, 0, -0.5], [-1.0, 0, 0, 0], [0, 0.5, 0, 0]])
K = Tb.T@Tb; G = np.linalg.inv(K); Gi = K
pairs = [(r, s) for r in range(4) for s in range(r, 4)]
def Hfull(h):
    H = np.zeros((4, 4, 4))
    for n in range(4):
        for k, (r, s) in enumerate(pairs):
            H[n, r, s] = H[n, s, r] = h[n*10 + k]
    return H
def J1_of_H(H):
    return np.array([np.einsum('rs,rs->', K, H[n]) - np.einsum('r,s,ms...->', Tb[n], Tb[n]*0, H) if False else
                     np.einsum('rs,rs->', K, H[n]) - sum(Tb[n, r]*Tb[m, s]*H[m, r, s] for r in range(4) for m in range(4) for s in range(4)) for n in range(4)])
def dTheta1(H):
    # d_k Theta1^{mn} = -(Tb^{m r} H^n_{rk} - Tb^{n r} H^m_{rk})
    d = np.zeros((4, 4, 4))
    for k in range(4):
        for m in range(4):
            for n in range(4):
                d[k, m, n] = -sum(Tb[m, r]*H[n, r, k] - Tb[n, r]*H[m, r, k] for r in range(4))
    return d
def b1_from_H(H):
    B = np.einsum('rt,rmn->tmn', Tb, dTheta1(H))
    return np.einsum('st,tmn->smn', G, B)
def S_of(b):
    l = np.array([[0.25*np.sum(eta[k]*b[s_]) for k in range(3)] for s_ in range(4)])
    r = np.array([[0.25*np.sum(etab[k]*b[s_]) for k in range(3)] for s_ in range(4)])
    a_ = l.T@Gi@l; b_ = r.T@Gi@r; c_ = l.T@Gi@r
    return 8*np.trace(a_)*np.trace(b_) + 16*np.trace(c_@c_.T), np.trace(a_), np.trace(b_)

# ---- Step 1: validate against exact jets (rational Theta_bar, small eps)
use_gaussian(3)
Tq = [[sp.Rational(str(round(Tb[i, j], 6))).limit_denominator(1000) for j in range(4)] for i in range(4)]
Tqm = sp.Matrix(Tq)
Tb_r = np.array(Tqm.tolist(), float)
Kq = (Tqm.T*Tqm)
def run_jets(Hn, eps):
    y = [Jet.var(i) for i in range(4)]
    psi = []
    for m in range(4):
        t = Jet.const(QQ_I(0)) + y[m]
        a = Jet()
        for (r, s), in zip(pairs):
            pass
        quad = Jet()
        for r in range(4):
            for s in range(4):
                c = sp.Rational(Hn[m, r, s]).limit_denominator(1000)
                if c != 0:
                    quad = quad + y[r]*y[s]*QQ_I.from_sympy(c/2)
        psi.append(y[m] + quad*QQ_I.from_sympy(eps))
    wbar = Tqm.inv()
    om = [[Jet() for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for s in range(4):
            t = Jet()
            for m in range(4):
                for n in range(4):
                    if wbar[m, n] != 0:
                        t = t + psi[m].diff(r)*psi[n].diff(s)*QQ_I.from_sympy(wbar[m, n])
            om[r][s] = t
    Th = jl.minv(om)
    J = [sum((Th[m][r].diff(0)*0 + Th[m][r]*Th[m][n].diff(r) for m in range(4) for r in range(4)), Jet()).c0() for n in range(4)]
    B = [[[sum((Th[r][t]*Th[m][n].diff(r) for r in range(4)), Jet()).c0() for n in range(4)] for m in range(4)] for t in range(4)]
    return [float(getattr(j, 'x', j)) for j in J], np.array([[[float(getattr(B[t][m][n], 'x', B[t][m][n])) for n in range(4)] for m in range(4)] for t in range(4)])
# redo with rational Tb consistently
Tb = Tb_r; K = Tb.T@Tb; G = np.linalg.inv(K); Gi = K
Hn = Hfull(rng.integers(-3, 4, size=40).astype(float))
eps = sp.Rational(1, 10**6)
J_j, B_j = run_jets(Hn, eps)
J1 = J1_of_H(Hn)
print('Step 1  J(0)/eps (jets):', np.array(J_j)/1e-6)
print('        J1 (formula)     :', J1)
Bf = np.einsum('rt,rmn->tmn', Tb, dTheta1(Hn))
print('        max |B_jets/eps - B^(1)| =', np.abs(B_j/1e-6 - Bf).max(), '  (O(eps) corrections expected)')

# ---- Step 2
Mlin = np.zeros((4, 40))
for j in range(40):
    e = np.zeros(40); e[j] = 1
    Mlin[:, j] = J1_of_H(Hfull(e))
u_, s_, vt = np.linalg.svd(Mlin)
rank = int((s_ > 1e-10).sum())
null = vt[rank:].T
print('Step 2  rank of J1 map on quadratic a: %d ; nullspace dimension %d (of 40)' % (rank, null.shape[1]))
for t in range(5):
    h = null@rng.normal(size=null.shape[1])
    H = Hfull(h)
    S, ta, tb = S_of(b1_from_H(H))
    print('   |J1| = %.2e   tr a = %.4f  tr b = %.4f   S = %.4f' % (np.abs(J1_of_H(H)).max(), ta, tb, S))
