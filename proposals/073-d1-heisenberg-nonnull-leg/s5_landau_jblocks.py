"""S5 (exact over QQ(i) after rational reconstruction, as in 072 s3).  Landau sectors (E_0 = i q0, E_2 = i p,
E_1, E_3 on oscillator levels) of the forty linearised equations at the SO(2)-symmetric rational untilted point
U1 of the family (s = 0, chi = 1/4, th = 1/2, al = ga = 3/4, be = -1/4, zeta = x = 0, tau = 7/4), where the
combined rotation J = n + helicity commutes with the operator (072 jblocks; the coupling of each block to the
other rows of the exact levels, 'leak', is printed).  For each J-block the determinantal divisor D_r is factored
into
   P_{Lambda,l}(q0) = q0^2 - p^2 + 2 Lambda (q0 - p) - kappa p l,  l odd >= -1,
   Lambda in {7i/8 (= i tau/2), 9i/8, 9i/8 +- 1/2, 11i/8 +- 3/4}   (common073.lambdas at this point),
i.e. (q_par + Lambda k)^2 + kappa p l = 0 with k = (1,0,1,0); 'remainder degree 0' means D_r is, up to a constant,
the product of the listed factors.  Points (kappa, p) = (1, 1/2) and (2, 1/4).
Run: python -I -B s5_landau_jblocks.py   (about 10 min)"""
import os, sys, time
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common073 import *
sys.path.insert(0, os.path.normpath(os.path.join(HERE, '..', '072-d1-heisenberg-wider-linearised')))
import jblocks as JB
import sympy as sp
from sympy import QQ_I, Poly

q = JB.q
I = sp.I
LSET = [7 * I / 8, 9 * I / 8, 9 * I / 8 + sp.Rational(1, 2), 9 * I / 8 - sp.Rational(1, 2),
        11 * I / 8 + sp.Rational(3, 4), 11 * I / 8 - sp.Rational(3, 4)]
PAR = dict(s=0.0, chi=0.25, th=0.5, zeta=0.0, x=0.0, al=0.75, be=-0.25, ga=0.75)


def block(basis, kap, p, J, N):
    Pn, Pin, lams = basis
    C, W, k, n = family(float(kap), **PAR)
    Mf = lambda q0: K.M_op(C, W, JB.modes_resc(float(p), q0, N, float(kap)))
    A0, B0, C0 = Tl.quad_coeffs(Mf)
    sel = [(j, J - lams[j]) for j in range(40) if 0 <= J - lams[j] <= N - 3]
    BigP = np.kron(Pn, np.eye(N)); BigPi = np.kron(Pin, np.eye(N))
    ids = [j * N + nn for (j, nn) in sel]
    other = [i for i in range(40 * N) if i not in ids and (i % N) <= N - 3]
    out = []; leak = 0.0
    for X in (A0, B0, C0):
        Y = BigPi @ X @ BigP
        out.append(Y[np.ix_(ids, ids)])
        if other and ids:
            leak = max(leak, float(np.abs(Y[np.ix_(other, ids)]).max()))
    return out, sel, leak


def factor(g, kap, p, lmax):
    rem = g; found = []
    for li, La in enumerate(LSET):
        for l in range(-1, lmax + 1, 2):
            Pc = Poly(q ** 2 - p ** 2 + 2 * La * (q - p) - kap * p * l, q, domain=QQ_I); m = 0
            while True:
                qq, rr = rem.div(Pc)
                if rr.is_zero:
                    rem = qq; m += 1
                else:
                    break
            if m:
                found.append((li, l, m))
    return found, rem


t0 = time.time()
B40 = JB.helicity_basis(JB.rho40())
C, W, k, n = family(1.0, **PAR)
B1, B2, T, R = bg.brackets(C, W, eta)
print('U1: |B1|, |B2| =', np.abs(B1).max(), np.abs(B2).max(), '; constraint', constraint(0.25, 0.5, 0.75, -0.25, 0.75),
      '; classes 0..5 =', [str(L) for L in LSET])
Jmax = 3
for kap, p in [(1, sp.Rational(1, 2)), (2, sp.Rational(1, 4))]:
    print('== kappa = %s, p = %s' % (kap, p), flush=True)
    tot = {}
    for J in range(-3, Jmax + 1):
        mats, sel, leak = block(B40, kap, p, J, max(J, 0) + 6)
        if not sel:
            continue
        r, nn, g, ps = JB.det_divisor(mats)
        found, rem = factor(g, kap, p, 2 * Jmax + 11)
        for li, l, m in found:
            tot[(li, l)] = tot.get((li, l), 0) + m
        print('  J=%2d size %2d rank %2d leak %.0e deg D_r %2d factors (class,l,mult) %s remainder degree %d [%.0fs]'
              % (J, nn, r, leak, g.degree(), found, rem.degree(), time.time() - t0), flush=True)
    lc = 2 * Jmax - 1
    print('  totals over J for l <= %d (class: {l: count}):' % lc,
          {li: {l: v for (lj, l), v in sorted(tot.items()) if lj == li and l <= lc} for li in range(6)}, flush=True)
