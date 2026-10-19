"""Diagonal Poisson-cone family  Theta^{12} = r^{-eps c_a},  Theta^{34} = r^{-eps c_b}  (first order in eps), about Theta-bar with
Theta^{12}=Theta^{34} (SD) or Theta^{12}=-Theta^{34} (ASD) up to orientation.  G = diag(r^{2 eps c_a} 1_2, r^{2 eps c_b} 1_2).
Delta content (d_a d_b ln r = pi delta_ab delta^2 + PV, traceless PV):
   R_delta'_{1212} = c_a ;  R_delta'_{a i b j} = (c_b/2) delta_ab delta_ij  (units 2 pi (1-n) delta_Sigma, standard cone = c_a=1,c_b=0)
   Ric'_{ab} = (c_a+c_b) delta_ab, Ric'_{ij} = c_b delta_ij ; holonomy of the vector connection  H' = c_a J_12 + c_b J_34 (derived in the proposal).
Cross term of the weighted a_2 (modes: R=E^(1)=X'^(1)=0):  24 pi sigma = 3 N_tot Phi_metric + kappa_X tau_{H'},
   Phi_metric = (1/90)(Riem.Riem' - Ric.Ric') = (1/90)[(c_a-c_b) R_ijij - c_a K - c_b P],  K = sum_{a in perp,i in par} R_{aiai}, P = sum_{i,j in par} R_{ijij}.
We test c=(1,0) against the 033 'completed' W coefficient and then ask for the gap as a function of (c_a,c_b)."""
import random, sympy as sp
from sympy import Rational as Q
import lin_lib as L, lib
from pairing_modes import modes, gen
ca, cb, Ns, nD = sp.symbols('c_a c_b N_s n_D')
Ntot = Ns + 2 - 4*nD; kX = 1 - nD/2
for name, Thb, chi in (('SD', lib.eta3()[2].inv(), 1), ('ASD', lib.etabar()[2].inv(), -1)):
    ms = modes(Thb, 8, 7)
    aW, aS = sp.symbols('aW aS')
    def fit(vals):
        sol = sp.solve([vals[i]-aW*ms[i]['W']-aS*ms[i]['Rsig'] for i in range(2)], [aW, aS], dict=True)[0]
        res = {sp.simplify(vals[i]-sol[aW]*ms[i]['W']-sol[aS]*ms[i]['Rsig']) for i in range(2, len(ms))}
        assert res == {0}, res
        return sol[aW], sol[aS]
    Kv = [sum(m['Rt'][(a, i, a, i)] for a in (0, 1) for i in (2, 3)) for m in ms]
    Pv = [sum(m['Rt'][(i, j, i, j)] for i in (2, 3) for j in (2, 3)) for m in ms]
    Rij = [m['Rj'] for m in ms]
    K = fit(Kv); P = fit(Pv); Rj = fit(Rij)
    t12 = fit([(gen(0,1)*m['Om12']).trace() for m in ms]) if 'Om12' in ms[0] else None
    print('==', name, ' K=(W,Rsig)', K, ' P', P, ' R_ijij', Rj, ' tau12', t12)
    tau12W = -2; tau34W = 2*chi
    PhiW = (1/sp.Integer(90))*((ca-cb)*Rj[0] - ca*K[0] - cb*P[0])
    AW_metric = 3*Ntot*PhiW
    AW_om = kX*(ca*tau12W + cb*tau34W)
    T = Ntot/10 - 4*kX
    print(' metric part 3 Phi_W :', sp.simplify(3*PhiW), ' ; at c=(1,0):', sp.simplify(3*PhiW.subs({ca:1, cb:0})))
    gap = sp.expand(AW_metric + AW_om - T)
    print(' gap(c_a,c_b) =', sp.factor(gap))
    print(' gap at (1,0) :', sp.factor(gap.subs({ca:1, cb:0})), ' [033 completed gap 2 - nD]')
    print(' coefficient of N_tot :', sp.simplify(sp.diff(gap, Ns)), '; coefficient of kappa_X (at fixed N_tot):', sp.simplify((gap - sp.diff(gap, Ns)*Ntot)/kX))
