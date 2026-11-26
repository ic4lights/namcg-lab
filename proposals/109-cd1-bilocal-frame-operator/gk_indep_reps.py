#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INDEPENDENT cross-check (third path) for 109-cd1-bilocal-frame-operator.

Method: so(3,1)_C = sl2 + sl2, so irreps are spin pairs (j1,j2).  Tensor
products factorize spin-by-spin via ordinary sl2 Clebsch-Gordan.  Sym^2 V and
wedge^2 V are obtained NOT from characters but by writing the explicit 16x16
swap permutation on V(x)V (V = (1/2,1/2) = spinor of factor 1 tensor spinor
of factor 2), forming the exact projectors (I +/- S)/2 over Q, reading the
weight multiplicities of the two Cartans inside each eigenspace by exact
traces, and decomposing each weight table by greedy highest-weight
subtraction.  Hom = sum of matching-sector multiplicity products.
No import from bilocal_reps_core.py or any proposal script.
Re-run: python -I gk_indep_reps.py    (stdout <= 40 lines)
"""
from fractions import Fraction as F
import sympy as sp

HALF = F(1, 2)


def d1(j):
    return int(2 * j + 1)


def drep(r):
    return sum(m * d1(a) * d1(b) for (a, b), m in r.items())


def cg(j, k):
    out = []
    x = abs(j - k)
    while x <= j + k:
        out.append(x)
        x += 1
    return out


def tprod(r1, r2):
    out = {}
    for (a1, b1), m1 in r1.items():
        for (a2, b2), m2 in r2.items():
            for j1 in cg(a1, a2):
                for j2 in cg(b1, b2):
                    out[(j1, j2)] = out.get((j1, j2), 0) + m1 * m2
    return out


def plus(*rs):
    out = {}
    for r in rs:
        for k, m in r.items():
            out[k] = out.get(k, 0) + m
    return out


def hom(r1, r2):
    return sum(m * r2.get(k, 0) for k, m in r1.items())


# ---- explicit swap on V(x)V, V = (1/2,1/2): basis a1,b1,a2,b2 in {0,1}^4 ---
def cart(m):
    return HALF if m == 0 else -HALF


IDX = [(a1, b1, a2, b2) for a1 in (0, 1) for b1 in (0, 1)
       for a2 in (0, 1) for b2 in (0, 1)]
N = 16
S = sp.zeros(N, N)
for i, (a1, b1, a2, b2) in enumerate(IDX):
    j = IDX.index((a2, b2, a1, b1))
    S[j, i] = 1
assert S * S == sp.eye(N)
I16 = sp.eye(N)
PP = (I16 + S) * sp.Rational(1, 2)   # projector onto Sym^2 V
PM = (I16 - S) * sp.Rational(1, 2)   # projector onto wedge^2 V
assert sp.simplify(PP * PP - PP) == sp.zeros(N, N)
assert sp.simplify(PM * PM - PM) == sp.zeros(N, N)
assert sum(PP[i, i] for i in range(N)) == 10 and sum(PM[i, i] for i in range(N)) == 6
WVEC = [(cart(a1) + cart(a2), cart(b1) + cart(b2)) for (a1, b1, a2, b2) in IDX]
MS = sorted({w[0] for w in WVEC})


def weight_table(P):
    tab = {}
    for m1 in MS:
        for m2 in MS:
            tr = sum(P[i, i] for i in range(N) if WVEC[i] == (m1, m2))
            if tr:
                tab[(m1, m2)] = int(tr)
    assert sum(tab.values()) == sum(P[i, i] for i in range(N))
    return tab


def greedy(tab):
    t = dict(tab)
    content = {}
    while any(v > 0 for v in t.values()):
        j1, j2 = max((k for k, v in t.items() if v > 0),
                     key=lambda k: (k[0] + k[1], k[0]))
        content[(j1, j2)] = content.get((j1, j2), 0) + 1
        i1 = j1
        while i1 >= -j1:
            i2 = j2
            while i2 >= -j2:
                t[(i1, i2)] = t.get((i1, i2), 0) - 1
                assert t[(i1, i2)] >= 0, "negative weight multiplicity"
                i2 -= 1
            i1 -= 1
    assert all(v == 0 for v in t.values())
    return content


SymV = greedy(weight_table(PP))      # explicit swap +1 eigenspace content
LamV = greedy(weight_table(PM))      # explicit swap -1 eigenspace content

V = {(HALF, HALF): 1}
ADJ = {(1, 0): 1, (0, 1): 1}
W = tprod(V, ADJ)
W2 = tprod(V, V)
J1 = plus(ADJ, V, W)
assert greedy(weight_table(I16)) == W2   # sanity: full table = CG content

fails = []


def chk(name, got, want):
    ok = (got == want)
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": got " + str(got)
          + ", want " + str(want))


chk("(a)", (W, drep(W)),
    ({(HALF, HALF): 2, (HALF, F(3, 2)): 1, (F(3, 2), HALF): 1}, 24))
chk("(b-sym)", SymV, {(0, 0): 1, (1, 1): 1})
chk("(b-wedge)", LamV, {(1, 0): 1, (0, 1): 1})
chk("(c)", hom(W, W2), 0)
chk("(d)", hom(tprod(W, W), SymV), 22)
chk("(e)", hom(tprod(W, W), W2), 42)
chk("(f)", SymV.get((0, 0), 0), 1)
chk("(g)", plus(SymV, LamV), W2)
chk("(h)", (drep(J1), hom(J1, W2), hom(V, W2)), (34, 2, 0))

print("ALL CHECKS PASS" if not fails else "FAILS: " + ", ".join(fails))
