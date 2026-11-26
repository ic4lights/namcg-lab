"""Exact sector data at a point of Sigma for a self-dual closed omega (copy of the 029 evaluation with extra outputs):
 R, R_ii, R_ijij, e, vector E_G normal-block trace, tr(J Omega_12) for the vector (J = rotation in internal normal plane),
 Dirac tau_Omega, X'. All in G-orthonormal normalisation (G = rho delta)."""
import sympy as sp
from common import *
import geom, sd_family, lib
use_gaussian(3)
gm = gam_mn_domain(); gam = gammas()

def C(z):
    z = z.c0() if hasattr(z, 'c0') else z
    return sp.sympify(QQ_I.to_sympy(z))

def run(x0, bsol, eta):
    return run_jets(sd_family.omega_jets(bsol, eta, x0))

def run_jets(wj):
    Th = theta_from_omega(wj)
    Ginv, G, rho = geom.metric_data(Th)
    Gam = geom.christoffel(G, Ginv)
    Rm, Ric, Rs = geom.riemann(Gam, G, Ginv)
    g0 = [[C(G[i][j]) for j in range(4)] for i in range(4)]
    gi = [[C(Ginv[i][j]) for j in range(4)] for i in range(4)]
    R = C(Rs); r = g0[0][0]
    Ricl = [[C(Ric[i][j]) for j in range(4)] for i in range(4)]
    Rii = (Ricl[0][0] + Ricl[1][1]) / r
    Rl = lambda a, b, c, d: sum(g0[a][p] * C(Rm[(p, b, c, d)]) for p in range(4))
    Rijij = sum(Rl(i, j, i, j) for i in range(2) for j in range(2)) / r**2
    A, Bm = geom.scalar_AB(Th, G, Ginv, rho); om, EV, Om = geom.vassilevich(A, Bm, G, Ginv, Gam, 1); e = -C(EV[0][0])
    A, Bm = geom.vector_AB(Th, G, Ginv, rho); om, EVv, Omv = geom.vassilevich(A, Bm, G, Ginv, Gam, 4)
    EG = sp.Matrix(4, 4, lambda i, j: C(EVv[i][j]))             # Gilkey sign: O = -(nabla+omega)^2 - E_V  (a_1 = tr(R/6 + E_V))
    trN_EG = EG[0, 0] + EG[1, 1]
    Om12v = sp.Matrix(4, 4, lambda i, j: C(Omv[0][1][i][j])) * gi[0][0]
    J = sp.zeros(4, 4); J[0, 1] = 1; J[1, 0] = -1               # J^mu_nu = d^mu_1 d_{nu 2} - d^mu_2 d_{nu 1}
    trJOm_v = (J * Om12v).trace()
    A, Bm = geom.dirac_AB(Th, G, Ginv, rho, gm); om, EVd, Omd = geom.vassilevich(A, Bm, G, Ginv, Gam, 4)
    Om12f = sp.Matrix(4, 4, lambda i, j: C(Omd[0][1][i][j])) * gi[0][0]
    tau = sp.simplify(((gam[0] * gam[1]) * Om12f).trace())
    trEf_G = sum(C(EVd[i][i]) for i in range(4))
    trEv_G = EG.trace()
    Xp = -(-trEv_G - 4 * e)                                       # X' = -tr(b b) = -(trE_pos - 4e), trE_pos = -trE_G
    return dict(R=R, Rii=Rii, Rijij=Rijij, e=e, trN_EG=trN_EG, trJOm_v=trJOm_v, tau=tau, Xp=Xp, trEv_G=trEv_G, trEf_G=trEf_G,
                Rsig=R - 2 * Rii + Rijij, rho=C(rho))
