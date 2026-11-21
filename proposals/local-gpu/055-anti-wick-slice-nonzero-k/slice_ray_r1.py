#!/usr/bin/env python3
"""Proposal 055 r1, script 1: anti-Wick-slice ray structure at u=0 and exact branch factors.

Scope: the commuting-ray (rank-one) model of proposal 054 at contour u=0, for slice k,
k^0 = e^{3 pi i/8} r0, k^i = e^{-pi i/8} r^i (r0 real, r in R^9, b=|r|), plus the exact
a-direction branch integral used by script 2 (reduced N=2 model normalization).

Checks:
 (1) Cauchy-Binet identity at N=2: rho_X^2 = k^mu k^nu G_munu with G_munu = sum_a A^a_mu A^a_nu
     equals sum_a (k^mu A^a_mu)^2 (symbolic a=1..3, 4 dims x 3 a-indices, plus a non-tautological
     random complex mpmath check: (lam_+-lam_-)^2 = -4 det(k.A) vs sum_{a=1..3}(k^mu A^a_mu)^2); and at u=1 with slice k the
     combination k^mu A_mu(u=1) has coefficients 1 on (A~0, A~i): Hermitian, rho_X real,
     |O_k| = |2 cos(rho_X/2)| <= 2 (the 054 RHS boundedness mechanism).
 (2) Growth functional at u=0: kappa(rho_hat) = k.rho_hat = u_k.rho_hat + i v_k.rho_hat with
     u_k = (cos(3pi/8) r0, cos(pi/8) r), v_k = (sin(3pi/8) r0, -sin(pi/8) r).
     B = v v^T - u u^T has rank <= 2, supported on span(e0, e_r), with 2x2 block
     (1/sqrt2) [[r0^2, -r0 b], [-r0 b, -b^2]], and
     lambda_max = [(r0^2 - b^2) + sqrt(r0^4 + 6 r0^2 b^2 + b^4)] / (2 sqrt2).
     Sign lemma: lambda_max > 0 iff r0 != 0; lambda_max = 0 at r0 = 0.
     054 criterion: strict growth ray exists iff lambda_max(B) > 0.
     So inside the slice: r0 != 0 (temporal/mixed) -> strict growth ray; r0 = 0 (pure
     spatial) -> no strict growth ray; neutral set {kappa=0} = {rho0 free, r.rho=0}, dim 9,
     off it |Im kappa|^2 - |Re kappa|^2 = -cos(pi/4) (r.rho)^2 / b^2-type < 0 (decay).
 (3) Exact branch integral in code normalization (a-Gaussian e^{-Q a^2}, insertion
     2 cos(gamma_c |a|), gamma_c = e^{3 pi i/8} r0/2):
       int e^{-Q a^2} 2cos(gamma_c|a|) da = 2 sqrt(pi/Q) e^{-gamma_c^2/(4Q)} (complex closed form),
     growth exponent at Q = eps real: -Re(gamma_c^2)/(4 eps) = r0^2/(16 sqrt2 eps).
     Cross-check against the 054 ray formula (b^2-a^2)/(8 c eps) with O = 2cos(kappa rho/2).
Run:  python -I slice_ray_r1.py  (r2: tee to slice_ray_r2.out; F1/F5/F7: full Pauli range a=1..3, non-tautological matrix check, corrected sec.3 label)
"""
import numpy as np, sympy as sp, mpmath as mp

mp.mp.dps = 50

def sec1():
    print("=== (1) Cauchy-Binet identity (full Pauli range a=1..3) and u=1 boundedness ===")
    w1, w2, w3, lam = sp.symbols('w1 w2 w3 lambda')
    s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]])
    M = (w1 * s1 + w2 * s2 + w3 * s3) / 2
    ch = sp.expand((lam * sp.eye(2) - M).det())
    print("  charpoly(lam I - sum w_a sigma^a/2) - (lam^2 - (w1^2+w2^2+w3^2)/4) =",
          sp.simplify(ch - (lam**2 - (w1**2 + w2**2 + w3**2) / 4)))
    print("  (=> eigenvalues +-sqrt(sum_{a=1..3} w_a^2)/2; Tr exp(iM)=2cos(sqrt(sum w^2)/2), branch-independent)")
    # NON-tautological check (F7): matrix side (rho_X^2 = (lam_+-lam_-)^2 = -4 det(k.A), traceless)
    # vs contraction side sum_{a=1..3}(k^mu A^a_mu)^2, at random complex data, dps=50.
    # NOTE mpmath 1.3.0: mp.matrix(m,n,S) (3-arg) silently builds a ZERO matrix for list/dict/callable S;
    # the working form is mp.matrix([row1, row2]) (single nested list of rows).
    ss = [mp.matrix([r[:2], r[2:]]) for r in ([0,1,1,0], [0,1j,-1j,0], [1,0,0,-1])]
    rng = np.random.default_rng(11)
    worst = mp.mpf(0); worst2 = mp.mpf(0)
    mpc = lambda z: mp.mpc(float(np.real(z)), float(np.imag(z)))  # explicit numpy->mpc conversion
    for _ in range(8):
        A = rng.normal(size=(3, 4)) + 1j * rng.normal(size=(3, 4))
        k = rng.normal(size=4) + 1j * rng.normal(size=4)
        km = [mpc(k[mu]) for mu in range(4)]
        Am = [[mpc(A[a][mu]) for mu in range(4)] for a in range(3)]
        Mm = mp.zeros(2, 2)
        for mu in range(4):
            for a in range(3):
                Mm += km[mu] * Am[a][mu] * ss[a] / 2
        rho2 = -4 * mp.det(Mm)  # (lam_+ - lam_-)^2 since tr M = 0
        contr = sum(sum(km[mu] * Am[a][mu] for mu in range(4))**2 for a in range(3))
        d = abs(rho2 - contr) / max(mp.mpf(1), abs(contr))
        worst = max(worst, d)
        contr12 = sum(sum(km[mu] * Am[a][mu] for mu in range(4))**2 for a in range(2))
        worst2 = max(worst2, abs(rho2 - contr12) / max(mp.mpf(1), abs(rho2)))
    print("  max rel |rho_X^2 - sum_{a=1..3}(k.A^a)^2| over 8 random complex trials:", mp.nstr(worst, 4))
    print("  same truncated to a=1..2 fails generically, max rel dev:", mp.nstr(worst2, 4))
    # explicit counterexample to the a=1..2 truncation (gatekeeper F1): A_0 = sigma^3/2, k^0 = 1
    Mx = mp.matrix([[mp.mpf('0.5'), 0], [0, mp.mpf('-0.5')]])
    print("  counterexample a=1..2: A_0=sigma^3/2, k^0=1: rho_X^2 = -4det =", mp.nstr(-4 * mp.det(Mx), 4),
          " but sum_{a=1..2} = 0 -> truncated identity FALSE")
    # pure-algebra expansion check (algebraic identity once G is defined by the same sum, kept
    # for completeness at a=1..3; the substantive check is the matrix-side comparison above)
    na, nmu = 3, 4
    X = sp.symbols('X0:%d' % (na * nmu))
    kk = sp.symbols('k0:%d' % nmu)
    Aa = [[X[a * nmu + m] for m in range(nmu)] for a in range(na)]
    G = [[sum(Aa[a][m] * Aa[a][n] for a in range(na)) for n in range(nmu)] for m in range(nmu)]
    rho2 = sum(kk[m] * kk[n] * G[m][n] for m in range(nmu) for n in range(nmu))
    cb = sum(sum(kk[m] * Aa[a][m] for m in range(nmu))**2 for a in range(na))
    print("  rho_X^2 - sum_{a=1..3}(k^mu A^a_mu)^2 simplified (a-poly identity):", sp.simplify(sp.expand(rho2 - cb)))
    r0, r1 = sp.symbols('r0 r1', real=True)
    k0s = sp.exp(sp.I * sp.Rational(3, 8) * sp.pi) * r0
    k1s = sp.exp(-sp.I * sp.pi / 8) * r1
    A0f = sp.exp(-sp.I * sp.Rational(3, 8) * sp.pi)   # contour factor on A~0 at u=1
    A1f = sp.exp(sp.I * sp.pi / 8)                    # contour factor on A~i at u=1
    print("  k^0 A~0 coefficient at u=1:", sp.simplify(k0s * A0f), "; k^1 A~1 coefficient:", sp.simplify(k1s * A1f))
    print("  (both equal the real r-component: r^mu A~_mu Hermitian, rho_X real, |2cos(rho_X/2)| <= 2)")

def sec2():
    print("=== (2) growth functional B = v v^T - u u^T at u=0 for slice k (sympy + numeric) ===")
    r0, b = sp.symbols('r0 b', nonnegative=True)
    ub = sp.Matrix([sp.cos(sp.Rational(3, 8) * sp.pi) * r0, sp.cos(sp.pi / 8) * b])
    vb = sp.Matrix([sp.sin(sp.Rational(3, 8) * sp.pi) * r0, -sp.sin(sp.pi / 8) * b])
    Bb = sp.expand(vb * vb.T - ub * ub.T)
    print("  2x2 block (basis e0, e_r), entries times sqrt(2):",
          [sp.nsimplify(sp.simplify(e * sp.sqrt(2))) for e in Bb])
    lam_formula = ((r0**2 - b**2) + sp.sqrt(r0**4 + 6 * r0**2 * b**2 + b**4)) / (2 * sp.sqrt(2))
    diffs = []
    for t in [(2, 1), (3, 2), (1, 5), (5, 1), (1, 1)]:
        ev = [sp.N(x.subs({r0: t[0], b: t[1]})) for x in Bb.eigenvals()]
        diffs.append(max(ev) - sp.N(lam_formula.subs({r0: t[0], b: t[1]})))
    print("  formula vs sympy eigenvalues max-diff:", [float(d) for d in diffs])
    print("  sign lemma (lambda_max > 0 iff r0 > 0):")
    for t in [(0, 1), (0, 3), (1, 0), (1, 1), (1, 5), (5, 1), (sp.Rational(1, 1000), 1)]:
        print("    r0=%s b=%s lambda_max = %s" % (t[0], t[1], sp.N(lam_formula.subs({r0: t[0], b: t[1]}))))
    # algebraic sign proof: sqrt(r0^4+6r0^2b^2+b^4) > b^2-r0^2 squared difference
    print("  square-difference (8 r0^2 b^2):", sp.expand((r0**4 + 6*r0**2*b**2 + b**4) - (b**2 - r0**2)**2))
    cPn, sPn, cMn, sMn = np.cos(3*np.pi/8), np.sin(3*np.pi/8), np.cos(np.pi/8), np.sin(np.pi/8)
    rng = np.random.default_rng(5)
    for (r0v, bv) in [(1.0, 0.0), (0.0, 1.0), (1.0, 1.0), (0.4, 2.0)]:
        e9 = rng.normal(size=9); e9 /= np.linalg.norm(e9)
        uvec = np.zeros(10); vvec = np.zeros(10)
        uvec[0] = cPn * r0v; vvec[0] = sPn * r0v
        uvec[1:] = cMn * bv * e9; vvec[1:] = -sMn * bv * e9
        Bn = np.outer(vvec, vvec) - np.outer(uvec, uvec)
        lN = np.linalg.eigvalsh(Bn)
        lamf = ((r0v**2 - bv**2) + np.sqrt((r0v**2 - bv**2)**2 + 8 * r0v**2 * bv**2)) / (2*np.sqrt(2))
        rk = np.linalg.matrix_rank(Bn, tol=1e-10)
        print("  numeric r0=%.2f b=%.2f: lambda_max(num)=%.6f formula=%.6f rank=%d nullspace dim=%d"
              % (r0v, bv, lN[-1], lamf, rk, 10 - rk))
    # r0 = 0: neutral 9-plane {r.rho=0}; decay off it
    bv = 2.5
    uvec = np.zeros(10); vvec = np.zeros(10)
    e10 = np.zeros(10); e10[1] = 1.0
    uvec[1:] = cMn * bv * e10[1:]; vvec[1:] = -sMn * bv * e10[1:]
    Bn = np.outer(vvec, vvec) - np.outer(uvec, uvec)
    t0 = np.zeros(10); t0[0] = 1.0
    orth = np.zeros(10); orth[2] = 1.0
    print("  r0=0: B[e0,e0]=%.2e B[ehat,ehat]=%.6f (=-cos(pi/4)b^2=%.6f) B[orth]=%.2e"
          % (t0 @ Bn @ t0, e10 @ Bn @ e10, -np.cos(np.pi/4) * bv**2, orth @ Bn @ orth))
    print("  r0=0: kappa=0 iff r.rho=0 (9-dim neutral subspace); off it B[rhohat,rhohhat]=-cos(pi/4)(r.rhohat)^2<0")

def sec3():
    print("=== (3) exact branch integral int e^{-Q a^2} 2cos(gamma_c|a|) da ===")
    # exact: int_{-inf}^{inf} e^{-Qa^2} 2cos(gc|a|) da = 2 sqrt(pi/Q) e^{-gc^2/(4Q)} (complex;
    # erf terms cancel between the two branches; modulus growth Re[-gc^2/(4Q)] at Q=eps real)
    closed = lambda Q, gc: 2 * mp.sqrt(mp.pi / Q) * mp.e**(-gc**2 / (4 * Q))
    def series(Q, gc, M=400):
        # int e^{-Qa^2} 2cos(gc|a|) da = sum_m 2(-1)^m gc^{2m}/(2m)! * Gamma(m+1/2) Q^{-m-1/2}
        s = mp.mpc(0)
        for m in range(M + 1):
            s += 2 * (-1)**m * gc**(2*m) / mp.factorial(2*m) * mp.gamma(mp.mpf(m) + mp.mpf(1)/2) * Q**(-mp.mpf(m) - mp.mpf(1)/2)
        return s
    for (Q, gc) in [(0.03 + 0.2j, mp.e**(mp.j*3*mp.pi/8) / 2), (1.0 + 0j, mp.e**(mp.j*3*mp.pi/8)),
                    (0.01 + 0.05j, mp.e**(mp.j*3*mp.pi/8))]:
        ser = series(Q, gc)
        print("  Q=%s: |series-closed|/|closed| = %.3e  (M=400)" % (complex(Q), abs(ser - closed(Q, gc)) / abs(closed(Q, gc))))
    # robust finite-interval quadrature at moderate width
    f = lambda a: mp.e**(-1 * a**2) * 2 * mp.cos(mp.e**(mp.j*3*mp.pi/8) * abs(a))
    q = mp.quad(f, [i*mp.mpf(0.5) for i in range(-80, 81)])
    print("  Q=1: series=%s closed=%s" % (series(mp.mpf(1), mp.e**(mp.j*3*mp.pi/8)), closed(mp.mpf(1), mp.e**(mp.j*3*mp.pi/8))))
    print("  Q=1 quadrature vs closed: rel err %.3e" % (abs(q - closed(mp.mpf(1), mp.e**(mp.j*3*mp.pi/8))) / abs(closed(mp.mpf(1), mp.e**(mp.j*3*mp.pi/8)))))
    gc2 = (mp.e**(mp.j*3*mp.pi/8) / 2)**2
    print("  r0=1: -Re(gamma_c^2) = %.10f  r0^2/(4 sqrt2) = %.10f" % (-mp.re(gc2), 1 / (4 * mp.sqrt(2))))
    ba = mp.sin(3*mp.pi/8)**2 - mp.cos(3*mp.pi/8)**2
    print("  054 ray formula exponent (b^2-a^2)/(8c eps), b^2-a^2 = r0^2/sqrt2 = %.10f, c=1/2: %.10f/eps"
          % (ba, ba / 4.0))
    print("  code-normalization exponent: -Re(gamma_c^2)/(4 eps) = %.10f/eps (ratio 4 vs ray value; Pauli normalization, (r0)^2 scaling)"
          % (-mp.re(gc2) / 4))
    print("done")

if __name__ == "__main__":
    sec1(); sec2(); sec3()
