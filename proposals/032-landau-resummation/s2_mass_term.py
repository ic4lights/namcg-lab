"""032 script 2: the mass-supertrace term of 028 with the orbital factor resummed (exact Landau factor of s1_orbital.py).
Mass-linear term without Z insertions:  +M_str Tr[(H-i0)^{-1}] = M_str * i int_0^inf ds Tr e^{-isH}, H = H0 (common orbital operator).
Per unit horizontal volume (centre variable fixed):  i int ds Theta(s) = (1/16 pi^2) [ 1/s0 + g(a,b) ] + O(s0),   a=f_e, b=f_m,
   g(a,b) = int_0^inf ds [ ab/(sinh(as) sin(bs - i0)) - 1/s^2 ].
(i) the integrand is analytic in the open fourth quadrant and |.|~exp(-|s|(a cos th + b sin th)): ray independence checked numerically;
(ii) closed form (both rotations of the contour, poles of 1/sinh at s = -i n pi/a and of 1/sin at s = n pi/b):
        g(a,b) = pi [ b S(b/a) + i a S(a/b) ],   S(r) = sum_{n>=1} (-1)^n / sinh(n pi r)  < 0,
     so Re g < 0 and Im g < 0 for all a,b > 0 (alternating series with decreasing terms); Re g -> -a ln2 (b<<a), Im g -> -b ln2 (a<<b);
(iii) g is homogeneous of degree one: g(la,lb) = l g(a,b)."""
import mpmath as mp, numpy as np, sys
mp.mp.dps = 50
DEL = mp.mpf('1e-8')

def integrand(s, a, b):
    return a * b / (mp.sinh(a * s) * mp.sin(b * s)) - 1 / s ** 2

def g_ray(a, b, th):
    ph = mp.expjpi(-th / mp.pi)          # e^{-i th}
    f = lambda r: integrand(r * ph, a, b) * ph
    # split at small r to avoid cancellation, then [0.5, inf)
    L = 60 / (a * mp.cos(th) + b * mp.sin(th))
    pts = [DEL, 0.5 / max(a, b), 2 / max(a, b)] + [k * L / 12 for k in range(1, 13)] + [mp.inf]
    pts = sorted(set(pts))
    return mp.quad(f, pts) + ph * (b ** 2 - a ** 2) / 6 * DEL

def re_g_series(a, b):
    return mp.pi * b * S(b / a)

def S(r):
    return mp.nsum(lambda n: (-1) ** int(n) / mp.sinh(n * mp.pi * r), [1, mp.inf])

def g_closed(a, b):
    return mp.pi * (b * S(b / a) + 1j * a * S(a / b))

if __name__ == "__main__":
    print("ray independence of g(a,b) (a=0.7,b=1.3) and comparison with the closed form:")
    a, b = mp.mpf('0.7'), mp.mpf('1.3')
    for th in [0.15, 0.5, 0.9, 1.3]:
        print("   theta=%.2f  g = %s" % (th, mp.nstr(g_ray(a, b, th), 14)))
    print("   closed form g = %s" % mp.nstr(g_closed(a, b), 14))
    print()
    print("table: a, b, g (ray th=0.6), closed form, abs. difference")
    for (a, b) in [(1, 0.05), (1, 0.3), (1, 1), (1, 2), (0.5, 3), (0.2, 3), (0.1, 4), (3, 0.5), (1, 1 / 0.2), (1, 1 / 1.7)]:
        a, b = mp.mpf(a), mp.mpf(b)
        gr = g_ray(a, b, 0.6); gc = g_closed(a, b)
        print("  a=%.2f b=%.3f  g_ray = % .12f %+.12fi   closed = % .12f %+.12fi   |diff| = %.1e" % (a, b, mp.re(gr), mp.im(gr), mp.re(gc), mp.im(gc), abs(gr - gc)))
    print()
    print("homogeneity g(l a, l b) = l g(a,b):")
    a, b = mp.mpf('0.7'), mp.mpf('1.3')
    g1 = g_ray(a, b, 0.6)
    for l in [0.5, 2.0, 5.0]:
        print("   l=%.1f  g(l a,l b)/(l g(a,b)) = %s" % (l, mp.nstr(g_ray(l * a, l * b, 0.6) / (l * g1), 12)))
    print()
    print("limits: Re g/(-a) -> ln 2 =", mp.nstr(mp.log(2), 12), " ; (a=1,b=1e-3):", mp.nstr(-re_g_series(mp.mpf(1), mp.mpf('1e-3')), 10))
    print("sign scan of Re g and Im g over r=b/a (a=1):")
    rows = []
    for r in [1e-3, 1e-2, 0.1, 0.3, 1, 3, 10, 30, 100]:
        gc = g_closed(mp.mpf(1), mp.mpf(r))
        rows.append((r, mp.re(gc), mp.im(gc)))
        print("   r=%-7g Re g = % .6e   Im g = % .6e" % (r, mp.re(gc), mp.im(gc)))
    print("   all Re g < 0:", all(x[1] < 0 for x in rows), "; all Im g < 0:", all(x[2] < 0 for x in rows))
