"""040 l10: complements to l9 on the same scan.
(1) massless supertrace Q_str(m2) = int ds/s e^{-i s m2} (vec + 4 scal - 2 dirac)(s) (no ultraviolet logarithm: the order-s coefficient cancels), for m2 regulators; gauge test, proportionality to A,
    quotient spectra, scheme-independent (no log scheme enters).
(2) relative defects ||Q - lam L||/||Q|| for the vector mass-linear form against L = 4A - F1 and A, real part; size of Im relative to Re; spectra.
(3) tail truncation: change of Fin when the upper limit rho_max is reduced from 45 to 38."""
import sys, pickle, numpy as np
sys.dont_write_bytecode = True
exec(open('l9_fin_analysis.py').read().split("# (b) small-s check")[0].replace("d = pickle.load(open(sys.argv[1], 'rb'))", "d = pickle.load(open(sys.argv[1], 'rb'))"))
def fin_cut(ia, ix, m2, rmax):
    c = c16[ia, ix] / (16 * np.pi ** 2); s = rho * ph; f = V[ia, :, ix]; reg = np.exp(-1j * s * m2)
    keep = rho <= rmax; p0 = pan == 0
    tot = np.sum(w[p0] * ph * (f[p0] * reg[p0] - c / s[p0])) + c * np.log(0.05 * ph)
    k = (~p0) & keep
    return tot + np.sum(w[k] * ph * f[k] * reg[k])
def str_val(ia, m2, rmax=1e9):
    s = rho * ph; f = V[ia, :, 1] + 4 * V[ia, :, 0] - 2 * V[ia, :, 2]; reg = np.exp(-1j * s * m2)
    k = rho <= rmax
    return np.sum(w[k] * f[k] / rho[k] * reg[k])
def Qstr(m2, rmax=1e9):
    return qform([str_val(ia, m2, rmax) for ia in range(10)])
def rel_def(Q, L):
    P = Q.real
    lam = np.sum(P * L.real) / np.sum(L.real ** 2)
    return lam, np.linalg.norm(P - lam * L.real) / np.linalg.norm(P)
print('--- (1) massless supertrace, regulated ---')
for m2 in (0.4, 0.6, 0.8, 1.0, 1.3):
    mm = m2 * max(a, b)
    Q = Qstr(mm); Qc = Qstr(mm, 38.0)
    lamA, dA = rel_def(Q, Lforms[0])
    print(' m2=%.1f max(a,b): gauge %.1e ; trunc(45->38) change %.1e ; Re vs A: lam=%.3e rel.defect=%.3f ; |Im|/|Re|=%.2f' % (m2, np.linalg.norm(Q @ kappa) / (np.linalg.norm(Q) * np.linalg.norm(kappa)), np.linalg.norm(Q - Qc) / np.linalg.norm(Q), lamA, dA, np.linalg.norm(Q.imag) / np.linalg.norm(Q.real)))
    print('    quotient spectra Re:', np.round(qspec(Q.real), 5), ' Im:', np.round(qspec(Q.imag), 5))
print('--- (2) vector mass-linear form (yy), relative defects and truncation ---')
for m2 in (0.4, 0.6, 0.8, 1.0, 1.3):
    mm = m2 * max(a, b)
    Q = qform([fin_cut(ia, 1, mm, 1e9) for ia in range(10)]); Qc = qform([fin_cut(ia, 1, mm, 38.0) for ia in range(10)])
    lamL, dL = rel_def(Q, Lforms[1]); lamA, dA = rel_def(Q, Lforms[0])
    print(' m2=%.1f: trunc change %.1e ; Re vs (4A-F1): lam=%.3e rel.defect=%.3f ; Re vs A: lam=%.3e rel.defect=%.3f ; |Im|/|Re|=%.2f ; quotient Re spectrum %s Im %s' % (m2, np.linalg.norm(Q - Qc) / np.linalg.norm(Q), lamL, dL, lamA, dA, np.linalg.norm(Q.imag) / np.linalg.norm(Q.real), np.round(qspec(Q.real), 3), np.round(qspec(Q.imag), 3)))
print('--- (3) scalar form for comparison (Re vs A, sign structure) ---')
for m2 in (0.4, 1.0):
    mm = m2 * max(a, b)
    Q = qform([fin_cut(ia, 0, mm, 1e9) for ia in range(10)])
    lamA, dA = rel_def(Q, Lforms[0])
    print(' m2=%.1f: scal Re vs A lam=%.3e rel.defect=%.3f ; spectra Re %s Im %s' % (m2, lamA, dA, np.round(qspec(Q.real), 4), np.round(qspec(Q.imag), 4)))
print('--- (4) definiteness of x Q_S + mu2 Q_V (mu2=-3) for the real part and the imaginary part, over x in [-60,60] ---')
for m2 in (0.4, 0.6, 0.8, 1.0, 1.3):
    mm = m2 * max(a, b)
    QS = qform([fin_cut(ia, 0, mm, 1e9) for ia in range(10)]); QV = qform([fin_cut(ia, 1, mm, 1e9) for ia in range(10)])
    out = {}
    for tag, fn in (('Re', lambda Q: Q.real), ('Im', lambda Q: Q.imag)):
        xs = [x for x in np.linspace(-60, 60, 481) if (lambda ev: ev.min() > 0 or ev.max() < 0)(qspec(fn(x * QS - 3.0 * QV)))]
        out[tag] = (len(xs), (min(xs), max(xs)) if xs else None)
    print(' m2=%.1f: definite for x (count of 481, range): Re %s ; Im %s' % (m2, out['Re'], out['Im']))
