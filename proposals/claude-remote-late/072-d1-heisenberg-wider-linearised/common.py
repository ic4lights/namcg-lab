"""Shared set-up for 072: imports the 071/068 linearisation code read-only (no bytecode written).
Background: time x Heisenberg, [E_3,E_1] = kappa E_2, E_0 and E_2 central, constant connection
w_a^{cd} = k_a (chi B + zeta N + x N')^{cd}, k_a = (1,0,1,0), normalisation of 071 (first-order part
E_a + 1/2 w S at u = 1).  Landau sector: E_0 = i q0, E_2 = i p, E_1, E_3 oscillator (core068.heisenberg_modes)."""
import os, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
P071 = os.path.normpath(os.path.join(HERE, '..', '071-d1-curved-torsion-backgrounds'))
sys.path.insert(0, P071)
import numpy as np
import core068 as K
import tools068 as Tl
import bg, lin

KL = np.array([1.0, 0, 1.0, 0])
Bg, N1, N2 = lin.Bg, lin.N1, lin.N2


def wider(kappa=1.0, chi=0.0, zeta=0.0, x=0.0):
    C = K.lie({(3, 1): {2: kappa}})
    W = np.einsum('a,cd->acd', KL, chi * Bg + zeta * N1 + x * N2)
    return C, W


def modes(p, q0, N, kappa):
    return K.heisenberg_modes(p, q0, N, kappa)
