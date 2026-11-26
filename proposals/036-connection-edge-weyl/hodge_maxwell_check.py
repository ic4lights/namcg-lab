"""Validation of the cross-term machinery on the metric-only Hodge-Maxwell operator (E = -Ric, Omega = Riemann, 4 components, Feynman gauge, ghosts = -2 scalars) on the 033 modes,
standard cone c = (1,0), units 1/(24 pi), calibration 24 pi sigma = 3 x [a_2 cross density with cross = 2 x bilinear], fixed by the scalar (1/30)(3W - Rsig).
a_2 = (1/360)[60 R tr E + 180 tr E^2 + 30 tr Omega^2 + tr1 (5R^2 - 2Ric^2 + 2Riem^2)]  (R^(1) = 0 on the modes).
Cross terms: tr E^2 -> 2 tr(E E_delta), E_delta = -Ric' (normal-block Ricci delta);  tr Omega^2 -> 2 tr(Omega Omega') = -2 Riem.Riem';  Riem^2 -> 2 Riem.Riem';  Ric^2 -> 2 Ric.Ric'.
Compare with the T-side coefficient 12 kappa_C of the same operator: 12 * [(1/360)(172 Ric^2 - 22 Riem^2) - 2 s]/C^2 with Ric^2 = C^2/2, Riem^2 = 2 C^2, s = C^2/120."""
import sympy as sp
from sympy import Rational as Q
import lin_lib as L, lib
from pairing_modes import modes
from profile_lib import Rprime, fit
ca, cb = sp.symbols('c_a c_b')
Rp = Rprime(1, 0)
Ricp = sp.Matrix(4, 4, lambda n, s: sum(Rp[(m, n, m, s)] for m in range(4)))
for name, Thb in (('SD', lib.eta3()[2].inv()), ('ASD', lib.etabar()[2].inv())):
    ms = modes(Thb, 6, 21)
    Av = fit(ms, [sp.expand(sum(m['Rt'][k]*Rp[k] for k in Rp)) for m in ms])
    Bv = fit(ms, [sp.expand(sum(m['Ric'][i, j]*Ricp[i, j] for i in range(4) for j in range(4))) for m in ms])
    A = sp.Matrix(Av); B = sp.Matrix(Bv)
    scalar = (A - B)*Q(1, 90)
    vec_metric = 4*scalar
    vec_E = B                        # (1/360)*180*2 tr(E E_delta) = Ric.Ric'
    vec_Om = -A/6                    # (1/360)*30*(-2 A)
    def u(x): return 3*x
    print('==', name)
    print(' scalar  (W,Rsig):', u(scalar).T, ' [calibration (1/10, -1/30)]')
    print(' Maxwell with Omega_delta only (no E contact):', (u(vec_metric + vec_Om) - 2*u(scalar)).T)
    tot = u(vec_metric + vec_E + vec_Om) - 2*u(scalar)
    print(' Maxwell with E_delta and Omega_delta        :', tot.T, ' [12 c_s = 6/5 in W; a-type -31/15 = 62 x (-1/30)]')
    Tside = 12*(Q(1, 360)*(172*Q(1, 2) - 22*2) - 2*Q(1, 120))
    print(' T-side 12 kappa_C of the Hodge-Maxwell operator =', Tside, ' ; W gap =', sp.simplify(tot[0] - Tside))
    print(' W carried by E-contact term:', u(vec_E)[0], '(Rsig:', u(vec_E)[1], ')')
