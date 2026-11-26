#!/usr/bin/env python3
"""Exact (sympy) checks of the identities and examples quoted in the 056 insert.
 1. h = M - 2 l l^T and Re h = Re M - 2 a a^T + 2 b b^T, and h v = -M v for v = Lambda^{-1} e_0 (generic 3x3
    symbolic Lambda with eta = diag(-1,1,1); the identities are dimension independent).
 2. Mass identity (eps + i g) h = M_eff - 2 eps l l^T with M_eff = Lambda^T (eps I + i g eta) Lambda.
 3. The anisotropic example: P = diag(1,1,1/4,...), Lambda = diag(1,1,2,...) Lambda'.
 4. The gamma > 0 example: Lambda = diag(e^{i pi/8}, e^{-3 pi i/8},...): h = -e^{i pi/4} 1, Re M_eff entries.
 5. Degree of the Pfaffian: 16 (N^2-1) real Majorana-Weyl components, Pf of degree 8 (N^2-1); i^{8(N^2-1)} = 1.
"""
import sympy as sp

out = []
pr = lambda *a: (print(*a), out.append(' '.join(str(x) for x in a)))
n = 3
eta = sp.diag(-1, 1, 1)
A = sp.Matrix(n, n, lambda i, j: sp.Symbol(f'a{i}{j}', real=True))
B = sp.Matrix(n, n, lambda i, j: sp.Symbol(f'b{i}{j}', real=True))
L = A + sp.I * B
M = L.T * L
h = L.T * eta * L
l = L[0, :].T
a = A[0, :].T; b = B[0, :].T
pr("1. h - (M - 2 l l^T) = 0:", sp.simplify(sp.expand(h - (M - 2 * l * l.T))) == sp.zeros(n))
reh = h.applyfunc(lambda z: sp.re(sp.expand(z)))
rem = M.applyfunc(lambda z: sp.re(sp.expand(z)))
pr("   Re h - (Re M - 2aa^T + 2bb^T) = 0:", sp.simplify(reh - (rem - 2 * a * a.T + 2 * b * b.T)) == sp.zeros(n))
# h v = -M v with v = L^{-1} e0  <=>  h L^{-1} e0 = -M L^{-1} e0  <=>  L^T eta e0 = -L^T e0
pr("   h L^{-1} e0 + M L^{-1} e0 = L^T (eta + 1) e0 = 0:", (L.T * (eta + sp.eye(n)) * sp.Matrix([1, 0, 0])) == sp.zeros(n, 1))
eps, g = sp.symbols('epsilon g', real=True)
Meff = L.T * (eps * sp.eye(n) + sp.I * g * eta) * L
pr("2. (eps + i g) h - (M_eff - 2 eps l l^T) = 0:", sp.simplify(sp.expand((eps + sp.I * g) * h - (Meff - 2 * eps * l * l.T))) == sp.zeros(n))

n10 = 10
P = sp.diag(1, 1, sp.Rational(1, 4), *([1] * 7))
Lp = sp.eye(n10)
Lp[0, :3] = sp.Matrix([[0, 0, 1]]); Lp[1, :3] = sp.Matrix([[1, 0, 0]]); Lp[2, :3] = sp.Matrix([[sp.Rational(4, 5) * sp.I, 1, 0]])
Lam = sp.diag(1, 1, 2, *([1] * 7)) * Lp
eta10 = sp.diag(-1, *([1] * 9))
MP = (Lam.T * P * Lam).applyfunc(sp.expand)
h10 = (Lam.T * eta10 * Lam).applyfunc(sp.expand)
pr("3. Re Lambda^T P Lambda =", MP.applyfunc(sp.re).diagonal(), " offdiag real part zero:",
   all(sp.re(MP[i, j]) == 0 for i in range(n10) for j in range(n10) if i != j))
pr("   Re h =", h10.applyfunc(sp.re).diagonal(), " offdiag real part zero:",
   all(sp.re(h10[i, j]) == 0 for i in range(n10) for j in range(n10) if i != j))

Lg = sp.diag(sp.exp(sp.I * sp.pi / 8), *([sp.exp(-3 * sp.I * sp.pi / 8)] * 9))
hg = (Lg.T * eta10 * Lg).applyfunc(sp.simplify)
pr("4. h + e^{i pi/4} 1 = 0:", (hg + sp.exp(sp.I * sp.pi / 4) * sp.eye(n10)).applyfunc(lambda z: sp.simplify(sp.expand_complex(z))) == sp.zeros(n10))
Mg = (Lg.T * (eps * sp.eye(n10) + sp.I * g * eta10) * Lg).applyfunc(sp.expand)
pr("   Re M_eff[0,0] =", sp.simplify(sp.re(sp.expand_complex(Mg[0, 0]))), "; Re M_eff[1,1] =", sp.simplify(sp.re(sp.expand_complex(Mg[1, 1]))))
pr("   h_00 h_11 =", sp.simplify(hg[0, 0] * hg[1, 1]), "; h_11 h_22 =", sp.simplify(hg[1, 1] * hg[2, 2]))
Nn = sp.Symbol('N', integer=True, positive=True)
pr("5. i^(8(N^2-1)) =", sp.simplify(sp.I ** (8 * (Nn ** 2 - 1))), "; i^4 =", sp.I ** 4)
open(__file__.replace('.py', '.txt'), 'w').write('\n'.join(out) + '\n')
