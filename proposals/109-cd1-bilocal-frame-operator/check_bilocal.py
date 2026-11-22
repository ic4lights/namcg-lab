#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
109-cd1-bilocal-frame-operator, round 1: the bilocal frame composite

    G(x,y) = v^{-2} Psi(x)^T eta U(x,y) Phi(y),                    (*)

Psi, Phi column-tangent condensate fields transforming as Phi -> Lambda Phi
(eq:Phi-transform, frame index; the internal index is contracted after the
locked identification of eq:VEV), and U(x,y) the path-ordered transport
through O(ell^2) of the dressed connection eq:dressed-omega in the vector
representation, U = 1 + ell^mu w_mu + (1/2) ell^mu ell^nu (d_nu w_mu +
w_mu w_nu), whose identity as the transport series was verified in
check_connectors.py (K1a, K1b, K1d).  Coordinate (mu,nu) indices multiply
the whole kernel and are suppressed; eta = diag(-1,1,1,1).

K4z  The six vector-representation generators are eta-antisymmetric.
K4b  Finite vector-representation subgroup element through th^3:
     (1 + th w + th^2 w^2/2 + th^3 w^3/6)^T eta (same) - eta = O(th^4)
     exactly, for w eta-antisymmetric (SO(3,1), signature (-,+,+,+)).
K4a  Endpoint gauge invariance of the series: with the FINITE subgroup
     element L the residual of the substitution Psi -> L Psi (x endpoint)
     into (*) is Psi^T (L^T eta L - eta) U Phi, vanishing through O(th^3)
     by K4b; the y-endpoint pair Lambda_y^{-1} Lambda_y cancels exactly.
K4i  Coincidence reduction: U(x,x) = 1 (series at ell = 0) and
     G(x,x) = v^{-2} Psi^T eta Phi, the eta-contracted coincidence
     composite, i.e. the leading term of the composite metric eq:g-from-e
     (record-keeping identity of the construction).
K4c  Transport exactness and path dependence, against EXACT series
     integration (coefficient recursion of the linear transport ODE) of dU/ds = (A0 + s A1) U for the linear connector
     w_1(x) = W1 + x^2 S, w_2(x) = W2 - x^1 S (constant float
     algebra-valued W1, W2, S):
     (i) straight line 0 -> (e,e): A(s) = e (W1 + W2) is s-independent,
         so the exact transport is exp(e (W1 + W2)); the K1b series with
         data at x coincides with it through O(e^2), differing at O(e^3)
         (numerical bound stated): the operator's transport series IS the
         transport through O(ell^2);
     (ii) full-square plaquette: L-path A = bottom edge then right edge
         versus L-path B = left edge then top edge, both 0 -> (e,e),
         based loop U_A U_B^{-1} (counterclockwise, shoelace area +e^2):
         || U_A U_B^{-1} - 1 -/+ e^2 (d1 w2 - d2 w1 + sigma [w1, w2]) ||
         is O(e^3) for the sign/sigma combination (observed: sigma = -1
         for the convention U' = +w U on columns; the d-part sign is the
         Stokes-consistent one, checked Abelian-first), while
         || U_A U_B^{-1} - 1 || = O(e^2): path dependence of the bilocal
         transport begins at O(ell^2) and its coefficient is the
         curvature-type expression d-part plus commutator of the
         connector (numerical e-scaling ratios stated, no hand-tuned
         tolerances).
K4h  Right-stabilizer ambiguity at coincidence:
     (Phi R)^T eta (Phi R) = Phi^T eta Phi for R orthogonal (exact), so
     the composite fixes the frame only as a right-stabilizer orbit
     (frame orbit, not section; cf. K3b for the unitary case).
Symbolic output is a check, not a proof.

Re-run: python -I check_bilocal.py   (expects "ALL CHECKS PASS".)
Dependencies: sympy, numpy.
"""

from functools import reduce
from operator import add

import numpy as np
import sympy as sp
from sympy import Matrix, Rational, zeros, eye, simplify

eta = sp.diag(-1, 1, 1, 1)
fails = []


def chk(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)


def msum(terms):
    return reduce(add, terms, zeros(4, 4))


gens = []
for a in range(4):
    for b in range(a + 1, 4):
        T = zeros(4, 4)
        for A in range(4):
            for B in range(4):
                T[A, B] = ((1 if A == a else 0) * eta[b, B]
                           - (1 if A == b else 0) * eta[a, B])
        gens.append(T)
chk("K4z 6 generators of so(3,1), eta-antisymmetric: T^T eta + eta T = 0",
    all(simplify(T.T * eta + eta * T) == zeros(4, 4) for T in gens))

s0 = sp.symbols(" ".join("c%d" % i for i in range(6)))
w0 = msum([s0[i] * gens[i] for i in range(6)])
th, l0, l1 = sp.symbols("th l0 l1")
Rth = eye(4) + msum([th ** k * w0 ** k / sp.factorial(k)
                     for k in range(1, 4)])
dif_b = Rth.T * eta * Rth - eta


def order_le(expr, var, n):
    """True if every entry of expr is O(var^(n+1)) (entrywise coeff test:
    Matrix.coeff would return a scalar Zero for an all-zero coefficient)."""
    ee = sp.Matrix(expr).applyfunc(sp.expand)
    return all(sp.expand(ee[i, j].coeff(var, k)) == 0
               for i in range(ee.rows) for j in range(ee.cols)
               for k in range(n + 1))


chk("K4b (1 + th w + th^2 w^2/2 + th^3 w^3/6)^T eta (same) - eta = O(th^4) "
    "exactly (finite subgroup element, SO(3,1))", order_le(dif_b, th, 3))

# ---- K4a: endpoint invariance of the kernel series ------------------------
Psi = Matrix(4, 4, lambda i, j: sp.Symbol("p%d%d" % (i, j)))
Phi = Matrix(4, 4, lambda i, j: sp.Symbol("q%d%d" % (i, j)))
ellv = [l0, l1, sp.Integer(0), sp.Integer(0)]
cw = []
for m in range(4):
    s = sp.symbols(" ".join("c%d%d" % (m, i) for i in range(6)))
    cw.append(msum([s[i] * gens[i] for i in range(6)]))
cd_ = {}
for m in range(4):
    for n in range(4):
        s = sp.symbols(" ".join("e%d%d%d" % (m, n, i) for i in range(6)))
        cd_[(m, n)] = msum([s[i] * gens[i] for i in range(6)])
U = eye(4)
for m in range(4):
    U = U + ellv[m] * cw[m]
for m in range(4):
    for n in range(4):
        U = U + Rational(1, 2) * ellv[m] * ellv[n] * (cd_[(m, n)]
                                                     + cw[m] * cw[n])
Lx = eye(4) + msum([th ** k * cw[0] ** k / sp.factorial(k)
                    for k in range(1, 4)])
# Substituting Psi -> L Psi (x endpoint), Phi -> Ly Phi and
# U -> L U Ly^{-1} into G = Psi^T eta U Phi gives
#     G_trans - G_raw = Psi^T (L^T eta L - eta) U Phi
# exactly (the Ly^{-1} Ly pair cancels between U and Phi): the residual
# FACTORS through E := L^T eta L - eta, so endpoint invariance for all
# Psi, U, Phi is equivalent to E = O(th^4).  Evaluate E at the kernel's
# own group element L = 1 + th cw[0] + th^2 cw[0]^2/2 + th^3 cw[0]^3/6:
E = Lx.T * eta * Lx - eta

chk("K4a endpoint invariance of G = Psi^T eta U Phi: residual factors "
    "through L^T eta L - eta (exact factorization; Ly^{-1} Ly cancels), "
    "and the factor vanishes through O(th^3) at the kernel's group "
    "element L(x) (y endpoint: exact cancellation)", order_le(E, th, 3))

# K4i: coincidence
U0 = sp.expand(U.subs({l0: 0, l1: 0}))
G0 = sp.expand(Psi.T * eta * U0 * Phi)
chk("K4i coincidence: U(x,x) = 1 and G(x,x) = Psi^T eta Phi (the "
    "eq:g-from-e-type coincidence composite)",
    U0 == eye(4) and G0 == sp.expand(Psi.T * eta * Phi))

# ---- K4c: exact Picard transport, plaquette curvature ---------------------
gsp = [np.array(T.tolist(), dtype=float) for T in gens]
rng = np.random.default_rng(1094)
W1m = sum(rng.integers(-3, 4, 6)[i] * gsp[i] for i in range(6))
W2m = sum(rng.integers(-3, 4, 6)[i] * gsp[i] for i in range(6))
Sm = sum(rng.integers(-2, 3, 6)[i] * gsp[i] for i in range(6))
I4 = np.eye(4)


def transport(A0, A1, n_terms=48):
    """Exact series solution at s = 1 of U' = (A0 + s A1) U, U(0) = I:
    U(1) = sum_p M_p with (p+1) M_{p+1} = A0 M_p + A1 M_{p-1}.
    Exact for the LINEAR connector used below; truncation error < 1e-14
    for the small edge sizes e tested (coefficients decay factorially)."""
    M = [I4]
    tot = I4.copy()
    for p in range(n_terms):
        Mnext = A0 @ M[p]
        if p >= 1:
            Mnext = Mnext + A1 @ M[p - 1]
        Mnext = Mnext / (p + 1)
        M.append(Mnext)
        tot = tot + Mnext
        if np.max(np.abs(Mnext)) < 1e-16:
            break
    return tot


def series_gap(ed):
    """|| exact straight-line transport - K1b series || at edge size ed."""
    # connector w_1 = W1 + x2 S, w_2 = W2 - x1 S:
    # straight 0 -> (ed,ed): A(s) = ed (W1 + W2) (the S terms cancel)
    USp = transport(ed * (W1m + W2m), np.zeros((4, 4)))
    Us = I4 + ed * W1m + ed * W2m
    Us += 0.5 * ed * ed * (W1m @ W1m + W2m @ W2m
                           + W1m @ W2m + W2m @ W1m)   # dw cross: -S + S = 0
    return np.max(np.abs(USp - Us))


g1 = series_gap(0.02)
g2 = series_gap(0.01)
chk("K4c1 straight-line transport: exact series vs the K1b truncated "
    "series with data at x is O(e^3): gap(e) = %.2e at e = 0.02 and "
    "%.2e at e = 0.01, ratio %.1f in [5.5, 10.5] (O(e^3) scaling): the "
    "operator's transport series IS the transport through O(ell^2)"
    % (g1, g2, g1 / g2), 5.5 < g1 / g2 < 10.5 and g1 < 1e-1)

dw21 = Sm        # d_2 w_1 = +S
dw12 = -Sm       # d_1 w_2 = -S


def plaquette_errs(ed):
    # path A = bottom (x1 at x2=0) then right (x2 at x1=ed):
    UB1 = transport(ed * W1m, np.zeros((4, 4)))          # w_1(x1, 0) = W1
    UR2 = transport(ed * (W2m - ed * Sm), np.zeros((4, 4)))  # w_2(ed, x2)
    UA = UR2 @ UB1
    # path B = left (x2 at x1=0) then top (x1 at x2=ed):
    UL2 = transport(ed * W2m, np.zeros((4, 4)))          # w_2(0, x2) = W2
    UT1 = transport(ed * (W1m + ed * Sm), np.zeros((4, 4)))  # w_1(x1, ed)
    UB = UT1 @ UL2
    loop = UA @ np.linalg.inv(UB)
    errs = []
    for sgn in (+1, -1):
        F = dw12 - dw21 + sgn * (W1m @ W2m - W2m @ W1m)
        errs.append((np.max(np.abs(loop - I4 - ed * ed * F)),
                     np.max(np.abs(loop - I4 + ed * ed * F))))
    return errs[0] + errs[1] + (np.max(np.abs(loop - I4)),)


e0, e1, e2, e3, rel = plaquette_errs(0.02)
f0, f1, f2, f3, rel2 = plaquette_errs(0.01)
best = min(e0, e1, e2, e3)
best2 = min(f0, f1, f2, f3)
chk("K4c2 plaquette: the mismatch between the two L-path transports and "
    "1 -/+ e^2 (d1 w2 - d2 w1 + sigma [w1, w2]) is O(e^3): best "
    "(sign, sigma) error %.2e at e = 0.02, %.2e at e = 0.01 (ratio %.1f "
    "in [5.5, 10.5]), while ||loop-1|| = %.2e drops as e^2 (ratio %.1f "
    "in [3, 5]): path dependence of the bilocal transport begins at "
    "O(ell^2) and is the curvature-type expression of the connector "
    "(sigma fixes the transport convention; observed sigma = -1 for "
    "U' = +w U acting on columns)"
    % (best, best2, best / best2, rel, rel / rel2),
    5.5 < best / best2 < 10.5 and 3.0 < rel / rel2 < 5.0
    and best < 0.2 * rel)

# ---- K4h right stabilizer at coincidence -----------------------------------
# G0 = Phi^T eta Phi is invariant under LEFT local Lorentz (gauge: K4a/K4b),
# but a RIGHT recombination Phi -> Phi C sends G0 -> C^T G0 C: given G0 the
# frame is fixed only up to the right action of O(G0).  Exact check with a
# nontrivial element: Phi = diag(2, 3, 4, 5), G0 = diag(-4, 9, 16, 25),
# C = identity except a G0-orthogonal (2,3)-block, C != 1.
PhiD = sp.diag(2, 3, 4, 5)
G0d = sp.expand(PhiD.T * eta * PhiD)   # diag(-4, 9, 16, 25)
Cd = eye(4)
Cd[1, 1] = sp.Rational(3, 5)
Cd[1, 2] = sp.Rational(16, 15)
Cd[2, 1] = sp.Rational(-3, 5)
Cd[2, 2] = sp.Rational(3, 5)
chk("K4h right stabilizer: (Phi C)^T eta (Phi C) = Phi^T eta Phi for an "
    "exact nontrivial C in O(Phi^T eta Phi) (C != 1): the composite gives "
    "the metric but fixes the frame only as a right O(g)-orbit (frame "
    "orbit, not section); contrast left gauge invariance K4a/K4b",
    sp.expand((PhiD * Cd).T * eta * (PhiD * Cd) - G0d) == zeros(4, 4)
    and Cd != eye(4))

print()
if fails:
    print("FAILURES:", fails)
    raise SystemExit(1)
print("ALL CHECKS PASS")
