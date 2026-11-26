"""s2: constant term of the heat trace of the 2d cone of angle 2*pi*n with a holonomy phase exp(2*pi*i*a) around the tip.

Orders nu_m = |m+a|/n, m in Z.  Numerical:   C(n,a) = (1/2) int_0^inf dx [ e^{-x} sum_m I_{nu_m}(x) - n ]
(per component; the volume term n*V/(4 pi s) is removed; Tr_1 on the plane gives sum_m e^{-x} I_{|m|}(x) = 1).
Prediction (zeta-regularised sum of Bessel orders, B_2(a)=a^2-a+1/6, 0<=a<=1):
    C(n,a) = B_2(a)/(2n) - n/12 .
Checks: a=0 gives (1/12)(1/n - n) (flat cone); n=1 gives -a(1-a)/2 (Aharonov-Bohm).
First-order consequence used in the proposal: for n=1-eps, a = alpha*eps (eps>0 or <0):
    C = (1/12)(1/n - n) - |alpha eps|/2 + O(eps^2),   i.e. a change -|alpha|/2 *eps*sgn per twisted component.
"""
import numpy as np
from scipy.special import ive
from scipy.integrate import quad

def C_num(n, a, M=600, X=80.0):
    ms = np.arange(-M, M+1)
    nu = np.abs(ms + a)/n
    def f(x):
        return 0.5*(np.sum(ive(nu, x)) - n)
    pts = [0.5, 1, 2, 5, 10, 20, 40]
    tot = 0.0
    edges = [0.0] + pts + [X]
    for lo, hi in zip(edges[:-1], edges[1:]):
        v, _ = quad(f, lo, hi, limit=400)
        tot += v
    return tot

def B2(a):
    return a*a - a + 1.0/6.0

def C_pred(n, a):
    a = a % 1.0
    return B2(a)/(2*n) - n/12.0

print("   n      a        numeric        predicted      diff")
for n, a in [(1.0, 0.0), (0.5, 0.0), (2.0, 0.0), (3.0, 0.0), (1.0, 0.3), (1.0, 0.5), (1.0, 0.8),
             (0.5, 0.3), (2.0, 0.3), (2.0, 0.75), (0.9, 0.1), (1.1, 0.1)]:
    cn = C_num(n, a); cp = C_pred(n, a)
    print(f"{n:5.2f} {a:6.2f} {cn:14.8f} {cp:14.8f} {cn-cp:10.2e}")

print("\nFirst order in eps = 1-n at fixed alpha (twist a=alpha*|eps| for the component with J-eigenvalue +-1):")
for eps in [0.02, -0.02]:
    n = 1 - eps
    for alpha in [0.0, 1.0, 2.0]:
        a = abs(alpha*eps)
        base = (1/n - n)/12
        shift = C_pred(n, a) - C_pred(n, 0.0)
        print(f" eps={eps:+.2f} alpha={alpha}: shift/eps = {shift/eps:+.4f}   (-alpha*sgn(eps)/2 = {-alpha*np.sign(eps)/2:+.4f}); base/eps={base/eps:.4f} (1/6={1/6:.4f})")
