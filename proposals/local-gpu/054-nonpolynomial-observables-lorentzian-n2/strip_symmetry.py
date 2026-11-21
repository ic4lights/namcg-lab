#!/usr/bin/env python3
"""Symbolic checks for proposal 054 (exponential probes Tr e^{i k.A} at N=2).

(1) su(2): for X = z_a sigma^a / 2 with z in C^3: X^2 = (z.z)/4 I exactly;
    Tr X^{2m+1} = 0 and Tr X^{2m} = 2 (z.z/4)^m, hence Tr e^{iX} = 2 cos(rho/2),
    rho^2 = z.z (branch-invariant); |2cos((x+iy)/2)|^2 = 4(cos^2(x/2)+sinh^2(y/2));
    z.z invariant under complex-orthogonal rotations.
(2) Flat-locus growth functional v_u(rho;k) = Im( k0 e^{-3 pi i u/8} rho0
    + e^{pi i u/8} k.rho ) with k complex (kR + i kI):
    - for u=1 the zero set in k (real 8-dim coefficients) is exactly the
      "anti-Wick" slice k0 = c0 e^{3 pi i/8}, k_i = c_i e^{-pi i/8} (real c), dim 4;
    - for u=0 the zero set is exactly k real (dim 4);
    - for u in (0,1] the zero set restricted to REAL k is {k=0}.
(3) v_1(real k) = -sin(3pi/8) k0 rho0 + sin(pi/8) k.rho, sign flips with rho.
(4) Mass real part on R_u: Re(iS_gamma) = gamma/(2g^2)[sin(3pi u/4) A0t^2
    + sin(pi u/4) sum Ai_t^2]; at u=1 common coefficient gamma sqrt2/(4 g^2);
    at u=0 pure phase. (S_gamma = -(gamma/2g^2) A_mu A^mu, eta=diag(-1,1,1,1),
    same convention as 053.)
Run:  python -I strip_symmetry.py
"""
import sympy as sp
import mpmath as mp

mp.mp.dps = 40

def main():
    ok = True
    def chk(name, cond):
        nonlocal ok
        print(("PASS " if cond else "FAIL ") + name)
        ok = ok and bool(cond)

    # ---- (1) su(2) ----
    z1, z2, z3 = sp.symbols('z1 z2 z3', complex=True)
    sg1 = sp.Matrix([[0, 1], [1, 0]]); sg2 = sp.Matrix([[0, -sp.I], [sp.I, 0]]); sg3 = sp.Matrix([[1, 0], [0, -1]])
    X = (z1 * sg1 + z2 * sg2 + z3 * sg3) / 2
    r2 = z1**2 + z2**2 + z3**2
    X2 = sp.simplify(X * X - (r2 / 4) * sp.eye(2))
    chk("(1a) X^2 = (z.z)/4 * I exactly", all(sp.simplify(X2[i, j]) == 0 for i in range(2) for j in range(2)))
    trp = []
    for m in range(7):
        trp.append(sp.simplify(sp.expand(sp.Trace(X**(2 * m)) - 2 * (r2 / 4)**m)) == 0)
        D = sp.expand(X**(2 * m + 1) - (r2 / 4)**m * X)
        trp.append(all(sp.expand(D[i, j]) == 0 for i in range(2) for j in range(2)))
    chk("(1b) Tr X^{2m} = 2(z.z/4)^m (m<=6) and X^{2m+1} = (z.z/4)^m X entrywise (m<=6), Tr X = 0",
        all(trp) and sp.simplify(sp.Trace(X)) == 0)
    # numeric high-precision check of the closed form for random complex z
    import random
    random.seed(4)
    errs = []
    for _ in range(5):
        zv = [mp.mpc(random.uniform(-3, 3), random.uniform(-3, 3)) for _ in range(3)]
        zmat = mp.matrix(2, 2)
        zmat[0, 0] = zv[2] / 2; zmat[0, 1] = (zv[0] - 1j * zv[1]) / 2
        zmat[1, 0] = (zv[0] + 1j * zv[1]) / 2; zmat[1, 1] = -zv[2] / 2
        trnum = sum((1j * zmat)**n / mp.factorial(n) for n in range(60))
        rho = mp.sqrt(sum(t * t for t in zv))
        cf = 2 * mp.cos(rho / 2)
        cf2 = 2 * mp.cos(-rho / 2)
        errs.append(min(abs(trnum[0, 0] + trnum[1, 1] - cf), abs(trnum[0, 0] + trnum[1, 1] - cf2)))
    chk("(1c) Tr e^{iX} == 2cos(rho/2) numerically (dps=40, series to n=59, max err < 1e-25)",
        max(errs) < 1e-25)
    x, y = sp.symbols('x y', real=True)
    Ld = sp.expand_complex(sp.Abs(2 * sp.cos((x + sp.I * y) / 2))**2)
    R = 4 * (sp.cos(x / 2)**2 + sp.sinh(y / 2)**2)
    chk("(1d) |2cos((x+iy)/2)|^2 = 4(cos^2(x/2)+sinh^2(y/2))", sp.simplify(sp.expand_trig(sp.re(Ld) - R)) == 0)
    th = sp.symbols('theta')
    c, s = sp.cos(th), sp.sin(th)
    w1 = c * z1 - s * z2; w2 = s * z1 + c * z2; w3 = z3
    chk("(1e) z.z invariant under complex-orthogonal rotation of z", sp.simplify(w1**2 + w2**2 + w3**2 - r2) == 0)

    # ---- (2) growth functional: full zero sets ----
    kR = sp.symbols('kr0 kr1 kr2 kr3', real=True)
    kI = sp.symbols('ki0 ki1 ki2 ki3', real=True)
    rr = sp.symbols('rho0 rho1 rho2 rho3', real=True)
    kv = [kR[i] + sp.I * kI[i] for i in range(4)]

    def coeffs(u):
        ph = sp.exp(-3 * sp.pi * sp.I * u / 8); pI = sp.exp(sp.pi * sp.I * u / 8)
        e = sp.expand(sp.im(ph * kv[0] * rr[0] + pI * (kv[1] * rr[1] + kv[2] * rr[2] + kv[3] * rr[3])))
        return [sp.simplify(sp.diff(e, r)) for r in rr], e

    unks = list(kR) + list(kI)
    for u, tag in [(sp.Integer(0), 'u=0'), (sp.Rational(1, 2), 'u=1/2'), (sp.Integer(1), 'u=1')]:
        cf, e = coeffs(u)
        sol = sp.linsolve(cf, unks)
        ndim = len(unks) - len(cf) + (0 if sp.nsimplify(0) else 0)
        # verify solution space dimension via rank
        Mm = sp.Matrix([[sp.simplify(sp.diff(c, v)) for v in unks] for c in cf])
        rank = Mm.rank()
        chk("(2a) zero set of v_%s has real dimension %d (rank %d)" % (tag, 8 - rank, rank), rank == 4)
        # anti-Wick family at u=1; real family at u=0
        cpar = sp.symbols('c0 c1 c2 c3', real=True)
        if u == 1:
            fam = [cpar[0] * sp.exp(3 * sp.pi * sp.I / 8)] + [cpar[i] * sp.exp(-sp.pi * sp.I / 8) for i in (1, 2, 3)]
        elif u == 0:
            fam = list(cpar)
        else:
            fam = None
        if fam:
            sub = {kv[i]: fam[i] for i in range(4)}
            # substitute into the expanded expression using kr/ki replacement
            rep = {}
            for i in range(4):
                re_ = sp.re(fam[i]); im_ = sp.im(fam[i])
                rep[kR[i]] = re_; rep[kI[i]] = im_
            chk("(2b) v_%s vanishes identically on the claimed 4-dim family" % tag,
                all(sp.simplify(cc.subs(rep)) == 0 for cc in cf))
    # real-k restriction for u in (0,1]: only k=0
    e1 = coeffs(1)[1]
    Mm1 = sp.Matrix([[sp.simplify(sp.diff(c, v)) for v in list(kR) + list(kI)] for c in coeffs(1)[0]])
    # restrict kI=0 and check remaining rank on kR is 4
    subR = {kI[i]: 0 for i in range(4)}
    Mr = sp.Matrix([[sp.simplify(sp.diff(c.subs(subR), v)) for v in kR] for c in coeffs(1)[0]])
    chk("(2c) v_1 restricted to real k vanishes for all rho only at k=0 (rank 4)", Mr.rank() == 4)
    Mr2 = sp.Matrix([[sp.simplify(sp.diff(c.subs(subR), v)) for v in kR] for c in coeffs(sp.Rational(1, 2))[0]])
    chk("(2d) same at u=1/2 (rank 4)", Mr2.rank() == 4)
    Mrh = sp.Matrix([[sp.simplify(sp.diff(c.subs(subR), v)) for v in kR] for c in coeffs(sp.Rational(1, 4))[0]])
    chk("(2e) same at u=1/4 (rank 4)", Mrh.rank() == 4)

    # ---- (3) u=1 real-k linear form and sign flip ----
    cc1 = coeffs(1)[0]
    cc1r = [sp.simplify(c.subs(subR)) for c in cc1]
    want = [-sp.sin(3 * sp.pi / 8) * kR[0], sp.sin(sp.pi / 8) * kR[1], sp.sin(sp.pi / 8) * kR[2], sp.sin(sp.pi / 8) * kR[3]]
    chk("(3) coefficient vector = (-sin(3pi/8)k0, sin(pi/8)k_vec)", [sp.simplify(a - b) for a, b in zip(cc1r, want)] == [0, 0, 0, 0])
    q = sp.symbols('q', positive=True)
    vpos = cc1r[0].subs(kR[0], q) * 1
    vneg = cc1r[0].subs(kR[0], q) * (-1)
    chk("(3b) sign flips between rho0>0 and rho0<0 for k0>0", vpos < 0 and vneg > 0)

    # ---- (4) mass real part on R_u ----
    g = sp.symbols('g', positive=True)
    A0t, A1t, A2t, A3t = sp.symbols('A0t A1t A2t A3t', positive=True)
    u = sp.symbols('u', real=True)
    A0 = sp.exp(-3 * sp.pi * sp.I * u / 8) * A0t
    Ai = [sp.exp(sp.pi * sp.I * u / 8) * t for t in (A1t, A2t, A3t)]
    gam = sp.symbols('gamma', real=True)
    AmuAmu = -A0**2 + sum(t**2 for t in Ai)
    reI = sp.simplify(sp.expand_complex(sp.re(sp.I * (-gam / (2 * g**2)) * AmuAmu)))
    pred = gam / (2 * g**2) * (sp.sin(3 * sp.pi * u / 4) * A0t**2 + sp.sin(sp.pi * u / 4) * (A1t**2 + A2t**2 + A3t**2))
    chk("(4a) Re(iS_gamma) on R_u = gamma/(2g^2)[sin(3pi u/4)A0t^2 + sin(pi u/4)sum Ai^2]  (damping on ALL components iff gamma<0, growth iff gamma>0, for u in (0,1])",
        sp.simplify(reI - pred) == 0)
    chk("(4b) at u=1 coefficient = gamma*sqrt2/(4g^2) on all four (growth iff gamma>0)",
        sp.simplify(reI.subs(u, 1) - gam * sp.sqrt(2) / (4 * g**2) * (A0t**2 + A1t**2 + A2t**2 + A3t**2)) == 0)
    chk("(4c) at u=0 the mass term is a pure phase", sp.simplify(reI.subs(u, 0)) == 0)
    # admissible-u closing coefficient: u_max(eps,gamma) from 053: eps cos(3 pi u/4) > (gamma/2) sin(pi u/4)... note sign; report u for which regulator damping coefficient cos(3pi u/4) vanishes: u=2/3
    chk("(4d) regulator damping on A0t vanishes at u=2/3 (cos(3pi u/4)=0)", sp.cos(3 * sp.pi / 4 * sp.Rational(2, 3)) == 0)
    print("NOTE: the quartic identity Re(iS_b(A(u,A~))) = -sin(pi u/2) S_E(A~) and the u=1 weight/phase")
    print("identities are 053 results (re-verified by the 053 gatekeeper); not re-derived here.")
    print("ALL PASS" if ok else "FAILURES PRESENT")
    return 0 if ok else 1

if __name__ == '__main__':
    raise SystemExit(main())
