"""Completed-replica W gap on the diagonal profile Theta^{12}=r^{-eps c_a}, |Theta^{34}|=r^{-eps c_b}, both chiralities, with the chirality sign of the J_34 holonomy
taken from diag_family_chirality.py (H = c_a J_12 + chi c_b J_34, chi=+1 SD, -1 ASD).
Independent re-derivation of the metric part: Riem' and Ric' are built from the exact deltas of 035 (R'_{1212}=c_a, R'_{a i b j}=(c_b/2) d_ab d_ij; units 2 pi eps delta_Sigma) and contracted
with the first-order Riemann/Ricci of the delta-rho=0 plane-wave modes; A = Riem.Riem', B = Ric.Ric'.  Decomposition into the Weyl cross term C.C' = A - 2B (+R R'/3 = 0) and the Euler cross term
E4.. = A - 4B (+ R R' = 0).  Calibrations (3 Phi per scalar, tr(H Omega_12) weight kappa_X) are those of 035; they are re-checked here against the periodic scalar value
(1/30)(3W - Rsig) and tau_Omega = -2W + Rsig at c=(1,0)."""
import itertools, sympy as sp
from sympy import Rational as Q
import lin_lib as L, lib
from pairing_modes import modes, gen
ca, cb, Ns, nD = sp.symbols('c_a c_b N_s n_D')
Ntot = Ns + 2 - 4*nD; kX = 1 - nD/2
from profile_lib import Rprime, fit
Rp = Rprime(ca, cb)
Ricp = sp.Matrix(4, 4, lambda n, s: sum(Rp[(m, n, m, s)] for m in range(4)))
print('Ric\' =', sp.simplify(Ricp).tolist())
out = {}
for name, Thb, chi in (('SD', lib.eta3()[2].inv(), 1), ('ASD', lib.etabar()[2].inv(), -1)):
    ms = modes(Thb, 8, 7)
    assert all(m['g0'] == 1 for m in ms) and all(m['R'] == 0 for m in ms)
    Av = [sum(m['Rt'][k]*Rp[k] for k in Rp) for m in ms]
    Bv = [sum(m['Ric'][i, j]*Ricp[i, j] for i in range(4) for j in range(4)) for m in ms]
    A = fit(ms, [sp.expand(a) for a in Av]); B = fit(ms, [sp.expand(b) for b in Bv])
    A = tuple(sp.expand(t) for t in A); B = tuple(sp.expand(t) for t in B)
    CC = tuple(sp.expand(a - 2*b) for a, b in zip(A, B)); E4 = tuple(sp.expand(a - 4*b) for a, b in zip(A, B)); AmB = tuple(sp.expand(a - b) for a, b in zip(A, B))
    print('==', name)
    print('  A  = Riem.Riem\'  (W, Rsig):', A); print('  B  = Ric.Ric\'    (W, Rsig):', B)
    print('  C.C\'  = A-2B     (W, Rsig):', CC, ' -> depends on c_a-c_b only:', sp.simplify(CC[0] - 2*(ca - cb)) == 0 and CC[1] == 0)
    print('  E4 x  = A-4B     (W, Rsig):', E4)
    print('  Phi*90 = A-B     (W, Rsig):', AmB)
    # scalar periodic value check at (1,0): 3 Phi = (1/30)(3W - Rsig)
    chk = [sp.simplify(3*t/90 - c) for t, c in zip(AmB, (Q(3, 30), Q(-1, 30)))]
    print('  calibration at c=(1,0): 3Phi - (1/30)(3W - Rsig) =', [sp.simplify(x.subs({ca: 1, cb: 0})) for x in chk])
    # connection pairing tr(H Omega_12), H = c_a J_12 + chi c_b J_34
    ms2 = ms
    for m in ms2:
        pass
    J12, J34 = gen(0, 1), gen(2, 3)
    tau12 = fit(ms2, [(J12*m['Om12']).trace()/m['g0'] for m in ms2]); tau34 = fit(ms2, [(J34*m['Om12']).trace()/m['g0'] for m in ms2])
    print('  tr(J12 Om12) (W,Rsig) =', tau12, '  tr(J34 Om12) =', tau34)
    conn = tuple(sp.expand(ca*a + chi*cb*b) for a, b in zip(tau12, tau34))
    print('  tr(H Om12) with H = c_a J12 + chi c_b J34 :', conn)
    T = Ntot/10 - 4*kX
    raw = sp.expand(3*Ntot*AmB[0]/90 + kX*conn[0]); gap_raw = sp.factor(sp.expand(raw - T))
    gap_weyl = sp.factor(sp.expand(sp.expand(3*Ntot*(sp.Rational(3, 2)*CC[0])/90 + kX*conn[0]) - T))
    print('  replica W (raw, 035 extension)   :', sp.factor(raw)); print('  gap_raw  = replica - 12 kappa_C^T :', gap_raw)
    print('  gap_Weyl (Euler cross W-part dropped):', gap_weyl)
    print('  gap_raw at c=(1,0):', sp.simplify(gap_raw.subs({ca: 1, cb: 0})), '; at c=(1,-1):', sp.factor(gap_raw.subs({ca: 1, cb: -1})), '; at c=(2,0):', sp.factor(gap_raw.subs({ca: 2, cb: 0})))
    print('  gap_Weyl at c=(1,-1):', sp.factor(gap_weyl.subs({ca: 1, cb: -1})), '; at c=(2,0):', sp.factor(gap_weyl.subs({ca: 2, cb: 0})))
    out[name] = (gap_raw, gap_weyl, conn)
print('rho-preserving profile: Pf(Theta) = Theta^{12}Theta^{34} => delta ln rho = eps (c_a + c_b) ln r (|Theta^{34}| exponent c_b), so delta rho = 0 <=> c_b = -c_a for both chiralities.')
def split(g):
    g1 = sp.simplify(sp.diff(g, Ns)); g2 = sp.simplify(sp.expand(g - g1*Ntot)/kX)
    return g1, g2
for name, (gr, gw, conn) in out.items():
    r1, r2 = split(gr); w1, w2 = split(gw)
    print(name, ': gap_raw  = N_tot*(%s) + kappa_X*(%s)' % (sp.factor(r1), sp.factor(r2)))
    print(name, ': gap_Weyl = N_tot*(%s) + kappa_X*(%s)' % (sp.factor(w1), sp.factor(w2)))
    print('     kappa_X part vanishes at c_a =', sp.solve(r2, ca), ' (raw) and', sp.solve(w2, ca), ' (Weyl)')
