"""
s1_pointwise_forms.py (proposal 048). Prints to stdout only; writes nothing.

Exact tests of the fibre-point (pointwise) forms and of the dictionary with arXiv:2601.08031.

Setting as in 045-047: base point y^i=0, m=y4, l^2=y0^2-m^2, wave vector q_mu, frame perturbation at a fibre point
delta E^{a mu} = alpha^a v^mu, alpha = n^i c_i, v = n^j s_j, c_i = D_ij s_j + g_i q^a, real wave phase averaged.

Claims tested:
 (P1) at a fibre point, for g=0 and any 3x3 D (symmetric or not):
        index density  X_n  = m^-4 q^2 (v.v)(alpha.alpha)
        scalar density SC_n = -(q^2/(24 m^4)) [ (alpha.alpha)(v.v) + 2 (alpha.v)^2 ]
      and both are unchanged by g.
 (P2) fibre averages (IX2, SC2 of 045): with P = D G D^T, A = D G
        IX2 = (q^2/(15 m^4)) [ trG trP + 2 tr(G P) ]
        SC2 = -(q^2/(24 m^4)) (1/15) [ trG trP + 2 tr(GP) + 2 ( (trA)^2 + tr(A A^T) + tr(A A) ) ]
 (P3) dictionary: for any q (exact)
        trG 1 + 2 G = (4a+b) 1 - 2 (a-b) qhat qhat^T ,  a-b = y0^2 k^2,
        4a+b = 5 m^2 (q0^2 - k^2/5) + 4 l^2 k^2 ,   2a+3b = 5 m^2 (q0^2 - 3k^2/5) + 2 l^2 k^2 ,
      so IX2 = (q^2/(15 m^4)) sum_ij ( trG delta_ij + 2 G_ij ) c_i.c_j reproduces the bracket of Eq. (4.41) of
      2601.08031, delta_ij (d0^2 - (1/5) d^2) - (2/5) d_i d_j, up to terms of relative order l^2/m^2 = 1/s^2.
 (P4) the numbers 1/3, 1/5, 3/5 are the moments of cos^2 theta against the weights 1, n_perp^2, n_par^2.
 (P5) the scout's helicity-zero values at q.y=0 at (5,3).
"""
import sys, os, random
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '046-fibre-regime-interpolation'))
from forms_lib import *
random.seed(4801)

cases = [(5, 3, [R(3, 7), R(1, 2), R(-2, 3), R(1, 5)], 1), (5, 3, [R(-1, 3), R(2, 5), R(1, 4), R(-3, 2)], 1), (5, 3, [R(2, 1), R(1, 3), R(-1, 2), R(1, 4)], 1),
         (13, 5, [R(2, 3), R(-1, 2), R(1, 3), R(1, 7)], 1), (5, 4, [R(1, 9), R(3, 4), R(-1, 2), R(2, 3)], 1), (-5, 3, [R(3, 7), R(1, 2), R(-2, 3), R(1, 5)], 1),
         (-5, 3, [R(3, 7), R(1, 2), R(-2, 3), R(1, 5)], -1), (5, 3, [R(0), R(1, 2), R(-2, 3), R(1, 5)], 1), (13, 5, [R(0), R(0), R(0), R(1)], 1)]
nvecs = [(R(1, 3), R(2, 3), R(2, 3)), (R(2, 7), R(-3, 7), R(6, 7)), (R(1, 9), R(4, 9), R(-8, 9)), (R(0), R(3, 5), R(4, 5))]

def pointwise(y0, y4, qq, chi, nv):
    """direct evaluation at one fibre point with the routines of forms_lib, same construction as cp12_forms"""
    S, ell = Smodel(y0, y4, chi); m = sp.Integer(y4); q = sp.Matrix(qq); qu = ETA * q
    s = [Si * q for Si in S]
    Dv = sp.symbols('D0:9'); gv = sp.symbols('g0:3'); Dm = sp.Matrix(3, 3, Dv)
    c = [sum((Dm[i, j] * s[j] for j in range(3)), sp.zeros(4, 1)) + gv[i] * qu for i in range(3)]
    n = sp.Matrix(nv); NN = n * n.T
    dE = sp.zeros(4, 4)
    for i in range(3):
        for j in range(3): dE += NN[i, j] * c[i] * s[j].T
    gamma_bar = m ** 2 * ETA.inv(); Eb = m * ETA.inv()
    dgamma = Eb.T * ETA * dE + dE.T * ETA * Eb
    K = [qu * c[i].T - c[i] * qu.T for i in range(3)]
    dT = [[[-m * sum(NN[i, j] * s[j][mu] * K[i][a, b] for i in range(3) for j in range(3)) for mu in range(4)] for b in range(4)] for a in range(4)]
    sc, eh = scalar_form(gamma_bar, dgamma, q)
    ix = index_form(gamma_bar, dT, ETA)
    alpha0 = sum((n[i] * sum((Dm[i, j] * s[j] for j in range(3)), sp.zeros(4, 1)) for i in range(3)), sp.zeros(4, 1))
    v = sum((n[j] * s[j] for j in range(3)), sp.zeros(4, 1))
    dot = lambda a, b: (a.T * ETA * b)[0]
    q2 = (q.T * ETA * q)[0]
    ix_c = q2 * dot(v, v) * dot(alpha0, alpha0) / m ** 4
    sc_c = -q2 * (dot(alpha0, alpha0) * dot(v, v) + 2 * dot(alpha0, v) ** 2) / (24 * m ** 4)
    # EH of the trace-reversed perturbation
    return sp.expand(ix), sp.expand(sc), sp.expand(ix_c), sp.expand(sc_c), Dv, gv, eh, q2, m, dot, alpha0, v

print("(P1) pointwise densities against the exact routines of forms_lib, g dependence, 4 fibre points x 5 cases")
okP1 = True
for (y0, y4, qq, chi) in cases[:5]:
    for nv in nvecs:
        ix, sc, ixc, scc, Dv, gv, eh, q2, m, dot, a0, v = pointwise(y0, y4, qq, chi, nv)
        g0 = {g: 0 for g in gv}
        r1 = sp.expand(ix.subs(g0) - ixc); r2 = sp.expand(sc.subs(g0) - scc)
        r3 = sp.expand(ix - ix.subs(g0)); r4 = sp.expand(sc - sc.subs(g0))
        ok = (r1 == 0 and r2 == 0 and r3 == 0 and r4 == 0)
        okP1 = okP1 and ok
        if not ok: print("  FAIL", (y0, y4), nv, r1 == 0, r2 == 0, r3 == 0, r4 == 0)
print("   all residuals exactly zero:", okP1)

print("\n(P2) fibre averages against cp12_forms on all nine D, exact rational, including static (q0=0) and pure-k cases")
okP2 = True
for (y0, y4, qq, chi) in cases:
    F = cp12_forms(y0, y4, qq, chi=chi)
    sub0 = {g: 0 for g in F['gv']}
    D = sp.Matrix(3, 3, F['Dv']); G = gram(F); m = F['m']; q = F['q']; q2 = (q.T * ETA * q)[0]
    P = D * G * D.T; A = D * G
    base = G.trace() * P.trace() + 2 * (G * P).trace()
    IX2c = q2 * base / (15 * m ** 4)
    SC2c = -q2 * (base + 2 * (A.trace() ** 2 + (A * A.T).trace() + (A * A).trace())) / (360 * m ** 4)
    r1 = sp.expand(F['IX2'].subs(sub0) - IX2c); r2 = sp.expand(F['SC2'].subs(sub0) - SC2c)
    r3 = sp.expand(F['IX2'] - F['IX2'].subs(sub0)); r4 = sp.expand(F['SC2'] - F['SC2'].subs(sub0))
    ok = (r1 == 0 and r2 == 0 and r3 == 0 and r4 == 0)
    okP2 = okP2 and ok
    print("   (y0,y4)=(%d,%d) chi=%+d q=%s : residuals zero: IX2 %s, SC2 %s, gauge independence %s" % (y0, y4, chi, [str(x) for x in qq], r1 == 0, r2 == 0, r3 == 0 and r4 == 0))
print("   all exact:", okP2)

print("\n(P3) dictionary, symbolic in q0,k,l,m (q along the third axis)")
q0, k, l, m = sp.symbols('q0 k l m', positive=True)
q2 = k ** 2 - q0 ** 2
y02 = l ** 2 + m ** 2
a = l ** 2 * q2 + q0 ** 2 * y02
b = -m ** 2 * q2
print("   a - (m^2 q0^2 + l^2 k^2) =", sp.expand(a - (m ** 2 * q0 ** 2 + l ** 2 * k ** 2)))
print("   a - b - y0^2 k^2 =", sp.expand(a - b - y02 * k ** 2))
print("   4a+b - [5 m^2 (q0^2 - k^2/5) + 4 l^2 k^2] =", sp.expand(4 * a + b - (5 * m ** 2 * (q0 ** 2 - k ** 2 / 5) + 4 * l ** 2 * k ** 2)))
print("   2a+3b - [5 m^2 (q0^2 - 3k^2/5) + 2 l^2 k^2] =", sp.expand(2 * a + 3 * b - (5 * m ** 2 * (q0 ** 2 - 3 * k ** 2 / 5) + 2 * l ** 2 * k ** 2)))
qh = sp.Matrix([0, 0, 1]); Gs = a * sp.eye(3) - (a - b) * qh * qh.T
Bracket = (Gs.trace() * sp.eye(3) + 2 * Gs)
# bracket of (4.41) in momentum space: delta_ij (d0^2 - d^2/5) - (2/5) d_i d_j -> -[delta_ij (q0^2 - k^2/5) - (2/5) k_i k_j]
pub = 5 * m ** 2 * (q0 ** 2 * sp.eye(3) - k ** 2 / 5 * sp.eye(3) - R(2, 5) * k ** 2 * qh * qh.T)
diff = (Bracket - pub).applyfunc(sp.expand)
print("   (trG 1 + 2G) - 5 m^2 [delta_ij (q0^2 - k^2/5) - (2/5) k_i k_j] =", diff.tolist())
print("   the difference is l^2 k^2 (4 delta_ij - 2 qhat_i qhat_j):", (diff - l ** 2 * k ** 2 * (4 * sp.eye(3) - 2 * qh * qh.T)).applyfunc(sp.expand).is_zero_matrix)

print("\n(P3b) Fourier sign of the printed Eq. (4.44): A Box (d0^2 - d^2/5 - m_c^2) A, Box = -gamma d d -> m^2 q^2, d0^2 -> -q0^2, d_i^2 -> -k^2")
mc = sp.Symbol('m_c', positive=True)
print("   second factor ->", sp.expand(-q0 ** 2 + k ** 2 / 5 - mc ** 2), " = -(q0^2 - k^2/5 + m_c^2), the factor printed in (4.46)")

print("\n(P4) moments of cos^2 theta, n3 = cos theta")
n1, n2, n3 = NSYM
print("   <n3^2> =", fibre_avg(n3 ** 2), "; <n3^2 n1^2>/<n1^2> =", fibre_avg(n3 ** 2 * n1 ** 2) / fibre_avg(n1 ** 2), "; <n3^2 n3^2>/<n3^2> =", fibre_avg(n3 ** 4) / fibre_avg(n3 ** 2))

print("\n(P5) helicity-zero eigenvalues at q.y=0, (y0,y4)=(5,3), exact forms against the printed closed forms and the scout's values")
F = cp12_forms(5, 3, [R(0), R(0), R(0), R(1)]); f = D_forms(F)
EH, IX2, SC2 = f['EH1'][:6, :6], f['IX2'][:6, :6], f['SC2'][:6, :6]
G = gram(F); print("   Gram matrix", G.tolist())
Es, _ = sym_ant_basis()
d = lambda Mat: sp.Matrix([Mat[i, j] for (i, j) in SYM_IDX])  # components in the symmetric basis
Dh0 = sp.diag(G[2, 2], G[2, 2], -2 * G[0, 0])          # traceless on G, rotationally symmetric about qhat
assert (G * Dh0).trace() == 0
vec = sp.Matrix([Dh0[0, 0], Dh0[1, 1], Dh0[2, 2], 0, 0, 0])
lam_ix = (vec.T * IX2 * vec)[0] / (vec.T * EH * vec)[0]; lam_sc = (vec.T * SC2 * vec)[0] / (vec.T * EH * vec)[0]
s2 = R(9, 16); x = -1 / s2
print("   IX2/EH =", lam_ix, float(lam_ix), " closed -(6/5)[2+(2+1/x)(1+(x-1)2/3)] =", -R(6, 5) * (2 + (2 + 1 / x) * (1 + (x - 1) * R(2, 3))), " scout -4+(2/5)s^2+8/(5 s^2) =", -4 + R(2, 5) * s2 + R(8, 5) / s2)
print("   SC2/EH =", lam_sc, float(lam_sc), " closed =", R(1, 20) * (6 + (2 + 1 / x) * (1 + (x - 1) * R(2, 3))), " scout (1/20)[22/3 - s^2/3 - 4/(3 s^2)] =", R(1, 20) * (R(22, 3) - s2 / 3 - R(4, 3) / s2))
