"""040: Zeeman-dressed extension of the 034 central-Y double-Duhamel engine (engine_e_mp), canonical frame F_01=a, F_23=b, eta=diag(-1,1,1,1).

Operator content at order eps^2 (nilpotent symbol, Y -> P central at the seam, see 034):
  H_Pi  = eta^{ab} Pi_a Pi_b,  Pi_a = omega_a - eps alpha_a P sin(phi)          (scalar part, as in 034)
  Z_i   = species Zeeman matrix  = Z0_i + eps P cos(phi) N_i,
          [Pi_a,Pi_b] = i F_ab + i eps P cos(phi) K_ab,  K_ab = kappa_a alpha_b - kappa_b alpha_a.
  vector:  Z_V = 2i [Pi,Pi] eta   ->  e^{-i s Z0} = M(s) = exp(s K_F), K_F = 2 F eta,   N_V = 2i K eta.
  Dirac :  Z_D = (i/4)[Gam^a,Gam^b] [Pi_a,Pi_b]/i ...  ->  e^{-i s Z0} = exp(s (1/4)[Gam^a,Gam^b]F_ab),  N_D = (i/4)[Gam^a,Gam^b] K_ab.
Dyson expansion e^{-is(H0+U)} = e^{-isH0}[1 - i s int U + (-i)^2 s^2 int_{0<u2<u1<1} U(s u1)U(s u2)], U = V + delta,
V = -eps P (sin phi w + w sin phi), delta = eps P cos phi N (matrix on species index).
Node weights (sum over sigma = +-1 of the exponentials e^{i sig phi(tau1)} e^{-i sig phi(tau2)}):
  nVV = sum_sig pref wick4(v1,v2,P,P)/4                    (the 034 term)
  nVd = sum_sig pref wick3(v1,P,P) * (i sig/4)             (V at tau1, delta at tau2)
  ndV = sum_sig pref wick3(v2,P,P) * (-i sig/4)            (delta at tau1, V at tau2)
  ndd = sum_sig pref wick2(P,P) / 4
T2 = -i s (1/2)(a_lo.alpha) PP chi(s) - s^2 sum_nodes w [ chi nVV + tr(M(s)N)(nVd+ndV) + tr(M(s-tau) N M(tau) N) ndd ],  tau = s(u1-u2).
Species sums: chi = sum_i w_i tr M_i(s), t1 = sum_i w_i tr(M_i(s) N_i), D(tau) = sum_i w_i tr(M_i(s-tau) N_i M_i(tau) N_i).
"""
import mpmath as mp, numpy as np
from engine_mp import blocks, Gmat, ETA, zeros
from engine_e_mp import vdot, vmat, matv
import engine_e_mp as e0

mp.mp.dps = 30

GLX = {}
def gl(nn):
    if nn not in GLX:
        x, w = np.polynomial.legendre.leggauss(nn)
        GLX[nn] = ([mp.mpf((xx + 1) / 2) for xx in x], [mp.mpf(ww / 2) for ww in w])
    return GLX[nn]

def wick3(mu, P):
    m1, m2, m3 = mu
    return m1 * m2 * m3 + P[(1, 2)] * m3 + P[(1, 3)] * m2 + P[(2, 3)] * m1

def wick2(mu, P):
    m1, m2 = mu
    return m1 * m2 + P[(1, 2)]

def orbital_nodes(a, b, kappa, alpha, y, c0, s, nquad=8):
    """returns (C-term T_C/chi, list of (w, tau, nVV, nVd, ndV, ndd)).  kappa: mpf array (already scaled)."""
    a = mp.mpf(a); b = mp.mpf(b)
    eta = [mp.mpf(e) for e in ETA]
    a_lo = np.array([eta[i] * alpha[i] for i in range(4)], dtype=object)
    kup = np.array([eta[i] * kappa[i] for i in range(4)], dtype=object)
    aa = vdot(a_lo, alpha)
    G = Gmat(a, b, s); GT = G.T
    Fm = zeros(4); Fm[0, 1] = a; Fm[1, 0] = -a; Fm[2, 3] = b; Fm[3, 2] = -b
    yG = vmat(y, G); PP = c0 ** 2 + vdot(yG, y)
    TC = -1j * s * aa * PP / 2
    us, ws = gl(nquad)
    out = []
    PPpair = vdot(yG, y)
    for u1, w1 in zip(us, ws):
        for un, w2 in zip(us, ws):
            u2 = u1 * un; w = w1 * w2 * u1
            t1, t2 = s * u1, s * u2
            M1, Ph1 = blocks(a, b, t1); M2, Ph2 = blocks(a, b, t2); M12, _ = blocks(a, b, t1 - t2)
            a1 = 2 * vmat(kup, Ph1); a2 = 2 * vmat(kup, Ph2)
            comm = 1j * (vdot(a2 - a1, kappa)) + 1j * vdot(vmat(a1, Fm), a2)
            dPhi = Ph1 - Ph2
            l0 = 2j * matv(dPhi.T, kup)
            nVV = nVd = ndV = ndd = mp.mpc(0)
            for sig in (1, -1):
                l = sig * l0
                pref = mp.exp(comm / 2) * mp.exp(vdot(vmat(l, G), l) / 2)
                v1 = 2 * vmat(a_lo, M1); c1 = sig * vdot(a_lo, kappa) - 2 * sig * vdot(vmat(a_lo, M12), kappa)
                v2 = 2 * vmat(a_lo, M2); c2 = -sig * vdot(a_lo, kappa)
                items = [(v1, c1), (v2, c2), (y, c0), (y, c0)]
                mu = [c + vdot(vmat(v, GT), l) for v, c in items]
                Pm = {}
                for i in range(4):
                    for j in range(i + 1, 4):
                        Pm[(i + 1, j + 1)] = vdot(vmat(items[i][0], G), items[j][0])
                nVV += pref * e0.wick4(mu, Pm) / 4
                # V at tau1, delta at tau2
                mu3 = [mu[0], mu[2], mu[3]]
                P3 = {(1, 2): Pm[(1, 3)], (1, 3): Pm[(1, 4)], (2, 3): Pm[(3, 4)]}
                nVd += pref * wick3(mu3, P3) * (1j * sig / 4)
                # delta at tau1, V at tau2
                mu3b = [mu[1], mu[2], mu[3]]
                P3b = {(1, 2): Pm[(2, 3)], (1, 3): Pm[(2, 4)], (2, 3): Pm[(3, 4)]}
                ndV += pref * wick3(mu3b, P3b) * (-1j * sig / 4)
                ndd += pref * wick2([mu[2], mu[3]], {(1, 2): Pm[(3, 4)]}) / 4
            out.append((w, t1 - t2, nVV, nVd, ndV, ndd))
    return TC, out

# ---------------- species ----------------
def gam_matrices():
    s1 = np.array([[0, 1], [1, 0]], dtype=complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    G0 = 1j * np.kron(s1, I2)
    Gs = [np.kron(s2, s) for s in (s1, s2, s3)]
    return [G0] + Gs

def to_mpm(Mnp):
    n, m = Mnp.shape
    return np.array([[mp.mpc(Mnp[i, j]) for j in range(m)] for i in range(n)], dtype=object)

def mexp(Mat, t):
    """exp(t*Mat) for a numpy object matrix via mpmath."""
    n = Mat.shape[0]
    A = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            A[i, j] = t * Mat[i, j]
    E = mp.expm(A)
    return np.array([[E[i, j] for j in range(n)] for i in range(n)], dtype=object)

def kmat(kappa, alpha):
    return np.array([[kappa[i] * alpha[j] - kappa[j] * alpha[i] for j in range(4)] for i in range(4)], dtype=object)

class Species:
    """weight w, generator matrix KF with M(t)=exp(t KF) (= e^{-i t Z0}), and N (delta-Z coefficient matrix)."""
    def __init__(self, name, w, KF, N, Mfun=None):
        self.name = name; self.w = w; self.KF = KF; self.N = N; self.Mfun = Mfun

def vector_species(a, b, kappa, alpha, w=1):
    a = mp.mpf(a); b = mp.mpf(b)
    eta = [mp.mpf(e) for e in ETA]
    Kt = kmat(kappa, alpha)
    N = np.array([[2j * Kt[i, j] * eta[j] for j in range(4)] for i in range(4)], dtype=object)   # N_V = 2i K eta
    return Species('vec', w, None, N, Mfun=lambda t: blocks(a, b, t)[0])

def dirac_species(a, b, kappa, alpha, w=mp.mpf(-8) / 4, ncopies=4):
    """4 copies of the real 4-component spinor, total weight -1/2 per component: here the 4x4 trace is multiplied by ncopies*(-1/2)."""
    a = mp.mpf(a); b = mp.mpf(b)
    G = [to_mpm(g) for g in gam_matrices()]
    Kt = kmat(kappa, alpha)
    def comm(i, j):
        return G[i].dot(G[j]) - G[j].dot(G[i])
    KF = np.zeros((4, 4), dtype=object); N = np.zeros((4, 4), dtype=object)
    for i in range(4):
        for j in range(4):
            KF[i, j] = mp.mpc(0); N[i, j] = mp.mpc(0)
    Fm = {(0, 1): a, (1, 0): -a, (2, 3): b, (3, 2): -b}
    for (i, j), f in Fm.items():
        KF = KF + comm(i, j) * (f / 4)
    for i in range(4):
        for j in range(4):
            if i != j:
                N = N + comm(i, j) * (1j * Kt[i, j] / 4)
    return Species('dirac', mp.mpf(ncopies) * mp.mpf(-1) / 2, KF, N)

def scalar_species(w=1):
    return Species('scal', w, None, None)

def traces(sp, s, tau_list):
    """chi, t1, [D(tau)] for a species at proper time s."""
    if sp.name == 'scal':
        return 1, 0, [0] * len(tau_list)
    if sp.name == 'vec':
        Ms = sp.Mfun(s)
        chi = sum(Ms[i, i] for i in range(4))
        N = sp.N
        t1 = sum(Ms.dot(N)[i, i] for i in range(4))
        D = []
        for tau in tau_list:
            A = sp.Mfun(s - tau).dot(N).dot(sp.Mfun(tau)).dot(N)
            D.append(sum(A[i, i] for i in range(4)))
        return chi, t1, D
    if sp.name == 'dirac':
        Ms = mexp(sp.KF, s)
        chi = sum(Ms[i, i] for i in range(4))
        N = sp.N
        t1 = sum(Ms.dot(N)[i, i] for i in range(4))
        D = []
        for tau in tau_list:
            A = mexp(sp.KF, s - tau).dot(N).dot(mexp(sp.KF, tau)).dot(N)
            D.append(sum(A[i, i] for i in range(4)))
        return chi, t1, D

def T2_total(species, TC, nodes, s, weights_mass=None):
    """sum over species of the order-eps^2 response; species with weights w_i (and optional mass factors m_i) multiply their traces."""
    taus = [nd[1] for nd in nodes]
    chi = t1 = mp.mpc(0); D = [mp.mpc(0)] * len(nodes)
    for k, sp in enumerate(species):
        m = 1 if weights_mass is None else weights_mass[k]
        c_, t_, D_ = traces(sp, s, taus)
        wgt = sp.w * m
        chi += wgt * c_; t1 += wgt * t_
        D = [D[i] + wgt * D_[i] for i in range(len(nodes))]
    tot = TC * chi
    acc = mp.mpc(0)
    for i, (w, tau, nVV, nVd, ndV, ndd) in enumerate(nodes):
        acc += w * (chi * nVV + t1 * (nVd + ndV) + D[i] * ndd)
    return tot - s ** 2 * acc

def scale_kappa(kappa, lam):
    return np.array([lam * k for k in kappa], dtype=object)

def k2coef_z(species_fn, a, b, kappa, alpha, y, c0, s, nquad=8, lam=mp.mpf('1e-8'), weights_mass=None):
    """kappa^2 coefficient [T(lam)+T(-lam)-2T(0)]/(2 lam^2); species_fn(kappa_scaled) -> species list."""
    ka = np.array([mp.mpf(x) for x in kappa], dtype=object)
    al = np.array([mp.mpf(x) for x in alpha], dtype=object)
    yy = np.array([mp.mpf(x) for x in y], dtype=object)
    c0 = mp.mpf(c0)
    vals = []
    for f in (lam, -lam, 0):
        kk = scale_kappa(ka, f)
        TC, nodes = orbital_nodes(a, b, kk, al, yy, c0, s, nquad)
        vals.append(T2_total(species_fn(kk), TC, nodes, s, weights_mass))
    return (vals[0] + vals[1] - 2 * vals[2]) / (2 * lam ** 2)
