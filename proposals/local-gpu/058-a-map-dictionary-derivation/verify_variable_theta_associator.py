import sympy as sp
import itertools

# Script 3: naive variable-bivector "Moyal-type" star product and its
# associativity obstruction (the bounded obstruction recorded in the proposal).
#
# On R^3 take the antisymmetric bivector with components
#   Theta^{12} = eps * a(x3),   Theta^{23} = eps * b(x2)   (and antisymmetry),
# so each displayed component is O(Theta) and eps tracks the Theta-order.
# Define the naive product obtained by inserting the variable bivector into the
# constant-coefficient Moyal formula (no Kontsevich-type corrections; the
# coefficients of the higher terms are NOT differentiated), truncated at
# Theta^2:
#   f*g = f g + (i/2) Pi(f,g) + (i/2)^2/2 Pi2(f,g).
# Checks (all symbolic, exact):
#  (1) the cyclic Schouten bracket component [Theta,Theta]^123 / eps^2 =
#      a(x3) b'(x2) is nonzero generically (non-Poisson bivector);
#  (2) the Theta^2 coefficient c2 of the associator (f*g)*h - f*(g*h) is
#      nonzero; all its 8 terms are pure first-derivative trilinears
#      (Theta dTheta)(df dg dh): the second-derivative pieces cancel;
#  (3) the FULLY ANTISYMMETRIZED c2 equals EXACTLY (factor one)
#      ([Theta,Theta]^123/eps^2) * det(df,dg,dh), verified by coefficient
#      comparison after building the antisymmetrization slot-by-slot (no
#      chained subs): the antisymmetric part of the Theta^2 associator is
#      exactly the Gerstenhaber/Schouten obstruction;
#  (4) control cases: for a CONSTANT bivector and for the Poisson
#      single-component variable bivector Theta^{12} = eps*a(x3) (x3 a
#      Casimir, [Theta,Theta] = 0), the Theta^2 associator coefficient
#      vanishes identically (the associator starts at Theta^3, as for the
#      ordinary truncated Moyal product).
#
# Consequence recorded in the proposal: a dictionary/continuum-limit star
# calculus at a nonconstant expectation-value Theta carries an O(Theta^2)
# associativity error unless the leading bivector is Poisson (Schouten-closed)
# or explicit O(Theta^2) correction bidifferential operators are added.

x1, x2, x3 = sp.symbols('x1 x2 x3', real=True)
X = (x1, x2, x3)
eps = sp.symbols('epsilon', real=True)
I = sp.I
a = sp.Function('a', real=True)(x3)
b = sp.Function('b', real=True)(x2)

TH = {(1, 2): eps * a, (2, 1): -eps * a,
      (2, 3): eps * b, (3, 2): -eps * b}

def Pi(f, g):
    return sum(T * sp.diff(f, X[p - 1]) * sp.diff(g, X[q - 1]) for (p, q), T in TH.items())

def Pi2(f, g):
    # naive constant-form second term: coefficients NOT differentiated
    return sum(T * S * sp.diff(f, X[p - 1], X[r - 1]) * sp.diff(g, X[q - 1], X[s - 1])
               for (p, q), T in TH.items() for (r, s), S in TH.items())

def star(f, g):
    return sp.expand(f * g + (I / 2) * Pi(f, g) + (I / 2) ** 2 / 2 * Pi2(f, g))

f = sp.Function('f', real=True)(*X)
g = sp.Function('g', real=True)(*X)
h = sp.Function('h', real=True)(*X)

assoc = sp.expand(star(star(f, g), h) - star(f, star(g, h)))
P = sp.Poly(assoc, eps)
print("degrees of associator in eps:", P.monoms())
c2 = sp.expand(P.coeff_monomial(eps ** 2))
print("(2a) non-Poisson bivector: order-Theta^2 associator coefficient nonzero:", c2 != 0)

def pure_first(t):
    fd = [d for d in t.atoms(sp.Derivative) if d.args[0].func.name in ('f', 'g', 'h')]
    return (len(fd) == 3 and all(len(d.variable_count) == 1 and d.variable_count[0][0] in X for d in fd)
            and sorted(d.args[0].func.name for d in fd) == ['f', 'g', 'h'])

print("(2b) all", len(sp.Add.make_args(c2)), "terms of c2 are pure first-derivative trilinears:",
      all(pure_first(t) for t in sp.Add.make_args(c2)))

# --- (1) cyclic Schouten bracket component [Theta,Theta]^123 ---
def THget(p, q):
    return TH.get((p, q), 0)
sch123 = (
    sum(THget(1, d) * sp.diff(THget(2, 3), X[d - 1]) for d in (1, 2, 3))
    + sum(THget(2, d) * sp.diff(THget(3, 1), X[d - 1]) for d in (1, 2, 3))
    + sum(THget(3, d) * sp.diff(THget(1, 2), X[d - 1]) for d in (1, 2, 3)))
sch123 = sp.simplify(sp.expand(sch123 / eps ** 2))   # = [Theta,Theta]^123 / eps^2
print("\n(1) [Theta,Theta]^123 / eps^2 =", sp.simplify(sch123), " (nonzero generically)")

# --- (3) antisymmetrize c2 by construction (slot relabelling, no chained subs) ---
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
detd = sp.expand(sp.Matrix([[sp.diff(u, X[j]) for j in range(3)] for u in (f, g, h)]).det())
ok3 = sp.simplify(sp.expand(alt - sch123 * detd)) == 0
print("\n(3) Alt(order-Theta^2 associator) == ([Theta,Theta]^123/eps^2) * det(df,dg,dh) exactly:", ok3)

# --- (4) control cases at order Theta^2 ---
TH_c = {(1, 2): eps * sp.Symbol('A0'), (2, 1): -eps * sp.Symbol('A0'),
        (2, 3): eps * sp.Symbol('B0'), (3, 2): -eps * sp.Symbol('B0')}
def star_c(f, g):
    P1 = sum(T * sp.diff(f, X[p - 1]) * sp.diff(g, X[q - 1]) for (p, q), T in TH_c.items())
    P2 = sum(T * S * sp.diff(f, X[p - 1], X[r - 1]) * sp.diff(g, X[q - 1], X[s - 1])
             for (p, q), T in TH_c.items() for (r, s), S in TH_c.items())
    return sp.expand(f * g + (I / 2) * P1 + (I / 2) ** 2 / 2 * P2)
assoc_c = sp.expand(star_c(star_c(f, g), h) - star_c(f, star_c(g, h)))
c2_c = sp.simplify(sp.Poly(assoc_c, eps).coeff_monomial(eps ** 2))
print("\n(4a) constant bivector: order-Theta^2 associator coefficient vanishes:", c2_c == 0)

TH_1 = {(1, 2): eps * a, (2, 1): -eps * a}
def star_1(f, g):
    P1 = sum(T * sp.diff(f, X[p - 1]) * sp.diff(g, X[q - 1]) for (p, q), T in TH_1.items())
    P2 = sum(T * S * sp.diff(f, X[p - 1], X[r - 1]) * sp.diff(g, X[q - 1], X[s - 1])
             for (p, q), T in TH_1.items() for (r, s), S in TH_1.items())
    return sp.expand(f * g + (I / 2) * P1 + (I / 2) ** 2 / 2 * P2)
assoc_1 = sp.expand(star_1(star_1(f, g), h) - star_1(f, star_1(g, h)))
c2_1 = sp.simplify(sp.Poly(assoc_1, eps).coeff_monomial(eps ** 2))
print("(4b) Poisson single-component variable bivector: order-Theta^2 associator coefficient vanishes:", c2_1 == 0)

print("\nALL CHECKS:")
print("(1) Schouten [Theta,Theta]^123 nonzero for two-component bivector:", sp.simplify(sch123) != 0)
print("(2) non-Poisson Theta^2 associator nonzero and purely first-derivative:",
      c2 != 0 and all(pure_first(t) for t in sp.Add.make_args(c2)))
print("(3) Alt(Theta^2 associator) = [Theta,Theta] contraction exactly:", ok3)
print("(4) constant bivector and Poisson variable bivector: Theta^2 associator vanishes:", c2_c == 0 and c2_1 == 0)
