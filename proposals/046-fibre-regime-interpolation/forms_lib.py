"""
forms_lib.py  (proposal 045) -- shared exact-rational routines for s2/s3.

Per unit coordinate volume d^4y, frozen constant background, a plane wave of phase u = q.y; the metric
(cometric) perturbation carries sin u and the torsion cos u; every quadratic form is phase averaged.

  EH2(gb, H, q):  second variation of sqrt|g| R[g] for g = gb + H sin u  (validated in s2 part (0) against a
                  direct curvature computation)
  scalar_form:    a_1 density of the operator -d_mu gamma^{mu nu} d_nu (divergence-free frame):
                  (1/6) sqrt|G| R[G] - sqrt|G| G^{mu nu} d phi d phi,  G = gamma^{-1},  phi = -(1/4) ln|det G|
  index_form:     X = sqrt|G| G_{mu nu} eta_ac eta_bd T^{ab mu} T^{cd nu}  (merged normalisation of rho^2 X)
"""
import sympy as sp, itertools
R = sp.Rational

def EH2(gb, H, q):
    gi = gb.inv(); sq = sp.sqrt(sp.Abs(gb.det()))
    Hu = gi * H * gi
    q2 = (q.T * gi * q)[0]
    HH = sum(H[a, b] * Hu[a, b] for a in range(4) for b in range(4))
    trH = sum(gi[a, b] * H[a, b] for a in range(4) for b in range(4))
    qH = Hu * q
    qHqH = (qH.T * gb * qH)[0]
    qHq = (q.T * Hu * q)[0]
    return sq * R(1, 4) * (-R(1, 2) * q2 * HH + qHqH - qHq * trH + R(1, 2) * q2 * trH ** 2)

def direct_sqrtgR_avg(gb, H, q):
    u, e = sp.symbols('u e')
    g = gb + e * H * sp.sin(u)
    gi0 = gb.inv(); d1 = H * sp.sin(u)
    gi = gi0 - e * gi0 * d1 * gi0 + e ** 2 * gi0 * d1 * gi0 * d1 * gi0
    dG = [q[mu] * sp.diff(g, u) for mu in range(4)]
    Gam = [[[sum(R(1, 2) * gi[l, s] * (dG[m][s, nn] + dG[nn][s, m] - dG[s][m, nn]) for s in range(4))
             for nn in range(4)] for m in range(4)] for l in range(4)]
    Ric = 0
    for m in range(4):
        for nn in range(4):
            term = 0
            for l in range(4):
                term += q[l] * sp.diff(Gam[l][m][nn], u) - q[nn] * sp.diff(Gam[l][m][l], u)
                for s in range(4):
                    term += Gam[l][l][s] * Gam[s][m][nn] - Gam[l][nn][s] * Gam[s][m][l]
            Ric += gi[m, nn] * term
    sq = sp.sqrt(sp.Abs(gb.det())) * sp.series(sp.sqrt(sp.expand(g.det() / gb.det())), e, 0, 3).removeO()
    expr = sp.expand(sp.series(sp.expand(sq * Ric), e, 0, 3).removeO()).coeff(e, 2)
    return sp.simplify(sp.integrate(expr, (u, 0, 2 * sp.pi)) / (2 * sp.pi))

def quad_matrix(Q, vars_):
    return sp.Matrix(len(vars_), len(vars_), lambda i, j: R(1, 2) * sp.diff(Q, vars_[i], vars_[j]))

def lin_coeffs(expr_list, vars_):
    return sp.Matrix([[sp.diff(ex, v) for v in vars_] for ex in expr_list])

def scalar_form(gamma_bar, dgamma, q):
    Gb = gamma_bar.inv(); dG = -Gb * dgamma * Gb
    eh = EH2(Gb, dG, q)
    dphi = -R(1, 4) * sum(gamma_bar[a, b] * dG[a, b] for a in range(4) for b in range(4))
    sq = sp.sqrt(sp.Abs(Gb.det()))
    dil = sq * (q.T * gamma_bar * q)[0] * dphi ** 2 * R(1, 2)
    return R(1, 6) * eh - dil, eh

def index_form(gamma_bar, dT_amp, etam):
    Gb = gamma_bar.inv(); sq = sp.sqrt(sp.Abs(Gb.det()))
    tot = 0
    for a, b, c, d in itertools.product(range(4), repeat=4):
        if etam[a, c] == 0 or etam[b, d] == 0: continue
        for mu in range(4):
            for nu in range(4):
                if Gb[mu, nu] == 0: continue
                tot += Gb[mu, nu] * etam[a, c] * etam[b, d] * dT_amp[a][b][mu] * dT_amp[c][d][nu]
    return sq * R(1, 2) * tot

ETA = sp.diag(-1, 1, 1, 1)

def Smodel(y0, y4, chi=1):
    """S_i = ell [e_i ^ vhat + chi e_j ^ e_k]_{0..3}, vhat = (y4,0,0,0,y0)/ell (013 model), normalised so that
       M^{mu rho} = sum_i n^i S_i^{mu rho} with n a unit vector of S^2 (fibre radius ell; s1)."""
    ell = sp.sqrt(sp.Integer(y0) ** 2 - sp.Integer(y4) ** 2); assert ell.is_rational
    v = sp.Matrix([y4, 0, 0, 0, y0]) / ell
    e = [sp.Matrix([0] * (i + 1) + [1] + [0] * (3 - i)) for i in (0, 1, 2)]
    wedge = lambda a, b: a * b.T - b * a.T
    S = []
    for i in range(3):
        j, k = (i + 1) % 3, (i + 2) % 3
        S.append(ell * (wedge(e[i], v) + chi * wedge(e[j], e[k]))[:4, :4])
    return S, ell

NSYM = sp.symbols('n1:4')
def fibre_avg(expr):
    poly = sp.Poly(sp.expand(expr), *NSYM)
    tot = 0
    df = lambda k: sp.factorial2(k - 1) if k > 0 else 1
    for mon, co in poly.terms():
        a, b, c = mon
        if a % 2 or b % 2 or c % 2: continue
        tot += co * R(df(a) * df(b) * df(c), sp.factorial2(a + b + c + 1))
    return sp.expand(tot)

def cp12_forms(y0, y4, q, chi=1, m=None):
    """Forms on the 12 amplitudes c_i = D_ij s_j + g_i q (q^a = eta^{a mu} q_mu) of the CP^{1,2} level-one sector."""
    etam = ETA
    S, ell = Smodel(y0, y4, chi)
    m = sp.Integer(y4) if m is None else m
    q = sp.Matrix(q); qu = etam * q
    s = [Si * q for Si in S]
    Dv = sp.symbols('D0:9'); gv = sp.symbols('g0:3')
    Dm = sp.Matrix(3, 3, Dv)
    c = [sum((Dm[i, j] * s[j] for j in range(3)), sp.zeros(4, 1)) + gv[i] * qu for i in range(3)]
    n = sp.Matrix(NSYM); NN = n * n.T
    dE = sp.zeros(4, 4)
    for i in range(3):
        for j in range(3):
            dE += NN[i, j] * c[i] * s[j].T
    gamma_bar = m ** 2 * etam.inv(); Eb = m * etam.inv()
    dgamma = Eb.T * etam * dE + dE.T * etam * Eb
    K = [qu * c[i].T - c[i] * qu.T for i in range(3)]
    dT = [[[-m * sum(NN[i, j] * s[j][mu] * K[i][a, b] for i in range(3) for j in range(3)) for mu in range(4)]
           for b in range(4)] for a in range(4)]
    sc_pt, eh_pt = scalar_form(gamma_bar, dgamma, q)
    ix_pt = index_form(gamma_bar, dT, etam)
    out = dict(S=S, s=s, q=q, qu=qu, m=m, ell=ell, Dv=Dv, gv=gv, dE=dE, dgamma=dgamma, dT=dT,
               SC2=fibre_avg(sc_pt), EHt2=fibre_avg(eh_pt), IX2=fibre_avg(ix_pt))
    dgbar = dgamma.applyfunc(fibre_avg)
    dTbar = [[[fibre_avg(dT[a][b][mu]) for mu in range(4)] for b in range(4)] for a in range(4)]
    SC1, EH1 = scalar_form(gamma_bar, dgbar, q)
    out.update(dgbar=dgbar, dTbar=dTbar, SC1=SC1, EH1=EH1, IX1=index_form(gamma_bar, dTbar, etam))
    return out

def torsion_parts(dT):
    """vector part V^a = T^{ab}{}_b and totally antisymmetric part T^{[ab mu]}, frame index identified with the
       coordinate index through the background frame m eta^{a mu}."""
    etam = ETA
    V = [sp.expand(sum(dT[a][b][mu] * etam[b, mu] for b in range(4) for mu in range(4))) for a in range(4)]
    Ax = {}
    for a, b, mu in itertools.combinations(range(4), 3):
        Ax[(a, b, mu)] = sp.expand(dT[a][b][mu] + dT[b][mu][a] + dT[mu][a][b] - dT[b][a][mu] - dT[a][mu][b] - dT[mu][b][a])
    return V, Ax

SYM_IDX = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
ANT_IDX = [(0, 1), (0, 2), (1, 2)]
def sym_ant_basis():
    Es, Ea = [], []
    for (i, j) in SYM_IDX:
        M = sp.zeros(3, 3); M[i, j] = 1; M[j, i] = 1; Es.append(M)
    for (i, j) in ANT_IDX:
        M = sp.zeros(3, 3); M[i, j] = 1; M[j, i] = -1; Ea.append(M)
    return Es, Ea

def D_forms(F, keys=('SC2', 'EHt2', 'IX2', 'SC1', 'EH1', 'IX1')):
    """9x9 matrices of the forms in the basis (6 symmetric, 3 antisymmetric D), gauge amplitudes set to zero."""
    Es, Ea = sym_ant_basis()
    B = sp.Matrix.hstack(*[sp.Matrix(list(M)) for M in Es + Ea])
    sub0 = {g: 0 for g in F['gv']}
    return {k: (B.T * quad_matrix(sp.expand(F[k].subs(sub0)), list(F['Dv'])) * B).applyfunc(sp.expand) for k in keys}

def gram(F):
    s = F['s']
    return sp.Matrix(3, 3, lambda i, j: (s[i].T * ETA * s[j])[0])

def cov_span_forms(G):
    """forms tr(G D G D) and (tr G D)^2 on symmetric D, in the symmetric basis."""
    Es, _ = sym_ant_basis()
    x = sp.symbols('x0:6'); Ds = sp.zeros(3, 3)
    for k, M in enumerate(Es): Ds += x[k] * M
    E1 = quad_matrix(sp.expand((G * Ds * G * Ds).trace()), list(x))
    E2 = quad_matrix(sp.expand((G * Ds).trace() ** 2), list(x))
    tr = sp.Matrix([[sp.diff((G * Ds).trace(), xi) for xi in x]])
    return E1, E2, tr

def span_coeffs(Q, basis):
    """exact rational least squares; returns (in_span, coefficients, relative residual)."""
    A = sp.Matrix.hstack(*[sp.Matrix(list(b)) for b in basis]); bvec = sp.Matrix(list(Q))
    sol = ((A.T * A).inv() * A.T * bvec).applyfunc(sp.simplify)
    resv = (A * sol - bvec).applyfunc(sp.simplify)
    if resv.is_zero_matrix:
        return True, list(sol), 0
    return False, [sp.N(x, 8) for x in sol], sp.N(resv.norm() / bvec.norm(), 6)

def gen_eigs(Q, E):
    """numerical generalised eigenvalues of the pencil (Q, E) (double precision, scipy QZ)."""
    import numpy as np, scipy.linalg as sl
    Qn = np.array(Q.evalf(30).tolist(), dtype=float); En = np.array(E.evalf(30).tolist(), dtype=float)
    ev = sl.eigvals(Qn, En)
    return sorted([complex(z) for z in ev], key=lambda z: (round(z.real, 7), round(z.imag, 7)))
