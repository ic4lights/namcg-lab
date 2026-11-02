"""052 s4 (r2): compares the algebras of relaxation (iv) with the list of Chatzistavrakidis, arXiv:1108.1107.  Exact integer arithmetic.

Checks, for the commutators printed in that paper, with the factor i dropped as a real form:
  (a) A_{4,12} is the third algebra of relaxation (iv) under X_1 -> E_2, X_2 -> E_3, X_3 -> -E_0, X_4 -> E_1;
  (b) sum_a ad_a ad_a = 0 for A_{4,12}, the paper's solution of its equation with the Euclidean sum;
  (c) for each of the two algebras of relaxation (iv): the Jacobi identity, the equation with delta, and the equation with eta
      for each of the four choices of the time generator in the printed basis;
  (d) the second algebra is aff(1) + aff(1), decomposable, under E_0 +- E_1;
  (e) unimodularity (trace of ad), which that paper uses for A_{4,12}.
Numbers only as a check of attribution.  Nothing here enters the insert."""
import itertools as it

import sympy as sp


def alg(pairs, n=4):
    c = [[[0] * n for _ in range(n)] for _ in range(n)]
    for (a, b), v in pairs.items():
        for d, x in v.items():
            c[a][b][d] += x
            c[b][a][d] -= x
    return c


def ad(c, a):
    n = len(c)
    return sp.Matrix(n, n, lambda b, d: c[a][b][d])


def jacobi(c):
    n = len(c)
    for a, b, f, d in it.product(range(n), repeat=4):
        if sum(c[a][b][e] * c[e][f][d] + c[b][f][e] * c[e][a][d] + c[f][a][e] * c[e][b][d] for e in range(n)) != 0:
            return False
    return True


def casimir_zero(c, diag):
    n = len(c)
    M = sp.zeros(n, n)
    for a in range(n):
        M += diag[a] * ad(c, a) * ad(c, a)
    return M == sp.zeros(n, n)


def report(name, c):
    n = len(c)
    print(name, ': Jacobi', jacobi(c), '; delta solves', casimir_zero(c, [1] * n))
    for t in range(n):
        print('   time generator index', t, ': eta solves', casimir_zero(c, [-1 if i == t else 1 for i in range(n)]))
    print('   trace ad_a =', [ad(c, a).trace() for a in range(n)])


# Chatzistavrakidis, printed: [X1,X3]=iX1, [X2,X3]=iX2, [X1,X4]=-iX2, [X2,X4]=iX1.  Zero-based indices 0,1,2,3 for X1,...,X4.
A412 = alg({(0, 2): {0: 1}, (1, 2): {1: 1}, (0, 3): {1: -1}, (1, 3): {0: 1}})
# Insert, third algebra: [E0,E2]=E2, [E0,E3]=E3, [E1,E2]=E3, [E1,E3]=-E2.
ThirdE = alg({(0, 2): {2: 1}, (0, 3): {3: 1}, (1, 2): {3: 1}, (1, 3): {2: -1}})
# Insert, second algebra: [E0,E2]=E2, [E0,E3]=E3, [E1,E2]=E2, [E1,E3]=-E3.
SecondE = alg({(0, 2): {2: 1}, (0, 3): {3: 1}, (1, 2): {2: 1}, (1, 3): {3: -1}})

# Map: X_{index i} = sum_k L[i][k] E_k with X1=E2, X2=E3, X3=-E0, X4=E1.
L = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, 1], [-1, 0, 0, 0], [0, 1, 0, 0]])
ok = True
for i, j in it.product(range(4), repeat=2):
    lhs = sp.zeros(1, 4)
    for k, m in it.product(range(4), repeat=2):
        for d in range(4):
            lhs[0, d] += L[i, k] * L[j, m] * ThirdE[k][m][d]
    rhs = sp.zeros(1, 4)
    for e in range(4):
        rhs += A412[i][j][e] * L[e, :]
    ok = ok and lhs == rhs
print('(a) A_{4,12} equals the third algebra under X1->E2, X2->E3, X3->-E0, X4->E1:', ok)
assert ok
report('A_{4,12}, printed basis', A412)
report('third algebra of relaxation (iv), printed basis', ThirdE)
report('second algebra of relaxation (iv), printed basis', SecondE)
assert casimir_zero(A412, [1] * 4) and casimir_zero(ThirdE, [1] * 4)
assert casimir_zero(SecondE, [-1, 1, 1, 1]) and not casimir_zero(SecondE, [1] * 4) and not casimir_zero(ThirdE, [-1, 1, 1, 1])

# (d) U=(E0+E1)/2, V=(E0-E1)/2: [U,E2]=E2, [U,E3]=0, [V,E2]=0, [V,E3]=E3, [U,V]=0.
half = sp.Rational(1, 2)
U = [half, half, 0, 0]
V = [half, -half, 0, 0]


def br(x, y, c):
    return [sum(x[a] * y[b] * c[a][b][d] for a in range(4) for b in range(4)) for d in range(4)]


E2, E3 = [0, 0, 1, 0], [0, 0, 0, 1]
print('(d) [U,E2], [U,E3], [V,E2], [V,E3], [U,V] =', br(U, E2, SecondE), br(U, E3, SecondE), br(V, E2, SecondE), br(V, E3, SecondE), br(U, V, SecondE))
assert br(U, E2, SecondE) == E2 and br(V, E3, SecondE) == E3 and br(U, E3, SecondE) == [0] * 4 and br(V, E2, SecondE) == [0] * 4 and br(U, V, SecondE) == [0] * 4
print('ALL ASSERTIONS PASSED')
