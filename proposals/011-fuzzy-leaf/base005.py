"""
Test whether rho^2 X, X = eta^{rl} eta_{ma} eta_{nb} d_r Theta^{mn} d_l Theta^{ab}, can be written, up to total
derivatives, as alpha*rho*R[g_rho] + beta*rho*|grad ln rho|^2_{g_rho} on the Poisson class, beyond quadratic order.

Poisson class (exact, local Darboux): omega = Theta^{-1} = psi^* omega_bar, psi = x + w(x):
  omega_{mn} = (d_m psi^a) omega_bar_{ab} (d_n psi^b),  Theta = omega^{-1}.
w = sum_j eps_j u_j exp(i p_j.x), eps_j^2 = 0.  A field is stored as {mask: coeff} (exp(i P_mask.x) implicit), so
products/derivatives are exact.  The coefficient of eps_1 eps_2 eps_3 at sum_j p_j = 0 is x-independent, and any total
derivative has zero such coefficient.  Hence a covariant rewriting with constants (alpha, beta) requires
C_X = alpha*C_h + beta*C_r for ALL samples.  Mask 3 (eps_1 eps_2, p_2 = -p_1) gives the quadratic order.
Sampled test, not a proof of non-existence in a larger candidate class.
Usage: python check_X_covariant_rewrite.py [nsamples]
"""
import numpy as np, sys
rng = np.random.default_rng(12345)
n = 4


class F:
    __slots__ = ('d',)

    def __init__(s, d=None):
        s.d = d if d is not None else {}

    def __add__(s, o):
        o = cf(o)
        r = dict(s.d)
        for k, v in o.d.items():
            r[k] = r.get(k, 0) + v
        return F(r)
    __radd__ = __add__

    def __neg__(s):
        return F({k: -v for k, v in s.d.items()})

    def __sub__(s, o):
        return s + (-cf(o))

    def __mul__(s, o):
        o = cf(o)
        r = {}
        for k1, v1 in s.d.items():
            for k2, v2 in o.d.items():
                if k1 & k2:
                    continue
                r[k1 | k2] = r.get(k1 | k2, 0) + v1*v2
        return F(r)
    __rmul__ = __mul__


def cf(x):
    return x if isinstance(x, F) else F({0: x})


ZERO = F()


def mm(A, B):
    return [[sum((A[i][k]*B[k][j] for k in range(n)), ZERO) for j in range(n)] for i in range(n)]


def mT(A):
    return [[A[j][i] for j in range(n)] for i in range(n)]


def minv(A):
    A0 = np.array([[A[i][j].d.get(0, 0) for j in range(n)] for i in range(n)], dtype=complex)
    A0i = np.linalg.inv(A0)
    N = [[F({k: v for k, v in A[i][j].d.items() if k != 0}) for j in range(n)] for i in range(n)]
    A0iF = [[cf(A0i[i][j]) for j in range(n)] for i in range(n)]
    negX = [[-e for e in row] for row in mm(A0iF, N)]
    term = [[cf(1.0 if i == j else 0.0) for j in range(n)] for i in range(n)]
    tot = [[cf(1.0 if i == j else 0.0) for j in range(n)] for i in range(n)]
    for _ in range(3):
        term = mm(term, negX)
        tot = [[tot[i][j] + term[i][j] for j in range(n)] for i in range(n)]
    return mm(tot, A0iF)


def finv(f):
    f0 = f.d.get(0, 0)
    nn = f - f0
    r = cf(1.0)
    t = cf(1.0)
    for _ in range(3):
        t = t*(-nn*(1.0/f0))
        r = r + t
    return r*(1.0/f0)


def flog(f):
    f0 = f.d.get(0, 0)
    x = (f - f0)*(1.0/f0)
    r = ZERO
    t = cf(1.0)
    for k in range(1, 4):
        t = t*x
        r = r + t*((-1)**(k+1)/k)
    return r


def run(sig, ab, ps, us, masks):
    eta = np.diag([sig, 1., 1., 1.])
    etai = np.linalg.inv(eta)
    k = len(ps)
    P = {0: np.zeros(n)}
    for m in range(1, 2**k):
        P[m] = sum(ps[j] for j in range(k) if m >> j & 1)

    def D(f, a):
        return F({m: 1j*P[m][a]*v for m, v in f.d.items()})
    w = [F({1 << j: us[j][a] for j in range(k)}) for a in range(n)]
    dw = [[D(w[a], m) for a in range(n)] for m in range(n)]
    Jm = [[cf(1.0 if m == a else 0.0) + dw[m][a] for a in range(n)] for m in range(n)]
    omb = np.zeros((n, n))
    omb[0, 1] = ab[0]; omb[1, 0] = -ab[0]; omb[2, 3] = ab[1]; omb[3, 2] = -ab[1]
    ombF = [[cf(omb[i, j]) for j in range(n)] for i in range(n)]
    om = mm(mm(Jm, ombF), mT(Jm))
    Th = minv(om)
    Pf = Th[0][1]*Th[2][3] - Th[0][2]*Th[1][3] + Th[0][3]*Th[1][2]
    rho = finv(Pf)
    etaF = [[cf(eta[i, j]) for j in range(n)] for i in range(n)]
    K = mm(mm(mT(Th), etaF), Th)
    gup = [[rho*K[i][j] for j in range(n)] for i in range(n)]
    g = minv(gup)
    dg = [[[D(g[b][c], a) for c in range(n)] for b in range(n)] for a in range(n)]
    Gam = [[[sum((gup[l][d]*(dg[c][d][b] + dg[b][d][c] - dg[d][b][c]) for d in range(n)), ZERO)*0.5
             for c in range(n)] for b in range(n)] for l in range(n)]
    dGam = [[[[D(Gam[l][b][c], a) for c in range(n)] for b in range(n)] for l in range(n)] for a in range(n)]

    def Riem(al, be, c, d):
        r = dGam[c][al][be][d] - dGam[d][al][be][c]
        for e in range(n):
            r = r + Gam[al][c][e]*Gam[e][be][d] - Gam[al][d][e]*Gam[e][be][c]
        return r
    Ric = [[sum((Riem(al, be, al, d) for al in range(n)), ZERO) for d in range(n)] for be in range(n)]
    R = sum((gup[p][q]*Ric[p][q] for p in range(n) for q in range(n)), ZERO)
    Lh = rho*R
    dl = [D(flog(rho), a) for a in range(n)]
    Lr = rho*sum((gup[a][b]*dl[a]*dl[b] for a in range(n) for b in range(n)), ZERO)
    dTh = [[[D(Th[m][nn], r) for nn in range(n)] for m in range(n)] for r in range(n)]
    X = ZERO
    for r in range(n):
        for l in range(n):
            if etai[r, l] == 0:
                continue
            for m in range(n):
                for nn in range(n):
                    for a in range(n):
                        for b in range(n):
                            c = etai[r, l]*eta[m, a]*eta[nn, b]
                            if c == 0:
                                continue
                            X = X + dTh[r][m][nn]*dTh[l][a][b]*c
    Lx = rho*rho*X
    drho = [D(rho, a) for a in range(n)]
    Ltd = sum((D(sum((gup[a][b]*drho[b] for b in range(n)), ZERO), a) for a in range(n)), ZERO)
    return {name: {mk: L.d.get(mk, 0) for mk in masks} for name, L in (('h', Lh), ('r', Lr), ('x', Lx), ('td', Ltd))}


def fit(rows):
    A = np.array([[r[0], r[1]] for r in rows])
    y = np.array([r[2] for r in rows])
    A_ri = np.vstack([A.real, A.imag])
    y_ri = np.concatenate([y.real, y.imag])
    sol = np.linalg.lstsq(A_ri, y_ri, rcond=None)[0]
    resid = y_ri - A_ri @ sol
    return sol, np.linalg.norm(resid)/np.linalg.norm(y_ri), np.linalg.norm(A_ri, axis=0), np.linalg.norm(y_ri)


if __name__ == '__main__':
    ns = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    quad, cub, td = [], [], []
    for s in range(ns):
        sig = rng.choice([1.0, -1.0])
        ab = rng.uniform(0.5, 2.5, 2)
        p1 = rng.integers(-3, 4, 4).astype(float)
        p2 = rng.integers(-3, 4, 4).astype(float)
        p3 = -p1 - p2
        us = [rng.normal(size=4) for _ in range(3)]
        o = run(sig, ab, [p1, p2, p3], us, [7])
        cub.append((o['h'][7], o['r'][7], o['x'][7]))
        td.append(abs(o['td'][7]))
        oq = run(sig, ab, [p1, -p1], us[:2], [3])
        quad.append((oq['h'][3], oq['r'][3], oq['x'][3]))
    for name, rows in (('QUADRATIC (mask eps1 eps2, p2=-p1)', quad), ('CUBIC (mask eps1 eps2 eps3, sum p = 0)', cub)):
        sol, rel, nr, ny = fit(rows)
        print(name, 'fit X = alpha*h + beta*r over', len(rows), 'random samples')
        print('  alpha, beta =', sol, ' relative residual =', rel, ' column norms', nr, ny)
    print('sanity: max |cubic coefficient of the total derivative d_a(g^{ab} d_b rho)| =', max(td), '(must be ~0; typical |C_h| scale', np.mean([abs(r[0]) for r in cub]), ')')
