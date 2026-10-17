"""023 script 10: local window analysis for R_kappa = kappa*C42 - C41 (positive principal symbol A_kappa = K41 - kappa*K42 = -sigma(Delta_kappa); convention: sigma(.) = quadratic form sum w (xi.v)^2 = minus the principal symbol, K_i = sigma(C_i), kappa in (1/2,1)).
(a) Lorentzian four-matrix symbol K_H = sum eta_a v_{a4}^2 against the window: generalised eigenvalues of (K_H, A_kappa) (3 positive, 1 negative, 2 zero), vs (y^4)^2.
(b) Euclid-contracted model (eta -> delta, as in 020): Zeeman depth |f1-f2| over the centre variable zeta with A_kappa(zeta) <= Lambda^2:  d_* = max_zeta |f1-f2| / sqrt(A_kappa(zeta)).
(c) window volume factor det(A_kappa)^(-1/2) against the closed form [(kappa-1/2)^2 (1-kappa)]^(-1) * const."""
import numpy as np, scipy.linalg as sl
from symbol_tools import *
from sym_signatures import forms, sig
rng = np.random.default_rng(41)
eta4 = [-1, 1, 1, 1]
def build(M0):
    V = {p: vec(M0, *p) for p in pairs}
    eta = lambda p: eta6[p[0], p[0]] * eta6[p[1], p[1]]
    K = lambda sel: sum(eta(p) * np.outer(V[p], V[p]) for p in pairs if sel(p))
    return V, K(lambda p: p[1] <= 4), K(lambda p: True)
kap = 0.75
print("(a) generalised eigenvalues of (K_H^{Lorentz}, A_kappa), kappa = 0.75; columns: (y^4)^2, ell^2, negative eigenvalue, positive ones")
rows = []
for t in range(8):
    z = rand_z_pos(rng, rng.uniform(0.5, 4)); M0 = Mfun(z)
    y = M0[:5, 5]; y4 = y[4]; e5 = np.diag([-1., 1, 1, 1, 1]); ell2 = -(y @ e5 @ y)
    rk, F = forms(M0)
    A = F['C41'] - kap * F['C42']
    ev = np.sort(np.real(sl.eig(F['Box4'], A)[0]))
    print("   %8.4f %8.4f   %s" % (y4 ** 2, ell2, np.round(ev, 4)))
print("(b) Euclid-contracted Zeeman depth d_* (|f1-f2| per sqrt(A_kappa)), kappa = 0.75, and f2/f1 range")
for t in range(6):
    z = rand_z_pos(rng, rng.uniform(0.5, 4)); M0 = Mfun(z)
    V, K41, K42 = build(M0)
    A15 = K41 - kap * K42
    sym = symbol(M0, [(a, 4) for a in range(4)], [1.0] * 4)
    c, Fh, Z = sym['c'], sym['F'], sym['Z']
    S = np.einsum('Ii,ijk,Jj->IJk', c, Fh, c)
    best = 0; rr = []
    for th in np.linspace(0, np.pi, 91):
        zeta = np.array([np.cos(th), np.sin(th)])
        p = Z.T @ zeta
        nrm = np.sqrt(p @ A15 @ p)
        Fab = np.einsum('abk,k->ab', S, zeta)
        f1, f2, pp, rr_ = planes(Fab)
        best = max(best, abs(f1 - f2) / nrm); rr.append(f2 / f1 if f1 > 0 else 1)
    print("   d_* = %.4f   f2/f1 in [%.3f, %.3f]" % (best, min(rr), max(rr)))
print("(c) det(A_kappa) ratios vs closed form 1/[(kappa-1/2)^2 (1-kappa)]  (volume factor of the window {A<=Lambda^2} up to a kappa-independent factor)")
z = rand_z_pos(rng, 1.3); M0 = Mfun(z); rk, F = forms(M0)
ref = None
for k in [0.55, 0.65, 0.75, 0.85, 0.95]:
    d = np.linalg.det(F['C41'] - k * F['C42']); val = d ** -0.5
    cf = 1 / ((k - 0.5) ** 2 * (1 - k)) ** 1  # det ~ (k-1/2)^4 (1-k)^2 -> det^(-1/2) ~ (k-1/2)^-2 (1-k)^-1
    if ref is None: ref = val / cf
    print("   kappa=%.2f  det^(-1/2)=%.4f  closed form*const=%.4f" % (k, val, ref * cf))
