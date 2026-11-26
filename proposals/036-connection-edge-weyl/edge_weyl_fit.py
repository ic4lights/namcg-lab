"""Weyl (W) content of Sigma-intrinsic edge densities on the 033 test modes (delta-rho=0 plane waves about constant SD / ASD Theta-bar, totally geodesic Sigma, first order in 1-n).
Units 1/(24 pi).  Basis (W, Rsig, R, e, X') of 033/035; on the modes R = e = X' = 0 at first order.
(1) (W, Rsig) are independent linear functionals on the 12 modes (rank 2), so the W coefficient of a density is well defined;
(2) the Donnelly-Wall edge density (negative scalar on Sigma with the intrinsic Laplacian) is -Rsig: W-coefficient 0;
(3) Hessians of the Theta-invariants Pf and tr(Theta^2) vanish on the modes, so a weight w(Pf, tr Theta^2) in -w^{-1} div(w grad) adds nothing at first order;
(4) the normal-plane Ricci R_ii, R_ijij, and the manuscript's Hodge contact -(R_Sigma - R_ii) in the (W, Rsig) basis: the R_ii part carries W, the intrinsic R_Sigma part does not;
(5) what a Sigma-potential would have to be: -(R_Sigma + 6 E_Sigma) with E_Sigma|_W = kappa_X/3 for a W-coefficient -2 kappa_X, a content-dependent requirement."""
import sympy as sp
from sympy import Rational as Q
import lin_lib as L, lib
from pairing_modes import modes
kX, nD = sp.symbols('kappa_X n_D')
def fit(ms, vals):
    aW, aS = sp.symbols('aW aS')
    sol = sp.solve([vals[i]-aW*ms[i]['W']-aS*ms[i]['Rsig'] for i in range(2)], [aW, aS], dict=True)[0]
    res = {sp.simplify(vals[i]-sol[aW]*ms[i]['W']-sol[aS]*ms[i]['Rsig']) for i in range(2, len(vals))}
    assert res == {0}, res
    return sp.simplify(sol[aW]), sp.simplify(sol[aS])
for name, Thb in (('SD', lib.eta3()[2].inv()), ('ASD', lib.etabar()[2].inv())):
    ms = modes(Thb, 8, 3)
    print('==', name)
    M = sp.Matrix([[m['W'], m['Rsig']] for m in ms]); print(' rank of [(W, Rsig) over 8 modes] =', M.rank(), ' ; R values', {m['R'] for m in ms})
    print(' R_ii       (W,Rsig) =', fit(ms, [m['Rii'] for m in ms]), ' ; R_ijij =', fit(ms, [m['Rj'] for m in ms]))
    edge = fit(ms, [-m['Rsig'] for m in ms]); print(' DW edge density -R_Sigma: (W,Rsig) =', edge)
    hodge_contact = fit(ms, [-(m['Rsig'] - m['Rii']) for m in ms]); print(' Hodge contact -(R_Sigma - R_ii): (W,Rsig) =', hodge_contact, ' [W coefficient is carried by the R_ii part]')
    # Hessians of Pf and tr Theta^2 on the modes
    import random
    worst = 0
    for m in ms:
        pass
    t = sp.Symbol('t')
    # recompute modes' Hessians: use S from pairing_modes by regenerating with same seed is not exposed; test on fresh modes via lin_lib.hat_S
    random.seed(3)
    rnd = lambda: Q(random.randint(-4, 4), random.randint(1, 3))
    cnt = 0
    while cnt < 6:
        p = [rnd() for _ in range(4)]
        if all(x == 0 for x in p): continue
        v = sp.symbols('v0:4'); S, w = L.hat_S(p, list(v))
        vv = [rnd() for _ in range(3)]
        sol = sp.solve(sp.expand((Thb*w).trace()).subs(dict(zip(v[:3], vv))), v[3], dict=True)
        if not sol: continue
        vals = dict(zip(v[:3], vv)); vals[v[3]] = sol[0][v[3]]
        S, w = L.hat_S(p, [x.subs(vals) for x in v])
        D2 = -Thb*S[(0, 0)]*Thb
        dtr2 = 2*(Thb*D2).trace()
        Th = Thb + t*D2
        dpf = sp.diff(lib.pf4(Th), t).subs(t, 0)
        worst = max(worst, abs(dtr2), abs(dpf)); cnt += 1
    print(' max |Hessian of tr Theta^2|, |Hessian of Pf| on 6 fresh modes:', worst)
Rs, Rii, Rij = sp.symbols('Rs Rii Rij')
print('\n(5) edge Sigma-potential: density -(R_Sigma + 6 E_Sigma); with E_Sigma = alpha R_ii + beta R_ijij (R=0), W,Rsig coefficients (R_ii=W-Rsig, R_ijij=2W-Rsig):')
al, be = sp.symbols('alpha beta'); W, Rsg = sp.symbols('W Rsig')
dens = sp.expand(-(Rsg + 6*(al*(W-Rsg) + be*(2*W-Rsg))))
print('  W coefficient =', sp.simplify(dens.coeff(W, 1)), ' ; Rsig coefficient =', sp.simplify(dens.coeff(Rsg, 1)))
print('  for W coefficient -2 kappa_X: alpha + 2 beta = kappa_X/3 (content-dependent: kappa_X = 1 - n_D/2)')
print('  a single vector edge field (weight 1, n_D-independent) can match 2 kappa_X = 2 - n_D for all n_D only if alpha+2beta = (1 - n_D/2)/3 varies with n_D: impossible for a constant.')
