import sympy as sp

# S3: fixed-D obstruction extrema on the constancy slice and comparison with the
# 082 sharp floor rho_p >= prod_{k=1}^{p-1}(1+k/D), equality iff uniform profile.
# rho_p(g) = p! h_p(g)/W^p, h_p complete homogeneous symmetric polynomial (081).

def h_complete(xs, p):
    # h_p = coefficient of t^p in prod_i 1/(1-x_i t); computed by convolution.
    coeff = [sp.sympify(1)] + [sp.sympify(0)]*p
    for x in xs:
        pw = [sp.sympify(1)]
        for n in range(1, p+1):
            pw.append(sp.expand(pw[n-1]*x))
        new = [sp.sympify(0)]*(p+1)
        for i in range(p+1):
            for j in range(p+1-i):
                new[i+j] = sp.expand(new[i+j] + coeff[i]*pw[j])
        coeff = new
    return coeff[p]

def rho_p(gv, p):
    Wv = sum(gv)
    return sp.simplify(sp.factorial(p)*h_complete(list(gv), p)/Wv**p)

# uniform profile D=4 attains the 082 floor.
for p in (2, 3, 4):
    val = rho_p([sp.Rational(1, 4)]*4, p)
    floor4 = sp.prod(1 + sp.Rational(k, 4) for k in range(1, p))
    print("uniform D=4 p=%d: rho_p = %s, 082 floor = %s, equal: %s" % (p, val, floor4, sp.simplify(val-floor4) == 0))

# two-block family on the slice for D=4, m=2: g = (a,a,b,b), b=(1-2a)/2 (W=1).
a = sp.symbols('a', real=True)
g2b = [a, a, (1-2*a)/2, (1-2*a)/2]
for p in (2, 3, 4):
    rp = sp.simplify(rho_p(g2b, p))
    der = [aa for aa in sp.solve(sp.Eq(sp.diff(rp, a), 0), a) if aa.is_real]
    print("two-block D=4 m=2 p=%d: interior critical rho %s ; uniform point a=1/4: %s"
          % (p, [sp.nsimplify(rp.subs(a, aa)) for aa in der], sp.nsimplify(rp.subs(a, sp.Rational(1, 4)))))

# nonuniform profiles strictly above the floor (D=4, p<=4).
tests = [[sp.Rational(3, 4), sp.Rational(1, 12), sp.Rational(1, 12), sp.Rational(1, 12)],
         [sp.Rational(1, 2), sp.Rational(1, 6), sp.Rational(1, 6), sp.Rational(1, 6)]]
for p in (2, 3, 4):
    fl = sp.prod(1 + sp.Rational(k, 4) for k in range(1, p))
    for gv in tests:
        rv = rho_p(gv, p)
        print("nonuniform p=%d: rho_p = %s > floor %s : %s" % (p, rv, fl, sp.simplify(rv-fl) > 0))

# frame-conditional sum g^2 on the equal-rest constancy slice.
for (Dn, m) in [(4, 2), (5, 3)]:
    Ubar, Ws = sp.symbols('Ubar Wsym', positive=True)
    Sq = m*Ubar**2 + (Ws-m*Ubar)**2/(Dn-m)
    print("slice sumsq D=%d m=%d at Ubar=W/D: %s ; at Ubar=0: %s ; at Ubar=W/m: %s"
          % (Dn, m, sp.simplify(Sq.subs(Ubar, Ws/Dn)), sp.simplify(Sq.subs(Ubar, 0)),
             sp.simplify(Sq.subs(Ubar, Ws/m))))

# uniform ladder limit: rho_p(uniform, D) = prod_{k=1}^{p-1}(1+k/D) -> 1 as D -> inf.
D = sp.symbols('D', positive=True)
for p in (2, 3, 4, 8):
    kk = sp.symbols("k", integer=True, positive=True)
    expr = sp.product(1 + kk/D, (kk, 1, p-1))
    print("uniform rho_p ladder p=%d: limit D->inf:" % p, sp.limit(expr, D, sp.oo))
print("S3 DONE")
