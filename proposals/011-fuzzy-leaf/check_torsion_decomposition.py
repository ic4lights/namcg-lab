"""
Does rho^2 X (X = eta^{rl} eta_{ma} eta_{nb} d_r Theta^{mn} d_l Theta^{ab}) lie, modulo total derivatives, in the span of
  h = rho R[g_rho],  r = rho |grad ln rho|^2_{g_rho},  and Weitzenboeck (coframe) torsion invariants of the coframe
  e^A_mu = eta^{AB} omega_{mu B}  (G_{mu nu} = eta_{AB} e^A_mu e^B_nu, omega = Theta^{-1})?
Torsion T^A_{mu nu} = d_mu e^A_nu - d_nu e^A_mu; with T_{lam|mu nu} := eta_{AB} e^A_lam T^B_{mu nu} (all coordinate
indices), G-contracted quadratic invariants
  I_A = T_{l|mn} T_{l'|m'n'} G^{ll'} G^{mm'} G^{nn'}
  I_B = T_{l|mn} T_{l'|m'n'} G^{lm'} G^{ml'} G^{nn'}
  I_V = V_m V_n G^{mn},  V_m = G^{ln} T_{l|mn}                       (vector torsion)
  I_S = S_{lmn} S_{l'm'n'} G G G,  S = totally antisymmetric part of T_{l|mn}   (axial torsion)
Same exact perturbative framework as proposal 005 (base005.py is a verbatim copy of 005's check_X_covariant_rewrite.py):
Poisson class omega = psi^* omega_bar, plane waves with eps_j^2 = 0; the coefficient of eps1 eps2 eps3 (sum p = 0) is a
constant and any total derivative has zero coefficient, so an identity mod total derivatives requires equality of these
cubic coefficients for ALL samples.  Mask 3 gives the quadratic order.
Also checks the exact algebraic identity  X = I_1 := G_{mu nu} T^{ab mu} T_{ab}^{nu},  T^{ab mu} = Theta^{mu r} d_r Theta^{ab}.
"""
import numpy as np, sys
import base005 as B
from base005 import F, cf, ZERO, mm, mT, minv, finv, flog, n

rng = np.random.default_rng(777)


def build(sig, ab, ps, us, masks):
    eta = np.diag([sig, 1., 1., 1.]); etai = np.linalg.inv(eta)
    k = len(ps)
    P = {0: np.zeros(n)}
    for m in range(1, 2**k):
        P[m] = sum(ps[j] for j in range(k) if m >> j & 1)
    D = lambda f, a: F({m: 1j*P[m][a]*v for m, v in f.d.items()})
    w = [F({1 << j: us[j][a] for j in range(k)}) for a in range(n)]
    dw = [[D(w[a], m) for a in range(n)] for m in range(n)]
    Jm = [[cf(1.0 if m == a else 0.0) + dw[m][a] for a in range(n)] for m in range(n)]
    omb = np.zeros((n, n)); omb[0, 1] = ab[0]; omb[1, 0] = -ab[0]; omb[2, 3] = ab[1]; omb[3, 2] = -ab[1]
    ombF = [[cf(omb[i, j]) for j in range(n)] for i in range(n)]
    om = mm(mm(Jm, ombF), mT(Jm))
    Th = minv(om)
    Pf = Th[0][1]*Th[2][3] - Th[0][2]*Th[1][3] + Th[0][3]*Th[1][2]
    rho = finv(Pf)
    etaF = [[cf(eta[i, j]) for j in range(n)] for i in range(n)]
    K = mm(mm(mT(Th), etaF), Th)           # K^{mu nu} = G^{mu nu}
    Gup = K
    G = minv(Gup)                           # G_{mu nu}
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
    dom = [[[D(om[m][nn], r) for nn in range(n)] for m in range(n)] for r in range(n)]   # d_r omega_{m nn}
    # T^B_{mu nu} = eta^{BA}(d_mu omega_{nu A} - d_nu omega_{mu A})
    TB = [[[sum((etai[b, a]*(dom[mu][nu][a] - dom[nu][mu][a]) for a in range(n) if etai[b, a] != 0), ZERO)
            for nu in range(n)] for mu in range(n)] for b in range(n)]
    # T_{lam|mu nu} = omega_{lam B} T^B_{mu nu}
    Tl = [[[sum((om[lam][b]*TB[b][mu][nu] for b in range(n)), ZERO) for nu in range(n)] for mu in range(n)]
          for lam in range(n)]
    # exact identity X = G_{mu nu} T^{ab mu} T_{ab}^nu ; T^{ab mu} = Theta^{mu r} d_r Theta^{ab}
    Tab = [[[sum((Th[mu][r]*dTh[r][a][b] for r in range(n)), ZERO) for mu in range(n)] for b in range(n)]
           for a in range(n)]
    I1 = ZERO
    for a in range(n):
        for b in range(n):
            for ap in range(n):
                for bp in range(n):
                    c = eta[a, ap]*eta[b, bp]
                    if c == 0:
                        continue
                    for mu in range(n):
                        for nu in range(n):
                            I1 = I1 + G[mu][nu]*Tab[a][b][mu]*Tab[ap][bp][nu]*c

    def raise3(T):
        r1 = [[[sum((Gup[l][lp]*T[lp][m][nn] for lp in range(n)), ZERO) for nn in range(n)] for m in range(n)]
              for l in range(n)]
        r2 = [[[sum((Gup[m][mp]*r1[l][mp][nn] for mp in range(n)), ZERO) for nn in range(n)] for m in range(n)]
              for l in range(n)]
        r3 = [[[sum((Gup[nn][np_]*r2[l][m][np_] for np_ in range(n)), ZERO) for nn in range(n)] for m in range(n)]
              for l in range(n)]
        return r3
    Tu = raise3(Tl)
    IA = sum((Tl[l][m][nn]*Tu[l][m][nn] for l in range(n) for m in range(n) for nn in range(n)), ZERO)
    IB = sum((Tl[l][m][nn]*Tu[m][l][nn] for l in range(n) for m in range(n) for nn in range(n)), ZERO)
    V = [sum((Gup[l][nn]*Tl[l][m][nn] for l in range(n) for nn in range(n)), ZERO) for m in range(n)]
    IV = sum((Gup[m][nn]*V[m]*V[nn] for m in range(n) for nn in range(n)), ZERO)

    def S(l, m, nn):
        return (Tl[l][m][nn] + Tl[m][nn][l] + Tl[nn][l][m])*(1.0/3.0)
    Sl = [[[S(l, m, nn) for nn in range(n)] for m in range(n)] for l in range(n)]
    Su = raise3(Sl)
    IS = sum((Sl[l][m][nn]*Su[l][m][nn] for l in range(n) for m in range(n) for nn in range(n)), ZERO)
    # Ricci scalar of G itself (independent of g_rho): sqrt|G| = rho^2
    dG_ = [[[D(G[b][c], a) for c in range(n)] for b in range(n)] for a in range(n)]
    GamG = [[[sum((Gup[l][d]*(dG_[c][d][b] + dG_[b][d][c] - dG_[d][b][c]) for d in range(n)), ZERO)*0.5
              for c in range(n)] for b in range(n)] for l in range(n)]
    dGamG = [[[[D(GamG[l][b][c], a) for c in range(n)] for b in range(n)] for l in range(n)] for a in range(n)]
    def RiemG(al, be, c, d):
        r = dGamG[c][al][be][d] - dGamG[d][al][be][c]
        for e in range(n):
            r = r + GamG[al][c][e]*GamG[e][be][d] - GamG[al][d][e]*GamG[e][be][c]
        return r
    RicG = [[sum((RiemG(al, be, al, d) for al in range(n)), ZERO) for d in range(n)] for be in range(n)]
    RG = sum((Gup[p][q]*RicG[p][q] for p in range(n) for q in range(n)), ZERO)
    dr = [D(rho, a) for a in range(n)]
    VmdL = [V[m] - dl[m] for m in range(n)]
    VpdL = [V[m] + dl[m] for m in range(n)]
    VmdL2 = sum((Gup[m][nn]*VmdL[m]*VmdL[nn] for m in range(n) for nn in range(n)), ZERO)
    VpdL2 = sum((Gup[m][nn]*VpdL[m]*VpdL[nn] for m in range(n) for nn in range(n)), ZERO)
    VdL = sum((Gup[m][nn]*V[m]*dl[nn] for m in range(n) for nn in range(n)), ZERO)
    Ltd = sum((D(sum((gup[a][b]*dr[b] for b in range(n)), ZERO), a) for a in range(n)), ZERO)
    rho2 = rho*rho
    rho2R = rho2*RG
    tele = rho2R + rho2*(IA*0.25 + IB*0.5 - IV)
    out = {'RG2': rho2R, 'tele': tele, 'Vm2': VmdL2, 'Vp2': VpdL2, 'h': Lh, 'r': Lr, 'x': rho2*X, 'A': rho2*IA, 'B': rho2*IB, 'V': rho2*IV, 'S': rho2*IS, 'VdL': rho2*VdL,
           'I1mX': rho2*(I1 - X), 'td': Ltd}
    return {nm: {mk: L.d.get(mk, 0) for mk in masks} for nm, L in out.items()}


def fit(cols, y):
    A = np.array(cols).T
    A_ri = np.vstack([A.real, A.imag]); y_ri = np.concatenate([y.real, y.imag])
    sol = np.linalg.lstsq(A_ri, y_ri, rcond=None)[0]
    res = np.linalg.norm(y_ri - A_ri@sol)/np.linalg.norm(y_ri)
    return sol, res


if __name__ == '__main__':
    ns = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    quad, cub = [], []
    maxI1 = 0.0
    for s in range(ns):
        sig = rng.choice([1.0, -1.0]); ab = rng.uniform(0.5, 2.5, 2)
        p1 = rng.integers(-3, 4, 4).astype(float); p2 = rng.integers(-3, 4, 4).astype(float); p3 = -p1 - p2
        us = [rng.normal(size=4) for _ in range(3)]
        o = build(sig, ab, [p1, p2, p3], us, [7]); cub.append(o)
        oq = build(sig, ab, [p1, -p1], us[:2], [3]); quad.append(oq)
        maxI1 = max(maxI1, abs(o['I1mX'][7]), abs(oq['I1mX'][3]))
    print('exact identity X = G_{mu nu} T^{ab mu} T_{ab}^nu : max |coefficient of rho^2 (I1 - X)| =', maxI1)
    for name, rows, mk in (('QUADRATIC', quad, 3), ('CUBIC', cub, 7)):
        print(name)
        get = lambda k: np.array([r[k][mk] for r in rows])
        y = get('x')
        for label, keys in (('x ~ h,r', ['h', 'r']),
                            ('x ~ h,r,S', ['h', 'r', 'S']),
                            ('x ~ h,r,V', ['h', 'r', 'V']),
                            ('x ~ h,r,S,V', ['h', 'r', 'S', 'V']),
                            ('x ~ h,r,S,V,VdL', ['h', 'r', 'S', 'V', 'VdL']),
                            ('x ~ h,r,A,B,V', ['h', 'r', 'A', 'B', 'V']),
                            ('x ~ A (trivial)', ['A'])):
            sol, res = fit([get(k) for k in keys], y)
            print('  %-18s coeffs %s  rel.resid %.3e' % (label, np.round(sol.real, 6), res))
    allk = ['h', 'r', 'A', 'B', 'V', 'S', 'VdL']
    M = np.array([[r[k][7] for r in cub] for k in allk]).T
    M = np.vstack([M.real, M.imag])
    sv = np.linalg.svd(M, compute_uv=False)
    print('singular values (normalized) of cubic coefficient matrix [h r A B V S VdL]:', np.round(sv/sv[0], 8))
