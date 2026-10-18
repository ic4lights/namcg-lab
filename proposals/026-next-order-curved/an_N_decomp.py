"""Decompose N^sigma_{mu nu} = Theta^{rho sigma} d_rho Theta^{mu nu} into so(4) irreps on (a) SU(2) family at several u (on-shell),
(b) random Poisson (off-shell). Report: |J|, totally antisymmetric part (Jacobi => 0), SD/ASD split l_sigma, r_sigma,
W_4 = tr_V (B.B)^2 - n_D tr_D (B.B)^2, and compare with sum_w tr E^2 from the heat-kernel operators."""
import random
import numpy as np
import sympy as sp
import jetlib as jl
from jetlib import Jet
from common import *
import geom, sd_family, su2_family as F
import lib

def Nsig_from_Theta_numeric(Th):
    N = np.zeros((4, 4, 4))   # N[s, m, n]
    for s in range(4):
        for m in range(4):
            for n in range(4):
                v = sum((Th[r][s]*Th[m][n].diff(r) for r in range(4)), Jet()).c0()
                N[s, m, n] = float(getattr(v, 'x', v))
    return N

eta = [np.array(e.tolist(), dtype=float) for e in lib.eta3()]
etab = [np.array(e.tolist(), dtype=float) for e in lib.etabar()]

def decompose(N):
    # trace J_nu = sum_m N[m, m, nu]*(+/-)  (J_nu = Theta^{m rho} d_rho Theta^{m nu} = sum_m N[m, m, nu] with N[s,m,n] = Theta^{rho s} d_rho Theta^{mn}, careful sign)
    # Theta^{m rho} d_rho Theta^{m nu} = - Theta^{rho m} d_rho Theta^{m nu} = - N[m, m, nu]
    Jv = -np.array([sum(N[m, m, n] for m in range(4)) for n in range(4)])
    totanti = np.zeros(4)
    for s in range(4):
        pass
    A = np.zeros((4, 4, 4))
    for s in range(4):
        for m in range(4):
            for n in range(4):
                A[s, m, n] = (N[s, m, n] + N[m, n, s] + N[n, s, m])/3
    # SD/ASD parts of each N^s (as 2-form in mn): l_s^k = 1/4 eta^k_{mn} N^s_{mn}, r_s^k = 1/4 etabar^k_{mn} N^s_{mn}
    l = np.array([[0.25*np.sum(eta[k]*N[s]) for k in range(3)] for s in range(4)])
    r = np.array([[0.25*np.sum(etab[k]*N[s]) for k in range(3)] for s in range(4)])
    return Jv, np.abs(A).max(), l, r

def W4(l, r):
    K = l.T @ r
    return 0.5*np.sum(l*l)*np.sum(r*r) + np.sum(K*K)

use_gaussian(3)
# (a) SU(2) family: need numeric Theta jets at x0=(r0,0,0,0) with numeric h-jets on-shell; use Q field (Fraction) -> use QQ_I with rational u
print('--- SU(2) family on-shell (r0=h0=1) ---')
from sympy import QQ
for uval in (sp.Rational(-1, 2), sp.Rational(-1), sp.Rational(-3), sp.Rational(1), sp.Rational(0), sp.Rational(-4)):
    u = uval
    h1 = u; h2 = -u*(u**2 + 4*u + 10)/2; h3 = 3*u*(u**4 + 8*u**3 + 26*u**2 + 40*u + 40)/4
    jl.set_field(QQ_I(1), QQ_I(0)); jl.set_order(3)
    K = QQ_I
    # build omega with numeric h-jets using su2_family with K=QQ_I and numeric syms
    Kd = QQ_I
    syms = (sp.Integer(1), sp.Integer(1), h1, h2, h3)
    # su2_family uses K.convert; for QQ_I use K.from_sympy
    class Wrap:
        one = QQ_I(1); zero = QQ_I(0)
        @staticmethod
        def convert(x): return QQ_I.from_sympy(sp.Rational(x))
    w = F.omega_jets_su2(Wrap, syms)
    geom.SIGN_OVERRIDE = None
    Th = theta_from_omega(w)
    N = Nsig_from_Theta_numeric(Th)
    Jv, anti, l, r = decompose(N)
    print('u=%s  |J|=%.3e  max|N_[s,mn]|=%.3e  |l|^2=%.4f |r|^2=%.4f  W4=%.5f' % (u, np.linalg.norm(Jv), anti, np.sum(l*l), np.sum(r*r), W4(l, r)))
