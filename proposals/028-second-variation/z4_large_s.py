"""028 script 5: large-proper-time growth of the order-Z^4 term (the s^4 (f_e^2+f_m^2)^2 character) in the Gaussian window at the leading symbol, A=0.
Flux: F_ab(xi) = xi . c[(a,b)] (lowered with eta), E_i=F_{0i}, B_i=(1/2) eps_ijk F_jk ; C(xi)=(E+iB).(E+iB), |C| = f_e^2+f_m^2 (checked against eigenvalues of eta F).
I(s) = (4pi)^-3 det(P+i s S)^(-1/2) s^4 < |C|^2 >_Gauss(covariance Gamma/2, Gamma=(P+isS)^-1).  Contour s = r e^{-i theta}.  Reports the log-slope d ln|I| / d ln r at large r:
slope 2 means the Schwinger integral int ds/s I(s) of this order diverges as r^2 (kernel-plane directions carry flux but no kinetic term)."""
import numpy as np, itertools
from geom28 import *
rng = np.random.default_rng(5)
eps3 = np.zeros((3, 3, 3))
for i, j, k in itertools.permutations(range(3)): eps3[i, j, k] = np.linalg.det(np.eye(3)[[i, j, k]])
def flux_vectors(M0):
    Pi, W, Yb, c, E = fields(M0)
    # F_ab = eta_aa eta_bb F^{ab},  F^{ab}(xi) = s xi.c[(a,b)] for a<b
    Fv = np.zeros((4, 4, 6))
    for a in range(4):
        for b in range(a + 1, 4):
            v = s*c[pidx[(a, b)]]*eta4[a, a]*eta4[b, b]
            Fv[a, b] = v; Fv[b, a] = -v
    Ev = np.array([Fv[0, i] for i in range(1, 4)])                       # (3,6)
    Bv = np.array([0.5*sum(eps3[i, j, k]*Fv[j + 1, k + 1] for j in range(3) for k in range(3)) for i in range(3)])
    return Fv, Ev, Bv, W, c
def fe_fm(F):
    ev = np.linalg.eigvals(eta4 @ F)
    return max(abs(ev.real)), max(abs(ev.imag))
def moment_abs2(Gam, u):
    """< |C|^2 > with C = xi^T Cm xi, Cm = sum_k u_k u_k^T (complex), conj(C)= xi^T conj(Cm) xi; Gaussian covariance Gam/2"""
    Cm = sum(np.outer(u[k], u[k]) for k in range(3)); Cc = Cm.conj()
    return 0.25*(np.trace(Cm @ Gam)*np.trace(Cc @ Gam) + 2*np.trace(Cm @ Gam @ Cc @ Gam))
if __name__ == "__main__":
    for t in range(4):
        z = rand_z_pos(rng, rng.uniform(0.6, 3)); M0 = Mfun(z)
        Fv, Ev, Bv, W, c = flux_vectors(M0)
        wf = window_forms(M0); P = wf['P']
        S = sum(eta4[a, a]*np.outer(W[a], W[a]) for a in range(4))
        # check |C| = fe^2+fm^2 on random xi
        xi = rng.normal(size=6)
        F = np.einsum('abk,k->ab', Fv, xi)
        fe, fm = fe_fm(F)
        Cval = sum((Ev[k] @ xi + 1j*(Bv[k] @ xi))**2 for k in range(3))
        # kernel plane of S
        w_, v_ = np.linalg.eigh(S); ker = v_[:, np.abs(w_) < 1e-9*np.abs(w_).max()]
        xk = ker @ rng.normal(size=ker.shape[1]); Fk = np.einsum('abk,k->ab', Fv, xk); fek, fmk = fe_fm(Fk)
        print("point %d: |C(xi)| = %.6f vs fe^2+fm^2 = %.6f ; on the kernel plane of S: fe=%.4f fm=%.4f (nonzero flux)" % (t, abs(Cval), fe**2 + fm**2, fek, fmk))
        u = np.array([Ev[k] + 1j*Bv[k] for k in range(3)])
        theta = np.pi/2 - 0.35
        rs = np.array([10., 30., 100., 300., 1000., 3000.])
        vals = []
        for r in rs:
            sc = r*np.exp(-1j*theta)
            A = P + 1j*sc*S
            Gam = np.linalg.inv(A)
            det = np.linalg.det(A)
            val = (4*np.pi)**-3*det**-0.5*sc**4*moment_abs2(Gam, u)
            vals.append(abs(val))
        sl = np.diff(np.log(vals))/np.diff(np.log(rs))
        print("   |I(s)| at r=", rs, ":", ["%.3e" % v for v in vals], " local log-slopes:", np.round(sl, 3))
