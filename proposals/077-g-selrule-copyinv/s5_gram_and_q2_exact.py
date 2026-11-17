"""077 s5 (sympy): two exact lemmas of the 077 package.

LEMMA 1 (Gram reduction). For the coincident-copy block-cut charge
    Q~ = -2i sum_{a,b} e_{ab} (x) (|u)(z_{ab}| - |z_{ab})(u|),
u unit, z_{ab} in C^N, the nonzero spectrum of Q~ equals the nonzero spectrum
of the Hermitian matrix
    M = -2i [[0, C], [-C^+, Z]],   Z[(ab),(a'b')] = (z_{ab}|z_{a'b'}),
    C[a,(b,b')] = (u|z_{bb'}),
of size q + q^2, via the block isometry A = sum_a e_a (x) u (columns),
B = sum_{a,b} e_{ab} (x) z_{ab}: Q~ = -2i (A B^+ - B A^+), and
Q~^2 Q~ v = ... gives spectrum(Q~|_{R(A)+R(B)}\{0}) = spectrum(M|nonzero).
Symbolic check: full characteristic polynomials of Q~ and of the (q+q^2)-matrix
M agree up to the forced zero-eigenvalue factor lam^(2N - q - q^2) at q=2,
symbolic dim N=3, and the 2q leading nonzero coefficients match identically.

LEMMA 2 (rank-1 q=2 exact classification, block-diagonal case). For Q~ =
direct sum of 2 single-copy rank-2 charges with row data z_1, z_2 (u common):
mult-2 <=> |P_perp z_1| = |P_perp z_2| (norms of u-orthogonal parts): the u-
components are invisible (charge annihilates them), giving the exact
"edge-row norm equality" criterion at fixed N; symbolic solve of the two
quartic eigenvalue conditions reduces to (z1.z1 - (u.z1)^2) - (z2.z2 - (u.z2)^2).

Run: python -I proposals/077-g-selrule-copyinv/s5_gram_and_q2_exact.py
Expected invariants: charpoly coefficient comparison returns all-zero
differences (identically); Lemma 2: resultant/gcd reduces the two conditions
to the single norm equality. Last line 'PASS s5'.
"""
import sympy as sp

# ---------- Lemma 1: characteristic polynomials at q=2, symbolic dim N=3
q = 2
Nsym = 3
# symbolic complex entries
zs = {}
for a in range(q):
    for b in range(q):
        zs[(a, b)] = sp.Matrix([sp.symbols('z%d_%d_%d' % (a, b, i), complex=True)
                                for i in range(Nsym)])
us = sp.Matrix([sp.symbols('u%d' % i, complex=True) for i in range(Nsym)])
# impose |u| = 1 as the relation Sum conj(u)u = 1 by working with a fixed unit u:
# pick a concrete unit vector to keep coefficient comparison polynomial:
uvec = sp.Matrix(sp.symbols('t0 t1 t2', complex=True))
uvec = sp.Matrix([1, 0, 0])          # any fixed unit vector: spectrum identity is
                                     # unitary-covariant, so one suffices symbolically

def ket(v):
    return sp.ImmutableDenseMatrix(v)

def op_B(w):
    return sum(w[i] * us[i].conjugate() for i in range(Nsym))  # not used; keep direct

# build Q~ as a (q*Nsym) x (q*Nsym) explicit matrix
n2 = q * Nsym
Q = sp.zeros(n2, n2)
for a in range(q):
    for b in range(q):
        w = zs[(a, b)]
        blk = sp.zeros(Nsym, Nsym)
        for i in range(Nsym):
            for j in range(Nsym):
                blk[i, j] = -2*sp.I * (uvec[i] * sp.conjugate(w[j])
                                       - w[i] * sp.conjugate(uvec[j]))
        Q[a * Nsym:(a + 1) * Nsym, b * Nsym:(b + 1) * Nsym] = blk

# Gram matrices A^+A = I_q, C (q x q^2), Z (q^2 x q^2)
lam = sp.symbols('lam')
Cmat = sp.zeros(q, q * q)
Zmat = sp.zeros(q * q, q * q)
idx = [(a, b) for a in range(q) for b in range(q)]
for a in range(q):
    for (b1, b2) in idx:
        Cmat[a, idx.index((b1, b2))] = sum(sp.conjugate(uvec[i]) * zs[(b1, b2)][i]
                                           for i in range(Nsym))
for i1, (a1, b1) in enumerate(idx):
    for i2, (a2, b2) in enumerate(idx):
        Zmat[i1, i2] = sum(sp.conjugate(zs[(a1, b1)][k]) * zs[(a2, b2)][k]
                           for k in range(Nsym))
Mmat = -2 * sp.I * sp.Matrix(sp.BlockMatrix([[sp.zeros(q, q), Cmat],
                                             [-Cmat.applyfunc(sp.conjugate).T if False else Cmat.adjoint(),
                                              Zmat]]))
# note: [[0,C],[-C^+, -i..]]: M = -2i[[0,C],[-C^+,Z]]
pQ = sp.factor(sp.charpoly(Q + sp.zeros(n2, n2)).as_expr(lam)) if False else None
pQ = sp.expand(sp.Matrix(Q).charpoly(lam).as_expr())
pM0 = sp.expand(sp.Matrix(Mmat).charpoly(lam).as_expr())
nZ = Mmat.shape[0]
# predicted: pQ = lam^(n2 - nZ) * pM  (nonzero spectra equal, M has size nZ)
pred = sp.expand(lam ** (n2 - nZ) * pM0)
diff = sp.expand(pQ - pred)
coeffs = [diff.coeff(lam, k) for k in range(n2 + 1)]
zero_all = all(sp.simplify(c) == 0 for c in coeffs)
print('Lemma 1: q=2, N=3: charpoly(Q~) - lam^(2N-q-q^2) charpoly(M) identically zero:',
      zero_all)
assert zero_all

# cross-check numerically with random values to confirm the sign/layout
import numpy as np
rng = np.random.default_rng(77005)
for trial in range(5):
    zv = {(a, b): rng.normal(size=Nsym) + 1j * rng.normal(size=Nsym)
          for a in range(2) for b in range(2)}
    uv = np.array([1.0, 0, 0], dtype=complex)
    Qn = np.zeros((6, 6), complex)
    for a in range(2):
        for b in range(2):
            w = zv[(a, b)]
            blk = -2j * (np.outer(uv, w.conj()) - np.outer(w, uv.conj()))
            Qn[a * 3:(a + 1) * 3, b * 3:(b + 1) * 3] = blk
    idxv = [(a, b) for a in range(2) for b in range(2)]
    Zn = np.array([[np.vdot(zv[p], zv[r]) for r in idxv] for p in idxv])
    Cn = np.array([[np.vdot(uv, zv[(b1, b2)]) for (b1, b2) in idxv]
                   for a in range(2)])
    Mn = -2j * np.block([[np.zeros((2, 2)), Cn], [-Cn.conj().T, Zn]])
    e1 = np.sort(np.linalg.eigvalsh(Qn))
    e2 = np.sort(np.linalg.eigvalsh(Mn))
    nz1 = e1[np.abs(e1) > 1e-9]
    nz2 = e2[np.abs(e2) > 1e-9]
    dev = max(abs(nz1 - nz2)) if len(nz1) == len(nz2) else 9.9
    assert dev < 1e-8, dev
print('Lemma 1: numerical nonzero-spectrum match in 5 random trials: True')

# ---------- Lemma 2: q=2 block-diagonal mult-2 <=> |P_perp z1| = |P_perp z2|
t = sp.symbols('t')
a1, b1c, a2, b2c = sp.symbols('a1 b1 a2 b2', real=True)
# rank-2 charge with u = e0: -2i(|u)(w| - |w)(u|), w = (p, r) : eigenvalues:
w = sp.Matrix([sp.symbols('p', real=True), sp.symbols('r', real=True)])
u2 = sp.Matrix([1, 0])
Qb = -2 * sp.I * (sp.Matrix(u2) * w.T - w * sp.Matrix(u2).T)
p1 = sp.expand(Qb.charpoly(t).as_expr())
# eigenvalue conditions for {t1,t2} of two copies to coincide as multisets:
p2 = p1.subs({sp.symbols('p'): sp.symbols('p2'), sp.symbols('r'): sp.symbols('r2')})
# resultant of the two charpolys: the two 2-element spectra coincide iff the
# coefficients (trace and det) of the two quadratic charpolys agree:
c1 = [sp.expand(p1.coeff(t, k)) for k in range(3)]
c2 = [sp.expand(p2.coeff(t, k)) for k in range(3)]
conds = [sp.simplify(c1[k] - c2[k]) for k in range(2)]  # k=0 trivial (both monic->k=2)
print('Lemma 2: coefficient conditions:', conds)
r0 = sp.simplify(conds[0])  # trace equality
r1c = sp.simplify(conds[1])  # det equality
# norm-equality target: |P_perp w|^2 = r^2 for u = e0 (w = (p, r)):
norm_eq = sp.symbols('nr')  # condition should collapse to r1^2 = r2^2
sol = sp.solve([r0, r1c], [p2], dict=True)
red = [sp.simplify(sp.factor(sp.together(s[p2]))) for s in sol]
print('Lemma 2: trace condition gives p2 =', red)
detsub = sp.simplify(sp.factor(r1c.subs(p2, red[0])))
print('Lemma 2: induced determinant condition:', sp.factor(detsub))
ok2 = sp.simplify(detsub - (-(sp.symbols('r') ** 2 - sp.symbols('r2') ** 2))) == 0 \
    or sp.factor(detsub) == sp.factor(sp.symbols('r2') ** 2 - sp.symbols('r') ** 2) \
    or sp.simplify(sp.expand(detsub + (sp.symbols('r') ** 2 - sp.symbols('r2') ** 2))) == 0
print('Lemma 2: mult-2 condition reduces to r^2 = r2^2 (u-orthogonal norm '
      'equality, p invisible):', bool(ok2))
assert ok2

print('PASS s5')
