"""
s2_helicity_two_poles.py (proposal 048). Prints to stdout only; writes nothing.

Helicity +-2 level-one two-point function with the tree form (leading symbol, frozen point, phase average).

Conventions: S_E[tree] = (rho_M/(4 g^2)) m^2 (q^2 <alpha.alpha> - <(q.alpha)^2>) per unit d^4y, from S_E = (1/(4g^2)) Tr F_ab F^ab
with Tr f = int d^4y rho_M <f>_fibre.  S_E[induced] = -(1/(32 pi^2)) [ W_R forms + W_X forms ], merged normalisation.
Formal continuation S_L = -S_E with the Lorentzian eta (the status of this continuation is that of the merged paragraphs).
Weights: V_0,T_0 (D), V_1,T_1 (B_1), V_2,T_2 (B_0), as in the merged 047 paragraph.

Checks:
 (A) coefficient c(x) = c_TT + kappa/x, kappa = (V1-T1)/20 + (3/20) T2, and the polynomial form in the amplitude c;
 (B) the two factors, v^2 and mu^2; 1 - v^2 = c_TT theta/(c_TT+kappa);
 (C) residues on q0^2 at fixed k in the amplitude c and in hbar;
 (D) exact-rational numerical confirmation at sampled data with forms from forms_lib (no closed form used);
 (E) quartic lemma: adding V00 + V01 q0^2, residues and the shift of the would-be massless root.
"""
import sys, os
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '046-fibre-regime-interpolation'))
from forms_lib import *

q0, k, l, m = sp.symbols('q0 k l m', positive=True)
V0, V1, V2, T0, T1, T2, t = sp.symbols('V0 V1 V2 T0 T1 T2 t', positive=True)
pi = sp.pi
q2 = k ** 2 - q0 ** 2
a = m ** 2 * q0 ** 2 + l ** 2 * k ** 2
b = -m ** 2 * q2
x = a / b
s2 = m ** 2 / l ** 2; th = 1 + l ** 2 / m ** 2

print("(A) helicity +-2 eigenvalues relative to EH(hbar) (merged closed forms) and induced coefficient")
IX2 = -R(6, 5) * (4 + 1 / x)      # phi=0: -(6/5)[2+(2+1/x)]
SC2 = R(1, 20) * (6 + 2 + 1 / x)  # r=1, phi=0
L1 = SC2 - R(1, 6)
WR0, WR1, WX0, WX2 = V0 - T0, V1 - T1, -T0 / 8, -T2 / 8
cx = WR0 / 6 + WR1 * L1 + WX0 * (-2) + WX2 * (IX2 + 2)
cTT = V0 / 6 + T0 / 12 + R(7, 30) * (V1 - T1) + R(7, 20) * T2
kap = (V1 - T1) / 20 + R(3, 20) * T2
print("   c(x) - (c_TT + kappa/x) =", sp.simplify(cx - (cTT + kap / x)))
print("   kappa >= (V1 + 2 T1)/20 when T2 >= T1: kappa - (V1+2T1)/20 =", sp.simplify(kap - (V1 + 2 * T1) / 20), " = 3 (T2-T1)/20 :", sp.simplify(kap - (V1 + 2 * T1) / 20 - R(3, 20) * (T2 - T1)) == 0)

print("\n(B) total form in the amplitude: EH = -q^2 hbar.hbar/(8m^6), hbar.hbar = (4m^2/9) a (c.c) on helicity +-2")
EHc = -q2 * (4 * m ** 2 / 9) * a / (8 * m ** 6)   # per unit c.c
indE = -(1 / (32 * pi ** 2)) * (cTT + kap / x) * EHc
print("   induced S_E / (q^2 c.c) - (c_TT a + kappa b)/(576 pi^2 m^4) =", sp.simplify(indE / q2 - (cTT * a + kap * b) / (576 * pi ** 2 * m ** 4)))
Z = (cTT + kap) / (576 * pi ** 2 * m ** 2)
vv = (kap - cTT * l ** 2 / m ** 2) / (cTT + kap)
print("   (c_TT a + kappa b) - (c_TT+kappa) m^2 (q0^2 - v^2 k^2) =", sp.simplify(cTT * a + kap * b - (cTT + kap) * m ** 2 * (q0 ** 2 - vv * k ** 2)))
print("   1 - v^2 - c_TT theta/(c_TT+kappa) =", sp.simplify(1 - vv - cTT * th / (cTT + kap)))
print("   index-only, degenerate weights V_i=T_i=T: v^2 =", sp.simplify(vv.subs({V0: T0, V1: T0, T1: T0, T2: T0}, simultaneous=True)), " (tends to 1/5 as l/m -> 0)")
rho_M, g2 = sp.symbols('rho_M g2', positive=True)
tree = rho_M * m ** 2 / (12 * g2)   # S_E[tree] = q^2 (c.c) tree, <alpha.alpha> = c.c/3
mu2 = tree / Z
print("   mu^2 = tree/Z =", sp.simplify(mu2), " = 48 pi^2 rho_M m^4/(g^2 (c_TT+kappa))")

print("\n(C) residues in q0^2 at fixed k. S_L = (c.c) Z (q0^2-k^2)(q0^2-w^2), w^2 = v^2 k^2 - mu^2")
w2, X = sp.symbols('w2 X', real=True)     # X = q0^2
Sc = Z * (X - k ** 2) * (X - w2)
print("   -S_E/(c.c) - Z (q0^2-k^2)(q0^2-w^2) =", sp.simplify((-q2 * (Z * (q0 ** 2 - vv * k ** 2) + tree) - Z * (q0 ** 2 - k ** 2) * (q0 ** 2 - (vv * k ** 2 - mu2)))))
print("   healthy oscillator: S_L = Z_res (q0^2 - w_0^2) with Z_res > 0.  Coefficient at each root:")
print("     at q0^2 = k^2 :", sp.simplify(sp.diff(Sc, X).subs(X, k ** 2)), " ; at q0^2 = w^2 :", sp.simplify(sp.diff(Sc, X).subs(X, w2)))
print("   k^2 - w^2 = k^2 (1-v^2) + mu^2 > 0 for c_TT>0, c_TT+kappa>0, so the massless root is healthy and the extra root has the opposite sign, in the variable c.")
a_at_w = (m ** 2 * (w2 + l ** 2 / m ** 2 * k ** 2))
print("   in hbar: propagator gets the factor (4m^2/9) a(q0^2); a at the massless root = m^2 theta k^2 > 0; a at the extra root = m^2 (w^2 + k^2/s^2)")
aw = sp.simplify(a_at_w.subs(w2, vv * k ** 2 - mu2))
print("     a(extra) - m^2 (k^2 kappa theta/(c_TT+kappa) - mu^2) =", sp.simplify(aw - m ** 2 * (k ** 2 * kap * th / (cTT + kap) - mu2)))
print("   large-k limit of the massless residue in hbar: (4m^2/9) a / (Z (k^2 - w^2)) ->", sp.simplify(sp.limit(((4 * m ** 2 / 9) * m ** 2 * th * k ** 2 / (Z * (k ** 2 * (1 - vv) + sp.Symbol('M2', positive=True)))), k, sp.oo)), " = 256 pi^2 m^6/c_TT (independent of kappa)")

print("\n(D) exact-rational check at sampled base points, D traceless on the block orthogonal to qhat, using cp12_forms")
for (y0, y4, qq) in [(5, 3, [R(1, 3), R(0), R(0), R(1, 2)]), (13, 5, [R(2, 3), R(0), R(0), R(1, 5)]), (5, 4, [R(1, 7), R(0), R(0), R(9, 4)]), (5, 3, [R(0), R(0), R(0), R(1)])]:
    F = cp12_forms(y0, y4, qq); fs = D_forms(F); M = F['m']; qv = F['q']
    Q2 = (qv.T * ETA * qv)[0]
    G = gram(F); A = G[0, 0]; B = G[2, 2]
    vec = sp.Matrix([1, -1, 0, 0, 0, 0])   # D = diag(1,-1,0) in the symmetric basis: note the basis has E_ii = 2 e_ii
    # symmetric basis E_ii has entries 2 at (i,i); c.c = tr(D G D) = A tr D^2 with D = vec.E
    Dmat = sum((vec[i] * Es_ for i, Es_ in enumerate(sym_ant_basis()[0])), sp.zeros(3, 3))
    cc = (Dmat * G * Dmat).trace()
    Ix2 = (vec.T * fs['IX2'][:6, :6] * vec)[0]; Sc2 = (vec.T * fs['SC2'][:6, :6] * vec)[0]; Eh = (vec.T * fs['EH1'][:6, :6] * vec)[0]
    print("   (y0,y4)=(%d,%d) q0=%s k=%s: IX2 - q^2 (4a+b) c.c/(15 m^4) = %s ; SC2 + q^2 (8a+b) c.c/(360 m^4) = %s ; EH + q^2 a c.c/(18 m^4) = %s"
          % (y0, y4, qq[0], qq[3], sp.simplify(Ix2 - Q2 * (4 * A + B) * cc / (15 * M ** 4)), sp.simplify(Sc2 + Q2 * (8 * A + B) * cc / (360 * M ** 4)), sp.simplify(Eh + Q2 * A * cc / (18 * M ** 4))))

print("\n(E) quartic lemma with the signs of (4.46): (X-k^2)(X-w^2) - V01 X - V00, in units of Z")
V00, V01 = sp.symbols('V00 V01', real=True)
P = (X - k ** 2) * (X - w2) - V01 * X - V00
disc = sp.discriminant(P, X)
print("   discriminant - [(k^2-w^2)^2 + 2 V01 (k^2+w^2) + V01^2 + 4 V00] =", sp.simplify(disc - ((k ** 2 - w2) ** 2 + 2 * V01 * (k ** 2 + w2) + V01 ** 2 + 4 * V00)))
print("   for distinct real roots X1 > X2: P'(X1) = X1 - X2 > 0, P'(X2) = -(X1 - X2) < 0, so the two coefficients have opposite signs.")
eps = sp.Symbol('e'); kk, ww = sp.symbols('kk ww', positive=True)
disc_e = (kk + ww + eps * V01) ** 2 - 4 * (kk * ww - eps * V00)
root = ((kk + ww + eps * V01) + sp.sqrt(disc_e)) / 2
sh = sp.diff(root, eps).subs(eps, 0)
print("   first-order shift of the larger root, at kk=1, ww=1/5:", sp.simplify(sh.subs({kk: 1, ww: sp.Rational(1, 5)})), " ; predicted (V00+V01 kk)/(kk-ww):", sp.simplify(((V00 + V01 * kk) / (kk - ww)).subs({kk: 1, ww: sp.Rational(1, 5)})))
