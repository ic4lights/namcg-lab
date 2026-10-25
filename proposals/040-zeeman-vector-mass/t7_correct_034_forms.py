"""040 t7: re-evaluate the 034 finite-part forms (pickles l5_forms_*_central.pkl, copied) after correcting the sign of the logarithmic term of 034 l3_fin.integrate
(correct: Fin = int(f - c/s) + c ln(s1) + int_{s1}; the code had -c ln(s1); see t6).  Fin_true = Fin_034 + 2 c ln(s1), s1 = (0.05/max(a,b)) e^{-0.6 i}, c = A/(16 pi^2).
Reports for yy and full: best proportional fit residual to the A-form (Re, Im), eigenvalues on the quotient by kappa, before and after the correction."""
import sys, pickle, numpy as np, mpmath as mp
sys.dont_write_bytecode = True
from l3_fin import *
def analyse(Q, Af, kappa, tag):
    Qb = np.linalg.svd(kappa[None, :])[2][1:]
    for nm, part in (('Re', Q.real), ('Im', Q.imag)):
        lam = np.sum(part * Af) / np.sum(Af * Af)
        res = np.linalg.norm(part - lam * Af) / max(np.linalg.norm(part), 1e-30)
        ev = np.linalg.eigvalsh(Qb @ part @ Qb.T)
        print('   %s %s: lambda=%.3e residual %.3f scheme-invariant defect |Q-lam A|/|A| = %.3e ; quotient eigenvalues (norm.) %s' % (tag, nm, lam, res, np.linalg.norm(part - lam * Af) / np.linalg.norm(Af), np.round(ev / np.abs(ev).max(), 3)))
for (seed, th) in ((12, 0.8), (12, 2.0), (21, 1.4)):
    out = pickle.load(open('l5_forms_%d_%.1f_central.pkl' % (seed, th), 'rb'))
    rng = np.random.default_rng(seed)
    M0 = rand_point(rng); q = rng.normal(size=4); _ = rng.normal(size=4)
    d = leaf_data(M0, q); kappa = d['kappa']; y = d['y']
    cd = canonical_data(d, np.array([np.cos(th), np.sin(th)]), np.zeros(4))
    a, b = cd['a'], cd['b']
    E = np.eye(4); Af = np.zeros((4, 4))
    for i in range(4): Af[i, i] = A_engine(E[i], kappa, y)
    for i in range(4):
        for j in range(i + 1, 4): Af[i, j] = Af[j, i] = (A_engine(E[i] + E[j], kappa, y) - Af[i, i] - Af[j, j]) / 2
    s1 = complex(mp.mpf('0.05') / max(a, b) * PH)
    shift = 2 * np.log(s1) / (16 * np.pi ** 2) * Af
    print('seed %d theta %.1f a=%.3f b=%.3f  shift factor 2 ln s1/(16pi^2) = %s' % (seed, th, a, b, np.round(2 * np.log(s1) / (16 * np.pi ** 2), 4)))
    for mode in ('yy', 'full'):
        analyse(out[mode], Af, kappa, mode + ' (034 as integrated)')
        analyse(out[mode] + shift, Af, kappa, mode + ' (corrected)      ')
