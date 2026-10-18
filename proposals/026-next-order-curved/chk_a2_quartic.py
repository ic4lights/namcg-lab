"""Claim: at (N_s, n_D) = (6, 2) the total a_2 density (mod box terms) equals (1/2) sqrtG * S,
S = tr_V[(b_s b^s)^2] - n_D tr_D[(beta_s beta^s)^2],  b_s = G_{st} B^t, B^t_{mu nu} = Theta^{rho t} d_rho Theta^{mu nu},
beta_s = (1/4) gamma^{mu nu} G_{st} B^t_{mu nu}; contraction with G.  Verified in exact arithmetic on random off-shell Poisson bivectors.
Also checks sum_w tr Omega^2 = 0 and sum_w tr E = 0 separately."""
import random
import jetlib as jl
from jetlib import Jet
from common import *
import geom
use_gaussian(3)
gm = gam_mn_domain()
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
def matmul(A, B):
    n = len(A)
    return [[sum((A[i][k]*B[k][j] for k in range(n)), QQ_I(0)) for j in range(n)] for i in range(n)]
def tr(A): return sum((A[i][i] for i in range(len(A))), QQ_I(0))
for seed in range(3):
    random.seed(200 + seed)
    rq = lambda: Q(random.randint(-6, 6), random.randint(1, 5))
    A = [rpoly(4, rq) for _ in range(4)]
    w = omega_from_A(A)
    w = [[w[m][n] + Jet.const(Q(c[m][n])) for n in range(4)] for m in range(4)]
    Th = theta_from_omega(w)
    out, sqrtG, base = geom.sector_all(Th, gm)
    Ginv, G, rho = geom.metric_data(Th)
    G0 = [[G[i][j].c0() for j in range(4)] for i in range(4)]
    B = [[[sum((Th[r][t]*Th[m][n].diff(r) for r in range(4)), Jet()).c0() for n in range(4)] for m in range(4)] for t in range(4)]  # B[t][m][n]
    # b_s = G_{st} B^t  (vector rep: matrix (b_s)^m_n = G_{st} B^t_{mn})
    bs = [[[sum((G0[s][t]*B[t][m][n] for t in range(4)), QQ_I(0)) for n in range(4)] for m in range(4)] for s in range(4)]
    # b.b = G^{st} b_s b_t
    Gi0 = [[Ginv[i][j].c0() for j in range(4)] for i in range(4)]
    def bb(reps):
        M = [[QQ_I(0)]*len(reps[0]) for _ in range(len(reps[0]))]
        n = len(reps[0])
        M = [[QQ_I(0) for _ in range(n)] for _ in range(n)]
        for s in range(4):
            for t in range(4):
                if Gi0[s][t] == 0: continue
                P = matmul(reps[s], reps[t])
                M = [[M[i][j] + Gi0[s][t]*P[i][j] for j in range(n)] for i in range(n)]
        return M
    Mv = bb(bs)
    trV = tr(matmul(Mv, Mv))
    # Dirac (complex 4x4): beta_s = 1/4 gamma^{mn} b_s,mn  (b_s,mn = G_{st}B^t_{mn})
    beta = []
    for s in range(4):
        M = [[QQ_I(0) for _ in range(4)] for _ in range(4)]
        for m in range(4):
            for n in range(4):
                coef = bs[s][m][n]
                for a in range(4):
                    for b in range(4):
                        M[a][b] = M[a][b] + coef*gm[m][n][a][b]/4
        beta.append(M)
    Md = bb(beta)
    trD = tr(matmul(Md, Md))
    nD = 2
    S = trV - nD*trD
    tot2 = sqrtG*((6-2)*out['scalar'][1] + out['vector'][1] - nD*out['dirac'][1])
    # separate checks
    sumtrE = sum(w_*out[k][2]['trE'] for k, w_ in (('scalar', 4), ('vector', 1), ('dirac', -nD)))
    sumOm = sum(w_*out[k][2]['trOm2'] for k, w_ in (('scalar', 4), ('vector', 1), ('dirac', -nD)))
    sumcur = sum(w_*out[k][2]['cur'] for k, w_ in (('scalar', 4), ('vector', 1), ('dirac', -nD)))
    print('seed', seed, ': sum w trE =', sumtrE, ' sum w trOm^2 =', sumOm, ' sum w cur =', sumcur)
    print('   a2_total =', float(tot2.x), '  (1/2) sqrtG S =', float((sqrtG*S/2).x), '  equal:', tot2 == sqrtG*S/2)
    print('   tr_V(bb)^2 =', float(trV.x), ' tr_D(bb)^2 =', float(trD.x), ' S=', float(S.x))
