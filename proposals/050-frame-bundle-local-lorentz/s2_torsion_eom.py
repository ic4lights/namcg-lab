"""
s2: the matrix equation in the first-order equivariant class with torsion, exact arithmetic (sparse polynomial ring over Q).

Input: frame e_b^mu(y), unipotent triangular with polynomial entries, and a metric connection w_mu^c_d(y) with polynomial
entries, antisymmetric after lowering with eta, not related to e.  Define T and R on the bundle by
    [D_a, D_b] = - T_ab^c D_c + (1/2) R_ab^{cd} S_cd   (sum over all ordered c,d),
and verify as identities at rational points of the Lorentz subbundle
    [D^a,[D_a,D_b]] = ( - D^a T_ab^e + T_ab^c T^a_c^e + R_ab^{ae} ) D_e
                      + (1/2)( D^a R_ab^{de} - T_ab^c R^a_c^{de} ) S_de .
Also: the divergence of D_a in the measure |det e|^{-1} d^dy dHaar(u), against the torsion trace T_ac^c.
"""
import random, sys
import sympy as sp
from sympy import QQ, ring


def rational_lorentz(d):
    def boost(axis, n, m):
        M = sp.eye(d); c = sp.Rational(m*m+n*n, m*m-n*n); s = sp.Rational(2*m*n, m*m-n*n)
        M[0, 0] = c; M[axis, axis] = c; M[0, axis] = s; M[axis, 0] = s
        return M
    def rot(i, j, n, m):
        M = sp.eye(d); c = sp.Rational(m*m-n*n, m*m+n*n); s = sp.Rational(2*m*n, m*m+n*n)
        M[i, i] = c; M[j, j] = c; M[i, j] = -s; M[j, i] = s
        return M
    return boost(1, 1, 3)*rot(1, 2, 1, 2)*boost(2, 1, 2)


def run(d, seed):
    random.seed(seed)
    names = ['y%d' % i for i in range(d)] + ['u%d_%d' % (a, b) for a in range(d) for b in range(d)]
    Rg, *gens = ring(names, QQ)
    L = rational_lorentz(d)
    # Taylor jets about the point: y = y0 + delta, u = L + delta, truncated at total degree ORDER
    ORDER = 2  # enough for two derivatives at the base point
    y = [gens[i] + QQ(i+1, 7) for i in range(d)]
    u = [[gens[d+d*a+b] + QQ(int(L[a, b].p), int(L[a, b].q)) for b in range(d)] for a in range(d)]
    N = len(gens)
    def tr(p):
        return Rg.from_dict({m: c for m, c in p.terms() if sum(m) <= ORDER})
    eta = [-1]+[1]*(d-1)
    uidx = lambda a, b: d+d*a+b
    def rr(den=4):
        return QQ(random.randint(-3, 3), random.randint(1, den))
    linear = lambda: Rg(rr()) + sum(y[i]*rr() for i in range(d))
    quad = lambda: linear() + sum(y[i]*y[j]*rr() for i in range(d) for j in range(d))
    # frame e[b][mu]: unipotent upper triangular
    e = [[Rg(1) if i == j else (tr(quad()) if j > i else Rg(0)) for j in range(d)] for i in range(d)]
    # th = e^{-1} by back substitution, th[mu][b]
    th = [[Rg(0) for _ in range(d)] for _ in range(d)]
    for i in reversed(range(d)):
        for j in range(d):
            th[i][j] = (Rg(1) if i == j else Rg(0)) - sum((tr(e[i][k]*th[k][j]) for k in range(i+1, d)), Rg(0))
    w = []
    for mu in range(d):
        m = [[Rg(0) for _ in range(d)] for _ in range(d)]
        for c in range(d):
            for f in range(c+1, d):
                val = linear()
                m[c][f] = val*eta[c]
                m[f][c] = -val*eta[f]
        w.append(m)
    Uinv = [[u[b][a]*(eta[a]*eta[b]) for b in range(d)] for a in range(d)]   # Uinv[a][b] = eta^{aa} u_b^a eta_{bb}: (u^{-1})^a_b

    def apply(V, f):
        out = Rg(0)
        for k in range(N):
            if V[k] != 0:
                out += tr(V[k]*f.diff(gens[k]))
        return out
    def comm(V, W):
        return [apply(V, W[k]) - apply(W, V[k]) for k in range(N)]

    D = []
    for a in range(d):
        V = [Rg(0)]*N
        for mu in range(d):
            co = tr(sum((u[a][b]*e[b][mu] for b in range(d)), Rg(0)))
            V[mu] = co
            for f in range(d):
                for c in range(d):
                    t = tr(sum((u[f][g]*w[mu][c][g] for g in range(d)), Rg(0)))
                    V[uidx(f, c)] = tr(V[uidx(f, c)] - co*t)
        D.append(V)

    def coeffs(V):
        # alpha^a from the y part: V^mu = alpha^a u_a^b e_b^mu; (u^{-1}) with (u^{-1})_b^a = eta^{aa} u_a... on the subbundle
        # u eta u^T = eta => u^{-1} = eta u^T eta, (u^{-1})^b_a index positions: u_a^b (u^{-1})_b^c = delta_a^c
        alpha = [Rg(0)]*d
        for a in range(d):
            tmp = Rg(0)
            for mu in range(d):
                for b in range(d):
                    tmp += tr(tr(V[mu]*th[mu][b])*Uinv[b][a])
            alpha[a] = tmp
        dV = [[V[uidx(a, b)] - sum((tr(alpha[c]*D[c][uidx(a, b)]) for c in range(d)), Rg(0)) for b in range(d)] for a in range(d)]
        # dV_a^b = beta^{f g}(eta_{a g} u_f^b) summed over all f,g with beta antisymmetric
        # => beta^f_a = dV_a^b (u^{-1})_b^f
        beta = [[Rg(0) for _ in range(d)] for _ in range(d)]
        for f in range(d):
            for g in range(d):
                beta[f][g] = sum((tr(dV[g][b]*Uinv[b][f]) for b in range(d)), Rg(0))*eta[g]
        return alpha, beta

    Tc, Rc, Fab = {}, {}, {}
    for a in range(d):
        for b in range(a+1, d):
            F = comm(D[a], D[b])
            Fab[(a, b)] = F
            al, be = coeffs(F)
            Tc[(a, b)] = [-v for v in al]
            Rc[(a, b)] = be
    def F(a, b):
        if a == b: return [Rg(0)]*N
        return Fab[(a, b)] if a < b else [-v for v in Fab[(b, a)]]
    def T(a, b, c):
        if a == b: return Rg(0)
        return Tc[(a, b)][c] if a < b else -Tc[(b, a)][c]
    def R(a, b, f, g):
        # the vertical part of F is sum over ordered f,g of beta^{fg} S-type with S_fg acting as eta_{a g}u_f - eta_{a f}u_g,
        # i.e. sum_{f<g} rho^{fg} S_fg with rho = beta^{fg}; the convention (1/2) R^{fg} S_fg over ordered pairs gives R = rho
        if a == b: return Rg(0)
        return Rc[(a, b)][f][g] if a < b else -Rc[(b, a)][f][g]

    ev = lambda p: p.coeff(1) if p != 0 else QQ(0)   # value at the base point: constant term of the jet
    # consistency: alpha, beta reconstruct, beta antisymmetric at the point
    anti_ok = all(ev(Rc[(a, b)][f][g] + Rc[(a, b)][g][f]) == 0 for (a, b) in Rc for f in range(d) for g in range(d))
    # torsion on the section: T_ab^c at u=1 equals e_a(e_b^mu)th - e_b(e_a^mu)th ... reported through the identity below only
    okD, okS = True, True
    mx = 0
    for b in range(d):
        V = [Rg(0)]*N
        for a in range(d):
            cc = comm(D[a], F(a, b))
            V = [V[k] + cc[k]*eta[a] for k in range(N)]
        al, be = coeffs(V)
        for g in range(d):
            rhs = Rg(0)
            for a in range(d):
                rhs += -apply(D[a], T(a, b, g))*eta[a]
                for c in range(d):
                    rhs += tr(T(a, b, c)*T(a, c, g))*eta[a]
                rhs += R(a, b, a, g)
            lhs_v, rhs_v = ev(al[g]), ev(rhs)
            mx = max(mx, abs(lhs_v))
            if lhs_v != rhs_v:
                okD = False
        for f in range(d):
            for g in range(f+1, d):
                rhs = Rg(0)
                for a in range(d):
                    rhs += apply(D[a], R(a, b, f, g))*eta[a]
                    for c in range(d):
                        rhs += -tr(T(a, b, c)*R(a, c, f, g))*eta[a]
                if ev(be[f][g]) != ev(rhs):
                    okS = False
    # divergence: the frame is unimodular so sqrt|g| is 1; vertical part: coefficient times right-multiplication fields, which are Haar divergence free
    divs, trs = [], []
    for a in range(d):
        hor = Rg(0)
        for mu in range(d):
            hor += sum((tr(u[a][b]*e[b][mu].diff(gens[mu])) for b in range(d)), Rg(0))
        ver = Rg(0)
        for mu in range(d):
            for b in range(d):
                for g in range(d):
                    ver += -tr(tr(u[a][g]*w[mu][b][g])*e[b][mu])
        divs.append(ev(hor+ver))
        trs.append(ev(sum((T(a, c, c) for c in range(d)), Rg(0))))
    print(f'd={d} seed={seed}: beta antisym {anti_ok}; D-part formula {okD}; S-part formula {okS}; '
          f'div D_a = T_ac^c for all a: {divs == trs}; = -T_ac^c: {divs == [-t for t in trs]}; max|coefficient| {float(mx):.4g}', flush=True)
    assert anti_ok and okD and okS


run(3, 50)
run(3, 51)
run(4, 52)
