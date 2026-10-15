"""
Exact rational check of the chain proving
  rho^2 X = -2 rho R[g_rho] - rho |grad ln rho|^2_{g_rho} + (3/2) rho^2 S^2 + 2 d_mu(g_rho^{mu nu} d_nu rho)
for a FINITE-amplitude generic 2-jet of a closed omega (omega = omega0 + dA, A cubic polynomial, random rationals),
eta = diag(sig,1,1,1), sig = +-1.  Everything is rational; equalities are tested with ==.
Conventions: omega_{mu nu} closed, Theta = omega^{-1}, e^A_mu = eta^{AB} omega_{mu B}, G = e^T eta e = omega eta omega^T,
rho = |Pf omega|, g_rho = G/rho (unimodular), T^A_{mu nu} = d_mu e^A_nu - d_nu e^A_mu, T_{lmn} = eta_AB e^A_l T^B_{mn},
V_mu = G^{ln} T_{l mu n}, I_A = T_{lmn}T^{lmn}, I_B = T_{lmn}T^{mln}, S = T_[lmn].
Steps tested: (i) X = I_A; (ii) V = d ln rho; (iii) teleparallel R[G] = -(I_A/4+I_B/2-V^2) - 2 nabla V
(also for a generic non-closed coframe); (iv) conformal relation; (v) S^2=(I_A-2I_B)/3; (vi) final identity.
"""
import itertools, random
from fractions import Fraction as F
import sympy as sp
n = 4; DEG = 2
exps = [e for e in itertools.product(range(DEG+1), repeat=n) if sum(e) <= DEG]
Z = (0,)*n


class S:
    __slots__ = ['c']

    def __init__(s, c=None):
        s.c = c if c else {}

    def __add__(s, o):
        o = cs(o); r = dict(s.c)
        for k, v in o.c.items():
            r[k] = r.get(k, 0)+v
        return S(r)
    __radd__ = __add__

    def __neg__(s):
        return S({k: -v for k, v in s.c.items()})

    def __sub__(s, o):
        return s+(-cs(o))

    def __rsub__(s, o):
        return cs(o)+(-s)

    def __mul__(s, o):
        o = cs(o); r = {}
        for e, a in s.c.items():
            for f, b in o.c.items():
                g = tuple(x+y for x, y in zip(e, f))
                if sum(g) <= DEG:
                    r[g] = r.get(g, 0)+a*b
        return S(r)
    __rmul__ = __mul__

    def d(s, a):
        r = {}
        for e, v in s.c.items():
            if e[a] > 0:
                g = list(e); g[a] -= 1
                r[tuple(g)] = r.get(tuple(g), 0)+e[a]*v
        return S(r)

    def v0(s):
        return s.c.get(Z, F(0))


def cs(x):
    return x if isinstance(x, S) else S({Z: F(x)})


def ssum(it):
    r = cs(0)
    for t in it:
        r = r+t
    return r


def sinv(s):
    a = s.v0(); u = s*(F(1)/a)-1
    return (cs(1)-u+u*u)*(F(1)/a)


def mm(A, B):
    return [[ssum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def minv(A):
    A0 = sp.Matrix(n, n, lambda i, j: sp.Rational(A[i][j].v0().numerator, A[i][j].v0().denominator)).inv()
    A0s = [[cs(F(int(A0[i, j].p), int(A0[i, j].q))) for j in range(n)] for i in range(n)]
    A1 = [[A[i][j]-A[i][j].v0() for j in range(n)] for i in range(n)]
    M = mm(A0s, A1); M2 = mm(M, M)
    T = [[cs(1 if i == j else 0)-M[i][j]+M2[i][j] for j in range(n)] for i in range(n)]
    return mm(T, A0s)


def curv(g):
    gi = minv(g)
    dg = [[[g[b][c].d(a) for c in range(n)] for b in range(n)] for a in range(n)]
    Gm = [[[ssum(gi[l][d_]*(dg[c][d_][b]+dg[b][d_][c]-dg[d_][b][c]) for d_ in range(n))*F(1, 2)
            for c in range(n)] for b in range(n)] for l in range(n)]

    def Rm(al, be, c, d_):
        r = Gm[al][be][d_].d(c)-Gm[al][be][c].d(d_)
        for e in range(n):
            r = r+Gm[al][c][e]*Gm[e][be][d_]-Gm[al][d_][e]*Gm[e][be][c]
        return r
    Ric = [[ssum(Rm(al, be, al, d_) for al in range(n)) for d_ in range(n)] for be in range(n)]
    R = ssum(gi[p][q]*Ric[p][q] for p in range(n) for q in range(n))
    return gi, Gm, R


def rnd(rng, k=3):
    return F(rng.randint(-k, k), rng.randint(1, 3))


def torsion_data(e, sig):
    eta = [sig, 1, 1, 1]
    G = [[ssum(e[A][i]*e[A][j]*eta[A] for A in range(n)) for j in range(n)] for i in range(n)]
    TB = [[[e[A][nu].d(mu)-e[A][mu].d(nu) for nu in range(n)] for mu in range(n)] for A in range(n)]
    T = [[[ssum(e[A][l]*TB[A][m][nn]*eta[A] for A in range(n)) for nn in range(n)] for m in range(n)] for l in range(n)]
    return G, T


def invariants(G, T):
    gi, Gm, R = curv(G)
    rg = range(n)
    g0 = [[gi[i][j].v0() for j in rg] for i in rg]
    T0 = [[[T[l][m][nn].v0() for nn in rg] for m in rg] for l in rg]

    def up3(X):
        t = [[[sum(g0[l][a]*X[a][m][nn] for a in rg) for nn in rg] for m in rg] for l in rg]
        t = [[[sum(g0[m][a]*t[l][a][nn] for a in rg) for nn in rg] for m in rg] for l in rg]
        t = [[[sum(g0[nn][a]*t[l][m][a] for a in rg) for nn in rg] for m in rg] for l in rg]
        return t
    Tu = up3(T0)
    IA = sum(T0[l][m][nn]*Tu[l][m][nn] for l in rg for m in rg for nn in rg)
    IB = sum(T0[l][m][nn]*Tu[m][l][nn] for l in rg for m in rg for nn in rg)
    Sx = [[[(T0[l][m][nn]+T0[m][nn][l]+T0[nn][l][m])/3 for nn in rg] for m in rg] for l in rg]
    Su = up3(Sx)
    IS = sum(Sx[l][m][nn]*Su[l][m][nn] for l in rg for m in rg for nn in rg)
    Vl = [ssum(gi[l][nn]*T[l][m][nn] for l in rg for nn in rg) for m in rg]
    V0 = [v.v0() for v in Vl]
    V2 = sum(g0[a][b]*V0[a]*V0[b] for a in rg for b in rg)
    Vu = [ssum(gi[m][a]*Vl[a] for a in rg) for m in rg]
    divV = ssum(Vu[m].d(m) for m in rg)+ssum(Gm[m][m][a]*Vu[a] for m in rg for a in rg)
    return dict(R=R.v0(), IA=IA, IB=IB, IS=IS, V=V0, V2=V2, divV=divV.v0())


def run(seed, sig):
    rng = random.Random(seed); eta = [sig, 1, 1, 1]
    while True:
        w0 = [[F(0)]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                w0[i][j] = rnd(rng, 3); w0[j][i] = -w0[i][j]
        pf = w0[0][1]*w0[2][3]-w0[0][2]*w0[1][3]+w0[0][3]*w0[1][2]
        if pf != 0:
            break
    mons = [e for e in itertools.product(range(4), repeat=n) if 1 <= sum(e) <= 3]
    A = []
    for nu in range(n):
        c = {}
        for m in mons:
            if rng.random() < 0.5:
                c[m] = rnd(rng, 2)
        A.append(c)

    def Aser(nu, deriv):
        r = {}
        for e, v in A[nu].items():
            if e[deriv] > 0:
                g = list(e); g[deriv] -= 1
                if sum(g) <= DEG:
                    r[tuple(g)] = r.get(tuple(g), 0)+e[deriv]*v
        return S(r)
    om = [[cs(w0[i][j])+Aser(j, i)-Aser(i, j) for j in range(n)] for i in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                cl = om[a][b].d(c)+om[b][c].d(a)+om[c][a].d(b)
                assert all(v == 0 for v in cl.c.values())
    Pf = om[0][1]*om[2][3]-om[0][2]*om[1][3]+om[0][3]*om[1][2]
    rho = Pf*(1 if Pf.v0() > 0 else -1)
    e = [[om[mu][B]*eta[B] for mu in range(n)] for B in range(n)]
    G, T = torsion_data(e, sig)
    inv = invariants(G, T)
    rho0 = rho.v0()
    G0 = sp.Matrix(n, n, lambda i, j: sp.Rational(G[i][j].v0().numerator, G[i][j].v0().denominator))
    ok_det = (abs(G0.det()) == sp.Rational(rho0.numerator, rho0.denominator)**4)
    Th = minv(om)
    dTh = [[[Th[m][k].d(r) for k in range(n)] for m in range(n)] for r in range(n)]
    X = sum(eta[r]*eta[m]*eta[k]*dTh[r][m][k].v0()**2 for r in range(n) for m in range(n) for k in range(n))
    ok_i = (X == inv['IA'])
    ok_ii = all(inv['V'][m] == rho.d(m).v0()/rho0 for m in range(n))
    ok_iii = (inv['R'] == -(inv['IA']/4+inv['IB']/2-inv['V2'])-2*inv['divV'])
    ir = sinv(rho)
    grho = [[G[i][j]*ir for j in range(n)] for i in range(n)]
    gi_r, _, Rr = curv(grho)
    dr = [rho.d(a) for a in range(n)]
    gr0 = [[gi_r[i][j].v0() for j in range(n)] for i in range(n)]
    rr = sum(gr0[a][b]*dr[a].v0()*dr[b].v0() for a in range(n) for b in range(n))/rho0
    td = ssum(ssum(gi_r[a][b]*dr[b] for b in range(n)).d(a) for a in range(n)).v0()
    h = rho0*Rr.v0()
    ok_iv = (rho0**2*inv['R'] == h+F(3, 2)*rr-3*td)
    ok_v = (inv['IS'] == (inv['IA']-2*inv['IB'])/3)
    lhs = rho0**2*X
    rhs = -2*h-rr+F(3, 2)*rho0**2*inv['IS']+2*td
    ok_vi = (lhs == rhs)
    return ok_det, ok_i, ok_ii, ok_iii, ok_iv, ok_v, ok_vi, float(lhs), float(rhs)


def run_generic_tele(seed, sig):
    rng = random.Random(seed)
    nz = [ee for ee in exps if 1 <= sum(ee) <= 2]
    e = []
    for A in range(n):
        row = []
        for mu in range(n):
            c = {Z: rnd(rng, 3)}
            for m in nz:
                if rng.random() < 0.5:
                    c[m] = rnd(rng, 3)
            row.append(S(c))
        e.append(row)
    G, T = torsion_data(e, sig)
    inv = invariants(G, T)
    return inv['R'] == -(inv['IA']/4+inv['IB']/2-inv['V2'])-2*inv['divV']


if __name__ == '__main__':
    names = ['|detG|=rho^4', '(i) X=I_A', '(ii) V=dln rho', '(iii) teleparallel', '(iv) conformal',
             '(v) S^2 algebra', '(vi) final identity']
    allok = [True]*7; cnt = 0
    for sig in (-1, 1):
        for seed in range(6):
            r = run(seed, sig); cnt += 1
            for i in range(7):
                allok[i] &= bool(r[i])
            print('sig', sig, 'seed', seed, [bool(x) for x in r[:7]], 'lhs=%.6g rhs=%.6g' % (r[7], r[8]))
    print('cases', cnt, dict(zip(names, allok)))
    print('generic (non-closed) coframe teleparallel identity, 6 seeds x 2 signatures:',
          all(run_generic_tele(s, sg) for s in range(6) for sg in (-1, 1)))
