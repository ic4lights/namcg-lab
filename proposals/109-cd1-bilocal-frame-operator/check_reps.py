#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
109-cd1-bilocal-frame-operator: representation / summand battery.

Re-run:  python check_reps.py      (expects "ALL CHECKS PASS" as the last
line; every line prints PASS/FAIL plus the checked invariant.)

Notation (manuscript appH sec:status-C):
  V    = (1/2,1/2)  vector of SO(3,1)             (4)
  ADJ  = (1,0)+(0,1) adjoint so(3,1)              (6)
  W    = V (x) ADJ                                (24) content of d Omega
  W2   = V (x) V                                  (16) vierbein content
  SymV = Sym^2 V = (0,0)+(1,1)                    (10) soldering / metric
  LamV = wedge^2 V = (1,0)+(0,1) = ADJ            (6)  Lorentz gauge part
  J1   = ADJ + V + W                              (34) 1-jet of lock data
  CONN = W                                        (24) connector linearization
Hom_G(.,.) = intertwiner-space dimension from exact character
multiplicities of so(3,1)_C (Weyl-integral constant terms in
bilocal_reps_core.py).  Cross-checked against a brute-force
Clebsch--Gordan enumeration (independent code path).
Symbolic output is a check, not a proof.
"""

from fractions import Fraction as F
from bilocal_reps_core import (tensor, sym2, wedge2, plus, decompose,
                               hom_dim, dim, char, invariant_rank,
                               mult_of_char, chi_pair, CT, lmul, lbar,
                               WEYL2, _cg_spin)

V = {(F(1, 2), F(1, 2)): 1}
ADJ = {(1, 0): 1, (0, 1): 1}
TRIV = {(0, 0): 1}
W = tensor(V, ADJ)
W2 = tensor(V, V)
SymV = sym2(V)
LamV = wedge2(V)
J1 = plus(ADJ, V, W)
CONN = W

failures = []


def chk(name, got, want):
    ok = (got == want)
    if not ok:
        failures.append(name)
    print(("PASS " if ok else "FAIL ") + name + f": got {got}, want {want}")


def decstr(d):
    items = sorted(d.items(), key=lambda kv: (kv[0][0], kv[0][1]))
    return " + ".join(f"{m}x({a},{b})" for (a, b), m in items)


def brute_mult(p, rep):
    """Independent multiplicity of irrep p in rep via CG enumeration."""
    # first decompose rep trivially (rep is already a label sum here)
    dec = decompose(rep)
    c = 0
    for (a, b), m in dec.items():
        if (a, b) == p:
            c += m
    return c


def brute_tensor_pair_mult(p, rep1, rep2):
    """Multiplicity of p in rep1 (x) rep2 by direct CG enumeration
    (independent of the character inner product)."""
    d1, d2 = decompose(rep1), decompose(rep2)
    tot = 0
    for (a1, b1), m1 in d1.items():
        for (a2, b2), m2 in d2.items():
            la, lb = _cg_spin(a1, a2), _cg_spin(b1, b2)
            if p[0] in la and p[1] in lb:
                tot += m1 * m2
    return tot


# --- 1. recorded decompositions (appH sec:status-C) -------------------------
dW = decompose(W)
dW2 = decompose(W2)
dSym = decompose(SymV)
dLam = decompose(LamV)
print("V (x) ADJ =", decstr(dW))
print("V (x) V   =", decstr(dW2))
print("Sym^2 V   =", decstr(dSym))
print("wedge^2 V =", decstr(dLam))
chk("D1 dOmega decomposition recorded", dW,
    {(F(3, 2), F(1, 2)): 1, (F(1, 2), F(1, 2)): 2, (F(1, 2), F(3, 2)): 1})
chk("D2 vierbein decomposition recorded", dW2,
    {(0, 0): 1, (1, 0): 1, (0, 1): 1, (1, 1): 1})
chk("D3 Sym^2 V = (0,0)+(1,1)", dSym, {(0, 0): 1, (1, 1): 1})
chk("D4 wedge^2 V = adjoint", dLam, {(1, 0): 1, (0, 1): 1})
chk("D5 V(x)V = Sym^2V + wedge^2V", decompose(plus(SymV, LamV)), dW2)
chk("dim V", dim(V), 4)
chk("dim ADJ", dim(ADJ), 6)
chk("dim W = dim dOmega", dim(W), 24)
chk("dim W2", dim(W2), 16)
chk("dim SymV", dim(SymV), 10)
chk("dim J1", dim(J1), 34)

# --- 2. the recorded Repair-I obstruction, reproduced -----------------------
chk("H1 Hom(dOmega, V(x)V) = 0  [no-shared-summands]", hom_dim(W, W2), 0)
chk("H2 Hom(dOmega, Sym^2V) = 0", hom_dim(W, SymV), 0)

# --- 3. refinement: full 1-jet and the connector channel --------------------
# hom(J1, V(x)V) = 2: the two chiral adjoint summands of V(x)V; both land
# in wedge^2 V (gauge part).  The soldering target is empty.
chk("H3 Hom(J1, V(x)V) = 2 (two chiral adjoint channels, gauge only)",
    hom_dim(J1, W2), 2)
chk("H4 Hom(J1, Sym^2V) = 0  [no soldering at linear level]",
    hom_dim(J1, SymV), 0)
chk("H5 Hom(J1, wedge^2V) = 2  (= H3: all image is gauge part)",
    hom_dim(J1, LamV), 2)
chk("H6 Hom(CONN, Sym^2V) = 0  [connector adds no linear soldering]",
    hom_dim(CONN, SymV), 0)
from bilocal_reps_core import ladd
B1 = ladd(ladd({k: 2 * v for k, v in ADJ.items()},
               {k: 3 * v for k, v in V.items()}),
          {k: 5 * v for k, v in W.items()})
chk("H7 bilocalization stability: Hom(2ADJ+3V+5W, Sym^2V) = 0",
    hom_dim(B1, SymV), 0)
chk("H8 no singlet in J1", mult_of_char(char(J1), (0, 0)), 0)
chk("H9 no singlet in the connector channel",
    mult_of_char(char(CONN), (0, 0)), 0)
chk("H10 dim (Sym^2V)^G = 1 (vacuum soldering forced to c * eta)",
    hom_dim(TRIV, SymV), 1)
chk("H11 dim (wedge^2V)^G = 0", hom_dim(TRIV, LamV), 0)

# --- 4. evasion at the bilinear level (what bilocality buys) ----------------
WW = tensor(W, W)
h_ww_w2 = hom_dim(WW, W2)
h_ww_sym = hom_dim(WW, SymV)
h_ww_lam = hom_dim(WW, LamV)
h_symW_sym = hom_dim(sym2(W), SymV)
print("Hom(W(x)W, V(x)V) =", h_ww_w2, "| into Sym^2V:", h_ww_sym,
      "| into wedge^2V:", h_ww_lam)
# independent brute-force CG cross-check of the soldering count:
m00 = brute_tensor_pair_mult((0, 0), W, W)
m11 = brute_tensor_pair_mult((1, 1), W, W)
m10 = brute_tensor_pair_mult((1, 0), W, W)
m01 = brute_tensor_pair_mult((0, 1), W, W)
print("brute-force mults in W(x)W: (0,0):", m00, " (1,0):", m10,
      " (0,1):", m01, " (1,1):", m11)
chk("E1 bilinear soldering structures: Hom(W(x)W, Sym^2V) = m00+m11 = 22",
    (h_ww_sym, m00 + m11), (22, 22))
chk("E2 bilinear frame structures: Hom(W(x)W, V(x)V) = 42 (character)",
    h_ww_w2, 42)
chk("E3 brute force agrees: m00+m10+m01+m11 = 42", m00 + m10 + m01 + m11, 42)
chk("E4 coincident-quadratic soldering structures Hom(Sym^2W, Sym^2V) = 15",
    h_symW_sym, 15)
ir = invariant_rank(W)
chk("E5 invariant bilinear structures on W = 6 (number of <OO> structures)",
    ir, 6)
h_AA_sym = hom_dim(tensor(ADJ, ADJ), SymV)
chk("E6 bilinear soldering also from adjoint-pair sources: "
    "Hom(adj(x)adj, Sym^2V) = 4 (not bifundamental-specific)",
    h_AA_sym, 4)

# --- 5. Endomorphism spaces (multiplicity-freeness; normalization freedom) --
chk("U1 End(V(x)V) = 4 (four irrep summands: scale freedom per summand)",
    hom_dim(W2, W2), 4)
chk("U2 End(Sym^2V) = 2 (trace and TT rescale independently)",
    hom_dim(SymV, SymV), 2)
chk("U3 End(wedge^2V) = 2 (two chiral halves)", hom_dim(LamV, LamV), 2)
chk("U4 V(x)V is multiplicity-free",
    all(m == 1 for m in dW2.values()), True)

print()
if failures:
    print("FAILURES:", failures)
    raise SystemExit(1)
print("ALL CHECKS PASS")
