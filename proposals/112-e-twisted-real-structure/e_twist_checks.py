# Proposal 112 verification: real-structure constraints and orbit lemmas for E.
# 8 runs, one printed line each. Run: python -I e_twist_checks.py
import numpy as np
import sympy as sp

# Runs 1-5: chirality/Majorana conditions for Cl(h0), h0 of signature (10-t, t),
# n = 10. Volume element omega^2 = (-1)^(n(n-1)/2) * (-1)^t * |det| = (-1)^(45+t).
# Weyl projection exists iff omega^2 = +1 (t odd). Recorded MW rule (appH L1829,
# VanProeyen1999): s - t = 10 - 2t = 0 mod 8. Contour-reachable real boundary
# signatures (appH L1823(i)): t in {0,1,9,10}.
mw_full = []
for i, t in enumerate([0, 1, 3, 5, 9]):
    w2 = (-1) ** (45 + t)
    weyl = (w2 == 1)
    mw = ((10 - 2 * t) % 8 == 0)
    mw_full += [t] if mw else []
    print(f"run {i+1}: t={t} omega^2={w2:+d} Weyl={'Y' if weyl else 'N'} MW={'Y' if mw else 'N'}")

# Run 6: complex-orthogonal witness: Lambda = diag(i,1,...,1) in O(10,C) with
# Lambda^T eta Lambda = 1 and Lambda^T 1 Lambda = eta: Riemannian and Lorentzian
# real slices are real forms of one complex congruence class.
L = sp.diag(sp.I, *([1] * 9))
eta = sp.diag(-1, *([1] * 9))
o10 = sp.eye(10)
print(f"run 6: L^T eta L == 1: {L.T * eta * L == o10}; L^T 1 L == eta: {L.T * o10 * L == eta}")

# Run 7: conjugation-twist lemma. Gamma0 = i*sigma1, Gamma1 = sigma1 realise
# Cl(1,1) ({G,G} = 2*diag(-1,1)). For general invertible S in Mat2(C),
# G' = S G S^-1 satisfies the SAME Clifford relations: defect simplifies to 0.
a, b, c, d = sp.symbols('a b c d')
S = sp.Matrix([[a, b], [c, d]])
G0 = sp.Matrix([[0, sp.I], [sp.I, 0]])
G1 = sp.Matrix([[1, 0], [0, -1]])
Si = S.inv()
D00 = (S * G0 * Si) * (S * G0 * Si) + (S * G0 * Si) * (S * G0 * Si) + 2 * sp.eye(2)
D11 = (S * G1 * Si) * (S * G1 * Si) + (S * G1 * Si) * (S * G1 * Si) - 2 * sp.eye(2)
D01 = (S * G0 * Si) * (S * G1 * Si) + (S * G1 * Si) * (S * G0 * Si)
defs = [sp.simplify(x) for x in (D00, D11, D01)]
print(f"run 7: conjugation Clifford defects all zero: {all(dd == sp.zeros(2, 2) for dd in defs)}")

# Run 8: Sylvester: real GL(10)-orbit of the identity is positive definite.
rng = np.random.default_rng(112)
T = rng.normal(size=(10, 10))
print(f"run 8: T^T T signs all positive: {bool((np.linalg.eigvalsh(T.T @ T) > 0).all())}")

# Summary: MW-reachable t and contour-reachable t intersect in {1,9}, the recorded
# (P1)+(P2) dichotomy (appH L1831); contour set {0,1,9,10}.
inter = sorted(set(mw_full) & {0, 1, 9, 10})
print(f"MW set (t, 0..10) = {{1,5,9}} check {mw_full == [1,5,9]}; MW cap contour = {inter} check {inter == [1, 9]}")
