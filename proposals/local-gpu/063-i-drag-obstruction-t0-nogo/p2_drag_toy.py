"""
Proposal 063 (Problem I, drag), P2 verification for the bounded
T=0 / sub-critical drag no-go.  Run with:  python -I p2_drag_toy.py
(stdout is the authoritative .out file, saved as p2_drag_toy.out.)

Checks performed:
 A. Spectral representation of the retarded force correlator
    (hbar = 1):
      Im chi^R_ij(omega) = pi * sum_{m,n} (p_n - p_m) F^i_mn F^j_nm
                          * delta(omega - (E_m - E_n)),   omega > 0,
    established identity, verified on random finite-dimensional passive
    systems two ways: (i) direct Heisenberg time evolution + damped DFT
    (delta part only), (ii) eigenbasis sum with Lorentzian smoothing.
    Also verifies that the weighted Bohr spectrum above a ground-state
    reference is gapped, so Gamma_ij = lim Im chi / omega = 0 exactly at
    finite dimension.
 B. Finite harmonic chain (bath) + one heavy site treated as a classical
    external parameter R (an explicitly reduced model with imported
    separation, exit-(iii) type: a benchmark, not NAMCG dynamics).
    Force operator F = -dH_int/dR with H_int = sum_x W(x-R) q_x,
    Gaussian core W(x) of size ell (ell = 0.6: a near-pointlike core, so
    the form factor does not hide the threshold kinematics).
    (a) exact support of Im chi^R on the discrete set {omega_k}: zero
        below the lowest weighted Bohr frequency;
    (b) Landau threshold: golden-rule absorption rate
        P(v) ~ sum_k |<k|F|0>|^2 delta(omega_k - v k).
        Exact resonance count (sign changes of omega_k - v k on the grid)
        is 0 for v < min_k omega_k/|k| and > 0 above; the broadened
        P_eps(v) below threshold shrinks proportionally to eps
        (evidence of an exact zero), while above threshold it is
        eps-independent.
 C. Continuum form-factor integrals (sympy, exact): for a Gaussian core of
    size ell (|W~(q)|^2 = exp(-q^2 ell^2)) with derivative coupling to a
    scalar field u = Int d^d q/(2pi)^d (b_q e^{iqx} + h.c.)/sqrt(2 eps_q):
      gapless linear eps_q = c q:
        d=1: Im chi = omega exp(-omega^2 ell^2/c^2)/(2 c^3)
             -> Ohmic, Gamma = 1/(2c^3) finite (open channel: the
                loophole ingredient), even though P(v<c_s)=0;
        d=3: Im chi = omega^3 exp(...)/(4 pi c^5) -> super-Ohmic, Gamma = 0;
      gapped eps_q = sqrt(Delta^2 + c^2 q^2): support only for
        omega >= Delta (Piecewise), hence Gamma = 0 for both d.
"""
import numpy as np
import sympy as sp

rng = np.random.default_rng(20261109)


def sym_hermitian(n):
    A = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    return (A + A.conj().T) / 2


print("=" * 74)
print("PART A: spectral representation of Im chi^R (finite-dimensional check)")
print("=" * 74)
for trial in range(3):
    n = 24
    H = sym_hermitian(n)
    F1 = sym_hermitian(n)
    F2 = F1                             # diagonal component i=j (the drag
                                        # sign statement is checked here; the
                                        # off-diagonal tensor components enter
                                        # the support/support-gap argument only)
    E, V = np.linalg.eigh(H)
    p = np.zeros(n)
    p[0] = 1.0                      # passive ground-state reference
    F1e = V.conj().T @ F1 @ V
    F2e = V.conj().T @ F2 @ V
    F1e = F1e - np.diag(np.diag(F1e))   # connected operators
    F2e = F2e - np.diag(np.diag(F2e))

    # (i) direct: chi^R(t) = i*theta(t)*<[F1(t),F2(0)]>, hbar=1, with the
    # manuscript-compatible transform convention chi^R(omega) =
    # Int_0^inf dt e^{+i omega t} chi^R(t) (so Im chi^R(omega>0) >= 0 for a
    # passive system); np.fft.fft uses e^{-i omega t}, so chi^R =
    # conj(fft(conj(chi_t))) * dt.
    eps = 0.05
    dt, nsteps = 0.02, 20000

    def F1t(t):
        ph = np.exp(1j * E * t)
        Fe = ph[:, None] * F1e * ph.conj()[None, :]
        return V @ Fe @ V.conj().T

    chi_t = np.empty(nsteps, dtype=complex)
    for s in range(nsteps):
        t = s * dt
        comm = F1t(t) @ F2 - F2 @ F1t(t)
        ce = V.conj().T @ comm @ V
        chi_t[s] = 1j * np.sum(p * np.diag(ce))
    chi_t *= np.exp(-eps * np.arange(nsteps) * dt)
    chi_w = np.conj(np.fft.fft(np.conj(chi_t))) * dt
    ws = np.fft.fftfreq(nsteps, dt) * 2 * np.pi
    pos = ws > 0
    ws_pos = np.sort(ws[pos]); chi_pos = chi_w[pos][np.argsort(ws[pos])]

    # (ii) eigenbasis delta part: Im chi(omega) =
    #      pi sum (p_n-p_m) Re(F1_mn F2_nm) delta(omega-(E_m-E_n))
    def imchi_eig(omega):
        out = 0.0
        for m in range(n):
            for nn in range(n):
                if p[nn] == p[m]:
                    continue
                A = F1e[m, nn] * F2e[nn, m]
                g = omega - (E[m] - E[nn])
                out += (p[nn] - p[m]) * float(np.real(A)) * eps / (g * g + eps * eps)
        return out

    om0 = E[1] - E[0]
    im_direct = float(np.interp(om0, ws_pos, np.imag(chi_pos)))
    im_eig = imchi_eig(om0)
    print(f"trial {trial}: gap E1-E0 = {om0:.4f}; Im chi^R at omega=gap: "
          f"eigenbasis {im_eig:+.5f}, direct DFT {im_direct:+.5f} "
          f"(same broadening eps={eps}; sign match: "
          f"{np.sign(im_direct) == np.sign(im_eig)})")
    sup = sorted({E[m] - E[0] for m in range(1, n)
                  if np.max(np.abs(F1e[m, :] * F2e[:, m])) > 1e-12})
    print(f"          weighted Bohr support min = {sup[0]:.4f} > 0 "
          f"=> Im chi = 0 on (0, {sup[0]:.4f}) => Gamma_ij = 0")

print()
print("=" * 74)
print("PART B: finite chain bath + heavy site as external parameter (benchmark)")
print("=" * 74)
N = 256
ell = 0.6

def dispersion(Delta):
    k = 2 * np.pi * np.fft.fftfreq(N, d=1.0)
    om = np.sqrt(Delta**2 + 4 * np.sin(k / 2)**2)
    return k, om

for Delta, tag in [(1.0, "gapped (Delta=1)"), (0.0, "gapless (Delta=0)")]:
    k, om = dispersion(Delta)
    Wk = np.exp(-0.5 * k**2 * ell**2)          # Gaussian core form factor
    # <k|F|0> = i k W~(k) e^{-ikR} / sqrt(2 N om_k)
    mask = om > 0
    f2 = np.zeros(N)
    f2[mask] = (k[mask] * Wk[mask])**2 / (2 * N * om[mask])
    wsup = np.sort(om[mask & (f2 > 1e-30)])
    print(f"{tag}:")
    print(f"    discrete support of Im chi^R: min weighted Bohr freq = "
          f"{wsup[0]:.5f} => Im chi = 0 below it exactly => Gamma = 0 at finite N")
    kk = np.abs(k[mask])
    ratio = np.where(kk > 0, om[mask] / np.where(kk > 0, kk, 1.0), np.inf)
    cs = ratio.min()
    print(f"    Landau threshold min omega_k/|k| = {cs:.4f}")

    def nres(v):
        g = om[mask] - v * k[mask]
        return int(np.sum(np.diff(np.sign(g)) != 0))

    def P(v, e):
        return float(np.sum(f2[mask] * (e / ((om[mask] - v * k[mask])**2 + e**2)) / np.pi))

    for v in [0.3, 0.5, 0.62, 0.7, 0.9, 1.2, 1.5]:
        p05 = P(v, 0.05)
        p02 = P(v, 0.02)
        print(f"    v={v:4.2f}: exact resonances = {nres(v):2d}; "
          f"P(v) at eps=0.05: {p05:.3e}; at eps=0.02: {p02:.3e}; "
          f"ratio p02/p05 = {(p02/p05 if p05 > 0 else float('nan')):.3f} "
          f"(<1 => tail of a true zero; ~1 => real on-shell rate)")

print()
print("=" * 74)
print("PART C: continuum form-factor integrals (sympy, exact)")
print("=" * 74)
w, c, ell_s, q, Delta_s, evar = sp.symbols('omega c ell q Delta eps', positive=True)
for d in (1, 3):
    S = {1: 2, 3: 4 * sp.pi}[d]
    epsq = c * q
    integ = q**(d - 1) * q**2 * sp.exp(-q**2 * ell_s**2) / (2 * epsq) * sp.DiracDelta(w - epsq)
    J = sp.simplify(sp.pi * S / (2 * sp.pi)**d * sp.integrate(integ, (q, 0, sp.oo)))
    gam = sp.simplify(sp.diff(J, w).subs(w, 0))
    print(f"d={d}, gapless linear: Im chi(omega) = {J}")
    print(f"      Gamma = lim Im chi/omega = {gam}")
for d in (1, 3):
    S = {1: 2, 3: 4 * sp.pi}[d]
    # substitute eps = sqrt(Delta^2 + c^2 q^2): q = sqrt(eps^2-Delta^2)/c,
    # dq = eps/(c^2 q) deps
    qof = sp.sqrt(evar**2 - Delta_s**2) / c
    integ = qof**(d - 1) * qof**2 * sp.exp(-qof**2 * ell_s**2) / (2 * evar) \
            * evar / (c**2 * qof) * sp.DiracDelta(w - evar)
    J = sp.simplify(sp.pi * S / (2 * sp.pi)**d * sp.integrate(integ, (evar, Delta_s, sp.oo)))
    print(f"d={d}, gapped sqrt(Delta^2+c^2 q^2): Im chi(omega) = {J}")
print("      (support omega >= Delta for both d  =>  Gamma = 0)")
print()
print("Summary of the bounded-class classification:")
print("  passive state + gapped weighted spectrum       : Gamma_ij = 0 (exact support)")
print("  gapless linear, d>=2, finite-size derivative   : Gamma_ij = 0 (super-Ohmic)")
print("  gapless linear, d=1,  derivative coupling      : Gamma_ij != 0 (Ohmic channel open)")
print("  sub-critical v < min eps_q/q                   : golden-rule absorption P(v) = 0")
print("  BEK-type lowered phase velocity                : reopens P(v) below bare c")
print("  (see p3_two_impurity.py for the modified-dispersion and separation")
print("   structure checks)")
