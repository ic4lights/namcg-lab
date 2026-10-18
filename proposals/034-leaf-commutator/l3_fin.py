"""034 script 3 (library): proper-time integral of the kappa^2 coefficient of the second-order response on the leaf, central-Y model (corrected) and interleaved model (032 form), same data.
Theta(s) = -i a b / (16 pi^2 sinh(s a) sin(s b)).   T2(s) = Theta(s) * k2coef.   Ray s = rho e^{-i th}.  Fin = lim [ int_{s0}^inf T2 ds - c ln(1/s0) ], c = A/(16 pi^2)."""
import numpy as np, mpmath as mp, sys, time
sys.dont_write_bytecode = True
from leafdata import *
from canon import canonical
from engine_e_mp import k2coef_e
import engine_mp as emp
mp.mp.dps = 40
TH = mp.mpf('0.6'); PH = mp.expj(-TH)
def Theta(s, a, b):
    return -1j * a * b / (16 * mp.pi ** 2 * mp.sinh(s * a) * mp.sin(s * b))
def glnodes(lo, hi, nn=8):
    x, w = np.polynomial.legendre.leggauss(nn)
    return [(mp.mpf((hi - lo) / 2 * (xx + 1) + lo), mp.mpf(ww * (hi - lo) / 2)) for xx, ww in zip(x, w)]
def integrate(fun, rho1, rho_max, c, nn=8, nint=6):
    tot = mp.mpc(0)
    for r, w in glnodes(0, rho1, nn):
        s = r * PH
        tot += w * PH * (fun(s) - c / s)
    tot += -c * mp.log(rho1 * PH)
    edges = [rho1 * (rho_max / rho1) ** (k / nint) for k in range(nint + 1)]
    for lo, hi in zip(edges[:-1], edges[1:]):
        for r, w in glnodes(lo, hi, nn):
            tot += w * PH * fun(r * PH)
    return tot
def A_engine(alpha, kappa, y):
    al_up = etan @ alpha
    return (1 / 24) * ((y @ etan @ y) * ((kappa @ al_up) ** 2 - (kappa @ etan @ kappa) * (alpha @ al_up)) - 2 * (kappa @ etan @ kappa) * (alpha @ y) ** 2)
def canonical_data(d, zeta, alpha):
    S, y, yk, kappa = d['S'], d['y'], d['yk'], d['kappa']
    F = -np.einsum('abk,k->ab', S, zeta)
    c0 = float(yk @ zeta)
    a, b, C, Bm, Fc = canonical(F)
    return dict(a=a, b=b, kappa=Bm @ kappa, alpha=Bm @ alpha, y=C.T @ y, c0=c0, Fc=Fc)
def fin_case(cd, model='central', nquad=10, nn=8, nint=6, lam=mp.mpf('1e-12'), rho_scale=22):
    a, b = mp.mpf(cd['a']), mp.mpf(cd['b'])
    kappa, alpha, y, c0 = cd['kappa'], cd['alpha'], cd['y'], cd['c0']
    A = A_engine(alpha, kappa, y)
    c = mp.mpf(A) / (16 * mp.pi ** 2)
    if model == 'central':
        f = lambda s: Theta(s, a, b) * k2coef_e(a, b, kappa, alpha, y, c0, s, nquad=nquad, lam=lam)
    else:
        m = -np.outer(alpha, y); n = -alpha * c0
        mm = emp.to_mp_mat(m); nn_ = emp.to_mp_vec(n)
        f = lambda s: Theta(s, a, b) * emp.k2coef(a, b, kappa, mm, nn_, s, nquad=nquad, lam=lam)
    rho1 = mp.mpf('0.05') / max(a, b)
    rho_max = rho_scale / (a * mp.cos(TH) + b * mp.sin(TH))
    return A, c, integrate(f, rho1, rho_max, c, nn=nn, nint=nint), f
