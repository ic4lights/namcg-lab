"""
Proposal 021, script 1: Lichnerowicz / Weitzenboeck structure of the Poisson-limit Dirac operator.

Setting (Euclidean eta = delta, Poisson-limit class of Appendix H, Problem F): omega = Theta^{-1} closed,
e^A_mu = omega_{mu A}, G = omega omega^T, rho = |Pf omega|, D_mu f = Theta^{mu nu} d_nu f,
O_f = -(gamma^mu D_mu)^2 on spinors, O_s = -D_mu D_mu (= D^dagger D on L^2(rho d^4x)).
Both are written as -(G^{ab} d_a d_b + A^b d_b) and the Laplace-type data are extracted with Gilkey's formulas
   omega_n = 1/2 (G_{nm} A^m + G^{se} Gamma^r_{se} G_{rn}),
   E_Gilkey = B - G^{nm}(d_n omega_m + omega_n omega_m - omega_s Gamma^s_{nm}),   O = -(nabla^2 + E_Gilkey);
the manuscript's E is E = -E_Gilkey (O = -nabla^2 + E), and the a_1 density is tr(R/6 - E).
Exact rational arithmetic on random closed omega (A_nu polynomial of degree 2,3), 2-jets at the origin.
Tests:
  (a) scalar: E_s = -1/2 box ln rho + 1/4 |d ln rho|^2 (reproduces the manuscript);
  (b) Dirac:  tr E_f / 4 = R_G/4 + a T^2 + b T T' + c V^2 + d box ln rho (fit; residual must vanish): Q_f = 1/4 per component;
  (c) Dirac:  tr(R_G/6 - E_f) = (4/6) R[g_rho]/rho + (1/2) X (the manuscript's table entry, re-derived independently).
Conventions: T^A_{mn} = d_m e^A_n - d_n e^A_m, T_{lmn} = e^A_l T^A_{mn}, V_m = G^{ln} T_{lmn} = d_m ln rho, X = T_{lmn} T^{lmn}.
"""
import itertools
import numpy as np
import sympy as sp

x = sp.symbols('x0:4')
rng = np.random.default_rng(20261016)
Rat = sp.Rational
ZERO = {xi: 0 for xi in x}


def trunc(expr, deg):
    expr = sp.expand(expr)
    if expr == 0:
        return sp.Integer(0)
    P = sp.Poly(expr, *x)
    return sum(c * sp.Mul(*[xi**e for xi, e in zip(x, m)]) for m, c in P.terms() if sum(m) <= deg)


def tmat(M, deg):
    return M.applyfunc(lambda e: trunc(e, deg))


def at0(e):
    return e.subs(ZERO)


def random_omega():
    A = []
    for nu in range(4):
        expr = 0
        for deg in (2, 3):
            for mono in itertools.combinations_with_replacement(range(4), deg):
                if rng.random() < 0.5:
                    expr += Rat(int(rng.integers(-3, 4)), 4) * sp.Mul(*[x[i] for i in mono])
        A.append(expr)
    base = rng.normal(size=(4, 4))
    base = base - base.T
    return sp.Matrix(4, 4, lambda m, n: Rat(int(round(base[m, n] * 4)), 4) + sp.diff(A[n], x[m]) - sp.diff(A[m], x[n]))


def gammas():
    s0 = sp.eye(2)
    s1 = sp.Matrix([[0, 1], [1, 0]])
    s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    s3 = sp.Matrix([[1, 0], [0, -1]])
    kp = sp.kronecker_product
    return [kp(s1, s0), kp(s2, s0), kp(s3, s1), kp(s3, s2)]


GAM = gammas()
for a in range(4):
    for b in range(4):
        assert GAM[a] * GAM[b] + GAM[b] * GAM[a] == 2 * (1 if a == b else 0) * sp.eye(4)


def run():
    om = random_omega()
    om0 = at0(om)
    assert om0.det() != 0
    Th0 = om0.inv()
    dl = om - om0
    Th = tmat(Th0 - Th0 * dl * Th0 + Th0 * dl * Th0 * dl * Th0, 2)     # Theta = omega^{-1} to degree 2
    Gdn = tmat(om * om.T, 2)
    Gup = tmat(Th.T * Th, 2)
    pf = lambda M: M[0, 1] * M[2, 3] - M[0, 2] * M[1, 3] + M[0, 3] * M[1, 2]
    rho = sp.expand(sp.sign(at0(pf(om))) * pf(om))
    rho0 = at0(rho)
    dlt = rho - rho0
    invrho = trunc((1 - dlt / rho0 + dlt**2 / rho0**2) / rho0, 2)
    lnr_d = [trunc(sp.diff(rho, x[i]) * invrho, 2) for i in range(4)]
    Gam_c = [-sum(sp.diff(Gup[s, r], x[s]) for s in range(4)) - sum(Gup[s, r] * 2 * lnr_d[s] for s in range(4)) for r in range(4)]

    def Gamma(l, m, n):
        return sum(Gup[l, s] * (sp.diff(Gdn[s, n], x[m]) + sp.diff(Gdn[s, m], x[n]) - sp.diff(Gdn[m, n], x[s])) for s in range(4)) / 2

    Gam0 = [[[at0(Gamma(l, m, n)) for n in range(4)] for m in range(4)] for l in range(4)]
    Gu0 = at0(Gup)

    def extract(Amat, nc):
        omg = []
        for nu in range(4):
            M = sp.zeros(nc, nc)
            for mu in range(4):
                M += Gdn[nu, mu] * Amat[mu]
            M = M + sp.eye(nc) * sum(Gdn[nu, r] * Gam_c[r] for r in range(4))
            omg.append(tmat(M / 2, 1))
        omg0 = [at0(w) for w in omg]
        Eg = sp.zeros(nc, nc)
        for n in range(4):
            for m in range(4):
                term = at0(omg[m].diff(x[n])) + omg0[n] * omg0[m]
                for s in range(4):
                    term = term - Gam0[s][n][m] * omg0[s]
                Eg += Gu0[n, m] * term
        return Eg.trace()          # E_Gilkey = B - Eg = -Eg (B = 0); manuscript E = -E_Gilkey = +Eg

    # scalar: O_s = -D_m D_m (D anti-self-adjoint on L^2(rho d^4x)), A^b = Theta^{ma} d_a Theta^{mb}
    As = []
    for b in range(4):
        e = sum(Th[m, a] * sp.diff(Th[m, b], x[a]) for a in range(4) for m in range(4))
        As.append(sp.Matrix([[e]]))
    As = [tmat(M, 1) for M in As]
    trEs = extract(As, 1)
    Af = []
    for b in range(4):
        M = sp.zeros(4, 4)
        for m in range(4):
            for n in range(4):
                c = trunc(sum(Th[m, a] * sp.diff(Th[n, b], x[a]) for a in range(4)), 1)
                M += GAM[m] * GAM[n] * c
        Af.append(M)
    trEf = extract(Af, 4)

    G0 = np.array(at0(Gdn).tolist(), dtype=float)
    Gi = np.linalg.inv(G0)
    dG = np.array([[[float(at0(sp.diff(Gdn[m, n], x[r]))) for n in range(4)] for m in range(4)] for r in range(4)])
    ddG = np.array([[[[float(at0(sp.diff(Gdn[m, n], x[r], x[s]))) for n in range(4)] for m in range(4)] for s in range(4)] for r in range(4)])
    t1 = np.einsum('msn->smn', dG)
    t2 = np.einsum('nsm->smn', dG)
    t3 = dG
    Gam = 0.5 * np.einsum('ls,smn->lmn', Gi, t1 + t2 - t3)
    dGi = -np.einsum('la,rab,bs->rls', Gi, dG, Gi)
    dt = np.einsum('rmsn->rsmn', ddG) + np.einsum('rnsm->rsmn', ddG) - np.einsum('rsmn->rsmn', ddG)
    dGam = 0.5 * (np.einsum('rls,smn->rlmn', dGi, t1 + t2 - t3) + np.einsum('ls,rsmn->rlmn', Gi, dt))
    Ric = (np.einsum('rrns->ns', dGam) - np.einsum('nrrs->ns', dGam)
           + np.einsum('rrl,lns->ns', Gam, Gam) - np.einsum('rnl,lrs->ns', Gam, Gam))
    R = float(np.einsum('ns,ns->', Gi, Ric))
    r0 = float(at0(rho))
    dr = np.array([float(at0(sp.diff(rho, x[i]))) for i in range(4)])
    ddr = np.array([[float(at0(sp.diff(rho, x[i], x[j]))) for j in range(4)] for i in range(4)])
    dlnr = dr / r0
    ddlnr = ddr / r0 - np.outer(dr, dr) / r0**2
    box = float(np.einsum('mn,mn->', Gi, ddlnr - np.einsum('lmn,l->mn', Gam, dlnr)))
    V2 = float(np.einsum('mn,m,n->', Gi, dlnr, dlnr))
    Es_formula = -0.5 * box + 0.25 * V2
    e0 = np.array(at0(om).tolist(), dtype=float)
    de = np.array([[[float(at0(sp.diff(om[m, A], x[r]))) for m in range(4)] for A in range(4)] for r in range(4)])
    Tab = np.einsum('mAn->Amn', de) - np.einsum('nAm->Amn', de)
    Tl = np.einsum('lA,Amn->lmn', e0, Tab)
    Tup = np.einsum('lmn,la,mb,nc->abc', Tl, Gi, Gi, Gi)
    T2 = float(np.einsum('lmn,lmn->', Tl, Tup))
    TT = float(np.einsum('lmn,mln->', Tl, Tup))
    V = np.einsum('ln,lmn->m', Gi, Tl)
    return dict(R=R, trEs=float(sp.re(trEs)), Es_formula=Es_formula, trEf=float(sp.re(trEf)), T2=T2, TT=TT,
                V2=float(np.einsum('mn,m,n->', Gi, V, V)), box=box, X=T2, rho=r0, Vdiff=float(np.abs(V - dlnr).max()))


if __name__ == '__main__':
    rows = []
    for k in range(7):
        r = run()
        rows.append(r)
        print(f"sample {k}: R={r['R']:.6f}  trE_s={r['trEs']:.8f}  E_s(formula)={r['Es_formula']:.8f}  "
              f"diff={abs(r['trEs'] - r['Es_formula']):.1e}  |V-dlnrho|={r['Vdiff']:.1e}")
    print('(a) scalar E_s reproduces -1/2 box ln rho + 1/4 |d ln rho|^2:', all(abs(r['trEs'] - r['Es_formula']) < 1e-9 for r in rows))
    M = np.array([[r['T2'], r['TT'], r['V2'], r['box']] for r in rows])
    y = np.array([r['trEf'] / 4 - r['R'] / 4 for r in rows])
    sol, res, rk, sv = np.linalg.lstsq(M, y, rcond=None)
    print("(b) fit  trE_f/4 - R/4 = a T^2 + b T T' + c V^2 + d box ln rho: (a,b,c,d) =", np.round(sol, 8), 'rank', rk,
          'max residual', np.abs(M @ sol - y).max())
    y_s = np.array([r['trEs'] - r['R'] / 4 for r in rows])
    sol_s = np.linalg.lstsq(M[:, :3], y_s, rcond=None)[0]
    print("    scalar analogue E_s - R/4 = a T^2 + b T T' + c V^2:", np.round(sol_s, 8), 'residual', np.abs(M[:, :3] @ sol_s - y_s).max())
    for r in rows[:4]:
        lnO_box = -0.5 * r['box']
        lnO_g2 = 0.25 * r['V2']
        Rg = r['rho'] * (r['R'] - 6 * lnO_box - 6 * lnO_g2)
        lhs = 4 * r['R'] / 6 - r['trEf']
        rhs = (4 / 6) * Rg / r['rho'] + 0.5 * r['X']
        print(f"(c) tr(R_G/6 - E_f) = {lhs:.8f}   (4/6) R[g_rho]/rho + X/2 = {rhs:.8f}   diff = {abs(lhs - rhs):.1e}")
