"""S7 (numerical, double precision).  Landau sectors of the forty linearised equations on tilted members of the
family (s = 3/5, so k = (1, -s, c, 0) has a component along the non-central E_1 and tau = 0).  The solutions are
not polynomial times the Landau Gaussian (a column cut, also after constant shifts of E_1, finds only part of the
class Lambda = 0), so the quadratic pencil of the square truncation to N levels is used:
 (a) background residual; kernel of the column cut at generic q0 = gauge directions (as in S6);
 (b) eigenvalues of the truncated pencil at N = 18 and N = 24; those that agree to 1e-8 and have |q0| < 2.5 are
     called converged; each converged eigenvalue is assigned to a class Lambda of common073.lambdas (tau = 0) and
     an odd l >= -1 with
        (q_par + Lambda k_par)^2 + kappa p l = 0,  k_par = (1, 0, c, 0),  k_par^2 = -s^2,
     that is  q0^2 - p^2 + 2 Lambda (q0 - c p) + s^2 Lambda^2 = kappa p l;
     the numbers per (class, l) and the number of converged eigenvalues left unassigned are printed;
 (c) for every class, the predicted roots at l = -1, 1, 3 and their distance to the nearest eigenvalue at N = 24;
 (d) the momentum-independent term s^2 Lambda^2 and the p -> 0 limits q0 = -Lambda (1 -+ c) of each class;
 (e) the column cut of S6 (polynomial times Gaussian solutions) at the same point: numbers of its roots per class.
Run: python -I -B s7_landau_tilted.py   (several minutes)"""
import os, sys, time
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common073 import *
import scipy.linalg as sl

t0 = time.time()


def solve_be(chi, th, al, ga):
    A = -2; B = -2 * th; Cc = th ** 2 - al ** 2 - ga ** 2 + 2 * chi * (al + ga)
    return (-B - np.sqrt(B * B - 4 * A * Cc)) / (2 * A)


def pencil_eigs(Mf):
    A, B, Cq = Tl.quad_coeffs(Mf); m = A.shape[0]; Z = np.zeros((m, m)); I = np.eye(m)
    ev = sl.eig(np.block([[Z, I], [-A, -B]]), np.block([[I, Z], [Z, Cq]]), right=False)
    return ev[np.isfinite(ev) & (np.abs(ev) < 50)]


ga2 = 0.1; al2 = -0.3 - ga2
pts = [('T1', (1.0, 0.6, 0.0, 1.0, 0.5, -1 / 3, -2 ** -0.5, 0.0, 2 ** -0.5)),
       ('T2', (1.0, 0.6, 0.3, 0.8, 0.4, -0.5, al2, solve_be(0.3, 0.8, al2, ga2), ga2))]
p = 0.45
for name, par in pts:
    kap, s, chi, th, zeta, x, al, be, ga = par
    c = np.sqrt(1 - s * s)
    C, W, k, n = family(*par); tau = chi + al + ga
    B1, B2, T, R = bg.brackets(C, W, eta)
    Ls, mult = lambdas(chi, th, tau)
    print('== %s (kappa,s,chi,th,zeta,x,al,be,ga) = %s: |B1|,|B2| = %.0e %.0e, constraint %.0e, tau %.0e, k = %s'
          % (name, tuple(round(v, 4) for v in par), np.abs(B1).max(), np.abs(B2).max(),
             constraint(chi, th, al, be, ga), abs(tau), np.round(k, 4)))
    N, L = 14, 5
    E = modes(p, 0.37 + 0.2j, N, kap); M = K.M_op(C, W, E)
    cols = [i * N + nn for i in range(40) for nn in range(L + 1)]
    Mc = M[:, cols]; U_, sv, Vh = np.linalg.svd(Mc); ker = Vh[np.sum(sv > 1e-9 * sv[0]):].conj().T
    G = lin.gauge_vectors_R(C, W, E); Gc = G[cols][:, [j for j in range(G.shape[1]) if j // 10 <= L - 1]]
    print('   (a) kernel dim %d, gauge %d, rank[ker|G] %d, |M G| %.0e' % (ker.shape[1], Gc.shape[1],
                                                                       K.rank(np.hstack([ker, Gc])), np.abs(Mc @ Gc).max()))
    ev = {}
    for N in (18, 24):
        ev[N] = pencil_eigs(lambda q0: K.M_op(C, W, modes(p, q0, N, kap)))
    conv = [z for z in ev[18] if abs(z) < 2.5 and np.min(np.abs(ev[24] - z)) < 1e-8]
    cnt = {}; bad = []
    for z in conv:
        best = None
        for j, La in enumerate(Ls):
            l = ((z + La) ** 2 - (p + c * La) ** 2) / (kap * p)
            lr = int(round(l.real))
            d = abs(l - lr)
            if lr % 2 and lr >= -1 and (best is None or d < best[0]):
                best = (d, j, lr)
        if best is None or best[0] > 1e-6:
            bad.append(z); continue
        cnt[(best[1], best[2])] = cnt.get((best[1], best[2]), 0) + 1
    print('   (b) converged eigenvalues %d, assigned %d, unassigned %d [%.0fs]' % (len(conv), len(conv) - len(bad), len(bad), time.time() - t0))
    print('       per (class, l):', dict(sorted(cnt.items())))
    for z in bad:
        print('       unassigned converged eigenvalue %.6f%+.6fi' % (z.real, z.imag))
    worst = 0.0
    for j, La in enumerate(Ls):
        for l in (-1, 1, 3):
            for sg in (1, -1):
                z = -La + sg * np.sqrt((p + c * La) ** 2 + kap * p * l)
                worst = max(worst, np.min(np.abs(ev[24] - z)))
    print('   (c) largest distance of a predicted root (all classes, l = -1, 1, 3) to the N = 24 eigenvalues: %.1e' % worst)
    for j, La in enumerate(Ls):
        print('   (d) class %d Lambda = %+.4f%+.4fi: s^2 Lambda^2 = %+.4f%+.4fi ; p -> 0 roots %s'
              % (j, La.real, La.imag, (s * s * La * La).real, (s * s * La * La).imag,
                 ' '.join('%.4f%+.4fi' % (z.real, z.imag) for z in (-La * (1 - c), -La * (1 + c)))))
    N, Lc = 16, 6
    cols = [i * N + nn for i in range(40) for nn in range(Lc + 1)]
    Mf = lambda q0: K.M_op(C, W, modes(p, q0, N, kap))[:, cols]
    r = K.rank(Mf(0.37 + 0.11j)); rt = Tl.char_roots(Mf, r)
    cc = [0] * len(Ls)
    for z in rt:
        for j, La in enumerate(Ls):
            l = ((z + La) ** 2 - (p + c * La) ** 2) / (kap * p)
            if abs(l - round(l.real)) < 5e-3 and int(round(l.real)) % 2:
                cc[j] += 1; break
    print('   (e) column cut: %d roots, per class %s' % (len(rt), cc), flush=True)
