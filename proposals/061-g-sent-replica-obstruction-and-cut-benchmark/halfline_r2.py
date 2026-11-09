"""Proposal 061 r2, script 1: quasi-free slab-interval cut entropy for the
free constant-Theta (Moyal) sector of eq:Smatrix.

Geometry (explicit): full infinite 1D chain per transverse mode p_perp,
lattice units a = 1 (theta-regularized cutoff Lambda_UV = pi, eq:LUV-def
with Theta^(1/2) = a up to O(1)). The restricted region is the contiguous
slab interval of sites 1..N along the cut direction: TWO entanglement cuts.
IR regulation (explicit, valid): every correlator is computed at a small
MASS mu > 0 from the symbol pair 1/(2 omega(k)), omega(k)/2 with
omega(k) = sqrt(mu^2 + 4 sin^2(k/2)); the k = 0 point of the massless
symbol 1/(2|sin(k/2)|) is NOT integrable and is never dropped.
Covariance blocks (Toeplitz symbols, full-BZ FFT):
  C_ij = ifft(1/(2w))[i-j],  D_ij = ifft(w/2)[i-j]
restricted to sites 1..N. Restricted symplectic spectrum
nu_k^2 = eig(D^{1/2} C D^{1/2}), nu_k >= 1/2 (diagnostic: count of
eigenvalues below 1/4 must be 0);
  s1(mu,N) = sum_k [(nu+1/2)ln(nu+1/2) - (nu-1/2)ln(nu-1/2)].
Two cuts at c = 1 imply slope c/3 = 1/3 in ln N (massless regime,
N << 1/mu) and s1 = (1/3)ln(1/mu) + b with b -> 0 (N >> 1/mu).

Checks (every quoted manuscript number comes from this output):
  (1) massless regime mu_reg = 1e-5: s1(N) - (1/3)ln N and doubling
      slopes (s1(2N)-s1(N))/ln 2 -> 1/3.
  (2) small mass, N >> 1/mu: s1 - (1/3)ln(1/mu) -> 0.
  (3) large mass: s1(mu) <= (pi/2) e^{-mu} (ratio reported; margin, no
      saturation claimed).
  (4) slab coefficient sigma = (2pi)^{-2} int_BZ2 d^2p_perp s1(mu(p_perp)),
      mu^2 = 4 sin^2(p1/2) + 4 sin^2(p2/2):
      route A: direct s1 on a 64^2 offset BZ grid for mu >= 0.05 plus the
        analytic tail int_{mu<0.05} with s1 ~ (1/3)ln(1/mu) + b_tail,
        b_tail = the check-(2) value at mu = 0.05 computed here;
      route B: fitted asymptotics (check-(2) form for mu <= 1.2, large-mu
        bound above 1.2) on a 512^2 offset grid.
Numerical check, not a proof. Run: python -I halfline_r2.py
"""
import numpy as np

NG = 1 << 14

def cov_arrays(mu, ng=NG):
    k = np.arange(ng)
    w = np.sqrt(mu*mu + 4*np.sin(np.pi*k/ng)**2)
    C0 = np.fft.ifft(1/(2*w)).real
    D0 = np.fft.ifft(w/2).real
    return C0, D0

def s1(mu, N, ng=NG):
    assert mu > 0.0, "massless point must be reached via mu_reg > 0"
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
    nbad = int(np.sum(ev < 0.2499))
    nu = np.sqrt(np.maximum(ev, 0.25))
    x = nu+0.5
    y = np.maximum(nu-0.5, 1e-300)
    return float(np.sum(x*np.log(x) - y*np.log(y))), nbad

def main():
    print("=== (1) massless regime via mass regulator mu_reg = 1e-5 ===")
    prev = None
    for N in (256, 512, 1024, 2048, 4096):
        s, nb = s1(1e-5, N)
        d = "-" if prev is None else f"{(s-prev)/np.log(2):.5f}"
        print(f"N={N:5d} s1={s:.6f} s1-(1/3)lnN={s-(1/3)*np.log(N):.6f} "
              f"doubling-slope={d} n(ev<1/4)={nb}")
        prev = s
    print("reference: 1/3 =", round(1/3, 5), " (two cuts, c=1)")

    print("=== (2) small mass, N >> 1/mu: s1 - (1/3)ln(1/mu) ===")
    bs = {}
    for mu in (0.3, 0.1, 0.03, 0.01):
        N = min(4096, int(20/mu))
        s, nb = s1(mu, N)
        v = s - (1/3)*np.log(1/mu)
        bs[mu] = v
        print(f"mu={mu:<6g} N={N:5d} s1={s:.5f} s1-(1/3)ln(1/mu)={v:.5f} nbad={nb}")

    print("=== (3) large mass: s1(mu) <= (pi/2)e^{-mu} ===")
    for mu in (1.0, 1.5, 2.0, 2.5, 3.0):
        s, nb = s1(mu, 300)
        ref = (np.pi/2)*np.exp(-mu)
        print(f"mu={mu}: s1={s:.6f} (pi/2)e^-mu={ref:.6f} ratio={s/ref:.4f}")

    print("=== (4a) sigma route A: direct 64^2 offset grid, mu>=0.05, N=512 ===")
    s05, _ = s1(0.05, 1024)
    b_tail = s05 - (1/3)*np.log(1/0.05)
    print(f"b_tail (check-2 form at mu=0.05, N=1024) = {b_tail:.5f}")
    nt = 64
    pc = 2*np.pi*(np.arange(nt)+0.5)/nt
    P1, P2 = np.meshgrid(pc, pc, indexing="ij")
    mud = np.sqrt(4*np.sin(P1/2)**2 + 4*np.sin(P2/2)**2)
    tot = 0.0; cache = {}
    for m in mud[mud >= 0.05].ravel():
        key = round(float(m), 4)
        if key not in cache:
            cache[key] = s1(m, 512, ng=1 << 13)[0]
        tot += cache[key]
    cell = (2*np.pi/nt)**2
    sig_dir = tot*cell/(2*np.pi)**2
    ut = 0.05
    tail = (1/(2*np.pi))*((1/3)*(0.25*ut**2*(1-2*np.log(ut))) + b_tail*0.5*ut**2)  # int_0^u t ln(1/t) dt = (u^2/4)(1-2 ln u)
    print(f"sigma_direct(mu>=0.05) = {sig_dir:.6f}  tail(mu<0.05) = {tail:.6f}")
    print(f"sigma_routeA_total = {sig_dir+tail:.6f}")

    print("=== (4b) sigma route B: interpolation table on 512^2 offset grid ===")
    mus_tab = np.array([0.05, 0.07, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.65, 0.8, 1.0, 1.25, 1.5, 2.0, 2.5, 3.0])
    s_tab = np.array([s1(m, 512, ng=1 << 13)[0] for m in mus_tab])
    nt2 = 512
    pc2 = 2*np.pi*(np.arange(nt2)+0.5)/nt2
    Q1, Q2 = np.meshgrid(pc2, pc2, indexing="ij")
    mu2 = np.sqrt(4*np.sin(Q1/2)**2 + 4*np.sin(Q2/2)**2)
    sB = np.where(mu2 < 0.05,
                  (1/3)*np.log(np.maximum(1/np.maximum(mu2, 1e-12), 1e-30)) + b_tail,
                  np.interp(mu2, mus_tab, s_tab))
    cellb = (2*np.pi/nt2)**2
    sigma_fit = sB.sum()*cellb/(2*np.pi)**2
    print(f"sigma_routeB_interp-table = {sigma_fit:.6f}")
    print(f"routeA-routeB agreement: "
          f"{abs(sigma_fit-(sig_dir+tail))/(sig_dir+tail)*100:.3f} percent")

if __name__ == "__main__":
    main()
