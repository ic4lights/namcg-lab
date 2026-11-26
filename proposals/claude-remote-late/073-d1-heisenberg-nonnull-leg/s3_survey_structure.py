"""S3 (numerical survey, not a classification).  Re-runs the survey of 072 s4 (Heisenberg algebra, kappa = 1,
general constant connection, 120 least-squares starts, seed 5, |w|^2 constrained to 1/4, 1, 4), polishes each
converged solution without the norm constraint, and tests whether it lies in the family of common073:
  (i)   a real null vector n with W_a n proportional to n for all a (least squares over the sphere of directions);
  (ii)  in the adapted basis B_n, J_n, N_e, N_f of that n, the B_n and J_n legs are proportional to k = -n^flat;
  (iii) the leg operator L = eta^{ab} W_a W_b on vectors satisfies L^2 = 0;
  (iv)  tau (T_ac^c = tau k_a) vanishes whenever n is not in the plane of E_0, E_2 (|n^1|, |n^3| > 1e-6);
  the family form (i, ii, iv) is tested at strict and at loose tolerances; near-degenerate solutions with
  nilpotent connection and R_abcd R^abcd close to zero make the null-line test ill-conditioned.
Run: python -I -B s3_survey_structure.py"""
import os, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common073 import *
from scipy.optimize import least_squares

C = K.lie({(3, 1): {2: 1.0}})


def resid(v, s2=None):
    B1, B2, T, R = bg.brackets(C, bg.W_of(v), eta)
    out = [B1.ravel(), B2.ravel()]
    if s2 is not None:
        out.append([np.dot(v, v) - s2])
    return np.concatenate(out)


def nvec(x):
    return np.array([1, np.sin(x[0]) * np.cos(x[1]), np.cos(x[0]), np.sin(x[0]) * np.sin(x[1])])


def null_line(Ms):
    def f(x):
        n = nvec(x); return np.concatenate([M @ n - (M @ n)[0] * n for M in Ms])
    best = None
    for t in np.linspace(0.05, np.pi - 0.05, 24):
        for ph in np.linspace(0, 2 * np.pi, 32, endpoint=False):
            r = least_squares(f, [t, ph], method='lm', xtol=3e-16, ftol=3e-16, gtol=3e-16)
            e = np.abs(f(r.x)).max()
            if best is None or e < best[0]:
                best = (e, nvec(r.x))
            if e < 1e-13:
                return best
    return best


rng = np.random.default_rng(5)
stats = dict(conv=0, clean=0, nullline=0, legs=0, nilp=0, tilted=0, tilted_tau0=0, rrpos=0, restA=0, restB=0, restC=0)
rng2 = np.random.default_rng(11)
worst = dict(nullline=0, legs=0, nilp=0, tau=0)
for trial in range(120):
    s2 = [0.25, 1.0, 4.0][trial % 3]
    v0 = rng.normal(scale=1.0, size=24)
    sol = least_squares(lambda v: resid(v, s2), v0, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=6000)
    if np.abs(resid(sol.x, s2)).max() > 1e-10:
        continue
    stats['conv'] += 1
    v = least_squares(resid, sol.x, method='lm', xtol=3e-16, ftol=3e-16, gtol=3e-16).x
    if np.abs(resid(v)).max() > 1e-13:
        continue
    stats['clean'] += 1
    W = bg.W_of(v); Om, T, Rup = bg.geom(C, W, eta); Ms = [Om[a].T for a in range(4)]
    Rl = np.einsum('abcd,ce,df->abef', Rup, eta, eta); RR = np.einsum('abcd,ax,by,xycd->', Rl, etai, etai, Rup)
    e_n, n = null_line(Ms)
    scale = max(1.0, np.abs(W).max())
    if e_n < 1e-10 * scale:
        stats['nullline'] += 1
    worst['nullline'] = max(worst['nullline'], e_n)
    nh = n[1:]; a_ = np.cross(nh, [0, 0, 1.]) if abs(nh[2]) < 0.9 else np.cross(nh, [1., 0, 0]); a_ /= np.linalg.norm(a_)
    b_ = np.cross(nh, a_)
    e = np.r_[0, a_]; f = np.r_[0, b_]; e0 = np.r_[1., 0, 0, 0]; mh = np.r_[0, -nh]
    basis = [wedge(e0, mh), wedge(e, f), wedge(n, e), wedge(n, f)]
    Bm = np.array([X.ravel() for X in basis]).T
    coef = np.array([np.linalg.lstsq(Bm, W[a].ravel(), rcond=None)[0] for a in range(4)])
    k = -eta @ n
    dev = 0.0
    for col in (0, 1):
        cc = np.linalg.lstsq(k[:, None], coef[:, col], rcond=None)[0][0]
        dev = max(dev, np.abs(coef[:, col] - cc * k).max())
    fitdev = max(np.abs(Bm @ coef[a] - W[a].ravel()).max() for a in range(4))
    infam = e_n < 1e-10 * scale and max(dev, fitdev) < 1e-9 * scale
    if max(dev, fitdev) < 1e-9 * scale:
        stats['legs'] += 1
    worst['legs'] = max(worst['legs'], dev, fitdev)
    L = sum(etai[a, a] * Ms[a] @ Ms[a] for a in range(4))
    if np.abs(L @ L).max() < 1e-12 * scale ** 4:
        stats['nilp'] += 1
    worst['nilp'] = max(worst['nilp'], np.abs(L @ L).max())
    trT = np.einsum('acc->a', T)
    if abs(n[1]) > 1e-6 or abs(n[3]) > 1e-6:
        stats['tilted'] += 1
        if np.abs(trT).max() < 1e-9:
            stats['tilted_tau0'] += 1
        worst['tau'] = max(worst['tau'], np.abs(trT).max())
    if RR > 1e-8:
        stats['rrpos'] += 1
    loose = (e_n < 1e-8 * scale and max(dev, fitdev) < 1e-6 * scale
             and (np.abs(trT).max() < 1e-6 or (abs(n[1]) < 1e-6 and abs(n[3]) < 1e-6)))
    strict = infam and (np.abs(trT).max() < 1e-9 or (abs(n[1]) < 1e-6 and abs(n[3]) < 1e-6))
    if strict:
        stats['restA'] += 1
    elif loose:
        stats['restB'] += 1
        worst['loose_RR'] = max(worst.get('loose_RR', 0.0), abs(RR))
    else:
        stats['restC'] += 1
        print('   not in the family at the loose tolerance: null-line defect %.1e, legs %.1e, |T_ac^c| %.1e, n = %s, RR %+.2e'
              % (e_n, max(dev, fitdev), np.abs(trT).max(), np.round(n, 4), RR))
print('converged %(conv)d of 120; residual below 1e-13 after polishing %(clean)d' % stats)
print('with a common real null eigenvector n: %(nullline)d ; B_n and J_n legs along k (family form): %(legs)d ;'
      ' L^2 = 0: %(nilp)d' % stats)
print('n outside the plane of E_0, E_2: %(tilted)d, of which with T_ac^c = 0: %(tilted_tau0)d ; R_abcd R^abcd > 1e-8: %(rrpos)d' % stats)
print('family form (null line, B_n and J_n legs along k, T_ac^c = 0 unless n is in the plane of E_0, E_2):'
      ' %(restA)d at tolerances 1e-10, 1e-9, 1e-9; %(restB)d more at 1e-8, 1e-6, 1e-6; %(restC)d not' % stats,
      '; largest |R_abcd R^abcd| among the latter group of %(restB)d:' % stats, '%.1e' % worst.get('loose_RR', 0.0))
print('largest defects: null line %.1e, family form %.1e, |L^2| %.1e, |T_ac^c| on tilted %.1e'
      % (worst['nullline'], worst['legs'], worst['nilp'], worst['tau']))
