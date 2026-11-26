"""S3 (exact over QQ(i) after rational reconstruction; see jblocks.py).  Wider Heisenberg family at
zeta = x = 0, at two rational parameter points with chi != 0 and one with chi = 0.  For each J-block of the
order-zero operator Q and of the forty equations: generic rank, degree of the determinantal divisor D_r and
its complete factorisation into
   P_{c,l}(q0) = q0^2 - p^2 + i c chi (q0 - p) - kappa p l,   c in {-1, 1, 3}, l odd >= -1
('remainder degree 0' means D_r is, up to a constant, the product of the listed factors).
Totals over J are printed per (c, l) for l <= 2 J_max - 1, where every block that can contain the level is
included on the observed pattern (block J >= 0 contains only the levels 2J-1, 2J+1, 2J+3; J >= -2
since the helicities are >= -2).
Run: python -I -B s3_exact_jblocks.py"""
import os, sys, time
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from jblocks import *

t = time.time()
B40 = helicity_basis(rho40())
BQ = helicity_basis(R13.copy())
print('helicities of the 40 components:', {l: B40[2].count(l) for l in sorted(set(B40[2]))},
      '; of A_b:', {l: BQ[2].count(l) for l in sorted(set(BQ[2]))})
Jmax = 3
for kap, p, chi in [(1, sp.Rational(1, 2), sp.Rational(1, 2)), (2, sp.Rational(1, 4), -sp.Rational(1, 3)),
                    (1, sp.Rational(1, 2), 0)]:
    print('== kappa = %s, p = %s, chi = %s, zeta = x = 0' % (kap, p, chi), flush=True)
    for name, op, nc, basis, cs in [('Q', lin.Qop, 4, BQ, (1,) if chi else (0,)),
                                    ('forty', K.M_op, 40, B40, (-1, 1, 3) if chi else (0,))]:
        tot = {}
        for J in range(-3, Jmax + 1):
            mats, sel, leak = block(op, nc, basis, float(kap), float(p), float(chi), J, max(J, 0) + 6)
            if not sel:
                continue
            r, n, g, ps = det_divisor(mats)
            found, rem = factor_on_levels(g, kap, p, chi, cs, lmax=2 * Jmax + 11)
            for c, l, m in found:
                tot[(c, l)] = tot.get((c, l), 0) + m
            print('  %-5s J=%2d size %2d rank %2d leak %.0e deg D_r %2d factors (c,l,mult) %s remainder degree %d [%.0fs]'
                  % (name, J, n, r, leak, g.degree(), found, rem.degree(), time.time() - t), flush=True)
        lc = 2 * Jmax - 1
        print('  %s totals over J for l <= %d:' % (name, lc), {k: v for k, v in sorted(tot.items()) if k[1] <= lc}, flush=True)
