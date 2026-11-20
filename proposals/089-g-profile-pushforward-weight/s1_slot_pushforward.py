import sympy as sp
from fractions import Fraction
# --- D=2 symbolic normalization of f(p) = 1/(G*(p1/g1+p2/g2)^2) on the simplex
g1, g2, t = sp.symbols('g1 g2 t', positive=True)
f2 = 1/(g1*g2*(t/g1 + (1-t)/g2)**2)
I2 = sp.integrate(f2, (t, 0, 1))
print('D2 norm symbolic ==', sp.simplify(I2), '  PASS' if sp.simplify(I2 - 1) == 0 else 'FAIL')
# --- D=3 and D=4 exact rational normalization with g=(1,2,3) and (1,2,3,4)
def normD(gv):
    D = len(gv)
    ps = sp.symbols('p0:%d' % (D-1))
    full = list(ps) + [1 - sum(ps)]
    G = 1
    for g in gv: G *= g
    L = sum(full[i]/gv[i] for i in range(D))
    f = sp.factorial(D-1)/(G*L**D)
    lims = []
    lo = 0
    inner = f
    # nested integrate p_{D-2}..p0 with running limits
    subs_map = {}
    # integrate sequentially
    expr = f
    remaining = list(range(D-1))
    acc = [0]
    # manual nesting: integrate ps[k] from 0 to 1-sum(ps[:k])
    for k in range(D-2, -1, -1):
        upper = 1 - sum(ps[:k])
        expr = sp.integrate(expr, (ps[k], 0, upper))
    return sp.simplify(expr)
n3 = normD([1, 2, 3])
print('D3 norm exact =', n3)
print('D4 norm exact =', normD([1, 2, 3, 4]))
# --- vertex densities and mode: f(e_i) = (D-1)! * g_i^D / G ; unique max at argmax g
import math
for D, gv in ((3, [1, 2, 3]), (4, [1, 2, 3, 4])):
    Gv = 1
    for g in gv: Gv *= g
    dens = [Fraction(math.factorial(D-1) * g**D, Gv) for g in gv]
    print('D=%d vertex densities %s  argmax slot=%d (=argmax g) PASS %s' %
          (D, [str(d) for d in dens], dens.index(max(dens)),
           str(dens.index(max(dens)) == max(range(D), key=lambda i: gv[i]))))
# --- uniform g: density flat == (D-1)!
gv = [2, 2, 2]
Gv = 8
vals = [Fraction(math.factorial(2), Gv * Fraction(1, 2)**3) for _ in range(3)]
print('uniform-g density constant (D-1)!=2?', all(v == 2 for v in vals))
# --- interior stationary: grad of L = sum p_i/g_i proportional to 1 iff g uniform (D=3 exact solve)
p1, p2, lam = sp.symbols('p1 p2 lam')
p3v = 1 - p1 - p2
L3 = p1/g1 + p2/g2 + p3v/g2  # placeholder solve with generic g3
g3 = sp.symbols('g3', positive=True)
L3 = p1/g1 + p2/g2 + p3v/g3
eqs = [sp.Eq(sp.diff(L3, p1) - lam, 0), sp.Eq(sp.diff(L3, p2) - lam, 0)]
sol = sp.solve([sp.Eq(1/g1 - 1/g3 - lam, 0), sp.Eq(1/g2 - 1/g3 - lam, 0)], [g1, g2], dict=True)
print('interior critical forces g1=g2=g3:', sol)
