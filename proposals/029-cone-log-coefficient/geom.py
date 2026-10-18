"""Poisson-limit heat-kernel data from a 4x4 matrix of jets Theta^{mu nu} (Euclid eta=delta).

Conventions: operator O = -(G^{mn} d_m d_n + A^s d_s + B); Vassilevich data
  omega_s = 1/2 G_{sn}(A^n + G^{ml} Gamma^n_{ml}),
  E_V = B - G^{nm}(d_n omega_m + omega_n omega_m - omega_s Gamma^s_{nm});
O = -(nabla+omega)^2 - E_V.   a_1 density: tr(R/6 + E_V).
a_2 (mod total derivatives): (1/360) tr[60 R E_V + 180 E_V^2 + 30 Omega^2 + (5R^2 - 2Ric^2 + 2Riem^2)].
"""
import itertools
import jetlib as jl
from jetlib import Jet, mm, madd, msub, mscal, mT, mtr, meye, mdiff, minv, pf4


SIGN_OVERRIDE = None
ETA = None   # None = Euclid (delta); otherwise list of 4 diagonal entries (+-1)


def eta_diag():
    return [1, 1, 1, 1] if ETA is None else list(ETA)


def metric_data(Th):
    ed = eta_diag()
    Ginv = mm(mT([[Th[a][b] * ed[a] for b in range(4)] for a in range(4)]), Th)   # G^{mn} = eta_{ab} Theta^{a m} Theta^{b n}
    G = minv(Ginv)
    P = pf4(Th)
    if SIGN_OVERRIDE is not None:
        s = jl.ONE * SIGN_OVERRIDE
    else:
        c = P.c0()
        c = getattr(c, 'x', c)
        s = jl.ONE if c > 0 else -jl.ONE
    rho = P.inv() * s                   # rho = 1/|Pf Theta|
    return Ginv, G, rho


def christoffel(G, Ginv):
    n = 4
    dG = [mdiff(G, i) for i in range(n)]
    Gam = [[[Jet() for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for l in range(n):
        for m in range(n):
            for k in range(m, n):
                t = Jet()
                for sg in range(n):
                    t = t + Ginv[l][sg] * (dG[m][sg][k] + dG[k][sg][m] - dG[sg][m][k])
                t = t * (jl.ONE / 2)
                Gam[l][m][k] = t
                Gam[l][k][m] = t
    return Gam


def riemann(Gam, G, Ginv):
    n = 4
    Rm = {}
    for r in range(n):
        for s in range(n):
            for m in range(n):
                for k in range(n):
                    t = Gam[r][k][s].diff(m) - Gam[r][m][s].diff(k)
                    for l in range(n):
                        t = t + Gam[r][m][l] * Gam[l][k][s] - Gam[r][k][l] * Gam[l][m][s]
                    Rm[(r, s, m, k)] = t
    Ric = [[sum((Rm[(r, s, r, k)] for r in range(n)), Jet()) for k in range(n)] for s in range(n)]
    Rs = sum((Ginv[s][k] * Ric[s][k] for s in range(n) for k in range(n)), Jet())
    return Rm, Ric, Rs


def curvature_invariants(Rm, Ric, Rs, G, Ginv):
    n = 4
    g0 = [[G[i][j].c0() for j in range(n)] for i in range(n)]
    gi0 = [[Ginv[i][j].c0() for j in range(n)] for i in range(n)]
    Rl = {}
    for idx in itertools.product(range(n), repeat=4):
        r, s, m, k = idx
        Rl[idx] = sum((g0[r][a] * Rm[(a, s, m, k)].c0() for a in range(n)), jl.ZERO)
    Ric0 = [[Ric[i][j].c0() for j in range(n)] for i in range(n)]
    cur = Rl
    for pos in range(4):
        new = {}
        for idx in itertools.product(range(n), repeat=4):
            acc = jl.ZERO
            for a in range(n):
                j = list(idx)
                j[pos] = a
                acc = acc + gi0[idx[pos]][a] * cur[tuple(j)]
            new[idx] = acc
        cur = new
    riem2 = sum((Rl[k] * cur[k] for k in Rl), jl.ZERO)
    ricu = [[sum((gi0[i][a] * gi0[j][b] * Ric0[a][b] for a in range(n) for b in range(n)), jl.ZERO)
             for j in range(n)] for i in range(n)]
    ric2 = sum((Ric0[i][j] * ricu[i][j] for i in range(n) for j in range(n)), jl.ZERO)
    return riem2, ric2


def vassilevich(A, B, G, Ginv, Gam, nfib):
    n = 4
    C = [sum((Ginv[m][l] * Gam[nu][m][l] for m in range(n) for l in range(n)), Jet()) for nu in range(n)]
    omega = []
    for s in range(n):
        M = [[Jet() for _ in range(nfib)] for _ in range(nfib)]
        for nu in range(n):
            for a in range(nfib):
                for b in range(nfib):
                    M[a][b] = M[a][b] + G[s][nu] * (A[nu][a][b] + (C[nu] if a == b else Jet()))
        omega.append(mscal(M, jl.ONE / 2))
    EV = [row[:] for row in B]
    for nu in range(n):
        for m in range(n):
            T = madd(mdiff(omega[m], nu), mm(omega[nu], omega[m]))
            for sg in range(n):
                T = msub(T, [[omega[sg][a][b] * Gam[sg][nu][m] for b in range(nfib)] for a in range(nfib)])
            EV = msub(EV, [[T[a][b] * Ginv[nu][m] for b in range(nfib)] for a in range(nfib)])
    Om = [[None] * n for _ in range(n)]
    for m in range(n):
        for k in range(n):
            T = msub(mdiff(omega[k], m), mdiff(omega[m], k))
            T = madd(T, msub(mm(omega[m], omega[k]), mm(omega[k], omega[m])))
            Om[m][k] = T
    return omega, EV, Om


def a_densities(EV, Om, Rs, riem2, ric2, Ginv, nfib):
    """(a1, a2, parts) at y=0, without the sqrt(G) factor."""
    n = 4
    R0 = Rs.c0()
    trE = mtr(EV).c0()
    a1 = nfib * R0 / 6 + trE
    E0 = [[EV[i][j].c0() for j in range(nfib)] for i in range(nfib)]
    trE2 = jl.ZERO
    for i in range(nfib):
        for j in range(nfib):
            trE2 = trE2 + E0[i][j] * E0[j][i]
    gi0 = [[Ginv[i][j].c0() for j in range(n)] for i in range(n)]
    Om0 = [[[[Om[m][k][a][b].c0() for b in range(nfib)] for a in range(nfib)] for k in range(n)] for m in range(n)]
    trOm2 = jl.ZERO
    for m in range(n):
        for k in range(n):
            for p in range(n):
                for q in range(n):
                    g = gi0[m][p] * gi0[k][q]
                    if jl.isz(g):
                        continue
                    for a in range(nfib):
                        for b in range(nfib):
                            trOm2 = trOm2 + g * Om0[m][k][a][b] * Om0[p][q][b][a]
    cur = nfib * (5 * R0 * R0 - 2 * ric2 + 2 * riem2)
    a2 = (60 * R0 * trE + 180 * trE2 + 30 * trOm2 + cur) / 360
    return a1, a2, dict(R=R0, trE=trE, trE2=trE2, trOm2=trOm2, cur=cur)


def scalar_AB(Th, G, Ginv, rho):
    n = 4
    rinv = rho.inv()
    A = []
    for nu in range(n):
        t = sum(((rho * Ginv[m][nu]).diff(m) for m in range(n)), Jet())
        A.append([[t * rinv]])
    return A, [[Jet()]]


def vector_AB(Th, G, Ginv, rho):
    n = 4
    ed = eta_diag()
    As, _ = scalar_AB(Th, G, Ginv, rho)
    A = []
    for s in range(n):
        M = [[Jet() for _ in range(n)] for _ in range(n)]
        for mu in range(n):
            for nu in range(n):
                t = sum((Th[r][s] * Th[mu][nu].diff(r) for r in range(n)), Jet()) * ed[nu]
                M[mu][nu] = t * 2 + (As[s][0][0] if mu == nu else Jet())
        A.append(M)
    return A, [[Jet() for _ in range(n)] for _ in range(n)]


def dirac_AB(Th, G, Ginv, rho, gam_mn):
    """gam_mn[m][k]: nf x nf matrices of field numbers, gamma^{mk}=1/2[gamma^m,gamma^k].
    O_f = O_s - 1/2 gamma^{mk}{Theta_{mk},.}  =>  A^s = A_s^s + 1/2 gamma^{mk} Th^{rs} d_r Th_{mk}."""
    n = 4
    ed = eta_diag()
    nf = len(gam_mn[0][1])
    As, _ = scalar_AB(Th, G, Ginv, rho)
    A = []
    for s in range(n):
        M = [[Jet() for _ in range(nf)] for _ in range(nf)]
        for m in range(n):
            for k in range(n):
                coef = sum((Th[r][s] * Th[m][k].diff(r) for r in range(n)), Jet()) * (ed[m] * ed[k])
                if not coef.d:
                    continue
                for a in range(nf):
                    for b in range(nf):
                        g = gam_mn[m][k][a][b]
                        if not jl.isz(g):
                            M[a][b] = M[a][b] + coef * (g / 2)
        for a in range(nf):
            M[a][a] = M[a][a] + As[s][0][0]
        A.append(M)
    return A, [[Jet() for _ in range(nf)] for _ in range(nf)]


def sector_all(Th, gam_mn=None, verbose=False):
    """Return dict sector -> (a1, a2, parts) densities (no sqrt G), plus sqrtG=rho^2 at 0, plus J and basic data."""
    Ginv, G, rho = metric_data(Th)
    Gam = christoffel(G, Ginv)
    Rm, Ric, Rs = riemann(Gam, G, Ginv)
    riem2, ric2 = curvature_invariants(Rm, Ric, Rs, G, Ginv)
    out = {}
    A, B = scalar_AB(Th, G, Ginv, rho)
    om, EV, Om = vassilevich(A, B, G, Ginv, Gam, 1)
    out['scalar'] = a_densities(EV, Om, Rs, riem2, ric2, Ginv, 1)
    A, B = vector_AB(Th, G, Ginv, rho)
    om, EV, Om = vassilevich(A, B, G, Ginv, Gam, 4)
    out['vector'] = a_densities(EV, Om, Rs, riem2, ric2, Ginv, 4)
    if gam_mn is not None:
        A, B = dirac_AB(Th, G, Ginv, rho, gam_mn)
        nf = len(gam_mn[0][1])
        om, EV, Om = vassilevich(A, B, G, Ginv, Gam, nf)
        out['dirac'] = a_densities(EV, Om, Rs, riem2, ric2, Ginv, nf)
    sqrtG = rho.c0() ** 2
    return out, sqrtG, dict(R=Rs.c0(), riem2=riem2, ric2=ric2, rho=rho.c0())
