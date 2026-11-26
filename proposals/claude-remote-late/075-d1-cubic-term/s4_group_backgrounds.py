"""075 s4: exact curved backgrounds with c != 0 in the classes with fibre Stab(v), vanishing connection.

 (A) timelike v = e_0, H = SO(3): base R x SU(2), [E_i, E_j] = kappa eps_ijk E_k (i,j,k = 1,2,3), E_0 central.
 (B) spacelike v = e_3, H = SO(2,1): base SL(2,R)~ x R, [E_a, E_b] = kappa eps_ab^d_3 E_d (a,b,d = 0,1,2), E_3 central.
For each: residual of the first two brackets with the cubic term (section values, w = v) as a function of kappa,
the root kappa = c/2 (sign fixed by eps^{0123} = +1), the order-zero field (t = 1/2 T_ac^c = 0, F = 0), and the
failure in the full SO(3,1) class (w = u^{-1} v at random u).
Then (C): linearised equations of the 28 fields of the SO(3) class on (A), in the spin-j sectors of L^2(SU(2)),
E_0 = i q0, E_i = -i kappa J_i^{(j)}; characteristic q0 (rank drop below the generic rank, gauge kernel 7(2j+1)).
These are levels of a background whose spatial sections are compact, of radius 2/|kappa| = 4/|c|.
"""
import os, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import itertools
import numpy as np
import scipy.linalg as sl
import common075 as C
K = C.K

c = 0.9
rng = np.random.default_rng(7504)


def su2(kap):
    cb = np.zeros((4, 4, 4))
    for i, j, k in itertools.permutations([1, 2, 3]):
        cb[i, j, k] = kap * np.linalg.det(np.eye(3)[[i - 1, j - 1, k - 1]])
    return cb


def sl2(kap):
    """[E_a,E_b] = kap eps_{ab}^{d}{}_{3} E_d, a,b,d in {0,1,2} (indices of eps raised with eta)."""
    e = np.einsum('abxy,xd->abdy', C.epsL, C.etai)[:, :, :, 3]
    cb = np.zeros((4, 4, 4))
    for a, b, d in itertools.product(range(3), repeat=3):
        cb[a, b, d] = kap * e[a, b, d]
    return cb


for name, alg, v in (('(A) R x SU(2), timelike v', su2, np.array([1.0, 0, 0, 0])),
                     ('(B) SL(2,R) x R, spacelike v', sl2, np.array([0, 0, 0, 1.0]))):
    print(name)
    print('    Jacobi residual', K.jacobi(alg(1.0)))
    for kap in (0.3, c / 2, -c / 2, 1.0):
        r = C.background_residual_c(alg(kap), np.zeros((4, 4, 4)), c * v)
        r0 = C.background_residual_c(alg(kap), np.zeros((4, 4, 4)), np.zeros(4))
        print(f'    kappa = {kap:+.3f}: residual with c = {c}: {max(r):.2e}   (c = 0: {max(r0):.2e})')
    kap = c / 2
    cb = alg(kap)
    T = -cb
    print('    trace T_ac^c =', np.abs(np.einsum('acc->a', T)).max(), ' T_abc T^abc =',
          f'{np.einsum("abc,ax,by,cz,xyz->", T, C.etai, C.etai, C.eta, T):+.4f}', ' (kappa^2 =', kap ** 2, ')')
    r = max(max(C.background_residual_c(cb, np.zeros((4, 4, 4)), c * np.linalg.solve(C.rand_lorentz(rng), v)))
            for _ in range(6))
    print(f'    full SO(3,1) class (w = u^-1 v, 6 random u): residual {r:.3f}')

# (C) linearised levels on (A)
print('(C) R x SU(2) at kappa = c/2, SO(3) class, spin-j sectors')
kap = c / 2
cb = su2(kap)
v = np.array([1.0, 0, 0, 0])
Hb = C.stabiliser_basis(v)


def Jmats(j):
    m = np.arange(j, -j - 1, -1); d = len(m)
    Jp = np.zeros((d, d))
    for k in range(1, d):
        Jp[k - 1, k] = np.sqrt(j * (j + 1) - m[k] * (m[k] + 1))
    return [(Jp + Jp.T) / 2, (Jp - Jp.T) / 2j, np.diag(m).astype(complex)]


def Eop(j, q0):
    J = Jmats(j); d = len(J[0])
    return np.array([1j * q0 * np.eye(d)] + [-1j * kap * Ji for Ji in J])


def Mred(j, q0):
    E = Eop(j, q0); N = E.shape[-1]
    P, Q = C.reduction(Hb, N)
    return Q @ C.M_c(cb, np.zeros((4, 4, 4)), E, c * v) @ P


for j in (0.0, 0.5, 1.0, 1.5):
    E = Eop(j, 0.37)
    comm = max(np.abs(E[a] @ E[b] - E[b] @ E[a] - np.einsum('d,dnm->nm', cb[a, b], E)).max()
               for a in range(4) for b in range(4))
    N = E.shape[-1]
    n = 28 * N
    Mx = Mred(j, 0.37)
    kern = n - C.rank(Mx)[0]
    A = Mred(j, 0.0); Pp = Mred(j, 1.0); Mm = Mred(j, -1.0)
    B = (Pp - Mm) / 2; Cq = (Pp + Mm) / 2 - A
    r = n - kern
    res = []
    for sd in (1, 2):
        g = np.random.default_rng(sd)
        Pr = g.normal(size=(r, n)); Vc = g.normal(size=(n, r))
        a, b, cc = [Pr @ X @ Vc for X in (A, B, Cq)]
        Z = np.zeros((r, r)); I = np.eye(r)
        ev = sl.eig(np.block([[Z, I], [-a, -b]]), np.block([[I, Z], [Z, cc]]), right=False)
        res.append(ev[np.isfinite(ev) & (np.abs(ev) < 1e6)])
    rts = np.array([x for x in res[0] if np.abs(res[1] - x).min() < 1e-4 * (1 + abs(x))])
    vals = {}
    for z in rts:
        key = (round(z.real, 4) + 0.0, round(z.imag, 4) + 0.0)
        vals[key] = vals.get(key, 0) + 1
    print(f'  j = {j}: [E,E] = cbar E residual {comm:.1e}; generic kernel {kern} (= 7(2j+1) = {7 * N}); '
          f'{len(rts)} roots, max |Im q0| = {np.abs(rts.imag).max() if len(rts) else 0:.4f}')
    nz = rts[np.abs(rts) > 1e-6]
    ll = np.arange(0, 12) / 2
    dev = max(np.min(np.abs((z / kap) ** 2 - ll * (ll + 1))) for z in nz) if len(nz) else 0.0
    print(f'     nonzero roots: max distance of (q0/kappa)^2 from the set l(l+1), l in N/2: {dev:.1e}')
    print('     roots q0/kappa (value: count):', ', '.join(f'{k[0]/kap:+.4f}{k[1]/kap:+.4f}i:{m}' for k, m in sorted(vals.items())))

# (D) unified form: cbar_ab^d = 1/2 eps_ab^d_f vsf^f  (vsf = c v), vanishing connection
print('(D) cbar_ab^d = 1/2 eps_ab^d_f vsf^f for vsf = c v')
for name, v in (('timelike', np.array([1.0, 0, 0, 0])), ('spacelike', np.array([0, 0, 0, 1.0])),
                ('null', np.array([1.0, 0, 0, 1.0])), ('timelike boosted', np.array([1.25, 0.75, 0, 0]))):
    vsf = c * v
    cb = 0.5 * np.einsum('abxf,xd,f->abd', C.epsL, C.etai, vsf)
    jac = K.jacobi(cb)
    r = C.background_residual_c(cb, np.zeros((4, 4, 4)), vsf)
    cen = np.abs(np.einsum('abd,a->bd', cb, vsf)).max()
    print(f'    {name:16s}: Jacobi {jac:.1e}, residual {max(r):.1e}, |vsf^a cbar_ab^d| = {cen:.1e},'
          f' T_abc T^abc = {np.einsum("abc,ax,by,cz,xyz->", cb, C.etai, C.etai, C.eta, cb):+.4f}')
