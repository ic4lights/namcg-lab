import random, sympy as sp
import jetlib as jl
from jetlib import Jet
from common import *
import geom

use_gaussian(3)
random.seed(7)
def rq(): return Q(random.randint(-6, 6), random.randint(1, 5))
y = [Jet.var(i) for i in range(4)]
# random polynomial A of degree <=4 in y, plus constant omega
def rpoly(deg):
    t = Jet()
    for mon in itertools.product(range(deg+1), repeat=4):
        if 1 <= sum(mon) <= deg:
            m = Jet.const(rq())
            for i, e in enumerate(mon):
                for _ in range(e): m = m * y[i]
            t = t + m
    return t
A = [rpoly(4) for _ in range(4)]
w = omega_from_A(A)
c = [[0,2,0,1],[-2,0,3,0],[0,-3,0,1],[-1,0,-1,0]]
w = [[w[m][n] + Jet.const(Q(c[m][n])) for n in range(4)] for m in range(4)]
Th = theta_from_omega(w)
# check w Th = 1 (to order 3)
P = jl.mm(w, Th)
print('w.Theta - 1 residual:', all((P[i][j] - (Jet.const(jl.ONE) if i==j else Jet())).d == {} for i in range(4) for j in range(4)))
# Jacobi residual valid to degree 2
def jacobi(Th):
    worst = 0
    for m in range(4):
        for n in range(4):
            for s in range(4):
                e = Jet()
                for r in range(4):
                    e = e + Th[m][r]*Th[n][s].diff(r) + Th[n][r]*Th[s][m].diff(r) + Th[s][r]*Th[m][n].diff(r)
                # keep degree<=2
                bad = [k for k in e.d if sum(k) <= 2]
                if bad: return False
    return True
print('Jacobi (to degree 2):', jacobi(Th))
# J_nu = Theta^{mr} d_r Theta^{m nu} (valid degree 2)
J = [sum((Th[m][r]*Th[m][n].diff(r) for m in range(4) for r in range(4)), Jet()) for n in range(4)]
print('J(0) =', [j.c0() for j in J])
# identity J^nu = Box_G x^nu - G^{mu nu} d_mu ln rho  :  Box_G x^nu = (1/sqrtG) d_mu(sqrtG G^{mu nu})
Ginv, G, rho = geom.metric_data(Th)
sq = rho*rho
lhs = []
for n in range(4):
    box = sum(((sq*Ginv[m][n]).diff(m) for m in range(4)), Jet()) * sq.inv()
    gl = sum((Ginv[m][n]*rho.diff(m)*rho.inv() for m in range(4)), Jet())
    lhs.append((box - gl).c0())
print('Box x - G dln rho =', lhs)
print('equal:', all(lhs[i] == J[i].c0() for i in range(4)))
# -D_m D_m = O_s check: O_s f vs -Th^{mr} d_r(Th^{ms} d_s f) for f random poly
f = rpoly(3)
Df = [sum((Th[m][s]*f.diff(s) for s in range(4)), Jet()) for m in range(4)]
DDf = sum((sum((Th[m][r]*Df[m].diff(r) for r in range(4)), Jet()) for m in range(4)), Jet())
A_s, _ = geom.scalar_AB(Th, G, Ginv, rho)
Osf = Jet()
for m in range(4):
    for n in range(4):
        Osf = Osf + Ginv[m][n]*f.diff(m).diff(n)
for n in range(4):
    Osf = Osf + A_s[n][0][0]*f.diff(n)
print('(G d d f + A d f) - D_m D_m f at 0 (should be 0):', (Osf - DDf).c0())
