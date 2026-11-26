"""
s3_closed_forms.py  (proposal 047)  --  prints to stdout only; writes nothing.

Closed forms for the two-derivative forms of the 045/046 paragraphs on the five traceless level-one polarisations.
Setting: base point y^i = 0, y = (y0,0,0,0), m = y4, l^2 = y0^2 - m^2, wave vector q_mu, level-one amplitudes
c_i = D_ij s_j (D symmetric), s_i^mu = S_i^{mu nu} q_nu, h^{mu nu} = (2m/3) D_ij s_i^mu s_j^nu, D traceless on the Gram
matrix G_ij = s_i.s_j.  Exact facts proved by hand in proposal-r1.md and tested here in exact arithmetic:
   G = a 1 - (a-b) qhat qhat^T, a = l^2 q^2 + (q.y)^2, b = -m^2 q^2,   x := a/b,
   y_perp^2 = y^2 - (q.y)^2/q^2 = m^2 (x-1).
Helicity of a polarisation is counted about y_perp in the three-space orthogonal to q; phi_h = (hy)^2/(h.h y_perp^2) takes
the values 0, 1/2, 2/3 on helicities 2, 1, 0.  All eigenvalues relative to EH(hbar):
   IX1 = -2,  SC1 = 1/6,
   IX2 : lambda_h = -(6/5) [ 2 + (2 + 1/x)(1 + (x-1) phi_h) ],
   SC2 : (1/20) [ 4 + 2 r_h + (2 + 1/x)(1 + (x-1) phi_h) ],  r_h = 1, (x + 1/x)/2, 1 on helicities 2, 1, 0,
   Q2_D/m^4 : (3/2) coth^2 tau + (x-1) phi_h ,
   P2 /m^4  : 9 coth^2 tau + (x-1)(8 - 6 phi_h) ,
   lambda_L := (IX2-IX1)/(Q2_D/m^4) mod EH = -(6/5)(2 + 1/x).
(A) test of these at the seven 045 cases, the ten 046 cases and at further random rational wave vectors;
(B) symbolic derivation of Q2_D and P2 from the exact second variations, with k-moments;
(C) covariant forms: EH = -f1/(8 m^6), IX2-IX1 and Q2, P2 in span{f1, f2, f4} with f1 = q^2 h.h, f2 = q^2 (hy).(hy), f4 = (q.y)^2 h.h.
"""
import sys, os
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '046-fibre-regime-interpolation'))
from forms_lib import *
import numpy as np, scipy.linalg as sl, itertools, random
random.seed(473)

# ---------- second-variation matrix routines of 046 s3 (numerical) ----------
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1.]).astype(complex); I2 = np.eye(2)
gE = [np.kron(sx, I2), np.kron(sy, I2), np.kron(sz, sx), np.kron(sz, sy)]
etaN = np.diag([-1., 1, 1, 1])
Gam = [1j * gE[0], gE[1], gE[2], gE[3]]
SigD = np.zeros((4, 4, 4, 4), complex); SigV = np.zeros((4, 4, 4, 4), complex)
for a in range(4):
    for b in range(4):
        SigD[a, b] = 0.25 * (Gam[a] @ Gam[b] - Gam[b] @ Gam[a])
        for c in range(4):
            for d in range(4):
                SigV[a, b, c, d] = etaN[a, c] * (1 if b == d else 0) - etaN[b, c] * (1 if a == d else 0)
def Zmats(T, Sig):
    Tl = np.einsum('ac,bd,cdm->abm', etaN, etaN, T)
    return [-1.0 * 1j * np.einsum('abij,ab->ij', Sig, Tl[:, :, mu]) for mu in range(4)]
def Q2(Zs, G):
    tot = 0
    for m_, n, r, s_ in itertools.product(range(4), repeat=4):
        g1 = G[m_, n] * G[r, s_]; g2 = G[m_, r] * G[n, s_]; g3 = G[m_, s_] * G[n, r]
        if g1 == 0 and g2 == 0 and g3 == 0: continue
        tot += (g1 + g2 + g3) * np.trace(Zs[m_] @ Zs[n] @ Zs[r] @ Zs[s_])
    return tot / 96.0
def tcoef2(F, D):
    ts = np.array([-2., -1., 0., 1., 2.]); vals = np.array([F(t * D) for t in ts])
    return np.linalg.solve(np.vander(ts, 5, increasing=True), vals)[2]
def quad_form(F, n):
    E = np.eye(n); Qm = np.zeros((n, n), complex)
    for i in range(n): Qm[i, i] = tcoef2(F, E[i])
    for i in range(n):
        for j in range(i + 1, n):
            Qm[i, j] = Qm[j, i] = (tcoef2(F, E[i] + E[j]) - Qm[i, i] - Qm[j, j]) / 2
    return Qm

def analyse(y0, y4, qq, chi=1, torsion=True):
    F = cp12_forms(y0, y4, qq, chi=chi); f = D_forms(F)
    A = lambda k: np.array(f[k].evalf(), dtype=float)[:6, :6]
    EH, IX1, IX2, SC1, SC2 = A('EH1'), A('IX1'), A('IX2'), A('SC1'), A('SC2')
    m = float(F['m']); q = np.array([float(v) for v in qq]); yv = np.array([float(y0), 0, 0, 0]); ell2 = float(y0) ** 2 - m ** 2
    q2 = q @ etaN @ q; qy = q @ yv
    a_ = ell2 * q2 + qy ** 2; b_ = -m ** 2 * q2; x = a_ / b_
    coth2 = (float(y0) / m) ** 2
    Gm = gram(F); E1, E2, trv = cov_span_forms(Gm)
    Ntl = np.array(sp.Matrix.hstack(*trv.nullspace()).evalf(), dtype=float)
    E5 = Ntl.T @ EH @ Ntl
    ev = lambda Qm: np.sort(sl.eigvals(Ntl.T @ Qm @ Ntl, E5).real)
    phis = np.array([0, .5, .5, 2 / 3, 0])          # helicity 2,1,1,0,2
    r_h = np.array([1, (x + 1 / x) / 2, (x + 1 / x) / 2, 1, 1])
    pred = {'IX1': -2 * np.ones(5), 'SC1': np.ones(5) / 6,
            'IX2': -(6 / 5) * (2 + (2 + 1 / x) * (1 + (x - 1) * phis)),
            'SC2': (4 + 2 * r_h + (2 + 1 / x) * (1 + (x - 1) * phis)) / 20}
    actual = {'IX1': ev(IX1), 'SC1': ev(SC1), 'IX2': ev(IX2), 'SC2': ev(SC2)}
    if torsion:
        ybv = yv
        Tbar = np.zeros((4, 4, 4))
        for a_ in range(4):
            for b_ in range(4):
                for mu in range(4):
                    Tbar[a_, b_, mu] = etaN[a_, mu] * ybv[b_] - etaN[b_, mu] * ybv[a_]
        G = etaN / m ** 2
        Es, Ea = sym_ant_basis()
        sub0 = {g: 0 for g in F['gv']}; Dv = list(F['Dv']); dTb = F['dTbar']
        lin = []
        for M_ in Es:
            subD = dict(zip(Dv, list(M_)))
            lin.append(np.array([[[float(sp.expand(dTb[a_][b_][mu].subs(sub0).subs(subD))) for mu in range(4)] for b_ in range(4)] for a_ in range(4)]))
        dT_of = lambda D: sum(D[p] * lin[p] for p in range(6))
        Q2D = quad_form(lambda D: Q2(Zmats(Tbar + dT_of(D), SigD), G), 6).real
        Q2V = quad_form(lambda D: Q2(Zmats(Tbar + dT_of(D), SigV), G), 6).real
        P2 = Q2V - 2 * Q2D
        pred['Q2D'] = (1.5 * coth2 + (x - 1) * phis); actual['Q2D'] = ev(Q2D) / m ** 4
        pred['P2'] = (9 * coth2 + (x - 1) * (8 - 6 * phis)); actual['P2'] = ev(P2) / m ** 4
    # covariant forms
    s = [np.array(sp.Matrix(si).evalf(), dtype=float).flatten() for si in F['s']]
    Es, Ea = sym_ant_basis()
    def hup(M):
        Mn = np.array(M.evalf(), dtype=float); H = np.zeros((4, 4))
        for i in range(3):
            for j in range(3): H += Mn[i, j] * np.outer(s[i], s[j])
        return (2 * m / 3) * H
    hs = [hup(M) for M in Es]; yl = etaN @ yv
    form = lambda fn: np.array([[fn(hs[p], hs[r]) for r in range(6)] for p in range(6)])
    low = lambda h: etaN @ h @ etaN
    f1 = form(lambda u, v: q2 * np.sum(low(u) * v)); f2 = form(lambda u, v: q2 * ((u @ yl) @ etaN @ (v @ yl)))
    f4 = form(lambda u, v: qy ** 2 * np.sum(low(u) * v))
    r5 = lambda Qm: (Ntl.T @ Qm @ Ntl).flatten()
    resid = {}
    # dTbar of the averaged frame against -(1/2)(q^a h^{b mu} - q^b h^{a mu}), six basis polarisations
    subg = {g: 0 for g in F['gv']}; Dvs = list(F['Dv'])
    qup = etaN @ q; dtmax = 0
    for idx_, M_ in enumerate(Es):
        subD = dict(zip(Dvs, list(M_)))
        dTn = np.array([[[float(sp.expand(F['dTbar'][a_][b_][mu].subs(subg).subs(subD))) for mu in range(4)] for b_ in range(4)] for a_ in range(4)])
        pr = -0.5 * (np.einsum('a,bm->abm', qup, hs[idx_]) - np.einsum('b,am->abm', qup, hs[idx_]))
        dtmax = max(dtmax, np.abs(dTn - pr).max() / max(np.abs(dTn).max(), 1e-30))
    resid['dT = -(q^h)/2'] = dtmax
    resid['EH + f1/(8m^6)'] = np.linalg.norm(r5(EH + f1 / (8 * m ** 6))) / np.linalg.norm(r5(EH))
    if torsion:
        # Q2D and P2 in covariant form: Q2D/m^4 ~ EH-units; express in f1, f2, f4 with EH = -f1/(8 m^6)
        # Q2_D = m^4 EH * [(3/2) coth^2] + m^4 EH*(x-1) phi -> (x-1) phi f1 = f2/m^2
        predQ = -(1.5 * coth2 * f1 + f2 / m ** 2) * m ** 4 / (8 * m ** 6)
        resid['Q2D closed'] = np.linalg.norm(r5(Q2D - predQ)) / np.linalg.norm(r5(Q2D))
        # (x-1) f1 = (y_perp^2/m^2) f1 = (y^2 q^2 - (q.y)^2) h.h / m^2
        predP = -(9 * coth2 * f1 + 8 * (-(float(y0) ** 2) * f1 - f4) / m ** 2 - 6 * f2 / m ** 2) * m ** 4 / (8 * m ** 6)
        resid['P2 closed'] = np.linalg.norm(r5(P2 - predP)) / np.linalg.norm(r5(P2))
    maxerr = {k: float(np.max(np.abs(np.sort(pred[k]) - actual[k]))) for k in pred}
    lamL = -(6 / 5) * (2 + 1 / x)
    return dict(x=x, q2=q2, qy=qy, coth2=coth2, maxerr=maxerr, resid=resid, lamL=lamL, eigs=actual, phis=phis)

cases045 = [(5, 3, [R(3, 7), R(1, 2), R(-2, 3), R(1, 5)], 1), (5, 3, [R(-1, 3), R(2, 5), R(1, 4), R(-3, 2)], 1), (5, 3, [R(2, 1), R(1, 3), R(-1, 2), R(1, 4)], 1),
            (13, 5, [R(2, 3), R(-1, 2), R(1, 3), R(1, 7)], 1), (5, 4, [R(1, 9), R(3, 4), R(-1, 2), R(2, 3)], 1), (-5, 3, [R(3, 7), R(1, 2), R(-2, 3), R(1, 5)], 1),
            (-5, 3, [R(3, 7), R(1, 2), R(-2, 3), R(1, 5)], -1), (25, 7, [R(3, 7), R(1, 2), R(-2, 3), R(1, 5)], 1), (5, 4, [R(3, 7), R(1, 2), R(-2, 3), R(1, 5)], 1),
            (17, 15, [R(3, 7), R(1, 2), R(-2, 3), R(1, 5)], 1)]
print("(A) closed forms against the exact 045/046 form routines; max |closed - computed| over the five eigenvalues")
worst = {}
for (y0, y4, qq, chi) in cases045:
    r = analyse(y0, y4, qq, chi)
    print("  (y0,y4)=(%d,%d) chi=%+d x=%+.5f lambda_L=%+.5f | %s | %s" % (y0, y4, chi, r['x'], r['lamL'], {k: float('%.1e' % v) for k, v in r['maxerr'].items()}, {k: float('%.1e' % v) for k, v in r['resid'].items()}))
    for k, v in r['maxerr'].items(): worst[k] = max(worst.get(k, 0), v)
for i in range(8):
    qq = [R(random.randint(-9, 9), random.randint(1, 7)) for _ in range(4)]
    base = random.choice([(5, 3), (5, 4), (13, 5), (13, 12), (25, 7), (17, 8)])
    r = analyse(base[0], base[1], qq, 1)
    print("  random (y0,y4)=%s x=%+.5f lambda_L=%+.5f | %s | %s" % (base, r['x'], r['lamL'], {k: float('%.1e' % v) for k, v in r['maxerr'].items()}, {k: float('%.1e' % v) for k, v in r['resid'].items()}))
    for k, v in r['maxerr'].items(): worst[k] = max(worst.get(k, 0), v)
print("  worst error over all cases:", {k: float('%.1e' % v) for k, v in worst.items()})

print("\n(B) symbolic derivation, q = (q0,0,0,q3), y = (y0,0,0,0), Gaussian k-moments <k k> = eta/(2 s m^2)")
q0, q3, Y0, M_, s_ = sp.symbols('q0 q3 y0 m s', positive=True)
k0, k1, k2, k3 = sp.symbols('k0 k1 k2 k3')
etaS = sp.diag(-1, 1, 1, 1)
kup = sp.Matrix([k0, k1, k2, k3])          # k^mu, moments <k^mu k^nu> = eta^{mu nu}/(2 s m^2)
ql = sp.Matrix([q0, 0, 0, q3])             # q_mu
qu = etaS * ql
yu = sp.Matrix([Y0, 0, 0, 0])
dot = lambda u, v: (u.T * etaS * v)[0]
q2s = dot(qu, qu)
nq = sp.sqrt(sp.Abs(q2s))
e1 = sp.Matrix([0, 1, 0, 0]); e2 = sp.Matrix([0, 0, 1, 0])
sg = sp.Symbol('sg')  # sign of q^2: +1 spacelike, -1 timelike
e3 = sp.Matrix([q3, 0, 0, -q0]) / sp.Symbol('nq', positive=True)   # upper components, orthogonal to qu = (-q0,0,0,q3), e3.e3 = -sg
pols = {'h2': e1 * e1.T - e2 * e2.T, 'h1': e1 * e3.T + e3 * e1.T}
nqS = sp.Symbol('nq', positive=True)
# helicity zero: traceless on the three-space orthogonal to q with respect to eta: e3.e3 = -sg
pols['h0'] = e3 * e3.T + sp.Rational(1, 2) * sg * (e1 * e1.T + e2 * e2.T)
def mom(expr):
    """Isserlis average over k^mu with <k^mu k^nu> = eta^{mu nu} /(2 s m^2), via monomial moments"""
    P = sp.Poly(sp.expand(expr), k0, k1, k2, k3)
    tot = 0; var = 1 / (2 * s_ * M_ ** 2)
    df = lambda n: sp.factorial2(n - 1) if n > 0 else 1
    for (a, b, c, d), co in P.terms():
        if a % 2 or b % 2 or c % 2 or d % 2: continue
        tot += co * df(a) * df(b) * df(c) * df(d) * (-var) ** (a // 2) * var ** ((b + c + d) // 2)
    return tot
def sub_all(e):
    e = e.subs(nqS ** 2, sg * (q3 ** 2 - q0 ** 2))
    return e
for name, hh in pols.items():
    u = hh * etaS * kup            # u^a = h^{a mu} k_mu , k_mu = eta k^mu
    uu = dot(u, u); ku = dot(kup, u); yuu = dot(yu, u)
    kk = dot(kup, kup); ky = dot(kup, yu); kq = dot(kup, qu); yq = dot(yu, qu); yy_ = dot(yu, yu)
    Lam2 = ky ** 2 - kk * yy_
    A2 = q2s * uu / 4
    A1 = -(kq * yuu - ku * yq)
    GM = sp.Matrix([[kk, ky, kq, ku], [ky, yy_, yq, yuu], [kq, yq, q2s, 0], [ku, yuu, 0, uu]])
    P12 = -GM.det(method='berkowitz')             # (eps(k,y,q,u))^2 = -det Gram (Lorentzian)
    # Dirac t^2 coefficient at order s^4 and vector minus twice Dirac at order s^4 (formulas in proposal-r1.md)
    D4 = (s_ ** 4 / 6) * (-2 * Lam2 * A2 + A1 ** 2 - P12)
    VmD4 = s_ ** 4 * (-2 * Lam2 * A2 + A1 ** 2 + P12)
    D2 = 2 * s_ ** 2 * A2
    q1 = sp.simplify(mom(D2) / s_)
    Q2s = sp.simplify(mom(D4) / s_ ** 2)
    Ps = sp.simplify(mom(VmD4) / s_ ** 2)
    x_ = (Y0 ** 2 * q0 ** 2 + (Y0 ** 2 - M_ ** 2) * (q3 ** 2 - q0 ** 2)) / (-M_ ** 2 * (q3 ** 2 - q0 ** 2))
    phi = {'h2': 0, 'h1': sp.Rational(1, 2), 'h0': sp.Rational(2, 3)}[name]
    # Q1 relative to EH: Q1 = -2 m^4 EH -> eigenvalue unit u_ = Q1/(-2)
    unit = q1 / (-2)
    rQ = sp.simplify((Q2s / unit - (sp.Rational(3, 2) * Y0 ** 2 / M_ ** 2 + (x_ - 1) * phi)).subs(nqS, sp.sqrt(sg * (q3 ** 2 - q0 ** 2))))
    rP = sp.simplify((Ps / unit - (9 * Y0 ** 2 / M_ ** 2 + (x_ - 1) * (8 - 6 * phi))).subs(nqS, sp.sqrt(sg * (q3 ** 2 - q0 ** 2))))
    # note: unit is Q1/(-2) evaluated with s_ independent; sign of EH eigen relative Q1 handled by the numerical part (A)
    rP1 = sp.simplify((sp.simplify(mom(s_ ** 2 * P12) / unit) - (x_ - 1) * (4 - 6 * phi)).subs(nqS, sp.sqrt(sg * (q3 ** 2 - q0 ** 2))))
    print("  %s: Q2_D/unit - closed = %s ; P2/unit - closed = %s ; <P1^2>/unit - (x-1)(4-6 phi) = %s" % (name, rQ.subs(sg, 1), rP.subs(sg, 1), rP1.subs(sg, 1)))
