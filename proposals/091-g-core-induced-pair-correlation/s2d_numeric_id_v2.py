# s2d_numeric_id_v2.py - numeric/limit re-checks: chart coincidence limit, Var(p1)=3/(8a+12),
# 089 D=2 density identity.  Run from repo root:
#   python -I proposals/091-g-core-induced-pair-correlation/s2d_numeric_id_v2.py
import sympy as sp, random
y1, y2, th, phi = sp.symbols('y1 y2 theta phi', real=True)
a, x, g1, g2, T = sp.symbols('a x g1 g2 T', positive=True)
c, s = sp.cos(th), sp.sin(th)
U = sp.Matrix([[c, s*sp.exp(sp.I*phi)], [-s*sp.exp(-sp.I*phi), c]])
Z = U * sp.diag(y1, y2) * U.H
rows = [[sp.simplify(sp.expand_complex(t)) for t in e.as_real_imag()]
        for e in (Z[0, 0], Z[0, 1], Z[1, 1])]
coords = (rows[0][0], rows[1][0], rows[1][1], rows[2][0])
Jm = sp.Matrix([[sp.diff(rd, p) for p in (th, phi, y1, y2)] for rd in coords])
detJ = Jm.det()
lim = sp.trigsimp(sp.limit(detJ/(y1 - y2)**2, y2, y1))
print("(i) limit detJ/(y1-y2)^2 at y2=y1 ==", lim, " ; == (1/2)sin(2 theta):",
      bool(sp.simplify(lim - sp.Rational(1, 2)*sp.sin(2*th)) == 0))
rnd = random.Random(92)
bad = 0
for _ in range(8):
    av = sp.Rational(rnd.randint(1, 40), 4)
    lhs = 3*sp.gamma(av + sp.Rational(3, 2))/(8*sp.gamma(av + sp.Rational(5, 2)))
    bad += float(abs(sp.N(lhs - 3/(8*av + 12), 30))) > 1e-25
print("(ii) 8 points, Var(p1) == 3/(8a+12):", bad == 0)
bad = 0
for _ in range(8):
    gv = {g1: sp.Rational(rnd.randint(1, 17), 4), g2: sp.Rational(rnd.randint(1, 17), 4),
          x: sp.Rational(rnd.randint(1, 99), 100)}
    L = 1/(g1*g2*(x/g1 + (1-x)/g2)**2)
    R = sp.integrate(T*sp.exp(-T*(x/g1 + (1-x)/g2))/(g1*g2), (T, 0, sp.oo))
    bad += float(abs(sp.N((L - R).subs(gv), 30))) > 1e-25
print("(iii) 8 points, direct fibre integral == integrated 089 closed form:", bad == 0)
print("S2D-V2 DONE")
