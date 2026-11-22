# --- I5: total O(l) coefficient: symmetric part is profile+radial only
for r in range(1, 5):
    G1r = G1[r]
    tgt = (1+a)*ar[r-1]*eta + (1+a)**2*sym(eta*e[r-1])
    ck(f"I5 r={r}: sym(G1_r) = (1+a)a_r eta + (1+a)^2 sym(eta e_r)",
       sp.simplify(sym(G1r) - tgt) == sp.zeros(4))
# identically, 2 sym(eta e_r) = eta e_r + (eta e_r)^T = (d_r g+) at locked frame
r1 = e[0]
ck("I5b 2*sym(eta e_1) = d_1 g+ definition",
   sp.simplify(2*sym(eta*r1) - (eta*r1 + r1.T*eta)) == sp.zeros(4))

# --- I7: full O(l^2) symmetric sector: profile f2 + radial e2 + mixed e-w
#      + connector anticommutator (soldering-type); derivatives d_w drop out.
ok7 = True
for (r, s) in [(1, 2), (2, 1), (1, 1), (2, 3)]:
    tgt7 = (Fd2[(r, s)]*eta
            + Fd0*sp.simplify(sym(eta*Ed2[(r, s)]))
            + Fd0*sp.simplify(sym(eta*(w[r-1]*e[s-1] + w[s-1]*e[r-1])))
            + sp.simplify(sym(Fd1[r]*eta*w[s-1] + Fd1[s]*eta*w[r-1]))
            + Fd0*sp.Rational(1, 2)*sp.simplify(
                  sym(eta*(w[r-1]*w[s-1] + w[s-1]*w[r-1])))
            + sp.simplify(sym(Fd1[r]*eta*Ed1[s] + Fd1[s]*eta*Ed1[r])))
    if sp.simplify(sym(G2[(r, s)]) - tgt7) != sp.zeros(4):
        ok7 = False
ck("I7 sym(G2_{rs}) = profile2 + radial2 + mixed(e,w) + 1/2 f sym(eta{w_r,w_s})", ok7)

# --- I6: path-dependent (curvature-type) piece is antisymmetric in (mu,nu)
F12 = dw[(1, 2)] - dw[(2, 1)] - (w[0]*w[1] - w[1]*w[0])
ck("I6 sym(eta F_12) = 0 (path dependence is connector-type, not soldering)",
   sym(eta*F12) == sp.zeros(4))
ck("I6b sym(eta d_1 w_1) = 0 (derivative connector piece antisymmetric)",
   sym(eta*dw[(1, 1)]) == sp.zeros(4))

print("FAILURES:", fails)
print("ALL CHECKS PASS" if not fails else "CHECKS FAILED")
