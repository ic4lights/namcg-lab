#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
110: right-action ambiguity of the composite, per the live text (appH,
item-109 paragraph): "the composite determines the frame only modulo the
right action of the orthogonal group of g+".  With G[E] = E^T eta E (locked
coincidence up to the radial factor), the redundancy is E -> E O with O in
the isometry group of G itself (O^T G O = G), NOT the right action of
SO(eta) on spacetime indices (checked non-invariant in check_locked_
coincidence.py, L3c).

L6a  Rational boost B (beta=3/5, gamma=5/4): B^T eta B = eta exactly.
L6b  E = diag(2,3,5,7): G = diag(-4,9,25,49); O := D^-1 B D satisfies
     O^T G O = G (conjugate isometry) and (E O)^T eta (E O) = E^T eta E:
     distinct frames E and E O share one composite.
L6c  The same O built with a WRONG centering (D' = diag with swapped
     entries) does NOT preserve G: the ambiguity is O(g+)-specific.
All entries rational -> exact arithmetic. Symbolic output is a check, not a
proof.
Re-run: python -I check_right_isometry.py   (expects ALL CHECKS PASS)
"""
import sympy as sp

eta = sp.diag(-1, 1, 1, 1)
fails = []
def ck(name, cond):
    ok = bool(cond)
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        fails.append(name)

g5, b35 = sp.Rational(5, 4), sp.Rational(3, 5)
B = sp.Matrix([[g5, sp.Rational(3, 4), 0, 0],
               [sp.Rational(3, 4), g5, 0, 0],
               [0, 0, 1, 0], [0, 0, 0, 1]])
ck("L6a rational boost: B^T eta B = eta", B.T*eta*B == eta)

D = sp.diag(2, 3, 5, 7)
G = D.T*eta*D
ck("L6b1 G = diag(-4,9,25,49)", G == sp.diag(-4, 9, 25, 49))
O = D.inv()*B*D
ck("L6b2 O^T G O = G (O in isometry group of the composite)", O.T*G*O == G)
ck("L6b3 (D O)^T eta (D O) = D^T eta D (right O(g+) ambiguity)",
   (D*O).T*eta*(D*O) == G)
ck("L6b4 the two frames differ: D O != D", D*O != D)

Dp = sp.diag(3, 2, 5, 7)
Op = Dp.inv()*B*Dp
Gp = Dp.T*eta*Dp
ck("L6c wrong centering: Op^T G Op != G (O(g+)-specific)",
   Op.T*G*Op != G)
print("O =", O.tolist())
print("FAILURES:", fails)
print("ALL CHECKS PASS" if not fails else "CHECKS FAILED")
