"""S1. Backgrounds, gauge directions and generic rank (adversary test F3).
Run from this folder: python s1_backgrounds.py > s1_backgrounds_output.txt"""
import numpy as np, sympy as sp
import core
from core import *

rng = np.random.default_rng(11)
BG = [('flat', flat()), ('null-rotation, left-invariant gauge', null_rotation_g1()),
      ('null-rotation, constant-connection gauge', null_rotation_g2()),
      ('Heisenberg', heisenberg()), ('second algebra', second_algebra())]


def eta_derivations(c):
    """dim of {lam in so(3,1): lam is a derivation of the Lie algebra c}."""
    lam = sp.symbols('l0:6'); L = sp.zeros(4, 4)
    eta = sp.diag(-1, 1, 1, 1)
    for n, (a, b) in enumerate(PAIRS):
        L[a, b] += lam[n]; L[b, a] -= lam[n]
    D = L * eta            # D(E_b) = D[a, b] E_a
    cs = [[[sp.nsimplify(c[a, b, d]) for d in range(4)] for b in range(4)] for a in range(4)]
    eqs = []
    for a in range(4):
        for b in range(a + 1, 4):
            for e in range(4):
                lhs = sum(cs[a][b][d] * D[e, d] for d in range(4))
                rhs = sum(D[d, a] * cs[d][b][e] + D[d, b] * cs[a][d][e] for d in range(4))
                eqs.append(sp.expand(lhs - rhs))
    A = sp.Matrix([[sp.diff(e, l) for l in lam] for e in eqs])
    return 6 - A.rank()


for name, (c, w) in BG:
    r1, r2, T, R = background_residual(c, w)
    dirs = [m for m in range(4) if np.abs(c[:, :, m]).max() == 0]
    tsq = np.einsum('abc,xyz,ax,by,cz->', T, T, ETA, ETA, np.linalg.inv(ETA))
    trv = np.einsum('acc->a', T)
    print('==', name)
    print('  Jacobi defect %.1e; background B1, B2 residual %.1e %.1e; |Rbar| %.1e' % (jacobi(c), r1, r2, np.abs(R).max()))
    print('  T_abc T^abc =', round(float(tsq), 12), '; trace T_ac^c =', trv,
          '; eta-derivations (commutant Lorentz labels):', eta_derivations(c) if np.abs(w).max() == 0 else 'n/a in this gauge')
    print('  character directions', dirs, '; rank M(0) (non-derivative coefficient) =', rank(M_of_q(c, w, np.zeros(4))))
    for trial in range(3):
        q = np.zeros(4)
        for m in dirs: q[m] = rng.normal()
        M = M_of_q(c, w, q); G = gauge_vectors(c, w, chars(q))
        print('  q =', q.round(3), ': rank M = %d of 40, rank gauge = %d, |M G| = %.1e, kernel = gauge directions: %s'
              % (rank(M), rank(G), np.abs(M @ G).max(), rank(M) + rank(G) == 40))

c1, w1 = null_rotation_g1(); c2, w2 = null_rotation_g2(-0.5)
T1 = background_residual(c1, w1)[2]; T2 = background_residual(c2, w2)[2]
print('== null rotation: max |T(left-invariant gauge) - T(flat frame, w_a^{12} = -k_a/2)| =', np.abs(T1 - T2).max())

c, w = heisenberg(); N = 12
E = heisenberg_modes(0.7, 0.3, N)
print('== Heisenberg, oscillator modes: representation defect below top level %.1e'
      % np.abs((E[3] @ E[1] - E[1] @ E[3] - E[2])[:N-1, :N-1]).max())
MG = M_op(c, w, E) @ gauge_vectors(c, w, E)
lev = np.repeat(np.arange(N), 10)
print('   |M G| for gauge parameters on levels <= N-5: %.1e' % np.abs(MG[:, lev <= N - 5]).max())

core.set_eta([1, 1, 1, 1])
for name, (c, w) in [BG[1]] + BG[3:]:
    r1, r2, _, _ = core.background_residual(c, w)
    print('== delta contraction,', name, ': background residual %.1e %.1e' % (r1, r2))
