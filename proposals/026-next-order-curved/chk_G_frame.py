"""G for omega = d(h(r) Lambda^3) at a generic Cartesian point:  G_{mn} = alpha^2 (x_m x_n + L3_m L3_n)/r^2 + beta^2 (L1_m L1_n + L2_m L2_n)/r^2,
alpha = r h' + 2h, beta = 2h, (L^i)_n = eta^i_{mn} x^m.  Closed-form h = c (1 + sig sqrt(1 - C/r^4)); also checks alpha/beta = sig/s."""
import mpmath as mp
import lib
from chk_J_cartesian import theta_num
mp.mp.dps = 50
eta = [mp.matrix(e.tolist()) for e in lib.eta3()]
x = [mp.mpf('0.7'), mp.mpf('-1.1'), mp.mpf('0.4'), mp.mpf('0.9')]
r = mp.sqrt(sum(xi*xi for xi in x))
for sig, Cv in ((1, mp.mpf('-0.8')), (-1, mp.mpf('0.8')), (1, mp.mpf('0.8'))):
    c = mp.mpf('1.3')
    hf = lambda rr, sig=sig, Cv=Cv: c*(1 + sig*mp.sqrt(1 - Cv/rr**4))
    hp = lambda rr, sig=sig, Cv=Cv: c*sig*(2*Cv/rr**5)/mp.sqrt(1 - Cv/rr**4)
    Th = theta_num(x, hf, hp)
    Ginv = Th.T*Th
    G = Ginv**-1
    h = hf(r); alpha = r*hp(r) + 2*h; beta = 2*h
    L = [mp.matrix([sum(eta[i][m, n]*x[m] for m in range(4)) for n in range(4)]) for i in range(3)]
    xv = mp.matrix(x)
    Gp = alpha**2*(xv*xv.T + L[2]*L[2].T)/r**2 + beta**2*(L[0]*L[0].T + L[1]*L[1].T)/r**2
    s = mp.sqrt(1 - Cv/r**4)
    print('sigma=%d C=%s: max|G - G_pred| = %s ; alpha/beta = %s, sigma/s = %s' % (sig, mp.nstr(Cv, 3), mp.nstr(max(abs(G[i, j]-Gp[i, j]) for i in range(4) for j in range(4)), 5), mp.nstr(alpha/beta, 10), mp.nstr(sig/s, 10)))
