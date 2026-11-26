# s2c_oddmap.py (083) Exact averaged map. Class: a independent of r; h_n=h_n(s^2 g),
# h_0=1; A_n=E[a^n]. Map: <Tr Q^m> = (-1)^m 2^(m+1) sum_{k<=m/2} C(m,2k)
# sum_{j=0}^k C(k,j) A_{m-2k+2j} (k-j)! h_{k-j}. Supersedes dead s2b_oddmap.py (sqrt(r)
# kept inside Poly; missing positivity assumptions; variable mismatch in Part D).
# Run: python -I proposals/083-g-moments-aoddsector/s2c_oddmap.py  (from repo root)
import sympy as sp
from sympy import factorial, binomial, expand, sqrt, pi, exp, oo, symbols, integrate, Rational, powsimp
x, r, t = symbols('x r t', real=True)
I = sp.I
def trP(m):
    Q = sp.Matrix([[-4*x, -2*I*t], [2*I*t, 0]])
    p = sp.Poly(expand((Q**m)[0, 0] + (Q**m)[1, 1]), x, t)
    assert all(mt % 2 == 0 for (_, mt) in p.monoms())
    return sum(c * x**mx * r**(mt//2) for (mx, mt), c in zip(p.monoms(), p.coeffs()))
def _comps(n, D):
    if D == 1: yield (n,); return
    for u in range(n+1):
        for rest in _comps(n-u, D-1): yield (u,)+rest
def hcomp(gs, n):
    return sp.simplify(sum(sp.Mul(*[g**ai for g, ai in zip(gs, al)]) for al in _comps(n, len(gs))))
X = sp.Function('A'); Hh = sp.Function('H')
def functional(expr):
    p = sp.Poly(sp.expand(expr), x, r)
    return sum(c * X(mx) * Hh(mt) for (mx, mt), c in zip(p.monoms(), p.coeffs()))
def map_m(m, Am, Hm):
    return (-1)**m * 2**(m+1) * sum(binomial(m, 2*k) *
        sum(binomial(k, j) * Am(m-2*k+2*j) * factorial(k-j) * Hm(k-j) for j in range(k+1))
        for k in range(m//2+1))
fails = 0
for m in range(1, 9):
    ok = sp.simplify(functional(trP(m)) - map_m(m, X, Hh)) == 0
    print('map identity m=%d: %s' % (m, ok)); fails += (not ok)
print('S2c invariant 1: map-vs-direct fail count =', fails)
a0 = symbols('a0', real=True); V = symbols('V', positive=True)
def Acl(n):
    return sum(binomial(n, 2*q) * a0**(n-2*q) * sp.factorial2(2*q-1) * V**q for q in range(n//2+1))
av = symbols('av', real=True)
den = exp(-(av-a0)**2/(2*V))/sqrt(2*pi*V)
fB = 0
for n in range(0, 7):
    iv = integrate(sp.expand(av**n * den), (av, -oo, oo))
    ok = sp.simplify(Acl(n)-iv) == 0
    print('A_%d closed==integral: %s' % (n, ok)); fB += (not ok)
print('S2c invariant 2: normal-moment closed form fail count =', fB)
# Part C: centred a (a0=0) -> every odd averaged moment vanishes for any V, any r-law
fC = 0
for m in (1, 3, 5, 7):
    Ac = lambda n: Acl(n).subs(a0, 0)
    ok = sp.simplify(map_m(m, Ac, Hh)) == 0
    print('centred odd vanish m=%d: %s' % (m, ok)); fC += (not ok)
print('S2c invariant 3: centred-vanishing fail count =', fC)
# Part D: explicit double integral vs map; D=1 Exp slot, rational noncentred data
v, aa, vv = Rational(5, 11), Rational(1, 3), Rational(2, 7)
pdf_a = exp(-(av-aa)**2/(2*vv))/sqrt(2*pi*vv)
pdf_r = exp(-r/v)/v
fD = 0
for p in (1, 2):
    di = integrate(integrate(trP(2*p+1).subs(x, av)*pdf_a, (av, -oo, oo))*pdf_r, (r, 0, oo))
    Ad = lambda n: Acl(n).subs({a0: aa, V: vv})
    Hd = lambda n: factorial(n)*v**n
    ok = sp.simplify(sp.expand(di - map_m(2*p+1, Ad, Hd))) == 0
    print('explicit p=%d direct==map: %s value=%s' % (p, ok, sp.together(sp.expand(di))))
    fD += (not ok)
print('S2c invariant 4: explicit double-integral fail count =', fD)
# Part E: V=0, a0=0 even sector reduces to the 081 integrated map 2^(2p+1) p! h_p(s^2 g)
gs = [Rational(1, 2), Rational(1, 3), Rational(1, 6)]
fE = 0
for p in range(1, 5):
    Am = lambda n: (1 if n == 0 else 0)
    got = sp.simplify(map_m(2*p, Am, lambda n: factorial(n)*hcomp(gs, n)//factorial(n) if False else factorial(n)*hcomp(gs, n)/factorial(n)))
    expv = sp.simplify(2**(2*p+1)*factorial(p)*hcomp(gs, p))
    ok = sp.simplify(got - expv) == 0
    print('V=0 even p=%d ==081 map: %s' % (p, ok)); fE += (not ok)
# Part F: odd moments are odd in a0: sign flip of the p=0,1,2 closed forms
fF = 0
for p in (0, 1, 2):
    m = 2*p+1
    Am = lambda n: Acl(n)
    Hs = lambda n: factorial(n)*Rational(3, 7)**n
    P = sp.expand(map_m(m, Am, Hs))
    ok = sp.simplify(P + P.subs(a0, -a0)) == 0 and sp.simplify(P.subs(a0, 0)) == 0
    print('odd-in-a0 p=%d: %s; leading factor: %s' % (p, ok, sp.factor(P)))
    fF += (not ok)
print('S2c invariant 5: odd-in-a0 fail count =', fF)
print('S2c invariant 6: 081-reduction fail count =', fE)
print('S2c OK' if fails+fB+fC+fD+fE+fF == 0 else 'S2c FAIL')
