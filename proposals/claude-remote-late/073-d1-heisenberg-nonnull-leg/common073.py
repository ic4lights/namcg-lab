"""Shared set-up for 073 (imports the 071/068 linearisation code read-only, no bytecode written).
Background: time x Heisenberg, [E_3,E_1] = kappa E_2 (E_0, E_2 central), constant connection in the
normalisation of 071 (first-order part E_a + 1/2 w_a^{cd} S_cd at u = 1).
Family (null line n = (1, s, -c, 0), c = sqrt(1 - s^2); e = (0, c, s, 0), f = (0, 0, 0, 1); k_a = -eta_ab n^b):
   w_a = k_a (chi B_n + th J_n) + P_a N_e + Q_a N_f,
   B_n = e_0 ^ (-nhat), J_n = e ^ f, N_e = n ^ e, N_f = n ^ f   (X^{cd} = u^c v^d - u^d v^c),
   P = zeta k + al e + (be + th) f,  Q = x k + be e + ga f      (e, f lowered with eta),
   constraint  th^2 - 2 th be - 2 be^2 - al^2 - ga^2 + 2 chi (al + ga) = 0,  and tau := chi + al + ga = 0 if s != 0.
At s = 0: n = (1,0,-1,0), k = (1,0,1,0), B_n = B, J_n = J_13, N_e = N, N_f = N' of 071/072; the 072 wider family is
th = al = be = ga = 0."""
import os, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
P071 = os.path.normpath(os.path.join(HERE, '..', '071-d1-curved-torsion-backgrounds'))
sys.path.insert(0, P071)
import numpy as np
import core068 as K
import tools068 as Tl
import bg, lin

eta = K.ETA; etai = np.linalg.inv(eta)


def wedge(u, v):
    return np.outer(u, v) - np.outer(v, u)


def family(kap, s, chi, th, zeta, x, al, be, ga):
    c = np.sqrt(1 - s * s)
    n = np.array([1, s, -c, 0.]); e = np.array([0, c, s, 0.]); f = np.array([0, 0, 0, 1.])
    mnh = np.array([0, -s, c, 0.]); e0 = np.array([1., 0, 0, 0])
    k = -eta @ n; eL = eta @ e; fL = eta @ f
    Bn, Jn, Ne, Nf = wedge(e0, mnh), wedge(e, f), wedge(n, e), wedge(n, f)
    P = zeta * k + al * eL + (be + th) * fL; Q = x * k + be * eL + ga * fL
    W = (np.einsum('a,cd->acd', k, chi * Bn + th * Jn) + np.einsum('a,cd->acd', P, Ne)
         + np.einsum('a,cd->acd', Q, Nf))
    return K.lie({(3, 1): {2: kap}}), W, k, n


def constraint(chi, th, al, be, ga):
    return th ** 2 - 2 * th * be - 2 * be ** 2 - al ** 2 - ga ** 2 + 2 * chi * (al + ga)


def lambdas(chi, th, tau):
    """Shift classes Lambda (roots on (q + Lambda k)^2 = 0) and their numbers of quadratic factors per level
    l >= 3 (half at l = +-1): iota/2 (10), i(tau/2+chi) (2), i(tau/2+chi) +- th (2 each), i(tau-3chi/2) +- rho (2 each)."""
    rho = np.sqrt(complex(1.5 * th ** 2 - chi ** 2 + (tau - 3 * chi) ** 2 / 4))
    L = [1j * tau / 2, 1j * (tau / 2 + chi), 1j * (tau / 2 + chi) + th, 1j * (tau / 2 + chi) - th,
         1j * (tau - 1.5 * chi) + rho, 1j * (tau - 1.5 * chi) - rho]
    return L, [10, 2, 2, 2, 2, 2]


def modes(p, q0, N, kap):
    return K.heisenberg_modes(p, q0, N, kap)
