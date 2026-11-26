#!/usr/bin/env python3
"""Checks for (iii) of proposal 057: the eps -> 0 limit of reachable linear contours at N = 2.

With Im h = -c v v^T (v = e_9 here, after a real rotation) and x^a = xV^a + y_a v, xV^a in v-perp:
 1. Im S_b (N=2 form, S_b = (1/4) sum_{a<b} [h(x^a,x^a)h(x^b,x^b) - h(x^a,x^b)^2], g=1) has no term of
    degree < 2 in y (so |Im S_b| <= C R^2 |y|^2 and is bounded for |y| <= R^{-3}).
 2. The mass form sum_a x^a.h.x^a has imaginary part -c sum_a y_a^2.
 3. det G restricted to y = 0 is a nonzero polynomial (h real on v-perp of rank >= 8), degree 6.
 4. Exponent count for the lower bound: 27 radial dims -> R^26, |Pf| ~ R^24, shift ball R^-9.
 5. The su(2)-block reduction: for N=3 traceless Hermitian X built from an su(2) block, Tr[X_a,X_b][X^a,X^b]
    equals the N=2 expression (numerical check of the restriction used for N >= 3).
"""
import numpy as np
import sympy as sp

out = []


def pr(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    out.append(s)


n = 10
rng = np.random.default_rng(57002)
# random real symmetric part with eta-like inertia, invertible; Im h = -c e9 e9^T
Rr = rng.integers(-3, 4, size=(n, n))
R = sp.Matrix((Rr + Rr.T)) / 2 + sp.diag(*([-5] + [4] * 9))
c = sp.Rational(3, 2)
I9 = sp.zeros(n, n)
I9[n - 1, n - 1] = -c
h = R + sp.I * I9
xs = [[sp.Symbol(f'x{a}_{m}', real=True) for m in range(n - 1)] for a in range(3)]
ys = [sp.Symbol(f'y{a}', real=True) for a in range(3)]
X = [sp.Matrix(xs[a] + [ys[a]]) for a in range(3)]


def hb(u, w):
    return (u.T * h * w)[0, 0]


Sb = sp.Rational(1, 4) * sum(hb(X[a], X[a]) * hb(X[b], X[b]) - hb(X[a], X[b]) ** 2 for a in range(3) for b in range(a + 1, 3))
ImSb = sp.expand(sp.im(sp.expand(Sb)))
poly = sp.Poly(ImSb, *ys)
mindeg = min(sum(m) for m in poly.monoms()) if not ImSb == 0 else None
pr('1. Im S_b: minimal total degree in y =', mindeg, '(expected 2); max degree in xV =', max(sp.Poly(ImSb, *[v for row in xs for v in row]).monoms(), key=sum).__len__() and max(sum(m) for m in sp.Poly(ImSb, *[v for row in xs for v in row]).monoms()))
mass = sp.expand(sum(hb(X[a], X[a]) for a in range(3)))
pr('2. Im mass form =', sp.simplify(sp.im(mass)), '(expected', -c, '* (y0^2+y1^2+y2^2))')
G = sp.Matrix(3, 3, lambda a, b: hb(X[a], X[b]))
detG0 = sp.expand(G.det().subs({y: 0 for y in ys}))
pr('3. det G at y=0 nonzero:', detG0 != 0, ', real:', sp.im(detG0) == 0, ', total degree', sp.Poly(detG0, *[v for row in xs for v in row]).total_degree())
pr('   rank of h restricted to v-perp:', R[:n - 1, :n - 1].rank())
pr('4. R exponent: 26 (radial) + 24 (|Pf| = |det G|^4) - 9 (shift ball) =', 26 + 24 - 9, '> -1: divergent')

# 5
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
etaE = np.diag([-1.0] + [1.0] * 9)
worst = 0
for t in range(50):
    Lam = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    hn = Lam.T @ etaE @ Lam
    x = rng.normal(size=(3, n))
    # N=3 block embedding of sum_a x^a_nu sigma^a/2
    Xn = []
    for nu in range(n):
        B = sum(x[a, nu] * sig[a] / 2 for a in range(3))
        M3 = np.zeros((3, 3), complex)
        M3[:2, :2] = B
        Xn.append(M3)
    # S_b on the contour: -(1/4) h_{al ga} h_{be de} Tr [X_al, X_be][X_ga, X_de]
    C = [[Xn[a] @ Xn[b] - Xn[b] @ Xn[a] for b in range(n)] for a in range(n)]
    S = 0
    for al in range(n):
        for be in range(n):
            for ga in range(n):
                for de in range(n):
                    S += hn[al, ga] * hn[be, de] * np.trace(C[al][be] @ C[ga][de])
    S = -S / 4
    hh = lambda u, w: u @ hn @ w
    S2 = 0.25 * sum(hh(x[a], x[a]) * hh(x[b], x[b]) - hh(x[a], x[b]) ** 2 for a in range(3) for b in range(a + 1, 3))
    worst = max(worst, abs(S - S2) / max(1, abs(S2)))
pr('5. N=3 su(2)-block S_b vs N=2 formula: max relative difference', f'{worst:.2e}')

with open(__file__.replace('.py', '.txt'), 'w') as f:
    f.write('\n'.join(out) + '\n')
