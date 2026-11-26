#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
109-cd1-bilocal-frame-operator: representation-theory core.

Exact characters of irreps (jL, jR) of so(3,1)_C = sl(2,C) + sl(2,C),
as Laurent polynomials in (z, w) over Z (dicts {(i, j): coeff}), with
chi_j(t) = sum_{m=-j..j} t^m on the spin lattice (half-integer powers
for half-integer j; z, w are the half-angle torus variables).

Multiplicity inner product = exact constant term against the Weyl
factor (2 - z^2 - z^-2)(2 - w^2 - w^-2), i.e. the normalized Haar
integral sin^2(theta/2) dtheta / pi for each SU(2) factor; verified
against orthonormality of the irreducible characters in selftest() and
in check_reps.py (C0).  This computes the complexified (jL, jR)
summand content that appears in the manuscript decomposition
paragraphs (appH sec:status-C).  Symbolic output is a check, not a
proof.

Sym^2 / wedge^2 use the Frobenius identities at the character level,
chi_{Sym^2 X}(g) = (chi_X(g)^2 + chi_X(g^2)) / 2 and the wedge
analogue, where chi_X(g^2) is the exact Adams operation (exponent
doubling of the Laurent polynomial; a virtual character in general).

Reference decompositions pinned to the manuscript (appH sec:status-C):
  V x so(3,1) = (3/2,1/2) + 2 x (1/2,1/2) + (1/2,3/2)
  V x V       = (0,0) + (1,0) + (0,1) + (1,1)
"""

from fractions import Fraction as F

# ---------- exact Laurent polynomials in (z, w) ----------


def lmul(f, g):
    out = {}
    for (i, j), a in f.items():
        for (k, l), b in g.items():
            e = (i + k, j + l)
            out[e] = out.get(e, 0) + a * b
    return {e: c for e, c in out.items() if c}


def ladd(f, g):
    out = dict(f)
    for e, c in g.items():
        out[e] = out.get(e, 0) + c
    return {e: c for e, c in out.items() if c}


def lbar(f):
    """z -> 1/z, w -> 1/w (character of the dual / conjugate)."""
    return {(-i, -j): c for (i, j), c in f.items()}


def lscale2(f):
    """z -> z^2, w -> w^2: the Adams operation chi(g) -> chi(g^2)."""
    return {(2 * i, 2 * j): c for (i, j), c in f.items()}


def CT(f):
    return f.get((0, 0), 0)


def ldim(f):
    return sum(f.values())


F1 = {(0, 0): 2, (1, 0): -1, (-1, 0): -1}
F2 = {(0, 0): 2, (0, 1): -1, (0, -1): -1}
WEYL2 = lmul(F1, F2)

# ---------- characters and multiplicities ----------


def chi_spin(j, which):
    """Character of spin j in variable 'z' or 'w' (half-angle lattice)."""
    idx = 0 if which == "z" else 1
    e = 2 * j
    if e < 0:
        raise ValueError("j must be >= 0")
    out = {}
    for k in range(int(e) + 1):
        expo = F(k) - j
        key = [F(0), F(0)]
        key[idx] = expo
        out[(key[0], key[1])] = 1
    return out


def chi_pair(p):
    return lmul(chi_spin(p[0], "z"), chi_spin(p[1], "w"))


def char(frep):
    """Character (Laurent dict) of a formal sum frep = {(jL,jR): mult}."""
    out = {}
    for p, m in frep.items():
        out = ladd(out, {e: c * m for e, c in chi_pair(p).items()})
    return out


def pair(f, g):
    """Normalized inner product on the spin lattice (Haar average of the
    class functions); exact integral constant term divided by 4."""
    t = CT(lmul(f, lmul(lbar(g), WEYL2)))
    assert t % 4 == 0, "pairing not integral"
    return t // 4


def mult_of_char(c, p):
    return pair(c, chi_pair(p))


def _halves(hi):
    return [F(k, 2) for k in range(0, int(2 * hi) + 1)]


def decompose_char(c):
    """Decompose an actual character into irreps; assert residual zero."""
    if not c:
        return {}
    zmax = max(abs(i) for (i, _) in c)
    wmax = max(abs(j) for (_, j) in c)
    out = {}
    for jL in _halves(zmax):
        for jR in _halves(wmax):
            m = mult_of_char(c, (jL, jR))
            if m > 0:
                out[(jL, jR)] = m
    resid = dict(c)
    for p, m in out.items():
        resid = ladd(resid, {e: -m * v for e, v in chi_pair(p).items()})
    assert not resid, "character residual nonzero: decomposition failed"
    return out


def decompose(frep):
    return decompose_char(char(frep))


def dim(frep):
    # dim (jL, jR) = (2jL+1)(2jR+1)
    return sum(m * (2 * p[0] + 1) * (2 * p[1] + 1) for p, m in frep.items())


def dim_of_char(c):
    return sum(c.values())


def _cg_spin(j1, j2):
    # j runs from |j1-j2| to j1+j2 in steps of 1 (unitary su(2) CG),
    # i.e. 2j runs by steps of 2.
    e1, e2 = 2 * j1, 2 * j2
    lo = abs(e1 - e2)
    hi = e1 + e2
    return [F(k, 2) for k in range(int(lo), int(hi) + 1, 2)]


def tensor(frep1, frep2):
    out = {}
    for (j1, k1), m1 in frep1.items():
        for (j2, k2), m2 in frep2.items():
            for a in _cg_spin(j1, j2):
                for b in _cg_spin(k1, k2):
                    p = (a, b)
                    out[p] = out.get(p, 0) + m1 * m2
    return {p: m for p, m in out.items() if m}


def plus(*freps):
    out = {}
    for r in freps:
        for p, m in r.items():
            out[p] = out.get(p, 0) + m
    return {p: m for p, m in out.items() if m}


def _frobenius(frep, sign):
    """(chi^2 + sign * chi(g^2)) / 2 at the character level; returns the
    decomposed result (asserts integrality)."""
    c = char(frep)
    d = lmul(c, c)
    g2 = lscale2(c)
    tot = ladd(d, {e: sign * v for e, v in g2.items()})
    assert all(v % 2 == 0 for v in tot.values()), "Frobenius char not integral"
    return decompose_char({e: v // 2 for e, v in tot.items() if v})


def sym2(frep):
    return _frobenius(frep, +1)


def wedge2(frep):
    return _frobenius(frep, -1)


def hom_dim(frepA, frepB):
    decA = decompose(frepA)
    decB = decompose(frepB)
    return sum(m * decB.get(p, 0) for p, m in decA.items())


def invariant_rank(frep):
    """Number of invariant bilinear structures on frep = sum m^2."""
    dec = decompose(frep)
    return sum(m * m for m in dec.values())


def selftest():
    """Pairing sanity: irreducible characters orthonormal; dims right."""
    for (jL, jR), d in [((0, 0), 1), ((F(1, 2), 0), 2), ((F(1, 2), F(1, 2)), 4),
                        ((1, 0), 3), ((1, 1), 9), ((F(3, 2), F(1, 2)), 8)]:
        c = chi_pair((jL, jR))
        assert pair(c, c) == 1, (jL, jR)
        assert ldim(c) == d, (jL, jR, ldim(c), d)
    c1, c2 = chi_pair((1, 0)), chi_pair((0, 1))
    assert pair(c1, c2) == 0
    return "core selftest OK"
