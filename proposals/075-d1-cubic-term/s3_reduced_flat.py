"""075 s3: classes whose fibre is the stabiliser H = Stab(v) (the variant on which the cubic term is consistent),
flat point, equivariant fluctuations h (16) and omega in Lie(H) (4 x 3), plane waves exp(i q.y).
In section values w = v at every fibre point, since H fixes v.

Checks:
 (1) the S-components of the 40 linearised equations outside Lie(H) vanish identically on these fields;
 (2) gauge directions (3 local H rotations + 4 diffeomorphisms) are in the kernel; generic kernel = 7;
 (3) characteristic roots q0 at fixed spatial k: every root is a root of the CFJ-type one-form operator
     M_b^d = -(q^2 delta_b^d - q_b q^d) + i eps_b^{cd}_f (c w)^f q_c, with the multiplicity 7 (= 3 connection
     one-forms + 4 frame one-forms) times that of the one-form operator;
 (4) closed form of the one-form dispersion, (q^2)^2 = c^2 ((q.w)^2 - q^2 w^2), checked at random q;
 (5) timelike / spacelike / null w: limits of the roots as k -> 0 (gap or no gap) and reality.
"""
import os, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import scipy.linalg as sl
import common075 as C
K = C.K

c = 0.9
vs = {'timelike': np.array([1.0, 0, 0, 0]), 'spacelike': np.array([0, 0, 0, 1.0]), 'null': np.array([1.0, 0, 0, 1.0])}
cb, wb = K.flat()


def Mred(q, v):
    Hb = C.stabiliser_basis(v)
    P, Q = C.reduction(Hb, 1)
    M40 = C.M_c(cb, wb, K.chars(q), c * v)
    return Q @ M40 @ P, M40 @ P, Hb, P


def roots_q0(Mfun, n, r, seeds=(1, 2, 3)):
    A = Mfun(0.0); Pp = Mfun(1.0); Mm = Mfun(-1.0)
    B = (Pp - Mm) / 2; Cq = (Pp + Mm) / 2 - A
    res = []
    for sd in seeds:
        g = np.random.default_rng(sd)
        Pr = g.normal(size=(r, n)); Vc = g.normal(size=(n, r))
        a, b, cc = [Pr @ X @ Vc for X in (A, B, Cq)]
        Z = np.zeros((r, r)); I = np.eye(r)
        ev = sl.eig(np.block([[Z, I], [-a, -b]]), np.block([[I, Z], [Z, cc]]), right=False)
        res.append(ev[np.isfinite(ev) & (np.abs(ev) < 1e6)])
    base = res[0]
    return np.array([x for x in base if all(np.abs(o - x).min() < 2e-4 * (1 + abs(x)) for o in res[1:])])


def cfj_roots(k, w):
    """Roots q0 of det' of the one-form operator: solve (q^2)^2 - c^2((q.w)^2 - q^2 w^2) = 0 for q0."""
    import numpy.polynomial.polynomial as Pl
    kk = np.asarray(k, float)
    wl = C.eta @ (c * w)
    # q = (q0, k) lower components; q^2 = -q0^2 + k^2 ; q.w = q0 w^0 + k.w^i  (w upper, q lower)
    q2 = np.array([kk @ kk, 0.0, -1.0])
    qw = np.array([kk @ (c * w)[1:], (c * w)[0]])
    w2 = (c * w) @ wl
    poly = Pl.polysub(Pl.polymul(q2, q2), Pl.polysub(Pl.polymul(qw, qw), w2 * q2))
    return np.roots(poly[::-1])


rng = np.random.default_rng(7503)
for vn, v in vs.items():
    print(f'=== w {vn} = {v}')
    q = rng.normal(size=4)
    Mr, Mfull, Hb, P = Mred(q, v)
    # (1) S-components outside Lie(H)
    S_out = Mfull[16:].reshape(4, 6, -1)
    proj = np.eye(6) - Hb @ np.linalg.pinv(Hb)
    print('  (1) S-components outside Lie(H):', f'{np.abs(np.einsum("xy,ayn->axn", proj, S_out)).max():.1e}')
    # (2) gauge directions
    G = K.gauge_vectors(cb, wb, K.chars(q))
    # local H rotations: combinations of the six rotation columns with lambda in Lie(H)
    Grot = G[:, :6] @ Hb
    Gh = np.column_stack([Grot] + [G[:, j] for j in range(6, 10)])
    Ghr = np.linalg.pinv(P) @ Gh
    print('  (2) gauge residual', f'{np.abs(Mr @ Ghr).max():.1e}', ' gauge rank', np.linalg.matrix_rank(Ghr),
          ' kernel at random q:', Mr.shape[1] - C.rank(Mr)[0], ' fields', Mr.shape[1])
    # (4) closed form of the one-form operator at random q
    for _ in range(3):
        qq = rng.normal(size=4) + 0j
        M1 = C.cfj_matrix(qq, c * v)
        qu = C.etai @ qq
        q2 = qq @ qu
        lhs = q2 ** 2
        qw = qq @ v * c
        rhs = (qw ** 2 - q2 * (c * v) @ C.eta @ (c * v))
        ev = np.linalg.eigvals(M1)
        ev = ev[np.argsort(np.abs(ev))][1:]
        print('  (4) prod of nonzero eigenvalues / [ -q^2 ((q^2)^2 - c^2((q.w)^2 - q^2 w^2)) ] =',
              f'{(np.prod(ev) / (-q2 * (lhs - rhs))).real:.6f}')
    # (3), (5) roots along k
    for k in ([0.3, 0.4, 0.5], [0.0, 0.0, 0.6], [0.6, 0.0, 0.0], [0.05, 0.02, 0.03], [0.0, 0.0, 0.01], [0.01, 0.0, 0.0]):
        k = np.array(k)
        Mfun = lambda t: Mred(np.array([t, *k]), v)[0]
        n = Mr.shape[1]
        r = n - 7
        rts = roots_q0(Mfun, n, r)
        cr = cfj_roots(k, v)
        # every root of the 28-field system is a one-form root; count multiplicities
        mult = [int(np.sum(np.abs(rts - z) < 1e-3 * (1 + abs(z)))) for z in cr]
        stray = [z for z in rts if np.abs(cr - z).min() > 1e-3 * (1 + abs(z))]
        crs = ', '.join(f'{z.real:+.4f}{z.imag:+.4f}i' for z in sorted(cr, key=lambda z: (z.real, z.imag)))
        print(f'  (3) k={k}: {len(rts)} roots; one-form roots [{crs}]; multiplicities {mult}; roots off them: {len(stray)}')
