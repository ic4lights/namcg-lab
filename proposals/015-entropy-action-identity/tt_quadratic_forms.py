"""
Independent re-derivation of the O(eps^2) phase-averaged quadratic forms of  rho*R[g_rho]  and  rho^2*X
about a constant Poisson bivector Thetabar (Euclidean section eta = delta), Poisson limit.

Setting (as in the integrated Poisson-limit paragraph of Appendix H, Problem F):
  Theta^{mu nu}(x) = Thetabar + eps*T,  T^{mu nu} = Thetabar^{mu r} d_r a^nu - Thetabar^{nu r} d_r a^mu,
  a^mu = u^mu cos(p.x),  q^mu = Thetabar^{mu r} p_r.
  K^{mu nu} = delta_{ab} Theta^{a mu} Theta^{b nu},  rho = 1/|Pf Theta|,  g_rho^{mu nu} = rho K^{mu nu}  (det = 1),
  X = delta^{rl} d_r Theta^{mu nu} d_l Theta^{mu nu}.
Everything depends on theta = p.x only, d_mu = p_mu d/dtheta.  Derivatives in theta are taken spectrally (FFT),
curvature of g_rho is computed pointwise from Gamma and Riemann, the eps^2 coefficient is extracted by
Richardson extrapolation in eps, and the theta average is the mean over a uniform grid (exact for the
trigonometric polynomials involved up to spectral truncation).
Output: eigenvalues of the two quadratic forms relative to the tree-level kernel M = q^2 delta - q q on the
3-dimensional quotient by u ~ q, divided by rho_bar^2 p^2 (p^2 = delta^{mu nu} p_mu p_nu).
"""
import numpy as np

rng = np.random.default_rng(12345)
N = 128
th = 2 * np.pi * np.arange(N) / N
k = np.fft.fftfreq(N, d=1.0 / N)


def dth(f):
    return np.real(np.fft.ifft(1j * k.reshape((-1,) + (1,) * (f.ndim - 1)) * np.fft.fft(f, axis=0), axis=0))


def pfaff(Th):
    return Th[..., 0, 1] * Th[..., 2, 3] - Th[..., 0, 2] * Th[..., 1, 3] + Th[..., 0, 3] * Th[..., 1, 2]


def forms(Tb, p, u, eps):
    q = Tb @ p
    qu = np.outer(q, u) - np.outer(u, q)
    Th = Tb[None, :, :] - eps * qu[None, :, :] * np.sin(th)[:, None, None]
    Pf = pfaff(Th)
    rho = 1.0 / np.abs(Pf)
    K = np.einsum('tab,tac->tbc', Th, Th)
    gup = rho[:, None, None] * K
    g = np.linalg.inv(gup)
    gp = dth(g)
    # Gamma^l_{mn} = 1/2 g^{ls}( p_m g'_{sn} + p_n g'_{sm} - p_s g'_{mn} )
    term = (np.einsum('m,tsn->tsmn', p, gp) + np.einsum('n,tsm->tsmn', p, gp) - np.einsum('s,tmn->tsmn', p, gp))
    Gam = 0.5 * np.einsum('tls,tsmn->tlmn', gup, term)
    dGam = dth(Gam)
    # R^r_{s m n} = p_m dGam^r_{n s} - p_n dGam^r_{m s} + Gam^r_{m l} Gam^l_{n s} - Gam^r_{n l} Gam^l_{m s}
    Riem = (np.einsum('m,trns->trsmn', p, dGam) - np.einsum('n,trms->trsmn', p, dGam)
            + np.einsum('trml,tlns->trsmn', Gam, Gam) - np.einsum('trnl,tlms->trsmn', Gam, Gam))
    Ric = np.einsum('trsrn->tsn', Riem)
    R = np.einsum('tsn,tsn->t', gup, Ric)
    Lh = rho * R
    dTh = dth(Th)
    X = (p @ p) * np.einsum('tab,tab->t', dTh, dTh)
    Lx = rho ** 2 * X
    return Lh.mean(), Lx.mean()


def second_order(Tb, p, u):
    h = 0.02
    out = []
    vals = {}
    for e in (-2 * h, -h, 0.0, h, 2 * h):
        vals[e] = np.array(forms(Tb, p, u, e))
    d2a = (vals[h] + vals[-h] - 2 * vals[0.0]) / (2 * h ** 2)
    d2b = (vals[2 * h] + vals[-2 * h] - 2 * vals[0.0]) / (2 * (2 * h) ** 2)
    return (4 * d2a - d2b) / 3.0, vals[0.0]


def run(a0, b0, p):
    Tb = np.zeros((4, 4))
    Tb[0, 1], Tb[1, 0], Tb[2, 3], Tb[3, 2] = a0, -a0, b0, -b0
    q = Tb @ p
    rhobar = 1.0 / (a0 * b0)
    # orthonormal basis of q-perp
    Q, _ = np.linalg.qr(np.column_stack([q, np.eye(4)]))
    B = Q[:, 1:4]
    MH = np.zeros((4, 4))
    MX = np.zeros((4, 4))
    basis = np.eye(4)
    # quadratic forms u^T M u via polarisation
    def Lq(u):
        return second_order(Tb, p, u)[0]
    L = {}
    for i in range(4):
        L[(i, i)] = Lq(basis[i])
    for i in range(4):
        for j in range(i + 1, 4):
            Lpp = Lq(basis[i] + basis[j])
            L[(i, j)] = 0.5 * (Lpp - L[(i, i)] - L[(j, j)])
    for i in range(4):
        for j in range(4):
            key = (i, j) if i <= j else (j, i)
            MH[i, j] = L[key][0]
            MX[i, j] = L[key][1]
    gauge_h = np.linalg.norm(MH @ q) / np.linalg.norm(MH)
    gauge_x = np.linalg.norm(MX @ q) / np.linalg.norm(MX)
    q2 = q @ q
    p2 = p @ p
    EH, VH = np.linalg.eigh(B.T @ MH @ B / q2)
    EX = np.linalg.eigvalsh(B.T @ MX @ B / q2)
    # delta(rho) at first order is proportional to  (*Thetabar)_{mu nu} q^mu u^nu  (variation of the Pfaffian)
    dual = np.zeros((4, 4))
    for m in range(4):
        for n in range(4):
            dual[m, n] = 0.5 * sum(np.linalg.det(np.eye(4)[[m, n, r, s]]) * Tb[r, s] for r in range(4) for s in range(4))
    drho = np.array([abs(q @ dual @ (B @ VH[:, i])) for i in range(3)])
    return EH / (rhobar ** 2 * p2), EX / (rhobar ** 2 * p2), gauge_h, gauge_x, drho


if __name__ == '__main__':
    np.set_printoptions(precision=6, suppress=True)
    for trial in range(3):
        a0 = rng.uniform(0.7, 1.6)
        b0 = rng.uniform(0.7, 1.6)
        p = rng.normal(size=4)
        EH, EX, gh, gx, dr = run(a0, b0, p)
        print(f"trial {trial}: a0={a0:.4f} b0={b0:.4f}")
        print("  eig(rho R[g_rho]) / (rho_bar^2 p^2 M) =", EH, " (gauge residual |M q|/|M|", f"{gh:.1e})")
        print("  |delta rho| weight of each R-eigenvector (nonzero only for the mode with delta rho != 0):", dr)
        print("  eig(rho^2 X)      / (rho_bar^2 p^2 M) =", EX, " (gauge residual |M q|/|M|", f"{gx:.1e})")
