"""034 toy: exact check of the central-Y (right-invariant) prescription in a 2D Euclidean Landau problem, Landau gauge.
omega_1 = p_1 = -i d/dx, omega_2 = k2 - B x   ([omega_1,omega_2] = i B),  phi = kappa x + phi0, y = (0,y2) (y.kappa = 0),
K = y.omega - y^a F_ab x^b = y2 k2 : the magnetic-translation generator, a c-number in each k2 sector (commutes with omega_a and with phi).
Omega_a = omega_a - eps alpha_a sin(phi) K,  H = Omega_1^2 + Omega_2^2.   Second-order response of the local density rho(0) = int dk2/(2pi) <x=0| e^{-tH} |x=0>, phase-averaged over phi0,
returned as T2 = (1/2) d^2 rho/d eps^2 (the coefficient of eps^2).   Finite differences on a grid; the result is compared with the Gaussian seam formula in toy2d_seam.py."""
import numpy as np, sys
def local_density(B, kappa, alpha, y2, c0, t, eps, phi0, k2, N=360, L=7.0):
    h = 2 * L / N
    xg = -L + h * np.arange(N)
    x = xg
    kk = 2 * np.pi * np.fft.fftfreq(N, d=h)
    Fm = np.fft.fft(np.eye(N), axis=0)
    p = np.fft.ifft(kk[:, None] * Fm, axis=0)     # spectral p = -i d/dx on the periodic grid (no fermion doubling)
    K = y2 * k2 + c0
    S = np.diag(np.sin(kappa * x + phi0))
    O1 = p - eps * alpha[0] * K * S
    O2 = np.diag(k2 - B * x).astype(complex) - eps * alpha[1] * K * S
    H = O1 @ O1 + O2 @ O2
    H = (H + H.conj().T) / 2
    w, v = np.linalg.eigh(H)
    i0 = np.argmin(np.abs(x))
    amp = v[i0, :]
    return np.real(np.sum(np.exp(-t * w) * np.abs(amp) ** 2)) / h
def T2_direct(B, kappa, alpha, y2, c0, t, nphi=6, nk=90, kmax=None, delta=0.02, **kw):
    kmax = kmax or (6.0 / np.sqrt(t) + 0.5 * B)
    ks = np.linspace(-kmax, kmax, nk); dk = ks[1] - ks[0]
    tot = 0.0
    for phi0 in (2 * np.pi * (np.arange(nphi) + 0.5) / nphi):
        for k2 in ks:
            f = lambda e: local_density(B, kappa, alpha, y2, c0, t, e, phi0, k2, **kw)
            tot += (f(delta) - 2 * f(0.0) + f(-delta)) / (2 * delta ** 2) / (2 * np.pi) * dk / nphi
    return tot
if __name__ == "__main__":
    B, kappa, t = 0.8, 1.7, 0.35
    alpha = np.array([0.6, -0.9]); y2 = 1.1
    for c0 in (0.0, 0.7):
        val = T2_direct(B, kappa, alpha, y2, c0, t)
        print("c0=%.1f  T2_direct(t=%.2f) = %.8f" % (c0, t, val))
