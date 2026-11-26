"""
s3_background_torsion.py  (proposal 046)

The background torsion of CP^{1,2}, Tbar^{ab mu} = eta^{a mu} y^b - eta^{b mu} y^a (exact, 045 s1), enters the flux
operator Z_ab = {F_ab, .} of every loop species on M at the frozen leading symbol: on a plane wave exp(i k.y) of a
fibre-constant (J = 0) loop mode the flux operator is i k_mu T_ab^mu with T = Tbar + dT_0 (dT_0 the fibre average of
the level-one torsion of 045).  The species operators are H_i = -Box + kappa Sigma_i^{ab} Z_ab, kappa = -1, with
Sigma_V the vector generators and Sigma_D = (1/4)[Gamma^a, Gamma^b] (tr_V Sigma Sigma = 2 tr_D Sigma Sigma).
At frozen coefficients Z(k) commutes with the kinetic symbol, so for J = 0 loop modes
   tr e^{-s H_i} - d_i tr e^{-s H_0}  =  N(s) < tr_i e^{-s Z_i(k)} - d_i >_k ,   <k_mu k_nu> = G_{mu nu}/(2s),
exactly (no Duhamel ordering), with N(s) the scalar Gaussian factor.  Expanding in s:
   < tr e^{-sZ} - d > = s Q1(T) + s^2 Q2(T) + ...,
   Q1 = (1/4) G_{mu nu} tr(Z^mu Z^nu),   Q2 = (1/96) [tr Z^mu Z_mu Z^rho Z_rho + tr Z^mu Z^rho Z_mu Z_rho + tr Z^mu Z^rho Z_rho Z_mu].
The part quadratic in dT_0 with no Tbar is the 045 averaged-frame index form (check: Q1_D proportional to IX1, Q1_V = 2 Q1_D).
Computed here, at the seven 045 cases and at further base points:
  (i)  Q2_D|_{Tbar^2 dT^2}: the first background-torsion correction of the mixed term (order (4,2) in the fluxes of M, K),
       relative weight s;
  (ii) P2 = (Q2_V - 2 Q2_D)|_{Tbar^2 dT^2}: the first term s0^K (v^M - 2 sigma^M) at fourth order in the flux of M
       (pure M, base torsion), which has no Tbar-free part at this order (Q1_V - 2 Q1_D = 0);
  generalised eigenvalues on the five traceless polarisations relative to EH(hbar), and their scaling with the base
  point (coth^2 tau = (y^0/y^4)^2 at y^i = 0).  Formal evaluation with the Lorentzian eta (Gamma^0 = i gamma_E^0), as in 045.
"""
import numpy as np, sympy as sp, itertools
from forms_lib import *

out = []
def P(*a):
    line = " ".join(str(x) for x in a); print(line); out.append(line)

# ---------------- representations ----------------
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1.]).astype(complex); I2 = np.eye(2)
gE = [np.kron(sx, I2), np.kron(sy, I2), np.kron(sz, sx), np.kron(sz, sy)]           # Euclidean Hermitian, {g,g} = 2 delta
etaN = np.diag([-1., 1, 1, 1])
Gam = [1j * gE[0], gE[1], gE[2], gE[3]]                                               # {Gam^a, Gam^b} = 2 eta^{ab}
assert all(np.allclose(Gam[a] @ Gam[b] + Gam[b] @ Gam[a], 2 * etaN[a, b] * np.eye(4)) for a in range(4) for b in range(4))
SigD = np.zeros((4, 4, 4, 4), complex); SigV = np.zeros((4, 4, 4, 4), complex)
for a in range(4):
    for b in range(4):
        SigD[a, b] = 0.25 * (Gam[a] @ Gam[b] - Gam[b] @ Gam[a])
        for c in range(4):
            for d in range(4):
                SigV[a, b, c, d] = etaN[a, c] * (1 if b == d else 0) - etaN[b, c] * (1 if a == d else 0)
okc = all(np.isclose(np.trace(SigV[a, b] @ SigV[c, d]), 2 * np.trace(SigD[a, b] @ SigD[c, d]))
          for a, b, c, d in itertools.product(range(4), repeat=4))
# same commutation relations
def comm_ok(S):
    for a, b, c, d in itertools.product(range(4), repeat=4):
        lhs = S[a, b] @ S[c, d] - S[c, d] @ S[a, b]
        rhs = etaN[b, c] * S[a, d] - etaN[a, c] * S[b, d] - etaN[b, d] * S[a, c] + etaN[a, d] * S[b, c]
        if not np.allclose(lhs, rhs) and not np.allclose(lhs, -rhs): return False
    return True
P("(R) Lorentzian Clifford relations ok; tr_V Sigma Sigma = 2 tr_D Sigma Sigma for all index pairs: %s; both sets close so(3,1) (common sign): %s"
  % (okc, comm_ok(SigD) and comm_ok(SigV)))
kappa = -1.0

def Zmats(T, Sig):
    """Z^mu = kappa * i * sum_{ab} Sig^{ab} T_ab^mu, T given with upper frame indices T[a][b][mu] (numpy array)"""
    Tl = np.einsum('ac,bd,cdm->abm', etaN, etaN, T)
    return [kappa * 1j * np.einsum('abij,ab->ij', Sig, Tl[:, :, mu]) for mu in range(4)]

def Q1(Zs, G):
    return 0.25 * sum(G[m, n] * np.trace(Zs[m] @ Zs[n]) for m in range(4) for n in range(4))
def Q2(Zs, G):
    Gi = G   # contractions with G_{mu nu} (lower), Z^mu carries the upper loop-momentum index contracted with k_mu
    tot = 0
    for m, n, r, s_ in itertools.product(range(4), repeat=4):
        g1 = Gi[m, n] * Gi[r, s_]; g2 = Gi[m, r] * Gi[n, s_]; g3 = Gi[m, s_] * Gi[n, r]
        if g1 == 0 and g2 == 0 and g3 == 0: continue
        tr = np.trace(Zs[m] @ Zs[n] @ Zs[r] @ Zs[s_])
        tot += (g1 + g2 + g3) * tr
    return tot / 96.0

def tcoef2(F, D):
    """coefficient of t^2 in F(t D) (F a polynomial of degree <= 4 in t)"""
    ts = np.array([-2., -1., 0., 1., 2.]); vals = np.array([F(t * D) for t in ts])
    V = np.vander(ts, 5, increasing=True)
    return np.linalg.solve(V, vals)[2]

def quad_form(F, n):
    E = np.eye(n); Qm = np.zeros((n, n), complex)
    for i in range(n): Qm[i, i] = tcoef2(F, E[i])
    for i in range(n):
        for j in range(i + 1, n):
            Qm[i, j] = Qm[j, i] = (tcoef2(F, E[i] + E[j]) - Qm[i, i] - Qm[j, j]) / 2
    return Qm

cases = [((5, 3), [R(3, 7), R(1, 2), R(-2, 3), R(1, 5)], 1),
         ((5, 3), [R(-1, 3), R(2, 5), R(1, 4), R(-3, 2)], 1),
         ((5, 3), [R(2, 1), R(1, 3), R(-1, 2), R(1, 4)], 1),
         ((13, 5), [R(2, 3), R(-1, 2), R(1, 3), R(1, 7)], 1),
         ((5, 4), [R(1, 9), R(3, 4), R(-1, 2), R(2, 3)], 1),
         ((-5, 3), [R(3, 7), R(1, 2), R(-2, 3), R(1, 5)], 1),
         ((-5, 3), [R(3, 7), R(1, 2), R(-2, 3), R(1, 5)], -1),
         ((25, 7), [R(3, 7), R(1, 2), R(-2, 3), R(1, 5)], 1),
         ((5, 4), [R(3, 7), R(1, 2), R(-2, 3), R(1, 5)], 1),
         ((17, 15), [R(3, 7), R(1, 2), R(-2, 3), R(1, 5)], 1)]
Es, Ea = sym_ant_basis()
Bsym = sp.Matrix.hstack(*[sp.Matrix(list(M)) for M in Es])
P("\n(Q) forms on the six polarisations (inert amplitudes zero), J = 0 loop modes, base point y^i = 0")
rows = []
for (y0, y4), qq, chi in cases:
    F = cp12_forms(y0, y4, qq, chi=chi)
    sub0 = {g: 0 for g in F['gv']}
    m = float(F['m']); G = etaN / m ** 2                       # G_{mu nu} = gbar^{-1}, gbar = m^2 eta^{-1}
    ybv = np.array([float(y0), 0., 0., 0.])
    Tbar = np.zeros((4, 4, 4))
    for a_ in range(4):
        for b_ in range(4):
            for mu in range(4):
                Tbar[a_, b_, mu] = etaN[a_, mu] * ybv[b_] - etaN[b_, mu] * ybv[a_]
    # fibre-averaged level-one torsion as a linear function of the six symmetric D (basis Es)
    dTb = F['dTbar']
    Dv = list(F['Dv'])
    lin = []
    for M_ in Es:
        subD = dict(zip(Dv, list(M_)))
        lin.append(np.array([[[float(sp.expand(dTb[a_][b_][mu].subs(sub0).subs(subD))) for mu in range(4)] for b_ in range(4)] for a_ in range(4)]))
    def dT_of(D): return sum(D[p] * lin[p] for p in range(6))
    f = D_forms(F)
    EH = np.array(f['EH1'][:6, :6].evalf(), dtype=float); IX1 = np.array(f['IX1'][:6, :6].evalf(), dtype=float)
    Gm = gram(F); E1, E2, trv = cov_span_forms(Gm)
    Ntl = np.array(sp.Matrix.hstack(*trv.nullspace()).evalf(), dtype=float)
    E5 = Ntl.T @ EH @ Ntl
    def ev5(Qm):
        import scipy.linalg as sl
        z = sl.eigvals(Ntl.T @ Qm @ Ntl, E5)
        return np.sort(z.real), np.abs(z.imag).max()
    res = {}
    for name, Sig in (('D', SigD), ('V', SigV)):
        Q1f = lambda D, S=Sig: Q1(Zmats(dT_of(D), S), G)                       # no Tbar
        Q2t = lambda D, S=Sig: Q2(Zmats(Tbar + dT_of(D), S), G)                 # t^2 part = Tbar^2 dT^2 (+ dT^2 Tbar-free part is t^4)
        res['Q1' + name] = quad_form(Q1f, 6)
        res['Q2' + name] = quad_form(Q2t, 6)
    # odd-in-Tbar check: Q1 with Tbar has a t^1 part only (Tbar dT), not t^2 beyond the Tbar-free one
    ratio_Q1D_IX1 = np.vdot(IX1.flatten(), res['Q1D'].real.flatten()) / np.vdot(IX1.flatten(), IX1.flatten())
    resid = np.linalg.norm(res['Q1D'].real - ratio_Q1D_IX1 * IX1) / np.linalg.norm(res['Q1D'])
    vd = np.linalg.norm(res['Q1V'] - 2 * res['Q1D']) / np.linalg.norm(res['Q1D'])
    imag = max(np.abs(res[k].imag).max() / np.abs(res[k]).max() for k in res)
    Q1D = res['Q1D'].real; Q2D = res['Q2D'].real; P2 = (res['Q2V'] - 2 * res['Q2D']).real
    coth2 = (y0 / y4) ** 2
    e_q1, _ = ev5(Q1D); e_q2, im2 = ev5(Q2D); e_p2, imp = ev5(P2)
    P("  case (y0,y4)=(%s,%s) chi=%d q=%s: Q1_D = %.6g x IX1 (rel. residual %.1e); |Q1_V - 2 Q1_D|/|Q1_D| = %.1e; max imaginary part %.1e"
      % (y0, y4, chi, [str(x) for x in qq], ratio_Q1D_IX1, resid, vd, imag))
    P("     on the five traceless, relative to EH: Q1_D %s | Q2_D (Tbar^2 dT^2, mixed term) %s | P2 = Q2_V - 2Q2_D (first term) %s | coth^2 tau = %.4f"
      % (np.round(e_q1, 5).tolist(), np.round(e_q2, 5).tolist(), np.round(e_p2, 5).tolist(), coth2))
    P("     normalised by the Q1_D eigenvalue and coth^2 tau: Q2_D/(|Q1_D| coth^2) %s ; P2/(|Q1_D| coth^2) %s"
      % (np.round(e_q2 / abs(e_q1[0]) / coth2, 5).tolist(), np.round(e_p2 / abs(e_q1[0]) / coth2, 5).tolist()))
    rows.append(((y0, y4), chi, coth2, e_q1[0], e_q2, e_p2))
open(__file__.replace('.py', '.out.txt'), 'w').write("\n".join(out) + "\n")
