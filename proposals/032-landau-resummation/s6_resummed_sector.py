"""032 script 6: Landau-resummed order-kappa^2 response of the mass-linear term  i int ds Tr e^{-isH}  to a plane-wave vielbein (EH sector, m = -alpha y^T),
gauge (Maxwell sector, n = -alpha c) and mixed perturbation, exact in the constant flux F=(a,b) in a random Lorentz frame.
T2(s) = Theta(s) * [kappa^2-coefficient of second_order]; ray s = rho e^{-i th}.
Reports: (1) UV log coefficient c = A/(16 pi^2) (flux independent); (2) large-rho decay; (3) finite part Fin of  int_{s0}^inf T2 ds - c ln(1/s0)  for the EH piece and
its dependence on the Lorentz frame of F at fixed (a,b) (covariance test); (4) the Maxwell piece  int T2 ds  (finite, ~1/f) and the sign of its quadratic form."""
import numpy as np, sys
from engine import *
from s5_engine_checks import rand_F, rand_perp, theta_F
import s5_engine_checks as C5
th = 0.6
ph = np.exp(-1j * th)
LAM = [0.03, 0.06, 0.09, 0.12]

def k2(F, kappa, m, n, s):
    vals = [second_order(F, l * kappa, m, n, s, nquad=20) for l in LAM]
    cf = np.polyfit([l ** 2 for l in LAM], vals, 3)[-2]
    return theta_F(F, s) * cf

def ray_int(f, rho_max, nseg=6, nn=16):
    xs, ws = np.polynomial.legendre.leggauss(nn)
    edges = np.concatenate([[0], np.geomspace(rho_max / 200, rho_max, nseg)])
    tot = 0j
    for i in range(len(edges) - 1):
        lo, hi = edges[i], edges[i + 1]
        for x, w in zip(xs, ws):
            r = (hi - lo) / 2 * (x + 1) + lo
            tot += w * (hi - lo) / 2 * f(r) * ph
    return tot

def finite_part(F, kappa, m, n, c, a, b):
    rho1 = 0.05 / max(a, b)
    rho_max = 45 / (a * np.cos(th) + b * np.sin(th))
    reg = ray_int(lambda r: k2(F, kappa, m, n, r * ph) - c / (r * ph), rho1)      # int_0^{s1} (T2 - c/s) ds
    s1 = rho1 * ph
    tail = ray_int(lambda r: k2(F, kappa, m, n, (r + rho1) * ph), rho_max - rho1) if False else None
    # tail from rho1 to rho_max
    xs, ws = np.polynomial.legendre.leggauss(16)
    edges = np.geomspace(rho1, rho_max, 9)
    tail = 0j
    for i in range(len(edges) - 1):
        lo, hi = edges[i], edges[i + 1]
        for x, w in zip(xs, ws):
            r = (hi - lo) / 2 * (x + 1) + lo
            tail += w * (hi - lo) / 2 * k2(F, kappa, m, n, r * ph) * ph
    return reg - c * np.log(s1) + tail, tail

if __name__ == "__main__":
    rng = np.random.default_rng(3)
    kappa = rng.normal(size=4); alpha = rng.normal(size=4); y = rand_perp(kappa); cch = 0.8
    m = -np.outer(alpha, y); n = -alpha * cch
    al_up = eta @ alpha
    A = (1 / 24) * ((y @ eta @ y) * ((kappa @ al_up) ** 2 - (kappa @ eta @ kappa) * (alpha @ al_up)) - 2 * (kappa @ eta @ kappa) * (alpha @ y) ** 2)
    c = A / (16 * np.pi ** 2)
    print("A =", A, " UV log coefficient c = A/(16 pi^2) =", c)
    for (a, b) in [(0.7, 1.3), (1 / np.sinh(0.5), 1.0), (1 / np.sinh(1.5), 1.0)]:
        print("\n=== (a,b)=(%.3f,%.3f)  a/b=%.3f  theta*=arctan(a/b)=%.3f" % (a, b, a / b, np.arctan(a / b)))
        # (1)(2) small-s and decay of the EH piece in one frame
        F, L = rand_F(a, b)
        for rho in [1e-3, 1e-2, 0.05, 0.5, 2, 6, 12]:
            s = rho * ph / max(a, b) * max(a, b)
            t = k2(F, kappa, m, np.zeros(4), s)
            print("   rho=%-6g s*T2_EH = %s   (UV limit c = %.4e)   |T2_EH| = %.3e" % (rho, np.round(s * t, 8), c.real if isinstance(c, complex) else c, abs(t)))
        # (3) covariance test: finite part in several Lorentz frames
        fins = []
        for fr in range(4):
            F, L = rand_F(a, b)
            # keep (kappa, alpha, y) fixed: only the frame of F varies
            fin, tail = finite_part(F, kappa, m, np.zeros(4), c, a, b)
            fins.append(fin)
            print("   frame %d: Fin_EH = %s" % (fr, np.round(fin, 8)))
        print("   spread of Fin_EH over frames (rel. to c):", np.round(np.std(fins) / abs(c), 4))
        # Maxwell piece: integral and sign structure, 3 frames
        for fr in range(3):
            F, L = rand_F(a, b)
            fin, tail = finite_part(F, kappa, np.zeros((4, 4)), n, 0.0, a, b)
            print("   frame %d: int T2_Maxwell ds = %s" % (fr, np.round(fin, 8)))
