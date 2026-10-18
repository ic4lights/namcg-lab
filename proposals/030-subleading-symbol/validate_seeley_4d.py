"""030 script 10: end-to-end validation of the weight-2 pipeline (symbol recursion + eps expansion + Gaussian moments + large-s tail) in the NON-degenerate case,
where the answer is the Seeley-DeWitt coefficient.
Setting (kappa_i y^i = 0 so that the vector fields are divergence free, as for Hamiltonian fields): n=4, w0_a = e_a (omega_a = xi_a), Y = y a vector in the span (zeta = y.omega), P an arbitrary positive 4x4 window, kappa_a = q_a arbitrary:
  H = eta^{ab} Pi_a Pi_b = -d_i G^{ij}(phi) d_j,  G^{ij} = eta^{ij} - eps S (u^i y^j + y^i u^j) + eps^2 S^2 (alpha.eta.alpha) y^i y^j,  u = eta alpha,  phi = q.x.
Heat kernel w.r.t. d^4x:  Tr e^{-tH} = (4 pi t)^{-2} int sqrt|g| [1 + t a_1 + ...],  g_ij = (G^{-1})_ij,  a_1 = R/6 + E,  E = (1/2) Lap(lambda) - (1/4)(grad lambda)^2, lambda = ln sqrt|g|
(H = -(nabla + omega)^2 - E with omega = -(1/2) grad lambda).  After the phi-average (Lap lambda is a total derivative of sqrt g Lap lambda):
  <sqrt g a_1>_{eps^2} = (1/6) FP[h] - (1/32)(kappa.kappa)(tr h)^2,   h_ij = S (alpha_i yt_j + yt_i alpha_j),  yt = eta y,
  FP[h] = (1/8)[ -(k.k) h_mn h^mn + 2 (k^m h_mn)(k_l h^ln) - 2 (k^m h_mn k^n) tr h + (k.k)(tr h)^2 ]   (second-order sqrt(-g) R, <cos^2> = 1/2;
  normalisation of the Fierz-Pauli form checked on g = e^{2 sigma} eta, where sqrt(-g) R -> +6 (d sigma)^2: see check_fp_conformal below).
Prediction for the integrand tail: K(s) -> (phase) (4 pi)^-2 s^-1 <sqrt|g| a_1>_{eps^2}.  The script prints the ratio c1 / <sqrt g a_1> for several random data; it must be a data-independent constant."""
import sys, numpy as np, mpmath as mp
sys.dont_write_bytecode = True
from gauss_tools import *
from tail_coeffs import tail
mp.mp.dps = 60
etaN = np.diag([-1., 1, 1, 1])

def FP_avg(h, k):
    kU = etaN @ k
    hU = etaN @ h @ etaN
    trh = np.trace(etaN @ h)
    t1 = -(k @ etaN @ k) * np.sum(h * hU)
    kh = kU @ h                                     # k^m h_{mn}  (lower n)
    t2 = 2 * (kh @ etaN @ kh)
    t3 = -2 * (kU @ h @ kU) * trh
    t4 = (k @ etaN @ k) * trh ** 2
    return (t1 + t2 + t3 + t4) / 8.0

def check_fp_conformal():
    """h = 2 sigma eta with sigma = cos(phi) f: FP[h] -> 6 (d sigma)^2 average"""
    k = np.array([0.3, -0.7, 1.1, 0.5])
    h = 2 * etaN                                    # h_mn = 2 sigma eta_mn with sigma = S
    val = FP_avg(h, k)
    pred = 6 * (k @ etaN @ k) * 0.5
    return val, pred

if __name__ == "__main__":
    v, p = check_fp_conformal()
    print("FP normalisation on g = e^{2 sigma} eta (sigma = sin(phi)): FP_avg = %.10f, 6 <(d sigma)^2> = %.10f" % (v, p))
    rng = np.random.default_rng(5)
    terms = load_terms(name='r2', k=2)
    for trial in range(6):
        alpha = np.round(rng.normal(size=4), 2); y = rng.normal(size=4); kap = np.round(rng.normal(size=4), 2)
        y = y - kap * (kap @ y) / (kap @ kap)                      # divergence-free fields: pairing <dphi, Y> = kappa_i y^i = 0 (as in the Hamiltonian case)
        Pm = rng.normal(size=(4, 4)); Pm = Pm @ Pm.T + 0.5 * np.eye(4)
        yt = etaN @ y
        h = np.outer(alpha, yt) + np.outer(yt, alpha)
        A1 = FP_avg(h, kap) / 6 - (kap @ etaN @ kap) * np.trace(etaN @ h) ** 2 / 32
        dat = dict(W=np.eye(4), Y=y, P=Pm, kappa=kap)
        c0, c1, c2 = tail(dat, alpha, terms)
        ratio = c1 / mp.mpf(A1)
        print("trial %d: <sqrt g a_1>_eps2 = %.8f ; c0 = %s ; c1 = %s ; (4pi)^2 c1/<..> = %s" % (trial, A1, mp.nstr(c0, 6), mp.nstr(c1, 10), mp.nstr(ratio * (4 * mp.pi) ** 2, 12)))
