"""
Null wave content of the leading-symbol tree-level sector (exact, sympy), base point (Y0,Y4), q = (1,1,0,0) covector (null).
Lorenz-gauge Maxwell solutions: q.c_i = 0 (9 amplitudes), modulo c ~ c + q lambda_i (3) -> 6 physical.
 - image of the physical amplitudes in h, modulo linearised diffeomorphisms q o xi;
 - E[h] = +1/2 q_mu q_nu tr(h) (convention of lin_einstein) on the Lorenz solutions (identity check);
 - TT content: are the two transverse-traceless polarisations (h_22 - h_33, h_23) in the image?
"""
import sympy as sp, os
exec(open('check_maxwell_factorisation.py').read().split("# (b) divisibility")[0].replace('print(', 'pass; (lambda *a, **k: None)('))
qn = {q[0]: 1, q[1]: 1, q[2]: 0, q[3]: 0}
qv = sp.Matrix([1, 1, 0, 0])
Lor = [sum(q[a]*cs[a][i] for a in range(4)).subs(qn) for i in range(3)]
sub0 = sp.solve(Lor, [cs[0][i] for i in range(3)], dict=True)[0]
free = [cs[nu][i] for nu in range(1, 4) for i in range(3)]
def vecs(expr_mat):
    return [expr_mat[i, j] for (i, j) in idx]
hl = (eta*hup_of(cs)*eta).applyfunc(lambda x: sp.expand(x.subs(qn).subs(sub0)))
Hmat = sp.Matrix([[sp.diff(e, f) for f in free] for e in vecs(hl)])          # 10 x 9
EHl = lin_einstein(hl, qv).applyfunc(sp.expand)
# identity E = -1/2 q_mu q_nu tr h   (lower indices)
trh = sum(eta[a, a]*hl[a, a] for a in range(4))      # eta^{mu nu} h_{mu nu}
ident = (EHl - sp.Rational(1, 2)*qv*qv.T*trh).applyfunc(sp.expand) == sp.zeros(4, 4)
print("E[h] = +1/2 q q tr h on Lorenz-gauge null solutions:", ident)
# diffeos q o xi (lower indices)
diffs = []
for k in range(4):
    xi = sp.zeros(4, 1); xi[k] = 1
    diffs.append(vecs(qv*xi.T + xi*qv.T))
Dm = sp.Matrix(diffs).T                                  # 10 x 4
rH = Hmat.rank(); rHD = Hmat.row_join(Dm).rank()
print("dim image of Lorenz solutions in h:", rH, "; dim of (image + diffeos):", rHD, "; => image mod diffeo:", rHD - Dm.rank())
# physical amplitudes: 9 Lorenz - 3 gauge (c ~ q lambda) = 6;  of these 3 inert (h=0) and 3 visible in h mod diffeo
print('kernel of H on Lorenz solutions (inert + gauge-to-zero):', 9 - Hmat.rank())
# which Lorenz solutions give tr h = 0 ?
print("tr h as a linear functional on the 9 Lorenz amplitudes is nonzero:", any(sp.diff(trh, f) != 0 for f in free))
# TT polarisations: h_22 - h_33 and h_23 (lower indices), q along x^1, null
def unit(i, j):
    m = sp.zeros(4, 4); m[i, j] = m[j, i] = 1; return sp.Matrix(vecs(m))
TT1 = sp.Matrix(vecs(sp.diag(0, 0, 1, -1))); TT2 = unit(2, 3)
for name, TT in (("h22-h33", TT1), ("h23", TT2)):
    inim = Hmat.row_join(Dm).rank() == Hmat.row_join(Dm).row_join(TT).rank()
    print("TT polarisation", name, "in image(+diffeo):", inim)
