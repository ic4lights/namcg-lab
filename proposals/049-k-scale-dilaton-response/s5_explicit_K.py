"""049 s5: explicit K: large-N fuzzy sphere, equal-weight test, flat-flux stacks, sign scan. Prints only.

 (A) S^2_N from the closed spectrum: V, T, Uhat, against brute force, up to N = 4096; numerical fits;
 (B) quantities of the consistency window for S^2_N (scale estimates);
 (C) equal weights: T_0, T_1, T_2, V_0, V_1 of the 047 definition against F T, for chi N / n;
 (D) off-diagonal modes of two stacks with constant relative flux (f1,f2,f3): v - tau, V, T, Uhat;
 (E) search for compact K with Uhat < 0 and no negative mode.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy import integrate
from klib import moments, K_sphere, K_two_spheres, K_squashed, su3_rep, spectra, moments_from_spectra, tree_data


def sphere_levels(N):
    """(eigenvalue, multiplicity) arrays: H0, vector (three components, the other three are H0), spinor (eight components)."""
    ls = np.arange(N, dtype=float)
    l0 = ls * (ls + 1)
    m0 = 2 * ls + 1
    wv = np.concatenate([ls * (ls - 1), l0[1:] + 2, (ls[1:] + 1) * (ls[1:] + 2)])
    mv = np.concatenate([2 * ls + 3, 2 * ls[1:] + 1, 2 * ls[1:] - 1])
    wd = np.concatenate([ls ** 2, (ls[1:] + 1) ** 2])
    md = 4 * np.concatenate([2 * ls + 2, 2 * ls[1:]])
    return (l0, m0), (wv, mv), (wd, md)


def plogp(w, c, p, shift=0.0):
    w = w + shift
    mask = w > 1e-12
    return np.sum(c[mask] * w[mask] ** p * np.log(w[mask]))


def sphere_moments(N, shift=0.0):
    (l0, m0), (wv, mv), (wd, md) = sphere_levels(N)
    # vector index part: three components differ from H0; the remaining three cancel
    V = plogp(wv, mv, 1, shift) - 3 * plogp(l0, m0, 1, shift)
    T = plogp(wd, md, 1, shift) - 8 * plogp(l0, m0, 1, shift)
    return V, T


def sphere_U(N):
    (l0, m0), (wv, mv), (wd, md) = sphere_levels(N)
    return -0.5 * (plogp(wv, mv, 2) - plogp(wd, md, 2) + 5 * plogp(l0, m0, 2))


print("(A) S^2_N")
for N in (2, 3, 8, 16):
    V, T, U, info = moments(K_sphere(N))
    Vc, Tc = sphere_moments(N)
    Uc = sphere_U(N)
    print("    N=%3d brute (V,T,U)=(%.6f,%.6f,%.6f) closed (%.6f,%.6f,%.6f)" % (N, V, T, U, Vc, Tc, Uc))
print("    %6s %14s %14s %12s %10s %10s %10s %12s" % ("N", "V", "T", "V-T", "(V-T)/T", "T/N^2", "U/N^2", "V-T-4lnN"))
rows = []
for N in (8, 16, 32, 64, 128, 256, 512):  # double precision loses V-T above this N
    V, T = sphere_moments(N)
    U = sphere_U(N)
    rows.append((N, V, T, U))
    print("    %6d %14.4f %14.4f %12.5f %10.3e %10.5f %10.5f %12.5f" % (N, V, T, V - T, (V - T) / T, T / N ** 2, U / N ** 2, V - T - 4 * np.log(N)))
abar = lambda N: N * (N ** 2 - 1) / 8
nbar = lambda N: N * (N ** 2 - 1) / 4
print("    tree data exact: abar = N(N^2-1)/8, nbar = N(N^2-1)/4; check N=5:", tree_data(K_sphere(5)), (abar(5), nbar(5)))

print("(B) window for S^2_N (scale estimates), undeformed quartic, V close to T, vartheta close to 1")
print("    chi^2 = 3 vartheta F That/(256 pi^2 abar Ehat), Ehat = E/g^2, weak coupling eps = F Uhat/(32 pi^2 abar Ehat) << 1")
for N, n in ((100, 10), (1000, 10), (1000, 30), (4096, 30)):
    F = (n + 1) ** 2
    V, T = sphere_moments(N)
    U = sphere_U(N)
    Ewc = F * U / (32 * np.pi ** 2 * abar(N))  # eps = 1 at this Ehat
    Elev = 3 * F * T * N ** 2 / (256 * np.pi ** 2 * abar(N) * n ** 2)  # chi^2 N^2 = n^2 at this Ehat
    print("    N=%5d n=%3d: eps=1 at Ehat=%.3e ; chi^2 N^2 = n^2 at Ehat=%.3e ; window eps<<1 and chi^2 N^2>>n^2 is %.3e << Ehat << %.3e" % (N, n, Ewc, Elev, Ewc, Elev))

print("(C) equal weights on S^2_N (D, B_0, B_1 of 047, levels J <= n), ratio to the equal-weight value")


def cg2(J, Jp):
    if Jp == J:
        return J * (J + 1) / ((2 * J - 1) * (2 * J + 3)) if J > 0 else 0.0
    if Jp == J + 2:
        return 3 * (J + 1) * (J + 2) / (2 * (2 * J + 1) * (2 * J + 3))
    if Jp == J - 2:
        return 3 * J * (J - 1) / (2 * (2 * J - 1) * (2 * J + 1)) if J >= 2 else 0.0
    return 0.0


gl_x, gl_w = np.polynomial.legendre.leggauss(12)
gl_a = 0.5 * (gl_x + 1)
gl_w = 0.5 * gl_w


def weights_sphere(N, chi2, n):
    """Return (V0,T0,V1,T1,T2) divided by F chi2 (Vhat or That)."""
    (l0, m0), (wv, mv), (wd, md) = sphere_levels(N)
    wv = wv * chi2
    wd = wd * chi2
    l0 = l0 * chi2
    mu = lambda J: J * (J + 2.0)

    def VT(shift):
        v = plogp(wv, mv, 1, shift) - 3 * plogp(l0, m0, 1, shift)
        t = plogp(wd, md, 1, shift) - 8 * plogp(l0, m0, 1, shift)
        return v, t

    F = (n + 1) ** 2
    V0 = T0 = V1 = T1 = T2 = 0.0
    for J in range(0, n + 1):
        v, t = VT(mu(J))
        V0 += (2 * J + 1) * v
        T0 += (2 * J + 1) * t
        for Jp in (J - 2, J, J + 2):
            if Jp < 0 or Jp > n:
                continue
            c = cg2(J, Jp)
            if J == 0 and Jp == 0:
                c = 0.0
            if c == 0.0:
                continue
            d = mu(Jp) - mu(J)
            for a, w in zip(gl_a, gl_w):
                vs, ts = VT(mu(J) + d * a)
                T2 += (2 * J + 1) * c * w * ts
                V1 += (2 * J + 1) * c * w * 6 * a * (1 - a) * vs
                T1 += (2 * J + 1) * c * w * 6 * a * (1 - a) * ts
    Vh, Th = sphere_moments(N)
    norm = F * chi2
    return V0 / (norm * Vh), T0 / (norm * Th), V1 / (norm * Vh), T1 / (norm * Th), T2 / (norm * Th)


print("    %6s %5s %8s %10s | %8s %8s %8s %8s %8s" % ("N", "n", "chi^2", "chiN/n", "V0", "T0", "V1", "T1", "T2"))
for N, n, chi2 in ((64, 4, 1.0), (256, 4, 1.0), (1024, 4, 1.0), (256, 10, 1.0), (1024, 10, 1.0), (1024, 10, 0.01), (1024, 10, 100.0)):
    r = weights_sphere(N, chi2, n)
    print("    %6d %5d %8.2f %10.2f | %8.4f %8.4f %8.4f %8.4f %8.4f" % (N, n, chi2, np.sqrt(chi2) * N / n, *r))
print("    the sum over J' of c(J,J') is 1, so V1, T1, T2 differ from V0, T0 by the truncation J' <= n, about 1 - 3/(2n):")
for n in (4, 10, 30, 100, 300):
    F = (n + 1) ** 2
    r = sum((2 * J + 1) * sum(cg2(J, Jp) for Jp in (J - 2, J, J + 2) if 0 <= Jp <= n) for J in range(n + 1)) / F
    print("      n=%3d  r_n=%.5f  1-3/(2n)=%.5f" % (n, r, 1 - 1.5 / n))

print("(D) stacks with constant relative flux; per unit density (f1 f2 f3 /(2 pi)^3 stripped where stated)")


def logsinh(z):
    return z + np.log1p(-np.exp(-2 * z)) - np.log(2.0)


def logs0(s, f):
    """log of prod x/(2 sinh(x s)), per unit density; every x > 0 here."""
    return sum(np.log(x) - np.log(2.0) - logsinh(x * s) for x in f)


def vtau(s, f):
    ls0 = logs0(s, f)
    v = sum(4 * np.exp(2 * logsinh(x * s) + ls0) for x in f)
    lc = sum(x * s + np.log1p(np.exp(-2 * x * s)) - np.log(2.0) for x in f)
    tau = 8 * np.exp(lc + ls0) - 8 * np.exp(ls0)
    return v, tau


def s0_flat(s, f):
    return np.exp(logs0(s, f))


def vmt(s, f):
    """v - tau from the product identity, free of cancellation."""
    a = sum(f)
    return 16 * s0_flat(s, f) * np.sinh(a * s / 2) * np.sinh((f[0] + f[1] - f[2]) * s / 2) * np.sinh((f[0] - f[1] + f[2]) * s / 2) * np.sinh((f[0] - f[1] - f[2]) * s / 2)


def flat_moments(f, sc):
    """The integrals are ultraviolet divergent per unit density (T ~ sc^-2, Uhat ~ 1/sc, V - T ~ ln sc); sc stands for the truncation of the modes."""
    breaks = [sc, 0.5, 2.0, 8.0, 40.0, 400.0]
    breaks = sorted(set([x for x in breaks if x >= sc]))
    VmT = U = T = 0.0
    for lo, hi in zip(breaks[:-1], breaks[1:]):
        VmT += integrate.quad(lambda s: vmt(s, f) / s ** 2, lo, hi, limit=200)[0]
        U += integrate.quad(lambda s: vmt(s, f) / s ** 3, lo, hi, limit=200)[0]
        T += integrate.quad(lambda s: vtau(s, f)[1] / s ** 2, lo, hi, limit=200)[0]
    return VmT, T, U


print("    with lower limit s_c on the proper time, standing for the truncation of the modes")
print("    %-18s %6s %12s %14s %12s %10s %14s" % ("(f1,f2,f3)", "s_c", "V-T", "T", "Uhat", "lowest HV", "sign(v-tau)"))
for f in ((1.0, 0.5, 0.5), (1.0, 0.7, 0.3), (1.0, 0.6, 0.6), (1.0, 0.8, 0.8), (1.0, 1.0, 1.0)):
    for sc in (0.1, 0.01):
        VmT, T, U = flat_moments(f, sc)
        low = sum(f) - 2 * max(f)
        sgn = np.sign(f[0] - f[1] - f[2])
        print("    %-18s %6.2f %12.6f %14.3f %12.6f %10.3f %14.0f" % (str(f), sc, VmT, T, U, low, sgn))
f = (1.0, 0.8, 0.6)
s = 0.7
print("    identity at s=0.7,(1,.8,.6): direct %.10f, product %.10f" % (vtau(s, f)[0] - vtau(s, f)[1], vmt(s, f)))
print("    for f1 >= f2, f3 and no negative mode (f1 <= f2 + f3) v - tau <= 0 for every s, with equality for all s iff f1 = f2 + f3")

print("(E) scan of compact K for Uhat < 0 with no negative mode")
gen = np.random.default_rng(4905)


def herm(d):
    r = gen.normal(size=(d, d)) + 1j * gen.normal(size=(d, d))
    return (r + r.conj().T) / 2


def scan(name, make, count):
    nok = 0
    umin = np.inf
    rmin = np.inf
    for _ in range(count):
        L = make()
        w0, wV, wD = spectra(L)
        if wV.min() < -1e-8:
            continue
        V, T, U = moments_from_spectra(w0, wV, wD)
        nok += 1
        if T > 1e-10:
            rmin = min(rmin, U / T)
        umin = min(umin, U)
    print("    %-44s samples %5d, without negative mode %5d, min Uhat %.5g, min Uhat/T %.5g" % (name, count, nok, umin, rmin))


def squashed_random():
    c = gen.uniform(0.2, 1.5, size=3)
    return K_squashed(su3_rep(int(gen.integers(1, 4))), tuple(c))


def two_sphere_random():
    return K_two_spheres(int(gen.integers(2, 4)), int(gen.integers(2, 4)), 1.0, float(gen.uniform(0.1, 1.5)))


def random_d(d, rank):
    def mk():
        return [herm(d) if k < rank else np.zeros((d, d), dtype=complex) for k in range(6)]
    return mk


scan("squashed su(3), weights random, reps (1,0)-(3,0)", squashed_random, 120)
scan("S^2 x S^2, radius ratio random", two_sphere_random, 60)
for d, rank in ((2, 3), (2, 6), (3, 3), (3, 6)):
    scan("random Hermitian d=%d, %d non-zero matrices" % (d, rank), random_d(d, rank), 300)
