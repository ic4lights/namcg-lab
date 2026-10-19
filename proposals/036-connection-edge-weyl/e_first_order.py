"""Lemma E.  First-order (in the amplitude eps) endomorphism data of the three sectors at the origin, for a cubic potential A_mu = eps*(1/6)C_{mu abc}x^a x^b x^c
about a constant (anti-)self-dual Theta-bar (Euclid eta = delta, jet code of 033, exact rational arithmetic, eps = 1/1000 and 1/4000).
Reported: (i) the matrix E_V (vector, 4x4) and E_f (Dirac, 4x4) and the scalar e, divided by eps, split into trace part, symmetric traceless part, antisymmetric part;
(ii) for generic C and for C subject to the delta-rho = 0 condition tr(Theta-bar S_ab) = 0 for all a,b (S_ab = d_a d_b delta-omega).
Expected: the antisymmetric parts and the symmetric traceless part vanish at O(eps); the trace part is proportional to delta ln rho and vanishes on the delta-rho=0 modes."""
import random, itertools, sympy as sp
from common import *
import jetlib as jl
from jetlib import Jet
import geom, lib
import lin_lib as L
use_gaussian(3)
gm = gam_mn_domain()

def cc(z):
    z = z.c0() if hasattr(z, 'c0') else z
    return sp.sympify(QQ_I.to_sympy(z))

def random_C(seed, Thb, constrained):
    random.seed(seed)
    idx = list(itertools.combinations_with_replacement(range(4), 3))
    syms = {(mu, t): sp.Symbol('c_%d_%d%d%d' % ((mu,) + t)) for mu in range(4) for t in idx}
    def Cfun(mu, a, b, c):
        return syms[(mu, tuple(sorted((a, b, c))))]
    C = [[[[Cfun(m, a, b, c) for c in range(4)] for b in range(4)] for a in range(4)] for m in range(4)]
    vals = {s: sp.Rational(random.randint(-3, 3), random.randint(1, 3)) for s in syms.values()}
    if constrained:
        S = L.cubic_S(C)
        eqs = sorted({sp.expand((Thb * S[(a, b)]).trace()) for a in range(4) for b in range(4)} - {0}, key=str)
        # solve for the c_0_* (mu=0) entries in terms of the others
        unk = [syms[(0, t)] for t in idx] + [syms[(1, t)] for t in idx]
        sol = sp.solve(eqs, unk, dict=True)[0]
        free = {s: v for s, v in vals.items() if s not in sol}
        vals = dict(free)
        for k, v in sol.items():
            vals[k] = sp.nsimplify(v.subs(free))
    return [[[[sp.Rational(sp.sympify(C[m][a][b][c]).subs(vals)) for c in range(4)] for b in range(4)] for a in range(4)] for m in range(4)]

def run(Thb, wbar, C, eps):
    A = []
    for mu in range(4):
        d = {}
        for tri in itertools.combinations_with_replacement(range(4), 3):
            mon = [0] * 4
            for t in tri: mon[t] += 1
            val = eps * C[mu][tri[0]][tri[1]][tri[2]] / 6 * len(set(itertools.permutations(tri)))
            if val != 0: d[tuple(mon)] = QQ_I.from_sympy(sp.Rational(val))
        A.append(Jet(d))
    w = omega_from_A(A)
    w = [[w[m][n] + Jet.const(QQ_I.from_sympy(sp.Integer(int(wbar[m, n])))) for n in range(4)] for m in range(4)]
    Th = theta_from_omega(w)
    Ginv, G, rho = geom.metric_data(Th)
    Gam = geom.christoffel(G, Ginv)
    out = {}
    A_, B_ = geom.scalar_AB(Th, G, Ginv, rho); om, EV, Om = geom.vassilevich(A_, B_, G, Ginv, Gam, 1); out['e'] = sp.Matrix(1, 1, lambda i, j: cc(EV[0][0]))
    A_, B_ = geom.vector_AB(Th, G, Ginv, rho); om, EV, Om = geom.vassilevich(A_, B_, G, Ginv, Gam, 4); out['EV'] = sp.Matrix(4, 4, lambda i, j: cc(EV[i][j]))
    A_, B_ = geom.dirac_AB(Th, G, Ginv, rho, gm); om, EV, Om = geom.vassilevich(A_, B_, G, Ginv, Gam, 4); out['Ef'] = sp.Matrix(4, 4, lambda i, j: cc(EV[i][j]))
    g0 = sp.Matrix(4, 4, lambda i, j: cc(G[i][j]))
    out['lnrho'] = cc(sp.log(1)) if False else None
    return out, g0

def parts(M):
    n = M.shape[0]
    tr = M.trace() / n
    sym = (M + M.T) / 2 - tr * sp.eye(n)
    asym = (M - M.T) / 2
    return tr, sym, asym

if __name__ == '__main__':
    for name, wbar in (('SD', lib.eta3()[2]), ('ASD', lib.etabar()[2])):
        Thb = wbar.inv()
        for constrained in (False, True):
            for seed in (1, 2):
                C = random_C(seed, Thb, constrained)
                S = L.cubic_S(C)
                drho = [sp.simplify((Thb * S[(a, b)]).trace()) for a in range(4) for b in range(4)]
                print('==', name, 'constrained' if constrained else 'generic', 'seed', seed, ' max|tr(Theta-bar S_ab)| =', max(abs(x) for x in drho))
                for eps in (sp.Rational(1, 1000), sp.Rational(1, 4000)):
                    out, g0 = run(Thb, wbar, C, eps)
                    for key in ('EV', 'Ef'):
                        tr, sym, asym = parts(out[key])
                        print('   eps=%s %s/eps: trace part %s ; |sym traceless|max %s ; |antisym|max %s' % (eps, key, sp.N(tr / eps, 6), sp.N(max(abs(x) for x in sym) / eps, 6), sp.N(max(abs(x) for x in asym) / eps, 6)))
                    print('   eps=%s e/eps = %s' % (eps, sp.N(out['e'][0, 0] / eps, 6)))
