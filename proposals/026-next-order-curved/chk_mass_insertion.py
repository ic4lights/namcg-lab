"""Mass insertion: O_i -> O_i + m_i^2 (constant) shifts E_V -> E_V - m_i^2 and
   a_2^{(i)}(m) = a_2^{(i)}(0) - m_i^2 a_1^{(i)} + (1/2) n_i m_i^4          (a_1^{(i)} = tr(R/6 + E_V), no sqrtG).
Checked in exact arithmetic with the full machinery on a random Poisson bivector for scalar, vector, Dirac; then the log-order Einstein-type
coefficient  - sum_i w_i m_i^2 a_1^{(i)} = - [sum_i w_i n_i m_i^2/6] rho R[g_rho] - [sum_i w_i b_i m_i^2] rho^2 X  (b_scalar = b_ghost = 0, b_vec = 1, b_Dirac = 1/2)."""
import random
import jetlib as jl
from jetlib import Jet
from common import *
import geom
use_gaussian(3)
gm = gam_mn_domain()
random.seed(21)
rq = lambda: Q(random.randint(-6, 6), random.randint(1, 5))
y = [Jet.var(i) for i in range(4)]
def rpoly(deg):
    t = Jet()
    for mon in itertools.product(range(deg+1), repeat=4):
        if 1 <= sum(mon) <= deg:
            m = Jet.const(rq())
            for i, e in enumerate(mon):
                for _ in range(e): m = m * y[i]
            t = t + m
    return t
c = [[0,2,0,1],[-2,0,3,0],[0,-3,0,1],[-1,0,-1,0]]
A = [rpoly(4) for _ in range(4)]
w = omega_from_A(A); w = [[w[m][n] + Jet.const(Q(c[m][n])) for n in range(4)] for m in range(4)]
Th = theta_from_omega(w)
Ginv, G, rho = geom.metric_data(Th)
Gam = geom.christoffel(G, Ginv); Rm, Ric, Rs = geom.riemann(Gam, G, Ginv); riem2, ric2 = geom.curvature_invariants(Rm, Ric, Rs, G, Ginv)
m2 = {'scalar': Q(3, 7), 'vector': Q(5, 3), 'dirac': Q(2, 5)}
ok = True
tot_log_EH = {}
for name in ('scalar', 'vector', 'dirac'):
    if name == 'scalar': A_, B_ = geom.scalar_AB(Th, G, Ginv, rho); nf = 1
    elif name == 'vector': A_, B_ = geom.vector_AB(Th, G, Ginv, rho); nf = 4
    else: A_, B_ = geom.dirac_AB(Th, G, Ginv, rho, gm); nf = 4
    om, EV, Om = geom.vassilevich(A_, B_, G, Ginv, Gam, nf)
    a1_0, a2_0, _ = geom.a_densities(EV, Om, Rs, riem2, ric2, Ginv, nf)
    # massive: B -> B - m^2 * identity
    B_m = [[B_[i][j] - (Jet.const(m2[name]) if i == j else Jet()) for j in range(nf)] for i in range(nf)]
    om, EVm, Omm = geom.vassilevich(A_, B_m, G, Ginv, Gam, nf)
    a1_m, a2_m, _ = geom.a_densities(EVm, Omm, Rs, riem2, ric2, Ginv, nf)
    pred = a2_0 - m2[name]*a1_0 + QQ_I(nf)*m2[name]**2/2
    good = (a2_m == pred) and (a1_m == a1_0 - nf*m2[name])
    ok = ok and good
    print(name, ': a2(m) = a2(0) - m^2 a1 + n m^4/2 :', good)
print('all ok:', ok)
