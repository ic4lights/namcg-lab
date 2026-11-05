"""050 s7 (r2): the 8 + 2*6 split as a corollary of the block-triangular linear equations. Exact rational arithmetic.

Fields h_b^e (16), w_b^{de} = i wt (24), written on e^{iq.y} as in s3 (written again here, nothing imported from s3).
  E1_b^e = q^a Th_ab^e - Rh_ab^{ae},  E2_b^{de} = q^a Rh_ab^{de},  E3_b = q^a(q_a t_b - q_b t_a), t_a = Th_ac^c.
Checks:
  A  symbolic: E2 has no h; E2 and the h part of E1 are Maxwell operators with extra indices; the wt part of E1 has
     the three-term form of the published linear source, with the published ratios.
  B  at null q: the map S -> q_c S^{c mu} has rank 3, image the orthogonal complement of q, kernel 3; two transverse i
     give rank 6, and 8 + 12 = 20 physical components.
  C  rank of the coupling induced from ker(E2 block) to coker(h block) at null q: 6.
  D  local Smith invariants at q^2 = 0 over Q[[eps]], blocks without coupling, the reduced 20 x 20 system, and the
     full operator with and without E3, on transversal lines and on one line tangent to the cone.
  E  heads of chains are frame-type modulo the rotation gauge directions.
Symbolic output and sampled lines are checks; the argument is in proposal-r2.md."""
from fractions import Fraction as Fr
from collections import Counter
import sympy as sp
from sympy import QQ
from sympy.polys.matrices import DomainMatrix

d = 4
eta = [-1, 1, 1, 1]
pairs = [(c, f) for c in range(d) for f in range(c + 1, d)]
NH, NW = d * d, d * len(pairs)
NV = NH + NW


def unpack(x):
    h = [[x[a * d + c] for c in range(d)] for a in range(d)]
    w = [[[0] * d for _ in range(d)] for _ in range(d)]
    for a in range(d):
        for i, (c, f) in enumerate(pairs):
            v = x[NH + a * len(pairs) + i]
            w[a][c][f] = v
            w[a][f][c] = -v
    return h, w


def operator(q, x, with_E3=True):
    h, wt = unpack(x)
    qu = [eta[a] * q[a] for a in range(d)]
    Th = [[[q[a] * h[b][c] - q[b] * h[a][c] + wt[b][c][a] * eta[a] - wt[a][c][b] * eta[b] for c in range(d)]
           for b in range(d)] for a in range(d)]
    Rh = [[[[q[a] * wt[b][c][f] - q[b] * wt[a][c][f] for f in range(d)] for c in range(d)]
           for b in range(d)] for a in range(d)]
    E1 = [[sum(qu[a] * Th[a][b][e] for a in range(d)) - sum(Rh[a][b][a][e] for a in range(d)) for e in range(d)]
          for b in range(d)]
    E2 = [[sum(qu[a] * Rh[a][b][c][f] for a in range(d)) for (c, f) in pairs] for b in range(d)]
    E3 = []
    if with_E3:
        t = [sum(Th[a][c][c] for c in range(d)) for a in range(d)]
        E3 = [sum(qu[a] * (q[a] * t[b] - q[b] * t[a]) for a in range(d)) for b in range(d)]
    return E1, E2, E3


def matrix(q, with_E3=True):
    cols = []
    for k in range(NV):
        x = [sp.S.Zero] * NV
        x[k] = sp.S.One
        E1, E2, E3 = operator(q, x, with_E3)
        cols.append([v for r in E1 for v in r] + [v for r in E2 for v in r] + list(E3))
    return sp.Matrix(cols).T


print("# A. block-triangular form, symbolic in q, h, wt")
qs = sp.symbols("q0:4")
xs = sp.symbols("x0:%d" % NV)
E1, E2, _ = operator(qs, list(xs), False)
hsyms, wsyms = xs[:NH], xs[NH:]
print("E2 independent of h:", all(sp.expand(v).free_symbols.isdisjoint(hsyms) for r in E2 for v in r))
h, wt = unpack(list(xs))
qu = [eta[a] * qs[a] for a in range(d)]
q2 = sum(qu[a] * qs[a] for a in range(d))
ok = True
for b in range(d):
    for i, (c, f) in enumerate(pairs):
        ok &= sp.expand(E2[b][i] - (q2 * wt[b][c][f] - qs[b] * sum(qu[a] * wt[a][c][f] for a in range(d)))) == 0
print("E2_b^{de} = q^2 wt_b^{de} - q_b q^a wt_a^{de} (Maxwell with extra indices):", ok)
ok_h, ok_w, ok_F = True, True, True
for b in range(d):
    for e in range(d):
        hp = q2 * h[b][e] - qs[b] * sum(qu[a] * h[a][e] for a in range(d))
        low = lambda a, b_, e_: wt[a][e_][b_] * eta[b_]
        s_ab = sum(qu[a] * (-low(a, b, e)) for a in range(d))
        s_ba = sum(qs[a] * wt[b][a][e] for a in range(d))
        s_tr = qs[b] * sum(wt[a][a][e] for a in range(d))
        wp = -2 * s_ba + s_tr + s_ab
        ok_h &= sp.expand(E1[b][e].subs({w: 0 for w in wsyms}) - hp) == 0
        ok_w &= sp.expand(E1[b][e].subs({x: 0 for x in hsyms}) - wp) == 0
        ok_F &= sp.expand(wp - 2 * (sp.Rational(1, 2) * s_ab - s_ba + sp.Rational(1, 2) * s_tr)) == 0
print("h part of E1 = q^2 h_b^e - q_b q^a h_a^e:", ok_h)
print("wt part of E1 = q^a wt_{ab}^e - 2 q^a wt_{ba}^e + q_b wt_a^{ae}:", ok_w)
print("  equals 2 (1/2 q^a S_ab^e - q^a S_ba^e + 1/2 q_b S_a^{ae}), the ratios 1/2 : -1 : 1/2 of the published j:", ok_F)

print("# A2. the same linear source from the published definitions of T and R (d=4, sign and scale)")
S = {}
sv = sp.symbols("s0:%d" % NW)
for a in range(d):
    for i, (c, f) in enumerate(pairs):
        S[(a, c, f)] = sv[a * len(pairs) + i]
        S[(a, f, c)] = -sv[a * len(pairs) + i]
        S[(a, c, c)] = 0
        S[(a, f, f)] = 0
Su = lambda a, c, f: S[(a, c, f)]
Sl = lambda a, b_, e: eta[b_] * Su(a, b_, e)  # S_a b^e
allok, ratio = True, set()
for b in range(d):
    for e in range(d):
        # d^a T_ab^e - R_b^e with T_ab^e = S_ab^e - S_ba^e, R_ab^{cd} = d_a S_b^{cd} - d_b S_a^{cd}, R_b^e = R_ab^{ae}
        val = sum(qu[a] * (Sl(a, b, e) - Sl(b, a, e)) for a in range(d)) - sum(
            qs[a] * Su(b, a, e) - qs[b] * Su(a, a, e) for a in range(d))
        jp = sum(sp.Rational(1, 2) * qu[a] * Sl(a, b, e) - qu[a] * Sl(b, a, e) for a in range(d)) + sp.Rational(1, 2) * qs[b] * sum(Su(a, a, e) for a in range(d))
        allok &= sp.expand(val - 2 * jp) == 0
print("from those definitions the linear term is exactly 2 x the printed -j, with the same three-term ratios:", allok)

print("# B. the map S -> q_c S^{c mu} at null q")
q0 = (sp.S.One, sp.S.One, sp.S.Zero, sp.S.Zero)
q0u = [eta[a] * q0[a] for a in range(d)]
print("q0 =", q0, "q0^2 =", sum(q0u[a] * q0[a] for a in range(d)), "transverse i = 2, 3 have q_i = q^i = 0")
rows = []
for k in range(len(pairs)):
    Sm = [[0] * d for _ in range(d)]
    c, f = pairs[k]
    Sm[c][f] = 1
    Sm[f][c] = -1
    rows.append([sum(q0[c_] * Sm[c_][m] for c_ in range(d)) for m in range(d)])
Mp = sp.Matrix(rows).T
perp = all(sum(q0[m] * Mp[m, k] for m in range(d)) == 0 for k in range(len(pairs)))
print("rank per transverse i:", Mp.rank(), "kernel:", len(pairs) - Mp.rank(), "image orthogonal to q:", perp,
      "; q-perp has dimension", d - 1)
print("two transverse i: rank", 2 * Mp.rank(), "; physical components h_i^mu", 2 * d, ", S_i^{cd}", 2 * len(pairs),
      ", total", 2 * d + 2 * len(pairs), "=", 2 * d - 2 * Mp.rank(), "+", 2 * len(pairs) - 2 * Mp.rank(), "+ 2 *", 2 * Mp.rank())


print("# C. coupling induced from ker(E2 block) to coker(h block) at null q")
M0 = matrix(q0, False)
H0 = M0[:16, :NH]
C0 = M0[:16, NH:]
W0 = M0[16:, NH:]
print("E2 block has zero h column block:", M0[16:, :NH] == sp.zeros(24, NH))
kerW = sp.Matrix.hstack(*W0.nullspace())
print("rank h block", H0.rank(), "rank wt block", W0.rank(), "ker wt block", kerW.shape[1], "coker h block", 16 - H0.rank())
img = sp.Matrix.hstack(H0, C0 * kerW)
print("rank of the induced map ker(wt block) -> coker(h block):", img.rank() - H0.rank())


def valuation(p):
    for i, c in enumerate(p):
        if c != 0:
            return i
    return None


def smith_local(M, eps, K=14):
    """Smith invariants over Q[[eps]] by elimination with series truncated at order K. Returns a Counter of valuations;
    entries that vanish to order K are counted as 'trunc'."""
    nr, nc = M.shape
    A = [[None] * nc for _ in range(nr)]
    for i in range(nr):
        for j in range(nc):
            v = sp.Poly(M[i, j], eps)
            c = [Fr(0)] * K
            for (m,), co in v.terms():
                if m < K:
                    c[m] = Fr(int(sp.Rational(co).p), int(sp.Rational(co).q))
            A[i][j] = c

    def mul(a, b):
        out = [Fr(0)] * K
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if i + j >= K:
                        break
                    if y:
                        out[i + j] += x * y
        return out

    def inv_unit(a):
        out = [Fr(0)] * K
        out[0] = 1 / a[0]
        for n in range(1, K):
            out[n] = -sum(a[k] * out[n - k] for k in range(1, n + 1)) / a[0]
        return out

    res = Counter()
    rows = list(range(nr))
    cols = list(range(nc))
    while rows and cols:
        best, bi, bj = None, None, None
        for i in rows:
            for j in cols:
                v = valuation(A[i][j])
                if v is not None and (best is None or v < best):
                    best, bi, bj = v, i, j
                    if v == 0:
                        break
            if best == 0:
                break
        if best is None:
            res["trunc"] += min(len(rows), len(cols))
            break
        res[best] += 1
        piv = A[bi][bj]
        unit = piv[best:] + [Fr(0)] * best
        iu = inv_unit(unit)
        for i in rows:
            if i != bi and valuation(A[i][bj]) is not None:
                f = A[i][bj][best:] + [Fr(0)] * best
                f = mul(f, iu)
                for j in cols:
                    if j != bj and any(A[bi][j]):
                        p = mul(f, A[bi][j])
                        A[i][j] = [x - y for x, y in zip(A[i][j], p)]
                A[i][bj] = [Fr(0)] * K
        rows.remove(bi)
        cols.remove(bj)
    return res


eps = sp.Symbol("eps")


def fmt(c):
    return ", ".join(f"{'unit' if k == 0 else 'eps^%s' % k if k != 'trunc' else 'zero to O(eps^14)'}: {c[k]}" for k in sorted(c, key=lambda z: (z == 'trunc', z)))


print("# D. local Smith invariants at q^2 = 0")
lines = [
    ("(1+e, 1, 0, 0)", (1 + eps, sp.S.One, sp.S.Zero, sp.S.Zero)),
    ("(1+e, 1, e, 0)", (1 + eps, sp.S.One, eps, sp.S.Zero)),
    ("(1+2e, 1-e, e, 3e)", (1 + 2 * eps, 1 - eps, eps, 3 * eps)),
    ("(1, 1+e, -2e, e)", (sp.S.One, 1 + eps, -2 * eps, eps)),
]
for name, q in lines:
    q2v = sp.expand(sum(eta[a] * q[a] ** 2 for a in range(d)))
    Ms = matrix(q, False).applyfunc(sp.expand)
    Ms3 = matrix(q, True).applyfunc(sp.expand)
    Hb, Wb = Ms[:16, :NH], Ms[16:, NH:]
    print(f"line {name}: q^2 = {q2v}")
    print("   h block alone:", fmt(smith_local(Hb, eps)))
    print("   wt block alone:", fmt(smith_local(Wb, eps)))
    print("   full, no E3:", fmt(smith_local(Ms, eps)))
    print("   full, with E3:", fmt(smith_local(Ms3, eps)))
    generic = Ms3.subs(eps, sp.Rational(3, 7))
    print("   rank at eps = 3/7:", DomainMatrix.from_Matrix(generic).convert_to(QQ).rank(), "of", NV)

print("# D2. the reduced 20 x 20 system on h_i^mu, S_i^{cd}, i = 2, 3, on the line (1+e, 1, 0, 0)")
q = lines[0][1]
q2v = sp.expand(sum(eta[a] * q[a] ** 2 for a in range(d)))
Red = sp.zeros(20, 20)
for n in range(20):
    x = [sp.S.Zero] * NV
    i_slot = (n if n < 8 else n - 8) // (4 if n < 8 else 6)
    i = 2 + i_slot
    if n < 8:
        x[i * d + n % 4] = sp.S.One
    else:
        x[NH + i * len(pairs) + (n - 8) % 6] = sp.S.One
    E1v, E2v, _ = operator(q, x, False)
    col = [E1v[2][e] for e in range(d)] + [E1v[3][e] for e in range(d)] + [E2v[2][k] for k in range(6)] + [E2v[3][k] for k in range(6)]
    for r in range(20):
        Red[r, n] = sp.expand(col[r])
print("off-diagonal rank at eps = 0:", Red[:8, 8:].subs(eps, 0).rank(), "; lower-left block zero:", Red[8:, :8] == sp.zeros(12, 8))
print("diagonal blocks are q^2 times the identity:", sp.expand(Red[:8, :8] - q2v * sp.eye(8)) == sp.zeros(8, 8),
      sp.expand(Red[8:, 8:] - q2v * sp.eye(12)) == sp.zeros(12, 12))
c = smith_local(Red, eps)
print("Smith invariants:", fmt(c))
print("zeros with multiplicity: simple", c[1], "+ 2 * double", c[2], "=", c[1] + 2 * c[2])

print("# D3. a line tangent to the cone: invariants become powers of q^2")
q = (sp.S.One, sp.S.One, eps, sp.S.Zero)
print("line (1, 1, e, 0): q^2 =", sp.expand(sum(eta[a] * q[a] ** 2 for a in range(d))))
print("   full, with E3:", fmt(smith_local(matrix(q, True).applyfunc(sp.expand), eps)))

print("# E. heads of chains: x0 in ker M0 with M1 x0 in im M0, on the line (1+e, 1, 0, 0)")
Ms = matrix(lines[0][1], True).applyfunc(sp.expand)
M0f = Ms.subs(eps, 0)
M1f = Ms.diff(eps).subs(eps, 0)
Kf = sp.Matrix.hstack(*M0f.nullspace())
A = sp.Matrix.hstack(M1f * Kf, M0f)
ns = DomainMatrix.from_Matrix(A).convert_to(QQ).nullspace().to_Matrix().T
heads = Kf * ns[:Kf.shape[1], :]
hb = sp.Matrix.hstack(*heads.columnspace())
print("null kernel", Kf.shape[1], "; heads including gauge, rank", hb.shape[1])
print("rank of the heads projected on wt:", hb[NH:, :].rank(), "(the six rotation gauge directions q_a lam^{cd})")
print("heads with wt = 0:", hb.shape[1] - hb[NH:, :].rank(), "(four diffeomorphism gauge directions + six frame-type tails)")
qL = lines[0][1]
q00 = [qL[a].subs(eps, 0) for a in range(d)]
Grot = sp.zeros(NW, len(pairs))
for k in range(len(pairs)):
    for a in range(d):
        Grot[a * len(pairs) + k, k] = q00[a]
print("wt projection of the heads equals the span of q_a lam^{cd}:", sp.Matrix.hstack(hb[NH:, :], Grot).rank() == 6 == Grot.rank())
