"""040 l9: from the l8 scan, build the regulated finite parts Fin_X(m2) (X = scalar, vector, Dirac block), the quadratic forms Q_X(alpha), and test
 (a) gauge invariance  Q kappa = 0 ;  (b) the 1/s coefficient against 16 pi^2 c = A, 4A - F1, 4A - F1/2 ;
 (c) proportionality of Q_vec to the log form (4A - F1) and to A (scheme-invariant defect |Q - lam L|/|L|) ;  (d) quotient spectra, and for the mass-linear combination
     x Q_S + mu2 Q_V (x = n_ex mu_i^2 free, mu2 = -3) whether any x gives a definite form on the quotient (real part of  i*(...) and of (...));
 (e) the massless supertrace  int ds/s (vec + 4 scal - 2 dirac) : its small-s order and its regulated value ;
 (f) dependence on the regulator m2 (units of a) and Richardson extrapolation m2 -> 0.
usage: python l9_fin_analysis.py pickle"""
import sys, pickle, numpy as np, mpmath as mp
sys.dont_write_bytecode = True
from l3_fin import A_engine, etan
from l8_scan import setup
d = pickle.load(open(sys.argv[1], 'rb'))
nodes = d['nodes']; V = d['vals']; seed, th0, r, mode = d['seed'], d['th0'], d['r'], d['mode']
cds = setup(seed, th0, r, mode)
a, b = cds[0]['a'], cds[0]['b']; ths = np.arctan(a / b); ph = np.exp(-1j * ths)
rho = np.array([n[0] for n in nodes]); w = np.array([n[1] for n in nodes]); pan = np.array([n[2] for n in nodes])
print('seed', seed, 'theta0', th0, 'r', r, 'mode', mode, 'a,b', a, b, 'theta*', ths)
E = np.eye(4)
alphas = [E[i] for i in range(4)] + [E[i] + E[j] for i in range(4) for j in range(i + 1, 4)]
def c16_of(cd):
    kap, y, al = cd['kappa'], cd['y'], cd['alpha']
    A = A_engine(al, kap, y)
    y2 = y @ etan @ y; k2 = kap @ etan @ kap; ka = kap @ etan @ al; a2 = al @ etan @ al
    F1 = y2 * (ka ** 2 - k2 * a2)
    return A, F1
c16 = np.zeros((10, 3), complex)
for ia, cd in enumerate(cds):
    A, F1 = c16_of(cd)
    c16[ia] = [A, 4 * A - F1, 4 * A - F1 / 2]
def fin(ia, ix, m2):
    c = c16[ia, ix] / (16 * np.pi ** 2)
    s = rho * ph
    f = V[ia, :, ix]
    reg = np.exp(-1j * s * m2)
    p0 = pan == 0
    tot = np.sum(w[p0] * ph * (f[p0] * reg[p0] - c / s[p0]))
    tot += c * np.log(0.05 * ph)
    tot += np.sum(w[~p0] * ph * f[~p0] * reg[~p0])
    return tot
def form(ix, m2, fun=None):
    v = [fin(ia, ix, m2) for ia in range(10)]
    Q = np.zeros((4, 4), complex)
    for i in range(4): Q[i, i] = v[i]
    k = 4
    for i in range(4):
        for j in range(i + 1, 4):
            Q[i, j] = Q[j, i] = (v[k] - v[i] - v[j]) / 2; k += 1
    return Q
def qform(vals10):
    Q = np.zeros((4, 4), complex)
    for i in range(4): Q[i, i] = vals10[i]
    k = 4
    for i in range(4):
        for j in range(i + 1, 4):
            Q[i, j] = Q[j, i] = (vals10[k] - vals10[i] - vals10[j]) / 2; k += 1
    return Q
# orig-variable data
rng = np.random.default_rng(seed)
from leafdata import rand_point, leaf_data
M0 = rand_point(rng); q = rng.normal(size=4); _ = rng.normal(size=4)
dd = leaf_data(M0, q); kappa = dd['kappa']; y = dd['y']
Lforms = []
for ix in range(3):
    Lforms.append(qform(c16[:, ix]))
Qb = np.linalg.svd(kappa[None, :])[2][1:]
def qspec(Q):
    return np.linalg.eigvalsh(Qb @ Q @ Qb.T)
def defect(Q, L):
    out = []
    for part, lpart in ((Q.real, L.real), (Q.imag, L.imag)):
        lam = np.sum(part * lpart) / np.sum(lpart * lpart)
        out.append((lam, np.linalg.norm(part - lam * lpart) / np.linalg.norm(lpart)))
    return out
# (b) small-s check of the coefficient
for ix, nm in enumerate(('scal', 'vec', 'dirac')):
    ia = 3; s = rho[0] * ph
    print('small-s %s: s*f/(c) at rho=%.4f : %s' % (nm, rho[0], np.round(V[ia, 0, ix] * s / (c16[ia, ix] / (16 * np.pi ** 2)), 4)))
m2s = [0.4, 0.5, 0.6, 0.8, 1.0, 1.3]
res = {}
for m2 in m2s:
    mm = m2 * max(a, b)
    Qs = {nm: form(ix, mm) for ix, nm in enumerate(('scal', 'vec', 'dirac'))}
    res[m2] = Qs
    print('=== regulator m2 = %.2f max(a,b) ===' % m2)
    for nm in Qs:
        Q = Qs[nm]
        print(' %-5s gauge |Qk|/(|Q||k|)=%.1e' % (nm, np.linalg.norm(Q @ kappa) / (np.linalg.norm(Q) * np.linalg.norm(kappa))))
    L_vec = Lforms[1]
    dv = defect(Qs['vec'], L_vec); ds_ = defect(Qs['scal'], Lforms[0]); dA = defect(Qs['vec'], Lforms[0])
    print(' vec vs log form (4A-F1): Re lam=%.3e defect=%.3e ; Im lam=%.3e defect=%.3e' % (dv[0][0], dv[0][1], dv[1][0], dv[1][1]))
    print(' vec vs A             : Re lam=%.3e defect=%.3e ; Im lam=%.3e defect=%.3e' % (dA[0][0], dA[0][1], dA[1][0], dA[1][1]))
    print(' scal vs A            : Re lam=%.3e defect=%.3e ; Im lam=%.3e defect=%.3e' % (ds_[0][0], ds_[0][1], ds_[1][0], ds_[1][1]))
    print(' quotient spectra  scal Re/Im:', np.round(qspec(Qs['scal'].real), 5), np.round(qspec(Qs['scal'].imag), 5))
    print('                   vec  Re/Im:', np.round(qspec(Qs['vec'].real), 5), np.round(qspec(Qs['vec'].imag), 5))
    mu2 = -3.0
    defin = []
    for x in np.linspace(-60, 60, 241):
        Q = x * Qs['scal'] + mu2 * Qs['vec']
        for tag, part in (('Re', Q.real), ('Im', Q.imag)):
            ev = qspec(part)
            if ev.min() > 0 or ev.max() < 0:
                defin.append((tag, round(x, 2)))
    print(' x = n_ex mu_i^2 values (grid -60..60) giving a definite quotient form for x*Q_S + mu2*Q_V :', defin[:6], '... count', len(defin))
# (f) extrapolation m2 -> 0
print('=== extrapolation of Fin_vec(m2) entries to m2 -> 0 (Neville, polynomial in m2) ===')
xs = np.array(m2s)
for nm in ('scal', 'vec'):
    ent = np.array([[res[m][nm][i, j] for (i, j) in ((0, 0), (1, 1), (2, 2), (3, 3), (0, 1), (2, 3))] for m in m2s])
    for nn in (3, 4, 6):
        P = ent[:nn].copy(); x = xs[:nn] * max(a, b)
        for k in range(1, nn):
            P = np.array([(-x[i + k] * P[i] + x[i] * P[i + 1]) / (x[i] - x[i + k]) for i in range(nn - k)])
        print(' %s extrap with first %d points:' % (nm, nn), np.round(P[0], 4))
    print(' %s at m2=%s (first, last):' % (nm, (m2s[0], m2s[-1])), np.round(ent[0], 4), np.round(ent[-1], 4))
# (e) massless supertrace
print('=== massless supertrace: integrand (vec + 4 scal - 2 dirac_block)/s ===')
fstr = V[:, :, 1] + 4 * V[:, :, 0] - 2 * V[:, :, 2]
for ia in (3, 7):
    print(' alpha-index %d: |f_str| at rho=%.4f, %.4f, 0.3, 1.5, 10:' % (ia, rho[0], rho[3]), [float(np.abs(fstr[ia, k])) for k in (0, 3)], [float(np.abs(fstr[ia, k])) for k in (np.argmin(np.abs(rho - 0.3)), np.argmin(np.abs(rho - 1.5)), np.argmin(np.abs(rho - 10)))])
