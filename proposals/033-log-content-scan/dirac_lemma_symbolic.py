"""Symbolic check: Z_n Dirac weights (x,y,z)=(-1/2,1,1/2) = periodic (1,1,0) + uniform E_delta contact + Omega_delta contact (J -> gamma^12/2).
Independent of data: identity in the symbols R, Rii, Rj, trEf (positive-sign trace), tau.  Contact normalisation from the Fursaev-Solodukhin cross term
(a_2 = (1/360) tr[60 R E_G + 180 E_G^2 + 30 Om^2 + ...], E_delta=-pi(1-n) d_S on each component, Om_delta = 2 pi (1-n) J d_S), 24 pi units."""
import sympy as sp
R, Rii, Rj, trEf, tau = sp.symbols('R Rii Rj trEf tau')
pi = sp.pi
Q = Rii - 2*Rj
D = -(sp.Rational(-1, 2)*(4*R/6 - trEf) - sp.Rational(4, 30)*Q + sp.Rational(1, 2)*tau)
Dper = -((4*R/6 - trEf) - sp.Rational(4, 30)*Q)
w = -1; nfib = 4
trEG = -trEf                                            # Gilkey sign
trE_d = -pi*nfib; trEE_d = -pi*trEG
cross = (60*(R*trE_d) + 360*trEE_d + 30*8*pi*(tau/2)) / 360 / (16*pi**2) * 24*pi   # Dirac J = gamma^12/2: tr(J Om) = tau/2
contact = sp.simplify(w*cross)
print('contact (E_delta + Omega_delta), weight -1 per Dirac field:', sp.expand(contact))
print('D - Dper - contact =', sp.simplify(D - Dper - contact))
