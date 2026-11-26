"""027 script 11: spin (Zeeman-squared) term of the vector sector on the full six-dimensional leaf in the Gaussian window of Delta_{3/4}.
Derivation (proposal): E_spin^V = 2 s^2 tr[ G_{mu nu} g_3^{mu nu} ],  G = (t W + i s S)^{-1},  g_3 = -sigma(C31) = sigma(Delta_3^{orb}) = W_inv-independent form (K_Box - K_C41 in the script's sign convention).
 In the invariant sector this gives 6 s^2 (1+a^2)/(t + i s a^2)  (checked against the matrix Seeley-DeWitt computation).
Here: whitened coordinates (|u|^2 = alpha q_b, |z|^2 = beta q_f), W = (1/4) I_6 (kappa = 3/4: -sigma(Delta_kappa) = (1/4)(|u|^2+|z|^2)), S = sigma(Box) (rank 4), K31 = sigma(C31).
 Checks:  (a) on the base subspace  -K31_uu = (1/2) I + S_uu  (so that the invariant sector is recovered with window form (1/2) I);  (b) Q-functionals with the Gaussian prefactor g_6(x) = det(I + i x W^{-1} S)^(-1/2).
 Q_X = int_0^oo dx/x g_6(x) d1_X(x) with t = 1 (x = s).  Re and Im reported."""
import numpy as np, scipy.linalg as sl
from scipy.integrate import quad
from cone_window_geometry import *
rng = np.random.default_rng(11)
ph = np.exp(-1j*np.pi/4)
def Qint(f, g):
    h = lambda u, part: ((ph*g(u*ph)*f(u*ph)/(u*ph)).real if part == 0 else (ph*g(u*ph)*f(u*ph)/(u*ph)).imag)
    return quad(h, 1e-12, 2e4, args=(0,), limit=800)[0] + 1j*quad(h, 1e-12, 2e4, args=(1,), limit=800)[0]
print("  y4^2   ell^2   a | (a) |-K31_uu-(I/2+S_uu)| | eigs(W^-1 S) nonzero | Q_mu(mu2=1) 6D (Re,Im) | Q_sp 6D (Re,Im) | 4D invariant-sector Re Q_mu=-2/(1+a^2), Re Q_sp=-8/(1+a^2) with the same normalisation? (ratio Re Q_sp/Re Q_mu)")
for t_ in range(8):
    z = rand_z_pos(rng, rng.uniform(0.5, 4)); M0 = Mfun(z); y = M0[:5, 5]
    r = analyse(M0); F = r['F']; T = r['T']
    S = r['S']; K31 = T.T @ F['C31'] @ T
    ell2 = -(y @ np.diag([-1., 1, 1, 1, 1]) @ y); a = abs(y[4])/np.sqrt(ell2)
    chk = np.max(np.abs(-K31[:4, :4] - (0.5*np.eye(4) + S[:4, :4])))
    W = 0.25*np.eye(6)
    ev = np.linalg.eigvalsh(S/0.25); ev = ev[np.abs(ev) > 1e-7]
    g6 = lambda x: np.prod([(1 + 1j*x*l)**-0.5 for l in ev])
    d1_mu = lambda x: -1j*x
    d1_sp = lambda x: 2*x**2*np.trace(np.linalg.solve(W + 1j*x*S, -K31))
    Qm = Qint(d1_mu, g6); Qs = Qint(d1_sp, g6)
    print("%8.3f %7.3f %6.3f | %.1e | %s | (%8.4f,%8.4f) | (%8.4f,%8.4f) | %.4f" % (y[4]**2, ell2, a, chk, np.round(ev, 3), Qm.real, Qm.imag, Qs.real, Qs.imag, Qs.real/Qm.real))

print("\nExact rotated real parts (x = -i u, u < 1/c' with c' = 2 the modulus of the negative eigenvalue of W^-1 S):")
print("   a   | eig(-K31) in 6D whitened coordinates | Re Q_sp(rot) = -2 int_0^{1/2} u g tr[(W+uS)^-1 (-K31)] du | Re Q_mu(rot) = -int_0^{1/2} g du | tr[(W+uS)^-1(-K31)] at u=0.25")
rng = np.random.default_rng(11)
for t_ in range(8):
    z = rand_z_pos(rng, rng.uniform(0.5, 4)); M0 = Mfun(z); y = M0[:5, 5]
    r = analyse(M0); F = r['F']; T = r['T']; S = r['S']; K31 = T.T @ F['C31'] @ T
    ell2 = -(y @ np.diag([-1., 1, 1, 1, 1]) @ y); a = abs(y[4])/np.sqrt(ell2)
    W = 0.25*np.eye(6); ev = np.linalg.eigvalsh(S/0.25); ev = ev[np.abs(ev) > 1e-7]
    gr = lambda u: np.prod([(1 + l*u)**-0.5 for l in ev])
    f = lambda u: u*gr(u)*np.trace(np.linalg.solve(W + u*S, -K31))
    rs = -2*quad(f, 0, 0.5, limit=400)[0]
    rm = -quad(gr, 0, 0.5, limit=400)[0]
    print("%6.3f | %s | %9.4f | %9.4f | %8.4f" % (a, np.round(np.linalg.eigvalsh(-K31), 3), rs, rm, np.trace(np.linalg.solve(W + 0.25*S, -K31))))
