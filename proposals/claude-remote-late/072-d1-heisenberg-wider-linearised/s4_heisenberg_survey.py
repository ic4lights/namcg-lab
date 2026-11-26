"""S4 (numerical survey, not a classification).  On the Heisenberg algebra [E_3, E_1] = kappa E_2 (kappa = 1),
solve the first two brackets B1 = B2 = 0 for a general constant connection w_a^{cd} (24 parameters) by
least squares from random starts (scipy), and record for each converged solution:
  - the 'leg' form  G^{cd,ef} = eta^{ab} w_a^{cd} w_b^{ef}  (6 x 6); on the wider family it vanishes
    identically, because w_a = k_a M with k null; it carries the w^2 part eta^{ab} w_a w_b of
    nabla^a nabla_a (G != 0 is invariant under constant Lorentz rotations of the frame index);
  - R_abcd R^abcd and the trace T_ac^c;
  - the third bracket nabla^a F_ab - T_ab^c F^a_c for F_ab = -c_ab^c t_c, t = T_ac^c / 2.
Each start constrains |w|^2 (sum of the 24 parameters squared) to 1/4, 1 or 4, which excludes w = 0.
Run: python -I -B s4_heisenberg_survey.py"""
import os, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
import numpy as np
from scipy.optimize import least_squares

eta = K.ETA; etai = np.linalg.inv(eta)
C = K.lie({(3, 1): {2: 1.0}})


def resid(v, s2=None):
    B1, B2, T, R = bg.brackets(C, bg.W_of(v), eta)
    out = [B1.ravel(), B2.ravel()]
    if s2 is not None:
        out.append([np.dot(v, v) - s2])
    return np.concatenate(out)


def third(W):
    Om, T, Rup = bg.geom(C, W, eta)
    t = 0.5 * np.einsum('acc->a', T)
    F = -np.einsum('abc,c->ab', C, t)
    nF = np.einsum('xaz,zb->xab', Om, F) + np.einsum('xbz,az->xab', Om, F)
    return np.einsum('xa,xab->b', etai, nF) - np.einsum('abc,ax,xc->b', T, etai, F)


def leg(W):
    Wp = np.array([[W[a, c, d] for (c, d) in bg.PAIRS] for a in range(4)])
    return np.einsum('ab,ai,bj->ij', etai, Wp, Wp)


rng = np.random.default_rng(5)
rows = []
NT = 120
for trial in range(NT):
    s2 = [0.25, 1.0, 4.0][trial % 3]
    v0 = rng.normal(scale=1.0, size=24)
    sol = least_squares(lambda v: resid(v, s2), v0, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=6000)
    r = np.abs(resid(sol.x, s2)).max()
    if r > 1e-10:
        continue
    W = bg.W_of(sol.x)
    Om, T, Rup = bg.geom(C, W, eta)
    Rl = np.einsum('abcd,ce,df->abef', Rup, eta, eta)
    RR = np.einsum('abcd,ax,by,xycd->', Rl, etai, etai, Rup)
    G = leg(W)
    rows.append((np.abs(G).max() / np.dot(sol.x, sol.x), RR, np.abs(third(W)).max(), np.abs(np.einsum('acc->a', T)).max(), np.abs(sol.x).max()))
print('converged %d of %d starts (|w|^2 constrained to 1/4, 1 or 4)' % (len(rows), NT))
rows.sort(key=lambda z: -z[0])
nz = [z for z in rows if z[0] > 1e-8]
print('solutions with a non-null leg (|G| / |w|^2 > 1e-8): %d' % len(nz))
print('among them: RR > 1e-8: %d, RR < -1e-8: %d, |RR| <= 1e-8: %d; |trace T| > 1e-8: %d; max |third bracket| %.1e'
      % (sum(z[1] > 1e-8 for z in nz), sum(z[1] < -1e-8 for z in nz), sum(abs(z[1]) <= 1e-8 for z in nz),
         sum(z[3] > 1e-8 for z in nz), max(z[2] for z in nz)))
for z in rows[:12]:
    print('  |G|/|w|^2 = %.3e  RR = %+.3e  |third bracket| = %.1e  |trace T| = %.3f  |w|max = %.3f' % z)
