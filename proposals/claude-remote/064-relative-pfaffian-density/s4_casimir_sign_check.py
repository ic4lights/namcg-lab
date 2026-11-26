"""
064 / s4: sign and normalisation of the eta-formed Casimirs on unitary (tempered) representations.

Generators on functions of R^{4,1}, eta = diag(-1,1,1,1,1): M_ab = -i (x_a d_b - x_b d_a), x_a = eta_ab x^b.
C5 = (1/2) eta^{aa'} eta^{bb'} M_ab M_a'b' (indices 0..4), C4 the same over 0..3 (the normalisation of the
Appendix H blocks: 4 on the vector of so(5), 3 on the vector of so(4)).

 (i)  on the linear function x^1 (vector): C5 = 4, C4 = 3.
 (ii) on the horospherical wave f = (x^0 + x^4)^(-lam) (a generalised eigenfunction on H^4: x.x = -1),
      C5 f = lam (lam - 3) f; for the unitary spherical principal series lam = 3/2 + i nu this is -(9/4 + nu^2),
      i.e. C5 = s(s+1) - 9/4 - nu^2 at s = 0 (the formula used in s1).
 (iii) on g = (x^0 + x^3)^(-mu), C4 g = mu (mu - 2) g; at mu = 1 + i p this is -(1 + p^2) = k^2 - p^2 - 1 at k = 0,
      the value of Eq. (297) of Martin-Dussaud used in the 062 block.
"""
import sympy as sp

out = []
def log(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)

X = sp.symbols('x0:5', real=True)
eta = [-1, 1, 1, 1, 1]
xl = [eta[a] * X[a] for a in range(5)]
def M(a, b, f):
    return -sp.I * (xl[a] * sp.diff(f, X[b]) - xl[b] * sp.diff(f, X[a]))
def Cas(f, idx):
    return sp.Rational(1, 2) * sum(eta[a] * eta[b] * M(a, b, M(a, b, f)) for a in idx for b in idx)

f = X[1]
log('(i) C5 x^1 =', sp.simplify(Cas(f, range(5))), '; C4 x^1 =', sp.simplify(Cas(f, range(4))))
assert sp.simplify(Cas(f, range(5)) - 4 * X[1]) == 0 and sp.simplify(Cas(f, range(4)) - 3 * X[1]) == 0

lam, nu, mu, p = sp.symbols('lam nu mu p')
f = (X[0] + X[4])**(-lam)
r = sp.simplify(sp.powsimp(sp.expand(Cas(f, range(5)) / f), force=True))
log('(ii) C5 f / f =', sp.factor(r))
assert sp.simplify(r - lam * (lam - 3)) == 0
log('     at lam = 3/2 + i nu:', sp.expand(r.subs(lam, sp.Rational(3, 2) + sp.I * nu)))
g = (X[0] + X[3])**(-mu)
r4 = sp.simplify(sp.powsimp(sp.expand(Cas(g, range(4)) / g), force=True))
log('(iii) C4 g / g =', sp.factor(r4), '; at mu = 1 + i p:', sp.expand(r4.subs(mu, 1 + sp.I * p)))
assert sp.simplify(r4 - mu * (mu - 2)) == 0
log('All checks passed.')
open(__file__.replace('.py', '.out.txt'), 'w').write('\n'.join(out) + '\n')
