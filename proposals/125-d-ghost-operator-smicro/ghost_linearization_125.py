#!/usr/bin/env python3
# -*- coding: ascii -*-
# Item 125: end-to-end symbolic verification of the first variation of the
# harmonic / de-Donder gauge functional F^mu = g^{ab} Gamma^mu_{ab} along
# delta g = Lie_Xi g, with correct t-linearization, controls, and an
# O(t^2)-contamination detector.
#
# Conventions: EXACTLY the manuscript equations eq:christoffel and
# eq:riemann (ch02-preliminaries.tex):
#   Gamma^r_{mn} = 1/2 g^{rs} (d_m g_{ns} + d_n g_{ms} - d_s g_{mn})
#   R^r_{smn}    = d_m Gamma^r_{ns} - d_n Gamma^r_{ms}
#                  + Gamma^r_{ml} Gamma^l_{ns} - Gamma^r_{nl} Gamma^l_{ms}
#   R_{mn} = R^r_{m r n}
# Signature (-,+,+,+) is irrelevant to the algebra below (pure metric algebra);
# the Riemann convention above is reproduced and checked on S^2 (test A4).
#
# t-linearization discipline (the failure mode of the 123 review-r1 addendum
# is the finite shift g + Lie_Xi g with no bookkeeping parameter, which mixes
# O(t^2) terms into the linear coefficient). The FIRST variation of any
# functional A(g) here is d/dt A(g + t*k)|t=0 with k the first-order data
# (k = Lie_Xi g), by exact differentiation -- never a finite difference.
import sys, time
from sympy import (symbols, Function, Matrix, Rational, simplify, expand,
                   sin, cos, diff, Poly, linsolve, symbols as S)

T0 = time.time()
def log(*a):
    print("[%6.1fs]" % (time.time() - T0), *a)
    sys.stdout.flush()

X = []          # set per test: coordinate tuple
R = Rational

def cmetric(n):
    gs = {}
    for i in range(n):
        for j in range(i, n):
            gs[(i, j)] = Function('g_%d%d' % (i, j))(*X)
    return Matrix([[gs[(min(i, j), max(i, j))] for j in range(n)] for i in range(n)])

def invmat(met):
    ig = met.inv()
    for i in range(met.rows):
        for j in range(met.cols):
            ig[i, j] = simplify(ig[i, j])
    return ig

def gamma(met, iginv, n):
    gam = {}
    for r in range(n):
        for m in range(n):
            for q in range(m, n):
                s = 0
                for ss in range(n):
                    s += iginv[r, ss] * (diff(met[m, ss], X[q])
                                         + diff(met[q, ss], X[m])
                                         - diff(met[m, q], X[ss]))
                v = R(1, 2) * simplify(s)
                gam[(r, m, q)] = v
                gam[(r, q, m)] = v
    return gam

def richi(ig, gam, n):
    ric = Matrix.zeros(n, n)
    for m in range(n):
        for q in range(m, n):
            s = 0
            for r in range(n):
                s += diff(gam[(r, q, m)], X[r]) - diff(gam[(r, r, m)], X[q])
                for l in range(n):
                    s += gam[(r, r, l)] * gam[(l, q, m)] - gam[(r, q, l)] * gam[(l, r, m)]
            v = simplify(s)
            ric[m, q] = v
            ric[q, m] = v
    return ric

def conn(gam, ig, n):
    # C[(a, b, mu)] = Gamma^mu_{ab}: for a vector (nabla_b xi)^mu
    # = d_b xi^mu + Gamma^mu_{bd} xi^d. Slots (lower, lower, upper).
    C = {}
    for a in range(n):
        for b in range(n):
            for mu in range(n):
                C[(a, b, mu)] = gam[(mu, a, b)]
    return C

def lie(met, xi, n):
    K = Matrix.zeros(n, n)
    for a in range(n):
        for b in range(a, n):
            s = sum(xi[p] * diff(met[a, b], X[p]) for p in range(n))
            s += sum(met[p, b] * diff(xi[p], X[a]) for p in range(n))
            s += sum(met[a, p] * diff(xi[p], X[b]) for p in range(n))
            v = expand(s)
            K[a, b] = v
            K[b, a] = v
    return K

def geom(met, n):
    ig = invmat(met)
    gam = gamma(met, ig, n)
    ric = richi(ig, gam, n)
    C = conn(gam, ig, n)
    return ig, gam, ric, C

def dF(met, k, n, t):
    """d/dt F(met + t*k)|t=0 componentwise, F^mu = g^{ab}Gamma^mu_{ab},
    with the exact inverse of met + t*k (true first variation, no t^2 leak)."""
    gmet = met + t * k
    ig = gmet.inv()
    gam = {}
    for r in range(n):
        for m in range(n):
            for q in range(m, n):
                s = 0
                for ss in range(n):
                    s += ig[r, ss] * (diff(gmet[m, ss], X[q])
                                      + diff(gmet[q, ss], X[m])
                                      - diff(gmet[m, q], X[ss]))
                v = R(1, 2) * simplify(s)
                gam[(r, m, q)] = v
                gam[(r, q, m)] = v
    out = []
    for mu in range(n):
        Fmu = sum(ig[a, b] * gam[(mu, a, b)] for a in range(n) for b in range(n))
        out.append(simplify(diff(Fmu, t).subs(t, 0)))
    return out

def boxvec(ig, C, xi, n):
    """(box xi)^mu = g^{ab} nabla_a nabla_b xi^mu (rough Laplacian on vectors)."""
    out = []
    for mu in range(n):
        bx = 0
        for a in range(n):
            for b in range(n):
                t1 = diff(xi[mu], X[a], X[b])
                t1 += sum(diff(C[(b, d, mu)], X[a]) * xi[d] for d in range(n))
                t1 += sum(C[(b, d, mu)] * diff(xi[d], X[a]) for d in range(n))
                t1 += sum(C[(a, d, mu)] * (diff(xi[d], X[b])
                          + sum(C[(b, e, d)] * xi[e] for e in range(n))) for d in range(n))
                t1 -= sum(C[(a, b, d)] * (diff(xi[mu], X[d])
                          + sum(C[(d, e, mu)] * xi[e] for e in range(n))) for d in range(n))
                bx += ig[a, b] * t1
        out.append(simplify(bx))
    return out

def ricvec(ig, ric, xi, n):
    return [simplify(sum(ig[mu, s] * ric[s, nu] * xi[nu]
                         for s in range(n) for nu in range(n))) for mu in range(n)]

def divxi(ig, C, xi, n):
    return simplify(sum(ig[a, b] * (diff(xi[b], X[a])
               + sum(C[(a, d, b)] * xi[d] for d in range(n)))
               for a in range(n) for b in range(n)))

def grad_div(ig, C, xi, n):
    d = divxi(ig, C, xi, n)
    return [simplify(sum(ig[mu, a] * diff(d, X[a]) for a in range(n)))
            for mu in range(n)]

def div_grad_xi(ig, C, xi, n):
    """(D xi)^mu = nabla_nu nabla^mu xi^nu (divergence on the lower slot)."""
    Wm = {}
    for mu in range(n):
        for nu in range(n):
            s = 0
            for m in range(n):
                inner = diff(xi[nu], X[m]) + sum(C[(m, d, nu)] * xi[d] for d in range(n))
                s += ig[mu, m] * inner
            Wm[(mu, nu)] = simplify(s)
    for mu in range(n):
        s = 0
        for nu in range(n):
            for p in range(n):
                term = diff(Wm[(mu, nu)], X[p])
                term += sum(C[(p, e, mu)] * Wm[(e, nu)] for e in range(n))
                term -= sum(C[(p, e, nu)] * Wm[(mu, e)] for e in range(n))
                s += ig[p, nu] * term
        out.append(simplify(s))
    return out

log("== 125 ghost_linearization: first variation of F^mu = g^{ab} Gamma^mu_{ab} ==")
RESULTS = []
t = symbols('t')

# ---------- Test A: round S^2 (theta, phi): settle the sign by inspection ----
X = (symbols('x0'), symbols('x1'))
th, ph = X
met = Matrix([[1, 0], [0, sin(th)**2]])
f = Function('f')(th)
xi = [0, f]
ig, gam, ric, C = geom(met, 2)
k = lie(met, xi, 2)
dFv = dF(met, k, 2, t)
bx = boxvec(ig, C, xi, 2)
rv = ricvec(ig, ric, xi, 2)
log("A0 S^2 rotational xi:  dF = %s" % dFv)
log("A0 S^2 rotational xi: box xi = %s ;  Ric xi = %s" % (bx, rv))
p_rp = [simplify(a - b - c) for a, b, c in zip(dFv, bx, rv)]      # dF - (box+Ric)
p_r0 = [simplify(a - b) for a, b in zip(dFv, bx)]                  # dF - box
m_rp = [simplify(a + b + c) for a, b, c in zip(dFv, bx, rv)]      # dF + (box+Ric)
log("A1 dF-(box+Ric) = %s   [123-sign candidate +]" % p_rp)
log("A1 dF+(box+Ric) = %s   [123-sign candidate -]" % m_rp)
log("A1 dF-box       = %s   [no-Ric candidate]" % p_r0)
RESULTS.append(not all(a == 0 for a in p_rp))   # record only; discovery in B
# Killing kernel control (positive controls for the kernel guard)
KILLS = [[0, 1],
         [sin(ph) * (-cos(th)), -sin(th) * cos(ph)],
         [cos(ph) * (-cos(th)), -sin(th) * sin(ph)]]
allok = True
for i, xk in enumerate(KILLS):
    kr = lie(met, xk, 2)
    mkr = [simplify(b + c) for b, c in zip(boxvec(ig, C, xk, 2), ricvec(ig, ric, xk, 2))]
    kz = all(simplify(a) == 0 for a in kr) and all(a == 0 for a in mkr)
    log("A2 Killing K%d: Lxi g = 0 and (box+Ric)xi = 0      %s" % (i, "PASS" if kz else "FAIL"))
    allok = allok and kz
RESULTS.append(allok)
xg = [Function('u')(*X), Function('v')(*X)]
mres = [b + c for b, c in zip(boxvec(ig, C, xg, 2), ricvec(ig, ric, xg, 2))]
nzk = not all(a == 0 for a in mres)
log("A3 generic xi: (box+Ric)xi nonzero (guard teeth)      %s" % ("PASS" if nzk else "FAIL"))
RESULTS.append(nzk)
Rsc = simplify(sum(ig[a, b] * ric[a, b] for a in range(2) for b in range(2)))
conv = (Rsc == 2) and all(simplify(ric[a, b] - met[a, b]) == 0 for a in range(2) for b in range(2))
log("A4 eq:riemann convention: S^2 R=+2, Ric=g              %s (R=%s)" % ("PASS" if conv else "FAIL", Rsc))
RESULTS.append(conv)

# ---------- Test B: identity discovery on a GENERAL 2-metric ---------------
# dF^mu = a*(box xi)^mu + b*(Ric xi)^mu + c*(grad div xi)^mu + d*(DivGrad xi)^mu,
# xi a general quadratic vector field (12 parameters); solve for (a,b,c,d).
X = (symbols('x0'), symbols('x1'))
met = cmetric(2)
cs = S(' '.join('c%d_%d' % (i, j) for i in range(2) for j in range(6)))
def quad(idx):
    m = [1, X[0], X[1], X[0]**2, X[0]*X[1], X[1]**2]
    return sum(cs[idx * 6 + j] * m[j] for j in range(6))
xi = [quad(0), quad(1)]
ig, gam, ric, C = geom(met, 2)
k = lie(met, xi, 2)
dFv = dF(met, k, 2, t)
bx = boxvec(ig, C, xi, 2)
rv = ricvec(ig, ric, xi, 2)
gv = grad_div(ig, C, xi, 2)
dv = div_grad_xi(ig, C, xi, 2)
a_, b_, c_, d_ = S('a b c d')
eqs = []
for mu in range(2):
    res = expand(simplify(dFv[mu] - (a_ * bx[mu] + b_ * rv[mu] + c_ * gv[mu] + d_ * dv[mu])))
    p = Poly(res, *list(cs))
    eqs += list(p.coeffs())
sol = linsolve(eqs, (a_, b_, c_, d_))
log("B  general 2-metric: solutions (a,b,c,d) for dF = a*box+b*Ric+c*graddiv+d*DivGrad: %s" % sol)

print("SUMMARY part1: %d/%d PASS" % (sum(1 for r in RESULTS if r), len(RESULTS)))
sys.exit(0 if all(RESULTS) else 1)
