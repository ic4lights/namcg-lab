"""
s2_lichnerowicz_general.py  (proposal 047)  --  prints to stdout only; writes nothing.

General identity behind the index density.  Let E^a = E^{a mu} d_mu be any four vector fields, rho-divergence free
(rho^{-1} d_mu(rho E^{a mu}) = 0), g^{mu nu} = eta_ab E^{a mu} E^{b nu}, T^{ab mu} = [E^a,E^b]^mu,
Z^mu = -i Sigma_ab T^{ab mu} (Dirac generators, sum over ordered pairs, kappa = -1), phi = (1/2) ln(rho/sqrt|g|).
Then the Dirac operator DD = Gamma_a E^a is similar to the Levi-Civita Dirac operator of g up to the axial torsion, and
    (P1) rho^{-1} d_mu (rho T^{ab mu}) = 0,
    (P2) index density  (1/4) g_{mu nu} tr_D Z^mu Z^nu  =  -R[g] + 4 Box_g phi + 4 |d phi|^2  +  c_A A_a A^a ,
         with A^d = eps^{abcd} T_{abc} the axial torsion vector (T_{abc} = T_ab^mu e_{c mu}); c_A is fitted.
    (P3) the matrix Z_mu Z^mu in the Dirac representation is scalar + (pseudoscalar) Gamma5 part, the latter vanishing
         identically in the sampled data if and only if eps^{abcd} T_ab^mu T_{cd mu} = 0.
Exact rational arithmetic at random two-jets (y = 0), for eta = diag(-1,1,1,1) and the Euclidean delta.
"""
import sys
sys.dont_write_bytecode = True
import sympy as sp, itertools, random
from sympy.combinatorics.permutations import Permutation
from sympy.physics.quantum import TensorProduct as TP
random.seed(471)
Y = sp.symbols('y0:4')
R_ = sp.Rational
clean = lambda v: sp.expand(v)

def randpoly(deg):
    tot = 0
    mons = [1] + list(Y)
    for i in range(4):
        for j in range(i, 4):
            mons.append(Y[i] * Y[j])
    if deg >= 3:
        for i in range(4):
            for j in range(i, 4):
                for k in range(j, 4):
                    if random.random() < 0.35: mons.append(Y[i] * Y[j] * Y[k])
    for mo in mons:
        if random.random() < 0.6: tot += R_(random.randint(-3, 3), random.randint(1, 3)) * mo
    return tot

def eps(a, b, c, d):
    if len({a, b, c, d}) < 4: return 0
    return Permutation([a, b, c, d]).signature()

def run(etaM, label, npts=10):
    sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -sp.I], [sp.I, 0]]); sz = sp.Matrix([[1, 0], [0, -1]]); I2 = sp.eye(2)
    gE = [TP(sx, I2), TP(sy, I2), TP(sz, sx), TP(sz, sy)]
    Gam = [gE[i] * (sp.I if etaM[i, i] == -1 else 1) for i in range(4)]
    SD = {(a, b): (Gam[a] * Gam[b] - Gam[b] * Gam[a]) / 4 for a in range(4) for b in range(4)}
    G5 = Gam[0] * Gam[1] * Gam[2] * Gam[3]
    rows = []; rhs_ = []; p1ok = True; gam5res = []
    for pt in range(npts):
        # exact two-jet at y = 0: rho = 1 + r.y, E^{a mu} = rho^{-1} d_nu A^{a nu mu} with A antisymmetric, cubic
        r1 = [R_(random.randint(-2, 2), 5) for _ in range(4)]
        rhop = 1 + sum(r1[i] * Y[i] for i in range(4))
        invrho = 1 - sum(r1[i] * Y[i] for i in range(4)) + sum(r1[i] * Y[i] for i in range(4)) ** 2     # to order 2
        E = [[None] * 4 for _ in range(4)]
        for a in range(4):
            Mx = sp.zeros(4, 4)
            for n in range(4):
                for mu in range(n + 1, 4):
                    Mx[n, mu] = randpoly(3); Mx[mu, n] = -Mx[n, mu]
            for mu in range(4):
                E[a][mu] = sp.expand(invrho * sum(sp.diff(Mx[n, mu], Y[n]) for n in range(4)))
        at0 = {y: 0 for y in Y}
        E0 = sp.Matrix(4, 4, lambda a, mu: E[a][mu].subs(at0))
        E1 = [sp.Matrix(4, 4, lambda a, mu: sp.diff(E[a][mu], Y[k]).subs(at0)) for k in range(4)]
        E2 = [[sp.Matrix(4, 4, lambda a, mu: sp.diff(E[a][mu], Y[k], Y[l]).subs(at0)) for l in range(4)] for k in range(4)]
        g0inv = E0.T * etaM * E0
        if g0inv.det() == 0: continue
        if etaM[0, 0] == 1 and False: continue
        g0 = g0inv.inv()
        dginv = [E1[k].T * etaM * E0 + E0.T * etaM * E1[k] for k in range(4)]
        ddginv = [[E2[k][l].T * etaM * E0 + E1[k].T * etaM * E1[l] + E1[l].T * etaM * E1[k] + E0.T * etaM * E2[k][l] for l in range(4)] for k in range(4)]
        dg = [-g0 * dginv[k] * g0 for k in range(4)]
        ddg = [[g0 * (dginv[l] * g0 * dginv[k] + dginv[k] * g0 * dginv[l] - ddginv[k][l]) * g0 for l in range(4)] for k in range(4)]
        # Christoffel at 0 and its derivative
        Gm = [[[sum(g0inv[l, s] * (dg[k][s, n] + dg[n][s, k] - dg[s][k, n]) for s in range(4)) / 2 for n in range(4)] for k in range(4)] for l in range(4)]
        dGm = [[[[sum(dginv[d][l, s] * (dg[k][s, n] + dg[n][s, k] - dg[s][k, n]) + g0inv[l, s] * (ddg[d][k][s, n] + ddg[d][n][s, k] - ddg[d][s][k, n]) for s in range(4)) / 2
                  for n in range(4)] for k in range(4)] for l in range(4)] for d in range(4)]
        Ric = sp.zeros(4, 4)
        for k in range(4):
            for n in range(4):
                t = 0
                for l in range(4):
                    t += dGm[l][l][k][n] - dGm[n][l][k][l]
                    for s in range(4):
                        t += Gm[l][l][s] * Gm[s][k][n] - Gm[l][n][s] * Gm[s][k][l]
                Ric[k, n] = t
        Rs = sum(g0inv[k, n] * Ric[k, n] for k in range(4) for n in range(4))
        # phi = (1/2) ln rho + (1/4) ln|det g^{-1}|; rho as above has d ln rho = r1, dd ln rho = - r1 r1 at 0
        lnrho_d = [r1[k] for k in range(4)]
        lnrho_dd = [[-r1[k] * r1[l] for l in range(4)] for k in range(4)]
        dlnd = [(g0 * dginv[k]).trace() for k in range(4)]
        ddlnd = [[(g0 * ddginv[k][l]).trace() - (g0 * dginv[k] * g0 * dginv[l]).trace() for l in range(4)] for k in range(4)]
        dphi = [lnrho_d[k] / 2 + dlnd[k] / 4 for k in range(4)]
        ddphi = [[lnrho_dd[k][l] / 2 + ddlnd[k][l] / 4 for l in range(4)] for k in range(4)]
        boxphi = sum(g0inv[k, l] * (ddphi[k][l] - sum(Gm[s][k][l] * dphi[s] for s in range(4))) for k in range(4) for l in range(4))
        dphi2 = sum(g0inv[k, l] * dphi[k] * dphi[l] for k in range(4) for l in range(4))
        T = [[[sum(E0[a, n] * E1[n][b, mu] - E0[b, n] * E1[n][a, mu] for n in range(4)) for mu in range(4)] for b in range(4)] for a in range(4)]
        if pt < 3:
            for a in range(4):
                for b in range(a + 1, 4):
                    div = 0
                    for mu in range(4):
                        for n in range(4):
                            div += E1[mu][a, n] * E1[n][b, mu] + E0[a, n] * E2[mu][n][b, mu] - E1[mu][b, n] * E1[n][a, mu] - E0[b, n] * E2[mu][n][a, mu]
                        div += r1[mu] * T[a][b][mu]
                    p1ok &= sp.simplify(div) == 0
        Tlow = [[[etaM[a, a] * etaM[b, b] * T[a][b][mu] for mu in range(4)] for b in range(4)] for a in range(4)]
        Zs = []
        for mu in range(4):
            Z_ = sp.zeros(4, 4)
            for a in range(4):
                for b in range(4):
                    if a != b: Z_ += -sp.I * SD[(a, b)] * Tlow[a][b][mu]
            Zs.append(Z_)
        ZZ = sp.zeros(4, 4)
        for m_ in range(4):
            for n_ in range(4):
                ZZ += g0[m_, n_] * Zs[m_] * Zs[n_]
        idx = ZZ.trace() / 4
        # frame coefficient at 0: e_{c mu} = g_{mu nu} E_c^nu
        Ec0 = etaM * E0
        e_cmu = Ec0 * g0                  # e_{c mu}
        Tabc = [[[sum(T[a][b][mu] * e_cmu[c_, mu] for mu in range(4)) for c_ in range(4)] for b in range(4)] for a in range(4)]
        # T^{ab}{}_c with c lower; axial: A_d = eps_{abcd} T^{abc}, raise c with eta
        Aup = [sum(eps(a, b, c_, d) * Tabc[a][b][c_] * etaM[c_, c_] for a in range(4) for b in range(4) for c_ in range(4)) for d in range(4)]
        A2 = sum(etaM[d, d] * Aup[d] ** 2 for d in range(4))
        # Gamma5 part of ZZ
        scalar = ZZ.trace() / 4
        rem = (ZZ - scalar * sp.eye(4)).applyfunc(sp.nsimplify)
        g5coef = clean((rem * G5).trace() / (G5 * G5).trace())
        resid5 = (rem - g5coef * G5).applyfunc(sp.simplify)
        ps = sum(eps(a, b, c_, d) * sum(g0[m_, n_] * Tlow[a][b][m_] * Tlow[c_][d][n_] for m_ in range(4) for n_ in range(4)) for a, b, c_, d in itertools.permutations(range(4), 4))
        gam5res.append((all(x == 0 for x in resid5), clean(g5coef), clean(ps)))
        rows.append([clean(sp.expand(v)) for v in (Rs, boxphi, dphi2, A2)]); rhs_.append(clean(sp.expand(idx)))
    A_ = sp.Matrix(rows); b_ = sp.Matrix(rhs_)
    sol = A_[:4, :].LUsolve(b_[:4, :]) if A_.rank() >= 4 else None
    res = [clean(sp.expand((A_[i, :] * sol)[0] - b_[i])) for i in range(A_.rows)]
    print("  %s: %d points; fitted (R, Box phi, |d phi|^2, A^2) = %s ; residual on all points zero: %s" % (label, A_.rows, [clean(sp.expand(v)) for v in sol], all(r == 0 for r in res)))
    print("     (P1) rho-divergence of T vanishes (2 points, 3 pairs): %s" % p1ok)
    allz = all(g[0] for g in gam5res)
    ratio = [clean(sp.simplify(g[1] / g[2])) if g[2] != 0 else None for g in gam5res]
    print("     (P3) Z.Z is scalar + c G5 in all points: %s; c / eps(T.T) values: %s" % (allz, sorted(set(ratio), key=str)))

print("General rho-divergence-free frames, random exact two-jets")
run(sp.diag(-1, 1, 1, 1), 'eta = diag(-1,1,1,1)')
run(sp.eye(4), 'eta = delta')
