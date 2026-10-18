"""Fixed-state log coefficient + imported Hodge-type vector contacts, on the non-self-dual family omega = d(h Lambda^3).
24 pi sigma_fs = S2 formula (029 assembly, with W);  24 pi (C_E + C_Om) = -(R + 3 tr_N E_G) + tr(J Omega_12)."""
import sys
import sympy as sp
from common import *
import sector_data as S, nonsd_family as NF
use_gaussian(3)
r = NF.r
def total(hexpr, x0):
    wj = NF.omega_jets(hexpr, x0)
    d = S.run_jets(wj)
    R, Rii, Rj, e = d['R'], d['Rii'], d['Rijij'], d['e']
    W = Rj - Rii + R / 3
    trEv = -d['trEv_G']; trEf = -d['trEf_G']
    Rsig = R - 2 * Rii + Rj
    s24 = sp.Rational(8, 6) * R - (4 * e + trEv) + R - trEf - d['tau'] - Rj - Rsig + 2 * W
    cE = -(R + 3 * d['trN_EG']); cO = d['trJOm_v']
    return dict(d=d, W=W, sigma24=s24, CE=cE, COm=cO, total=sp.simplify(s24 + cE + cO))
if __name__ == '__main__':
    c = sp.Rational(1)
    pts = [(0, 0, sp.Rational(3, 5), sp.Rational(4, 5)), (0, 0, sp.Rational(4, 5), sp.Rational(-3, 5))]
    # J = 0 profiles: h = c (1 +- sqrt(1 - C/r^4)); at r = 1 choose C = 16/25 so sqrt = 3/5 ; need exact symbolic profile
    C0 = sp.Rational(16, 25)
    for sign in (+1, -1):
        h = c * (1 + sign * sp.sqrt(1 - C0 / r**4))
        for x0 in pts:
            out = total(h, x0)
            print('J=0 profile sign', sign, 'x0', x0, ' W=', out['W'], ' 24pi sigma_fs =', out['sigma24'], ' 24pi C_E =', out['CE'], ' 24pi C_Om =', out['COm'], ' TOTAL =', out['total'])
            sys.stdout.flush()
    # J != 0 control profiles
    for name, h in (('1+r^2', 1 + r**2), ('1/(1+r^2)', 1 / (1 + r**2)), ('r^3+2', r**3 + 2)):
        x0 = pts[0]
        out = total(h, x0)
        print('J!=0 profile', name, 'x0', x0, ' W=', out['W'], ' 24pi sigma_fs =', out['sigma24'], ' 24pi C_E =', out['CE'], ' 24pi C_Om =', out['COm'], ' TOTAL =', out['total'])
        sys.stdout.flush()

    # additional diagnostics: e - R/6 (scalar/ghost uniform contact is 6(e - R/6) in 24 pi units) and J (radial) value
    for sign in (+1, -1):
        h = c * (1 + sign * sp.sqrt(1 - C0 / r**4))
        out = total(h, pts[0])
        print('J=0 sign', sign, ' e - R/6 =', sp.simplify(out['d']['e'] - out['d']['R'] / 6), ' uniform scalar+ghost contact (24pi units) 6(e-R/6) =', sp.simplify(6 * (out['d']['e'] - out['d']['R'] / 6)))
    for name, h in (('1+r^2', 1 + r**2), ('1/(1+r^2)', 1 / (1 + r**2))):
        out = total(h, pts[0])
        print('J!=0', name, ' e - R/6 =', sp.simplify(out['d']['e'] - out['d']['R'] / 6))
