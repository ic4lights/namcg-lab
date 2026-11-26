"""a_1, a_2 sector densities on the SU(2)-invariant family A = h(r) Lambda^3 at x0=(r0,0,0,0), symbolic in (r0,h0,h1,h2,h3).
Dirac = 1/2 (upper + lower real Weyl). Output pickled for use in analysis."""
import pickle, sys, time
import sympy as sp
import jetlib as jl
from jetlib import Jet
from common import theta_from_omega, gam_weyl_real
import su2_family as F
import geom

import sympy as sp
from sympy import QQ
syms = sp.symbols('r0 h0 h1 h2 h3')
K = QQ.frac_field(*syms[2:])
syms = (sp.Integer(1), sp.Integer(1)) + tuple(syms[2:])
F.setup(K, 3)
geom.SIGN_OVERRIDE = 1   # assumes Pf(omega)>0 at the point; sign fixed below by rho = |Pf|
t0 = time.time()
w = F.omega_jets_su2(K, syms)
Th = theta_from_omega(w)
Ginv, G, rho = geom.metric_data(Th)
# note: Pf(Theta)=1/Pf(omega); rho = 1/|Pf Theta| = |Pf omega|; SIGN_OVERRIDE=1 assumes Pf Theta >0 (i.e. Pf omega>0): fine for local structure
Gam = geom.christoffel(G, Ginv)
Rm, Ric, Rs = geom.riemann(Gam, G, Ginv)
riem2, ric2 = geom.curvature_invariants(Rm, Ric, Rs, G, Ginv)
res = {}
res['R'] = K.to_sympy(Rs.c0()); res['riem2'] = K.to_sympy(riem2); res['ric2'] = K.to_sympy(ric2)
res['rho'] = K.to_sympy(rho.c0())
A, B = geom.scalar_AB(Th, G, Ginv, rho)
om, EV, Om = geom.vassilevich(A, B, G, Ginv, Gam, 1)
res['scalar'] = [K.to_sympy(v) if not isinstance(v, dict) else {k: K.to_sympy(x) for k, x in v.items()} for v in geom.a_densities(EV, Om, Rs, riem2, ric2, Ginv, 1)]
A, B = geom.vector_AB(Th, G, Ginv, rho)
om, EV, Om = geom.vassilevich(A, B, G, Ginv, Gam, 4)
res['vector'] = [K.to_sympy(v) if not isinstance(v, dict) else {k: K.to_sympy(x) for k, x in v.items()} for v in geom.a_densities(EV, Om, Rs, riem2, ric2, Ginv, 4)]
dsum = None
for blk in ('upper', 'lower'):
    gm = gam_weyl_real(blk, K)
    A, B = geom.dirac_AB(Th, G, Ginv, rho, gm)
    om, EV, Om = geom.vassilevich(A, B, G, Ginv, Gam, 4)
    r = geom.a_densities(EV, Om, Rs, riem2, ric2, Ginv, 4)
    res['weyl_' + blk] = [K.to_sympy(v) if not isinstance(v, dict) else {k: K.to_sympy(x) for k, x in v.items()} for v in r]
J = [sum((Th[m][r]*Th[m][n].diff(r) for m in range(4) for r in range(4)), Jet()) for n in range(4)]
res['J'] = [K.to_sympy(j.c0()) for j in J]
res['Pf_omega'] = K.to_sympy(jl.pf4(w).c0())
pickle.dump(res, open('su2_a2_unit.pkl', 'wb'))
print('done in', time.time() - t0)
