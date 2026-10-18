"""Convention check: with the Levi-Civita bundle (E_pos = Ric, Omega^c_d,12 = R^c_{d 12}) in the SAME conventions as sector_data,
   tr(J Omega_12) G^{11} = -R_ijij  and  tr_N E_G = -R_ii  (E_G = -Ric).  Run on the 029 example and one rotation-invariant SD member."""
import sympy as sp
from common import *
import geom, sd_family, sd_rot_family, sector_data as S
use_gaussian(3)
def lc_check(bsol, eta, x0):
    wj = sd_family.omega_jets(bsol, eta, x0)
    Th = theta_from_omega(wj)
    Ginv, G, rho = geom.metric_data(Th)
    Gam = geom.christoffel(G, Ginv)
    Rm, Ric, Rs = geom.riemann(Gam, G, Ginv)
    C = S.C
    gi = [[C(Ginv[i][j]) for j in range(4)] for i in range(4)]
    g0 = [[C(G[i][j]) for j in range(4)] for i in range(4)]
    Om12 = sp.Matrix(4, 4, lambda c, d: C(Rm[(c, d, 0, 1)])) * gi[0][0]
    J = sp.zeros(4, 4); J[0, 1] = 1; J[1, 0] = -1
    trJ = (J * Om12).trace()
    Ricl = [[C(Ric[i][j]) for j in range(4)] for i in range(4)]
    # mixed Ric^mu_nu = Ginv Ric ; tr over normal block
    mixed = sp.Matrix(4, 4, lambda i, j: sum(gi[i][k] * Ricl[k][j] for k in range(4)))
    trN_Ric = mixed[0, 0] + mixed[1, 1]
    d = S.run_jets(wj)
    return dict(trJ_LC=trJ, minus_Rijij=-d['Rijij'], trN_EG_LC=-trN_Ric, minus_Rii=-d['Rii'])
b1 = -(sd_family.X[0]*sd_family.X[2] + sd_family.X[1]*sd_family.X[3]); b2 = sd_family.X[0]*sd_family.X[3] - sd_family.X[1]*sd_family.X[2]; b3 = 1 + sd_family.X[2]**2 - sd_family.X[3]**2
eta = sd_family.lib.eta3()
for x0 in [(0, 0, sp.Rational(1, 3), sp.Rational(1, 5)), (0, 0, sp.Rational(2, 3), sp.Rational(1, 7))]:
    print('029 example', x0, lc_check([b1, b2, b3], eta, x0))
bsol, eta2, nf = sd_rot_family.rot_solution(4, 2)
print('rot family seed 2', lc_check(bsol, eta2, (0, 0, sp.Rational(1, 2), sp.Rational(1, 3))))
