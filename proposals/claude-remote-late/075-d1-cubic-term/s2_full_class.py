"""075 s2: the first-order equivariant class with full SO(3,1) fibre and c != 0.

(1) Backgrounds of 068/071/072/073: their section values do not solve the section equations at all fibre
    points once c != 0 (the lemma of s1 says no deformation can: [D_a, D_b] must vanish).
(2) Flat point, equivariant fluctuations (the 40 fields h, omega of the preceding paragraphs), plane waves:
    the section equations must hold with w = u^{-1} v for every fibre point u.  Stacking random u, the kernel
    is the 10 gauge directions at generic, null and zero-free q, against 10 + 14 at null q for c = 0.
    The kernel equals the kernel of the linearised (T, R), i.e. delta[D_a, D_b] = 0.
(3) Order-zero field: CFJ-type operator with w = u^{-1} v stacked: kernel = 1 gauge direction (A ~ q) at q != 0.
"""
import os, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import common075 as C
K = C.K

rng = np.random.default_rng(7501)
c = 0.9
vs = {'timelike': np.array([1.0, 0, 0, 0]), 'spacelike': np.array([0, 0, 0, 1.0]), 'null': np.array([1.0, 0, 0, 1.0])}

# (1) backgrounds of the preceding paragraphs
import importlib
sys.path.insert(0, os.path.normpath(os.path.join(C.HERE, '..', '071-d1-curved-torsion-backgrounds')))
bgs = {'Heisenberg (068)': K.heisenberg(1.0), 'null rotation g2 (068)': K.null_rotation_g2(0.5)}
try:
    import lin as L071
    bgs['family (i) (071)'] = L071.bg_F()
    bgs['Heisenberg + connection (071/072)'] = L071.bg_H(1.0, 1.0, 0.3)
except Exception as e:  # pragma: no cover
    print('071 import failed:', e)
print('(1) background residuals (max over 8 random fibre points) at c = 0 and c =', c)
for name, (cb, wb) in bgs.items():
    r0 = C.background_residual_c(cb, wb, np.zeros(4))
    for vn, v in vs.items():
        r = max(max(C.background_residual_c(cb, wb, c * np.linalg.solve(C.rand_lorentz(rng), v))) for _ in range(8))
        print(f'    {name:36s} c=0: {max(r0):.1e}   c!=0, v {vn:9s}: {r:.3f}')

# (2) flat point
cb, wb = K.flat()
qs = {'generic': np.array([0.7, -0.3, 0.5, 1.1]), 'null': np.array([1.0, 0.6, 0.0, 0.8]),
      'timelike': np.array([1.3, 0.2, -0.1, 0.4]), 'spacelike': np.array([0.2, 1.0, 0.5, -0.3])}
print('(2) flat point, kernel dimension of the 40 linearised equations')
for qn, q in qs.items():
    E = K.chars(q)
    k0 = 40 - C.rank(C.M_c(cb, wb, E, np.zeros(4)))[0]
    G = K.gauge_vectors(cb, wb, E)
    line = f'    q {qn:9s} (q^2 = {q @ C.etai @ q:+.2f}):  c = 0: {k0:2d}  gauge rank {np.linalg.matrix_rank(G)}'
    for vn, v in vs.items():
        Ms = np.vstack([C.M_c(cb, wb, E, c * np.linalg.solve(C.rand_lorentz(rng), v)) for _ in range(6)])
        kern = 40 - C.rank(Ms)[0]
        # gauge directions solve the stacked system
        gres = np.abs(Ms @ G).max()
        line += f' | v {vn}: {kern:2d} (gauge residual {gres:.0e})'
    print(line)
    # kernel of the linearised (T, R) map
    TR = np.zeros((64 + 256, 40), dtype=complex)
    for n in range(40):
        vec = np.zeros(40); vec[n] = 1
        _, _, T, R = K.brackets(cb, wb, E, vec)
        TR[:, n] = np.concatenate([T[1].reshape(-1), R[1].reshape(-1)])
    print(f'      kernel of delta(T, R): {40 - C.rank(TR)[0]}')
# constant fluctuations q = 0
E = K.chars(np.zeros(4))
Ms = np.vstack([C.M_c(cb, wb, E, c * np.linalg.solve(C.rand_lorentz(rng), vs['timelike'])) for _ in range(6)])
print('    q = 0: kernel of the stacked system', 40 - C.rank(Ms)[0], '(constant frame deformations h: 16, omega = 0)')

# (3) order-zero field
print('(3) order-zero field, stacked over fibre points: kernel dimension (gauge A ~ q gives 1)')
for qn, q in qs.items():
    for vn, v in vs.items():
        Ms = np.vstack([C.cfj_matrix(q, c * np.linalg.solve(C.rand_lorentz(rng), v)) for _ in range(6)])
        print(f'    q {qn:9s} v {vn:9s}: {4 - C.rank(Ms)[0]}', end='')
    print()
