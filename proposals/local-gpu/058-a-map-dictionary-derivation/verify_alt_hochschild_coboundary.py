import itertools
import sympy as sp

# Script 5 (round 3): Schouten closure is necessary for an associative
# Moyal-type product with leading bivector Theta, whatever order-Theta^2
# correction is added.
#
# Product: f*g = fg + B1(f,g) + B2(f,g) + O(Theta^3), with B1 = (i/2) Theta^{ab} d_a f d_b g.
# Order-Theta^2 associator:
#   A2(f,g,h) = B1(B1(f,g),h) - B1(f,B1(g,h)) - (dB2)(f,g,h),
#   (dB2)(f,g,h) = f B2(g,h) - B2(fg,h) + B2(f,gh) - B2(f,g) h.
# Alt(T)(f,g,h) := sum over the six orderings of (f,g,h), with signs, of T
# (plain signed sum, no 1/6).
#
# Checks (exact, symbolic, generic functions f,g,h):
#  (A) Alt(dB2) = 0 identically for a generic bidifferential B2 with arbitrary
#      variable coefficients: 2D up to order 3 in each slot, 3D up to order 2.
#  (B) Alt(A2) = [Theta,Theta]^{abc} d_a f d_b g d_c h exactly (factor one)
#      for a generic 3D bivector (three arbitrary component functions of x1,x2,x3),
#      [Theta,Theta]^{abc} := Theta^{ad} d_d Theta^{bc} + cyclic.
#      By (A) this holds for every B2, so no order-Theta^2 correction removes it.
#  (C) Order-Theta freedom: replacing B1 by B1 + dC (C a generic differential
#      operator up to order 2, 3D) leaves Alt of the B1 o B1 part unchanged.
#  (D) Alt of the 1/6-averaged convention equals (B)/6 (normalisation statement).

I = sp.I


def multis(n, order):
    out = [()]
    for k in range(1, order + 1):
        out += list(itertools.combinations_with_replacement(range(n), k))
    return out


def D(f, m, X):
    for a in m:
        f = sp.diff(f, X[a])
    return f


def sign(p):
    inv = sum(1 for i in range(len(p)) for j in range(i + 1, len(p)) if p[i] > p[j])
    return -1 if inv % 2 else 1


def alt(T, F):
    return sp.expand(sum(sign(p) * T(F[p[0]], F[p[1]], F[p[2]])
                         for p in itertools.permutations(range(3))))


def generic_B2(X, order, tag):
    ms = multis(len(X), order)
    coef = {}
    k = 0
    for m1 in ms:
        for m2 in ms:
            coef[(m1, m2)] = sp.Function('%s%d' % (tag, k))(*X)
            k += 1

    def B2(f, g):
        return sp.expand(sum(c * D(f, m1, X) * D(g, m2, X) for (m1, m2), c in coef.items()))
    return B2, len(coef)


def dB(B, f, g, h):
    return f * B(g, h) - B(f * g, h) + B(f, g * h) - B(f, g) * h


# ---------- (A) ----------
resA = []
for n, order in ((2, 3), (3, 2)):
    X = sp.symbols('x1:%d' % (n + 1))
    F = [sp.Function(nm)(*X) for nm in ('f', 'g', 'h')]
    B2, nc = generic_B2(X, order, 'c')
    val = alt(lambda a, b, c: dB(B2, a, b, c), F)
    ok = sp.simplify(val) == 0
    resA.append(ok)
    print("(A) dim %d, B2 up to order %d per slot (%d coefficient functions): Alt(dB2) == 0 :" % (n, order, nc), ok)

# ---------- (B) ----------
X = sp.symbols('x1:4')
F = [sp.Function(nm)(*X) for nm in ('f', 'g', 'h')]
t12, t23, t31 = [sp.Function(nm)(*X) for nm in ('t12', 't23', 't31')]
T = sp.zeros(3, 3)
T[0, 1], T[1, 2], T[2, 0] = t12, t23, t31
T[1, 0], T[2, 1], T[0, 2] = -t12, -t23, -t31


def B1(f, g, Tm=T):
    return sp.expand(I / 2 * sum(Tm[a, b] * sp.diff(f, X[a]) * sp.diff(g, X[b])
                                 for a in range(3) for b in range(3)))


def comp(B):
    return lambda f, g, h: B(B(f, g), h) - B(f, B(g, h))


def schouten(a, b, c, Tm=T):
    return sum(Tm[a, d] * sp.diff(Tm[b, c], X[d]) + Tm[b, d] * sp.diff(Tm[c, a], X[d])
               + Tm[c, d] * sp.diff(Tm[a, b], X[d]) for d in range(3))


S123 = sp.expand(schouten(0, 1, 2))
antisym = all(sp.expand(schouten(*p) - sign(p) * S123) == 0 for p in itertools.permutations(range(3)))
print("\n[Theta,Theta]^{abc} (cyclic definition) totally antisymmetric:", antisym)
target = sp.expand(sum(schouten(a, b, c) * sp.diff(F[0], X[a]) * sp.diff(F[1], X[b]) * sp.diff(F[2], X[c])
                       for a in range(3) for b in range(3) for c in range(3)))
altBB = alt(comp(B1), F)
okB = sp.simplify(altBB - target) == 0
print("(B) generic 3D bivector: Alt(B1 o B1 part) == [Theta,Theta]^{abc} d_af d_bg d_ch (factor one):", okB)
print("    [Theta,Theta]^{123} =", S123)

# naive Moyal B2 as one instance: full A2 for the naive truncation
def B2naive(f, g):
    return sp.expand((I / 2) ** 2 / 2 * sum(T[a, b] * T[c, d] * D(f, (a, c), X) * D(g, (b, d), X)
                                            for a in range(3) for b in range(3) for c in range(3) for d in range(3)))


def A2naive(f, g, h):
    return comp(B1)(f, g, h) - dB(B2naive, f, g, h)


okBn = sp.simplify(alt(A2naive, F) - target) == 0
print("    naive Moyal B2 instance: Alt(A2) == same contraction:", okBn)

# ---------- (C) ----------
ms = multis(3, 2)
cC = {m: sp.Function('k%d' % i)(*X) for i, m in enumerate(ms)}


def C(f):
    return sum(c * D(f, m, X) for m, c in cC.items())


def dC(f, g):
    return sp.expand(f * C(g) - C(f * g) + C(f) * g)


eps = sp.Symbol('eps')


def B1p(f, g):
    return sp.expand(B1(f, g) + eps * dC(f, g))


altBBp = alt(comp(B1p), F)
okC = sp.simplify(sp.expand(altBBp - altBB)) == 0
print("\n(C) B1 -> B1 + dC (generic order-2 operator C): Alt of B1 o B1 part unchanged:", okC)

# ---------- (D) ----------
okD = sp.simplify(altBB / 6 - target / 6) == 0
print("(D) 1/6-averaged alternation equals [Theta,Theta]-contraction / 6:", okD)

print("\nALL CHECKS:", all(resA) and antisym and okB and okBn and okC and okD)
