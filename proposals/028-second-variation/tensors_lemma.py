"""028 script 1: species tensors of the supertrace lemma.
H_i = H (x) 1 + sum_{a<b}... : each species has Z_i = sum_{a,b} Sigma_i^{ab} (x) Zop_ab with Zop_ab = {F_ab,.}.
Vector:  (Z A)_c = -2 {F_cb, A^b}  => Sigma_V^{ab} with (Sigma_V^{ab})_c^d = delta^a_c eta^{bd} - delta^b_c eta^{ad}, Z_V = -Sigma_V^{ab} Zop_ab (sum over all a,b).
Fermion: Dslash^2 = Box + (1/2) Gamma^{ab} Zop_ab = Box + Sigma_D^{ab} Zop_ab; the operator compared with H = -Box is H_D = -Dslash^2 = -Box - Sigma_D^{ab} Zop_ab, so Z_D = -Sigma_D (same sign convention as Z_V = -Sigma_V);
 Sigma_D^{ab} = (1/4)[Gamma^a,Gamma^b] (real Majorana 4x4, 4 copies = 16 real comps).
Weights: vector +1 (4 comps), 6 extra scalars +1, ghost -2 (1 comp), fermions -1/2 per real component (16 comps).
Checks: T_n = sum_i w_i tr_i( Z^{a1b1} ... Z^{anbn} ) for n=0..4 (non-symmetrised tensors), and the Dirac/vector ratio of tr(Sigma Sigma)."""
import numpy as np, itertools
rng = np.random.default_rng(1)
eta = np.diag([-1., 1, 1, 1])
# vector rep
def SigV(a, b):
    M = np.zeros((4, 4))
    for c in range(4):
        for d in range(4):
            M[c, d] = (c == a)*eta[b, d] - (c == b)*eta[a, d]     # eta^{bd} with eta^-1 = eta
    return M
# Dirac gamma matrices, real Majorana representation of Cliff(3,1) with Gamma_a Gamma_b + Gamma_b Gamma_a = 2 eta_ab  (signature -+++)
s1 = np.array([[0, 1], [1, 0]]); s3 = np.array([[1, 0], [0, -1]]); e2 = np.array([[0, 1], [-1, 0]]); I2 = np.eye(2)
# real 4x4: gamma^0 antisymmetric squares to -1; gamma^i symmetric squares to +1
g0 = np.kron(e2, I2)
g1 = np.kron(s1, I2)
g2 = np.kron(s3, s1)
g3 = np.kron(s3, s3)
G = [g0, g1, g2, g3]
for a in range(4):
    for b in range(4):
        assert np.allclose(G[a] @ G[b] + G[b] @ G[a], 2*eta[a, b]*np.eye(4)), (a, b)
print("Clifford relation (real 4x4): OK")
def SigD(a, b):
    return 0.25*(G[a] @ G[b] - G[b] @ G[a])
# check algebra: [Sigma^{ab}, Sigma^{cd}] same structure constants for V and D (up to the sign convention of V)
def comm(A, B): return A @ B - B @ A
def struct(Sig, a, b, c, d):
    return comm(Sig(a, b), Sig(c, d))
# find the sign/relation: V gen satisfy the algebra with eta^{..}; check [S^{ab},S^{cd}] = eta^{bc} S^{ad} - ... for both with possible overall sign sD
def lie_rhs(Sig, a, b, c, d):
    return eta[b, c]*Sig(a, d) - eta[a, c]*Sig(b, d) - eta[b, d]*Sig(a, c) + eta[a, d]*Sig(b, c)
for name, S in (("V", SigV), ("D", SigD)):
    errp = max(np.abs(struct(S, a, b, c, d) - lie_rhs(S, a, b, c, d)).max() for a, b, c, d in itertools.product(range(4), repeat=4))
    errm = max(np.abs(struct(S, a, b, c, d) + lie_rhs(S, a, b, c, d)).max() for a, b, c, d in itertools.product(range(4), repeat=4))
    print(name, "algebra: [S,S] = +rhs err %.2e ; = -rhs err %.2e" % (errp, errm))
# species data: list of (weight, [Z matrices Z^{ab}] with Z_i = sum Z^{ab} Zop_ab, mass, dim)
def species():
    sp = []
    ZV = {(a, b): -SigV(a, b) for a in range(4) for b in range(4)}
    sp.append((1.0, ZV, 4, "vector"))
    Z0 = {(a, b): np.zeros((1, 1)) for a in range(4) for b in range(4)}
    sp.append((1.0, {k: np.zeros((6, 6)) for k in Z0}, 6, "6 extra scalars"))
    sp.append((-2.0, {k: np.zeros((1, 1)) for k in Z0}, 1, "ghost"))
    ZD = {(a, b): -SigD(a, b) for a in range(4) for b in range(4)}
    ZD16 = {k: np.kron(np.eye(4), v) for k, v in ZD.items()}
    sp.append((-0.5, ZD16, 16, "16 real fermion comps"))
    return sp
SP = species()
print("component count sum w d =", sum(w*d for w, _, d, _ in SP))
def Tn(n, trials=40):
    """max |sum_i w_i tr(Z^{a1b1}...Z^{anbn})| over all index tuples (random subset for n>=3)"""
    idx = [(a, b) for a in range(4) for b in range(4) if a != b]
    mx = 0.0
    tuples = itertools.product(idx, repeat=n) if n <= 3 else (tuple(idx[i] for i in rng.integers(0, len(idx), n)) for _ in range(trials*50))
    for t in tuples:
        tot = 0.0
        for w, Z, d, _ in SP:
            M = np.eye(Z[idx[0]].shape[0])
            for k in t: M = M @ Z[k]
            tot += w*np.trace(M)
        mx = max(mx, abs(tot))
    return mx
for n in range(0, 5):
    if n == 0: print("T_0 =", sum(w*d for w, _, d, _ in SP)); continue
    print("n=%d : max |sum_i w_i tr(Z...Z)| = %.3e" % (n, Tn(n)))
# ratio tr(Sigma_D Sigma_D) / tr(Sigma_V Sigma_V)
r = []
for a, b, c, d in itertools.product(range(4), repeat=4):
    tv = np.trace(SigV(a, b) @ SigV(c, d)); td = np.trace(SigD(a, b) @ SigD(c, d))
    if abs(tv) > 1e-12: r.append(td/tv)
    else: assert abs(td) < 1e-12
print("tr(Sigma_D Sigma_D)/tr(Sigma_V Sigma_V) over all index pairs: min %.6f max %.6f" % (min(r), max(r)))
# totally symmetrised quartic: character check with commuting field F: sum_i w_i tr exp(-i s Z(F)) vs 4 (cos s f_m - cosh s f_e)^2 ; F_ab(xi) real antisymmetric; Zop_ab -> i F_ab (symbol of derivation)
def char_num(F, s):
    tot = 0.0
    for w, Z, d, _ in SP:
        Zm = sum(Z[(a, b)]*(1j*F[a, b]) for a in range(4) for b in range(4) if a != b)
        ev = np.linalg.eigvals(Zm)
        tot += w*np.sum(np.exp(-1j*s*ev))
    return tot
def fef_m(F):
    ev = np.linalg.eigvals(F @ np.linalg.inv(eta))  # eta F eigenvalues: +-f_e real, +-i f_m
    ev = np.linalg.eigvals(eta @ F)
    fe = max(abs(ev.real)); fm = max(abs(ev.imag))
    return fe, fm
for trial in range(4):
    A = rng.normal(size=(4, 4)); F = A - A.T
    fe, fm = fef_m(F)
    for s in (0.05, 0.3):
        lhs = char_num(F, s); rhs = 4*(np.cos(s*fm) - np.cosh(s*fe))**2
        print("random F: f_e=%.4f f_m=%.4f s=%.2f  Str-char numeric %s  4(cos s f_m - cosh s f_e)^2 = %.8f   s^4 (fe^2+fm^2)^2 = %.8f" % (fe, fm, s, np.round(lhs, 8), rhs, s**4*(fe**2 + fm**2)**2))
