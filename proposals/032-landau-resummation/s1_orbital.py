"""032 script 1: exact Lorentzian Landau (nilpotent) orbital factor.
Algebra: [omega_a, omega_b] = i F_ab (constant), H0 = eta^{ab} omega_a omega_b, eta = diag(-1,1,1,1),
Fe := eigenvalues of F eta = (+-f_e real, +-i f_m).  Claim:
   Theta(s) := Tr_{per unit coordinate volume} exp(-i s H0) = -i f_e f_m / (16 pi^2 sinh(s f_e) sin(s f_m)),   s -> s - i0.
Checks: (1) magnetic plane by direct Landau-level sum; (2) KMS/Gaussian identity  d ln Theta/ds = -i <H0>,  <H0> = eta^{ab} G_ab,
G = -i F M^T (1-M^T)^{-1}, M = exp(2 s F eta)  (derived from Tr[rho A B] = Tr[rho B(t=s) A], [omega,omega]=iF);
(3) small-s limit -i/(16 pi^2 s^2); (4) properties G - G^T = iF, G = (M G)^T."""
import numpy as np, scipy.linalg as sl, mpmath as mp
eta = np.diag([-1., 1, 1, 1])

def boost_frame_F(fe, fm):
    F = np.zeros((4, 4))
    F[0, 1] = fe; F[1, 0] = -fe          # (F eta)_{01} = F_01 eta^{11} = fe, (F eta)_{10} = F_10 eta^{00} = fe  -> eigenvalues +-fe
    F[2, 3] = fm; F[3, 2] = -fm          # magnetic plane: eigenvalues +-i fm
    return F

def G_of(F, s):
    K = 2 * F @ eta
    M = sl.expm(s * K)
    return -1j * F @ M.T @ np.linalg.inv(np.eye(4) - M.T), M

def theta(s, fe, fm):
    return -1j * fe * fm / (16 * mp.pi ** 2 * mp.sinh(s * fe) * mp.sin(s * fm))

if __name__ == "__main__":
    fe, fm = 0.7, 1.3
    F = boost_frame_F(fe, fm)
    ev = np.linalg.eigvals(F @ eta)
    print("eigenvalues of F eta:", np.round(np.sort_complex(ev), 6))
    # (4) properties of G at complex s on the ray s = r e^{-i theta}
    for s in [0.4 * np.exp(-0.5j), 1.1 * np.exp(-0.9j), 2.0 * np.exp(-0.3j)]:
        G, M = G_of(F, s)
        print("s=%s : |G-G^T-iF| = %.2e   |G-(MG)^T| = %.2e" % (np.round(s, 3), np.abs(G - G.T - 1j * F).max(), np.abs(G - (M @ G).T).max()))
        # (2) KMS identity  d ln Theta/ds = -i tr(eta G)
        lhs = -1j * np.trace(eta @ G)
        h = 1e-6
        mp.mp.dps = 30
        d = mp.diff(lambda x: mp.log(theta(x, fe, fm)), mp.mpc(s))
        print("      -i tr(eta G) = %s   d ln Theta/ds = %s" % (np.round(lhs, 10), complex(d)))
    # (3) small-s limit
    s = 1e-3 * np.exp(-0.4j)
    print("small s: Theta*(16 pi^2 s^2) =", complex(theta(mp.mpc(s), fe, fm) * 16 * mp.pi ** 2 * mp.mpc(s) ** 2), " (expect -i(1 + s^2 (fm^2-fe^2)/6))",
          -1j * (1 + s ** 2 * (fm ** 2 - fe ** 2) / 6))
    # (1) magnetic plane by Landau-level sum: density per unit area = (f/2pi) sum_n exp(-i s f (2n+1)), s -> s - i0
    s = 0.37 * np.exp(-0.2j)
    lev = sum((fm / (2 * np.pi)) * np.exp(-1j * s * fm * (2 * n + 1)) for n in range(4000))
    print("Landau-level sum vs f/(4 pi i sin(s f)):", lev, fm / (4 * np.pi * 1j * np.sin(s * fm)))
    # electric plane: continuation of oscillator trace 1/(2i sin(kappa s)) with kappa^2 -> -E^2 (kappa = i E): density f/(4 pi sinh) ; sign fixed by small-s free limit 1/(4 pi s)
    s = 0.01
    print("electric plane small-s: f_e/(4 pi sinh(s f_e)) * 4 pi s =", fe / np.sinh(s * fe) * s, "(free limit 1)")
    # Weyl check of the electric plane free limit: int dw0 dw1/(2pi)^2 exp(-i s (-w0^2+w1^2)) = 1/(4 pi s)
    print("free electric plane integral (analytic): 1/(4 pi s) =", 1 / (4 * np.pi * s))
