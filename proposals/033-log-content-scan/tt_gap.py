"""Log-order, variable-independent c-type comparison on delta-rho=0 plane-wave modes about a constant (anti-)self-dual Theta-bar.
T side : coefficient kappa_C^T of C^2 in the weighted a_2 (average over the wave; E4 averages to zero, R=0):
         kappa_C^T = Ntot * (3/360) + b * kappa_J,   kappa_J = (1/12) tr Omega^2 / C^2   (v-4s = (1/12) tr Omega^2 at 2nd order, d-4s = (v-4s)/2: quad_check.py)
A side : first-order functional of Sigma-density (24 pi units), pieces from the same per-component formulas as content_scan.py, evaluated with
         all endomorphism data zero at first order (e^(1)=X'^(1)=0 on delta-rho=0 modes).  Wald universality: a quadratic action
         kC C^2 + kE E4 + kR R^2 has entropy density 12 kC W + 12 kE Rsig + 12 kR R.   Gap = alpha_W(A) - 12 kappa_C^T.
Also the Lambda^2 gaps of appH (c_A - c_T) for the same replicas, for comparison."""
import random, sympy as sp
from sympy import Rational as Q
import lin_lib as L, lib
Ns, nD = sp.symbols('Ns nD')
Ntot = Ns + 2 - 4*nD; b = 1 - nD/2
def modes(Thb, n, seed):
    random.seed(seed); out = []
    rnd = lambda: Q(random.randint(-4, 4), random.randint(1, 3))
    while len(out) < n:
        p = [rnd() for _ in range(4)]
        if all(x == 0 for x in p): continue
        v = sp.symbols('v0:4'); S, w = L.hat_S(p, list(v))
        cond = sp.expand((Thb*w).trace()); vv = [rnd() for _ in range(3)]
        sol = sp.solve(cond.subs(dict(zip(v[:3], vv))), v[3], dict=True)
        if not sol: continue
        vals = dict(zip(v[:3], vv)); vals[v[3]] = sol[0][v[3]]
        S, w = L.hat_S(p, [x.subs(vals) for x in v]); d = L.linear_data(Thb, S)
        if d['C2'] != 0: out.append(d)
    return out
for name, Thb in (('SD  Theta-bar=(eta^3)^-1', lib.eta3()[2].inv()), ('ASD Theta-bar=(etabar^3)^-1', lib.etabar()[2].inv())):
    ms = modes(Thb, 6, 11)
    print('==', name, ' (6 delta-rho=0 modes)')
    kJs = {sp.Rational(1, 12)*m['trOm2']/m['C2'] for m in ms}
    print(' kappa_J values:', kJs, ' R values', {m['R'] for m in ms}, ' Euler', {m['Euler'] for m in ms}, ' tau+Rj', {m['tau'] + m['Rj'] for m in ms})
    kJ = list(kJs)[0]
    # A-side first-order functionals (e=X'=trE=0, R=0): per-component pieces
    def A_of(m, kind):
        Q_ = m['Rii'] - 2*m['Rj']; tau = m['tau']
        Dper_c = (4*sp.Rational(1, 30))*Q_ * (-1) * (-1)           # Dper = -(0) + (4/30) Q  (E-terms zero)
        D = (4*sp.Rational(1, 30))*Q_ - tau/2                       # Z_n Dirac: -[x*0 - y(4/30)Q + z tau]
        bos = -((Ns + 2)/30)*Q_
        per = bos + nD*(Dper_c) * (1)
        # periodic Dirac per field: -(0 - (4/30)Q) = +(4/30)Q
        fs = bos + nD*D
        comp = fs + tau                                              # C_E = 0 (a1=0), C_Om = tau
        return {'per': per, 'fs': fs, 'comp': comp}[kind]
    res = {}
    for kind in ('per', 'fs', 'comp'):
        # fit A = aW*W + aS*Rsig (R=0)
        aW, aS = sp.symbols('aW aS')
        eqs = [sp.expand(A_of(m, kind) - aW*m['W'] - aS*m['Rsig']) for m in ms[:2]]
        sol = sp.solve(eqs, [aW, aS], dict=True)[0]
        resid = [sp.simplify(sp.expand(A_of(m, kind) - sol[aW]*m['W'] - sol[aS]*m['Rsig'])) for m in ms[2:]]
        res[kind] = (sp.simplify(sol[aW]), sp.simplify(sol[aS]))
        print(' replica', kind, ': alpha_W =', res[kind][0], ' alpha_Rsig =', res[kind][1], ' residuals on other modes:', set(resid))
    kT = Ntot*sp.Rational(3, 360) + b*kJ
    print(' T side kappa_C^T =', sp.expand(kT), ' ; 12 kappa_C^T =', sp.expand(12*kT))
    for kind in ('per', 'fs', 'comp'):
        gap = sp.expand(res[kind][0] - 12*kT)
        print('  gap(', kind, ') = alpha_W - 12 kappa_C^T =', gap, ' =', sp.factor(gap), '; zero at nD =', sp.solve(gap, nD))
print()
print('Lambda^2 gaps of appH (c_A - c_T, c_T = Ntot/6 - 4b): periodic 4-2nD = 4b ; antiperiodic fixed-state 4 - nD ; smooth/completed c_A^sm - c_T = -Ntot/4 + 4b')
cT = Ntot/6 - 4*b
print(' check:', sp.expand(Ntot/6 - cT), sp.expand(Ntot/6 + nD - cT), sp.expand(-Ntot/12 - cT))
