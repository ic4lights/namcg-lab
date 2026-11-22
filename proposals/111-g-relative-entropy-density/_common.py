# _common.py v4 (round 1, pass 3; sole script authority).
# A_of_G closed form: Kh = -i G^{1/2} Om G^{1/2} (Hermitian, eigen +-nu; the
# "modular-frequency matrix"), Kf = sign(Kh) h(|Kh|), h(nu) = ln((nu+.5)/(nu-.5)),
#   A0 = -i G^{-1/2} Kf G^{1/2} Om   (Om = Omega, interleaved x1,p1,... order).
# This is the dead pass's formula A0 = 2i artanh((2i Om^{-1} G)^{-1}) Om^{-1} rewritten:
# with T = G^{1/2}Om^{-1}G^{1/2}, B = -(i/2)T^{-1} = (1/2) Kh^{-1} (similarity via
# G^{1/2}), so artanh(B) = Kf/2 is computed by ONE eigh of Kh - no matrix inverse, no
# artanh of round-off-perturbed eigenvalues near +-1, no clipping. Ground truths that
# pin it: exact single-mode A0 = h*nu*G^{-1} (squeezed-thermal oscillator, derived by
# hand in the proposal), Fock-covariance roundtrip, first law S = 1/2 Tr(A0 G) - c0,
# and regression against the dead pass's B-route at moderate states (dead-pass crash
# log shows those tests passed before the near-pure crash).
# Other fixes vs v1 (dead pass): entropy_from_modes formula (was sign-flawed:
#   correct s = (nu-.5)h - ln(1-e^{-h})); c0_from_nus added (stable); symplectic
#   dedup kept from v1 (v1 already summed s(nu) over N modes once, NOT double -
#   checked against first law and Fock entropy, see DEADPASS NOTES).
import numpy as np
from scipy.linalg import expm

def omega(N):
    return np.kron(np.eye(N), np.array([[0.0, 1.0], [-1.0, 0.0]]))

def chain_ring(L, mu):
    """Full-chain ground-state covariance of H = sum_j [pi_j^2/2 + mu^2 phi_j^2/2
    + (phi_{j+1}-phi_j)^2/2] on a ring of L sites. Returns (C, Pi)."""
    K = (2.0 + mu * mu) * np.eye(L)
    idx = np.arange(L)
    K[idx, (idx + 1) % L] -= 1.0
    K[idx, (idx - 1) % L] -= 1.0
    w, V = np.linalg.eigh(K)
    rt = V @ np.diag(np.sqrt(w)) @ V.T
    C = 0.5 * np.linalg.inv(rt)
    Pi = 0.5 * rt
    return C, Pi

def restrict(L, mu, sites):
    C, Pi = chain_ring(L, mu)
    return C[np.ix_(sites, sites)], Pi[np.ix_(sites, sites)]

def G_block(C, Pim, Cc=None):
    n = C.shape[0]
    Rc = np.zeros_like(C) if Cc is None else 0.5 * (Cc - Cc.T)
    G = np.zeros((2 * n, 2 * n))
    G[0::2, 0::2] = C
    G[1::2, 1::2] = Pim
    G[0::2, 1::2] = Rc
    G[1::2, 0::2] = Rc.T
    return G

def symplectic_spectrum(G):
    ev = np.linalg.eigvals(1j * omega(G.shape[0] // 2) @ G)
    return np.sort(np.abs(ev))

def nus(G):
    """Distinct symplectic eigenvalues (N of them): dedup of the 2N absolute eigenvalues
    of i Om G, where each mode appears twice."""
    nu = symplectic_spectrum(G)
    return 0.5 * (nu[0::2] + nu[1::2])

def is_physical(G, tol=1e-10):
    return nus(G).min() >= 0.5 - tol

def hvec(nu):
    nu = np.maximum(nu, 0.5 + 1e-15)
    return np.log((nu + 0.5) / (nu - 0.5))

def A_of_G_raw(G):
    """Complex A0 from the closed form, NO imag-part assert (diagnostics/certification)."""
    n = G.shape[0] // 2
    O = omega(n)
    wG, U = np.linalg.eigh(0.5 * (G + G.T))
    assert wG.min() > 0, "G not positive definite"
    sq = U @ np.diag(np.sqrt(wG)) @ U.T
    isq = U @ np.diag(1.0 / np.sqrt(wG)) @ U.T
    Kh = -1j * (sq @ O @ sq)              # Hermitian, eigen +-nu
    hw, HV = np.linalg.eigh(Kh)
    assert np.min(np.abs(hw)) >= 0.5 - 1e-9, "unphysical G: |eig Kh| < 0.5"
    Kf = HV @ np.diag(np.sign(hw) * hvec(np.abs(hw))) @ HV.conj().T
    A = -1j * ((isq @ Kf @ sq) @ O)
    return A


# Imag-part tolerance policy (pass 4, measured scalars, stab_probe1/3):
# exact A0 is real; round-off leakage max|Im|/(1+max|Re|) is 1e-10..1e-7 for chain
# cuts with <= 8 near-pure modes, but grows to 1e-4..1e-3 once the cut entanglement
# spectrum carries more modes with nu-0.5 below the double-precision eig floor
# (h(nu) is then unresolvable; A0 itself is not determined to 1e-6 relative).
# A_of_G therefore asserts leakage <= 1e-6 (1e-6*scale + 1e-12) and the battery
# certifies only cuts that pass it. Dropping the (discarded) imag part is anchored
# by the Fock covariance/entropy round-trip (Tests A1/A4) on Fock-feasible cuts.
IMAG_RELTOL = 1e-6

def A_of_G(G):
    """Modular exponent: -ln sigma = 1/2 R A0 R - ln Z, c0 = -ln Z. Closed form in header."""
    A = A_of_G_raw(G)
    scale = np.max(np.abs(A.real))
    assert np.max(np.abs(A.imag)) <= IMAG_RELTOL * scale + 1e-12, "A0 imag part not noise"
    A = A.real
    return 0.5 * (A + A.T)

def c0_from_nus(nu):
    return float(np.sum(np.log(2.0 * np.sinh(0.5 * hvec(nu)))))

def c0_from_G_alt(G):
    n = G.shape[0] // 2
    O = omega(n)
    M = -(G @ O @ G @ O) - 0.25 * np.eye(2 * n)
    ev = np.linalg.eigvals(M)
    assert np.max(np.abs(ev.imag)) < 1e-8 and ev.real.min() > 0
    return -0.25 * float(np.sum(np.log(ev.real)))

def s_of_nu(nu):
    """s(nu) = (nu+.5)ln(nu+.5) - (nu-.5)ln(nu-.5), stable as nu -> 1/2."""
    vm = np.maximum(nu - 0.5, 0.0)
    return (nu + 0.5) * np.log(nu + 0.5) - np.where(vm > 0, vm * np.log(np.maximum(vm, 1e-300)), 0.0)

def entropy_from_G(G):
    return float(np.sum(s_of_nu(nus(G))))

def h_modes(G):
    return hvec(symplectic_spectrum(G))

def entropy_from_modes(G):
    """Same entropy via modular frequencies: s = (nu-.5)h - ln(1-e^{-h})."""
    nu = nus(G)
    h = hvec(nu)
    return float(np.sum((nu - 0.5) * h - np.log1p(-np.exp(-h))))

def S_rel_formula(G1, G0):
    """S(rho1||rho0) = -S1 + 1/2 Tr(A0 G1) - c0, faithful Gaussian sigma."""
    A0 = A_of_G(G0)
    c0 = c0_from_nus(nus(G0))
    return -entropy_from_G(G1) + 0.5 * float(np.trace(A0 @ G1)) - c0

def S_rel_terms(G1, G0):
    A0 = A_of_G(G0)
    nu0 = nus(G0)
    c0 = c0_from_nus(nu0)
    return dict(S1=entropy_from_G(G1), tA=0.5 * float(np.trace(A0 @ G1)), c0=c0,
                S0=float(np.sum(s_of_nu(nu0))), tA0=0.5 * float(np.trace(A0 @ G0)))

def ladder(nmax):
    ad = np.diag(np.sqrt(np.arange(1, nmax + 1)), 1)
    a = ad.T
    x = (ad + a) / np.sqrt(2.0)
    p = 1j * (ad - a) / np.sqrt(2.0)
    return x, p

def embed(nmodes, op, which, nmax):
    mats = [op if m == which else np.eye(nmax + 1) for m in range(nmodes)]
    out = mats[0]
    for m in mats[1:]:
        out = np.kron(out, m)
    return out

def r_ops(nmodes, nmax):
    x, p = ladder(nmax)
    Rint = [None] * (2 * nmodes)
    for m in range(nmodes):
        Rint[2 * m] = embed(nmodes, x, m, nmax)
        Rint[2 * m + 1] = embed(nmodes, p, m, nmax)
    return Rint

def quad_form_matrix(A, nmax):
    nmodes = A.shape[0] // 2
    Rint = r_ops(nmodes, nmax)
    H = np.zeros_like(Rint[0], dtype=complex)
    for i in range(2 * nmodes):
        for j in range(2 * nmodes):
            H += 0.5 * A[i, j] * (Rint[i] @ Rint[j])
    return H

def rho_fock(A, nmax):
    H = quad_form_matrix(A, nmax)
    r = expm(-H)
    Z = np.trace(r).real
    return r / Z, Z

def cov_from_rho(rho, nmodes, nmax):
    Rint = r_ops(nmodes, nmax)
    d = 2 * nmodes
    G = np.zeros((d, d))
    for i in range(d):
        for j in range(d):
            val = 0.5 * np.trace(rho @ (Rint[i] @ Rint[j] + Rint[j] @ Rint[i]))
            G[i, j] = val.real
    return G

def entropy_fock(rho):
    w = np.linalg.eigvalsh((rho + rho.conj().T) / 2)
    w = w[w > 1e-14]
    return float(-np.sum(w * np.log(w)))

def S_rel_fock(A1, A0, nmax):
    """Ground truth: Tr rho1 (ln rho1 - ln rho0), rho_i = exp(-1/2 R A_i R)/Z_i,
    ln rho_i = -1/2 R A_i R - ln Z_i, within the same truncated Fock space."""
    r1, Z1 = rho_fock(A1, nmax)
    H1 = quad_form_matrix(A1, nmax)
    H0 = quad_form_matrix(A0, nmax)
    Z0 = np.trace(expm(-H0)).real
    d = H1.shape[0]
    ln1 = -H1 - np.log(Z1) * np.eye(d)
    ln0 = -H0 - np.log(Z0) * np.eye(d)
    return float(np.trace(r1 @ (ln1 - ln0)).real)

def rand_symplectic(n, seed, scale=0.08):
    rng = np.random.default_rng(seed)
    O = omega(n)
    Y = rng.normal(size=(2 * n, 2 * n)); Y = 0.5 * (Y + Y.T) * scale
    return expm(O @ Y)

def rand_G(n, seed, nu_lo=0.6, nu_hi=1.3):
    rng = np.random.default_rng(seed + 777)
    nu = np.sort(rng.uniform(nu_lo, nu_hi, size=n))
    D = np.kron(np.diag(nu), np.eye(2))
    S = rand_symplectic(n, seed)
    G = S @ D @ S.T
    return 0.5 * (G + G.T)
