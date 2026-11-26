"""Independent check (mpmath, finite differences, 60 digits) that the closed-form SU(2)-invariant solutions
h(r) = c (1 + sigma sqrt(1 - C/r^4)) give J_nu = Theta^{mu rho} d_rho Theta^{mu nu} = 0 at generic Cartesian points,
and that SD (h=const) and ASD (h=c/r^4) also do, while a generic h (h=r^k, k=1) does not."""
import mpmath as mp
import lib
mp.mp.dps = 60
eta3 = lib.eta3()
E3 = [[int(eta3[2][m, n]) for n in range(4)] for m in range(4)]

def omega_num(x, hfun, hprime):
    r = mp.sqrt(sum(xi*xi for xi in x))
    h = hfun(r); hp = hprime(r)
    # A_nu = h(r) E3_{mu nu} x_mu ; dA_{mn} = d_m A_n - d_n A_m
    w = mp.zeros(4, 4)
    for m in range(4):
        for n in range(4):
            # d_m A_n = h' (x_m/r) E3_{k n} x_k + h E3_{m n}
            dmAn = hp*x[m]/r*sum(E3[k][n]*x[k] for k in range(4)) + h*E3[m][n]
            dnAm = hp*x[n]/r*sum(E3[k][m]*x[k] for k in range(4)) + h*E3[n][m]
            w[m, n] = dmAn - dnAm
    return w

def theta_num(x, hfun, hprime):
    w = omega_num(x, hfun, hprime)
    return w**-1

def Jvec(x, hfun, hprime, eps=mp.mpf(10)**-25):
    Th0 = theta_num(x, hfun, hprime)
    J = [mp.mpf(0)]*4
    for r in range(4):
        xp = list(x); xm = list(x); xp[r] += eps; xm[r] -= eps
        dTh = (theta_num(xp, hfun, hprime) - theta_num(xm, hfun, hprime))/(2*eps)
        for n in range(4):
            J[n] += sum(Th0[m, r]*dTh[m, n] for m in range(4))
    return J

if __name__ == '__main__':
    x = [mp.mpf('0.7'), mp.mpf('-1.1'), mp.mpf('0.4'), mp.mpf('0.9')]
    cases = {}
    Cc = mp.mpf('0.8')
    for sig in (1, -1):
        for Csign in (1, -1):
            Cv = Csign*Cc
            cases['closed form sigma=%d C=%s' % (sig, '+0.8' if Csign > 0 else '-0.8')] = (
                lambda r, sig=sig, Cv=Cv: 1 + sig*mp.sqrt(1 - Cv/r**4),
                lambda r, sig=sig, Cv=Cv: sig*(2*Cv/r**5)/mp.sqrt(1 - Cv/r**4))
    cases['SD h=1'] = (lambda r: mp.mpf(1), lambda r: mp.mpf(0))
    cases['ASD h=r^-4'] = (lambda r: r**-4, lambda r: -4*r**-5)
    cases['NOT a solution h=r'] = (lambda r: r, lambda r: mp.mpf(1))
    for name, (hf, hp) in cases.items():
        J = Jvec(x, hf, hp)
        print('%-34s |J| = %s   Pf(omega) = %s' % (name, mp.nstr(mp.sqrt(sum(j*j for j in J)), 5), mp.nstr(omega_num(x, hf, hp)[0,1]*omega_num(x, hf, hp)[2,3]-omega_num(x, hf, hp)[0,2]*omega_num(x, hf, hp)[1,3]+omega_num(x, hf, hp)[0,3]*omega_num(x, hf, hp)[1,2], 5)))
