"""023 script 7: compact (Euclidean, so(6), delta) four-matrix analogue X^a = M^{a5}, a=1..4, on the N-th symmetric power of the 4 of su(4).
(1) Gauge-fixed vector operator H_gf = H + G^dag G (G a = sum_a [X^a, a^a]) versus the group-theory formula (positive Casimir convention)
        lambda = c5(a,b) - c4(c',d') + 3 + m^2 ,  m^2 = -3,
    over  L^2(CP^3_N) = sum_{k<=N} (so(6) irrep (k,k,0)) = sum_{(a,b): a<=N, 0<=b<=a} (so(5) irrep (a,b)) (each once; a = k fixes C_6 = 2a^2+6a),
    (c,d) in (a,b)|so(4) (a>=c>=b>=|d|),  (c',d') in (c,d) x (1,0).
(2) exact lowest eigenvalue as a function of the C_6 window and the number of negative modes."""
import numpy as np, itertools, sys
from quantum_compact_hessian import sym_power_ops, Sig, comm
from math import comb

def c5(a, b): return a * (a + 3) + b * (b + 1)
def c4(c, d): return c * (c + 2) + d * d
def dim5(a, b): return (2 * a + 3) * (2 * b + 1) * (a - b + 1) * (a + b + 2) // 6
def dim4(c, d): return (c + d + 1) * (c - d + 1)
def so4_children(a, b):
    out = []
    for c in range(b, a + 1):
        for d in range(-b, b + 1):
            out.append((c, d))
    return out
def vec_prod(c, d):
    """(c,d) x vector = (1/2,1/2) x (jL,jR); jL=(c+d)/2, jR=(c-d)/2"""
    jL, jR = (c + d) / 2, (c - d) / 2
    res = []
    for dl in (-0.5, 0.5):
        for dr in (-0.5, 0.5):
            l2, r2 = jL + dl, jR + dr
            if l2 >= 0 and r2 >= 0: res.append((int(round(l2 + r2)), int(round(l2 - r2))))
    return res
def formula_spectrum(Amax, m2=-3):
    ev = []
    for a in range(Amax + 1):
        for b in range(a + 1):
            for (c, d) in so4_children(a, b):
                for (cp, dp) in vec_prod(c, d):
                    lam = c5(a, b) - c4(cp, dp) + 3 + m2
                    ev.append((lam, dim4(cp, dp), a, b))     # each (c,d) occurs once in (a,b)|so4; dim4(c',d') states
    return ev
def check_dims(N):
    tot = sum(dim5(a, b) * 4 for a in range(N + 1) for b in range(a + 1))
    tot2 = sum(w for (_, w, _, _) in formula_spectrum(N))
    d = comb(N + 3, 3)
    return tot, tot2, 4 * d * d
if __name__ == "__main__":
    Ns = [1, 2, 3]
    for N in Ns:
        mats = [Sig[a, 4] for a in range(4)]
        X, dd = sym_power_ops(mats, N)
        nA = 4; n2 = dd * dd; I = np.eye(dd)
        ad = [np.kron(x, I) - np.kron(I, x.T) for x in X]
        m2 = -3.0
        F = [[X[A] @ X[B] - X[B] @ X[A] for B in range(nA)] for A in range(nA)]
        Hm = np.zeros((nA * n2, nA * n2), complex)
        for B in range(nA):
            Hm[B*n2:(B+1)*n2, B*n2:(B+1)*n2] += sum(a_ @ a_ for a_ in ad) + m2 * np.eye(n2)
            for A in range(nA):
                adF = np.kron(F[A][B], I) - np.kron(I, F[A][B].T)
                Hm[B*n2:(B+1)*n2, A*n2:(A+1)*n2] += -adF - ad[A] @ ad[B]
        Gm = np.hstack(ad)                                      # (n2, nA n2): a -> sum_A [X^A, a^A]
        Hgf = Hm + Gm.conj().T @ Gm
        ev = np.sort(np.linalg.eigvalsh((Hgf + Hgf.conj().T) / 2))
        fs = formula_spectrum(N)
        fev = np.sort(np.concatenate([[lam] * w for (lam, w, _, _) in fs]))
        print("N=%d: dim check (sum 4*dim5, sum formula multiplicities, 4 d^2) = %s ; numerical lowest = %.6f ; formula lowest = %.6f ; max |sorted difference| = %.2e" % (
            N, check_dims(N), ev[0], fev[0], np.max(np.abs(ev - fev)) if len(ev) == len(fev) else float('nan')))
    print()
    print("exact counts from the formula (compact Euclidean analogue). a = so(6) label (C_6 = 2a^2+6a), window a<=A:")
    print("  A  total_modes  negative  zero  min_eigenvalue  frac_negative")
    for A in [1, 2, 3, 4, 6, 8, 12, 16, 24, 32]:
        fs = formula_spectrum(A)
        tot = sum(w for (_, w, _, _) in fs); neg = sum(w for (l, w, _, _) in fs if l < -1e-9); zer = sum(w for (l, w, _, _) in fs if abs(l) <= 1e-9)
        mn = min(l for (l, _, _, _) in fs)
        print("  %2d %11d %9d %5d %14.1f  %.5f" % (A, tot, neg, zer, mn, neg / tot))
