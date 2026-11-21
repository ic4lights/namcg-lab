# s3_noncentral_r.py (083) Noncentral slot-mixture law for r = s2 * sum_i g_i chi_i,
# chi_i independent 2-df noncentral chi-square (noncentrality c_i), per-slot MGF
#   (1 - s2*g_i*t)^-1 * exp(c_i * s2*g_i*t / (1 - s2*g_i*t)).
# Invariants: (1) c=0 reduces H_n = <r^n> to n! h_n(s2*g), n=1..6;
# (2) Bell/set-partition identity H_n = sum_{pi |- [n]} prod_B kappa_|B| with cumulants
#     kappa_k = d^k/dt^k log M(0) = (k-1)! s2^k sum_i g_i^k (1 + k c_i), n=1..5;
# (3) D=1 slot moments agree with Bessel-density integrals (mpmath, 25 dps), n=1..3;
# (4) same via Poisson-gamma mixture (150 terms), n=1..3;
# (5) full odd-charge map with shifts present: a0=0 still kills every odd moment; <Tr Q> = -4 a0.
# Run: python -I proposals/083-g-moments-aoddsector/s3_noncentral_r.py  (from repo root)
import sympy as sp
from sympy import factorial, binomial, Rational, diff, simplify
import mpmath
mpmath.mp.dps = 25
gv = [Rational(1,2), Rational(1,3), Rational(1,6)]
cv = [Rational(2,5), Rational(1,7), Rational(3,11)]
s2 = Rational(3,5)
t = sp.Symbol('t')
def Mfun(cs):
    M = 1
    for g, c in zip(gv, cs):
        u = s2*g*t
        M = M * (1-u)**sp.Integer(-1) * sp.exp(c*u/(1-u))
    return M
def Hseries(cs, N):
    ser = sp.series(Mfun(cs), t, 0, N+1).removeO()
    return [sp.simplify(factorial(n)*ser.coeff(t, n)) for n in range(N+1)]
def _comps(n, D):
    if D == 1: yield (n,); return
    for u in range(n+1):
        for rest in _comps(n-u, D-1): yield (u,)+rest
def hcomp(gs, n):
    return sp.simplify(sum(sp.Mul(*[g**ai for g, ai in zip(gs, al)]) for al in _comps(n, len(gs))))
f1 = 0
H0 = Hseries([0,0,0], 6)
for n in range(1, 7):
    ok = simplify(H0[n] - factorial(n)*hcomp([s2*g for g in gv], n)) == 0
    print('H_%d(c=0) == %d! h_n: %s' % (n, n, ok)); f1 += (not ok)
print('S3 invariant 1: c=0 reduction fail count =', f1)
# Part 2: cumulants + Bell/set-partition identity
def setpartitions(n):
    # standard restricted-growth enumeration of set partitions of {0..n-1}
    def rec(i, curr, best):
        if i == n: yield [list(b) for b in curr]; return
        for j in range(len(curr)+1):
            newb = (j == len(curr))
            if newb: curr.append([i])
            else: curr[j].append(i)
            yield from rec(i+1, curr, None)
            if newb: curr.pop()
            else: curr[j].pop()
    yield from rec(0, [], None)
M = Mfun(cv)
def kap(k): return simplify(diff(sp.log(M), t, k).subs(t, 0))
f2 = 0
for k in range(1, 6):
    pred = factorial(k-1)*s2**k*sum(g**k*(1+k*c) for g, c in zip(gv, cv))
    print('kappa_%d == closed form: %s' % (k, simplify(kap(k)-pred) == 0))
for n in range(1, 6):
    bell = sum(sp.Mul(*[kap(len(b)) for b in pi_]) for pi_ in setpartitions(n))
    Hn = Hseries(cv, n)[n]
    ok = simplify(bell - Hn) == 0
    print('Bell identity n=%d: %s' % (n, ok)); f2 += (not ok)
print('S3 invariant 2: Bell/partition fail count =', f2)
# Part 3/4: D=1 independent probabilistic cross-checks (single slot g=1/2, c=2/5)
gD, cD = sp.Rational(1,2), sp.Rational(2,5)
uD = s2*gD*t
Ms = (1-uD)**sp.Integer(-1)*sp.exp(cD*uD/(1-uD))
sersD = sp.series(Ms, t, 0, 4).removeO()
HD = [sp.simplify(factorial(n)*sersD.coeff(t, n)) for n in range(4)]  # true D=1 single slot
f3 = f4 = 0
for n in (1, 2, 3):
    f = lambda x: (mpmath.mpf(s2)*mpmath.mpf(gD)*x)**n * mpmath.mpf('0.5') \
        * mpmath.exp(-(x+mpmath.mpf(cD))/2) * mpmath.besseli(0, mpmath.sqrt(mpmath.mpf(cD)*x))
    val = mpmath.quad(f, [0, mpmath.inf])
    exact = mpmath.mpf(HD[n])
    print('Bessel n=%d: relerr<1e-18: %s' % (n, abs(val-exact)/abs(exact) < mpmath.mpf('1e-18')))
    f3 += not (abs(val-exact)/abs(exact) < mpmath.mpf('1e-18'))
    mix = mpmath.mpf(0)
    for k in range(151):
        w = mpmath.exp(-mpmath.mpf(cD)/2)*mpmath.mpf(cD)**k/mpmath.factorial(k)
        mix += w*(mpmath.mpf(2*s2*gD))**n*mpmath.factorial(n+k)/mpmath.factorial(k)
    print('mixture n=%d: relerr<1e-15: %s' % (n, abs(mix-exact)/abs(exact) < mpmath.mpf('1e-15')))
    f4 += not (abs(mix-exact)/abs(exact) < mpmath.mpf('1e-15'))
print('S3 invariant 3: Bessel-density fail count =', f3)
print('S3 invariant 4: Poisson-mixture fail count =', f4)
# Part 5: odd charge map with slot shifts present: a0=0 kills all odd moments; <Tr Q> = -4 a0
a0 = sp.Symbol('a0', real=True); V = sp.Symbol('V', positive=True)
def Acl(n): return sum(binomial(n, 2*q)*a0**(n-2*q)*sp.factorial2(2*q-1)*V**q for q in range(n//2+1))
def map_m(m, Am, Hm):
    return (-1)**m*2**(m+1)*sum(binomial(m, 2*k)*
        sum(binomial(k, j)*Am(m-2*k+2*j)*Hm(k-j) for j in range(k+1)) for k in range(m//2+1))
HN = Hseries(cv, 8)
Hm = lambda n: HN[n]
f5 = 0
for m in (1, 3, 5, 7):
    ok = simplify(map_m(m, lambda n: Acl(n).subs(a0, 0), Hm)) == 0
    print('shifted-slot centred odd vanish m=%d: %s' % (m, ok)); f5 += (not ok)
lin = simplify(map_m(1, Acl, Hm) + 4*a0) == 0
print('map <Tr Q> == -4 a0 exactly: %s' % lin); f5 += (not lin)
print('S3 invariant 5: shifted-slot odd-sector fail count =', f5)
print('S3 OK' if f1+f2+f3+f4+f5 == 0 else 'S3 FAIL')
