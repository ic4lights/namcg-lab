"""B-R2 pairing test.  First-order Omega^v_{12} about constant (A)SD Theta-bar on delta-rho=0 plane-wave modes
(033 lin_lib, copied).  For every so(4) generator J_ab (J[a,b]=1,J[b,a]=-1) compute  tau_ab = tr(J_ab Omega_12)/g0 and fit
tau_ab = a_W W + a_S Rsig  (R=0 on these modes).  tau_01 is the 029/033 tau_Omega (= -Rijij).
Then ask which holonomy H = alpha J_01 + beta J_23 has  tr(H Omega_12)|_W = -4 (twice the Levi-Civita value -2),
i.e. makes the Omega^2 part of the area-side W coefficient equal to the T side 12*kappa_J = -4 per unit kappa_X."""
import random, itertools, sympy as sp
from sympy import Rational as Q
import lin_lib as L, lib

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
        S, w = L.hat_S(p, [x.subs(vals) for x in v])
        d = L.linear_data(Thb, S)
        if d['C2'] == 0: continue
        # recompute Omega_12 matrix (linear_data only returns scalars) 
        D2Th = {k: -Thb * S[k] * Thb for k in S}
        g0 = d['g0']
        Om12 = g0 * sum((Thb[r, 1]*D2Th[(0, r)] - Thb[r, 0]*D2Th[(1, r)] for r in range(4)), sp.zeros(4, 4))
        d['Om12'] = Om12
        out.append(d)
    return out

def gen(a, b):
    J = sp.zeros(4, 4); J[a, b] = 1; J[b, a] = -1; return J

if __name__ == '__main__':
    pairs = [(0,1),(2,3),(0,2),(1,3),(0,3),(1,2)]
    for name, Thb in (('SD', lib.eta3()[2].inv()), ('ASD', lib.etabar()[2].inv())):
        ms = modes(Thb, 8, 5)
        print('==', name, 'background; g0 =', ms[0]['g0'])
        aW, aS = sp.symbols('aW aS')
        res = {}
        for (a, b) in pairs:
            J = gen(a, b)
            taus = [(J*m['Om12']).trace()/m['g0'] for m in ms]
            sol = sp.solve([taus[i]-aW*ms[i]['W']-aS*ms[i]['Rsig'] for i in range(2)], [aW, aS], dict=True)[0]
            resid = {sp.simplify(taus[i]-sol[aW]*ms[i]['W']-sol[aS]*ms[i]['Rsig']) for i in range(2, len(ms))}
            res[(a,b)] = (sol[aW], sol[aS])
            print(' J_%d%d : tr(J Omega_12) = %s W + %s Rsig ; residual on other modes %s' % (a+1, b+1, sol[aW], sol[aS], resid))
        # check tau_01 = -Rijij
        print(' check tau_01 + Rj :', {sp.simplify((gen(0,1)*m['Om12']).trace()/m['g0'] + m['Rj']) for m in ms})
        # required holonomy: alpha*aW01 + beta*aW23 = -4
        a01, a23 = res[(0,1)][0], res[(2,3)][0]
        print(' W-coeff of tau_01, tau_23 :', a01, a23, '; need alpha*a01+beta*a23 = -4 ; (alpha,beta)=(1,0) gives', a01, '; (1,+-1):', a01+a23, a01-a23)
        # full Omega_12 compared with Riemann: norm ratio  tr Omega_{st}^2 vs Riemann
        print(' kappa_J (tr Om^2/(12 C2)) :', {sp.Rational(1,12)*m['trOm2']/m['C2'] for m in ms})
