"""S4.  Sector p = 0 (characters E_a = i q_a with q_2 = 0, so no truncation) of the forty linearised equations
and of the order-zero operator Q on the family of common073.
 (a) numerical: for each characteristic root q0 at fixed (q1, q3) the number
       Lambda = -(q.q) / (2 k.q)   (so that (q + Lambda k)^2 = 0, k null)
     is computed; at three (q1, q3) the set of values is the same and equals common073.lambdas (tau, chi, th),
     at untilted (s = 0) and tilted (s != 0) points;
 (b) exact over QQ(i) at the rational untilted point U1 (kappa = 1, s = 0, chi = 1/4, th = 1/2, al = ga = 3/4,
     be = -1/4, tau = 7/4, rho = 3/4) and at U1 with zeta = 1/2, x = -1/3, for (q1, q3) = (1/2, 1/3): the
     determinantal divisor D_r of M(q0) (gcd of two random compressions to the generic rank, 072 jblocks.det_divisor,
     entries rationally reconstructed from double precision) factors completely into
       q0^2 + 2 Lambda q0 - (q1^2 + q3^2),  Lambda in {7i/8, 9i/8, 9i/8 +- 1/2, 11i/8 +- 3/4}.
Run: python -I -B s4_p0_cones.py"""
import os, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common073 import *
sys.path.insert(0, os.path.normpath(os.path.join(HERE, '..', '072-d1-heisenberg-wider-linearised')))
import jblocks as JB
import sympy as sp
from sympy import QQ_I, Poly


def lam_values(C, W, k, q1, q3, op):
    if op == 'forty':
        Mf = lambda q0: K.M_of_q(C, W, [q0, q1, 0, q3])
    else:
        Mf = lambda q0: lin.Qop(C, W, K.chars([q0, q1, 0, q3]))
    r = K.rank(Mf(0.37 + 0.11j)); rt = Tl.char_roots(Mf, r)
    q = lambda z: np.array([z, q1, 0, q3])
    return r, [-(q(z) @ etai @ q(z)) / (2 * (k @ etai @ q(z))) for z in rt]


def solve_be(chi, th, al, ga):
    A = -2; B = -2 * th; Cc = th ** 2 - al ** 2 - ga ** 2 + 2 * chi * (al + ga)
    return (-B - np.sqrt(B * B - 4 * A * Cc)) / (2 * A)


print('== (a) numerical Lambda sets')
pts = []
pts.append(('U2  s=0  chi=0   th=1  al=3/5 be=0 ga=4/5 zeta=1/2 x=-1/3', (1.0, 0.0, 0.0, 1.0, 0.5, -1 / 3, 0.6, 0.0, 0.8)))
al, ga = 0.2, -0.3; be = solve_be(0.4, 1.3, al, ga)
pts.append(('G1  s=0  chi=0.4 th=1.3 al=0.2 ga=-0.3 zeta=0.5 x=-0.7', (1.0, 0.0, 0.4, 1.3, 0.5, -0.7, al, be, ga)))
pts.append(('T1  s=3/5 chi=0 th=1 al=-1/sqrt2 be=0 ga=1/sqrt2 zeta=1/2 x=-1/3', (1.0, 0.6, 0.0, 1.0, 0.5, -1 / 3, -2 ** -0.5, 0.0, 2 ** -0.5)))
ga = 0.1; al = -0.3 - ga; be = solve_be(0.3, 0.8, al, ga)
pts.append(('T2  s=3/5 chi=0.3 th=0.8 ga=0.1 al=-chi-ga zeta=0.4 x=-0.5', (1.0, 0.6, 0.3, 0.8, 0.4, -0.5, al, be, ga)))
for name, par in pts:
    kap, s, chi, th, zeta, x, al, be, ga = par
    C, W, k, n = family(*par)
    B1, B2, T, R = bg.brackets(C, W, eta); tau = chi + al + ga
    pred, mult = lambdas(chi, th, tau)
    print(' %s: |B1|,|B2| = %.0e %.0e, constraint %.0e, tau = %.4f' % (name, np.abs(B1).max(), np.abs(B2).max(),
                                                                       constraint(chi, th, al, be, ga), tau))
    for op in ('Q', 'forty'):
        dev_all = 0.0; counts = None
        for (q1, q3) in [(0.3, 0.1), (0.7, -0.4), (1.3, 0.5)]:
            r, Ls = lam_values(C, W, k, q1, q3, op)
            cnt = [0] * len(pred); dev = 0.0
            for La in Ls:
                d = [abs(La - P) for P in pred]; j = int(np.argmin(d)); cnt[j] += 1; dev = max(dev, d[j])
            dev_all = max(dev_all, dev); counts = cnt
        print('    %-5s rank %d, roots per class %s (expected 2 x %s for forty), largest |Lambda - predicted| %.1e'
              % (op, r, counts, mult, dev_all))
print('    (for Q the class iota/2 carries all 4 roots; multiple roots split numerically by up to ~1e-2 in Lambda)')

print('== (b) exact determinantal divisor at p = 0')
q = sp.Symbol('q0')
for name, zeta, x in [('U1', 0.0, 0.0), ('U1z', 0.5, -1 / 3)]:
    par = (1.0, 0.0, 0.25, 0.5, zeta, x, 0.75, -0.25, 0.75)
    C, W, k, n = family(*par)
    q1, q3 = 0.5, 1 / 3
    Mf = lambda q0: K.M_of_q(C, W, [q0, q1, 0, q3])
    mats = Tl.quad_coeffs(Mf)
    r, nn, g, ps = JB.det_divisor(list(mats))
    Q13 = sp.Rational(1, 4) + sp.Rational(1, 9)
    I = sp.I
    Lset = [7 * I / 8, 9 * I / 8, 9 * I / 8 + sp.Rational(1, 2), 9 * I / 8 - sp.Rational(1, 2),
            11 * I / 8 + sp.Rational(3, 4), 11 * I / 8 - sp.Rational(3, 4)]
    rem = g; found = []
    for La in Lset:
        Pc = Poly(q ** 2 + 2 * La * q - Q13, q, domain=QQ_I); m = 0
        while True:
            qq, rr = rem.div(Pc)
            if rr.is_zero:
                rem = qq; m += 1
            else:
                break
        found.append((str(La), m))
    print(' %s: size %d, generic rank %d, degree of D_r %d, factors (Lambda, multiplicity) %s, remainder degree %d'
          % (name, nn, r, g.degree(), found, rem.degree()))
