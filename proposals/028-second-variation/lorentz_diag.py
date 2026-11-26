"""028 script 6: leading-q block of the order-Z^4 term and its Lorentz structure, at the INTEGRAND level (fixed proper time s = e^{-i theta}, theta = pi/2-0.35, Gaussian window kappa=3/4).
First-harmonic/gauge-type plane wave A^a = alpha^a cos(q.y):  flux  F_ab(xi) -> F^0_ab(xi) + eps lambda(xi) Fq_ab ,  Fq_ab = q_a alpha_b - q_b alpha_a ,  lambda(xi) = xi.Y_q   (exact at O(q^2) leading, script 3 part A).
phi = E(Fq) + i B(Fq) in C^3.  (f_e^2+f_m^2)^2 = |C|^2, C = sum_k z_k^2, z_k = z0_k + eps lambda phi_k.   Second order in eps:
   |C_1|^2 + C_0 conj(C_2) + conj(C_0) C_2 ,  C_1 = 2 lambda z0.phi , C_2 = lambda^2 phi.phi
= 4 lambda^2 |z0.phi|^2 + lambda^2 (C_0 conj(phi.phi) + conj(C_0) phi.phi).
Gaussian averages (covariance Gamma/2, Gamma=(P+isS)^-1) give  4 T_kl phi_k conj(phi_l) + kappa' conj(phi).conj(phi) + kappa phi.phi ,
 T_kl=<lambda^2 z0_k conj(z0_l)>, kappa=<conj(C0) lambda^2>, kappa'=<C0 lambda^2>.   phi.phi and conj(phi).conj(phi) are Lorentz invariants of Fq (F.F +- i F.dualF); |phi|^2 = E^2+B^2 is not.
Reports the size of the non-invariant part 4T relative to the invariant part, and the dependence of <lambda^2> on the direction of q at fixed q.q (Lorentz-violation by the vector y)."""
import numpy as np
from z4_large_s import *
rng = np.random.default_rng(13)
theta = np.pi/2 - 0.35
sc = np.exp(-1j*theta)
def blocks(M0, q):
    Fv, Ev, Bv, W, c = flux_vectors(M0)
    Pi, W, Yb, c, E = fields(M0)
    wf = window_forms(M0); P = wf['P']
    S = sum(eta4[a, a]*np.outer(W[a], W[a]) for a in range(4))
    Gam = np.linalg.inv(P + 1j*sc*S)
    pref = (4*np.pi)**-3*np.linalg.det(P + 1j*sc*S)**-0.5*sc**4
    u = np.array([Ev[k] + 1j*Bv[k] for k in range(3)])
    Yq = sum(q[m]*Yb[m] for m in range(4))
    return Gam, pref, u, Yq
def mom(Gam, Y, a, b):
    return 0.25*((Y @ Gam @ Y)*(a @ Gam @ b) + 2*(Y @ Gam @ a)*(Y @ Gam @ b))
def analyse(M0, q):
    Gam, pref, u, Yq = blocks(M0, q)
    ub = u.conj()
    T = np.array([[pref*mom(Gam, Yq, u[k], ub[l]) for l in range(3)] for k in range(3)])
    kap = pref*sum(mom(Gam, Yq, ub[k], ub[k]) for k in range(3))
    kapp = pref*sum(mom(Gam, Yq, u[k], u[k]) for k in range(3))
    return T, kap, kapp
if __name__ == "__main__":
    print("point | a=y4/l | ||4T||_F | |kappa|+|kappa'| | ratio non-invariant/invariant | eigenvalues of Hermitian part of T (rel. to ||T||)")
    for t in range(8):
        if t < 3:
            z = point_y_spatial_zero(t, n=[1.0,2.0,0.7][t])
        else:
            z = rand_z_pos(rng, rng.uniform(0.6, 3))
        M0 = Mfun(z); y = M0[:5, 5]; a_ = abs(M0[4, 5])/np.sqrt(-(y @ np.diag([-1., 1, 1, 1, 1]) @ y))
        q = rng.normal(size=4)
        T, kap, kapp = analyse(M0, q)
        nT = np.linalg.norm(4*T); ninv = abs(kap) + abs(kapp)
        H = (T + T.conj().T)/2; ev = np.linalg.eigvalsh(H)
        print("  %d | %.3f | %.3e | %.3e | %.3f | %s" % (t, a_, nT, ninv, nT/ninv, np.round(ev/np.linalg.norm(T), 3)))
    print()
    print("Dependence of L(q)=<lambda^2> (up to the common prefactor) on the direction of q at fixed eta-norm q.q=+1 and fixed point (y^i=0): scan over q.yhat")
    z = point_y_spatial_zero(0, n=1.0); M0 = Mfun(z); Gam, pref, u, Yq0 = blocks(M0, np.zeros(4))
    Pi, W, Yb, c, E = fields(M0)
    yv = M0[:4, 5]
    rows = []
    for th in np.linspace(0, 1.2, 7):
        # q = (sinh th * e_time-ish ...) keep q.q = +1 : q = (sinh t, cosh t, 0, 0)  (boost of a spatial unit vector)
        q = np.array([np.sinh(th), np.cosh(th), 0, 0]); qup = eta4 @ q
        Y = sum(q[m]*Yb[m] for m in range(4))
        L = 0.5*(Y @ Gam @ Y)
        rows.append((th, qup @ q, (q @ yv), L))
        print("  boost %.2f : q.q=%.3f  q_mu y^mu=%.4f   <lambda^2> = %s" % (th, qup @ q, q @ yv, np.round(L, 6)))
