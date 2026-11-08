"""060 / s5 (r2, finding M2 of review-r1): the four T^a = M^{a c0} and their commutators span the subalgebra
so(eta restricted to {a, c0}); compute its dimension and Killing-form inertia in the defining representation.
Cases: so(4,2) c0=4 (class: indices 0..4, so(4,1)); so(4,2) c0=5 (indices 0..3,5: so(3,2));
so(6) c0=4 (so(5)); so(5,1) with four spacelike indices 1..4 and c0=5 spacelike (so(5), compact: the
non-compact real form so(5,1) still has a finite-N solution through a compact subalgebra)."""
import numpy as np
from itertools import combinations

def gen(eta, A, B):
    n = len(eta); m = np.zeros((n, n), complex)
    for C in range(n):
        for D in range(n):
            m[C, D] = 1j*(eta[A]*(A == C)*(B == D) - eta[B]*(B == C)*(A == D))
    return m

def span_closure(mats):
    basis = []
    def add(X):
        v = np.concatenate([X.real.ravel(), X.imag.ravel()])
        Bm = np.array([np.concatenate([b.real.ravel(), b.imag.ravel()]) for b in basis] + [v])
        if np.linalg.matrix_rank(Bm, tol=1e-9) > len(basis):
            basis.append(X); return True
        return False
    for X in mats:
        add(X)
    changed = True
    while changed:
        changed = False
        for X, Y in combinations(list(basis), 2):
            if add(X @ Y - Y @ X):
                changed = True
    return basis

def killing_inertia(eta, idx):
    """Trace form tr(XY) on real elements X = i M^{AB}, A<B in idx (proportional to the Killing form of
    the so(p,q) they generate); also checks that these M^{AB} span the closure of the T^a."""
    reals = [1j*gen(eta, A, B) for A, B in combinations(idx, 2)]
    G = np.array([[np.trace(x @ y).real for y in reals] for x in reals])
    ev = np.linalg.eigvalsh(G)
    return int(np.sum(ev > 1e-9)), int(np.sum(ev < -1e-9)), reals

cases = [("so(4,2), c0=4 (manuscript class)", [-1, 1, 1, 1, 1, -1], [0, 1, 2, 3], 4),
         ("so(4,2), c0=5 (base coordinates)", [-1, 1, 1, 1, 1, -1], [0, 1, 2, 3], 5),
         ("so(6), c0=4 (compact twin)", [1]*6, [0, 1, 2, 3], 4),
         ("so(5,1), S={1,2,3,4}, c0=5", [-1, 1, 1, 1, 1, 1], [1, 2, 3, 4], 5)]
for name, eta, S, c0 in cases:
    T = [gen(eta, a, c0) for a in S]
    B = span_closure(T)
    kp, km, R = killing_inertia(eta, sorted(S + [c0]))
    Vb = np.array([b.ravel() for b in B]); Vr = np.array([b.ravel() for b in R])  # complex spans
    rb, rr, rboth = (np.linalg.matrix_rank(x, tol=1e-9) for x in (Vb, Vr, np.vstack([Vb, Vr])))
    same = (rb == rr == rboth == 10)
    sig = [eta[i] for i in S + [c0]]
    print(f"{name}: span dim {len(B)}; eta on the five indices {sig}; span = so(eta|five indices): {same}; "
          f"trace form on real elements (+,-) = ({kp},{km}) -> {'compact' if kp == 0 else 'non-compact'}")
