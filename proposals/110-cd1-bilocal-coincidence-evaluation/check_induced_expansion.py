#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
110: induced coincidence expansion of G at the locked identity frame.

G = f * eta * U * E (locked data Phi = (v+sigma) e, e(0)=I, g+ = eta):
  f = (1+a)(1+a+delta), delta = l^r a_r + 1/2 l^r l^s a_rs   (a = sigma/v),
  U = I + l^r w_r + 1/2 l^r l^s (d_s w_r + w_r w_s)   (eq:bilocal-frame-expansion),
  E = I + l^r e_r + 1/2 l^r l^s (e_rs + e_sr)          (condensate profile).
w_r, d_s w_r are so(eta)-valued (dressed connection, eq:dressed-omega);
e_r general.  Symmetry of a (mu,nu) matrix = plain transpose (g+ = eta).
Coefficients G00 = G(0,0), G1(r) = d_r G|0, G2(r,s) = d_r d_s G|0 are built
mechanically from the product rule on f, U, E (derivatives of U, E by
sympy .diff on the small factor matrices; no global polynomial expansion).

I1  G00 = (1+a)^2 eta; vacuum a=0 gives eta = g+ exactly.
I2  Pure connector at O(l): eta w_r antisymmetric (pure gauge, no soldering).
I3  sym of d_s w_r piece: 0 (derivative part stays antisymmetric at O(l^2)).
I4  Soldering-type connector first at O(l^2): sym(eta{w_r,w_s}) nonzero
    generically (abelian subcase included) - explicit entries printed.
I5  G1(r) symmetric part = profile + radial data only (connector is
    antisymmetric); 2 sym(eta e_r) is d_r g+ at the locked frame.
I6  Path-dependent (curvature-type) piece eta*F_{rs} is antisymmetric:
    O(l^2) path dependence never touches the symmetric sector.
Symbolic output is a check, not a proof.
Re-run: python -I -c "exec(open('check_induced_expansion.py').read());
  exec(open('check_induced_expansion_part2.py').read());
  exec(open('check_induced_expansion_part3.py').read())"   (ALL CHECKS PASS)
"""
import sympy as sp

eta = sp.diag(-1, 1, 1, 1)
I4 = sp.eye(4)
fails = []
def ck(name, cond):
    ok = bool(cond)
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        fails.append(name)

def msum(it):
    t = sp.zeros(4)
    for m in it:
        t = t + m
    return t

T = []
for i in range(4):
    for j in range(i+1, 4):
        M = sp.zeros(4)
        if i == 0:
            M[0, j] = 1; M[j, 0] = 1
        else:
            M[i, j] = 1; M[j, i] = -1
        T.append(M)

R = lambda nm, k: sp.Symbol(f"{nm}{k}")
def soexp(nm):
    return msum(R(nm, k)*T[k] for k in range(6))

l = [sp.Symbol(f"l{i}") for i in range(1, 5)]
w = [soexp(f"w{i}") for i in range(1, 5)]
dw = {(i, j): soexp(f"dw{i}{j}") for i in range(1, 5) for j in range(1, 5)}
e = [sp.Matrix(4, 4, lambda p, q: R(f"e{i}", 10*p+q)) for i in range(1, 5)]
e2 = {(i, j): sp.Matrix(4, 4, lambda p, q: R(f"ee{i}{j}", 10*p+q))
      for i in range(1, 5) for j in range(1, 5)}
ar = [sp.Symbol(f"a{i}") for i in range(1, 5)]
ars = {(i, j): sp.Symbol(f"a{i}{j}") for i in range(1, 5) for j in range(1, 5)}
a = sp.Symbol("a")

delta = sum(l[r-1]*ar[r-1] for r in range(1, 5)) \
        + sp.Rational(1, 2)*sum(l[r-1]*l[s-1]*ars[(r, s)]
                                for r in range(1, 5) for s in range(1, 5))
f = sp.expand((1+a)**2 + (1+a)*delta)
U = I4 + msum(l[r-1]*w[r-1] for r in range(1, 5)) \
    + sp.Rational(1, 2)*msum(l[r-1]*l[s-1]*(dw[(s, r)] + w[r-1]*w[s-1])
                             for r in range(1, 5) for s in range(1, 5))
E = I4 + msum(l[r-1]*e[r-1] for r in range(1, 5)) \
    + sp.Rational(1, 2)*msum(l[r-1]*l[s-1]*(e2[(r, s)] + e2[(s, r)])
                             for r in range(1, 5) for s in range(1, 5))

z = {x: 0 for x in l}
def d1m(M, i):
    return sp.simplify(M.diff(l[i-1]).subs(z))
def d2m(M, i, j):
    return sp.simplify(M.diff(l[i-1], l[j-1]).subs(z))

Fd0 = f.subs(z)
Fd1 = {r: d1m(f, r) for r in range(1, 5)}
Fd2 = {(r, s): d2m(f, r, s) for r in range(1, 5) for s in range(1, 5)}
Ud1 = {r: d1m(U, r) for r in range(1, 5)}
Ud2 = {(r, s): d2m(U, r, s) for r in range(1, 5) for s in range(1, 5)}
Ed1 = {r: d1m(E, r) for r in range(1, 5)}
Ed2 = {(r, s): d2m(E, r, s) for r in range(1, 5) for s in range(1, 5)}

G00 = sp.simplify(Fd0 * eta)
G1 = {r: sp.expand(Fd1[r]*eta + Fd0*eta*Ud1[r] + Fd0*eta*Ed1[r])
      for r in range(1, 5)}
G2 = {(r, s): sp.expand(
        Fd2[(r, s)]*eta
        + Fd1[r]*eta*Ud1[s] + Fd1[s]*eta*Ud1[r]
        + Fd0*eta*Ud2[(r, s)]
        + Fd0*eta*(Ud1[r]*Ed1[s] + Ud1[s]*Ed1[r])
        + Fd1[r]*eta*Ed1[s] + Fd1[s]*eta*Ed1[r]
        + Fd0*eta*Ed2[(r, s)])
      for r in range(1, 5) for s in range(1, 5)}

# sanity: G00 must also equal (f*eta*U*E) at l=0 computed as product
G00p = sp.simplify((f * eta * U * E).subs(z))
ck("I0 product-rule G00 matches direct substitution",
   sp.simplify(G00 - G00p) == sp.zeros(4))
ck("I1 G(0,0) = (1+a)^2 eta", sp.simplify(G00 - (1+a)**2*eta) == sp.zeros(4))
ck("I1b vacuum a=0: G(0,0)=eta", sp.simplify(G00.subs(a, 0) - eta) == sp.zeros(4))
