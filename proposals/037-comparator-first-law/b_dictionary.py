"""037-b: replica <-> fibre-holonomy dictionary for the W coefficient on the 033 modes, and the holonomy that reproduces the metric-universal comparator.
A side (033 per-component first-order functionals of the Sigma-density, 24 pi units, evaluated with e = X' = a1 = 0 at first order):
   Q = R_ii - 2 R_ijij,  tau = tr(J_12 Omega_12) (vector bundle; = Dirac tau with J -> gamma^12/2)
   periodic : -((Ns+2)/30) Q + nD (4/30) Q
   fixed    : -((Ns+2)/30) Q + nD ((4/30) Q - tau/2)
   completed: fixed + tau
T side, Noether in the variables (G, omega) with holonomy H = alpha_v J_12 on the vector bundle and alpha_f gamma^12/2 on each Dirac fibre:
   metric part Ntot/120 C^2 -> Wald universality 12*Ntot/120 W ; connection part kappa_v alpha_v tau + nD kappa_f alpha_f tau, kappa_v = 1, kappa_f = -1/2 (weights of the Dynkin index).
Comparator (metric-universal): 12 kappa_C^T, kappa_C^T = Ntot/120 + kappa_X (1/12) tr Omega^2 / C^2."""
import sympy as sp
from modes_lib import *
Ns, nD, av, af = sp.symbols('Ns nD alpha_v alpha_f')
Ntot = Ns + 2 - 4*nD; kX = 1 - nD/2
def fitW(ms, vals):
    aW, aS = sp.symbols('aW aS')
    sol = sp.solve([vals[i] - aW*ms[i]['W'] - aS*ms[i]['Rsig'] for i in range(2)], [aW, aS], dict=True)[0]
    res = {sp.simplify(vals[i] - sol[aW]*ms[i]['W'] - sol[aS]*ms[i]['Rsig']) for i in range(2, len(vals))}
    assert res == {0}, res
    return sp.simplify(sol[aW]), sp.simplify(sol[aS])
for name, Thb in backgrounds():
    ms = modes(Thb, 6, 11)
    print('==', name)
    Qs = [m['Rii'] - 2*m['Rj'] for m in ms]; taus = [m['tau'] for m in ms]
    A = {'periodic': [-((Ns+2)/sp.Integer(30))*q + nD*sp.Rational(4, 30)*q for q in Qs],
         'fixed':    [-((Ns+2)/sp.Integer(30))*q + nD*(sp.Rational(4, 30)*q - t/2) for q, t in zip(Qs, taus)]}
    A['completed'] = [f + t for f, t in zip(A['fixed'], taus)]
    aW = {k: fitW(ms, v)[0] for k, v in A.items()}
    tauW, tauS = fitW(ms, taus)
    kJ = {sp.Rational(1, 12)*m['trOm2']/m['C2'] for m in ms}; assert len(kJ) == 1; kJ = kJ.pop()
    kCT = Ntot*sp.Rational(3, 360) + kX*kJ
    univ = sp.expand(12*kCT)
    print(' W-coefficient of tau = tr(J12 Omega12):', tauW, ' ; kappa_J = tr Omega^2/(12 C^2) =', kJ)
    print(' universal comparator 12 kappa_C^T =', univ)
    def TN(a_v, a_f):
        return sp.expand(12*Ntot*sp.Rational(1, 120) + (a_v*1 + nD*(-sp.Rational(1, 2))*a_f)*tauW)
    hol = {'periodic': (0, 0), 'fixed': (0, 1), 'completed': (1, 1)}
    for k in A:
        g_univ = sp.expand(aW[k] - univ); g_N = sp.expand(aW[k] - TN(*hol[k]))
        print('  %-9s A_W = %s ; gap vs universal = %s ; gap vs Noether%s = %s' % (k, sp.expand(aW[k]), g_univ, hol[k], g_N))
    # residual gaps against the spin-complete Noether value (1,1)
    print(' residual of each replica against T_N(1,1):', {k: sp.expand(aW[k] - TN(1, 1)) for k in A})
    # holonomy reproducing the universal comparator: common alpha_v = alpha_f = a
    a = sp.symbols('a')
    print(' common alpha with T_N(a,a) = 12 kappa_C^T :', sp.solve(sp.expand(TN(a, a) - univ), a))
    print(' T_N(0,0) - universal =', sp.expand(TN(0, 0) - univ), ' (= 4 kappa_X =', sp.expand(4*kX), ')')
