"""(1) Validate lin_lib against the exact jet code at small epsilon (cubic potential about Theta-bar = (eta^3)^-1).
(2) Plane-wave TT comparison: kappa_J (T side, (1/12) tr Omega^2 / C^2) and the A-side linear functional tau^(1) vs Riemann components."""
import random, itertools, sys
import sympy as sp
from sympy import Rational as Q
import lin_lib as L
import lib

eta3 = lib.eta3()
wbar = eta3[2]
Thb = wbar.inv()

def validate():
    from common import use_gaussian, omega_from_A, QQ_I
    import jetlib as jl
    from jetlib import Jet
    import sector_data as S
    from common import Q as QQ
    use_gaussian(3)
    random.seed(5)
    C = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for mu in range(4):
        for tri in itertools.combinations_with_replacement(range(4), 3):
            val = Q(random.randint(-3, 3), random.randint(1, 3))
            for perm in set(itertools.permutations(tri)):
                C[mu][perm[0]][perm[1]][perm[2]] = val
    eps = Q(1, 10**5)
    A = []
    for mu in range(4):
        d = {}
        for tri in itertools.combinations_with_replacement(range(4), 3):
            mon = [0]*4
            for t in tri: mon[t] += 1
            val = eps * C[mu][tri[0]][tri[1]][tri[2]] / 6 * sp.factorial(3) / sp.prod([sp.factorial(k) for k in mon]) * sp.prod([sp.factorial(k) for k in mon]) / sp.factorial(3) * len(set(itertools.permutations(tri)))
            # monomial x^a x^b x^c coefficient in (1/6) sum_{abc} C x^a x^b x^c = (1/6) * (#perms) * C
            if val != 0:
                d[tuple(mon)] = QQ(val.p, val.q)
        A.append(Jet(d))
    w = omega_from_A(A)
    w = [[w[m][n] + Jet.const(QQ(int(wbar[m, n]))) for n in range(4)] for m in range(4)]
    d = S.run_jets(w)
    S0 = L.cubic_S([[[[eps * C[m][a][b][c] for c in range(4)] for b in range(4)] for a in range(4)] for m in range(4)])
    lin = L.linear_data(Thb, S0)
    for k in ('R', 'Rii', 'Rijij', 'trJOm_v'):
        kk = {'R': 'R', 'Rii': 'Rii', 'Rijij': 'Rj', 'trJOm_v': 'tau'}[k]
        print('validate', k, ' jets:', float(sp.nsimplify(d[k])), ' linear:', float(lin[kk]), ' (sign convention of tau: jets trJOm_v)')
    return

if __name__ == '__main__':
    validate()
