"""Does the vector-sector bundle curvature Omega^v differ from the Levi-Civita curvature (in the Hamiltonian frame E_A = Theta^{A rho} d_rho)
by an expression that is algebraic in the first jet of omega (torsion), i.e. independent of the second jet?
Test: fix omega(0), d omega(0); vary the second-order jet (cubic part of the potential A, omega = dA).  For each sign/transposition
convention compute D = Omega^v_{st} - R_frame_{st} and compare the two second-jet choices.
Frame: E_B^l = Theta^{B l}, coframe e^A_r = (E^{-1})_r^A.  R_frame[A][B] = e^A_r R^r_{l s t} E_B^l.
"""
import sys, random, itertools
import sympy as sp
from common import *
import jetlib as jl
from jetlib import Jet
import geom
use_gaussian(3)

base = [[Q(0), Q(2), Q(1), Q(0)], [Q(-2), Q(0), Q(0), Q(1)], [Q(-1), Q(0), Q(0), Q(3)], [Q(0), Q(-1), Q(-3), Q(0)]]

def A_jets(seed2, seed3, seed4):
    A = [dict() for _ in range(4)]
    for deg, seed in ((2, seed2), (3, seed3), (4, seed4)):
        random.seed(seed)
        for mu in range(4):
            for mon in itertools.product(range(deg + 1), repeat=4):
                if sum(mon) == deg:
                    c = Q(random.randint(-3, 3), random.randint(1, 3))
                    if random.random() < 0.6 and not jl.isz(c):
                        A[mu][mon] = c
    return [Jet(d) for d in A]

def cc(z):
    z = z.c0() if hasattr(z, 'c0') else z
    return sp.sympify(QQ_I.to_sympy(z))

def data(Aj):
    w = omega_from_A(Aj)
    w = [[w[m][n] + Jet.const(base[m][n]) for n in range(4)] for m in range(4)]
    Th = theta_from_omega(w)
    Ginv, G, rho = geom.metric_data(Th)
    Gam = geom.christoffel(G, Ginv)
    Rm, Ric, Rs = geom.riemann(Gam, G, Ginv)
    Av, Bv = geom.vector_AB(Th, G, Ginv, rho)
    om, EV, Om = geom.vassilevich(Av, Bv, G, Ginv, Gam, 4)
    Th0 = sp.Matrix(4, 4, lambda i, j: cc(Th[i][j]))
    Rl = {k: cc(v) for k, v in Rm.items()}
    Omc = [[sp.Matrix(4, 4, lambda i, j: cc(Om[m][k][i][j])) for k in range(4)] for m in range(4)]
    return Th0, Rl, Omc

def frame_R(Th0, Rl, s, t, conv):
    E = Th0 if conv[0] == 0 else Th0.T                     # E[B][l] = Theta^{B l}  or Theta^{l B}
    Einv = E.inv()                                         # Einv[r][A]
    M = sp.zeros(4, 4)
    for A in range(4):
        for B in range(4):
            M[A, B] = sum(Einv[r, A] * Rl[(r, l, s, t)] * E[B, l] for r in range(4) for l in range(4))
    return M

if __name__ == '__main__':
    d1 = data(A_jets(11, 21, 31)); d2 = data(A_jets(11, 22, 32))          # same first jet, different second jet
    Th0a, Rla, Oma = d1; Th0b, Rlb, Omb = d2
    print('same Theta(0):', Th0a == Th0b)
    for conv in ((0,), (1,)):
        for sgn in (+1, -1):
            for transp in (False, True):
                diffs = []
                for (s, t) in ((0, 1), (0, 2), (2, 3)):
                    Da = Oma[s][t] - sgn * (frame_R(Th0a, Rla, s, t, conv).T if transp else frame_R(Th0a, Rla, s, t, conv))
                    Db = Omb[s][t] - sgn * (frame_R(Th0b, Rlb, s, t, conv).T if transp else frame_R(Th0b, Rlb, s, t, conv))
                    diffs.append(sp.simplify(Da - Db).is_zero_matrix)
                print('frame conv', conv, 'sign', sgn, 'transpose', transp, ': (Omega - R_frame) independent of 2nd jet at 3 components ->', diffs)
                sys.stdout.flush()
    # also report whether Omega itself and R_frame separately depend on the 2nd jet
    print('Omega depends on 2nd jet:', not all(sp.simplify(Oma[s][t] - Omb[s][t]).is_zero_matrix for (s, t) in ((0, 1), (0, 2))))
