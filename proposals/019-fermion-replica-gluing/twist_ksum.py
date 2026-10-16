"""
R-a1: fermion replica twist, k-sum, domain, n->1.  sympy/fractions only.
Conventions: transverse plane, cone angle 2 pi n, Cartesian component phase e^{2 pi i theta}.
Heat-trace conical constant per 2-component 2D block (units: scalar real component C=1/12 at theta=0):
  scalar-like (componentwise-regular domain): C(theta) = B2({theta})/2 per component
  Dirac domain (first-order operator): one mode order flips sign -> C_D(a) = B2({a}) + |a| = a^2 + 1/6  per 2 components
"""
import sympy as sp
from fractions import Fraction as Fr

n, a = sp.symbols('n a', positive=True)
B2 = lambda x: x**2 - x + sp.Rational(1, 6)

print('--- (1) polar antiperiodic -> Cartesian phase ---')
# psi_p = exp(-i theta Sigma) psi_c ; psi_p(theta+2 pi n) = - psi_p(theta)  =>  psi_c(theta+2 pi n) = - exp(2 pi i n Sigma) psi_c
for N in range(1, 7):
    ph = [sp.simplify(-sp.exp(sp.I*sp.pi*N*s)) for s in (+1, -1)]
    print('n=%d  Cartesian phases (-e^{+-i pi n}) = %s ; (-1)^{n+1} = %d' % (N, ph, (-1)**(N+1)))

print('--- (2) k-sum sets and sum a_k^2 ---')
def aset(N, kind):
    if kind == 'anti':      # lambda^n = (-1)^{n+1}
        return [Fr(2*j - (N-1), 2*N) for j in range(N)]           # k=-(n-1)/2..(n-1)/2, a=k/n
    if kind == 'per':       # lambda^n = 1, Cartesian phase +1 for all n : a = k/n, k=0..n-1 folded to (-1/2,1/2]
        out = []
        for k in range(N):
            x = Fr(k, N)
            if x > Fr(1, 2): x -= 1
            out.append(x)
        return out
    if kind == 'graded':    # lambda^n = (-1)^n : a = 1/2 + j/n, folded to (-1/2,1/2]
        out = []
        for j in range(N):
            x = Fr(1, 2) + Fr(j, N)
            x = x - (1 if x > Fr(1, 2) else 0)
            out.append(x)
        return out
for N in range(1, 8):
    row = {}
    for kind in ('anti', 'per', 'graded'):
        A = aset(N, kind)
        row[kind] = (sum(x*x for x in A), sorted(A))
    print('n=%d  sum a^2: anti=%s per=%s graded=%s | (n^2-1)/(12 n)=%s' %
          (N, row['anti'][0], row['per'][0], row['graded'][0], Fr(N*N-1, 12*N)))
    assert row['anti'][0] == Fr(N*N-1, 12*N)
    if N % 2 == 1:  assert sorted(row['anti'][1]) == sorted(row['per'][1])
    if N % 2 == 0:  assert sorted(row['graded'][1]) == sorted(row['per'][1])
print('periodic Cartesian set == antiperiodic set for odd n:', all(sorted(aset(N,'anti'))==sorted(aset(N,'per')) for N in (1,3,5,7)))
print('periodic Cartesian set == graded set for even n:', all(sorted(aset(N,'graded'))==sorted(aset(N,'per')) for N in (2,4,6)))
print('graded n=1: a =', aset(1,'graded'), ' sum a^2 =', sum(x*x for x in aset(1,'graded')), '(!=0: not normalised at n=1)')

print('--- (3) Dirac domain: C_D(a) = a^2+1/6 (per 2 components) ---')
CD = B2(a) + a
print('C_D(a) =', sp.expand(CD))
# sum over anti set using C_D(a_k)-C_D(0)
for N in range(1, 7):
    S = sum(sp.Rational(x.numerator, x.denominator)**2 for x in aset(N,'anti'))
    print(' n=%d sum_k [C_D(a_k)-C_D(0)] = %s' % (N, S))

print('--- (4) polar zeta, n<1 branch vs k-sum ---')
th = (n+1)/2
Cc = B2(th)/(2*n)
f = sp.simplify(Cc - n*Cc.subs(n, 1))
print(' per component f(n) =', sp.factor(f), ' ; 2 f = (n^2-1)/(12 n):', sp.simplify(2*f - (n**2-1)/(12*n)) == 0)
print(' (1-n d_n) f at n=1 :', sp.simplify((f - n*sp.diff(f, n)).subs(n, 1)))
# n>1 componentwise-regular branch + restoring the flipped mode
thg = (n-1)/2
Cg = B2(thg)/(2*n); fg = Cg - n*Cg.subs(n, 1)
corr = (n-1)/(2*n)       # |nu|/n with |nu|=(n-1)/2 : order flips from +|nu| to -|nu|
print(' n>1 regular branch + sign-flipped mode == n<1 analytic form:', sp.simplify(fg + corr - f) == 0)
print(' (1-n d_n) of n>1 regular branch at 1 :', sp.simplify((fg - n*sp.diff(fg, n)).subs(n, 1)))

print('--- (5) n -> 1 derivative from the k-sum (2D Dirac = two components) ---')
F = (n**2-1)/(12*n)
print(' F(1)=', F.subs(n,1), ' F\'(1)=', sp.diff(F,n).subs(n,1), ' (1-n d_n)F|_1 =', sp.simplify((F - n*sp.diff(F,n)).subs(n,1)))
print(' per 4D Dirac (two 2D blocks), weight -1:   c_A(Dirac) = -(-1/6)*... ->',
      -2*sp.simplify((F - n*sp.diff(F,n)).subs(n,1)) , ' (units: scalar real component = 1/6)')
Fs = sp.Rational(1,6)*(1/n - n)/2   # one scalar-like component: (1/12)(1/n-n)
print(' scalar-like component (1-n d_n)[(1/12)(1/n-n)] at 1 =', sp.simplify((Fs/1 - n*sp.diff(Fs,n)).subs(n,1)))

print('--- (6) periodic scalar-like (017 branch) at integer n: B2 k-sum vs Dirac-domain k-sum ---')
for N in (3,5,7):
    A = aset(N,'anti')
    sB = sum(B2(sp.Abs(sp.Rational(x.numerator,x.denominator))) - B2(0) for x in A)
    sD = sum(sp.Rational(x.numerator,x.denominator)**2 for x in A)
    print(' n=%d  scalar-like pair sum[B2-B2(0)] = %s ; Dirac sum a^2 = %s ; ratio = %s' % (N, sB, sD, sp.simplify(sB/sD)))
print(' => same twists at odd n, different tip domain: ratio -2 per block (= -1/2 per component convention of 017)')

print('--- (7) rotated vs unrotated vector: integer-n data ---')
Cvec = lambda nn: B2(nn - sp.floor(nn))/(2*nn)           # rotated: theta=n -> {n}
Cunr = lambda nn: B2(0)/(2*nn)
for N in range(1, 6):
    print(' n=%d rotated=%s unrotated=%s' % (N, Cvec(sp.Integer(N)), Cunr(sp.Integer(N))))
nb = sp.symbols('nb')
br = B2(nb)/(2*nb)       # n<1 analytic branch of rotated vector
print(' analytic n<1 branch of rotated vector at n=2:', br.subs(nb, 2), ' unrotated:', Cunr(sp.Integer(2)), ' -> branch does not reproduce integer-n data')
