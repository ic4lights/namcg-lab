"""032 engine: exact second-order response of the Landau problem to a plane-wave vielbein (metric) and gauge perturbation.

Operator algebra (4 kinetic momenta):  [omega_a, omega_b] = i F_ab (constant),  omega_a e^{i kappa.x} = e^{i kappa.x}(omega_a + kappa_a),  eta = diag(-1,1,1,1).
H(eps) = eta^{ab} Omega_a Omega_b,   Omega_a = omega_a + eps sin(phi) (u_a + n_a),   u_a = m_a^c omega_c,   phi = kappa.x,
with the divergence-free condition m_a^c kappa_c = 0 (so Omega_a is symmetric and u_a commutes with e^{i phi}).
  m = 0 : pure gauge field a_b = eps n_b sin(phi);   n = 0 : pure vielbein perturbation e_a^c = delta_a^c + eps sin(phi) m_a^c.
  The frozen sector of proposal 030 is  m_a^c = -alpha_a y^c,  n_a = -alpha_a c   (y.kappa = 0), c = vertical charge.
Second order in eps (per unit coordinate volume, phase-averaged):
  Tr e^{-isH}|_{eps^2} = Theta(s) * { -i s <V2> - s^2 int_0^1 du (1-u) <V1(su) V1(0)> },
  V2 = eta^{ab} S^2 (u_a+n_a)(u_b+n_b) -> (1/2) eta^{ab}(u_a+n_a)(u_b+n_b),   V1 = eta^{ab}(omega_a S (u_b+n_b) + S (u_a+n_a) omega_b),
evaluated with the quasi-free (KMS) state rho = e^{-isH0}/Tr:  <omega_a omega_b> = G_ab = -i F M^T (1-M^T)^{-1}, M = exp(2 s F eta), Wick's theorem,
the Heisenberg picture omega(t) = exp(2 t F eta) omega, x(t)-x(0) = 2 eta int_0^t omega(t') dt', and the exponentials moved to the left:
  e^{i s_ phi(tau)} v_s(omega(tau)) e^{-i s_ phi(0)} v_-s(omega(0)) = e^{-i kappa^T eta Phi kappa} e^{L} v_s(omega(tau) - s_ M kappa) v_-s(omega(0)),
  L = 2 i s_ (Phi^T eta kappa).omega,   Phi(tau) = int_0^tau exp(t 2 F eta) dt.
Returns T2(s)/Theta(s) (complex).  Verified against closed forms in s5_engine_checks.py."""
import numpy as np, scipy.linalg as sl
eta = np.diag([-1., 1, 1, 1])
GL = {}

def gl_nodes(n):
    if n not in GL:
        x, w = np.polynomial.legendre.leggauss(n)
        GL[n] = ((x + 1) / 2, w / 2)
    return GL[n]

def G_and_M(F, s, tau_list):
    K = 2 * F @ eta
    if np.abs(F).max() < 1e-12:
        G = -1j * eta / (2 * s)
        Ms = [np.eye(4) for _ in tau_list]
        Ph = [t * np.eye(4) for t in tau_list]
        return G, Ms, Ph
    M = sl.expm(s * K)
    G = -1j * F @ M.T @ np.linalg.inv(np.eye(4) - M.T)
    Ms, Ph = [], []
    big = np.zeros((8, 8), complex); big[:4, :4] = K; big[:4, 4:] = np.eye(4)
    for t in tau_list:
        E = sl.expm(t * big)
        Ms.append(E[:4, :4]); Ph.append(E[:4, 4:])
    return G, Ms, Ph

def E4_sum(mu, P, w):
    """mu: list of 4 arrays (len 4) for items 1..4 (items 1,2 carry index pair (a,b) with weight w=eta^{ab}; items 3,4 index pair (c,d) with eta^{cd});
    P: dict (i,j)->(4x4) matrix of pair contractions between index of item i and item j.  Full Wick sum over (a,b,c,d) with eta^{ab} eta^{cd}."""
    m1, m2, m3, m4 = mu
    e = np.einsum
    t = e('a,b,c,d,ab,cd->', m1, m2, m3, m4, w, w)
    t += e('ab,c,d,ab,cd->', P[(1, 2)], m3, m4, w, w)
    t += e('ac,b,d,ab,cd->', P[(1, 3)], m2, m4, w, w)
    t += e('ad,b,c,ab,cd->', P[(1, 4)], m2, m3, w, w)
    t += e('bc,a,d,ab,cd->', P[(2, 3)], m1, m4, w, w)
    t += e('bd,a,c,ab,cd->', P[(2, 4)], m1, m3, w, w)
    t += e('cd,a,b,ab,cd->', P[(3, 4)], m1, m2, w, w)
    t += e('ab,cd,ab,cd->', P[(1, 2)], P[(3, 4)], w, w)
    t += e('ac,bd,ab,cd->', P[(1, 3)], P[(2, 4)], w, w)
    t += e('ad,bc,ab,cd->', P[(1, 4)], P[(2, 3)], w, w)
    return t

def factor_items(kind, sig, m, n, kappa):
    """items of v_sig: kind 1: (omega_a + sig kappa_a) , (u_b + n_b);  kind 2: (u_a + n_a), omega_b.  Returns two (vec(4x4 rows), const(4)) pairs."""
    I4 = np.eye(4)
    if kind == 1:
        return (I4, sig * kappa), (m, n)
    return (m, n), (I4, np.zeros(4))

def second_order(F, kappa, m, n, s, nquad=24):
    """T2(s)/Theta(s).  F: 4x4 antisymmetric (lower indices); kappa: lower-index covector; m: 4x4 (m_a^c), n: 4-vector (n_a); s complex."""
    F = np.array(F, float); kappa = np.array(kappa, float); m = np.array(m, float); n = np.array(n, float)
    assert np.abs(m @ kappa).max() < 1e-9 * (1 + np.abs(m).max() * np.abs(kappa).max()), "need m kappa = 0"
    kup = eta @ kappa
    us, ws = gl_nodes(nquad)
    taus = [s * u for u in us]
    G, Ms, Ph = G_and_M(F, s, taus)
    w = eta.copy()
    # V2 term
    mm = m.T  # (u_a)=m_a^c omega_c -> vec_a = m[a,:]
    V2 = 0.5 * np.einsum('ab,ab->', w, np.array([[m[a] @ G @ m[b] + n[a] * n[b] for b in range(4)] for a in range(4)]))
    total = -1j * s * V2
    acc = 0j
    for u, wu, tau, M, Phi in zip(us, ws, taus, Ms, Ph):
        for sig in (+1, -1):
            l = 2j * sig * (Phi.T @ kup)
            ph = np.exp(-1j * kup @ Phi @ kappa)
            pref = ph * np.exp(0.5 * l @ G @ l)
            for k1 in (1, 2):
                it1 = factor_items(k1, sig, m, n, kappa)
                # time-tau transformation of items: vec' = M^T vec, const' = const - sig * vec'.kappa
                v1 = []
                for vec, c0 in it1:
                    vp = vec @ M            # rows: (M^T vec_row)^T = vec_row @ M
                    v1.append((vp, c0 - sig * vp @ kappa))
                for k2 in (1, 2):
                    it2 = factor_items(k2, -sig, m, n, kappa)
                    items = v1 + [(vec, c0) for vec, c0 in it2]
                    mu = [c0 + vec @ G.T @ l * 1.0 for vec, c0 in items]      # <L (vec.omega)> = l^T G vec  = (vec @ G.T) @ l
                    P = {}
                    for i in range(4):
                        for j in range(i + 1, 4):
                            P[(i + 1, j + 1)] = items[i][0] @ G @ items[j][0].T
                    val = E4_sum(mu, P, w) * 0.25
                    acc += wu * (1 - u) * pref * val
    total += -s ** 2 * acc
    return total

def theta_ab(F):
    ev = np.linalg.eigvals(F @ eta)
    a = np.max(np.abs(ev.real)); b = np.max(np.abs(ev.imag))
    return a, b
