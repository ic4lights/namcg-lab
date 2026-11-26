"""032 r2, finding F1: on s = rho e^{-i th} a mass phase e^{-i s m} shifts the growth rate of |Theta chi_str| by -m sin(th).
Checks the shift and that for the vector mass-squared mu^2 = -3 the rate |a cos th - b sin th| + 3 sin th is > 0 on a grid of rays (so no convergent ray),
whereas for m > 0 there is a window of negative rate near th* (massless term only)."""
import mpmath as mp
mp.mp.dps = 40
a, b = mp.mpf('0.7'), mp.mpf('1.3')
def C(s):
    x, y = s * a, s * b
    return -1j * a * b / (16 * mp.pi ** 2 * mp.sinh(x) * mp.sin(y)) * 4 * (mp.cos(y) - mp.cosh(x)) ** 2
def rate(th, m, r1=mp.mpf(20), r2=mp.mpf(30)):
    f = lambda r: abs(mp.exp(-1j * r * mp.expj(-th) * m) * C(r * mp.expj(-th)))
    return mp.log(f(r2) / f(r1)) / (r2 - r1)
print("(th=0.50 lies within 0.006 of th*=0.4939 where the leading exponential cancels and the constant/oscillating subleading term dominates the finite-rho slope; the formula applies away from th*)")
print("th, measured rate, |a cos-b sin| - m sin th   (m=-3 and m=+1)")
for th in [0.2, 0.5, 0.8, 1.2]:
    th = mp.mpf(th)
    for m in (-3, 1):
        print(" th=%.2f m=%+d : %s  vs %s" % (th, m, mp.nstr(rate(th, m), 6), mp.nstr(abs(a*mp.cos(th)-b*mp.sin(th)) - m*mp.sin(th), 6)))
print("min over 400 rays th in (0.01,1.55) of |a cos-b sin| + 3 sin th (mu^2=-3):",
      mp.nstr(min(abs(a*mp.cos(t)-b*mp.sin(t)) + 3*mp.sin(t) for t in [mp.mpf(0.01)+mp.mpf(k)*mp.mpf(1.54)/399 for k in range(400)]), 6))
ths = mp.atan(a/b)
print("m=+1 at th*=%s: rate %s (<0: convergent window, massless term)" % (mp.nstr(ths, 5), mp.nstr(-mp.sin(ths), 6)))
