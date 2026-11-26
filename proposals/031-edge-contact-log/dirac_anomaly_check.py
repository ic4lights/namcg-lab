"""Consistency of the 029 Dirac (Z_n, antiperiodic, less singular) weights with the Dirac a- and c-anomaly, Weyl-covariant form.
Unweighted Dirac field (4 comps), Levi-Civita data on a totally geodesic Sigma:
   S_u = x*(1/24pi)*(4R/6 - trE) + y*4*(-(Rii-2Rj)/(720 pi)) + z*(1/24pi)*tau,   trE = R (E=R/4), tau = tr(g^12 Omega_12) = -Rj.
Z_n derivation of 029:  x = -1/2 (E-linear weight -c_B/2, tr R/6 weighted alike),  y = 1 (scalar d_B per component),
 z = +1/2 (term -(1/2) S_2 tr(g12 Om12) with the 24pi normalisation -> see below). The physical field carries statistical weight -1.
Solve for (x,y,z) demanding alpha R_Sigma + beta W with the Dirac anomaly values: physical alpha = -11/720, beta = +1/40 (units 1/pi)."""
import sympy as sp
R, Rii, Rj = sp.symbols('R Rii Rj')
x, y, z = sp.symbols('x y z')
pi = sp.pi
Rs = R - 2*Rii + Rj
Wd = Rj - Rii + R/3
trE = R
tau = -Rj
Su = x*(4*R/6 - trE)/(24*pi) + y*4*(-(Rii - 2*Rj)/(720*pi)) + z*tau/(24*pi)
Sphys = -Su                                                      # statistical weight -1 per Dirac field
a_t, b_t = sp.Rational(-11, 720), sp.Rational(1, 40)
target = (a_t*Rs + b_t*Wd)/pi
eqs = sp.Poly(sp.expand((Sphys - target)*pi), R, Rii, Rj).coeffs()
sol = sp.solve(eqs, [x, y, z], dict=True)
print('anomaly-implied (x,y,z) =', sol)
print('029 Z_n values (x,y,z) = (-1/2, 1, 1/2):', sp.simplify(sp.expand((Sphys - target).subs({x: -sp.Rational(1, 2), y: 1, z: sp.Rational(1, 2)})*pi)) == 0)
# sphere
vals = {R: 12, Rii: 6, Rj: 2}
print('S^4/S^2 physical Dirac:', sp.nsimplify(Sphys.subs({x: -sp.Rational(1, 2), y: 1, z: sp.Rational(1, 2)}).subs(vals)*4*pi), '(expect -11/90)')
# 24pi*S for the (6,2) content assembled from the weights: compare with 029 formula
Rr, e, Xp, T, W = sp.symbols('Rr e Xp T W')
Q = Rii - 2*Rj
bos = (6+2)*(R/6 - e) + Xp - sp.Rational(8, 30)*Q                       # 6 scalars + vector(4) - 2 ghosts ; trE_v = 4e - X'
# unweighted S_u*24pi = x(4R/6-trE_f) - y*(4/30)Q + z*tau , trE_f = 4e - Xp/2
Su24 = sp.Rational(-1, 2)*(4*R/6 - (4*e - Xp/2)) - sp.Rational(4, 30)*Q + sp.Rational(1, 2)*T
tot = bos + 2*(-1)*Su24
print('24pi sigma (6,2) from weights =', sp.expand(tot))
a029 = sp.Rational(4, 3)*R + 2*Rii - 2*Rj + 2*Wd - 12*e + sp.Rational(3, 2)*Xp - T
print('minus 029 formula =', sp.simplify(tot - a029))
# all-periodic (Dirac x=+1,y=1,z=0): zero for every background at (6,2)
Su24p = (4*R/6 - (4*e - Xp/2)) - sp.Rational(4, 30)*Q
totp = bos + 2*(-1)*Su24p
print('all-periodic 24pi sigma =', sp.simplify(totp), '; antiperiodic minus periodic =', sp.simplify(tot - totp))
