"""052 s6 (r3): exact check of the algebra behind S1 and S2 of review-r2.md.  It reads no manuscript file and enters no text.

(a) Third algebra of relaxation (iv), [E0,E2]=E2, [E0,E3]=E3, [E1,E2]=E3, [E1,E3]=-E2.  With P the projector on the (E2,E3) plane:
    ad_0^2 = P, ad_1^2 = -P, ad_2^2 = ad_3^2 = 0.
    Hence, for h = diag(h0,h1,h2,h3), the sum h_a ad_a^2 is (h0-h1) P, so it vanishes exactly when h0 = h1.
    delta solves; eta with the time index on E0 or E1 does not; eta with it on E2 or E3 does.
(b) The map of S2 with its factors of i, X1 = iE2, X2 = iE3, X3 = -iE0, X4 = iE1, on all six commutators of A_{4,12} as printed
    in arXiv:1108.1107: [X1,X3]=iX1, [X2,X3]=iX2, [X1,X4]=-iX2, [X2,X4]=iX1, all others zero.
(c) First algebra of the commutant part, for S1: E0-E3 central, J=E0+E3 null for eta with time index 0, [J,E1]=E2, [J,E2]=-E1,
    that is e(2) + R with J the rotation generator and E1, E2 the translations; Jacobi; eta solves the equation."""
import itertools as it

import sympy as sp

I = sp.I


def alg(pairs, n=4):
    c = [[[0] * n for _ in range(n)] for _ in range(n)]
    for (a, b), v in pairs.items():
        for d, x in v.items():
            c[a][b][d] += x
            c[b][a][d] -= x
    return c


def ad(c, a):
    """Matrix of ad_a: column b holds the components of [E_a,E_b]."""
    n = len(c)
    return sp.Matrix(n, n, lambda d, b: c[a][b][d])


def jacobi(c):
    n = len(c)
    return all(sum(c[a][b][e] * c[e][f][d] + c[b][f][e] * c[e][a][d] + c[f][a][e] * c[e][b][d] for e in range(n)) == 0 for a, b, f, d in it.product(range(n), repeat=4))


def br(x, y, c):
    """Bracket of complex combinations, bilinear."""
    return [sp.simplify(sum(x[a] * y[b] * c[a][b][d] for a in range(4) for b in range(4))) for d in range(4)]


Third = alg({(0, 2): {2: 1}, (0, 3): {3: 1}, (1, 2): {3: 1}, (1, 3): {2: -1}})
assert jacobi(Third)
P = sp.diag(0, 0, 1, 1)
Z = sp.zeros(4, 4)
print('(a) third algebra, Jacobi', jacobi(Third))
checks = {'ad_0^2 = P': ad(Third, 0) ** 2 == P, 'ad_1^2 = -P': ad(Third, 1) ** 2 == -P, 'ad_2^2 = 0': ad(Third, 2) ** 2 == Z, 'ad_3^2 = 0': ad(Third, 3) ** 2 == Z}
for k, v in checks.items():
    print('   ', k, v)
assert all(checks.values())
print('    ad_0 =', ad(Third, 0).tolist())
print('    ad_1 =', ad(Third, 1).tolist())
h = sp.symbols('h0:4')
S = sp.zeros(4, 4)
for a in range(4):
    S += h[a] * ad(Third, a) ** 2
S = S.applyfunc(sp.expand)
print('    sum_a h_a ad_a^2 =', S.tolist())
assert S == (h[0] - h[1]) * P
for name, d in (('delta', [1, 1, 1, 1]), ('eta, time on E0', [-1, 1, 1, 1]), ('eta, time on E1', [1, -1, 1, 1]), ('eta, time on E2', [1, 1, -1, 1]), ('eta, time on E3', [1, 1, 1, -1])):
    sol = S.subs(dict(zip(h, d))) == Z
    print('   ', name, 'solves:', sol)
    assert sol == (d[0] == d[1])

E = lambda k: [1 if i == k else 0 for i in range(4)]
X = [[I * v for v in E(2)], [I * v for v in E(3)], [-I * v for v in E(0)], [I * v for v in E(1)]]
printed = {(0, 2): (I, 0), (1, 2): (I, 1), (0, 3): (-I, 1), (1, 3): (I, 0)}
print('(b) X1=iE2, X2=iE3, X3=-iE0, X4=iE1 against A_{4,12} as printed')
for i, j in it.combinations(range(4), 2):
    lhs = br(X[i], X[j], Third)
    if (i, j) in printed:
        f, k = printed[(i, j)]
        rhs = [sp.simplify(f * v) for v in X[k]]
    else:
        rhs = [0] * 4
    print('    [X%d,X%d] =' % (i + 1, j + 1), lhs, 'expected', rhs, lhs == rhs)
    assert lhs == rhs

First = alg({(0, 1): {2: sp.Rational(1, 2)}, (3, 1): {2: sp.Rational(1, 2)}, (0, 2): {1: -sp.Rational(1, 2)}, (3, 2): {1: -sp.Rational(1, 2)}})
assert jacobi(First)
K, J = [1, 0, 0, -1], [1, 0, 0, 1]
print('(c) first algebra, Jacobi', jacobi(First))
print('    [E0-E3,E_b] =', [br(K, E(b), First) for b in range(4)])
assert all(br(K, E(b), First) == [0] * 4 for b in range(4))
print('    [J,E1], [J,E2], [J,E0-E3], [E1,E2] =', br(J, E(1), First), br(J, E(2), First), br(J, K, First), br(E(1), E(2), First))
assert br(J, E(1), First) == E(2) and br(J, E(2), First) == [0, -1, 0, 0] and br(J, K, First) == [0] * 4 and br(E(1), E(2), First) == [0] * 4
eta = sp.diag(-1, 1, 1, 1)
print('    eta(J,J) =', (sp.Matrix(J).T * eta * sp.Matrix(J))[0], '; eta(E0-E3,E0-E3) =', (sp.Matrix(K).T * eta * sp.Matrix(K))[0])
assert (sp.Matrix(J).T * eta * sp.Matrix(J))[0] == 0
S1 = sp.zeros(4, 4)
for a in range(4):
    S1 += eta[a, a] * ad(First, a) ** 2
print('    sum_a eta_aa ad_a^2 = 0:', S1 == Z)
assert S1 == Z
print('ALL ASSERTIONS PASSED')
