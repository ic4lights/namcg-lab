from sympy import symbols, Matrix, cos, sin, simplify, diff, Rational, sqrt, expand, log as slog
src = open("ghost_linearization_125b.py").read()
seg = src[src.index("def gamma("):src.index("def solveabc(")]
g = {'simplify': simplify, 'diff': diff, 'Matrix': Matrix, 'R': Rational,
     'sin': sin, 'cos': cos, 'sqrt': sqrt, 'expand': expand, 'slog': slog}
exec(seg, g)
X = (symbols('x0'), symbols('x1'))
g['X'] = X
rP, phP = X
metP = Matrix.diag(1, rP**2)
igP, gamP, ricP, CP = g['geom'](metP, 2)
xiP = [rP*cos(phP)**2, -cos(phP)*sin(phP)]
bxP = [simplify(b) for b in g['boxvec'](igP, CP, xiP, 2)]
gdP = [simplify(b) for b in g['grad_div'](igP, CP, xiP, 2)]
dgP = [simplify(b) for b in g['div_grad'](igP, CP, xiP, 2)]
rvP = [simplify(b) for b in g['ricvec'](igP, ricP, xiP, 2)]
print("box:", bxP)
print("ric:", rvP)
print("gd :", gdP)
print("dvg:", dgP)
