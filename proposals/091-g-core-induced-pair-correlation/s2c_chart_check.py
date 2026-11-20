# s2c_chart_check.py - verify claim (1) of s2 by trigsimp and by 6 random numeric substitutions.
# Run: python -I proposals/091-g-core-induced-pair-correlation/s2c_chart_check.py
import sympy as sp, random
y1, y2, th, phi = sp.symbols('y1 y2 theta phi', real=True)
c, s = sp.cos(th), sp.sin(th)
U = sp.Matrix([[c, s*sp.exp(sp.I*phi)], [-s*sp.exp(-sp.I*phi), c]])
Z = U * sp.diag(y1, y2) * U.H
rows = [[sp.simplify(sp.expand_complex(t)) for t in e.as_real_imag()]
        for e in (Z[0, 0], Z[0, 1], Z[1, 1])]
coords = (rows[0][0], rows[1][0], rows[1][1], rows[2][0])
params = (th, phi, y1, y2)
Jm = sp.Matrix([[sp.diff(rd, p) for p in params] for rd in coords])
detJ = Jm.det()
target = sp.Rational(1, 2)*(y1 - y2)**2*sp.sin(2*th)
diff = sp.trigsimp(sp.expand_trig(sp.expand(detJ - target)))
print("(1') trigsimp(det J - target) == 0 symbolic:", sp.simplify(diff) == 0)
rnd = random.Random(91)
bad = 0
for _ in range(6):
    vals = {y1: sp.Rational(rnd.randint(1, 9), 4), y2: sp.Rational(rnd.randint(10, 19), 4),
            th: sp.Rational(rnd.randint(1, 44), 64), phi: sp.Rational(rnd.randint(1, 62), 64)}
    d = complex(sp.N(detJ.subs(vals) - target.subs(vals), 40))
    bad += abs(d) > 1e-30
print("(1'') 6 random rational points, all matching:", bad == 0)
# exponent of coincidence: det J / (y1-y2)^2 smooth and nonzero at y1=y2 (a.e. in theta)
at = sp.simplify((detJ/(y1 - y2)**2).subs(y2, y1))
print("(1''') det J/(y1-y2)^2 at coincidence =", sp.trigsimp(at), " (nonzero a.e., exponent exactly 2)")
