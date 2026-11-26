"""043 / s3: bookkeeping of edge terms against the gap c_A - c_T (n_D = 0), in units of c.

Inputs, all merged in Appendix H (Problem B):
  c_A  = N_tot/6                (fixed-state replica, rho regular)                       [015]
  c_T  = N_tot/6 - 4 kappa_X    (tensor coefficient on the two delta rho = 0 modes)      [015, 038]
  c_W(r) = N_tot/6 + kappa_X r  (Noether coefficient of the presentation r)              [038, 042]
  Moser variables: a_1(Maxwell-axion) = -R_G/3 + box ln rho - |V|^2 + 6 s |d theta - theta V|^2  [041]
  stationary-set identity: s|d theta - theta V|^2 = -R_G/2 + |V|^2 - 3/2 box ln rho       [041, numerical]
  contact rule: E = Q R with conical delta shifts c by -tr Q                              [015 contact paragraph]
Checks:
 (1) the Ricci delta R_mn -> 2 pi (1-n) n_mn delta, traced over the four components of a one-form,
     equals the delta of R -> 4 pi (1-n) delta: tr Q_eff = 1, the Kabat shift Delta c = -1 per vector.
 (2) the Hodge (Moser) vector operator has R-coefficient -1/3 in a_1, i.e. 4/6 - 1: r = -1 for kappa_X = 1,
     and c_A - 1 = c_W(-1) (n_D = 0).
 (3) the axion-gradient term carries, through the stationary-set identity, the coefficient -3 of R_G:
     X = -R - box ln rho + 6 s|..|^2 = -4 R + 6|V|^2 - 10 box ln rho, so r = -4 = -1 + (-3).
 (4) residues c - c_T for the edge terms considered: T^op superpotential (r = -4 by construction): 0
     relative to c_T but c_A - c_T = 4 kappa_X; Chen-type Noether charge of the tree-level fluctuation
     Lagrangians: 0 -> residue 4 kappa_X; Maxwell edge sector (Moser): -kappa_X -> residue 3 kappa_X.
"""
import sympy as sp

N, kX, n = sp.symbols('N_tot kappa_X n')
cA = N / 6
cT = N / 6 - 4 * kX
cW = lambda r: N / 6 + kX * r
ok = True

# (1) Ricci delta traced over a one-form fibre vs scalar curvature delta
eta = sp.diag(1, 1, 1, 1)
nmn = sp.diag(1, 1, 0, 0)                  # projector on the normal plane of Sigma
ric_delta_trace = sum(2 * sp.pi * (1 - n) * nmn[i, i] for i in range(4))
R_delta = 4 * sp.pi * (1 - n)
trQ = sp.simplify(ric_delta_trace / R_delta)
print(f"(1) trace of the Ricci delta over a one-form / delta of R = {trQ}  -> Kabat shift Delta c = {-trQ} per vector")
ok &= trQ == 1

# (2) Hodge operator: a_1 coefficient of R (per vector, convention O = -nabla^2 + E, a_1 = tr(R/6 - E), E = Ric)
a1R_vector = sp.Rational(4, 6) - trQ
r_moser = sp.solve(sp.Eq(sp.Rational(4, 6) + 1 * sp.Symbol('r'), a1R_vector), sp.Symbol('r'))[0]
print(f"(2) R-coefficient of a_1 for the Hodge operator per vector = {a1R_vector} = 4/6 + kappa_X r with r = {r_moser}")
ok &= a1R_vector == sp.Rational(-1, 3) and r_moser == -1
print(f"    c_A - 1 - c_W(-1) at kappa_X = 1: {sp.simplify((cA - 1 - cW(-1)).subs(kX, 1))}")
ok &= sp.simplify((cA - 1 - cW(-1)).subs(kX, 1)) == 0

# (3) stationary-set identity: X in Moser variables
R, BL, V2, ax = sp.symbols('R boxlnrho V2 axion')        # ax = s|d theta - theta V|^2
X_moser = -R - BL + 6 * ax
ax_on_set = -R / 2 + V2 - sp.Rational(3, 2) * BL
X_on_set = sp.expand(X_moser.subs(ax, ax_on_set))
print(f"(3) X on the stationary set = {X_on_set}; R-coefficient {X_on_set.coeff(R)} = -1 (Hodge) + {sp.expand(6*ax_on_set).coeff(R)} (axion gradient)")
ok &= X_on_set.coeff(R) == -4 and sp.expand(6 * ax_on_set).coeff(R) == -3

# (4) residues at n_D = 0
rows = [('T^op superpotential, edge term carried by T^op (r = -4)', cW(-4)),
        ('fixed-state replica, no extra edge term (r = 0)', cA),
        ('Chen-type Noether charge of tree-level fluctuation Lagrangians (zero on Sigma)', cA + 0),
        ('Maxwell edge sector in Moser variables (Kabat value -1 per vector)', cA - kX),
        ('stipulated local dressing (039), r = -2', cW(-2))]
for name, val in rows:
    print(f"(4) {name}: c = {sp.simplify(val)}, c - c_T = {sp.simplify(val - cT)}")
ok &= sp.simplify(cW(-4) - cT) == 0 and sp.simplify(cA - cT) == 4 * kX and sp.simplify(cA - kX - cT) == 3 * kX
print("ALL CHECKS PASSED" if ok else "SOME CHECK FAILED")
