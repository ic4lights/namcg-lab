"""
s2_forms_exact.py  (proposal 045) -- driver; routines in forms_lib.py.

(0) EH2 (second variation of sqrt|g| R) validated against a direct curvature computation.
(1) Calibration in the merged four-coordinate class: on the two delta rho = 0 modes the index form X equals
    -4 x EH and the scalar a_1 form equals (1/6) x EH (merged: rho^2 X acts as -4 rho R[g_rho]).
(2) CP^{1,2} level-one sector (frozen base point y^i = 0, leading symbol, fibre trace = exact fibre average):
    gauge invariance; the averaged metric hbar depends on the symmetric part of D (six physical polarisations);
    torsion content; trace reading (fibre average of the pointwise densities: SC2, IX2) versus averaged-frame
    reading (densities of the fibre-averaged frame: SC1, IX1); comparison with EH of hbar on the six and on the
    five traceless polarisations; existence of a ratio W_R : W_X giving an Einstein or covariant form;
    pointwise formula X(t) = m^{-4} (v.v)(alpha M alpha) for alpha = sum_i n^i c_i, v = sum_j n^j s_j.
"""
import sympy as sp, random, itertools
from forms_lib import *
out = []
def P(*a):
    line = " ".join(str(x) for x in a); print(line); out.append(line)
random.seed(7)
def rrat(): return R(random.randint(-6, 6), random.randint(1, 4))

# ---------------- (0)
P("(0) EH2 validation: phase-averaged O(H^2) part of sqrt|g| R, direct curvature computation vs EH2:")
for trial in range(2):
    gb = sp.diag(-R(1, 4), R(1, 4), R(1, 4), R(1, 4)) if trial == 0 else sp.diag(R(1, 9), R(1, 9), R(1, 9), R(1, 9))
    H = sp.zeros(4, 4)
    for a in range(4):
        for b in range(a, 4):
            H[a, b] = H[b, a] = rrat()
    q = sp.Matrix([rrat() for _ in range(4)])
    d = direct_sqrtgR_avg(gb, H, q); f = EH2(gb, H, q)
    P("    %s background: direct = %s, EH2 = %s, equal: %s" % ('Lorentzian' if trial == 0 else 'Euclidean', d, f, sp.simplify(d - f) == 0))

# ---------------- (1)
P("\n(1) four-coordinate class calibration (constant Theta, a^mu = u^mu cos(p.x), delta rho = 0 modes, gauge u ~ Theta p removed):")
for sig, etam in (("Euclidean", sp.eye(4)), ("Lorentzian", sp.diag(-1, 1, 1, 1))):
    for trial in range(2):
        while True:
            Th = sp.zeros(4, 4)
            for a in range(4):
                for b in range(a + 1, 4):
                    Th[a, b] = rrat(); Th[b, a] = -Th[a, b]
            if Th.det() != 0: break
        p = sp.Matrix([rrat() for _ in range(4)])
        us = sp.symbols('u0:4'); u = sp.Matrix(us)
        Tp = Th * p
        dTh = Tp * u.T - u * Tp.T                         # dTheta^{mu nu} amplitude
        gamma_bar = Th.T * etam * Th
        dgamma = dTh.T * etam * Th + Th.T * etam * dTh
        dT_amp = [[[Tp[mu] * dTh[a, b] for mu in range(4)] for b in range(4)] for a in range(4)]
        sc, eh = scalar_form(gamma_bar, dgamma, p)
        ix = index_form(gamma_bar, dT_amp, etam)
        ns = sp.Matrix([[p[i] for i in range(4)]]).nullspace()
        basis = []
        for v in ns:
            M = sp.Matrix.hstack(*(basis + [Tp, v]))
            if M.rank() == len(basis) + 2: basis.append(v)
            if len(basis) == 2: break
        Bm = sp.Matrix.hstack(*basis)
        rs = lambda Q: (Bm.T * quad_matrix(sp.expand(Q), list(us)) * Bm).applyfunc(sp.expand)
        IX, EH, SC = rs(ix), rs(eh), rs(sc)
        gauge_ok = sp.expand(ix.subs(dict(zip(us, list(Tp))))) == 0 and sp.expand(eh.subs(dict(zip(us, list(Tp))))) == 0
        P("    %s, draw %d: gauge invariant %s | EH^-1 X = %s | EH^-1 a1_scalar = %s"
          % (sig, trial, gauge_ok, (EH.inv() * IX).applyfunc(sp.simplify).tolist(), (EH.inv() * SC).applyfunc(sp.simplify).tolist()))

# ---------------- (2)
P("\n(2) CP^{1,2} level-one sector, frozen base point (y^0, y^i = 0, y^4), leading symbol, exact fibre moments")
cases = [((5, 3), [R(3, 7), R(1, 2), R(-2, 3), R(1, 5)], 1),
         ((5, 3), [R(-1, 3), R(2, 5), R(1, 4), R(-3, 2)], 1),
         ((5, 3), [R(2, 1), R(1, 3), R(-1, 2), R(1, 4)], 1),          # time-like q
         ((13, 5), [R(2, 3), R(-1, 2), R(1, 3), R(1, 7)], 1),
         ((5, 4), [R(1, 9), R(3, 4), R(-1, 2), R(2, 3)], 1),
         ((-5, 3), [R(3, 7), R(1, 2), R(-2, 3), R(1, 5)], 1),
         ((-5, 3), [R(3, 7), R(1, 2), R(-2, 3), R(1, 5)], -1)]
store = []
for (y0, y4), q, chi in cases:
    F = cp12_forms(y0, y4, q, chi=chi)
    Dv, gv = F['Dv'], F['gv']; qv, qu = F['q'], F['qu']
    q2 = (qv.T * ETA * qv)[0]
    G = gram(F)
    P("\n  base (y0,y4) = (%s,%s), chirality %s, ell = %s, q = %s, q^2 = %s, eigenvalues of Gram s_i.s_j: %s"
      % (y0, y4, chi, F['ell'], list(qv), q2, sorted([sp.N(e, 6) for e in G.eigenvals(multiple=True)])))
    zeroD = {d: 0 for d in Dv}
    gauge = all(sp.expand(F[k].subs(zeroD)) == 0 for k in ('SC2', 'EHt2', 'IX2', 'SC1', 'EH1', 'IX1'))
    cross = all(sp.expand(sp.diff(F[k], g, d)) == 0 for k in ('SC2', 'IX2', 'SC1', 'IX1') for g in gv for d in Dv)
    P("   gauge amplitudes g_i q: all forms vanish on them: %s; no cross terms with D: %s" % (gauge, cross))
    hbar = F['dgbar'].subs({g: 0 for g in gv})
    Aex = dict(zip(Dv, [0, 1, 0, -1, 0, 0, 0, 0, 0]))
    hb_ant0 = hbar.subs(Aex).applyfunc(sp.expand).is_zero_matrix
    hb_rank = lin_coeffs([hbar[a, b] for a in range(4) for b in range(a, 4)], list(Dv)).rank()
    trans = (hbar * qv).applyfunc(sp.expand).is_zero_matrix     # hbar^{mu nu} q_nu
    P("   averaged metric: independent of antisymmetric D: %s; rank of D -> hbar: %d; transverse (hbar.q = 0): %s" % (hb_ant0, hb_rank, trans))
    # torsion content
    Vb, Axb = torsion_parts(F['dTbar']); Vp, Axp = torsion_parts(F['dT'])
    sym = dict(zip(Dv, sp.symbols('d11 d12 d13 d12 d22 d23 d13 d23 d33'))); sub0 = {g: 0 for g in gv}
    ax_sym0 = all(sp.expand(v.subs(sub0).subs(sym)) == 0 for v in Axb.values())
    ax_inert = any(sp.expand(v.subs(sub0).subs(Aex)) != 0 for v in Axb.values())
    trDG = sum(sp.Matrix(3, 3, Dv)[i, j] * G[j, i] for i in range(3) for j in range(3))
    Vrat = set(sp.simplify(Vb[a].subs(sub0) / (qu[a] * trDG)) for a in range(4) if qu[a] != 0)
    Dtl = dict(zip(Dv, [1, 0, 0, 0, -1, 0, 0, 0, 0])); Did = dict(zip(Dv, [1, 0, 0, 0, 1, 0, 0, 0, 1]))
    ax_tl = any(sp.expand(v.subs(sub0).subs(Dtl)) != 0 for v in Axp.values())
    ax_tl_avg0 = all(fibre_avg(v.subs(sub0).subs(Dtl)) == 0 for v in Axp.values())
    ax_id0 = all(sp.expand(v.subs(sub0).subs(Did)) == 0 for v in Axp.values())
    P("   torsion of the averaged frame: axial = 0 on symmetric D: %s; axial != 0 on an inert D: %s; vector V^a = %s q^a tr(DG)" % (ax_sym0, ax_inert, Vrat))
    P("   fibre-resolved torsion: axial != 0 for D = diag(1,-1,0): %s (its fibre average = 0: %s); axial = 0 for D = 1: %s" % (ax_tl, ax_tl_avg0, ax_id0))
    # pointwise closed form of X(t)
    n = sp.Matrix(NSYM)
    s = F['s']
    alpha = sum((n[i] * (sum((sp.Matrix(3, 3, Dv)[i, j] * s[j] for j in range(3)), sp.zeros(4, 1)) + gv[i] * qu) for i in range(3)), sp.zeros(4, 1))
    vv = sum((n[j] * s[j] for j in range(3)), sp.zeros(4, 1))
    Mq = q2 * ETA - qv * qv.T   # lower-index Maxwell kernel acting on upper alpha: alpha^T eta(...)eta alpha
    aMa = sp.expand((alpha.T * ETA * (q2 * ETA.inv() - qu * qu.T) * ETA * alpha)[0])
    Xpt = sp.expand(F['m'] ** -4 * (vv.T * ETA * vv)[0] * aMa)
    ixpt = index_form(F['m'] ** 2 * ETA.inv(), F['dT'], ETA)
    P("   pointwise index density X(t) = m^-4 (v.v)(alpha M alpha), alpha = n^i c_i, v = n^j s_j: %s" % (sp.expand(ixpt - Xpt) == 0))
    # forms on D
    f = D_forms(F)
    ss, aa = slice(0, 6), slice(6, 9)
    for k in ('IX2', 'SC2', 'IX1', 'SC1'):
        P("   %s: sym-antisym cross block zero: %s; antisym block zero: %s" % (k, f[k][ss, aa].is_zero_matrix, f[k][aa, aa].is_zero_matrix))
    EH = f['EH1'][ss, ss]
    E1, E2, trv = cov_span_forms(G)
    ok, co, _ = span_coeffs(EH, [E1, E2])
    P("   EH(hbar) = %s tr(GDGD) + %s (tr GD)^2  [i.e. proportional to h.h - (tr h)^2]: %s" % (co[0], co[1], ok and sp.simplify(co[0] + co[1]) == 0))
    ok1, c1, _ = span_coeffs(f['IX1'][ss, ss] + 2 * EH, [E2])
    okS, cS, _ = span_coeffs(f['SC1'][ss, ss] - R(1, 6) * EH, [E2])
    P("   averaged-frame reading: X = -2 EH + (%s)(tr GD)^2 exactly: %s ; a1_scalar = (1/6) EH + (%s)(tr GD)^2 exactly: %s" % (c1[0], ok1, cS[0], okS))
    for k in ('IX2', 'SC2'):
        okk, ck, rk = span_coeffs(f[k][ss, ss], [E1, E2])
        P("   trace reading %s in the covariant span {tr(GDGD), (tr GD)^2}: %s (relative residual of the best fit %s)" % (k, okk, rk))
    Ntl = sp.Matrix.hstack(*trv.nullspace())
    E5 = Ntl.T * EH * Ntl
    for k in ('IX1', 'SC1', 'IX2', 'SC2'):
        ev = gen_eigs(Ntl.T * f[k][ss, ss] * Ntl, E5)
        P("   %s / EH on the five traceless polarisations: %s" % (k, ["%.6g%+.2gi" % (z.real, z.imag) if abs(z.imag) > 1e-12 else "%.6g" % z.real for z in ev]))
    # trace polarisation (complement of the five in the EH-orthogonal sense): generalized eigenvalue on the six
    for k in ('IX1', 'SC1'):
        ev6 = gen_eigs(f[k][ss, ss], EH)
        P("   %s / EH on the six: %s" % (k, ["%.6g" % z.real for z in ev6]))
    wR, wX, a1, a2 = sp.symbols('wR wX a1 a2')
    sol_cov = sp.solve(list(wR * f['SC2'][ss, ss] + wX * f['IX2'][ss, ss] - a1 * E1 - a2 * E2), [wR, wX, a1, a2], dict=True)
    sol_eh = sp.solve(list(wR * f['SC2'][ss, ss] + wX * f['IX2'][ss, ss] - a1 * EH), [wR, wX, a1], dict=True)
    sol_eh5 = sp.solve(list(Ntl.T * (wR * f['SC2'][ss, ss] + wX * f['IX2'][ss, ss] - a1 * EH) * Ntl), [wR, wX, a1], dict=True)
    P("   trace reading: solutions (wR, wX) of wR*SC2 + wX*IX2 in the covariant span: %s; proportional to EH on the six: %s; on the five traceless: %s"
      % (sol_cov, sol_eh, sol_eh5))
    store.append(((y0, y4, chi), q, f))

open(__file__.replace('.py', '.out.txt'), 'w').write("\n".join(out) + "\n")
