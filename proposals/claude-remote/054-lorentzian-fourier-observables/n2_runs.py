#!/usr/bin/env python3
"""Numerical checks at N=2 for proposal 054 (Tr e^{i kappa A_0}, kappa along the regulator's time axis).

Usage: python n2_runs.py OUTFILE      (refuses to overwrite OUTFILE)
Notation: J(kappa) = <Tr e^{i kappa A_0}> on the contour, eps as stated; kappa = K e^{i alpha} complex.
Sections:
 R1  Euclidean ray u=1 (alpha = 3 pi/8): F_E(K^2) = <Tr e^{i K At_0}>_E and Euclidean moments <|at|^{2n}>_E.
 R2  Ray alpha = 3 pi 0.8/8 at eps = 0 on two contours, beta = alpha/3 (R_0.8) and beta = alpha/2 (Cauchy in beta at
     fixed a-phase); moments against e^{3 pi i n (u-1)/4}<|at|^{2n}>_E; small K against the Taylor polynomial
     built from Euclidean moments.  (The ray u = 1.4 is not independent: there all values are complex conjugates
     of those at u = 0.6, since the N = 2 Euclidean weight is real.)
 R3  Statement (i): regulated Lorentzian <.>_eps at complex kappa = K e^{i alpha}, alpha = 3 pi 0.6/8, on R_0.6,
     eps -> 0 against eps = 0, and the same moments/Taylor checks on that ray at eps = 0; Stokes check at
     eps = 0.1 on R_0.4 for the same complex kappa.
 R4  Statement (iii): with phi(kappa) = exp(-(kappa-k0)^2/l^2), the smeared observable
     int phi(kappa) <Tr e^{i kappa A_0}> d kappa = sqrt(pi) l <Tr exp(i k0 A_0 - l^2 A_0^2/4)>,
     regulated on R_0.6 for eps -> 0 (in R3) and at eps = 0 on R_0.6 and on R_0.5.
 R5  Grid check: R1 and the eps = 0 values of R3 on a finer grid.
All observables are ratios to the partition function on the same contour and grid.  Grid GF: composite
Gauss-Legendre in (s, v, z) = (log w1, log w1/w2, log w2/w3); angular rule 48 x 10.  Finer grid GF2 in R5.
"""
import sys, os, time, math, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from n2_fourier import integrate, Ru

GF = [[(24, -9., -2.), (90, -2., 3.5), (40, 3.5, 20.)], [(50, 0., 4.), (30, 4., 12.), (24, 12., 32.)],
      [(50, 0., 4.), (24, 4., 12.), (16, 12., 32.)]]
GF2 = [[(30, -9., -2.), (120, -2., 3.5), (50, 3.5, 20.)], [(66, 0., 4.), (40, 4., 12.), (30, 12., 32.)],
       [(66, 0., 4.), (32, 4., 12.), (20, 12., 32.)]]
G = dict(pieces=GF, angpar=(48, 10))
OUT = None

def say(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    OUT.write(s+"\n"); OUT.flush()

def run(kappas, eps, al, be, extra=()):
    t = time.time()
    r = integrate(list(kappas), eps, al, be, extra_specs=list(extra), **G)
    return r, time.time()-t

def taylor(K, u, mE, nmax=3):
    return 2*sum((-1)**n*(K/2)**(2*n)/math.factorial(2*n)*(1 if n == 0 else np.exp(3j*np.pi*n*(u-1)/4)*mE[n-1])
                 for n in range(0, nmax+1))

def fmt(v):
    return f"{v.real:+.8f}{v.imag:+.8f}i"

if __name__ == "__main__":
    fn = sys.argv[1]
    if os.path.exists(fn):
        sys.exit(f"{fn} exists; refusing to overwrite")
    OUT = open(fn, "w")
    say("grid", G)
    MOM = [('mom', n) for n in (1, 2, 3, 4)]
    KT = [0.25, 0.5, 1.0, 2.0, 3.0]
    # R1
    al, be = Ru(1.0)
    K1 = [0.25, 0.5, 1.0, 2.0, 3.0, 4.0]
    (ZE, N, X), dt = run([k*np.exp(1j*al) for k in K1], 0.0, al, be, extra=MOM)
    mE = X/ZE
    FE = 2*N/ZE
    say(f"R1 Euclidean u=1: Z2={ZE:.10e}  ({dt:.0f}s)")
    say("   moments <|at|^{2n}>_E, n=1..4:", "  ".join(fmt(m) for m in mE))
    for k, f in zip(K1, FE):
        say(f"   K={k:5.2f}  F_E(K^2)={fmt(f)}   Taylor(n<=3)={fmt(taylor(k, 1.0, mE))}")
    # R2
    u = 0.8; al = Ru(u)[0]
    vals = {}
    for be in (al/3, al/2):
        (Z, N, X), dt = run([k*np.exp(1j*al) for k in KT], 0.0, al, be, extra=MOM[:3])
        vals[be] = 2*N/Z
        say(f"R2 alpha={al:.5f} beta={be:.5f} eps=0: Z2/Z2_E={fmt(Z/ZE)}  ({dt:.0f}s)")
        for n in (1, 2, 3):
            say(f"   moment n={n}: ratio to e^(3 pi i n(u-1)/4)<|at|^2n>_E = {fmt((X[n-1]/Z)/(np.exp(3j*np.pi*n*(u-1)/4)*mE[n-1]))}")
        for k, v in zip(KT, 2*N/Z):
            say(f"   K={k:5.2f}  J={fmt(v)}   Taylor(n<=3)={fmt(taylor(k, u, mE))}   |diff|={abs(v-taylor(k, u, mE)):.1e}")
    b1, b2 = list(vals)
    say("   max over K of |J(beta=alpha/3) - J(beta=alpha/2)|:", f"{np.max(np.abs(vals[b1]-vals[b2])):.2e}")
    # R3 and R4 on R_0.6
    u = 0.6; al, be = Ru(u)
    K4 = [0.5, 1.0, 2.0]
    k0s, ell = (1.0, 2.0), 1.5
    smear = [('cos', k0*np.exp(-1j*al)/2, ell**2*np.exp(-2j*al)/16) for k0 in k0s]
    res = {}
    for eps in (0.1, 0.03, 0.01, 0.003, 0.0):
        kap = [k*np.exp(1j*al) for k in K4]
        ext = smear+(MOM[:3] if eps == 0.0 else [])
        if eps == 0.0:
            kap = kap+[k*np.exp(1j*al) for k in KT]
        (Z, N, X), dt = run(kap, eps, al, be, extra=ext)
        res[eps] = (2*N[:len(K4)]/Z, np.sqrt(np.pi)*ell*2*X[:2]/Z, Z)
        say(f"R3 u=0.6 eps={eps}: Z2/Z2_E={fmt(Z/ZE)} ({dt:.0f}s)")
        say("   <Tr e^{i kappa A_0}>_eps, kappa=K e^{i alpha}:", "  ".join(f"K={k}: {fmt(v)}" for k, v in zip(K4, res[eps][0])))
        say("   R4 smeared int phi <Tr e^{i kappa A_0}>_eps d kappa:", "  ".join(f"k0={k0}: {fmt(v)}" for k0, v in zip(k0s, res[eps][1])))
        if eps == 0.0:
            for n in (1, 2, 3):
                say(f"   moment n={n}: ratio to e^(3 pi i n(u-1)/4)<|at|^2n>_E = {fmt((X[1+n]/Z)/(np.exp(3j*np.pi*n*(u-1)/4)*mE[n-1]))}")
            for k, v in zip(KT, 2*N[len(K4):]/Z):
                say(f"   K={k:5.2f}  J={fmt(v)}   Taylor(n<=3)={fmt(taylor(k, u, mE))}   |diff|={abs(v-taylor(k, u, mE)):.1e}")
    J0 = res[0.0][0]
    for eps in (0.1, 0.03, 0.01, 0.003):
        say(f"   eps={eps}: |<.>_eps - J|/eps =", "  ".join(f"{abs(a-b)/eps:.4f}" for a, b in zip(res[eps][0], J0)),
            "  smeared:", "  ".join(f"{abs(a-b)/eps:.4f}" for a, b in zip(res[eps][1], res[0.0][1])))
    al2, be2 = Ru(0.4)
    (Z, N), dt = run([k*np.exp(1j*al) for k in K4], 0.1, al2, be2)
    say("R3 Stokes at eps=0.1: same complex kappa on R_0.4:", "  ".join(fmt(v) for v in 2*N/Z), f"({dt:.0f}s)")
    say("                                  and on R_0.6:", "  ".join(fmt(v) for v in res[0.1][0]))
    # R4 second contour
    al3, be3 = Ru(0.5)
    smear3 = [('cos', k0*np.exp(-1j*al3)/2, ell**2*np.exp(-2j*al3)/16) for k0 in k0s]
    (Z, N, X), dt = run([], 0.0, al3, be3, extra=smear3)
    say(f"R4 eps=0 on R_0.5: Z2/Z2_E={fmt(Z/ZE)} ({dt:.0f}s)")
    for i, k0 in enumerate(k0s):
        say(f"   k0={k0} l={ell}: smeared on R_0.5 = {fmt(np.sqrt(np.pi)*ell*2*X[i]/Z)}   on R_0.6 = {fmt(res[0.0][1][i])}")
    # R5 grid check
    G = dict(pieces=GF2, angpar=(56, 12))
    say("R5 grid check with", G)
    al, be = Ru(1.0)
    (Zf, N, X), dt = run([k*np.exp(1j*al) for k in K1], 0.0, al, be, extra=MOM)
    say(f"   R1 fine: Z2/Z2(GF)={fmt(Zf/ZE)}  max|F_E diff|={np.max(np.abs(2*N/Zf-FE)):.2e}  moments ratio:",
        "  ".join(fmt((x/Zf)/m) for x, m in zip(X, mE)), f"({dt:.0f}s)")
    al, be = Ru(0.6)
    (Z, N, X), dt = run([k*np.exp(1j*al) for k in K4], 0.0, al, be, extra=smear)
    say(f"   R3 eps=0 fine: Z2/Z2_E(fine)={fmt(Z/Zf)}  max|J diff|={np.max(np.abs(2*N/Z-res[0.0][0])):.2e}  "
        f"max|smeared diff|={np.max(np.abs(np.sqrt(np.pi)*ell*2*X/Z-res[0.0][1])):.2e} ({dt:.0f}s)")
    OUT.close()
