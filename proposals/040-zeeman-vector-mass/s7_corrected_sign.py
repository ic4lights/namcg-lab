"""032 script 7: Landau-resummed kappa^2 response of  i int ds Tr e^{-isH}  (mass-linear term) to a plane-wave vielbein (EH sector) and to a plane-wave gauge field (Maxwell sector),
multiprecision, exact in the constant flux (a,b)=(f_e,f_m).  Covariance test: the SAME (a,b) with the data (kappa, alpha, y) rotated by random Lorentz transformations
(kappa, alpha covectors: L^{-T}; y vector: L), which leaves A, G and every F-independent invariant unchanged.
Output per case: Fin_EH = lim [ int_{s0}^inf T2_EH ds - c ln(1/s0) ] (c = A/16pi^2, ray s = rho e^{-i th}), and  int T2_Maxwell ds.
T2 = Theta(s) * k2coef."""
import numpy as np, mpmath as mp, sys, time
from engine_mp import *
mp.mp.dps = 40
TH = mp.mpf('0.6')
PH = mp.expj(-TH)
etan = np.diag([-1., 1, 1, 1])

def Theta(s, a, b):
    return -1j * a * b / (16 * mp.pi ** 2 * mp.sinh(s * a) * mp.sin(s * b))

def rand_lorentz(rng):
    from scipy.linalg import expm
    gens = []
    for i in range(1, 4):
        B = np.zeros((4, 4)); B[0, i] = B[i, 0] = 1; gens.append(B)
    for (i, j) in [(1, 2), (1, 3), (2, 3)]:
        R = np.zeros((4, 4)); R[i, j] = 1; R[j, i] = -1; gens.append(R)
    return expm(sum(rng.normal() * 0.5 * g for g in gens))

def glnodes(lo, hi, nn=8):
    x, w = np.polynomial.legendre.leggauss(nn)
    return [(mp.mpf((hi - lo) / 2 * (xx + 1) + lo), mp.mpf(ww * (hi - lo) / 2)) for xx, ww in zip(x, w)]

def integrate(fun, rho1, rho_max, c):
    """returns (int_0^{s1}(T2 - c/s) ds - c ln s1 + int_{s1}^{inf} T2 ds) along the ray"""
    tot = mp.mpc(0)
    for r, w in glnodes(0, rho1, 8):
        s = r * PH
        tot += w * PH * (fun(s) - c / s)
    tot += c * mp.log(rho1 * PH)
    edges = [rho1 * (rho_max / rho1) ** (k / 6) for k in range(7)]
    for lo, hi in zip(edges[:-1], edges[1:]):
        for r, w in glnodes(lo, hi, 8):
            tot += w * PH * fun(r * PH)
    return tot

def case(a, b, kappa, alpha, y, cch=0.8):
    m = -np.outer(alpha, y); n = -alpha * cch
    al_up = etan @ alpha
    A = (1 / 24) * ((y @ etan @ y) * ((kappa @ al_up) ** 2 - (kappa @ etan @ kappa) * (alpha @ al_up)) - 2 * (kappa @ etan @ kappa) * (alpha @ y) ** 2)
    c = mp.mpf(A) / (16 * mp.pi ** 2)
    mm = to_mp_mat(m); nn_ = to_mp_vec(n); z4 = to_mp_vec(np.zeros(4)); z44 = to_mp_mat(np.zeros((4, 4)))
    fEH = lambda s: Theta(s, a, b) * k2coef(a, b, kappa, mm, z4, s, nquad=10, lam=mp.mpf('1e-12'))
    fMX = lambda s: Theta(s, a, b) * k2coef(a, b, kappa, z44, nn_, s, nquad=10, lam=mp.mpf('1e-12'))
    rho1 = mp.mpf('0.05') / max(a, b)
    rho_max = 22 / (a * mp.cos(TH) + b * mp.sin(TH))
    return A, integrate(fEH, rho1, rho_max, c), integrate(fMX, rho1, rho_max, 0)

if __name__ == "__main__":
    rng = np.random.default_rng(11)
    kappa0 = rng.normal(size=4); alpha0 = rng.normal(size=4)
    kup = etan @ kappa0
    y0 = rng.normal(size=4); y0 = y0 - kup * (y0 @ kappa0) / (kup @ kappa0)
    cases = [(0.7, 1.3), (float(1 / np.sinh(0.5)), 1.0), (float(1 / np.sinh(1.5)), 1.0)]
    nfr = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    for (a, b) in cases:
        print("\n=== (a,b) = (%.4f, %.4f)  a/b = %.4f   decay rate on ray: %.3f" % (a, b, a / b, a * np.cos(0.6) + b * np.sin(0.6)), flush=True)
        for fr in range(nfr):
            L = np.eye(4) if fr == 0 else rand_lorentz(rng)
            Li = np.linalg.inv(L)
            kappa = Li.T @ kappa0; alpha = Li.T @ alpha0; y = L @ y0
            t = time.time()
            A, fin, mx = case(a, b, kappa, alpha, y)
            c = A / (16 * np.pi ** 2)
            print("  frame %d: A=%.6f  c=A/16pi^2=%.6e  Fin_EH=%s  Fin_EH/c=%s   int T2_Maxwell=%s   [%.0fs]" % (fr, A, c, mp.nstr(fin, 8), mp.nstr(fin / c, 8), mp.nstr(mx, 8), time.time() - t), flush=True)
