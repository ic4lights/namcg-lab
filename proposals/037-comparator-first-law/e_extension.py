"""037-e: the quadratic form on the delta-rho=0 test modes does not determine the pairing with a direction outside it.
Gamma_1 = (1/12) tr Omega^2   (the actual connection-sector invariant)   vs   Gamma_2 = kappa_J C^2, kappa_J = -1/3   (metric functional with the same value on every mode).
Q_i(S) are quadratic in the second jet S of delta-omega; B_i = polarisation.  We (i) check Q_1 = Q_2 on the plane-wave modes and on sums of modes with different wave vectors
(by polarisation), (ii) exhibit jets S' (generic closed delta-omega, cubic potential) with B_1(S_m,S') != B_2(S_m,S'), i.e. the same quadratic form has different cross terms."""
import random, sympy as sp
from sympy import Rational as Q
import lin_lib as L, lib
from modes_lib import modes, backgrounds
def add(S1, S2): return {k: S1[k] + S2[k] for k in S1}
def Qvals(Thb, S):
    d = L.linear_data(Thb, S)
    return Q(1, 12)*d['trOm2'], Q(-1, 3)*d['C2'], d
def B(Thb, S1, S2, which):
    q = lambda S: Qvals(Thb, S)[which]
    return (q(add(S1, S2)) - q(S1) - q(S2))/2
random.seed(5)
for name, Thb in backgrounds():
    print('==', name)
    ms = modes(Thb, 4, 31)
    Sm = [m['S'] for m in ms]
    print(' (i) Q_1 - Q_2 on single modes :', [sp.simplify(Qvals(Thb, S)[0] - Qvals(Thb, S)[1]) for S in Sm])
    print('     B_1 - B_2 on pairs of modes (different wave vectors):', [sp.simplify(B(Thb, Sm[i], Sm[j], 0) - B(Thb, Sm[i], Sm[j], 1)) for i in range(4) for j in range(i+1, 4)])
    # generic closed jets from a cubic potential
    for trial in range(3):
        Cc = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
        import itertools
        for mu in range(4):
            vals = {}
            for t in itertools.combinations_with_replacement(range(4), 3):
                vals[t] = Q(random.randint(-3, 3), random.randint(1, 3))
            for a in range(4):
                for b in range(4):
                    for c in range(4):
                        Cc[mu][a][b][c] = vals[tuple(sorted((a, b, c)))]
        Sg = L.cubic_S(Cc)
        b1 = B(Thb, Sm[0], Sg, 0); b2 = B(Thb, Sm[0], Sg, 1)
        print(' (ii) trial %d: B_1(S_mode, S_generic) = %s ; B_2 = %s ; difference = %s' % (trial, b1, b2, sp.simplify(b1 - b2)))
