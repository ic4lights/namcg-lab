#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
110-cd1-bilocal-coincidence-evaluation: transport path dependence.

Convention (matches eq:bilocal-frame-expansion, appH L713-718):
  U(x, x+ell) solves dV/ds = M(s) V,  V(0)=I, along the path x -> x+ell,
  M = gamma'(s)^rho w_rho(gamma(s)); truncated straight-line series
  U = I + ell.w + (1/2) ell^rho ell^sigma (d_sigma w_rho + w_rho w_sigma).

P1  Straight-line series equals the claimed truncated series exactly
    through O(eps^2), coefficient matrices generic (noncommuting).
P2  U_Lpath - U_line = (ab/2)*( (B21 - B12) - [C1,C2] ) at order eps^2,
    where w_rho = C_rho + B_{rho mu} x^mu; i.e. loop coefficient
    (1/2) A^{rho sigma} (d_rho w_sigma - d_sigma w_rho - [w_rho,w_sigma])
    with A^{12} = ab/2 the CCW area bivector, in this convention.
    Same eps^2 coefficient for a parabolic comparison path.
P3  Commutative (single-generator) subcase: commutator part drops.
P4  so(eta)-valuedness: generators eta-antisymmetric => F^T_{12} eta +
    eta F^T_{12} = 0 at O(eps^2) coefficients.

Symbolic output is a check, not a proof.
Re-run: python -I check_path_curvature.py   (expects ALL CHECKS PASS)
"""
import sympy as sp

a, b, eps = sp.symbols('a b eps')
I3 = sp.eye(3)
fails = []

def ck(name, cond):
    ok = bool(cond)
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        fails.append(name)

def gen(name):
    return sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"{name}{i}{j}"))

C1, C2 = gen('C1'), gen('C2')
B11, B12, B21, B22 = gen('B11'), gen('B12'), gen('B21'), gen('B22')

def transport1(P0, P1_of_s, nord=4):
    """Solve V' = (eps P0 + eps^2 P1(s)) V, V(0)=I; return list [V1(1),V2(1)..].
    P0, P1 entries are s-polynomials (sympy expressions)."""
    V = [None, sp.zeros(3), sp.zeros(3), sp.zeros(3), sp.zeros(3)]
    # V_e' = P0 V_{e-1} + P1(s) V_{e-2}; integrate 0..1 keeping s-polys
    Vs = [{0: sp.eye(3)}]  # Vs[e] = dict s_pow -> Matrix (V_e(s))
    for e in range(1, nord):
        rhs = {}
        prev = Vs[e-1]
        for sp1, M1 in prev.items():
            rhs[sp1] = rhs.get(sp1, sp.zeros(3)) + P0 * M1
        if e-2 >= 0:
            for sp1, M1 in Vs[e-2].items():
                for sp2, M2 in P1_of_s.items():
                    rhs[sp1+sp2] = rhs.get(sp1+sp2, sp.zeros(3)) + M2 * M1
        Ve_s = {}
        Ve1 = sp.zeros(3)
        for s, M in rhs.items():
            Ve_s[s+1] = M / sp.Integer(s+1)
            Ve1 = Ve1 + M / sp.Integer(s+1)
        Vs.append(Ve_s)
        V[e] = Ve1
    return V

def series_product(A, B, nord=4):
    out = [None, sp.zeros(3), sp.zeros(3), sp.zeros(3), sp.zeros(3)]
    for i in range(1, nord):
        for j in range(1, nord):
            if i + j < nord:
                out[i+j] = out[i+j] + A[i] * B[j]
    return out

def ser(A):  # I + sum
    tot = sp.eye(3)
    for e in range(1, 4):
        tot = tot + eps**e * A[e]
    return tot

# --- straight line: M = eps M0 + eps^2 s M1
M0 = a * C1 + b * C2
M1 = (a*a) * B11 + a*b * (B12 + B21) + b*b * B22
Vs = transport1(M0, {1: M1})
U_line = sp.eye(3) + eps*Vs[1] + eps**2*Vs[2] + eps**3*Vs[3]

# P1: matches eq:bilocal-frame-expansion
tgt2 = sp.Rational(1,2) * (M1 + M0*M0)
tgt1 = M0
ck("P1 linear term = ell.w", sp.simplify(Vs[1] - tgt1) == sp.zeros(3))
ck("P1 quadratic term = 1/2(d_sigma w_rho + w_rho w_sigma) sym-contracted",
   sp.simplify(Vs[2] - tgt2) == sp.zeros(3))
