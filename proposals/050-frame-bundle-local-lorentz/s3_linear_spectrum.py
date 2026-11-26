"""
s3: linearised matrix equation of the first-order equivariant class about the flat background, d = 4, exact.

Fields (section values, equivariant): h_a^c (16), w_a^{cd} (24).  D_a -> D_a - h_a^c D_c + (1/2) w_a^{cd} S_cd, plus tau_a = (1/2) T_ac^c
from Hermiticity (the independent real order-zero field A_a decouples at this order and is treated separately).

    T_ab^c   = d_a h_b^c - d_b h_a^c + w_b^c_a - w_a^c_b
    R_ab^{cd}= d_a w_b^{cd} - d_b w_a^{cd}
    E1_b^e   = - d^a T_ab^e + R_ab^{ae}
    E2_b^{de}=   d^a R_ab^{de}
    E3_b     =   d^a (d_a tau_b - d_b tau_a)

On e^{iq.y} write w = i wt so that the matrix is rational in q.  Reports: gauge kernel, rank at non-null q, kernel at null q,
the Jordan structure at q^2 = 0 along q = (s,1,0,0), s -> 1, and the content of the modes.
"""
import itertools, sys
import sympy as sp

d = 4
eta = [-1, 1, 1, 1]
pairs = [(c, f) for c in range(d) for f in range(c+1, d)]
nh, nw = d*d, d*len(pairs)
NV = nh+nw


def unpack(x):
    h = [[x[a*d+c] for c in range(d)] for a in range(d)]      # h_a^c
    w = [[[0]*d for _ in range(d)] for _ in range(d)]         # w_a^{cf}, both upper
    for a in range(d):
        for i, (c, f) in enumerate(pairs):
            v = x[nh+a*len(pairs)+i]
            w[a][c][f] = v
            w[a][f][c] = -v
    return h, w


def operator(q, x, with_E3=True):
    """returns E1, E2, E3 with an overall factor conventions: d -> i q, w = i wt."""
    h, wt = unpack(x)
    qup = [eta[a]*q[a] for a in range(d)]
    # T = i Th, with Th_ab^c = q_a h_b^c - q_b h_a^c + wt_b^c_a - wt_a^c_b;  wt_b^c_a = wt_b^{c f} eta_{f a}
    Th = [[[q[a]*h[b][c] - q[b]*h[a][c] + wt[b][c][a]*eta[a] - wt[a][c][b]*eta[b] for c in range(d)] for b in range(d)] for a in range(d)]
    # R = (i q)(i wt) = - Rh, with Rh_ab^{cf} = q_a wt_b^{cf} - q_b wt_a^{cf}
    Rh = [[[[q[a]*wt[b][c][f] - q[b]*wt[a][c][f] for f in range(d)] for c in range(d)] for b in range(d)] for a in range(d)]
    # E1 = - (i q^a)(i Th) + (-Rh_ab^{a e}) = q^a Th_ab^e - Rh_ab^{ae}
    E1 = [[sum(qup[a]*Th[a][b][e] for a in range(d)) - sum(Rh[a][b][a][e] for a in range(d)) for e in range(d)] for b in range(d)]
    # E2 = (i q^a)(-Rh) -> proportional to q^a Rh_ab^{de}
    E2 = [[sum(qup[a]*Rh[a][b][c][f] for a in range(d)) for (c, f) in pairs] for b in range(d)]
    out = [v for row in E1 for v in row] + [v for row in E2 for v in row]
    if with_E3:
        # tau = (1/2) i Th_ac^c ; E3 proportional to q^a (q_a t_b - q_b t_a), t_a = Th_ac^c
        t = [sum(Th[a][c][c] for c in range(d)) for a in range(d)]
        E3 = [sum(qup[a]*(q[a]*t[b]-q[b]*t[a]) for a in range(d)) for b in range(d)]
        out += E3
    return out


def matrix(q, with_E3=True):
    cols = []
    for k in range(NV):
        x = [sp.S.Zero]*NV
        x[k] = sp.S.One
        cols.append(operator(q, x, with_E3))
    return sp.Matrix(cols).T


def gauge_vectors(q):
    """diffeo xi^c: delta h_a^c ~ q_a xi^c (in the rescaled convention), and local rotation lam^{cf}: delta h_a^c = lam-term, delta wt ~ q lam."""
    vs = []
    for c in range(d):
        x = [sp.S.Zero]*NV
        for a in range(d):
            x[a*d+c] = q[a]
        vs.append(x)
    for i, (c, f) in enumerate(pairs):
        x = [sp.S.Zero]*NV
        # delta wt_a^{cf} = q_a, delta h_a^g = sigma ( delta_a... ) with sigma fixed by Th = 0 below
        for a in range(d):
            x[nh+a*len(pairs)+i] = q[a]
        # Th must vanish: q_a dh_b^g - q_b dh_a^g + dwt_b^g_a - dwt_a^g_b = 0 with dwt_b^{cf} = q_b (e_c^g e_f^k - e_f^g e_c^k)
        # solved by dh_b^g = lam^g_b, lam^{cf} = unit bivector
        for b in range(d):
            for g in range(d):
                lam = (1 if (g, b) == (c, f) else 0)*eta[b] - (1 if (g, b) == (f, c) else 0)*eta[b]
                x[b*d+g] += lam
        vs.append(x)
    return vs


print('# s3: linear spectrum about flat. Exact rational arithmetic.')
# non-null q
for q in [(sp.Rational(3), sp.Rational(1), sp.Rational(2), sp.Rational(5)), (sp.Rational(1), sp.Rational(2), sp.Rational(-1), sp.Rational(1, 2)), (sp.Rational(2), sp.Rational(1), 0, 0)]:
    q2 = sum(eta[a]*q[a]**2 for a in range(d))
    M = matrix(q)
    G = sp.Matrix(gauge_vectors(q)).T
    res = M*G
    print(f'q={q} q^2={q2}: rank M={M.rank()} of {NV}, kernel dim {NV-M.rank()}, gauge vectors independent rank {G.rank()}, M*gauge=0: {res==sp.zeros(*res.shape)}; rank without E3={matrix(q,False).rank()}')

# null q
q0 = (sp.S.One, sp.S.One, sp.S.Zero, sp.S.Zero)
M0 = matrix(q0)
G0 = sp.Matrix(gauge_vectors(q0)).T
ker = M0.nullspace()
print(f'null q={q0}: rank={M0.rank()}, kernel dim {len(ker)}, gauge rank {G0.rank()}, M*gauge=0: {(M0*G0)==sp.zeros(*(M0*G0).shape)}, physical kernel dim (kernel minus gauge) {len(ker)-G0.rank()}')

# content on the kernel at null q
Kmat = sp.Matrix.hstack(*ker)
def Th_vec(q, x):
    h, wt = unpack(list(x))
    return [q[a]*h[b][c] - q[b]*h[a][c] + wt[b][c][a]*eta[a] - wt[a][c][b]*eta[b] for a in range(d) for b in range(a+1, d) for c in range(d)]
def Rh_vec(q, x):
    h, wt = unpack(list(x))
    return [q[a]*wt[b][c][f] - q[b]*wt[a][c][f] for a in range(d) for b in range(a+1, d) for (c, f) in pairs]
def lin_map(fn, q, K):
    cols = []
    for j in range(K.shape[1]):
        cols.append(fn(q, K[:, j]))
    return sp.Matrix(cols).T
TK = lin_map(Th_vec, q0, Kmat)
RK = lin_map(Rh_vec, q0, Kmat)
print(f'on the null kernel: rank of the map to torsion = {TK.rank()}; to curvature = {RK.rank()}; joint rank (T,R) = {sp.Matrix.vstack(TK,RK).rank()}')
zeroT = TK.nullspace()
print(f'  subspace with T = 0: dim {len(zeroT)} (gauge {G0.rank()} + {len(zeroT)-G0.rank()} torsion-free modes)')
if zeroT:
    Z = Kmat*sp.Matrix.hstack(*zeroT)
    print(f'  curvature rank on T = 0 subspace: {lin_map(Rh_vec, q0, Z).rank()}')
zeroR = RK.nullspace()
print(f'  subspace with R = 0: dim {len(zeroR)}')

# Jordan structure along q = (s,1,0,0), s = 1 + eps
eps = sp.Symbol('eps')
qs = (1+eps, sp.S.One, sp.S.Zero, sp.S.Zero)
Ms = matrix(qs)
Ms = Ms.applyfunc(sp.expand)
deg = max(sp.Poly(v, eps).degree() if v != 0 else 0 for v in Ms)
coefs = [Ms.applyfunc(lambda v: sp.Poly(v, eps).coeff_monomial(eps**j) if v != 0 else 0) for j in range(deg+1)]
print(f'M(eps) has degree {deg} in eps; q^2 = -(1+eps)^2 + 1 = -2 eps - eps^2')
prev = 0
Nk = []
for k in range(1, 7):
    rows = []
    for i in range(k):
        row = []
        for j in range(k):
            row.append(coefs[i-j] if 0 <= i-j <= deg else sp.zeros(*Ms.shape))
        rows.append(sp.Matrix.hstack(*row))
    block = sp.Matrix.vstack(*rows)
    # rank over Q via rational elimination with a fast routine
    from sympy.polys.matrices import DomainMatrix
    from sympy import QQ
    dm = DomainMatrix.from_Matrix(block).convert_to(QQ)
    r = dm.rank()
    N = block.shape[1]-r
    Nk.append(N)
    print(f'k={k}: dim of truncated kernel N_k = {N}, chains of length >= k: {N-prev}', flush=True)
    prev = N
print('chains of length >= k minus the 10 gauge families:', [Nk[0]-10]+[Nk[i]-Nk[i-1]-10 for i in range(1, len(Nk))])

# which null-kernel vectors head a chain of length 2?
M1 = coefs[1]
from sympy.polys.matrices import DomainMatrix
from sympy import QQ
# x0 in ker M0 with M1 x0 in im M0
K = Kmat
A = sp.Matrix.hstack(M1*K, M0)
nsp = DomainMatrix.from_Matrix(A).convert_to(QQ).nullspace().to_Matrix().T if True else None
heads = K*nsp[:K.shape[1], :]
hr = heads.rank()
print(f'heads of chains of length >= 2 (including the gauge directions): rank {hr}')
hbasis = sp.Matrix.hstack(*heads.columnspace())
TH = lin_map(Th_vec, q0, hbasis); RH = lin_map(Rh_vec, q0, hbasis)
print(f'  on the heads: rank to torsion {TH.rank()}, to curvature {RH.rank()}, joint {sp.Matrix.vstack(TH,RH).rank()}')
Zspace = Kmat*sp.Matrix.hstack(*zeroT)
print(f'  torsion-free null modes that head a length-2 chain, modulo gauge: {sp.Matrix.hstack(hbasis,Zspace).rank()*-1 + hbasis.rank()+Zspace.rank() - G0.rank()}')
print('  (intersection dimension of the heads with the T = 0 subspace, minus 10 gauge)')

def Tfull(q, x):
    h, wt = unpack(list(x))
    return [[[q[a]*h[b][c] - q[b]*h[a][c] + wt[b][c][a]*eta[a] - wt[a][c][b]*eta[b] for c in range(d)] for b in range(d)] for a in range(d)]
def Tlow(q, x):
    Th = Tfull(q, x)
    return [[[Th[a][b][c]*eta[c] for c in range(d)] for b in range(d)] for a in range(d)]
# irreducible parts: trace vector, axial, tensor
def Tvec(q, x):
    Th = Tfull(q, x)
    return [sum(Th[a][c][c] for c in range(d)) for a in range(d)]
def Taxial(q, x):
    L = Tlow(q, x)
    out = []
    for a, b, c in itertools.combinations(range(d), 3):
        out.append(L[a][b][c]+L[b][c][a]+L[c][a][b])
    return out
def Tnonaxial(q, x):
    L = Tlow(q, x)
    A = {}
    out = []
    for a in range(d):
        for b in range(a+1, d):
            for c in range(d):
                ax = (L[a][b][c]+L[b][c][a]+L[c][a][b])/3
                out.append(L[a][b][c]-ax)
    return out
print(f'on the null kernel: rank of trace vector {lin_map(Tvec,q0,Kmat).rank()}, axial {lin_map(Taxial,q0,Kmat).rank()}, non-axial {lin_map(Tnonaxial,q0,Kmat).rank()}')
print(f'on the heads: rank of trace vector {lin_map(Tvec,q0,hbasis).rank()}, axial {lin_map(Taxial,q0,hbasis).rank()}, non-axial {lin_map(Tnonaxial,q0,hbasis).rank()}')
# sectors: subspace of the null kernel with T purely axial, purely vector
NA = lin_map(Tnonaxial,q0,Kmat).nullspace()
print(f'subspace of null kernel with T totally antisymmetric: dim {len(NA)}, minus gauge and the two torsion-free modes: {len(NA)-12}')
if NA:
    NAsp = Kmat*sp.Matrix.hstack(*NA)
    print(f'  curvature rank there {lin_map(Rh_vec,q0,NAsp).rank()}; intersection with heads modulo gauge {hbasis.rank()+NAsp.rank()-sp.Matrix.hstack(hbasis,NAsp).rank()-10}')

# torsion-free sector off shell: the map h -> Ricci, order two, second order only: T = 0 solved for w
print('torsion-free sector: T = 0 forces w = w(h) and E1 becomes the linearised Ricci operator of the symmetric part of h (see the proposal).')

# a second transversal line through the same null q, to test that the chain counts do not depend on the line
qs2 = (1+eps, sp.S.One, eps, sp.S.Zero)
Ms2 = matrix(qs2).applyfunc(sp.expand)
deg2 = max(sp.Poly(v, eps).degree() if v != 0 else 0 for v in Ms2)
cf2 = [Ms2.applyfunc(lambda v: sp.Poly(v, eps).coeff_monomial(eps**j) if v != 0 else 0) for j in range(deg2+1)]
prev = 0; Nk2 = []
for k in range(1, 5):
    rows = []
    for i in range(k):
        row = []
        for j in range(k):
            row.append(cf2[i-j] if 0 <= i-j <= deg2 else sp.zeros(*Ms2.shape))
        rows.append(sp.Matrix.hstack(*row))
    block = sp.Matrix.vstack(*rows)
    r = DomainMatrix.from_Matrix(block).convert_to(QQ).rank()
    Nk2.append(block.shape[1]-r)
print('second line q=(1+eps,1,eps,0), q^2 = -2 eps: chains of length >= k minus 10:', [Nk2[0]-10]+[Nk2[i]-Nk2[i-1]-10 for i in range(1, len(Nk2))])
