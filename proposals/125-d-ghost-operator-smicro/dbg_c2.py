import importlib.util, sys
from sympy import symbols, Matrix, cos, sin, simplify
spec = importlib.util.spec_from_file_location("m", "ghost_linearization_125b.py")
# avoid running the whole module: copy minimal funcs via exec of top section
src = open("ghost_linearization_125b.py").read()
top = src.split('log("== 125')[0]
g = {}
exec(top, g)
X = (symbols('x0'), symbols('x1'))
g['X'] = X
rP, phP = X
metP = Matrix.diag(1, rP**2)
igP, gamP, ricP, CP = g['geom'](metP, 2)
xiP = [rP*cos(phP)**2, -cos(phP)*sin(phP)]
bxP = g['boxvec'](igP, CP, xiP, 2)
gdP = g['grad_div'](igP, CP, xiP, 2)
dgP = g['div_grad'](igP, CP, xiP, 2)
rvP = g['ricvec'](igP, ricP, xiP, 2)
print("box:", [simplify(b) for b in bxP])
print("ric:", [simplify(b) for b in rvP])
print("gd :", [simplify(b) for b in gdP])
print("dvg:", [simplify(b) for b in dgP])
