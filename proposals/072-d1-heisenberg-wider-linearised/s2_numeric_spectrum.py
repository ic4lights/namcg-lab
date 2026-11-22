"""S2 (numerical, double precision).  Forty linearised frame and connection equations on the wider
Heisenberg family in the Landau sectors (E_0 = i q0, E_2 = i p, E_1, E_3 oscillator on N levels), using
core068.M_op (068 linearisation, arbitrary constant c, w) read-only from proposals/071-.../.
 (a) background brackets vanish; kernel at generic complex q0 (columns at levels <= L, rows on all N
     levels, as in 068 S3) equals the span of the gauge directions (lin.gauge_vectors_R, with the
     curvature term), 10 per level of the parameter;
 (b) frame-label reduction for the central labels I = 0, 2: h_a^c = -f_a delta^c_I,
     omega_a^{cd} = -f_a w_I^{cd} is mapped to B1_b^e = (Qf)_b delta^e_I, B2_b^{de} = -(Qf)_b w_I^{de};
 (c) characteristic roots (rank drop below generic rank): for each root the real number c with
     Im[q0^2 - p^2 + i c chi (q0 - p)] = 0 is computed, and then l = Re[...] / (kappa p); all roots are
     found at c in {-1, 1, 3} and odd integer l >= -1; counts per (c, l) for l well below the column cut,
     at zeta = x = 0 and at zeta, x != 0 (the same values and counts); the last case is family (ii)
     (chi = 0), where c is set to 0 and the 068 levels are recovered;
 (d) the order-zero operator Q is independent of zeta, x and its roots are at c = 1;
 (e) the forty equations are not affine in w (unlike Q): the second difference in w is nonzero; it
     squares to zero at the sampled points (an observation, not used for any claim).
Run: python -I -B s2_numeric_spectrum.py"""
import os, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
import numpy as np


def roots(op, ncomp, par, p, N, L):
    C, W = wider(*par); kap = par[0]
    cols = [i * N + n for i in range(ncomp) for n in range(L + 1)]
    Mf = lambda q0: op(C, W, modes(p, q0, N, kap))[:, cols]
    r = K.rank(Mf(0.37 + 0.11j)); return r, len(cols), Tl.char_roots(Mf, r)


def classify(rt, par, p):
    kap, chi = par[0], par[1]
    # at chi = 0 the multiple roots carry long chains and split numerically by ~1e-3 (as in 068 S3),
    # so the tolerance on l is 2e-2 there; at chi != 0 it is 1e-4 on both c and l
    tol = 1e-4 if chi else 2e-2
    out = {}
    bad = []; dev = 0.0
    for z in rt:
        c = -(z ** 2).imag / (chi * (z - p).real) if chi else 0.0
        l = ((z ** 2 - p ** 2 + 1j * c * chi * (z - p)) / (kap * p)).real
        cr, lr = round(c), round(l)
        if abs(c - cr) > 1e-4 or abs(l - lr) > tol or lr % 2 == 0:
            bad.append((z, c, l)); continue
        if lr <= 5:
            dev = max(dev, abs(c - cr), abs(l - lr))
        out[(cr, lr)] = out.get((cr, lr), 0) + 1
    return out, bad, dev


print('== (a) background and gauge kernel')
for par in [(1.0, 0.5, 0.0, 0.0), (1.0, 0.5, 0.7, -0.2), (1.3, -0.8, 0.3, 0.5)]:
    C, W = wider(*par)
    B1, B2, T, R = bg.brackets(C, W, K.ETA)
    N, L, p = 14, 5, 0.4
    E = modes(p, 0.37 + 0.2j, N, par[0]); M = K.M_op(C, W, E)
    cols = [i * N + n for i in range(40) for n in range(L + 1)]
    Mc = M[:, cols]; U_, s, Vh = np.linalg.svd(Mc); ker = Vh[np.sum(s > 1e-9 * s[0]):].conj().T
    G = lin.gauge_vectors_R(C, W, E); Gc = G[cols][:, [j for j in range(G.shape[1]) if j // 10 <= L - 1]]
    print('  (kappa,chi,zeta,x) = %s: |B1|,|B2| = %.0e %.0e ; kernel dim %d, gauge %d, rank[ker|G] %d, |M G| %.0e'
          % (par, np.abs(B1).max(), np.abs(B2).max(), ker.shape[1], Gc.shape[1], K.rank(np.hstack([ker, Gc])), np.abs(Mc @ Gc).max()))

print('== (b) central frame labels')
N = 10; kap = 1.0; p = 0.4
for par in [(1.0, 0.7, 0.3, -0.4), (1.3, -0.8, 0.3, 0.5)]:
    C, W = wider(*par); E = modes(p, 0.37 + 0.2j, N, par[0]); M = K.M_op(C, W, E); Q = lin.Qop(C, W, E)
    rng = np.random.default_rng(3)
    f = np.zeros((4, N), complex); f[:, :N - 3] = rng.normal(size=(4, N - 3)) + 1j * rng.normal(size=(4, N - 3))
    rows = [i * N + n for i in range(40) for n in range(N - 1)]
    for I in (0, 2):
        h = np.zeros((4, 4, N), complex); w = np.zeros((4, 4, 4, N), complex)
        for a in range(4):
            h[a, I] = -f[a]; w[a] = -np.einsum('cd,n->cdn', W[I], f[a])
        Qf = (Q @ f.reshape(-1)).reshape(4, N)
        hB = np.zeros((4, 4, N), complex); wB = np.zeros((4, 4, 4, N), complex)
        for b in range(4):
            hB[b, I] = Qf[b]; wB[b] = -np.einsum('cd,n->cdn', W[I], Qf[b])
        print('  %s label I=%d: |M v - u(Qf)| = %.1e' % (par, I, np.abs((M @ K.pack_hw(h, w) - K.pack_hw(hB, wB))[rows]).max()))

print('== (c) roots of the forty equations: counts per (c, l), l <= 5 (column cut L = 6 at N = 16)')
for par, p in [((1.0, 0.5, 0.0, 0.0), 0.3), ((1.0, 0.5, 0.0, 0.0), 0.7), ((1.3, -0.8, 0.0, 0.0), 0.3),
               ((1.0, 0.5, 0.7, -0.2), 0.3), ((1.3, -0.8, 0.3, 0.5), 0.7), ((2.0, 0.25, -1.0, 0.6), 0.45),
               ((1.0, 0.0, 0.7, -0.2), 0.3)]:
    r, n, rt = roots(K.M_op, 40, par, p, 16, 6)
    cnt, bad, dev = classify(rt, par, p)
    print('  %s p=%.2f: generic rank %d of %d, roots %d, unclassified %d, max deviation of c, l for l <= 5: %.1e'
          % (par, p, r, n, len(rt), len(bad), dev))
    print('     ', {k: v for k, v in sorted(cnt.items()) if k[1] <= 5})
    for z, c, l in bad:
        print('      unclassified root q0 = %.6f%+.6fi (c = %.4f, l = %.4f)' % (z.real, z.imag, c, l))

print('== (d) order-zero operator Q')
for par, p in [((1.0, 0.5, 0.0, 0.0), 0.3), ((1.0, 0.5, 0.7, -0.2), 0.3), ((1.3, -0.8, 0.3, 0.5), 0.7)]:
    C, W = wider(*par); C0, W0 = wider(par[0], par[1], 0, 0); E = modes(p, 0.37, 12, par[0])
    dz = np.abs(lin.Qop(C, W, E) - lin.Qop(C0, W0, E)).max()
    r, n, rt = roots(lin.Qop, 4, par, p, 16, 6)
    cnt, bad, dev = classify(rt, par, p)
    print('  %s p=%.2f: |Q(zeta,x) - Q(0,0)| = %.0e ; rank %d of %d ; counts (c,l) %s ; unclassified %d'
          % (par, p, dz, r, n, {k: v for k, v in sorted(cnt.items()) if k[1] <= 5}, len(bad)))

print('== (e) part quadratic in w')
N = 10; p = 0.4
E = modes(p, 0.37 + 0.2j, N, 1.0)
for a in [(0.7, 0, 0), (0, 0.3, 0), (0.7, 0.3, -0.4)]:
    a = np.array(a); Mof = lambda v: K.M_op(*wider(1.0, *v), E)
    D2 = Mof(2 * a) - 2 * Mof(a) + Mof(0 * a)
    print('  (chi,zeta,x) = %s: |second difference| = %.2f, |(second difference)^2| = %.0e' % (tuple(a), np.abs(D2).max(), np.abs(D2 @ D2).max()))
