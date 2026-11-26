"""
064 / s1: exact fibre algebra of the chiral block of the squared fermion operator on the joint spectrum
of (C5, C4, P), and the relative logarithm that defines Pf_rel.

Notation (as in the 062 block of Appendix H): on one chirality c^{-1} D_- D_+ = A - 2X, A = C5 - C4,
X = sigma.J_L, X^2 + X = J_L^2, 4 J_L^2 = C4 +- 2 i P.  On the principal series (k, p) of SL(2,C):
C4 = k^2 - p^2 - 1, P = +-k p, so 4 J_L^2 + 1 = z^2 with z = k + i p (one chirality) or its conjugate.

Checks:
 (1) X has the two roots x1 = (z-1)/2, x2 = -(z+1)/2 of x^2 + x - (z^2-1)/4.
 (2) spinor partial-trace weights w1 = (z+1)/z, w2 = (z-1)/z (sum 2); compact limit z = 2j+1.
 (3) eigenvalues lambda1 = A + 1 - z, lambda2 = A + 1 + z; explicit form in (c5, k, p).
 (4) large-|A| expansion of sum_i w_i log(lambda_i / A): order 1 vanishes, order 2 = (1 - z^2)/A^2,
     and the sum over the two chiralities of the order-2 coefficient is -2 C4.
 (5) zero set: lambda = 0 only at p = 0, c5 = k(k+-1) - 2, identical to the 062 kernel condition.
 (6) gap: for integer k and c5 <= -9/4, |lambda| >= 1/4; for -9/4 < c5 < -2 the bound min_k |lambda| > 0.
 (7) Casimir values from the infinitesimal character, checked against the compact formulas of 061.
 (8) compact members: zero eigenvalue only on the top so(4) component, multiplicity from the weights,
     total kernel 8 * sum (m1+m2+2)(m1-m2+1) = (4/3) n (n+4)(n^2+4n+7)  (061's count).
"""
import sympy as sp
import numpy as np

out = []
def log(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)

z, A, t = sp.symbols('z A t')
k, p, c5, nu = sp.symbols('k p c5 nu', real=True)

# (1)
x1, x2 = (z - 1) / 2, -(z + 1) / 2
for x in (x1, x2):
    assert sp.simplify(x**2 + x - (z**2 - 1) / 4) == 0
log('(1) roots of x^2 + x - (z^2-1)/4: x1 = (z-1)/2, x2 = -(z+1)/2  [exact]')

# (2) partial trace: f(X) = alpha + beta X with f(x_i) = L_i; tr_C2(alpha + beta sigma.J) = 2 alpha
L1, L2 = sp.symbols('L1 L2')
beta = (L1 - L2) / (x1 - x2)
alpha = sp.simplify(L1 - beta * x1)
w1 = sp.simplify(sp.diff(2 * alpha, L1)); w2 = sp.simplify(sp.diff(2 * alpha, L2))
assert sp.simplify(w1 - (z + 1) / z) == 0 and sp.simplify(w2 - (z - 1) / z) == 0
assert sp.simplify(w1 + w2 - 2) == 0
jj = sp.symbols('j', positive=True)
log('(2) weights w1 =', sp.factor(w1), ', w2 =', sp.factor(w2), '; w1 + w2 = 2;',
    'compact z = 2j+1:', sp.factor(w1.subs(z, 2 * jj + 1)), ',', sp.factor(w2.subs(z, 2 * jj + 1)))
# finite-dimensional check of the partial-trace formula (z = 2j+1 real), with a non-polynomial f
def spin_mats(j):
    d = int(round(2 * j + 1)); m = np.arange(j, -j - 1, -1)
    Jz = np.diag(m).astype(complex)
    Jp = np.zeros((d, d), complex)
    for i in range(1, d):
        Jp[i - 1, i] = np.sqrt(j * (j + 1) - m[i] * (m[i] + 1))
    Jx = (Jp + Jp.conj().T) / 2; Jy = (Jp - Jp.conj().T) / (2j)
    return Jx, Jy, Jz
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
for j in (0.5, 1.0, 2.5):
    J = spin_mats(j); d = J[0].shape[0]
    X = sum(np.kron(sig[i], J[i]) for i in range(3))
    a0 = 7.3 + 0.4j
    xe, V = np.linalg.eigh(X)   # X Hermitian here (z real); eigh avoids ill-conditioned degenerate eigenvectors
    F = V @ np.diag(np.log(a0 - 2 * xe)) @ V.conj().T
    ptr = F[:d, :d] + F[d:, d:]
    zz = 2 * j + 1
    pred = ((zz + 1) / zz * np.log(a0 - (zz - 1)) + (zz - 1) / zz * np.log(a0 + (zz + 1)))
    err = np.abs(ptr - pred * np.eye(d)).max()
    log(f'    partial trace of log(a - 2 sigma.J) for j = {j}: deviation from (w1 L1 + w2 L2) 1 = {err:.1e}')
    assert err < 1e-10

# (3)
lam1 = A + 1 - z; lam2 = A + 1 + z
C4 = k**2 - p**2 - 1
sub = {A: c5 - C4, z: k + sp.I * p}
l1 = sp.expand(lam1.subs(sub)); l2 = sp.expand(lam2.subs(sub))
assert sp.simplify(l1 - (c5 + 2 - k * (k + 1) + p**2 - sp.I * p)) == 0
assert sp.simplify(l2 - (c5 + 2 - k * (k - 1) + p**2 + sp.I * p)) == 0
log('(3) lambda1/c = c5 + 2 - k(k+1) + p^2 - i p ;  lambda2/c = c5 + 2 - k(k-1) + p^2 + i p   [z = k + i p]')
log('    Im lambda1 = -c p, Im lambda2 = +c p  (exact, any real c5)')

# (4) expansion in t = 1/A of G = w1 log(1 + (1 - z) t) + w2 log(1 + (1 + z) t)  (= sum w_i log(lambda_i/A))
G = w1 * sp.log(1 + (1 - z) * t) + w2 * sp.log(1 + (1 + z) * t)
ser = sp.series(G, t, 0, 6).removeO()
coeffs = [sp.factor(sp.simplify(ser.coeff(t, n))) for n in range(1, 6)]
for n, cf in enumerate(coeffs, 1):
    log(f'(4) order t^{n} coefficient:', cf)
assert coeffs[0] == 0
assert sp.simplify(coeffs[1] - (1 - z**2)) == 0
c2sum = sp.simplify(coeffs[1].subs(z, k + sp.I * p) + coeffs[1].subs(z, k - sp.I * p))
assert sp.simplify(c2sum + 2 * C4) == 0
log('    sum over the two chiralities (z, conj z) of the t^2 coefficient =', sp.factor(c2sum), '= -2 C4')

# (5) zero set and comparison with the 062 condition B = 1 + C4 - (A+1)^2 = 0, P = 0
sol1 = sp.solve([sp.re(l1), sp.im(l1)], [c5, p], dict=True)
sol2 = sp.solve([sp.re(l2), sp.im(l2)], [c5, p], dict=True)
log('(5) zeros of lambda1:', sol1, '; zeros of lambda2:', sol2)
B = (1 + C4 - (c5 - C4 + 1)**2).subs(p, 0)
for s in sol1 + sol2:
    assert sp.simplify(B.subs(c5, s[c5])) == 0
log('    both satisfy B = 1 + C4 - (A+1)^2 = 0 and P = 0 (the 062 kernel condition)')

# (6) gap
R = sp.symbols('R', real=True); tt = sp.symbols('tt', nonnegative=True)
mod2 = (R + tt)**2 + tt   # |lambda|^2 with tt = p^2, R = c5 + 2 - k(k+-1)
crit = sp.solve(sp.diff(mod2, tt), tt)[0]
log('(6) |lambda|^2 = (R + p^2)^2 + p^2, R = c5 + 2 - k(k+-1); stationary at p^2 =', crit,
    '; value there =', sp.simplify(mod2.subs(tt, crit)))
lam_sph = (p - sp.I / 2)**2 - nu**2
assert sp.simplify(sp.expand(l1.subs({c5: -sp.Rational(9, 4) - nu**2, k: 0})) - sp.expand(lam_sph)) == 0
fac = sp.expand(((p - nu)**2 + sp.Rational(1, 4)) * ((p + nu)**2 + sp.Rational(1, 4)))
assert sp.simplify(sp.expand(sp.re(lam_sph)**2 + sp.im(lam_sph)**2) - fac) == 0
log('    spherical (k = 0, c5 = -9/4 - nu^2): lambda1/c = (p - i/2)^2 - nu^2, |lambda1/c|^2 = ((p-nu)^2+1/4)((p+nu)^2+1/4) >= 1/16')
# integer k and c5 <= -9/4: R <= -1/4 (since k(k+-1) >= 0 for integers); min over p of |lambda|^2:
#   R <= -1/2: -R - 1/4 >= 1/4 ; -1/2 < R <= -1/4: R^2 >= 1/16
Rs = np.linspace(-60, -0.25, 200001)
mins = np.where(Rs <= -0.5, -Rs - 0.25, Rs**2)
log(f'    integer k, c5 <= -9/4: min over p of |lambda/c|^2 >= {mins.min():.6f} (= 1/16 at R = -1/4)')
assert mins.min() >= 1 / 16 - 1e-12
def g(c):
    Rv = c + 2.0   # worst integer k: k(k+-1) = 0
    return (-Rv - 0.25) if Rv <= -0.5 else Rv**2
log('    -9/4 < c5 < -2: gap g(c5)^(1/2) =', ', '.join(f'{np.sqrt(g(c)):.4f} at c5={c}' for c in (-2.2, -2.1, -2.01)))

# (7) Casimir from infinitesimal character: so(5) rho = (3/2, 1/2); Ind(sigma_s (x) nu): (i nu, s + 1/2)
s_, m1, m2, k1, k2 = sp.symbols('s m1 m2 k1 k2')
Om5 = sp.expand((sp.I * nu)**2 + (s_ + sp.Rational(1, 2))**2 - sp.Rational(9, 4) - sp.Rational(1, 4))
assert sp.simplify(Om5 - (s_ * (s_ + 1) - sp.Rational(9, 4) - nu**2)) == 0
comp = sp.expand(Om5.subs({s_: m2, nu: sp.I * (m1 + sp.Rational(3, 2))}))
assert sp.simplify(comp - (m1 * (m1 + 3) + m2 * (m2 + 1))) == 0
Om4 = sp.expand((sp.I * p)**2 + k**2 - 1)
comp4 = sp.expand(Om4.subs({k: k1 + 1, p: -sp.I * k2}))
assert sp.simplify(comp4 - (k1**2 + 2 * k1 + k2**2)) == 0
log('(7) C5 on the principal series (s, nu) of Spin(4,1): s(s+1) - 9/4 - nu^2; at s = m2, nu = i(m1+3/2) this is',
    'm1(m1+3) + m2(m2+1) (061); C4 on (k, p) = k^2 - p^2 - 1; at k = k1+1, p = -i k2 this is k1^2 + 2k1 + k2^2 (061)')

# (8) compact members: zero eigenvalue only on the top component, multiplicity from the weights
def C5c(a, b): return a * (a + 3) + b * (b + 1)
def C4c(a, b): return a * a + 2 * a + b * b
ok = True
for M1 in range(0, 13):
    for M2 in range(0, M1 + 1):
        for K1 in range(M2, M1 + 1):
            for K2 in range(-M2, M2 + 1):
                Aval = C5c(M1, M2) - C4c(K1, K2)
                zL = K1 + K2 + 1           # 2 j_L + 1
                for lam, mult in ((Aval + 1 - zL, zL + 1), (Aval + 1 + zL, zL - 1)):
                    if lam == 0 and mult > 0:
                        if not (K1 == M1 and K2 == M2):
                            ok = False
assert ok
log('(8) compact so(5) (m1,m2) > so(4) (k1,k2), m1 <= 12: a zero eigenvalue occurs only at (k1,k2) = (m1,m2), in lambda1')
nn = sp.symbols('n', integer=True, nonnegative=True)
for n in range(1, 21):
    tot = sum(8 * (a + b + 2) * (a - b + 1) for a in range(0, n + 1) for b in range(0, a + 1) if (a, b) != (0, 0))
    assert tot * 3 == 4 * n * (n + 4) * (n * n + 4 * n + 7)
log('    kernel on the 16 components = 8 * sum_{(m1,m2) != (0,0)} (m1+m2+2)(m1-m2+1) = (4/3) n (n+4)(n^2+4n+7) for n = 1..20;',
    'n = 1, 2: 80, 304')
log('All checks passed.')
open(__file__.replace('.py', '.out.txt'), 'w').write('\n'.join(out) + '\n')
