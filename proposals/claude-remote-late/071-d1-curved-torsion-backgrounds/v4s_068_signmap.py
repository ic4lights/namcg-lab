"""V4S (071 round 2). Re-verification of the merged 068 sentence at appH L1623 under the sign map
w = -omega between the code normalisation of proposals/068-d1-torsion-nonzero/core.py
(first-order part E_a + 1/2 w_a^{cd} S_cd at u = 1) and the coordinate form of the paragraph on
local SO(3,1) inside the unitary group (e_a^mu omega_mu^{cd} = -w_a^{cd}).
The merged text uses omega: omega_a^{12} = vartheta k_a, k_a = (1,0,0,1), i.e. code w = -vartheta k.
Checks:
 (1) torsion of the constant-frame gauge equals that of the left-invariant null-rotation gauge
     for omega-vartheta = +1/2 (code w = -1/2) and not for omega-vartheta = -1/2; T^2 = 0 there;
 (2) characteristic roots on (q + j vartheta k)^2 = 0, multiplicities 4, 6, 2 for j = 0, +-1, +-2,
     for omega-vartheta in {-1/2, 1/2, 1, 2} (code w = -vartheta) -- the values the text names --
     and also for the opposite signs;
 (3) chains of length at most three (partial multiplicities) and exact rational ranks on each cone
     for omega-vartheta = 1 (code w = -1), the value at which the text states them.
Imports 068 core/tools read-only; bytecode writing is disabled so nothing is written there.
Run: python -I v4s_068_signmap.py"""
import os
import sys
sys.dont_write_bytecode = True
from fractions import Fraction
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
P068 = os.path.join(os.path.dirname(HERE), '068-d1-torsion-nonzero')
sys.path.insert(0, HERE)
import bg  # noqa: E402
sys.path.insert(0, P068)
from core import M_of_q, M_coeffs, null_rotation_g1, null_rotation_g2, rank, NF  # noqa: E402
from tools import char_roots, grouped, partial_mult  # noqa: E402

ETA = np.diag([-1.0, 1.0, 1.0, 1.0])
k = np.array([1.0, 0.0, 0.0, 1.0])
q0 = np.array([0.31, 0.42, -0.45, -0.72])
n = np.array([2.5, -0.57, -0.22, -0.23])
sq = lambda q: q @ ETA @ q

print('== (1) torsion: constant-frame gauge omega_a^{12} = vartheta k_a versus left-invariant gauge')
c1, w1 = null_rotation_g1()
_, _, T1, _ = bg.brackets(c1, w1, ETA)
for th in (0.5, -0.5):
    c2, w2 = null_rotation_g2(-th)                 # code w = -omega
    _, _, T2, _ = bg.brackets(c2, w2, ETA)
    TT = np.einsum('abc,ax,by,cz,xyz->', np.einsum('abc,cd->abd', T2, ETA), ETA, ETA, ETA,
                   np.einsum('abc,cd->abd', T2, ETA))
    print('  omega-vartheta = %+.1f (code w = %+.1f): max|T - T_left-invariant| = %.1e ; T_abc T^abc = %.1e'
          % (th, -th, np.abs(T2 - T1).max(), TT))

print('== (2) characteristic roots, omega-vartheta values (code w = -vartheta)')
allok = True
for th in (-0.5, 0.5, 1.0, 2.0, -1.0, -2.0):
    c, w = null_rotation_g2(-th)
    roots = char_roots(lambda t: M_of_q(c, w, q0 + t * n), 30)
    mult = {}; worst = 0.0; worst_im = 0.0; ok_all = True
    for (re, im), cnt in grouped(roots):
        q = q0 + (re + 1j * im) * n
        x = -sq(q) / (2 * th * (k @ ETA @ q))       # (q + j th k)^2 = q^2 + 2 j th k.q
        j = int(np.floor(x.real + 0.5)); dx = abs(x - j)
        ok_all &= dx < 1e-8; worst = max(worst, dx); worst_im = max(worst_im, abs(im))
        mult.setdefault(j, []).append(cnt)
    allok &= ok_all
    print('  omega-vartheta = %+.1f: roots %d; max|Im t| %.1e; max|x-j| %.1e; all on cones %s; j -> mult %s'
          % (th, len(roots), worst_im, worst, ok_all, dict(sorted(mult.items()))))
print('  ALL ROOTS ON CONES (q + j vartheta k)^2 = 0 WITH MULTIPLICITIES 4,6,6,2,2:', allok)

print('== (3) omega-vartheta = 1 (code w = -1): partial multiplicities and exact ranks on the cones')
th = 1.0
c, w = null_rotation_g2(-th)
rng = np.random.default_rng(5)
nn = np.array([1.0, 0.3, -0.2, 0.5])
for j in (-2, -1, 0, 1, 2):
    v = rng.normal(size=3); nv = np.array([np.linalg.norm(v), *v])
    qj = nv - j * th * k                            # (qj + j th k)^2 = nv^2 = 0
    pm = partial_mult(lambda t: M_of_q(c, w, qj + t * nn), 10)
    print('  j = %+d: cumulative sum_i min(m_i, L), L = 1..4: %s (constant from L = 3 on: chains <= 3: %s)'
          % (j, pm, pm[2] == pm[3]))
M0, M1, M2 = M_coeffs(c, w)


def frac(X):
    out = [[Fraction(float(x)).limit_denominator(64) for x in row] for row in X]
    assert max(abs(float(out[i][jj]) - X[i, jj]) for i in range(X.shape[0]) for jj in range(X.shape[1])) < 1e-12
    return out


M0f, M1f, M2f = frac(M0), {kk: frac(v) for kk, v in M1.items()}, {kk: frac(v) for kk, v in M2.items()}


def exact_rank(q):
    X = [[M0f[i][jj] - sum(q[m] * q[n2] * v[i][jj] for (m, n2), v in M2f.items()) for jj in range(NF)] for i in range(NF)]
    Y = [[sum(q[m] * M1f[m][i][jj] for m in range(4)) for jj in range(NF)] for i in range(NF)]
    A = [X[i] + [-y for y in Y[i]] for i in range(NF)] + [Y[i] + X[i] for i in range(NF)]
    r = 0
    for col in range(2 * NF):
        piv = next((i for i in range(r, len(A)) if A[i][col] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        for i in range(r + 1, len(A)):
            if A[i][col] != 0:
                f = A[i][col] / A[r][col]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        r += 1
    return r // 2


thf = Fraction(1)
qg = [Fraction(3, 7), Fraction(-2, 5), Fraction(1, 3), Fraction(5, 11)]
print('  generic rational q: exact rank', exact_rank(qg))
nvec = [Fraction(13), Fraction(3), Fraction(4), Fraction(12)]
for j in (-2, -1, 0, 1, 2):
    q = [nvec[0] - j * thf, nvec[1], nvec[2], nvec[3] - j * thf]
    print('  q = %s on (q %+d k)^2 = 0: exact rank %d' % ([str(x) for x in q], j, exact_rank(q)))
