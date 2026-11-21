"""081-088 r3, v3 (replaces v3_row_length_profile.py, whose repeated-commutator tensors lose
orthogonality at N=400): slot profile of the Gaussian state of the Row length paragraph.

Construction (stable). Basis |k), k=0..N-1, J^3 eigenvalue j-k, j=(N-1)/2, (J+)_{k-1,k}=c_k,
c_k = sqrt(j(j+1)-(j-k)(j-k+1)). The Casimir superoperator C(X)=sum_a [J_a,[J_a,X]] preserves each
fixed-offset subspace {X : X_{a,a+m} only}, and on it is the symmetric tridiagonal matrix
   diag_a = (c_a^2 + c_{a+1}^2 + c_b^2 + c_{b+1}^2)/2 + m^2,  offdiag_{a,a+1} = -c_{a+1} c_{b+1},  b=a+m,
with simple eigenvalues l(l+1), l=m..N-1. Its Frobenius-orthonormal eigenvectors are the trace-normalised
T_{l,m} up to a phase (phases do not enter the variances). scipy eigh_tridiagonal is used.
Variances: E|Pi_{vj}|^2 = sum_l f(l) |T_{l,m}(v,j)|^2, m the offset of (v,j) (each entry gets one m).
Block = k<M, v=|M), u=|M-1) (distance 1 from v); slots of r are j<M-1.

Checks:
 A  eigenvalues equal l(l+1) (max rel dev), eigenvectors orthonormal, at N=400;
 B  exact Clebsch-Gordan cross-check at N=12: |T_{lm}(m1,m2)|^2 = (2l+1)/N |<j m2; l m | j m1>|^2 (sympy, exact),
    and dense diagonalisation of the full superoperator at N=12 (degenerate-free per offset);
 C  full-row sum N^-1 sum_l (2l+1) f(l) at the N actually used (row v, all j), asserted;
 D  slots: g_j = 0 for distance > l_c, at most l_c-1 slots of r, D_eff <= l_c-1;
 E  table at N=400, M=200: W_block (full block-row sum incl. u), g_u/W_block, D_eff(r), 6N(W-g_u)/l_c^3
    (f=l/2), 16N(W-g_u)/l_c^4 and 16N W/l_c^4 (f=l(l+1)/4), local exponents of W-g_u and W in l_c;
 F  diagnosis of the old construction: overlap <T_{40,3},T_{38,3}> from repeated commutators.
Run: python -I proposals/local-gpu/081-088-r2/v3_row_length_profile_r3.py     Last line: PASS v3-r3
"""
import numpy as np
from scipy.linalg import eigh_tridiagonal

ok = True


def cvec(N):
    j = (N - 1) / 2
    k = np.arange(N + 1, dtype=float)
    c = np.zeros(N + 1)
    kk = np.arange(1, N)
    c[1:N] = np.sqrt(j*(j + 1) - (j - kk)*(j - kk + 1))   # c_0 = c_N = 0
    return c


def offset_tensors(N, m, lmax):
    """Rows: index a of X_{a,a+m}, a=0..N-1-m; columns: l=m..min(lmax,N-1). Returns (ls, evals, V)."""
    c = cvec(N)
    n = N - m
    a = np.arange(n)
    b = a + m
    d = 0.5*(c[a]**2 + c[a + 1]**2 + c[b]**2 + c[b + 1]**2) + m*m
    e = -c[a[:-1] + 1]*c[b[:-1] + 1]
    hi = min(lmax, N - 1) - m
    if n == 1:
        return np.array([m]), d.copy(), np.ones((1, 1))
    w, V = eigh_tridiagonal(d, e, select='i', select_range=(0, hi))
    return np.arange(m, m + hi + 1), w, V


def profile(N, M, lc, f):
    """g[j] = E|Pi_{vj}|^2 for all j=0..N-1 (v=M)."""
    v = M
    g = np.zeros(N)
    for m in range(0, lc + 1):
        ls, w, V = offset_tensors(N, m, lc)
        fl = np.array([f(l) for l in ls])
        # entry (v, v+m): index a=v (if v+m<N); entry (v, v-m) is the transpose entry (v-m, v): index a=v-m
        if v + m < N:
            g[v + m] += np.sum(fl*V[v, :]**2) if m > 0 else np.sum(fl*V[v, :]**2)
        if m > 0 and v - m >= 0:
            g[v - m] += np.sum(fl*V[v - m, :]**2)
    return g


# A: spectrum and orthonormality at N=400
N = 400
devA, ortA = 0.0, 0.0
for m in (0, 1, 3, 17, 40):
    ls, w, V = offset_tensors(N, m, N - 1)
    devA = max(devA, np.max(np.abs(w - ls*(ls + 1))/(ls*(ls + 1) + 1)))
    ortA = max(ortA, np.max(np.abs(V.T @ V - np.eye(V.shape[1]))))
print('A N=400: max rel dev of eigenvalues from l(l+1) %.1e | orthonormality dev %.1e' % (devA, ortA))
ok &= devA < 1e-10 and ortA < 1e-10

# B: exact CG at N=12, and dense superoperator
from sympy import Rational, S
from sympy.physics.quantum.cg import CG
N0 = 12
j0 = Rational(N0 - 1, 2)
devB = 0.0
for m in range(0, N0):
    ls, w, V = offset_tensors(N0, m, N0 - 1)
    for col, l in enumerate(ls):
        for a in range(N0 - m):
            b = a + m
            m1, m2 = j0 - a, j0 - b          # X_{a,b}: <m1| T |m2>, m1 - m2 = m
            cg = CG(j0, m2, S(l), S(m), j0, m1).doit()
            exact = float(Rational(2*l + 1, N0)*cg**2)
            devB = max(devB, abs(V[a, col]**2 - exact))
print('B N=12: max |T|^2 deviation from exact Clebsch-Gordan %.1e' % devB)
ok &= devB < 1e-12
# dense superoperator at N=12: eigenvalues l(l+1) with multiplicity 2l+1
c = cvec(N0)
Jp = np.diag(c[1:N0], 1)
Jm = Jp.T
J3 = np.diag(j0.__float__() - np.arange(N0))
Jx, Jy = (Jp + Jm)/2, (Jp - Jm)/(2j)
I = np.eye(N0)
sup = sum(np.kron(Ja @ Ja, I) + np.kron(I, (Ja @ Ja).T) - 2*np.kron(Ja, Ja.T) for Ja in (Jx, Jy, J3))
ev = np.sort(np.linalg.eigvalsh(sup))
exp_ev = np.sort(np.concatenate([[l*(l + 1)]*(2*l + 1) for l in range(N0)]))
devD = np.max(np.abs(ev - exp_ev))
print('B N=12: dense Casimir superoperator spectrum dev %.1e' % devD)
ok &= devD < 1e-9

# C-E
fl2 = lambda l: l/2
fq = lambda l: l*(l + 1)/4
M = 200


def stats(N, M, lc, f):
    g = profile(N, M, lc, f)
    full = g.sum()
    target = sum((2*l + 1)*f(l) for l in range(1, lc + 1))/N
    blk = g[:M]
    gu = g[M - 1]
    gr = g[:M - 1]
    nz = int(np.sum(gr > 1e-12*gr.max()))
    far = np.max(np.abs(g[:M - lc])) if M - lc > 0 else 0.0
    Deff = gr.sum()**2/np.sum(gr**2)
    return dict(full=full, target=target, W=blk.sum(), gu=gu, Wr=gr.sum(), nz=nz, far=far, Deff=Deff)


print('C/D/E N=400 M=200:')
res = {}
for lc, name, f in [(20, 'l/2', fl2), (40, 'l/2', fl2), (20, 'l(l+1)/4', fq), (40, 'l(l+1)/4', fq)]:
    s = stats(N, M, lc, f)
    res[(lc, name)] = s
    rowdev = abs(s['full'] - s['target'])/s['target']
    print('  lc=%d f=%s: full-row sum %.6f vs N^-1 sum(2l+1)f %.6f (rel %.1e) | slots of r %d (<= %d) | '
          'max g at distance > lc %.1e | W_block %.4f | g_u %.4f | g_u/W %.4f | W-g_u %.4f | D_eff(r) %.2f'
          % (lc, name, s['full'], s['target'], rowdev, s['nz'], lc - 1, s['far'], s['W'], s['gu'],
             s['gu']/s['W'], s['Wr'], s['Deff']))
    ok &= rowdev < 1e-10 and s['nz'] <= lc - 1 and s['far'] < 1e-14 and s['Deff'] <= lc - 1
    ok &= s['W'] <= s['full'] + 1e-9

for lc in (20, 40):
    s = res[(lc, 'l/2')]
    print('  f=l/2 lc=%d: 6N(W-g_u)/lc^3 = %.4f | 6N W/lc^3 = %.4f' % (lc, 6*N*s['Wr']/lc**3, 6*N*s['W']/lc**3))
s = res[(40, 'l(l+1)/4')]
print('  f=l(l+1)/4 lc=40: 16N(W-g_u)/lc^4 = %.4f | 16N W/lc^4 = %.4f' % (16*N*s['Wr']/40**4,
                                                                         16*N*s['W']/40**4))


def local_exp(f, lc, key):
    a, b = stats(N, M, lc - 1, f), stats(N, M, lc + 1, f)
    return np.log(b[key]/a[key])/np.log((lc + 1)/(lc - 1))


for name, f in (('l/2', fl2), ('l(l+1)/4', fq)):
    print('  local exponent at lc=40 (central difference 39,41), f=%s: of W-g_u %.3f, of W %.3f'
          % (name, local_exp(f, 40, 'Wr'), local_exp(f, 40, 'W')))

# gatekeeper table
t = res[(40, 'l/2')]
chk = [round(t['W'], 3) == 27.856, round(t['gu']/t['W'], 4) == 0.0230, round(t['Deff'], 2) == 37.96,
       round(6*N*t['Wr']/40**3, 4) == 1.0206]
t20 = res[(20, 'l/2')]
chk += [round(t20['gu']/t20['W'], 4) == 0.0441, round(t20['Deff'], 2) == 18.68, round(6*N*t20['Wr']/20**3, 4) == 1.0414]
tq = res[(40, 'l(l+1)/4')]
chk += [round(tq['Deff'], 2) == 38.07, round(16*N*tq['Wr']/40**4, 3) == 1.069]
print('E gatekeeper table reproduced:', chk)
ok &= all(chk)

# F: old construction diagnosis
def old_tensors(N, lc, want):
    c = cvec(N)
    Jp = np.diag(c[1:N], 1); Jm = Jp.T.copy()
    P = np.eye(N); out = {}
    for l in range(1, lc + 1):
        P = Jp @ P; P /= np.linalg.norm(P); T = P.copy(); out[(l, l)] = T
        for mm in range(l, -l, -1):
            T = Jm @ T - T @ Jm; T /= np.linalg.norm(T); out[(l, mm - 1)] = T
    return {k: out[k] for k in want}


old = old_tensors(400, 40, [(40, 3), (38, 3)])
ov = abs(np.sum(old[(40, 3)]*old[(38, 3)]))
print('F old repeated-commutator construction at N=400: |<T_{40,3},T_{38,3}>| = %.3f (should be 0)' % ov)
ok &= ov > 0.5
print('PASS v3-r3' if ok else 'FAIL v3-r3')
