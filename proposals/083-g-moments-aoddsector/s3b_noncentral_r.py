# s3b_noncentral_r.py (083) Same verification as s3, with the kernel moments
# computed by the exact ODE coefficient recurrence M' = L M, L = M'/M, where
# M(t) = prod_i (1 - s2*g_i*t)^-1 exp(c_i s2 g_i t/(1 - s2 g_i t)).
# (s3 itself spent 100 s per sympy series call; superseded for speed, same math.)
# Invariants: (1) c=0 gives H_n = n! h_n(s2*g), n=1..6; (2) Bell/set-partition
# identity with cumulants kappa_k = (k-1)! s2^k sum_i g_i^k (1 + k c_i), n=1..5;
# (3) D=1 moments vs Bessel-density integrals (mpmath, 25 dps) n=1..3;
# (4) D=1 vs Poisson-gamma mixture (151 terms) n=1..3;
# (5) with shifts present, a0=0 still kills every odd charge moment, <Tr Q> = -4 a0.
# Run: python -I proposals/083-g-moments-aoddsector/s3b_noncentral_r.py  (repo root)
import sympy as sp
from sympy import factorial, binomial, Rational
import mpmath
mpmath.mp.dps = 25
gv = [Rational(1, 2), Rational(1, 3), Rational(1, 6)]
cv = [Rational(2, 5), Rational(1, 7), Rational(3, 11)]
s2 = Rational(3, 5)
def hcoeffs(pairs, N):
    # h_n = [t^n] M(t) via (n+1) h_{n+1} = sum_m l_m h_{n-m}; l_m from
    # L(t) = sum_i s2 g_i/(1-u_i) + c_i s2 g_i/(1-u_i)^2, u_i = s2 g_i t.
    L = [Rational(0)] * (N + 1)
    for g, c in pairs:
        a = s2 * g
        for m in range(N + 1):
            L[m] += a**(m + 1) * (1 + c * (m + 1))
    h = [Rational(1)] + [Rational(0)] * N
    for n in range(N):
        h[n + 1] = sum(L[m] * h[n - m] for m in range(n + 1)) / (n + 1)
    return h
def _comps(n, D):
    if D == 1: yield (n,); return
    for u in range(n + 1):
        for rest in _comps(n - u, D - 1): yield (u,) + rest
def hcomp(gs, n):
    return sum(sp.Mul(*[g**ai for g, ai in zip(gs, al)]) for al in _comps(n, len(gs)))
f1 = 0
H0 = hcoeffs([(g, Rational(0)) for g in gv], 6)
for n in range(1, 7):
    ok = sp.simplify(factorial(n) * H0[n] - factorial(n) * hcomp([s2*g for g in gv], n)) == 0
    print('H_%d(c=0) == %d! h_n: %s' % (n, n, ok)); f1 += (not ok)
print('S3b invariant 1: c=0 reduction fail count =', f1)
def setpartitions(n):
    def rec(i, curr):
        if i == n: yield [list(b) for b in curr]; return
        for j in range(len(curr) + 1):
            newb = (j == len(curr))
            if newb: curr.append([i])
            else: curr[j].append(i)
            yield from rec(i + 1, curr)
            if newb: curr.pop()
            else: curr[j].pop()
    yield from rec(0, [])
f2 = 0
kap = lambda k: factorial(k - 1) * s2**k * sum(g**k * (1 + k * c) for g, c in zip(gv, cv))
HN = hcoeffs(list(zip(gv, cv)), 5)
for n in range(1, 6):
    bell = sum(sp.Mul(*[kap(len(b)) for b in pi_]) for pi_ in setpartitions(n))
    ok = sp.simplify(bell - factorial(n) * HN[n]) == 0
    print('Bell identity n=%d: %s' % (n, ok)); f2 += (not ok)
print('S3b invariant 2: Bell/partition fail count =', f2)
# Parts 3/4: D=1 slot (g=1/2, c=2/5). Kernel (1-s2 g t)^-1 exp(c s2 g t/(1-s2 g t))
# = scaled Gamma-type slot Y with MGF (1-t')^-1 exp(c t'/(1-t')):
# density f(y)=exp(-(y+c)) I_0(2 sqrt(c y)), y in (0,oo) [chi2_2(c)/2], and
# Y is Gamma(K+1, scale 1) given K~Poisson(c). r = s2*g*Y.
gD, cD = Rational(1, 2), Rational(2, 5)
HD = hcoeffs([(gD, cD)], 3)
f3 = f4 = 0
for n in (1, 2, 3):
    f = lambda y: (mpmath.mpf('0.3')*y)**n * mpmath.exp(-(y+mpmath.mpf('0.4'))) \
        * mpmath.besseli(0, 2*mpmath.sqrt(mpmath.mpf('0.4')*y))
    val = mpmath.quad(f, [0, mpmath.inf])
    exact = mpmath.mpf(factorial(n) * HD[n])
    r3 = abs(val - exact) / abs(exact) < mpmath.mpf('1e-12')
    print('Bessel n=%d: relerr<1e-12: %s val=%s' % (n, r3, mpmath.nstr(val, 12)))
    f3 += (not r3)
    mix = mpmath.mpf(0)
    for k in range(151):
        w = mpmath.exp(-mpmath.mpf('0.4'))*mpmath.mpf('0.4')**k/mpmath.factorial(k)
        mix += w*(mpmath.mpf('0.3'))**n*mpmath.factorial(n + k)/mpmath.factorial(k)
    r4 = abs(mix - exact) / abs(exact) < mpmath.mpf('1e-15')
    print('mixture n=%d: relerr<1e-15: %s val=%s' % (n, r4, mpmath.nstr(mix, 12)))
    f4 += (not r4)
print('S3b invariant 3: Bessel-density fail count =', f3)
print('S3b invariant 4: Poisson-mixture fail count =', f4)
# Part 5: odd charge map with slot shifts present (kernel moments): a0=0 kills
# every odd moment, and <Tr Q> = -4 a0 exactly.
a0 = sp.Symbol('a0', real=True); V = sp.Symbol('V', positive=True)
def Acl(n): return sum(binomial(n, 2*q)*a0**(n-2*q)*sp.factorial2(2*q-1)*V**q for q in range(n//2+1))
def map_m(m, Am, Hm):
    return (-1)**m*2**(m+1)*sum(binomial(m, 2*k)*
        sum(binomial(k, j)*Am(m-2*k+2*j)*Hm(k-j) for j in range(k+1)) for k in range(m//2+1))
H8 = hcoeffs(list(zip(gv, cv)), 8)
Hm = lambda n: factorial(n) * H8[n]
f5 = 0
for m in (1, 3, 5, 7):
    ok = sp.simplify(map_m(m, lambda n: Acl(n).subs(a0, 0), Hm)) == 0
    print('shifted-slot centred odd vanish m=%d: %s' % (m, ok)); f5 += (not ok)
lin = sp.simplify(map_m(1, Acl, Hm) + 4*a0) == 0
print('map <Tr Q> == -4 a0 exactly: %s' % lin); f5 += (not lin)
print('S3b invariant 5: shifted-slot odd-sector fail count =', f5)
print('S3b OK' if f1+f2+f3+f4+f5 == 0 else 'S3b FAIL')
