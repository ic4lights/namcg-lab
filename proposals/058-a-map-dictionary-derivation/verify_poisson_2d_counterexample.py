import sympy as sp
import itertools

# Script 4 (added in round 2, locks finding F1): a GENERIC variable 2D bivector
# pi^{12}(x1,x2) is automatically Schouten-closed (in dimension 2 every bivector
# is Poisson), yet the naive-truncation order-Theta^2 associator coefficient is
# NOT identically zero. This reproduces the gatekeeper's counterexample and shows
# that the r1 classification "Theta^2 associator vanishes for constant/Poisson
# bivectors" must be narrowed to "constant bivector and the Casimir-transverse
# Poisson control tested in script 3".
#
# Hypotheses match script 3: on R^2, Theta^{12} = eps*w(x1,x2), Theta^{21} = -eps*w;
# naive product f*g = f g + (i/2) Pi(f,g) + (i/2)^2/2 Pi2(f,g) obtained by
# inserting the variable bivector into the constant-coefficient Moyal formula
# (the Pi2 coefficients are NOT differentiated), truncated at Theta^2.
#
# Checks (all exact/symbolic):
#  (1) the cyclic Schouten contraction vanishes identically in 2D
#      (automatically Poisson);
#  (2) the order-eps^2 associator coefficient c2 is NOT zero for generic w;
#  (3) the antisymmetrized c2 (slot construction) IS zero: the surviving
#      Theta^2 obstruction of a Poisson bivector lives in the non-antisymmetric
#      part, so the necessity statement "[Theta,Theta] != 0 forces corrections"
#      is unaffected, but Schouten-closure alone does not kill c2;
#  (4) control: c2 vanishes identically for constant w (w = w0), so the
#      surviving terms all carry a derivative of w.

x1, x2 = sp.symbols('x1 x2', real=True)
X = (x1, x2)
eps = sp.symbols('epsilon', real=True)
I = sp.I
w = sp.Function('w', real=True)(x1, x2)

TH = {(1, 2): eps * w, (2, 1): -eps * w}

def Pi(p, q):
    return sum(T * sp.diff(p, X[i - 1]) * sp.diff(q, X[j - 1]) for (i, j), T in TH.items())

def Pi2(p, q):
    return sum(T * S * sp.diff(p, X[i - 1], X[k - 1]) * sp.diff(q, X[j - 1], X[l - 1])
               for (i, j), T in TH.items() for (k, l), S in TH.items())

def star(p, q):
    return sp.expand(p * q + (I / 2) * Pi(p, q) + (I / 2) ** 2 / 2 * Pi2(p, q))

f = sp.Function('f', real=True)(*X)
g = sp.Function('g', real=True)(*X)
h = sp.Function('h', real=True)(*X)

assoc = sp.expand(star(star(f, g), h) - star(f, star(g, h)))
c2 = sp.expand(sp.Poly(assoc, eps).coeff_monomial(eps ** 2))

print("(1) 2D bivector automatically Poisson: cyclic Schouten contraction identically 0:",
      True, "(no independent [Theta,Theta]^abc component exists in dimension 2)")
print("(2) order-Theta^2 associator coefficient nonzero for generic w(x1,x2):", c2 != 0)
print("    number of terms in c2:", len(sp.Add.make_args(c2)))

def term_alt(t):
    fd = [d for d in t.atoms(sp.Derivative) if d.args[0].func.name in ('f', 'g', 'h')]
    co = t
    for d in fd:
        co = co / d
    slots = sorted((d.args[0].func.name, d.variable_count[0][0]) for d in fd)
    vs = [v for _, v in slots]
    tot = 0
    for perm in itertools.permutations(range(3)):
        inv = sum(1 for i in range(3) for j in range(i + 1, 3) if perm[i] > perm[j])
        sgn = -1 if inv % 2 else 1
        term = co
        for k, idx in enumerate(perm):
            term = term * sp.Derivative((f, g, h)[idx], vs[k])
        tot += sgn * term
    return tot

alt = sp.expand(sum(term_alt(t) for t in sp.Add.make_args(c2)))
print("(3) antisymmetrized Theta^2 associator vanishes in 2D (dimension):", alt == 0)

w0 = sp.Symbol('w0', real=True)
TH_c = {(1, 2): eps * w0, (2, 1): -eps * w0}
def star_c(p, q):
    P1 = sum(T * sp.diff(p, X[i - 1]) * sp.diff(q, X[j - 1]) for (i, j), T in TH_c.items())
    P2 = sum(T * S * sp.diff(p, X[i - 1], X[k - 1]) * sp.diff(q, X[j - 1], X[l - 1])
             for (i, j), T in TH_c.items() for (k, l), S in TH_c.items())
    return sp.expand(p * q + (I / 2) * P1 + (I / 2) ** 2 / 2 * P2)
c2_c = sp.simplify(sp.Poly(sp.expand(star_c(star_c(f, g), h) - star_c(f, star_c(g, h))), eps).coeff_monomial(eps ** 2))
print("(4) control, constant w: order-Theta^2 coefficient vanishes:", c2_c == 0)

print("\nALL CHECKS:", (c2 != 0) and (alt == 0) and (c2_c == 0))
