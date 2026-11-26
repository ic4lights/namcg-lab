"""034 script 1: the Jacobi identity [W_a, Y] = sigma q_a V on the leaf, and what it fixes in the nilpotent model.
Checks at random orbit points / random q:
 (a) kappa_a = W_a(phi) = sigma m q_a with sigma = +-1, m = M^{45}   (conformal flatness of the base: K^{mu nu} = m^2 eta^{mu nu});
 (b) y^c kappa_c = 0   (Y(phi) = 0);
 (c) [W_a, Y] = sigma_B q_a V as vector fields (full 6-vectors);
 (d) the decomposition  [W_a,Y] = y^c [W_a,W_c] + (W_a y^c) W_c + ...  : the centre (weight-2) part gives
        y^c S_ac^k = sigma_B q_a v^k         (Jacobi-fixed alignment of the flux with the plane-wave vector),
     i.e. F_ac(zeta) y^c = - sigma_B q_a nu_c(zeta), nu_c = v^k zeta_k  for every centre variable zeta,
     where F_ab = -S_ab^k zeta_k.   Reported: residual of the alignment, and the same quantity for a RANDOM Lorentz frame of F, kappa, y (what the unconstrained Landau model of 032 assumed).
 (e) V(phi) = v^c kappa_c  and  Z_k(phi) = 0.
"""
import numpy as np
from leafdata import *
rng = np.random.default_rng(7)
print("point | sigma(kappa=sigma m q) | |y.kappa| | |[W_a,Y]-sB q_a V| | alignment resid |y^c S_ac^k - sB q_a v^k| (rel) | random-frame misalignment (rel)")
for t in range(8):
    M0 = rand_point(rng); q = rng.normal(size=4)
    d = leaf_data(M0, q)
    m = M0[4, 5]
    kap = d['kappa']
    qup = eta_a * q
    sig = kap @ qup / (m * (qup @ qup))
    resA = np.abs(kap - sig * m * qup).max()
    y = d['y']; yk = d['yk']
    res_b = abs(y @ kap)
    # (c) [W_a,Y] = sB q_a V (6-vectors)
    WY = np.array([sum(q[mu] * bracket_field(M0, d['E'], (a, 4), (mu, 5)) for mu in range(4)) for a in range(4)])
    # find sB by least squares
    num = sum(WY[a] @ (qup[a] * d['Vv']) for a in range(4)); den = sum((qup[a] * d['Vv']) @ (qup[a] * d['Vv']) for a in range(4))
    sB = num / den
    resc = max(np.abs(WY[a] - sB * qup[a] * d['Vv']).max() for a in range(4))
    # (d) centre part
    S = d['S']; v_k = d['vk']
    lhs = np.einsum('c,ack->ak', y, S)            # y^c S_{ac}^k
    rhs = sB * np.outer(qup, v_k)
    ali = np.abs(lhs - rhs).max() / max(np.abs(lhs).max(), 1e-30)
    # random-frame comparison: replace y by a random vector orthogonal-to-kappa (as in 032 s7) and keep S, q
    yr = rng.normal(size=4); kup = etan @ kap; yr = yr - kup * (yr @ kap) / (kup @ kap)
    lhsr = np.einsum('c,ack->ak', yr, S)
    mis = np.abs(lhsr - sB * np.outer(qup, v_k * (np.linalg.norm(yr) / np.linalg.norm(y)))).max() / np.abs(lhsr).max()
    # (e)
    resV = abs(d['Vv'] @ d['dphi'] - d['v'] @ kap)
    resZ = np.abs(d['fr']['Z'] @ d['dphi']).max()
    print("%d | sigma=%+.0f resid %.1e | %.1e | %.1e (sB=%+.0f) | %.1e | %.2f   (V(phi) test %.1e, Z(phi) %.1e)" % (t, sig, resA, res_b, resc, sB, ali, mis, resV, resZ))
print("\nweight-1 part of [W_a,Y] (dropped in the nilpotent model) vs weight-2 part, point 0:")
M0 = rand_point(np.random.default_rng(7)); q = np.random.default_rng(8).normal(size=4)
d = leaf_data(M0, q)
for a in range(4):
    hc, vc = d['WY'][a]
    print("  a=%d  horizontal coefficients of [W_a,Y]: %s   vertical: %s" % (a, np.round(hc, 4), np.round(vc, 4)))
