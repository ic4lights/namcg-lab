#!/usr/bin/env python3
"""Proposal 057 r1, script 2: reduced N=2 chart (055 structure, copied below) with
mode 'factoru': the FACTORIZED branch insertion using the CONTOUR-DEPENDENT
coefficient gc(u) = e^{3 pi i (1-u)/8} r0/2 of A~_0 in k^mu A_mu on R_u, instead of
055's frozen u=0 value e^{3 pi i/8} r0/2. Probes, at u in {0.3, 0.6}, pure temporal
slice k (r=0, r0=1), regulator (A), eps ladder down to 0.003, gamma ladder
0,-0.2,-0.1,-0.05,-0.02:
  P0  sanity: factoru with r0=1e-6 -> ratio 2 vs bare (O_k -> Tr I as k -> 0).
  P1  |Z[O_k]|/|Z[1]| per gamma: growth slope in 1/eps vs true-phase prediction
      r0^2/(16 sqrt2) = 0.044194 (u-independent) vs frozen-phase 0.0623 (u=0.3),
      0.0506 (u=0.6).
  P2  signed bridge difference D(eps,gam) = |Z_eps[O_k;gam] - Z_eps[O_k;0]| / |Z_eps[1;0]|
      and the per-|gam| constant C = D/|gam|: its growth in 1/eps is the model-level
      statement that the link constant is NOT eps-uniform (Leg C obstruction).
  P3  Zmod/|Z| cancellation diagnostic at gamma=0.
Run: python -I chart_bridge.py   (~2-4 min on one core)
"""
import numpy as np, math, itertools, time
import sympy as sp
from scipy.special import gamma as Gam
LAM = 0.5

def nodes(n, lo, hi):
    x, w = np.polynomial.legendre.leggauss(n)
    return 0.5 * (hi - lo) * x + 0.5 * (hi + lo), 0.5 * (hi - lo) * w

def branch_qpolys(gc2, jmax=4):
    x = sp.Symbol('x')
    g = sp.nsimplify(complex(gc2))
    B = 2 * sp.sqrt(sp.pi) * sp.sqrt(x) * sp.exp(-g * x / 4)
    qs = [sp.Integer(1)]
    for j in range(jmax):
        qn = sp.expand(x**2 * (sp.diff(B * qs[-1], x) / B))
        qs.append(qn)
    out = []
    for q in qs:
        p = sp.Poly(sp.expand(q), x)
        cf = [complex(c) for c in p.all_coeffs()[::-1]]
        out.append(np.array(cf, dtype=np.complex128))
    return out

def compute(D, fermions, eps, u, gam=0.0, mode='bare', r0=1.0, M=64, tol=1e-9,
            cb=0.0, ca=0.0, wmask=1.0, ns=96, nv=44, nz=44, srange=None,
            vmax=40., zmax=36., chunk=4):
    """As in 055 n2_slice_r1.compute, plus mode 'factoru' (contour-dependent gc)."""
    d = D - 1; p = (D // 2 - 1) if fermions else 0
    al = 3 * np.pi * u / 8; be = np.pi * u / 8
    ph_meas = np.exp(1j * (3 * d * be - 3 * al))
    if mode in ('exact', 'factor'):
        gc2 = (np.exp(1j * 3 * np.pi / 8) ** 2) * (r0 ** 2) / 4.0
    elif mode == 'factoru':
        gc2 = (np.exp(1j * 3 * np.pi * (1 - u) / 8) ** 2) * (r0 ** 2) / 4.0
    else:
        gc2 = None
    qlist = branch_qpolys(gc2, p) if mode in ('factor', 'factoru') else None
    if srange is None:
        hi = np.log(80.0 / max(eps, 1e-9)) if eps > 0 else 22.0
        srange = (-10.0, min(hi, 24.0))
    s, ws = nodes(ns, *srange); v, wv = nodes(nv, 0.0, vmax); z, wz = nodes(nz, 0.0, zmax)
    t = np.exp(s)
    terms = [n for n in itertools.product(range(p + 1), repeat=3) if sum(n) <= p]
    nt = len(terms)
    Z = 0j; Zmod = 0.0; maxterm = 0.0; Mused = 0
    for start in range(0, ns, chunk):
        idx = np.arange(start, min(start + chunk, ns))
        T1, V, Z_ = np.meshgrid(t[idx], v, z, indexing='ij')
        W_ = (t[idx] * ws[idx])[:, None, None] * wv[None, :, None] * wz[None, None, :]
        w1 = T1; w2 = T1 * np.exp(-V); w3 = w2 * np.exp(-Z_)
        jac = w2 * w3
        Vd = (w1 - w2) * (w1 - w3) * (w2 - w3)
        dens = W_ * jac * Vd * (w1 * w2 * w3) ** ((d - 4) / 2)
        T = w1 + w2 + w3
        e2 = w1 * w2 + w1 * w3 + w2 * w3
        ex = np.exp(1j * LAM * np.exp(4j * be) * e2 - (eps + 1j * gam / 2) * np.exp(2j * be) * T)
        Tk = [w2 + w3, w1 + w3, w1 + w2]
        Q = [eps * np.exp(-2j * al) + 1j * LAM * np.exp(2j * (be - al)) * Tk[k] - 1j * (gam / 2) * np.exp(-2j * al) for k in range(3)]
        D0 = np.exp(6j * be) * w1 * w2 * w3
        pref = np.exp(-2j * al + 4j * be)
        rk = [-pref * w2 * w3 / Q[0], -pref * w1 * w3 / Q[1], -pref * w1 * w2 / Q[2]]
        Gr = [Gam(n + 0.5) / Gam(0.5) for n in range(p + 2)]
        Dpow = [np.ones_like(D0)]
        for j in range(p): Dpow.append(Dpow[-1] * D0)
        rpow = [[np.ones_like(D0)] for k in range(3)]
        for k in range(3):
            for j in range(p): rpow[k].append(rpow[k][-1] * rk[k])
        coefn = []
        for n in terms:
            n0 = p - sum(n)
            coefn.append(math.factorial(p) / (math.factorial(n0) * math.factorial(n[0]) * math.factorial(n[1]) * math.factorial(n[2])))
        if mode in ('bare', 'trivial'):
            factor = 2.0 if mode == 'trivial' else 1.0
            base0 = Gam(0.5) ** 3 * Q[0] ** (-0.5) * Q[1] ** (-0.5) * Q[2] ** (-0.5)
            tot = np.zeros_like(D0)
            for i, n in enumerate(terms):
                n0 = p - sum(n)
                tot = tot + coefn[i] * Dpow[n0] * rpow[0][n[0]] * rpow[1][n[1]] * rpow[2][n[2]] \
                      * (Gr[n[0]] * Q[0] ** (-n[0])) * (Gr[n[1]] * Q[1] ** (-n[1])) * (Gr[n[2]] * Q[2] ** (-n[2]))
            tot = tot * base0 * factor
        elif mode in ('factor', 'factoru'):
            x1 = 1.0 / Q[0]
            Bv = 2.0 * math.sqrt(math.pi) * np.sqrt(x1) * np.exp(-gc2 * x1 / 4)
            Iarr = [Bv * np.polynomial.polynomial.polyval(x1, qc) for qc in qlist]
            basef = Gam(0.5) ** 2 * Q[1] ** (-0.5) * Q[2] ** (-0.5)
            tot = np.zeros_like(D0)
            for i, n in enumerate(terms):
                n0 = p - sum(n)
                tot = tot + coefn[i] * Dpow[n0] * rpow[0][n[0]] * rpow[1][n[1]] * rpow[2][n[2]] \
                      * Iarr[n[0]] * (Gr[n[1]] * Q[1] ** (-n[1])) * (Gr[n[2]] * Q[2] ** (-n[2]))
            tot = tot * basef
        else:
            raise SystemExit("mode not supported here")
        F = np.ones_like(D0)
        if cb != 0.0: F = F * np.cosh(cb * np.sqrt(w1))
        if ca != 0.0: F = F * np.cosh(ca / np.sqrt(w2 + w3))
        integ = dens * ex * tot * F
        Z += np.sum(integ)
        Zmod += np.sum(np.abs(integ))
    return {'Z': Z * ph_meas, 'Zmod': abs(Zmod * ph_meas)}

def srng(eps, smax=14.0):
    return (-8.0, min(np.log(80.0 / eps), smax))

def main():
    np.seterr(all='ignore')
    G = dict(ns=56, nv=28, nz=28, vmax=40., zmax=36., chunk=4)
    esf = (0.03, 0.01, 0.003)
    gams = (0.0, -0.2, -0.1, -0.05, -0.02)
    t0 = time.time()
    print("=== P0 sanity: factoru at r0=1e-6 (u=0.3, eps=0.03) -> ratio 2 vs bare ===")
    A = compute(10, True, 0.03, 0.3, mode='bare', srange=srng(0.03), **G)
    F = compute(10, True, 0.03, 0.3, mode='factoru', r0=1e-6, srange=srng(0.03), **G)
    print("  |Z_factoru|/|Z_bare| = %.10f (must -> 2 = Tr I)" % abs(F['Z'] / A['Z']))
    for u in (0.3, 0.6):
        print("=== u=%.1f: P1 branch-factor ratios |Z[O_k]|/|Z[1]| (factoru vs bare) ===" % u)
        pred_true = 1.0 / (16 * math.sqrt(2))
        pred_frozen = math.cos(3 * np.pi * u / 4 - np.pi / 4) / 16
        print("  predictions: true-phase slope %.4f (u-independent); frozen-phase %.4f" % (pred_true, pred_frozen))
        Z0 = {}
        for gam in gams:
            rows = []
            for eps in esf:
                Ae = compute(10, True, eps, u, gam=gam, mode='bare', srange=srng(eps), **G)
                Rf = compute(10, True, eps, u, gam=gam, mode='factoru', r0=1.0, srange=srng(eps), **G)
                rows.append(abs(Rf['Z'] / Ae['Z']))
                if gam == 0.0:
                    Z0[eps] = (Rf['Z'], Ae['Z'], Rf['Zmod'])
            line = "  gam=%+.2f ratio (eps=0.03,0.01,0.003): " % gam + " ".join("%.4e" % x for x in rows)
            if gam == 0.0:
                lg = np.log(rows); inv = 1.0 / np.array(esf)
                sl = np.polyfit(inv, lg, 1)[0]
                line += " | slope(1/eps) %.4f" % sl
            print(line)
        print("  === P2 signed bridge difference D(eps,gam) and constant C = D/|gam| ===")
        for gam in gams[1:]:
            Ds = []
            for eps in esf:
                Rg = compute(10, True, eps, u, gam=gam, mode='factoru', r0=1.0, srange=srng(eps), **G)
                Ds.append(abs(Rg['Z'] - Z0[eps][0]) / abs(Z0[eps][1]))
            C = [Ds[i] / abs(gam) for i in range(len(esf))]
            lg = np.log(C); inv = 1.0 / np.array(esf)
            sl = np.polyfit(inv, lg, 1)[0]
            print("  gam=%+.2f D: " % gam + " ".join("%.4e" % x for x in Ds) +
                  " | C=D/|gam|: " + " ".join("%.4e" % x for x in C) +
                  " | slope ln C vs 1/eps = %.4f (eps-NOT-uniform if > 0)" % sl)
        print("  === P3 cancellation diagnostic (gamma=0) ===")
        for eps in esf:
            print("  eps=%.3f Zmod/|Z| = %.3e" % (eps, Z0[eps][2] / abs(Z0[eps][0])))
    print("done")

if __name__ == '__main__':
    main()
