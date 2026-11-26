#!/usr/bin/env python3
"""s2: q=2 double-pair criterion at the quartic-coefficient level.
(A) symbolic: f = lam^4+a lam^3+b lam^2+c lam+d is a perfect square of monic p=lam^2+s0 lam+t0
    iff 8c = a(4b-a^2) and 64d = (4b-a^2)^2; then t0 = (4b-a^2)/8.
(B) block-diagonal per-copy data: the two conditions reduce to h1=h2 and n1=n2
    (077's criterion, recovered at polynomial level); exact-rational sampling.
(C) 078 example (rows (3,7),(5,11)): double root at 2, quartic (lam-2)^2(lam+14)(lam+22):
    conditions fail (double root is not a double pair).
(D) random general (H,K) q=2: double-root locus hits vs double-pair locus hits.
Deterministic seed 20261117; verdicts only.
"""
import numpy as np, sympy as sp
from fractions import Fraction as Fr
rng = np.random.default_rng(20261117)
lam, a, b, c, d = sp.symbols('a b c d lam', real=True)

# (A) perfect-square conditions
p = lam**2 + (a/2)*lam + (4*b - a**2)/8
E1 = sp.expand((p**2) - (lam**4 + a*lam**3 + b*lam**2 + c*lam + d))
# E1 with c,d substituted zero out; check the remainder basis
g = sp.gcd(sp.Poly(sp.expand(8*c - a*(4*b - a**2)), a, b, c, d),
           sp.Poly(sp.expand(64*d - (4*b - a**2)**2), a, b, c, d))
chkA = sp.expand((p**2).subs({c: a*(4*b-a**2)/8, d: (4*b-a**2)**2/64})
                 - (lam**4 + a*lam**3 + b*lam**2 + a*(4*b-a**2)/8*lam + (4*b-a**2)**2/64)) == 0
print('A perfect-square substitution identity:', chkA, '| gcd of conditions:', g.as_expr())

# (B) block-diagonal: coefficients in terms of (h1,n1),(h2,n2); factor the conditions
h1, n1, h2, n2 = sp.symbols('h1 n1 h2 n2', real=True)
A1 = 4*(h1+h2)
B1 = sp.expand(16*h1*h2 - 4*(n1+n2))
C1 = sp.expand(-16*(h1*n2 + h2*n1))
D1 = sp.expand(16*n1*n2)
E1s = sp.factor(sp.expand(8*C1 - A1*(4*B1 - A1**2)))
E2s = sp.factor(sp.expand(64*D1 - (4*B1 - A1**2)**2))
print('B block-diag condition1 factored:', E1s)
print('B block-diag condition2 factored:', E2s)

# (C) 078 example: mismatched rows (3,7),(5,11); quartic (lam-2)^2(lam+14)(lam+22)
ex = sp.factor(sp.expand((lam**2+12*lam-28)*(lam**2+20*lam-44) - (lam-2)**2*(lam+14)*(lam+22)))
exE1 = sp.expand(8*C1 - A1*(4*B1 - A1**2)).subs({h1:3,n1:7,h2:5,n2:11})
exE2 = sp.expand(64*D1 - (4*B1 - A1**2)**2).subs({h1:3,n1:7,h2:5,n2:11})
print('C 078-example quartic identity (0 means match):', ex, '| condition values (nonzero both):', exE1, exE2)

# (B') exact rational check: joint locus of the two conditions on positive rational data
# is exactly h1=h2 and n1=n2; and the key identity 4B1-A1^2 = -16((h1-h2)^2+n1+n2).
ident = sp.simplify(4*B1 - A1**2 + 16*((h1-h2)**2 + n1 + n2)) == 0
def conds(h1_, n1_, h2_, n2_):
    subs = {h1: h1_, n1: n1_, h2: h2_, n2: n2_}
    e1 = sp.expand(8*C1 - A1*(4*B1 - A1**2)).subs(subs)
    e2 = sp.expand(64*D1 - (4*B1 - A1**2)**2).subs(subs)
    return e1 == 0 and e2 == 0
rnd = [(Fr(int(rng.integers(1,60)), 10), Fr(int(rng.integers(1,90)), 10),
        Fr(int(rng.integers(1,60)), 10), Fr(int(rng.integers(1,90)), 10)) for _ in range(200)]
bad1 = 0
for x in rnd:
    on_locus = conds(*x)
    equal = (x[0] == x[2]) and (x[1] == x[3])
    if on_locus != equal: bad1 += 1
onloc = 0
for k in range(30):  # deliberate on-locus samples: h1=h2, n1=n2
    hh, nn = Fr(int(rng.integers(-40, 40)), 7), Fr(int(rng.integers(1, 80)), 4)
    if conds(hh, nn, hh, nn): onloc += 1
print("B' identity 4B1-A1^2=-16((h1-h2)^2+n1+n2):", ident,
      "| off-locus mismatches:", bad1, "on 200 random tuples; on-locus pass:", onloc, "/30")

# (D) random general (H,K) at q=2 via pencil eigenvalues: perfect-square hits expected 0
hits = 0; dblroot = 0; Ns = 2000
for _ in range(Ns):
    X = rng.standard_normal((2,2)) + 1j*rng.standard_normal((2,2))
    Hm = (X + X.conj().T)/2
    Y = rng.standard_normal((2,2)) + 1j*rng.standard_normal((2,2)); Kmat = Y @ Y.conj().T + 0.1*np.eye(2)
    C0 = (rng.standard_normal((2,2))+1j*rng.standard_normal((2,2))) + 1j*Hm
    Z0 = Kmat + C0.conj().T @ C0
    T = -2j*np.block([[C0.conj().T, Z0], [-np.eye(2), -C0]])
    ev = np.linalg.eigvals(T)
    aa, bb, cc, dd = np.poly(ev)[0:4]  # monic quartic coeffs lam^4+a lam^3+b lam^2+c lam+d
    E1v = 8*cc - aa*(4*bb - aa**2); E2v = 64*dd - (4*bb - aa**2)**2
    sc = max(1.0, abs(aa)**4, abs(bb)**2, abs(cc), abs(dd))
    if abs(E1v) < 1e-9*sc and abs(E2v) < 1e-9*sc and (4*bb - aa**2) < 0: hits += 1
print('D general q=2 samples=%d perfect-square(double-pair) hits=%d (expect 0)' % (Ns, hits))
