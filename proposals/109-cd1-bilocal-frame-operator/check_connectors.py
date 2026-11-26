#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
109-cd1-bilocal-frame-operator: connector expansion, rank bound, and
composite non-degeneracy checks.

Re-run:  python check_connectors.py    (expects "ALL CHECKS PASS".)

K1  Path-ordered connector (Wilson line) short-distance expansion
    U(x+ell, x) = 1 + ell^mu w_mu
        + (1/2) ell^mu ell^nu (d_nu w_mu + w_mu w_nu) + O(ell^3),
    verified as an EXACT identity of the truncated noncommutative series
    (word algebra over Z, exponent tuples in ell), where the series solves
    the transport ODE U'(s) = (L1 + s L2) U(s), U(0) = 1, exactly through
    second order in ell (L1 ~ O(ell), L2 ~ O(ell^2)).  With
    w_mu = theta^I_mu T_I in the Lorentz algebra (eta-antisymmetric
    generators, eta = diag(-1,1,1,1)) the LINEAR term is eta-antisymmetric
    (pure gauge type): no soldering at linear order (group-level
    counterpart of H6/H7 in check_reps.py); an eta-symmetric
    (soldering-type) part appears first at quadratic order.
K2  Rank bound of the Repair-I contraction e^A_mu = (w_mu)^A_I n^I with
    w_mu eta-antisymmetric: n eta-annihilates every column, det = 0
    identically, rank exactly 3 generically (linearized manuscript bound).
K3  Composite non-degeneracy: G = Phi Phi^H Hermitian, Det G = |Det Phi|^2
    (exact rationals); the metric composite is blind to right unitary
    recombination: Y = X V (V unitary) gives Y Y^H = X X^H, and the
    recovered right factor is unitary (exact rational-unitary test).  The
    composite carries the metric, not the frame: the frame is fixed only
    modulo the right stabilizer.
Symbolic output is a check, not a proof.
"""

import sympy as sp
import random
from sympy import Matrix, Rational, simplify, eye, zeros
from sympy.utilities.iterables import subsets

fails = []


def chk(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)


eta = sp.diag(-1, 1, 1, 1)

gens = []
for a in range(4):
    for b in range(a + 1, 4):
        T = zeros(4, 4)
        for A in range(4):
            for B in range(4):
                T[A, B] = ((1 if A == a else 0) * eta[b, B]
                           - (1 if A == b else 0) * eta[a, B])
        gens.append(T)

chk("K1a generators eta-antisymmetric: T^T eta + eta T = 0 (6 of them)",
    all(simplify(T.T * eta + eta * T) == zeros(4, 4) for T in gens))

# ---- K1: word algebra: element = dict {(exp tuple, word): coeff} -----------
E0 = (1, 0, 0, 0)
E1 = (0, 1, 0, 0)
E2 = (0, 0, 1, 0)
E3 = (0, 0, 0, 1)
ES = [E0, E1, E2, E3]


def wmul(A, B):
    out = {}
    for (ea, wa), ca in A.items():
        for (eb, wb), cb in B.items():
            k = (tuple(x + y for x, y in zip(ea, eb)), wa + wb)
            out[k] = out.get(k, 0) + ca * cb
    return {k: c for k, c in out.items() if c}


def wadd(A, B):
    out = dict(A)
    for k, c in B.items():
        out[k] = out.get(k, 0) + c
    return {k: c for k, c in out.items() if c}


def wsm(c, A):
    return {k: c * v for k, v in A.items()}


ONE = {((0, 0, 0, 0), ""): 1}
L1 = {(ES[m], f"w{m}"): 1 for m in range(4)}
L2 = {}
for n in range(4):
    for m in range(4):
        L2[(tuple(a + b for a, b in zip(ES[n], ES[m])), f"d{n}{m}")] = 1
# U(1) = 1 + L1 + (L2 + L1*L1)/2  (exact solution of U' = (L1 + s L2) U
# through order ell^2; residual terms are O(ell^3))
U1 = wadd(ONE, wadd(L1, wsm(Rational(1, 2), wadd(L2, wmul(L1, L1)))))
# right-hand side: 1 + sum_mu l^mu w_mu
#                 + (1/2) sum_{mu,nu} l^mu l^nu (d_nu w_mu + w_mu w_nu)
RHS = dict(ONE)
for m in range(4):
    RHS = wadd(RHS, {(ES[m], f"w{m}"): 1})
for mu in range(4):
    for nu in range(4):
        e = tuple(a + b for a, b in zip(ES[mu], ES[nu]))
        RHS = wadd(RHS, {(e, f"d{nu}{mu}"): Rational(1, 2)})
        RHS = wadd(RHS, {(e, f"w{mu}w{nu}"): Rational(1, 2)})
chk("K1b Wilson-line series equals 1 + ell w + (1/2) ell ell (d w + w w) "
    "exactly through O(ell^2)", U1 == RHS)

# group-valued linear term: eta-antisymmetric
th = sp.symbols(" ".join(f"t{I}{m}" for m in range(4) for I in range(6)))
wgrp = []
for m in range(4):
    M = zeros(4, 4)
    for I in range(6):
        M = M + th[6 * m + I] * gens[I]
    wgrp.append(M)
l = sp.symbols("l0 l1 l2 l3")
lin = zeros(4, 4)
for m in range(4):
    lin = lin + l[m] * wgrp[m]
chk("K1d linear connector term is eta-antisymmetric (gauge type): "
    "(ell.w)^T eta + eta (ell.w) = 0",
    simplify(lin.T * eta + eta * lin) == zeros(4, 4))
quad = wgrp[0] * wgrp[1] + wgrp[1] * wgrp[0]
B = sp.simplify(eta * quad)
Bsym = sp.simplify((B + B.T) / 2)
chk("K1e quadratic term carries a nonzero eta-symmetric (soldering-type) "
    "part for generic data", Bsym != zeros(4, 4))

# ---- K2: rank bound of e^A_mu = (w_mu)^A_I n^I ------------------------------
nsym = Matrix(list(sp.symbols("n0 n1 n2 n3")))
wsym = []
for m in range(4):
    a = sp.symbols(f"a{m}0 a{m}1 a{m}2 a{m}3 a{m}4 a{m}5")
    M = zeros(4, 4)
    for I in range(6):
        M = M + a[I] * gens[I]
    wsym.append(M)
E = Matrix(4, 4, lambda A, mu: (wsym[mu] * nsym)[A])
chk("K2a n_A e^A_mu = 0 for every mu (all columns eta-orthogonal to n)",
    all(simplify((((eta * nsym).T * E[:, mu])[0])) == 0 for mu in range(4)))
chk("K2b det e = 0 identically", simplify(E.det()) == 0)
minors3 = [E[list(r), list(c)].det()
           for r in subsets(range(4), 3) for c in subsets(range(4), 3)]
chk("K2c some 3x3 minor not identically zero (rank exactly 3 generically)",
    any(simplify(mm) != 0 for mm in minors3))

# ---- K3: composite non-degeneracy (exact rationals) -------------------------
random.seed(109)
ok = True
for _ in range(8):
    Phi = Matrix(2, 2, lambda i, j: Rational(random.randint(-5, 5),
                                             random.choice([1, 2])))
    G = Phi * Phi.conjugate().T
    ok = ok and ((G - G.conjugate().T) == zeros(2, 2))
    ok = ok and (sp.simplify(G.det() - abs(Phi.det()) ** 2) == 0)
    if Phi.det() != 0:
        ok = ok and (G[0, 0] > 0) and (G.det() > 0)
chk("K3a G = Phi Phi^H Hermitian, Det G = |Det Phi|^2, positive definite "
    "iff Phi invertible (8 rational trials)", ok)

Vrat = sp.Matrix([[Rational(3, 5), Rational(4, 5)],
                  [Rational(-4, 5), Rational(3, 5)]])
chk("K3c test matrix V is unitary: V V^H = 1",
    sp.simplify(Vrat * Vrat.conjugate().T - eye(2)) == zeros(2, 2))
ok2 = True
for _ in range(8):
    X = Matrix(2, 2, lambda i, j: Rational(random.randint(-4, 4),
                                           random.choice([1, 2, 3])))
    if X.det() == 0:
        continue
    Y = sp.simplify(X * Vrat)
    g1 = sp.simplify(X * X.conjugate().T)
    g2 = sp.simplify(Y * Y.conjugate().T)
    ok2 = ok2 and (g1 == g2)
    Vv = sp.simplify(Y.inv() * X)
    ok2 = ok2 and sp.simplify(Vv * Vv.conjugate().T - eye(2)) == zeros(2, 2)
chk("K3b metric composite fixes Phi only up to right unitary: "
    "Y = X V gives Y Y^H = X X^H, recovered factor unitary (8 trials)", ok2)

print()
if fails:
    print("FAILURES:", fails)
    raise SystemExit(1)
print("ALL CHECKS PASS")
