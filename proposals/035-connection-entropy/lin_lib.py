"""First-order (linearised) maps about a constant Theta-bar, in terms of the second-derivative tensor S_{ab,mn} = d_a d_b delta-omega_{mn}
of a perturbation omega = omega_bar + delta-omega with d(delta-omega) = 0 and delta-omega(0) = d delta-omega(0) = 0 (cubic potential).
Euclid eta = delta; G_{mn}-bar = rho-bar^{-1}-independent: computed from Theta-bar.
All formulas exact (sympy Rational).  Conventions as geom.py / sector_data.py:
   G^{mn} = sum_a Theta^{am} Theta^{an};  b_s^{mu nu} = sum_{nu'} G_{s nu'} sum_r Theta^{r nu'} d_r Theta^{mu nu};  Omega_{st} = d_s b_t - d_t b_s (+[b,b] second order);
   tau = tr(J Omega_{12}) G^{11}  (J[0][1]=1, J[1][0]=-1, chart indices 0,1 = normal plane).
Riemann: MTW, R_{mnrs} = g_{mp} R^p_{n r s}.
"""
import itertools
import sympy as sp
from sympy import Rational as Q

def eta3_matrices():
    import lib
    return lib.eta3(), lib.etabar()

def hat_S(p, v):
    """S_{ab,mn} = p_a p_b w_{mn},  w = p^v  (plane-wave amplitude; closed).  Returns dict (a,b)->4x4 Matrix."""
    w = sp.Matrix(4, 4, lambda m, n: p[m] * v[n] - p[n] * v[m])
    return {(a, b): p[a] * p[b] * w for a in range(4) for b in range(4)}, w

def cubic_S(Ccoef):
    """S from a cubic potential A_mu = (1/6) C[mu][a][b][c] x^a x^b x^c (C symmetric in a,b,c): omega_{mn} = d_m A_n - d_n A_m.
    S_{ab,mn} = d_a d_b omega_{mn}(0) = C[n][m][a][b] - C[m][n][a][b]."""
    return {(a, b): sp.Matrix(4, 4, lambda m, n: Ccoef[n][m][a][b] - Ccoef[m][n][a][b]) for a in range(4) for b in range(4)}

def linear_data(Thb, S):
    """Thb: constant Theta-bar (4x4).  S: dict (a,b)-> 4x4 Hessian of delta-omega.  Returns first-order scalars at the point."""
    D2Th = {k: -Thb * S[k] * Thb for k in S}                                   # Hessian of delta-Theta
    Ginv_b = Thb.T * Thb
    G_b = Ginv_b.inv()
    D2Ginv = {k: D2Th[k].T * Thb + Thb.T * D2Th[k] for k in S}
    # metric perturbation h = delta G = -G Ginv' G
    H = {k: -(G_b * D2Ginv[k] * G_b) for k in S}                                 # H[(a,b)][m,n] = d_a d_b h_{mn}
    def Rl(m, n, r, s):
        return Q(1, 2) * (H[(n, r)][m, s] + H[(m, s)][n, r] - H[(m, r)][n, s] - H[(n, s)][m, r])
    Rt = {(m, n, r, s): Rl(m, n, r, s) for m in range(4) for n in range(4) for r in range(4) for s in range(4)}
    Gi = Ginv_b
    # indices raised with background inverse metric
    Ric = sp.zeros(4, 4)
    for n in range(4):
        for s in range(4):
            Ric[n, s] = sum(Gi[m, r] * Rt[(m, n, r, s)] for m in range(4) for r in range(4))
    Rs = sum(Gi[n, s] * Ric[n, s] for n in range(4) for s in range(4))
    # normal plane = chart (0,1); G-orthonormal only when G_b = rho delta; here we assume G_b = g0*delta
    g0 = G_b[0, 0]
    assert G_b == g0 * sp.eye(4), 'background metric must be conformally flat for this evaluation'
    Rii = (Ric[0, 0] + Ric[1, 1]) / g0
    Rj = sum(Rt[(i, j, i, j)] for i in range(2) for j in range(2)) / g0**2
    # Omega_{st} first order
    def Om(s, t):
        return sum((Thb[r, t] * D2Th[(s, r)] - Thb[r, s] * D2Th[(t, r)] for r in range(4)), sp.zeros(4, 4))
    J = sp.zeros(4, 4); J[0, 1] = 1; J[1, 0] = -1
    # G_{s nu'} Theta^{r nu'}: b_s = sum_{nu'} G_{s nu'} Theta^{r nu'} d_r Theta ;  with G = g0 delta:
    OmegaT = {(s, t): g0 * Om(s, t) for s in range(4) for t in range(4)}
    tau = (J * OmegaT[(0, 1)]).trace() / g0
    # Weyl squared and Riemann squared (first order amplitude squared)
    def raise4(T):
        out = {}
        for (m, n, r, s), val in T.items():
            out[(m, n, r, s)] = val
        return out
    riem2 = sum(Rt[(m, n, r, s)] ** 2 for m in range(4) for n in range(4) for r in range(4) for s in range(4)) / g0**4 * g0**0
    ric2 = sum(Ric[n, s] ** 2 for n in range(4) for s in range(4)) / g0**2
    # tr Omega^2 (sum over s,t, matrices)
    trOm2 = sum(((OmegaT[(s, t)] * OmegaT[(s, t)]).trace() / g0**2 for s in range(4) for t in range(4)), 0)
    # delta ln rho = 1/2 tr(Theta delta-omega) (first jet vanishes; only Hessian: use Hessian of ln rho)
    D2lnrho = {k: Q(1, 2) * (Thb * S[k]).trace() for k in S}
    W = Rj - Rii + Rs / 3
    Rsig = Rs - 2 * Rii + Rj
    return dict(R=Rs, Rii=Rii, Rj=Rj, W=W, Rsig=Rsig, tau=tau, riem2=riem2, ric2=ric2, trOm2=trOm2, g0=g0,
                Euler=riem2 - 4 * ric2 + Rs**2, C2=riem2 - 2 * ric2 + Rs**2 / 3, D2lnrho=D2lnrho, Rt=Rt, Ric=Ric)
