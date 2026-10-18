"""032 engine_mp: multiprecision version of engine.second_order for F in block-diagonal (Lorentz) frame
F_01 = a (electric, real eigenvalue pair of F eta), F_23 = b (magnetic).  Any other Lorentz frame is obtained by rotating (kappa, m, n) -- the physics is covariant.
Needed because the kappa^2 coefficient is a difference of exponentially large terms at large |s| (double precision overflows beyond rho ~ 8).
Same formulas as engine.py (see its docstring).  k2coef(...) = (T(lam kappa) - T(0)) / lam^2 / ... returns T2/Theta kappa^2-coefficient."""
import mpmath as mp, numpy as np
mp.mp.dps = 60
ETA = [-1, 1, 1, 1]

def mpm(rows):
    return np.array(rows, dtype=object)

def zeros(n, m=None):
    m = n if m is None else m
    return np.array([[mp.mpc(0)] * m for _ in range(n)], dtype=object)

def eye4():
    Z = zeros(4)
    for i in range(4):
        Z[i, i] = mp.mpc(1)
    return Z

ETAM = zeros(4)
for _i in range(4):
    ETAM[_i, _i] = mp.mpc(ETA[_i])

def blocks(a, b, t):
    """exp(t K) and Phi(t)=int_0^t exp(t'K) dt' for K = 2 F eta, F=F01=a,F23=b, complex t."""
    M = zeros(4); P = zeros(4)
    ch, sh = mp.cosh(2 * a * t), mp.sinh(2 * a * t)
    M[0, 0] = M[1, 1] = ch; M[0, 1] = M[1, 0] = sh
    P[0, 0] = P[1, 1] = sh / (2 * a); P[0, 1] = P[1, 0] = (ch - 1) / (2 * a)
    c, s = mp.cos(2 * b * t), mp.sin(2 * b * t)
    M[2, 2] = M[3, 3] = c; M[2, 3] = s; M[3, 2] = -s
    P[2, 2] = P[3, 3] = s / (2 * b); P[2, 3] = (1 - c) / (2 * b); P[3, 2] = -(1 - c) / (2 * b)
    return M, P

def inv2(X):
    d = X[0, 0] * X[1, 1] - X[0, 1] * X[1, 0]
    return mpm([[X[1, 1] / d, -X[0, 1] / d], [-X[1, 0] / d, X[0, 0] / d]])

def Gmat(a, b, s):
    F = zeros(4)
    F[0, 1] = a; F[1, 0] = -a; F[2, 3] = b; F[3, 2] = -b
    M, _ = blocks(a, b, s)
    MT = M.T
    I = eye4()
    X = I - MT
    Xi = zeros(4)
    Xi[:2, :2] = inv2(X[:2, :2]); Xi[2:, 2:] = inv2(X[2:, 2:])
    return -1j * F.dot(MT).dot(Xi)

def E4(mu, P, w):
    m1, m2, m3, m4 = mu
    d = [mp.mpc(x) for x in ETA]
    # use diagonal eta: eta^{ab} = d[a] delta_ab
    tot = mp.mpc(0)
    for a_ in range(4):
        for c_ in range(4):
            wa, wc = d[a_], d[c_]
            # item1 index a, item2 index a (b=a), item3 index c, item4 index c (d=c)
            tot += wa * wc * (m1[a_] * m2[a_] * m3[c_] * m4[c_]
                              + P[(1, 2)][a_, a_] * m3[c_] * m4[c_]
                              + P[(1, 3)][a_, c_] * m2[a_] * m4[c_]
                              + P[(1, 4)][a_, c_] * m2[a_] * m3[c_]
                              + P[(2, 3)][a_, c_] * m1[a_] * m4[c_]
                              + P[(2, 4)][a_, c_] * m1[a_] * m3[c_]
                              + P[(3, 4)][c_, c_] * m1[a_] * m2[a_]
                              + P[(1, 2)][a_, a_] * P[(3, 4)][c_, c_]
                              + P[(1, 3)][a_, c_] * P[(2, 4)][a_, c_]
                              + P[(1, 4)][a_, c_] * P[(2, 3)][a_, c_])
    return tot

def factor_items(kind, sig, m, n, kappa):
    I4 = eye4()
    zero = np.array([mp.mpc(0)] * 4, dtype=object)
    if kind == 1:
        return (I4, sig * kappa), (m, n)
    return (m, n), (I4, zero)

GLX = {}
def gl(nn):
    if nn not in GLX:
        x, w = np.polynomial.legendre.leggauss(nn)
        GLX[nn] = ([mp.mpf((xx + 1) / 2) for xx in x], [mp.mpf(ww / 2) for ww in w])
    return GLX[nn]

def second_order_mp(a, b, kappa, m, n, s, nquad=12):
    """T2(s)/Theta(s); a,b mpf; kappa (lower index), n arrays of mp numbers; m 4x4 object array; s mpc."""
    a = mp.mpf(a); b = mp.mpf(b)
    kup = ETAM.dot(kappa)
    us, ws = gl(nquad)
    G = Gmat(a, b, s)
    w = ETAM
    V2 = mp.mpc(0)
    for i in range(4):
        for j in range(4):
            if i == j:
                V2 += ETA[i] * (m[i].dot(G).dot(m[j]) + n[i] * n[j])
    total = -1j * s * V2 / 2
    acc = mp.mpc(0)
    for u, wu in zip(us, ws):
        tau = s * u
        M, Phi = blocks(a, b, tau)
        for sig in (1, -1):
            l = 2j * sig * (Phi.T.dot(kup))
            ph = mp.exp(-1j * kup.dot(Phi).dot(kappa))
            pref = ph * mp.exp(l.dot(G).dot(l) / 2)
            for k1 in (1, 2):
                it1 = factor_items(k1, sig, m, n, kappa)
                v1 = []
                for vec, c0 in it1:
                    vp = vec.dot(M)
                    v1.append((vp, c0 - sig * vp.dot(kappa)))
                for k2 in (1, 2):
                    it2 = factor_items(k2, -sig, m, n, kappa)
                    items = v1 + list(it2)
                    mu = [c0 + vec.dot(G.T).dot(l) for vec, c0 in items]
                    P = {}
                    for i in range(4):
                        for j in range(i + 1, 4):
                            P[(i + 1, j + 1)] = items[i][0].dot(G).dot(items[j][0].T)
                    acc += wu * (1 - u) * pref * E4(mu, P, w) / 4
    return total - s ** 2 * acc

def to_mp_vec(v):
    return np.array([mp.mpf(float(x)) for x in v], dtype=object)

def to_mp_mat(M):
    return np.array([[mp.mpf(float(x)) for x in row] for row in M], dtype=object)

def k2coef(a, b, kappa, m, n, s, nquad=12, lam=mp.mpf('1e-15')):
    ka = to_mp_vec(kappa) if not isinstance(kappa[0], mp.mpf) else kappa
    t1 = second_order_mp(a, b, lam * ka, m, n, s, nquad)
    t0 = second_order_mp(a, b, 0 * ka, m, n, s, nquad)
    return (t1 - t0) / lam ** 2
