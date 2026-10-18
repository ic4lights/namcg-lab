"""Two linearised null waves about a constant Lorentzian Theta_bar (J = 0 at first order), and the quartic S of the a_2 identity.
Setting (eta = diag(-1,1,1,1)): Theta = Theta_bar + eps sum_i T_i cos-type waves, T_i^{mu nu} = -(q_i^mu u_i^nu - u_i^mu q_i^nu), q_i = Theta_bar p_i,
J^(1)=0 requires q_i^2 = eta(q_i,q_i) = 0 and u_i . q_i = 0.  First-order connection b_sigma = G_{sigma tau} Theta_bar^{rho tau} d_rho Theta^{mu nu}.
S(b) = tr_V[(b.b)^2] - n_D tr_D[(beta.beta)^2], n_D = 2, contraction G^{sigma tau}, spinors via Cl(3,1) gammas.  (The identity a_2^{tot} = (1/2) sqrt|G| S is an
algebraic identity proved/verified in the Euclidean section; its Lorentzian form is its analytic continuation, not separately checked here.)"""
import numpy as np
rng = np.random.default_rng(4)
eta = np.diag([-1., 1, 1, 1])
etai = np.linalg.inv(eta)
# Cl(3,1) gammas, {g^m, g^n} = 2 eta^{mn}
s = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
Z = np.zeros((2, 2), complex); E2 = np.eye(2, dtype=complex)
g0 = 1j*np.block([[Z, E2], [E2, Z]]) @ np.diag([1, 1, 1, 1])
# build: gamma^0 anti-Hermitian squares to -1; gamma^k Hermitian
g0 = np.block([[Z, 1j*E2], [1j*E2, Z]])
gk = [np.block([[Z, 1j*s[k]], [-1j*s[k], Z]]) for k in range(3)]
# fix: choose standard chiral Dirac: gamma^0 = [[0,1],[1,0]]*i? verify Clifford numerically
gam = [g0] + gk
def cliff_err(gam):
    err = 0
    for m in range(4):
        for n in range(4):
            ac = gam[m]@gam[n] + gam[n]@gam[m]
            err = max(err, np.abs(ac - 2*etai[m, n]*np.eye(4)).max())
    return err
if cliff_err(gam) > 1e-12:
    # alternative: gamma^0 = i*[[0,1],[1,0]] , gamma^k = [[0,-i s],[i s,0]]
    g0 = 1j*np.block([[Z, E2], [E2, Z]])
    gk = [np.block([[Z, -1j*s[k]], [1j*s[k], Z]]) for k in range(3)]
    gam = [g0] + gk
print('Clifford error:', cliff_err(gam))
gmn = [[0.5*(gam[m]@gam[n] - gam[n]@gam[m]) for n in range(4)] for m in range(4)]   # gamma^{mn}, upper indices

def S_of_b(bmat, Ginv_, nD=2):
    """bmat[s]: 4x4 matrices (b_s)^m_n  (so(3,1) valued, vector rep); returns S."""
    bb = sum(Ginv_[s_, t]*bmat[s_]@bmat[t] for s_ in range(4) for t in range(4))
    trV = np.trace(bb@bb)
    # spinor lift: beta_s = (1/4) gamma^{mn} b_{s,mn},  b_{s,mn} = eta_{ma} (b_s)^a_n
    beta = []
    for s_ in range(4):
        lower = eta@bmat[s_]       # b_{mn} = eta_{ma} b^a_n
        beta.append(0.25*sum(lower[m, n]*gmn[m][n] for m in range(4) for n in range(4)))
    bbD = sum(Ginv_[s_, t]*beta[s_]@beta[t] for s_ in range(4) for t in range(4))
    trD = np.trace(bbD@bbD)
    return trV - nD*trD

# Theta_bar = a d0^d1 + b d2^d3  (toy of the manuscript) ; Lorentzian K = Theta^T eta Theta
a_, b_ = 1.3, 0.9
Tb = np.zeros((4, 4)); Tb[0, 1] = a_; Tb[1, 0] = -a_; Tb[2, 3] = b_; Tb[3, 2] = -b_
K = Tb.T@eta@Tb        # K^{mn} = G^{mn}
G = np.linalg.inv(K)
print('K = G^{-1} diag:', np.diag(K), ' (signature check)')
def null_wave():
    # find p with K(p,p) = 0, i.e. q = Tb p has eta(q,q)=0; random direction scaled
    while True:
        p = rng.normal(size=4)
        # solve K(p,p)=0 by rescaling the first component
        # K(p,p) = sum K_mm p_m^2 (diagonal) ; K = diag(a^2, -a^2, b^2, b^2)
        pp = p.copy()
        rest = K[1,1]*pp[1]**2 + K[2,2]*pp[2]**2 + K[3,3]*pp[3]**2
        pp[0] = np.sqrt(-rest/K[0,0]) if -rest/K[0,0] >= 0 else None
        if pp[0] is None or np.isnan(pp[0]): continue
        q = Tb@pp
        # polarisation u with eta(u,q) = 0
        u = rng.normal(size=4); u = u - (q@eta@u)/(q@eta@q + 0j) * q if abs(q@eta@q) > 1e-9 else u
        return pp, q, u
def fieldstrength(q, u):
    # T^{mn} = -(q^m u^n - u^m q^n)  upper indices
    return -(np.outer(q, u) - np.outer(u, q))
waves = []
for i in range(2):
    pp, q, u = null_wave()
    # polarisation: need eta(u,q)=0 ; q is eta-null here? check
    print('wave', i, ' eta(q,q) =', q@eta@q, ' K(p,p) =', pp@K@pp)
    # choose u with eta(u,q)=0
    uu = rng.normal(size=4)
    # project: u -> u - (eta(u,q)/eta(w,q)) w with w generic having eta(w,q)!=0
    w = rng.normal(size=4)
    uu = uu - (uu@eta@q)/(w@eta@q)*w
    waves.append((pp, q, uu))
    print('        eta(u,q) =', uu@eta@q)
def bmats(cs):
    # first-order b_sigma = G_{sigma tau} Tb^{rho tau} d_rho Theta^{mu nu}, with d_rho Theta^{(1)} = -eps p_rho sin(..) T ... use amplitude factors cs[i]
    # B^tau_{mu nu}: Theta_bar^{rho tau} p_rho T_i^{mu nu} c_i = (p Tb)^tau ... -> contravariant vector Tb^{rho tau} p_rho = -(Tb p)^tau = -q^tau
    out = np.zeros((4, 4, 4), complex)   # (b_s)^m_n
    for i, (pp, q, u) in enumerate(waves):
        T = fieldstrength(q, u)          # upper-index T^{mn}
        Tmix = T@eta                     # T^m_n = T^{ma} eta_{an}
        lam = G@(-q)                     # lower index: G_{s tau} B^tau, B^tau ~ -q^tau
        for s_ in range(4):
            out[s_] += cs[i]*lam[s_]*Tmix
    return out
Ginv_ = K
print('S for single wave 1 :', S_of_b(bmats([1.0, 0.0]), Ginv_))
print('S for single wave 2 :', S_of_b(bmats([0.0, 1.0]), Ginv_))
# quartic polynomial P(c1,c2): fit coefficients by sampling
import itertools
samples = []
for _ in range(40):
    c = rng.normal(size=2)
    samples.append((c, S_of_b(bmats(c), Ginv_)))
A = np.array([[c[0]**4, c[0]**3*c[1], c[0]**2*c[1]**2, c[0]*c[1]**3, c[1]**4] for c, _ in samples])
y = np.array([v for _, v in samples])
coef, res, rk, sv = np.linalg.lstsq(A, y, rcond=None)
print('P(c1,c2) coefficients [c1^4, c1^3c2, c1^2c2^2, c1c2^3, c2^4] =', np.round(coef, 8), ' residual', np.abs(A@coef - y).max())
print('phase-average <S> = coef[2]/4 (+ coef[0]*3/8 + coef[4]*3/8) =', coef[2]/4 + 3*(coef[0]+coef[4])/8)
print('k1.k2 (eta^{-1}(p1,p2)) =', waves[0][0]@etai@waves[1][0], ' K(p1,p2)=', waves[0][0]@K@waves[1][0])
