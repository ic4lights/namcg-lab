"""Is the matrix-derived (Poisson-limit, target-frame) vector operator equivalent, on the 033 modes, to the Hodge-Maxwell operator of the metric G (E = -Ric, Omega = Riemann)?
Quadratic a_2 on the delta-rho=0 modes (R = 0, constant background):  a_2 = (1/360)[180 tr E^2 + 30 tr Omega^2 + tr1 (2 Riem^2 - 2 Ric^2)].
Hodge vector: tr E^2 = Ric^2, tr Omega^2 = -Riem^2, tr1 = 4.   Scalar s = (1/360)(2 Riem^2 - 2 Ric^2).   Matrix-derived vector (033): v - 4s = (1/12) tr Omega^2 = -C^2/3."""
import sympy as sp
import lin_lib as L, lib
from pairing_modes import modes
for name, Thb in (('SD', lib.eta3()[2].inv()), ('ASD', lib.etabar()[2].inv())):
    ms = modes(Thb, 6, 13)
    for m in ms[:3]:
        C2, R2, Ri2, tO = m['C2'], m['riem2'], m['ric2'], m['trOm2']
        s = sp.Rational(1, 360)*(2*R2 - 2*Ri2)
        vH = sp.Rational(1, 360)*(180*Ri2 - 30*R2 + 4*(2*R2 - 2*Ri2))
        print(name, ' Riem2/C2 =', R2/C2, ' Ric2/C2 =', Ri2/C2, ' trOm2/C2 =', tO/C2, ' | s/C2 =', s/C2, ' Hodge (v-4s)/C2 =', sp.simplify((vH-4*s)/C2), ' matrix-derived (v-4s)/C2 = -1/3')
