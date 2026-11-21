#!/usr/bin/env python3
"""Proposal 055 r1, script 2: reduced N=2 model at u=0 / u=0.6 with the anti-Wick-slice
insertion for pure temporal slice k (k^0 = e^{3 pi i/8} r0, spatial r = 0), plus gamma<0
contrast and a pure-spatial cosh-carrier proxy run.

Model: the 053/054 reduced N=2 integrand (same structure as 054 n2_exp_mech.py). Variables
w1=e^s, w2=e^{s-v}, w3=e^{s-v-z} (spatial gram eigenvalues, d=10, LAM = 0.5), a_k the A_0
components in the spatial eigenframe; a-Gaussian weights Q_k = eps e^{-2i alpha}
+ i LAM e^{2i(beta-alpha)} T_k - i (gam/2) e^{-2i alpha}, alpha = 3 pi u/8, beta = pi u/8,
T_k = [w2+w3, w1+w3, w1+w2].

Insertion modes (parameter `mode`):
 bare    : O = 1 (exactly the 053 path).
 trivial : O = Tr I = 2 (k = 0 check; must give Z ratio exactly 2 vs bare).
 exact   : O_k = 2 cos(gc |a|), gc = e^{3 pi i/8} r0/2 (exact: insertion depends only on
           |a|, SO(3)_a x SO(9) invariant, so it inserts exactly in this chart). Taylor
           series in (a^2)^m integrated termwise against the anisotropic a-Gaussian with
           polynomial Pfaffian insertion (D0 + sum r_k a_k^2)^p, p=4. Stacked recursion
             m c_m = sum_{t=1}^m c_{m-t} sigma_t,  sigma_t = sum_k (n_k+1/2) Q_k^{-t},
             T_n = 2 sum_m (-gc^2)^m m!/(2m)! c_m.
           Used ONLY at eps >= 0.1: the cos Taylor partial sums overshoot like
           exp(|gc^2| sum_k |1/Q_k| / 2), exhausting float64 at smaller eps (documented
           in the output; this is why the factorized surrogate below is used at small eps).
 factor  : FACTORIZED surrogate for the same insertion: 2 cos(gc |a_1|) along the k-soft
           direction a_1 (the axis paired with k^0; Q_1 as above), transverse directions
           untouched. All a-integrals then analytic:
             I_j(Q) = (-1)^j d^j/dQ^j [ 2 sqrt(pi) Q^{-1/2} e^{-gc^2/(4Q)} ]
           (sympy-generated polynomials in x = 1/Q times the branch factor), reducing to
           2x the bare 053 path as gc -> 0. Asymptotically exact for the growth exponent
           at the rank-1 corner (Q_1 -> eps e^{-2i alpha}, transverse widths hard), and
           validated numerically against mode=exact at eps in {1, 0.3, 0.1}.

Closed-form branch prediction (script 1), at the corner Lambda = w2+w3 = 0,
Q_1 = e^{-2i alpha}(eps - i gam/2):
  gam = 0:      Re[-gc^2/(4 Q_1)] = r0^2 cos(3 pi u/4 - pi/4)/(16 eps)   (grows as eps->0)
  gam<0 fixed:  -> r0^2 sin(3 pi u/4 - pi/4)/(8 |gam|)                   (saturates; blows
                 up as gam -> 0-, so the fixed-gam<0 chain is NON-UNIFORM as gam -> 0-)

Experiments:
 E0  bare vs trivial at u=1: |Z| ratio exactly 2 (factor 2 = Tr I normalisation).
 E1  u=0, gam=0, r0 in {1,2}: exact vs factorized at eps in {1,0.3,0.1}; then factorized
     eps ladder down to 0.003; fit ln(|Z_inserted|/|Z_bare|) = A/eps + B (ratio cancels the
     eps-polynomial prefactors); compare A to r0^2 cos(3piu/4-pi/4)/16
     = r0^2/(16 sqrt2) at u=0 (0.04419 r0^2); report exact-series truncation evidence.
 E2  u=0.6, r0=1: gam = 0 (growing, predicted slope cos(3piu/4-pi/4)/16 = 0.05057) vs
     gam = -0.2, -0.05 (saturating, predicted corner factor exp(r0^2 sin(3piu/4-pi/4)/(8|gam|))
     = 1.44 / 4.35): gamma -> 0- non-uniformity in the model (rank-2 avenue).
 E3  u=0 pure-spatial carrier: cb = sin(pi/8)/2 (054-style cosh modulus proxy for slice k
     with r0 = 0), signed |Z| vs modulus diagnostic Zmod, eps ladder.
Run:  python -I n2_slice_r1.py   (tee to n2_slice_r1.out; ~10-20 min on one core)
"""
import numpy as np, math, itertools, time
import sympy as sp
from scipy.special import gamma as Gam
LAM = 0.5

def nodes(n, lo, hi):
    x, w = np.polynomial.legendre.leggauss(n)
    return 0.5 * (hi - lo) * x + 0.5 * (hi + lo), 0.5 * (hi - lo) * w

def branch_qpolys(gc2, jmax=4):
    """q_j(x) with I_j = B(x) q_j(x), B(x) = 2 sqrt(pi) x^{1/2} e^{-gc2 x/4}, x = 1/Q,
    I_j = (-1)^j d^j/dQ^j B  (i.e. I_{j+1} = -x^2 d/dx (B q_j)). Returns list of ascending
    complex coefficient arrays (numeric gc2)."""
    x = sp.Symbol('x')
    g = sp.nsimplify(complex(gc2))
    B = 2 * sp.sqrt(sp.pi) * sp.sqrt(x) * sp.exp(-g * x / 4)
    qs = [sp.Integer(1)]
    for j in range(jmax):
        qn = sp.expand(x**2 * (sp.diff(B * qs[-1], x) / B))  # I_{j+1} = (-1)d_Q(B q_j) = +x^2 d_x(B q_j)
        qs.append(qn)
    out = []
    for q in qs:
        p = sp.Poly(sp.expand(q), x)
        cf = [complex(c) for c in p.all_coeffs()[::-1]]  # ascending
        out.append(np.array(cf, dtype=np.complex128))
    return out

def compute(D, fermions, eps, u, gam=0.0, mode='bare', r0=1.0, M=64, tol=1e-9,
            cb=0.0, ca=0.0, wmask=1.0, ns=96, nv=44, nz=44, srange=None,
            vmax=40., zmax=36., chunk=4):
    """Reduced integral. mode in {'bare','trivial','exact','factor'}. Returns dict with
    Z, Zmod, maxterm (largest series term kept, truncation evidence), Mused."""
    d = D - 1; p = (D // 2 - 1) if fermions else 0
    al = 3 * np.pi * u / 8; be = np.pi * u / 8
    ph_meas = np.exp(1j * (3 * d * be - 3 * al))
    gc2 = (np.exp(1j * 3 * np.pi / 8) ** 2) * (r0 ** 2) / 4.0 if mode in ('exact', 'factor') else None
    qlist = branch_qpolys(gc2, p) if mode == 'factor' else None
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
        elif mode == 'factor':
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
        else:  # exact Taylor series
            npts = D0.size
            Aco = np.array([[n[k] + 0.5 for k in range(3)] for n in terms], dtype=np.float64)
            Ppow = [[np.ones_like(D0)] for _ in range(3)]
            for k in range(3):
                for tt in range(1, M + 1):
                    Ppow[k].append(Ppow[k][-1] / Q[k])
            cstack = [np.ones((nt, npts), dtype=np.complex128)]  # c_0 = 1 (Gr/Q^{1/2} factors live in base0 and the n-loop)
            Tn_st = np.zeros((nt, npts), dtype=np.complex128) + 2.0
            stcache = [None] * (M + 1)
            for m in range(1, M + 1):
                sig = np.zeros((nt, npts), dtype=np.complex128)
                for tt in range(1, m + 1):
                    if stcache[tt] is None:
                        stcache[tt] = (Aco[:, 0:1] * Ppow[0][tt].ravel()[None, :] +
                                       Aco[:, 1:2] * Ppow[1][tt].ravel()[None, :] +
                                       Aco[:, 2:3] * Ppow[2][tt].ravel()[None, :])
                    sig += stcache[tt] * cstack[m - tt]
                cm = sig / m
                cstack.append(cm)
                coefm = 2.0 * (-gc2) ** m * math.factorial(m) / math.factorial(2 * m)
                tm = coefm * cm
                Tn_st += tm
                mt = abs(coefm) * float(np.max(np.abs(cm)))
                if mt > maxterm: maxterm = mt
                Mused = m
                if mt < tol * float(np.max(np.abs(Tn_st))) and m >= 4:
                    break
            base0 = Gam(0.5) ** 3 * Q[0] ** (-0.5) * Q[1] ** (-0.5) * Q[2] ** (-0.5)
            tot = np.zeros_like(D0)
            for i, n in enumerate(terms):
                n0 = p - sum(n)
                Tn = Tn_st[i].reshape(D0.shape)
                tot = tot + coefn[i] * Dpow[n0] * rpow[0][n[0]] * rpow[1][n[1]] * rpow[2][n[2]] \
                      * (Gr[n[0]] * Q[0] ** (-n[0])) * (Gr[n[1]] * Q[1] ** (-n[1])) * (Gr[n[2]] * Q[2] ** (-n[2])) * Tn
            tot = tot * base0
        F = np.ones_like(D0)
        if cb != 0.0: F = F * np.cosh(cb * np.sqrt(w1))
        if ca != 0.0: F = F * np.cosh(ca / np.sqrt(w2 + w3))
        if (ca != 0.0 or cb != 0.0) and wmask is not None:
            F = np.where(w1 > wmask, F, 1.0)
        integ = dens * ex * tot * F
        Z += np.sum(integ)
        Zmod += np.sum(np.abs(integ))
    return {'Z': Z * ph_meas, 'Zmod': abs(Zmod * ph_meas), 'maxterm': maxterm, 'Mused': Mused}

def srng(eps, smax=14.0):
    return (-8.0, min(np.log(80.0 / eps), smax)) if eps > 0 else (-8.0, smax)

def main():
    np.seterr(all='ignore')
    G = dict(ns=96, nv=44, nz=44, vmax=40., zmax=36., chunk=4)
    GS = dict(ns=64, nv=32, nz=32, vmax=40., zmax=36., chunk=4)  # exact-series grids
    t0 = time.time()
    print("=== E0: normalization checks ===")
    A = compute(10, True, 0.0, 1.0, mode='bare', srange=(-10., 20.), **G)
    B = compute(10, True, 0.0, 1.0, mode='trivial', srange=(-10., 20.), **G)
    print("  u=1: bare |Z|=%.8e ph/pi=%.6f ; trivial |Z|=%.8e ; ratio trivial/bare=%.10f (must be 2 = Tr I)" %
          (abs(A['Z']), np.angle(A['Z']) / np.pi, abs(B['Z']), abs(B['Z'] / A['Z'])))
    A2 = compute(10, True, 0.01, 1.0, mode='bare', srange=(-8., 14.), **G)
    F0 = compute(10, True, 0.01, 1.0, mode='factor', r0=1e-6, srange=(-8., 14.), **G)
    E0x = compute(10, True, 0.01, 1.0, mode='exact', r0=1e-6, M=64, srange=(-8., 14.), **GS)
    print("  u=1 eps=0.01 r0=1e-6: factor/bare=%.10f exact/bare=%.10f (both -> 2: O_k -> Tr I as k -> 0)" %
          (abs(F0['Z'] / A2['Z']), abs(E0x['Z'] / A2['Z'])))
    print("=== E1: u=0, gam=0: exact vs factorized insertion; ratio growth vs eps ===")
    esx = (1.0, 0.3, 0.1)
    esf = (1.0, 0.3, 0.1, 0.03, 0.01, 0.003)
    for r0 in (1.0, 2.0):
        for eps in esx:
            Ae = compute(10, True, eps, 0.0, mode='bare', srange=srng(eps), **G)
            Re_ = compute(10, True, eps, 0.0, mode='exact', r0=r0, M=96, srange=srng(eps), **GS)
            Rf = compute(10, True, eps, 0.0, mode='factor', r0=r0, srange=srng(eps), **G)
            print("  r0=%.1f eps=%.2f: bare %.4e ; exact %.4e (maxterm %.1e M=%d) ratio %.3e ; factor %.4e ratio %.3e" %
                  (r0, eps, abs(Ae['Z']), abs(Re_['Z']), Re_['maxterm'], Re_['Mused'],
                   abs(Re_['Z'] / Ae['Z']), abs(Rf['Z']), abs(Rf['Z'] / Ae['Z'])))
        rb, rf = [], []
        for eps in esf:
            Ae = compute(10, True, eps, 0.0, mode='bare', srange=srng(eps), **G)
            Rf = compute(10, True, eps, 0.0, mode='factor', r0=r0, srange=srng(eps), **G)
            rb.append(abs(Ae['Z'])); rf.append(abs(Rf['Z']))
        ratio = [rf[i] / rb[i] for i in range(len(esf))]
        print("  r0=%.1f factor/bare |Z| ratio (eps=1,0.3,0.1,0.03,0.01,0.003): " % r0 +
              " ".join("%.4e" % x for x in ratio))
        lg = np.log(ratio); inv = 1.0 / np.array(esf)
        Afit = np.polyfit(inv, lg, 1)
        Afit3 = np.polyfit(inv[3:], lg[3:], 1)
        print("       fit ln ratio = %.4f*(1/eps)+%.3f (all) ; %.4f (eps<=0.03)  predicted A = r0^2 cos(3piu/4-pi/4)/16 = %.4f" %
              (Afit[0], Afit[1], Afit3[0], r0**2 * np.cos(3 * np.pi * 0.0 / 4 - np.pi / 4) / 16))
    print("=== E2: u=0.6, r0=1, factorized vs bare ratio: gam=0 growth vs gam<0 saturation ===")
    Zg0 = None
    for gam in (0.0, -0.2, -0.05):
        rows = []
        for eps in esf[2:]:
            Ae = compute(10, True, eps, 0.6, mode='bare', srange=srng(eps), **G)
            Rf = compute(10, True, eps, 0.6, gam=gam, mode='factor', r0=1.0, srange=srng(eps), **G)
            rows.append(abs(Rf['Z'] / Ae['Z']))
        if gam == 0.0: Zg0 = rows
        print("  gam=%+.2f |Z_fac|/|Z_bare| (eps=0.1,0.03,0.01,0.003): " % gam + " ".join("%.4e" % x for x in rows))
        if gam == 0.0:
            lg = np.log(rows); inv = 1.0 / np.array(esf[2:])
            Afit = np.polyfit(inv, lg, 1)
            print("       fit slope (1/eps) %.4f ; predicted cos(3piu/4-pi/4)/16 = %.4f" %
                  (Afit[0], np.cos(3 * np.pi * 0.6 / 4 - np.pi / 4) / 16))
        else:
            pred = np.exp(np.sin(3 * np.pi * 0.6 / 4 - np.pi / 4) / (8 * abs(gam)))
            rr = [rows[i] / Zg0[i] for i in range(len(rows))]
            print("       predicted saturation factor vs gam=0: exp(sin(3piu/4-pi/4)/(8|gam|)) = %.3f ; measured ratio %s" %
                  (pred, " ".join("%.3f" % x for x in rr)))
    print("=== E3: u=0 pure-spatial carrier proxy cb = sin(pi/8)/2 (054 machinery, |O|>=1 modulus) ===")
    cbv = np.sin(np.pi / 8) / 2
    for eps in (1.0, 0.3, 0.1, 0.03):
        R = compute(10, True, eps, 0.0, mode='bare', cb=cbv, srange=srng(eps), **G)
        A0 = compute(10, True, eps, 0.0, mode='bare', srange=srng(eps), **G)
        print("  eps=%.2f |Z|=%.4e (bare %.4e, ratio %.3e) Zmod=%.4e (Zmod/|Z| %.3e)" %
              (eps, abs(R['Z']), abs(A0['Z']), abs(R['Z'] / A0['Z']), R['Zmod'], R['Zmod'] / abs(R['Z'])))
    print("done in %.1f s" % (time.time() - t0))

if __name__ == "__main__":
    main()
