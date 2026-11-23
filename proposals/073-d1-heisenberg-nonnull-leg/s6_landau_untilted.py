"""S6 (numerical, double precision).  Landau sectors of the forty linearised equations on untilted (s = 0)
members of the family without the SO(2) symmetry of S5 (general al, be, ga, nonzero zeta, x and chi), with the
column cut of 072 s2 (columns on levels <= L, rows on all N levels, so a root is a value of q0 at which a
polynomial-times-Gaussian solution exists):
 (a) background residual; kernel at generic complex q0 = span of the gauge directions (lin.gauge_vectors_R);
 (b) every characteristic root is assigned to the class Lambda of common073.lambdas and the odd integer l with
       q0^2 - p^2 + 2 Lambda (q0 - p) = kappa p l     (that is (q_par + Lambda k)^2 + kappa p l = 0),
     and the numbers of roots per (class, l) are printed for l <= 5 (two roots per quadratic factor); a root is
     assigned if |l - odd integer| < 5e-3: the multiple roots of the class i tau/2 carry chains and split
     numerically by about 1e-3 (as at chi = 0 in 072 s2), the simple roots of the other classes agree to < 1e-5;
 (c) the order-zero operator Q has its roots in the class i tau/2 only.
Run: python -I -B s6_landau_untilted.py"""
import os, sys, time
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common073 import *

t0 = time.time()


def solve_be(chi, th, al, ga):
    A = -2; B = -2 * th; Cc = th ** 2 - al ** 2 - ga ** 2 + 2 * chi * (al + ga)
    return (-B - np.sqrt(B * B - 4 * A * Cc)) / (2 * A)


pts = [('U2', (1.0, 0.0, 0.0, 1.0, 0.5, -1 / 3, 0.6, 0.0, 0.8)),
       ('G1', (1.0, 0.0, 0.4, 1.3, 0.5, -0.7, 0.2, solve_be(0.4, 1.3, 0.2, -0.3), -0.3)),
       ('G2', (1.7, 0.0, -0.6, 0.9, -0.3, 0.8, 0.5, solve_be(-0.6, 0.9, 0.5, 0.1), 0.1))]
for name, par in pts:
    kap, s, chi, th, zeta, x, al, be, ga = par
    C, W, k, n = family(*par); tau = chi + al + ga
    B1, B2, T, R = bg.brackets(C, W, eta)
    Ls, mult = lambdas(chi, th, tau)
    print('== %s (kappa,s,chi,th,zeta,x,al,be,ga) = %s, tau = %.4f: |B1|,|B2| = %.0e %.0e, constraint %.0e'
          % (name, tuple(round(v, 4) for v in par), tau, np.abs(B1).max(), np.abs(B2).max(), constraint(chi, th, al, be, ga)))
    print('   classes:', ' '.join('%.4f%+.4fi' % (L.real, L.imag) for L in Ls))
    N, L, p = 14, 5, 0.4
    E = modes(p, 0.37 + 0.2j, N, kap); M = K.M_op(C, W, E)
    cols = [i * N + nn for i in range(40) for nn in range(L + 1)]
    Mc = M[:, cols]; U_, sv, Vh = np.linalg.svd(Mc); ker = Vh[np.sum(sv > 1e-9 * sv[0]):].conj().T
    G = lin.gauge_vectors_R(C, W, E); Gc = G[cols][:, [j for j in range(G.shape[1]) if j // 10 <= L - 1]]
    print('   (a) kernel dim %d, gauge %d, rank[ker|G] %d, |M G| %.0e' % (ker.shape[1], Gc.shape[1],
                                                                       K.rank(np.hstack([ker, Gc])), np.abs(Mc @ Gc).max()))
    for op, nc, lab in [(K.M_op, 40, 'forty'), (lin.Qop, 4, 'Q')]:
        for p in (0.3, 0.7):
            N, Lc = 16, 6
            cols = [i * N + nn for i in range(nc) for nn in range(Lc + 1)]
            Mf = lambda q0: op(C, W, modes(p, q0, N, kap))[:, cols]
            r = K.rank(Mf(0.37 + 0.11j)); rt = Tl.char_roots(Mf, r)
            cnt = {}; bad = 0; devc = {}
            for z in rt:
                best = None
                for j, La in enumerate(Ls):
                    l = (z * z - p * p + 2 * La * (z - p)) / (kap * p)
                    lr = int(round(l.real))
                    d = abs(l - lr)
                    if lr % 2 and (best is None or d < best[0]):
                        best = (d, j, lr)
                if best is None or best[0] > 5e-3:
                    bad += 1; continue
                if best[2] <= 5:
                    devc[best[1]] = max(devc.get(best[1], 0.0), best[0])
                    cnt[(best[1], best[2])] = cnt.get((best[1], best[2]), 0) + 1
            print('   (%s) %-5s p=%.1f: rank %d of %d, roots %d, unassigned %d; max |l - odd integer| per class (l<=5): %s'
                  % ('b' if lab == 'forty' else 'c', lab, p, r, len(cols), len(rt), bad,
                     {j: float('%.1e' % v) for j, v in sorted(devc.items())}))
            print('        roots per (class, l):', dict(sorted(cnt.items())), '[%.0fs]' % (time.time() - t0), flush=True)
