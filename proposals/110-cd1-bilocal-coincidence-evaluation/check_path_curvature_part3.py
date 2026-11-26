# P3/P4 block (runs after check_path_curvature.py and part2; Dc[1] = eps^2 coeff)
# P3: commutative (single-generator) subcase: C2 -> c2*C1, B_{rho mu} -> b_{..}*C1.
c2s = sp.symbols('c2')
bmat = {'B11': B11, 'B12': B12, 'B21': B21, 'B22': B22}
bsym = {nm: sp.symbols(nm + 's') for nm in bmat}
subs3 = [(C2[i, j], c2s*C1[i, j]) for i in range(3) for j in range(3)]
for nm, M in bmat.items():
    subs3 += [(M[i, j], bsym[nm]*C1[i, j]) for i in range(3) for j in range(3)]
Dcomm = sp.expand(Dc[1].subs(subs3))
Fder = sp.Rational(1, 2) * a * b * (bsym['B21'] - bsym['B12']) * C1
ck("P3 abelian subcase: loop coeff = (ab/2)(d1 w2 - d2 w1), commutator gone",
   sp.simplify(Dcomm - Fder) == sp.zeros(3))

# P4: so(eta) closure of the loop coefficient
eta = sp.diag(-1, 1, 1, 1)
T = []
for i in range(4):
    for j in range(i+1, 4):
        Mgen = sp.zeros(4)
        if i == 0:
            Mgen[0, j] = 1; Mgen[j, 0] = 1
        else:
            Mgen[i, j] = 1; Mgen[j, i] = -1
        T.append(Mgen)
ck("P4a basis eta-antisymmetric",
   all(sp.simplify(t.T*eta + eta*t) == sp.zeros(4) for t in T))
coeffs = [sp.symbols(f"q{k}") for k in range(12)]
w1x = sp.zeros(4)
w2x = sp.zeros(4)
for c, t in zip(coeffs[:6], T):
    w1x = w1x + c*t
for c, t in zip(coeffs[6:], T):
    w2x = w2x + c*t
F12 = w1x*w2x - w2x*w1x
ck("P4b so(eta) closed under commutator",
   sp.simplify(F12.T*eta + eta*F12) == sp.zeros(4))

print("LOOPCOEFF_over_halfab verified for L-path; parabolic = ab/6 area.")
print("FAILURES:", fails)
print("ALL CHECKS PASS" if not fails else "CHECKS FAILED")
