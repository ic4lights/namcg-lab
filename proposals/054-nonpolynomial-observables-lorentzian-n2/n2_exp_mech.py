#!/usr/bin/env python3
"""Mechanism numerics for proposal 054: exponential probes Tr e^{ik.A} at N=2.

Uses the 053 exact N=2 reduced integrand (same code path) with a MULTIPLICATIVE PROXY
FACTOR F(w) applied to the full reduced integrand. The proxies lower-bound
|Tr e^{ik.A(u,A~)}| along the flat (commuting, rank-1) corner of the reduced domain and carry
NO boundedness information (one-sided evidence, labeled as such in the proposal):

  flat corner: w1 = e^s large, w2 = e^{s-v}, w3 = e^{s-v-z}; S_E ~ e2 = w1(w2+w3)+w2w3
  stays bounded (->0 on exact rank-1 rays) for v ~ 2s + sigma, so this corner carries the
  exponential growth of O_k against the polynomial transverse suppression.
  - large-radius growth carrier (any nonzero real k, both temporal and spatial ray
    directions: on a ray A~_mu = rho_mu H the radius is rho ~ sqrt(w1); the growth
    coefficient is |Im omega_u(rho_hat;k)| rho = sin-type * |k| * rho, see strip_symmetry.py
    check (3)): |2cos(z/2)|^2 = 4(cos^2 Re z/2 + sinh^2 Im z/2) gives pointwise
    |Tr e^{ik.A}| >= e^{c sqrt(w1)}/2; proxy cosh(c sqrt(w1)) (parameter cb).
  - temporal (a-flat) Fresnel-strip growth at eps = gam = 0 only: the a-Gaussian width is
    Q_1 = lambda(w2+w3)-type, so the reachable a-radius grows like (w2+w3)^{-1/2} with
    growth e^{c_a r}; proxy cosh(c_a (w2+w3)^{-1/2}) (parameter ca). This proxy is NOT a
    lower bound when a mass or regulator damps the a-direction (eps>0 or gam<0): the true
    a-radius is then bounded, so ca is used only at eps=gam=0 and is switched off in
    experiments 2 and 3 (it overestimates there).
  Proxies are masked to w1 > 1 (large-radius corner).

Experiments:
 0  F=1 validation: reproduce the 053 Euclidean Z (u=1, eps=0, gam=0) and its phase
    7g/4 mod 2 = 1.25 (np.angle prints the principal value, -0.75 == 1.25 mod 2), and
    confirm the k=0 modulus integral converges.
 1  u=1, eps=0, gam=0: modulus partial integrals |Zmod|(smax) with cosh proxies:
    unbounded growth for any c>0 (RHS absolute divergence at every nonzero k).
 2  u=1, eps=0: mass sign gam=+0.2 / 0 / -0.2 bare (k=0 only), and with the large-radius
    cosh proxy (cb only, honest lower bound at every gam): growth iff gam>0; gam<0
    Gaussian damping dominates the linear-growth proxy (supports the fixed-gamma<0
    extension to all k; gam>0 divergence even at k=0).
 3  u=0.6 / u=0.3, eps-series with the masked large-radius cosh proxy (cb only):
    fixed-eps integrals exist but the modulus grows like exp(c/sqrt(eps)); fit
    log|Zmod| vs eps^{-1/2}; slope reference c*sqrt(80) from the regulator cap
    w1 <= ~80/eps used by srange.
Run:  python -I n2_exp_mech.py   (a few minutes; tee to n2_exp_mech.out)
"""
import numpy as np, math, itertools
from scipy.special import gamma as Gam
LAM = 0.5

def nodes(n, lo, hi):
    x, w = np.polynomial.legendre.leggauss(n)
    return 0.5 * (hi - lo) * x + 0.5 * (hi + lo), 0.5 * (hi - lo) * w

def compute(D, fermions, eps, u, gam=0.0, ca=0.0, cb=0.0, wmask=1.0,
            ns=300, nv=120, nz=120, srange=None, vmax=40., zmax=36., chunk=40):
    """Reduced integral with factor F = cosh(cb*sqrt(w1))*cosh(ca/sqrt(w2+w3)), masked to
    w1>wmask (ca term only used at eps=gam=0). Returns complex signed Z and modulus Zmod."""
    d = D - 1; p = (D // 2 - 1) if fermions else 0
    al = 3 * np.pi * u / 8; be = np.pi * u / 8
    ph_meas = np.exp(1j * (3 * d * be - 3 * al))
    if srange is None:
        hi = np.log(80.0 / max(eps, 1e-9)) if eps > 0 else 22.0
        srange = (-10.0, min(hi, 24.0))
    s, ws = nodes(ns, *srange); v, wv = nodes(nv, 0.0, vmax); z, wz = nodes(nz, 0.0, zmax)
    t = np.exp(s)
    terms = [n for n in itertools.product(range(p + 1), repeat=3) if sum(n) <= p]
    Z = 0j; Zmod = 0.0
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
        ex = np.exp(1j * LAM * np.exp(4j * be) * e2 - eps * np.exp(2j * be) * T - 1j * (gam / 2) * np.exp(2j * be) * T)
        Tk = [w2 + w3, w1 + w3, w1 + w2]
        Q = [eps * np.exp(-2j * al) + 1j * LAM * np.exp(2j * (be - al)) * Tk[k] - 1j * (gam / 2) * np.exp(-2j * al) for k in range(3)]
        D0 = np.exp(6j * be) * w1 * w2 * w3
        pref = np.exp(-2j * al + 4j * be)
        rk = [-pref * w2 * w3 / Q[0], -pref * w1 * w3 / Q[1], -pref * w1 * w2 / Q[2]]
        base0 = Gam(0.5) ** 3 * Q[0] ** (-0.5) * Q[1] ** (-0.5) * Q[2] ** (-0.5)
        Gr = [Gam(n + 0.5) / Gam(0.5) for n in range(p + 2)]
        Dpow = [np.ones_like(D0)]
        for j in range(p): Dpow.append(Dpow[-1] * D0)
        rpow = [[np.ones_like(D0)] for k in range(3)]
        for k in range(3):
            for j in range(p): rpow[k].append(rpow[k][-1] * rk[k])
        tot = np.zeros_like(D0)
        for n in terms:
            n0 = p - sum(n)
            coef = math.factorial(p) / (math.factorial(n0) * math.factorial(n[0]) * math.factorial(n[1]) * math.factorial(n[2]))
            tot = tot + coef * Dpow[n0] * rpow[0][n[0]] * rpow[1][n[1]] * rpow[2][n[2]] * Gr[n[0]] * Gr[n[1]] * Gr[n[2]]
        tot = tot * base0
        F = np.ones_like(D0)
        if cb != 0.0: F = F * np.cosh(cb * np.sqrt(w1))
        if ca != 0.0: F = F * np.cosh(ca / np.sqrt(w2 + w3))
        if (ca != 0.0 or cb != 0.0) and wmask is not None:
            F = np.where(w1 > wmask, F, 1.0)
        integ = dens * ex * tot * F
        Z += np.sum(integ)
        Zmod += np.sum(np.abs(integ))
    return {'Z': Z * ph_meas, 'Zmod': abs(Zmod * ph_meas)}

def srng(eps, smax=14.0):
    return (-8.0, min(np.log(80.0 / eps), smax)) if eps > 0 else (-8.0, smax)

def main():
    np.seterr(all='ignore')
    G = dict(ns=300, nv=120, nz=120, vmax=40., zmax=36.)
    def lg10(x):
        return "%.4f" % np.log10(x) if np.isfinite(x) and x > 0 else ">%d" % 308
    print("=== 0. validation F=1 (053 chain): u=1, eps=0, gam=0, D=10, fermions ===")
    E = compute(10, True, 0.0, 1.0, srange=(-10., 22.), **G)
    E2 = compute(10, True, 0.0, 1.0, srange=(-10., 20.), ns=400, nv=150, nz=150, vmax=44., zmax=44.)
    print("  Z = %.8e   phase/pi = %.6f   (principal value; expected 7g/4 mod 2 = %.4f, i.e. %.6f mod 2)" %
          (abs(E['Z']), np.angle(E['Z']) / np.pi, (7 * 3 / 4) % 2, (np.angle(E['Z']) / np.pi) % 2))
    print("  grid stability |Z2/Z1| = %.8f ; |Zmod|/|Z| = %.4f (k=0 modulus converges)" %
          (abs(E2['Z'] / E['Z']), E2['Zmod'] / abs(E2['Z'])))
    print("=== 1. u=1, eps=0, gam=0: masked cosh proxies, |Zmod|(smax) partial integrals ===")
    print("  (float64 overflows above log10 ~ 308; log10 printed; smax capped to keep most values finite)")
    print("  cb = large-radius growth carrier (valid lower bound for every nonzero real k);")
    print("  ca = a-Fresnel-strip carrier (valid only at eps=gam=0, see header)")
    for (ca, cb) in [(0.0, 0.0), (0.0, 0.15), (0.0, 0.4), (0.15, 0.0), (0.4, 0.0)]:
        row = []
        for smax in (8., 10., 12., 13.5):
            R = compute(10, True, 0.0, 1.0, ca=ca, cb=cb, srange=(-8., smax), **G)
            row.append(lg10(R['Zmod']))
        print("  ca=%.2f cb=%.2f  log10|Zmod|(smax=8,10,12,13.5): " % (ca, cb) + "  ".join(row))
    print("=== 2. u=1, eps=0: mass sign (proxy = cb only, honest lower bound at every gam) ===")
    for gam in (0.2, 0.0, -0.2):
        row = []
        for smax in (8., 10., 12.):
            R = compute(10, True, 0.0, 1.0, gam=gam, srange=(-8., smax), **G)
            row.append(lg10(R['Zmod']))
        print("  bare(k=0) gam=%+.2f  log10|Zmod|(8,10,12): " % gam + "  ".join(row))
    for gam in (0.2, -0.2):
        row = []
        for smax in (8., 10., 12., 13.5):
            R = compute(10, True, 0.0, 1.0, gam=gam, cb=0.4, srange=(-8., smax), **G)
            row.append(lg10(R['Zmod']))
        print("  proxy(cb=0.4) gam=%+.2f  log10|Zmod|(8,10,12,13.5): " % gam + "  ".join(row))
    print("=== 3. fixed-eps u=0.6 / u=0.3: masked large-radius cosh proxy (cb=0.4), eps series ===")
    es = (1.0, 0.3, 0.1, 0.03, 0.01)
    for u in (0.6, 0.3):
        rows = []
        for eps in es:
            R = compute(10, True, eps, u, cb=0.4, srange=srng(eps), **G)
            rows.append((abs(R['Z']), R['Zmod']))
        print("  u=%.1f signed |Z|(eps=1,0.3,0.1,0.03,0.01): " % u + "  ".join("%.4e" % x[0] for x in rows))
        print("       log10 Zmod(eps): " + "  ".join(lg10(x[1]) for x in rows))
        lg = [np.log(x[1]) for x in rows if np.isfinite(x[1])]; inv = [1 / np.sqrt(e) for e, xx in zip(es, rows) if np.isfinite(xx[1])]
        A = np.polyfit(inv, lg, 1)
        print("       fit log Zmod = %.4f * eps^{-1/2} + %.4f   (reference: c*sqrt(80) = %.3f, c=0.4)" % (A[0], A[1], 0.4 * np.sqrt(80)))
    print("done")

if __name__ == "__main__":
    main()
