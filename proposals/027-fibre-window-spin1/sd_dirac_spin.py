"""027 script 15: Dirac (spinor) sector of the invariant sector.  D-slash^2 = Box + s Sigma_D^{ab} J_{ab} (sum over all a,b), Sigma_D^{ab} = (1/4)[gamma^a,gamma^b]; on fibre-constant functions
J^{ab} f = s (y^b d^a - y^a d^b) f.   P_D = t Delta_4 + i s ( Box + eps * cross_D ),  eps = +-1,  cross_D = sum_{ab} J^{ab} Sigma_{ab}  (indices lowered with eta).
Check:  tr(E + R/6) = 4 D1_scalar + (1/2) * [6 s^2 (1+a^2)/(t + i s a^2)]   for both eps  (index of the Dirac representation is half the vector index), no mass term."""
import sympy as sp
from sd_core import *
y = sp.symbols('y0:4', real=True); ell, t, s = sp.symbols('ell t s', positive=True)
eta = sp.diag(-1, 1, 1, 1)
yl = [sum(eta[i, j]*y[j] for j in range(4)) for i in range(4)]
yy = sum(y[i]*yl[i] for i in range(4)); m2 = -yy - ell**2
ginv4 = sp.Matrix(4, 4, lambda i, j: eta[i, j] + y[i]*y[j]/ell**2)
I2 = sp.eye(2); X = sp.Matrix([[0, 1], [1, 0]]); Yp = sp.Matrix([[0, -sp.I], [sp.I, 0]]); Zm = sp.Matrix([[1, 0], [0, -1]])
kp = sp.kronecker_product
Gm = [sp.I*kp(X, I2), kp(Yp, X), kp(Yp, Yp), kp(Yp, Zm)]          # gamma^a (upper), {g^a,g^b} = 2 eta^{ab}
SigU = lambda a, b: (Gm[a]*Gm[b] - Gm[b]*Gm[a])/4                  # Sigma^{ab}
SigL = lambda a, b: eta[a, a]*eta[b, b]*SigU(a, b)                 # Sigma_{ab}
z0, w0, a = sp.symbols('z0 w0 a', positive=True)
C = 1 + a**2; c4 = 8*a**4 + 8*a**2 + 1
D1 = -(-5*w0**2*z0*(c4 - 1) + 16*w0*z0*(w0*C + z0)*(3*C - 2) + (32*w0 + 64*z0)*(w0*C + z0)**2)/(32*(w0*C + z0)**2)
for (tt, ss, ee, y0v, y1v) in [(sp.Rational(1, 3), sp.Rational(1, 2), 1, 2, 0), (sp.Rational(2, 1), sp.Rational(-1, 3), sp.Rational(3, 2), 3, 1)]:
    for eps in (1, -1):
        sub = {t: tt, s: ss, ell: ee}
        m2n = m2.subs(sub); ginv4n = ginv4.subs(sub); sqrtg4n = ee/sp.sqrt(m2n)
        ADn = [ee**2*sum(sp.diff(sqrtg4n*ginv4n[i, j], y[i]) for i in range(4))/sqrtg4n for j in range(4)]
        ABoxn = [-y[j] for j in range(4)]
        Ginv_n = tt*ee**2*ginv4n + sp.I*ss*m2n*sp.Matrix(4, 4, lambda i, j: eta[i, j])
        ppn = tt*ee**2 + sp.I*ss*m2n
        Gcov_n = sp.Matrix(4, 4, lambda i, j: eta[i, j]/ppn - tt*yl[i]*yl[j]/(ppn*m2n*(sp.I*ss - tt)))
        # cross_D = sum_{ab} (y^b d^a - y^a d^b) Sigma_{ab} = 2 sum_{ab} y^b eta^{aa} d_a Sigma_{ab}  -> coefficient of d_mu:  2 sum_b y^b eta^{mu mu} Sigma_{mu b}
        def Xm(mu):
            return 2*sum((y[b]*eta[mu, mu]*SigL(mu, b) for b in range(4)), sp.zeros(4, 4))
        Amat = [(tt*ADn[j] + sp.I*ss*ABoxn[j])*sp.eye(4) + sp.I*ss*eps*Xm(j) for j in range(4)]
        pt = {y[0]: y0v, y[1]: y1v, y[2]: 0, y[3]: 0}
        trE, R6, _ = sd_first(Ginv_n, Amat, sp.zeros(4, 4), y, pt, rank=4, Gcov=Gcov_n)
        m2v = y0v**2 - y1v**2 - ee**2; aval = sp.sqrt(m2v)/ee
        sc = D1.subs({z0: tt - sp.I*ss, w0: sp.I*ss, a: aval})
        spinV = 6*ss**2*(1 + aval**2)/(tt + sp.I*ss*aval**2)
        full = trE + 4*R6; pred = 4*sc + spinV/2
        print("t=%s s=%s a^2=%s eps=%d | tr(E+R/6) = %s | 4 D1_sc + (1/2) spin_V = %s | diff %s" % (tt, ss, sp.nsimplify(aval**2), eps, sp.N(full, 12), sp.N(pred, 12), sp.N(full - pred, 3)))
