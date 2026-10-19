"""032 script 3: order-F^4 character term with the orbital factor resummed, and the vector-Zeeman dressing of the mass-linear term.
Integrand  C(s) = Theta(s) * chi_str(s),  chi_str = 4 (cos y - cosh x)^2,  x = s f_e, y = s f_m   (28 content, n_ex = 6: vector 2cosh2x+2cos2y, 4+... see the identity below)
and  V(s) = Theta(s) * (chi_V(s) - 4),  chi_V = 2 cosh 2x + 2 cos 2y   (the Zeeman dressing of the vector mass-linear term).
Claims checked: (1) species identity  chi_str = 2cosh2x + 2cos2y + 6 - 2 - 8 cosh x cos y ;  (2) on the ray s = rho e^{-i th}: |C| ~ exp(rho |a cos th - b sin th|),
    |V| ~ same rate; vanishes only for th* = arctan(a/b);  (3) asymptotic form C -> (a b/pi^2) sinh^2( s (a - i b)/2 );  (4) on th* the integrand is bounded and oscillatory
    (decays only through the remainder), the integral  I4 = int_{ray th*} ds/s C(s)  exists (conditionally);  a real-axis (th=0, i eps) integral diverges exponentially for a>0.
(5) masses enter chi as phases exp(-i s m): unchanged rates on the real axis only; on a ray of angle th a mass m shifts the rate by -m sin th (see s8_mass_shift.py)."""
import mpmath as mp, numpy as np
mp.mp.dps = 40

def Theta(s, a, b):
    return -1j * a * b / (16 * mp.pi ** 2 * mp.sinh(s * a) * mp.sin(s * b))
def chi_str(s, a, b):
    x, y = s * a, s * b
    return 4 * (mp.cos(y) - mp.cosh(x)) ** 2
def chi_V(s, a, b):
    x, y = s * a, s * b
    return 2 * mp.cosh(2 * x) + 2 * mp.cos(2 * y)

if __name__ == "__main__":
    a, b = mp.mpf('0.7'), mp.mpf('1.3')
    x, y = mp.mpf('0.37') + 0.2j, mp.mpf('0.81') - 0.1j
    lhs = 2 * mp.cosh(2 * x) + 2 * mp.cos(2 * y) + 6 - 2 - 8 * mp.cosh(x) * mp.cos(y)
    print("(1) species identity:", mp.nstr(lhs - 4 * (mp.cos(y) - mp.cosh(x)) ** 2, 5))
    ths = a / b
    print("(2) growth rate of |C| along rays (a=%.2f, b=%.2f, th*=%.4f):" % (a, b, mp.atan(ths)))
    for th in [0.0, 0.2, mp.atan(ths), 0.8, 1.2]:
        ph = mp.expj(-th)
        r1, r2 = mp.mpf(20), mp.mpf(30)
        if th == 0:
            r1, r2 = mp.mpf('20.31'), mp.mpf('30.31')   # avoid the poles at s = n pi / b, take the envelope between them
        v1 = abs(Theta(r1 * ph, a, b) * chi_str(r1 * ph, a, b)); v2 = abs(Theta(r2 * ph, a, b) * chi_str(r2 * ph, a, b))
        rate = mp.log(v2 / v1) / (r2 - r1)
        print("   th=%.4f : measured d ln|C|/d rho = % .4f ;  |a cos th - b sin th| = %.4f" % (th, rate, abs(a * mp.cos(th) - b * mp.sin(th))))
    print("(3) asymptotic form ratio C / [(ab/pi^2) sinh^2(s(a-ib)/2)] at rho=25, th=0.6, 1.0:")
    for th in [0.6, 1.0]:
        s = 25 * mp.expj(-th)
        print("   th=%.1f ratio = %s" % (th, mp.nstr(Theta(s, a, b) * chi_str(s, a, b) / (a * b / mp.pi ** 2 * mp.sinh(s * (a - 1j * b) / 2) ** 2), 10)))
    print("(4) integral I4 = int_{ray} ds/s C(s) on th* (UV: integrand ~ s (f_e^2+f_m^2)^2 finite), with tail truncation test")
    ths = mp.atan(a / b); ph = mp.expj(-ths)
    f = lambda r: Theta(r * ph, a, b) * chi_str(r * ph, a, b) / (r * ph) * ph
    for R in [20, 40, 80]:
        val = mp.quad(f, mp.linspace(0, R, 4 * R + 1))
        print("   R=%3d  I4 = %s" % (R, mp.nstr(val, 10)))
    print("   asymptotic oscillation: |C| at rho=20,40,80,160 on th*:", [mp.nstr(abs(Theta(r * ph, a, b) * chi_str(r * ph, a, b)), 6) for r in (20, 40, 80, 160)])
    print("   same integrand on th=0.2 (should blow up): ", [mp.nstr(abs(Theta(r * mp.expj(-0.2), a, b) * chi_str(r * mp.expj(-0.2), a, b)), 6) for r in (10, 20, 40)])
    print("(5) leaf values: f_e/f_m = 1/sinh(tau) (028 kernel-plane closed form) -> th* = arctan(1/sinh tau):")
    for tau in [0.2, 0.5, 1.0, 1.5, 3.0]:
        print("   tau=%.1f  |y^4|/l = %.3f  f_e/f_m = %.3f  th* = %.4f rad" % (tau, np.sinh(tau), 1 / np.sinh(tau), np.arctan(1 / np.sinh(tau))))
