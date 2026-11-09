"""Proposal 061 script 1: half-line entanglement benchmark for the free
constant-Theta (Moyal) sector of eq:Smatrix, used for the alpha_0-type
benchmark value in the G paragraph.

Setting (lattice units a = 1, so the theta-regularised trace cutoff is
Lambda = pi, Eq. eq:LUV-def with Theta^(1/2) = a up to O(1)): quadratic
fluctuations of a real scalar on the Moyal background: per transverse Fourier
mode p_perp the kinetic dispersion is omega(p) = sqrt(mu^2 + 4 sin^2(p/2)); the
half-space cut is the one-particle spectral cut of the single coordinate
operator Xhat^3 (the x^3 > 0 half-line for each p_perp). The ground-state
covariance of each 1D problem is
  C_ij = int dp/(2 pi) e^{ip(i-j)} / (2 omega_p)   (x-x block)
  D_ij = int dp/(2 pi) e^{ip(i-j)} (omega_p / 2)   (p-p block)
restricted to sites i,j in [1,N] of the HALF-INFINITE chain (the unrestricted
spectrum is exactly {1/2} per mode: C D = 1/4 in the full translation setting,
checked in script 2, so the restricted spectrum carries all the entropy).
Restricted symplectic spectrum: nu_k^2 = eigenvalues of D^{1/2} C D^{1/2}
(nu_k >= 1/2);
  s1(mu) = sum_k [ (nu+1/2) ln(nu+1/2) - (nu-1/2) ln(nu-1/2) ].
Correlator arrays C0[r], D0[r] come from an inverse DFT of the p-grid samples
(p = 2 pi k / n; the p = 0 point of 1/(2 omega) is dropped at mu = 0, its
divergent part is r-independent and lies in the null direction of D,
1^T D 1 = 0, so it cannot enter the symplectic spectrum; this is the standard
massless treatment).

Checks:
  (1) massless half-line: s1(N) - (1/6) ln N -> k (converges to ln2/3).
  (2) large-mu decay: s1 ~ (pi/2) e^{-mu}.
  (3) small-mu log: s1 = (1/(6 pi)) ln(1/mu) + c0; continuum reference
      c0_ref = ln2/3 - 9/(16 pi) + ln(4/pi)/(6 pi) (K1 asymptotics, script 2).
  (4) slab coefficient sigma = (1/(2 pi)^2) int_BZ2 d^2p s1(mu(p_perp)),
      mu^2 = 4 sin^2(p1/2)+4 sin^2(p2/2): fitted asymptotics on a 512^2 grid,
      direct s1 on a 64^2 grid for mu >= 0.05, and the asymptotic reference
      1/(48 pi^2) + (ln 2 - 9/16)/(2 pi) (continuum-only, leading).

Numerical check, not a proof. Run: python -I halfline_ee.py
"""
import numpy as np

NG = 1 << 14

def cov_arrays(mu, ng=NG):
    k = np.arange(ng)
    w = np.sqrt(mu*mu + 4*np.sin(np.pi*k/ng)**2)
    fC = np.where(w > 0, 1/(2*w), 0.0)
    fD = w/2
    C0 = np.fft.ifft(fC).real
    D0 = np.fft.ifft(fD).real
    return C0, D0

def s1(mu, N, ng=NG):
    C0, D0 = cov_arrays(mu, ng)
    idx = np.abs(np.subtract.outer(np.arange(N), np.arange(N)))
    C = C0[idx]; D = D0[idx]
    C = 0.5*(C+C.T); D = 0.5*(D+D.T)
    wD, VD = np.linalg.eigh(D)
    wD = np.clip(wD, 0, None)
    Dh = (VD*np.sqrt(wD))@VD.T
    M = Dh@C@Dh
    M = 0.5*(M+M.T)
    ev = np.linalg.eigvalsh(M)
    nu = np.sqrt(np.clip(ev, 0.25, None))
    nu = np.clip(nu, 0.5, None)
    x = nu+0.5
    y = np.clip(nu-0.5, 0, None)
    s = np.sum(x*np.log(x) - y*np.log(np.maximum(y, 1e-300)))
    return s, nu

def main():
    print("=== (1) massless half-line: s1(N) - (1/6) ln N ===")
    prev = None
    for N in (256, 1024, 2048, 4096, 8192):
        s, nu = s1(0.0, N)
        val = s - (1/6)*np.log(N)
        d = "-" if prev is None else f"{val-prev:.2e}"
        print(f"N={N:6d} s1={s:.6f} s1-(1/6)lnN={val:.6f} delta={d}")
        prev = val
    print("predicted k = ln(2)/3 =", np.log(2)/3)

    print("=== (2) large-mu decay s1(mu) ~ (pi/2) e^{-mu} ===")
    for mu in (1.0, 1.5, 2.0, 2.5):
        s, _ = s1(mu, 300)
        print(f"mu={mu}: s1={s:.6f} ratio={s/(np.pi/2*np.exp(-mu)):.4f}")

    print("=== (3) small-mu log: s1 - (1/(6pi)) ln(1/mu) ===")
    ref = np.log(2)/3 - 9/(16*np.pi) + np.log(4/np.pi)/(6*np.pi)
    print("continuum reference c0_ref =", round(ref, 6))
    fits = {}
    for mu in (0.3, 0.1, 0.03, 0.01, 0.003, 0.001):
        N = int(min(8192, 6.0/mu))
        s, _ = s1(mu, N)
        v = s - (1/(6*np.pi))*np.log(1/mu)
        fits[mu] = v
        print(f"mu={mu:<7g} N={N:6d} s1={s:.5f} v=s1-(1/(6pi))ln(1/mu)={v:.5f}")
    a_coef = 1/(6*np.pi); b_fit = fits[0.01]
    print(f"fitted (a,b) = ({a_coef:.6f}, {b_fit:.6f})")

    print("=== (4a) sigma from fitted asymptotics on 512^2 offset grid ===")
    nt = 512
    pc = 2*np.pi*(np.arange(nt)+0.5)/nt
    P1, P2 = np.meshgrid(pc, pc, indexing="ij")
    mu = np.sqrt(4*np.sin(P1/2)**2 + 4*np.sin(P2/2)**2)
    s = a_coef*np.log(1/np.maximum(mu, 1e-12)) + b_fit
    s = np.where(mu > 1.2, 0.05*np.exp(-mu), s)
    sigma_fit = s.sum()*(2*np.pi/nt)**2/(2*np.pi)**2
    print(f"sigma_fitted-grid = {sigma_fit:.6f}")

    print("=== (4b) direct s1 on coarse 64^2 offset grid, mu>=0.05, N=1024 ===")
    ntc = 64
    pd = 2*np.pi*(np.arange(ntc)+0.5)/ntc
    Q1, Q2 = np.meshgrid(pd, pd, indexing="ij")
    mud = np.sqrt(4*np.sin(Q1/2)**2 + 4*np.sin(Q2/2)**2)
    tot = 0.0; cache = {}
    for m in mud[mud >= 0.05].ravel():
        key = round(float(m), 4)
        if key not in cache:
            cache[key] = s1(m, 1024)[0]
        tot += cache[key]
    cell = (2*np.pi/ntc)**2
    sigma_dir = tot*cell/(2*np.pi)**2
    # small-mu tail (mu<0.05) with fitted form:
    ut = 0.05
    tail = (1/(2*np.pi))*(a_coef*(0.5*ut**2*(1-2*np.log(ut))) + b_fit*0.5*ut**2)
    # region 0.05<=mu with fitted form vs direct differ negligibly; report both:
    print(f"sigma_direct(mu>=0.05) = {sigma_dir:.6f}; tail(mu<0.05) = {tail:.6f}")
    print(f"sigma_total_direct-estimate = {sigma_dir+tail:.6f}")
    sig_ref = 1/(48*np.pi**2) + (1/(2*np.pi))*(np.log(2) - 9/16)
    print("asymptotic continuum reference 1/(48pi^2)+(ln2-9/16)/(2pi) =", round(sig_ref, 6))

if __name__ == "__main__":
    main()
