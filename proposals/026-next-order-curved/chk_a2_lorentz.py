"""Lorentzian check (eta = diag(-1,1,1,1)) of  a_2^{tot} = (1/2) sqrt|G| S  at (N_s,n_D)=(6,2), exact arithmetic, random real off-shell Theta."""
import random
import sympy as sp
import jetlib as jl
from jetlib import Jet
from common import *
import geom
use_gaussian(3)
geom.ETA = [-1, 1, 1, 1]
eta_d = [-1, 1, 1, 1]
I = sp.I
s_ = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
Z = sp.zeros(2, 2); E2 = sp.eye(2)
g0 = I*sp.Matrix(sp.BlockMatrix([[Z, E2], [E2, Z]]))
gk = [sp.Matrix(sp.BlockMatrix([[Z, -I*s_[k]], [I*s_[k], Z]])) for k in range(3)]
gam = [g0] + gk
for a in range(4):
    for b in range(4):
        ac = gam[a]*gam[b] + gam[b]*gam[a]
        assert sp.simplify(ac - (2*eta_d[a] if a == b else 0)*sp.eye(4)) == sp.zeros(4, 4)
gm = [[None]*4 for _ in range(4)]
for m in range(4):
    for n in range(4):
        M = (gam[m]*gam[n] - gam[n]*gam[m])/2
        gm[m][n] = [[QQ_I.from_sympy(sp.nsimplify(M[i, j])) for j in range(4)] for i in range(4)]
y = [Jet.var(i) for i in range(4)]
def rpoly(deg, rq):
    t = Jet()
    for mon in itertools.product(range(deg+1), repeat=4):
        if 1 <= sum(mon) <= deg:
            m = Jet.const(rq())
            for i, e in enumerate(mon):
                for _ in range(e): m = m * y[i]
            t = t + m
    return t
c = [[0,2,0,1],[-2,0,3,0],[0,-3,0,1],[-1,0,-1,0]]
def mmq(A, B):
    return [[sum((A[i][k]*B[k][j] for k in range(4)), QQ_I(0)) for j in range(4)] for i in range(4)]
for seed in range(3):
    random.seed(300 + seed)
    rq = lambda: Q(random.randint(-6, 6), random.randint(1, 5))
    A = [rpoly(4, rq) for _ in range(4)]
    w = omega_from_A(A)
    w = [[w[m][n] + Jet.const(Q(c[m][n])) for n in range(4)] for m in range(4)]
    Th = theta_from_omega(w)
    out, sqrtG, base = geom.sector_all(Th, gm)
    Ginv, G, rho = geom.metric_data(Th)
    G0 = [[G[i][j].c0() for j in range(4)] for i in range(4)]
    Gi0 = [[Ginv[i][j].c0() for j in range(4)] for i in range(4)]
    # B^t_{mn} (lower mn with eta): B[t][m][n] = Theta^{r t} d_r Theta_{mn}
    B = [[[sum((Th[r][t]*Th[m][n].diff(r) for r in range(4)), Jet()).c0()*eta_d[m]*eta_d[n] for n in range(4)] for m in range(4)] for t in range(4)]
    # vector rep matrices (b_s)^m_n = eta^{ma} b_{s,an}
    bs_low = [[[sum((G0[s][t]*B[t][m][n] for t in range(4)), QQ_I(0)) for n in range(4)] for m in range(4)] for s in range(4)]
    bs = [[[bs_low[s][m][n]*eta_d[m] for n in range(4)] for m in range(4)] for s in range(4)]
    def bb(reps):
        n = len(reps[0])
        M = [[QQ_I(0) for _ in range(n)] for _ in range(n)]
        for s in range(4):
            for t in range(4):
                if jl.isz(Gi0[s][t]): continue
                P = [[sum((reps[s][i][k]*reps[t][k][j] for k in range(n)), QQ_I(0)) for j in range(n)] for i in range(n)]
                M = [[M[i][j] + Gi0[s][t]*P[i][j] for j in range(n)] for i in range(n)]
        return M
    Mv = bb(bs)
    trV = sum((sum((Mv[i][k]*Mv[k][i] for k in range(4)), QQ_I(0)) for i in range(4)), QQ_I(0))
    beta = []
    for s in range(4):
        M = [[QQ_I(0) for _ in range(4)] for _ in range(4)]
        for m in range(4):
            for n in range(4):
                for a in range(4):
                    for b in range(4):
                        M[a][b] = M[a][b] + bs_low[s][m][n]*gm[m][n][a][b]/4
        beta.append(M)
    Md = bb(beta)
    trD = sum((sum((Md[i][k]*Md[k][i] for k in range(4)), QQ_I(0)) for i in range(4)), QQ_I(0))
    S = trV - 2*trD
    tot1 = sqrtG*(4*out['scalar'][0] + out['vector'][0] - 2*out['dirac'][0])
    tot2 = sqrtG*(4*out['scalar'][1] + out['vector'][1] - 2*out['dirac'][1])
    sq = abs(base['rho'])**2 if not hasattr(base['rho'], 'x') else base['rho']**2
    print('seed', seed, ' a1_total =', tot1, ' a2_total == (1/2) sqrtG S :', tot2 == sqrtG*S/2, ' value', float(tot2.x), ' G signature (eigen signs):', 'ok')
