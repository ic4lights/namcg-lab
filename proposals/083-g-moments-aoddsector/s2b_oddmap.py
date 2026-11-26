# s2b_oddmap.py (083) Exact averaged map. Class: a independent of r; h_n=h_n(s^2 g),
# h_0=1; A_n=E[a^n]. Map: <Tr Q^m> = (-1)^m 2^(m+1) sum_{k<=m/2} C(m,2k)
# sum_{j=0}^k C(k,j) A_{m-2k+2j} (k-j)! h_{k-j}.  Supersedes dead stub s2_oddmap.py.
# Run: python -I proposals/083-g-moments-aoddsector/s2b_oddmap.py  (from repo root)
import sympy as sp
from sympy import factorial, binomial, expand, sqrt, pi, exp, oo, symbols, integrate, Rational
a, r = symbols('a r', real=True)
I = sp.I
def trP(m):
    Q = sp.Matrix([[-4*a, -2*I*sqrt(r)], [2*I*sqrt(r), 0]])
    return expand((Q**m)[0, 0] + (Q**m)[1, 1])
def _comps(n, D):
    if D == 1: yield (n,); return
    for x in range(n+1):
        for rest in _comps(n-x, D-1): yield (x,)+rest
def hcomp(gs, n):
    return sp.simplify(sum(sp.Mul(*[g**ai for g, ai in zip(gs, al)]) for al in _comps(n, len(gs))))
A = sp.Function('A'); H = sp.Function('H')
def functional(expr):
    p = sp.Poly(sp.expand(expr), a, r)
    return sum(c * A(ma) * H(mt) for (ma, mt), c in zip(p.monoms(), p.coeffs()))
def map_m(m, Am, Hm):
    return (-1)**m * 2**(m+1) * sum(binomial(m, 2*k) *
        sum(binomial(k, j) * Am(m-2*k+2*j) * factorial(k-j) * Hm(k-j) for j in range(k+1))
        for k in range(m//2+1))
fails = []
for m in range(1, 9):
    ok = sp.simplify(functional(trP(m)) - map_m(m, A, H)) == 0
    print('map identity m=%d: %s' % (m, ok)); fails.append(not ok)
print('S2b invariant 1: map-vs-direct fail count =', sum(fails))
# Part B: noncentred normal moments A_n(a0,V) closed form vs exact Gaussian integrals
a0, V = symbols('a0 V', real=True)
def Acl(n):
    return sum(binomial(n, 2*q) * a0**(n-2*q) * sp.factorial2(2*q-1) * V**q for q in range(n//2+1))
av = symbols('av', real=True)
den = exp(-sp.Rational(1, 2)*(av-a0)**2/V)/sqrt(2*pi*V)
for n in range(0, 7):
    iv = integrate(sp.expand(av**n * den), (av, -oo, oo))
    print('A_%d closed==integral: %s' % (n, sp.simplify(Acl(n)-iv) == 0))
# Part C: centred a (a0=0) -> all odd averaged moments vanish for every V, every r-law
fC = 0
for m in (1, 3, 5, 7):
    Ac = lambda n, _m=m: Acl(n).subs(a0, 0)
    val = sp.simplify(map_m(m, Ac, lambda n: H(n)))
    ok = val == 0
    print('centred odd vanish m=%d: %s' % (m, ok)); fC += (not ok)
print('S2b invariant 2: centred-vanishing fail count =', fC)
# Part D: fully explicit double integral vs map, p=1,2; D=1 Exp slot, rational data
v, aa, vv = Rational(5, 11), sp.Rational(1, 3), sp.Rational(2, 7)
pdf_a = exp(-(av-aa)**2/(2*vv))/sqrt(2*pi*vv)
pdf_r = exp(-r/v)/v
fD = 0
for p in (1, 2):
    di = integrate(integrate(trP(2*p+1)*pdf_a, (av, -oo, oo))*pdf_r, (r, 0, oo))
    Ad = lambda n: Acl(n).subs({a0: aa, V: vv})
    Hd = lambda n: factorial(n)*v**n
    print('explicit p=%d direct==map: %s value=%s' % (p, sp.simplify(sp.expand(di - map_m(2*p+1, Ad, Hd))) == 0, sp.nsimplify(sp.together(sp.expand(di)))))
    fD += 0 if sp.simplify(sp.expand(di - map_m(2*p+1, Ad, Hd))) == 0 else 1
print('S2b invariant 3: explicit double-integral fail count =', fD)
# Part E: V=0, a0=0 even sector reduces to the 081 integrated map 2^(2p+1) p! h_p(s^2 g)
gs = [Rational(1, 2), Rational(1, 3), Rational(1, 6)]
fE = 0
for p in range(1, 5):
    Am = lambda n: (1 if n == 0 else 0)
    got = sp.simplify(map_m(2*p, Am, lambda n: factorial(n)*hcomp(gs, n)/factorial(n)))
    exp_ = sp.simplify(2**(2*p+1)*factorial(p)*hcomp(gs, p))
    ok = sp.simplify(got - exp_) == 0
    print('V=0 even p=%d ==081 map: %s' % (p, ok)); fE += (not ok)
print('S2b invariant 4: 081-reduction fail count =', fE)
print('S2b OK' if fC+fD+fE == 0 and sum(fails) == 0 else 'S2b FAIL')
