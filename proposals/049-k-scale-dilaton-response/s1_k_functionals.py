"""049 s1: exact one-loop K functionals for explicit K; operator conventions. Prints only.

 (A) HV is the Hessian of -(1/4)Tr[X,X]^2 plus the Feynman background gauge term (finite differences);
 (B) closed spectra on fuzzy S^2 against brute force;
 (C) str H^k on a random non-commuting K: k = 0..3 vanish, k = 4 does not;
 (D) table of V, T, Uhat, W_R = V - T, abar, nbar for S^2_N, S^2 x S^2, squashed su(3) orbits.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from klib import *

rng = np.random.default_rng(49)


def herm(d):
    r = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    return (r + r.conj().T) / 2


def S(X):
    tot = 0.0
    for i in range(6):
        for j in range(6):
            c = comm(X[i], X[j])
            tot += -0.25 * np.trace(c @ c).real
    return tot


print("(A) Hessian of the action against HV (background Feynman gauge)")
d = 3
L = [herm(d) for _ in range(6)]
a = [herm(d) for _ in range(6)]
eps = 1e-3
d2S = (S([x + eps * y for x, y in zip(L, a)]) + S([x - eps * y for x, y in zip(L, a)]) - 2 * S(L)) / eps ** 2
g = 1j * sum(comm(L[i], a[i]) for i in range(6))  # Hermitian
d2gf = np.trace(g @ g).real  # second derivative of (1/2)Tr g^2
vec = [x.flatten(order="F") for x in a]
adsc = [adc(x) for x in L]
H0c = sum(p @ p for p in adsc)
quad = 0.0
for i in range(6):
    for j in range(6):
        blk = 2 * adc(comm(L[i], L[j])) + (H0c if i == j else 0)
        quad += (vec[i].conj() @ blk @ vec[j]).real
print("  d2S + d2(gauge term) = %.8f, <a,HV a> = %.8f, rel diff %.2e" % (d2S + d2gf, quad, abs(d2S + d2gf - quad) / abs(quad)))

print("(B) fuzzy S^2: vector l(l-1) [2l+3], l(l+1)+2 [2l+1], (l+1)(l+2) [2l-1]; spinor l^2 [2l+2], (l+1)^2 [2l]")
for N in (2, 3, 5, 8):
    w0, wV, wD = spectra(K_sphere(N))
    cV = []
    cD = []
    for l in range(N):
        cV += [l * (l - 1)] * (2 * l + 3)
        if l >= 1:
            cV += [l * (l + 1) + 2] * (2 * l + 1)
            cV += [(l + 1) * (l + 2)] * (2 * l - 1)
        cD += [l ** 2] * (2 * l + 2)
        if l >= 1:
            cD += [(l + 1) ** 2] * (2 * l)
    cV += [l * (l + 1) for l in range(N) for _ in range(3 * (2 * l + 1))]
    cD = cD * 4
    print("  N=%d vector max dev %.1e, spinor max dev %.1e" % (N, np.abs(np.sort(cV) - wV).max(), np.abs(np.sort(cD) - wD).max()))

print("(C) str H^k on a random K (d=4); ghost weight -2, 16 -> 8 Dirac components of so(6)")
w0, wV, wD = spectra([herm(4) for _ in range(6)])
for k in range(0, 5):
    print("  str H^%d = % .6e" % (k, str_moment(w0, wV, wD, k)))

print("(D) unit-scale data; Uhat = int s^-3 (v-tau), V, T as in the 047 weights without D(s)")
fmt = "  %-26s %5s %9s %9s %9s %10s %10s %10s %10s %9s"
print(fmt % ("K", "d", "minV", "V", "T", "W_R=V-T", "Uhat", "Uhat/T", "abar", "nbar"))


def row(name, L):
    V, T, U, info = moments(L)
    a, n = tree_data(L)
    print("  %-26s %5d %9.4f %9.3f %9.3f %10.4f %10.4f %10.5f %10.3f %9.2f" % (name, L[0].shape[0], info["minV"], V, T, V - T, U, U / T, a, n))


for N in (2, 3, 4, 6, 8, 12, 16):
    row("S2_%d" % N, K_sphere(N))
for N in (2, 3, 4, 5):
    row("S2_%d x S2_%d" % (N, N), K_two_spheres(N, N))
row("S2_3 x S2_5", K_two_spheres(3, 5))
row("S2_4 x S2_4 r2/r1=0.7", K_two_spheres(4, 4, 1.0, 0.7))
row("S2_4 x S2_4 r2/r1=0.3", K_two_spheres(4, 4, 1.0, 0.3))
for p in (1, 2, 3, 4, 5):
    row("squashed su3 (%d,0)" % p, K_squashed(su3_rep(p)))
for p, q in ((1, 1), (2, 1), (2, 2)):
    E, dm = su3_mixed(p, q)
    row("squashed su3 (%d,%d) d=%d" % (p, q, dm), K_squashed(E))
