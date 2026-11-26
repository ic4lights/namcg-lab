"""022 script 9: exact quantum (compact, finite N) check of the Casimir completion of the gauge-fixed vector operator in the 5-matrix presentation:
    H_V = H + G^dag G = C_6 - C_5^{tot} + C_5^{vec} + m^2      (m^2 = -4, background X^A = M^{A6}, A=1..5, on Sym^N(4) of su(4)=so(6))
C_6 = sum_{A<B} ad(M_AB)^2 (so(6)), C_5^{tot} = sum_{C<D} (ad(M_CD) (x) 1 + 1 (x) R_CD)^2 (so(5), acting on End(V) (x) C^5), C_5^{vec} = sum R_CD^2.
G(a) = sum_A [X^A,a^A] (background-gauge function); H = Hessian of quantum_compact_hessian.py.
Also prints the spectrum of C_6 - C_5^{tot} + C_5^{vec} on the 'LLL family' (eigenvalue m^2 of H): it vanishes exactly there.
"""
import numpy as np, sys
from quantum_compact_hessian import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 2
mats5 = [Sig[A, 5] for A in range(5)]
X, dd = sym_power_ops(mats5, N)
Mall = {}
allm, _ = sym_power_ops([Sig[A, B] for A in range(6) for B in range(A + 1, 6)], N)
k = 0
for A in range(6):
    for B in range(A + 1, 6):
        Mall[(A, B)] = allm[k]; k += 1
I = np.eye(dd); n2 = dd * dd
def ad(m): return np.kron(m, I) - np.kron(I, m.T)
# kappa: [M_CD, X^A] = kappa i (delta_DA X^C - delta_CA X^D)   (C,D in 0..4)
def comm_(a, b): return a @ b - b @ a
kap = None
C_, D_, A_ = 0, 1, 1
lhs = comm_(Mall[(C_, D_)], X[A_])
rhs = 1j * ((1 if D_ == A_ else 0) * X[C_] - (1 if C_ == A_ else 0) * X[D_])
kap = 1 if np.allclose(lhs, rhs, atol=1e-9) else (-1 if np.allclose(lhs, -rhs, atol=1e-9) else None)
print("kappa =", kap)
# R_CD on vector index: (R v)^A = -kappa i (delta_DA v^C - delta_CA v^D)
def Rmat(C, D):
    R = np.zeros((5, 5), complex)
    R[D, C] += -kap * 1j; R[C, D] += kap * 1j
    return R
Eye5 = np.eye(5)
C6 = sum(ad(Mall[(A, B)]) @ ad(Mall[(A, B)]) for A in range(6) for B in range(A + 1, 6))
C6 = np.kron(Eye5, C6)
C5tot = 0; C5vec = 0
for C in range(5):
    for D in range(C + 1, 5):
        T = np.kron(Eye5, ad(Mall[(C, D)])) + np.kron(Rmat(C, D), np.eye(n2))
        C5tot = C5tot + T @ T
        Rf = np.kron(Rmat(C, D), np.eye(n2))
        C5vec = C5vec + Rf @ Rf
lam = None
acc = sum(comm_(X[B], comm_(X[B], X[0])) for B in range(5)); lam = (np.vdot(X[0], acc) / np.vdot(X[0], X[0])).real
m2 = -lam
H = hessian(X, m2)
# gauge function G: End^5 -> End,  G(a) = sum_A [X^A, a^A];  vec index ordering: block A of size n2
Gm = np.hstack([ad(X[A]) for A in range(5)])
for cG in (+1, -1):
    HV = H + cG * (Gm.conj().T @ Gm)
    R = C6 - C5tot + C5vec + m2 * np.eye(5 * n2)
    print(f"N={N} c_G={cG:+d}: max |H + c_G G^dag G - (C6 - C5tot + C5vec + m2)| =", np.max(np.abs(HV - R)))
