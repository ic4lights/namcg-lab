#!/usr/bin/env python3
"""N=2 reduced engine for the regulated Lorentzian integral with the observable Tr exp(i kappa A_0).

Conventions (as in proposals/053-lorentzian-integral-limit-order/n2_reduced.py, re-implemented here so that this
folder is self-contained):
  A_mu = sum_a A_mu^a sigma^a/2, a = (A_0^a) in R^3, B = (A_i^a) in R^{9x3}, W = B^T B, G = W - a a^T.
  S_b = lam e2(G), lam = 1/(4 g^2) = 1/2.  Pf = c_P det(G)^4 (D = 10).  Regulator eps(|a|^2 + tr W)
  (this is eps' sum_mu Tr A_mu^2 with eps' = 2 eps; limits eps -> 0 are unaffected).
  Tr exp(i kappa A_0) = 2 cos(kappa sqrt(a.a)/2), a.a the bilinear (not Hermitian) square, entire in a.
Contour (alpha, beta): a = e^{-i alpha} at, B = e^{i beta} Bt.  R_u is alpha = 3 pi u/8, beta = pi u/8.
On it sqrt(a.a) = e^{-i alpha} |at|, so the observable is 2 cos(zeta |at|) with zeta = kappa e^{-i alpha}/2.
For each W (diagonal, ordered w1>=w2>=w3) the at-integral
    A(zeta) = int d^3at exp(-sum_k Q_k at_k^2) (D0 - sum_k C_k at_k^2)^4 2 cos(zeta |at|)
is done in polar coordinates: the radial integral is closed form,
    int_0^inf r^{2+2j} e^{-q r^2} cos(zeta r) dr = (1/2) Gamma(j+3/2) q^{-(j+3/2)} e^{-y} 1F1(-j-1; 1/2; y),
    y = zeta^2/(4q)   (Kummer transformation; valid for Re q > 0, principal branch),
and the angular integral is a product Gauss-Legendre rule on one octant (log theta, phi).
"""
import numpy as np, math
from scipy.special import gamma as Gam
LAM = 0.5
D, d, P = 10, 9, 4

def nodes(n, lo, hi):
    x, w = np.polynomial.legendre.leggauss(n)
    return 0.5*(hi-lo)*x+0.5*(hi+lo), 0.5*(hi-lo)*w

def kummer_coeffs(j):
    n = j+1
    c = []
    for m in range(n+1):
        num = 1.0
        for i in range(m):
            num *= (-n+i)
        den = 1.0
        for i in range(m):
            den *= (0.5+i)
        c.append(num/(den*math.factorial(m)))
    return c
KC = [kummer_coeffs(j) for j in range(P+1)]
GJ = [0.5*Gam(j+1.5) for j in range(P+1)]
BIN = [math.comb(P, j) for j in range(P+1)]

class Angles:
    def __init__(self, nth=40, nph=10, thmin=1e-8):
        v, wv = nodes(nth, math.log(thmin), math.log(math.pi/2))
        th = np.exp(v); wth = wv*th*np.sin(th)
        ph, wph = nodes(nph, 0.0, math.pi/2)
        TH, PH = np.meshgrid(th, ph, indexing='ij')
        self.x1 = np.cos(TH).ravel()**2
        self.x2 = (np.sin(TH)*np.cos(PH)).ravel()**2
        self.x3 = (np.sin(TH)*np.sin(PH)).ravel()**2
        self.w = 8.0*(wth[:, None]*wph[None, :]).ravel()

def a_integral(Q, Cc, D0, zetas, ang):
    """Q, Cc: lists of 3 arrays (n,), D0: (n,).  Returns array (len(zetas), n)."""
    q = Q[0][:, None]*ang.x1+Q[1][:, None]*ang.x2+Q[2][:, None]*ang.x3
    C = Cc[0][:, None]*ang.x1+Cc[1][:, None]*ang.x2+Cc[2][:, None]*ang.x3
    D0b = D0[:, None]
    lq = np.log(q)
    pre = [BIN[j]*D0b**(P-j)*(-C)**j*GJ[j]*np.exp(-(j+1.5)*lq) for j in range(P+1)]
    Sm = []
    for m in range(P+2):
        acc = 0
        for j in range(P+1):
            if m < len(KC[j]):
                acc = acc+KC[j][m]*pre[j]
        Sm.append(acc)
    out = []
    for zeta in zetas:
        if zeta == 0:
            tot = Sm[0]
        else:
            y = zeta**2/(4*q)
            tot = Sm[P+1]
            for m in range(P, -1, -1):
                tot = tot*y+Sm[m]
            tot = tot*np.exp(-y)
        out.append(2.0*(tot@ang.w))
    return np.array(out)

def a_integral_zero_exact(Q, Cc, D0):
    """Gaussian-moment formula for int d^3at exp(-sum Q at^2)(D0 - sum C at^2)^4 (no observable), times 2."""
    tot = 0
    import itertools
    for n in itertools.product(range(P+1), repeat=3):
        if sum(n) > P:
            continue
        n0 = P-sum(n)
        coef = math.factorial(P)/(math.factorial(n0)*math.factorial(n[0])*math.factorial(n[1])*math.factorial(n[2]))
        mono = coef*D0**n0
        for k in range(3):
            mono = mono*(-Cc[k])**n[k]*Gam(n[k]+0.5)*Q[k]**(-(n[k]+0.5))
        tot = tot+mono
    return 2.0*tot

def _chunk(args):
    (S, V, Zg, Wt, eps, alpha, beta, zetas, angpar, check_zero) = args
    ang = Angles(*angpar)
    w1 = np.exp(S); w2 = w1*np.exp(-V); w3 = w2*np.exp(-Zg)
    jac = w2*w3
    Vd = (w1-w2)*(w1-w3)*(w2-w3)
    dens = Wt*jac*Vd*(w1*w2*w3)**((d-4)/2)
    T = w1+w2+w3; e2 = w1*w2+w1*w3+w2*w3
    ex = np.exp(1j*LAM*np.exp(4j*beta)*e2-eps*np.exp(2j*beta)*T)
    sk = [w2+w3, w1+w3, w1+w2]
    Q = [np.exp(-2j*alpha)*(eps+1j*LAM*np.exp(2j*beta)*sk[k]) for k in range(3)]
    D0 = np.exp(6j*beta)*w1*w2*w3
    pref = np.exp(-2j*alpha+4j*beta)
    Cc = [pref*w2*w3, pref*w1*w3, pref*w1*w2]
    with np.errstate(over='ignore', invalid='ignore'):
        A = a_integral(Q, Cc, D0, zetas, ang)
    r = A@(dens*ex)
    r0 = np.sum(a_integral_zero_exact(Q, Cc, D0)*dens*ex) if check_zero else 0j
    return r, r0

_POOL = None
def pool(n=None):
    global _POOL
    if _POOL is None:
        import multiprocessing as mp
        _POOL = mp.Pool(n or max(1, mp.cpu_count()-2))
    return _POOL

def integrate(kappas, eps, alpha, beta, ns=160, nv=60, nz=60, srange=(-8.0, 13.0), vmax=32., zmax=32.,
              angpar=(30, 8), chunk=2000, check_zero=False, parallel=True):
    """Returns (Z2, N) with N[i] = int 2cos(kappa_i sqrt(a.a)/2) x weight on the contour (alpha, beta) and
    Z2 = int 2 x weight (same rules).  So <Tr e^{i kappa A_0}> = 2 N/Z2.  kappas may be complex."""
    zetas = [0]+[k*np.exp(-1j*alpha)/2 for k in kappas]
    s, ws = nodes(ns, *srange); v, wv = nodes(nv, 0.0, vmax); z, wz = nodes(nz, 0.0, zmax)
    S, V, Zg = np.meshgrid(s, v, z, indexing='ij')
    Wt = (np.exp(s)*ws)[:, None, None]*wv[None, :, None]*wz[None, None, :]
    S = S.ravel(); V = V.ravel(); Zg = Zg.ravel(); Wt = Wt.ravel()
    jobs = [(S[i:i+chunk], V[i:i+chunk], Zg[i:i+chunk], Wt[i:i+chunk], eps, alpha, beta, zetas, angpar, check_zero)
            for i in range(0, len(S), chunk)]
    outs = pool().map(_chunk, jobs) if parallel else [_chunk(j) for j in jobs]
    res = sum(o[0] for o in outs); r0 = sum(o[1] for o in outs)
    ph = np.exp(1j*(3*d*beta-3*alpha))
    res = res*ph; r0 = r0*ph
    if check_zero:
        return res[0], res[1:], r0
    return res[0], res[1:]

def Ru(u):
    return 3*np.pi*u/8, np.pi*u/8
