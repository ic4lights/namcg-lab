"""
Helicity-sector (about the spatial direction of q) analysis of the leading-symbol tree+induced form, exact/symbolic.
In the eigenbasis of G: G = diag(g, g, xi),  g = q_perp^2,  xi = -sigma q^2  (sigma = y4^2/ell5^2).
Colour matrix D (3x3), tree form A = q^2 tr(D G D^T), induced form B = 2 q^2 [tr(D^S G D^S G) - (tr D^S G)^2]
(from c^T Mlow c = q^2 tr(D G D^T) and h.E[h] = (q^2/2)(h.h - (tr h)^2), h = 2 s^T D^S s).
Total form  Lam*A + w*B.  Generalised eigenvalues lambda of (B - lambda A) on the 9-dim space; poles: Lam + w lambda = 0.
Also: eigenvalues of the crossover operator  Lc = (1/2) L^{-1} o (2 - P tr)  acting on transverse symmetric E, so that
(w + Lam Lc) E = T  (Lc has dimension 1/q^2).
Cross-check against proposals/014 generalised eigenvalues (q=(0,1/3,-5,3), base (5,3): ratios to q^2 = 2, 7/16, -1 +- i sqrt(14)/2).
"""
import sympy as sp
g, xi, q2, Lam, w, lam = sp.symbols('g xi q2 Lam w lam')
Gm = sp.diag(g, g, xi)
d = sp.Matrix(3, 3, lambda i, j: sp.Symbol('d%d%d' % (i, j)))
ds = (d + d.T)/2
A = sp.expand(q2*(d*Gm*d.T).trace())
B = sp.expand(2*q2*((ds*Gm*ds*Gm).trace() - (ds*Gm).trace()**2))
vars_ = list(d)
def hess(f):
    return sp.Matrix(9, 9, lambda i, j: sp.diff(f, vars_[i], vars_[j]))/2
HA, HB = hess(A), hess(B)
pen = sp.factor((HB - lam*HA).det())
print("det(B - lam A) on D-space (9x9):", pen)
roots = sp.roots(sp.Poly(sp.numer(sp.together(pen)), lam))
print("generalised eigenvalues lambda (with multiplicity):", roots)
tot = sp.factor((Lam*HA + w*HB).det())
print("det(Lam A + w B):", tot)
# numeric cross-check with 014: base (5,3), q=(0,1/3,-5,3): q2=307/9, g=q2 (q.y=0), sigma=9/16, xi=-sigma q2
q2v = sp.Rational(307, 9); sg = sp.Rational(9, 16)
vals = {g: q2v, xi: -sg*q2v, q2: q2v}
rv = sp.roots(sp.Poly(sp.numer(sp.together(pen.subs(vals))), lam))
print("014 cross-check: lambda/q^2 =", sorted([sp.nsimplify(k/q2v) for k in rv], key=lambda z: sp.re(sp.N(z))), " (014: 0 x3, 2 x2, 7/16 x2, -1 +- i sqrt(14)/2)")
# crossover operator Lc on transverse symmetric tensors, basis adapted: components E_ab in orthonormal-like frame where Q=G
# Work with symmetric matrix Z (3x3) in the s-basis dual comps: L[Z] = G Z + Z G, tr = tr(G^{-1} .)?  Use covariant form:
# for E with s-basis components Ehat_ij = E(s_i,s_j): L acts as Ehat -> G Zhat + Zhat G (derived: (eta Q) Z + Z (Q eta) evaluated on (s_i,s_j));
# P tr E: (P)(s_i,s_j) = G_ij, tr E = tr(G^{-1} Ehat).
Z = sp.Matrix(3, 3, lambda i, j: sp.Symbol('z%d%d' % (min(i, j), max(i, j))))
zs = sorted(Z.free_symbols, key=str)
Lc_rows = []
Ehat = sp.Matrix(3, 3, lambda i, j: sp.Symbol('e%d%d' % (min(i, j), max(i, j))))
es = sorted(Ehat.free_symbols, key=str)
R = 2*Ehat - Gm*(Gm.inv()*Ehat).trace()
LZ = Gm*Z + Z*Gm
sol = sp.solve(list(LZ - R), zs, dict=True)[0]
Zs = Z.subs(sol)
Lc = sp.Matrix([[sp.diff(Zs[i, j], e)/2 for e in es] for (i, j) in [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]])
# Lc here maps Ehat -> (1/2)... note: (Lam/2) L^{-1}[R] : define Lc = (1/2) L^{-1}[R]; (w + Lam Lc) E = T
# express as 6x6 matrix on components (e00,e11,e22,e01,e02,e12)
order = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
es_ord = [Ehat[i, j] for (i, j) in order]
Lmat = sp.Matrix([[sp.diff(Zs[i, j], e)/2 for e in es_ord] for (i, j) in order])
print("Lc matrix eigenvalues (units 1/q^2):")
for k, m in sp.Matrix(Lmat).eigenvals().items():
    print("  ", sp.simplify(k), " mult", m)
print("-> (w + Lam Lc) eigenvalues: w + Lam*(above);  zeros give the poles of the sourced response.")
