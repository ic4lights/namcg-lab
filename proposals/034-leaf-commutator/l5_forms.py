"""034 script 5: quadratic forms in alpha of the finite part Fin, split by the content of P = y.omega + c0:  yy (tetrad^2, c0 = 0),  cc (charge^2, y = 0),  cross = full - yy - cc.
Central (corrected) model, leaf data, one orbit point and one centre direction.  Fin is a quadratic form Fin(alpha) = alpha^T Q alpha; Q reconstructed by polarisation (10 evaluations).
Reports: gauge test |Q kappa|/(|Q||kappa|); best proportional fit of Q_yy to the A-form (the coefficient of the log); eigenvalues on the quotient by kappa."""
import numpy as np, mpmath as mp, sys, time, pickle
sys.dont_write_bytecode = True
from multiprocessing import Pool
from l3_fin import *
def evalFin(args):
    seed, th, mode, al, model, nq, nn, nint = args
    rng = np.random.default_rng(seed)
    M0 = rand_point(rng); q = rng.normal(size=4); _ = rng.normal(size=4)
    d = leaf_data(M0, q)
    cd = canonical_data(d, np.array([np.cos(th), np.sin(th)]), np.array(al))
    if mode == 'yy': cd['c0'] = 0.0
    if mode == 'cc': cd['y'] = np.zeros(4)
    A, c, fin, f = fin_case(cd, model=model, nquad=nq, nn=nn, nint=nint)
    return complex(fin), float(A), float(c)
def forms(seed, th, model='central', nq=12, nn=6, nint=5):
    E = np.eye(4)
    alphas = [E[i] for i in range(4)] + [E[i] + E[j] for i in range(4) for j in range(i + 1, 4)]
    out = {}
    for mode in ('yy', 'cc', 'full'):
        jobs = [(seed, th, mode, tuple(a), model, nq, nn, nint) for a in alphas]
        with Pool(16) as p:
            res = p.map(evalFin, jobs, chunksize=1)
        v = [r[0] for r in res]
        Q = np.zeros((4, 4), complex)
        for i in range(4): Q[i, i] = v[i]
        k = 4
        for i in range(4):
            for j in range(i + 1, 4):
                Q[i, j] = Q[j, i] = (v[k] - v[i] - v[j]) / 2; k += 1
        out[mode] = Q
    return out
if __name__ == "__main__":
    seed = int(sys.argv[1]); th = float(sys.argv[2]); model = sys.argv[3] if len(sys.argv) > 3 else 'central'
    t0 = time.time()
    out = forms(seed, th, model)
    pickle.dump(out, open('l5_forms_%d_%.1f_%s.pkl' % (seed, th, model), 'wb'))
    rng = np.random.default_rng(seed)
    M0 = rand_point(rng); q = rng.normal(size=4); _ = rng.normal(size=4)
    d = leaf_data(M0, q); kappa = d['kappa']; y = d['y']
    cd = canonical_data(d, np.array([np.cos(th), np.sin(th)]), np.zeros(4))
    # A-form in the ORIGINAL (non-canonical) variables
    E = np.eye(4); Af = np.zeros((4, 4))
    for i in range(4): Af[i, i] = A_engine(E[i], kappa, y)
    for i in range(4):
        for j in range(i + 1, 4): Af[i, j] = Af[j, i] = (A_engine(E[i] + E[j], kappa, y) - Af[i, i] - Af[j, j]) / 2
    # forms were computed with alpha in the ORIGINAL variables (canonical_data transforms inside) -> comparable
    print("model", model, "seed", seed, "theta", th, "time %.0fs" % (time.time() - t0))
    kn = np.linalg.norm(kappa)
    Qb = np.linalg.svd(kappa[None, :])[2][1:]
    for mode in ('yy', 'cc', 'full'):
        Q = out[mode]
        gauge = np.linalg.norm(Q @ kappa) / (np.linalg.norm(Q) * kn)
        print(" %s: |Q kappa|/(|Q||kappa|) = %.1e" % (mode, gauge))
    Q = out['yy']
    for nm, part in (('Re', Q.real), ('Im', Q.imag)):
        lam = np.sum(part * Af) / np.sum(Af * Af)
        res = np.linalg.norm(part - lam * Af) / max(np.linalg.norm(part), 1e-30)
        ev = np.linalg.eigvalsh(Qb @ part @ Qb.T)
        print(" yy %s: best fit lambda*A-form: lambda=%.4e  residual %.3f ; eigenvalues on quotient (normalised) %s" % (nm, lam, res, np.round(ev / np.abs(ev).max(), 3)))
    evA = np.linalg.eigvalsh(Qb @ Af @ Qb.T); print(" A-form eigenvalues on quotient (normalised):", np.round(evA / np.abs(evA).max(), 3))
    Qc = out['cc']
    for nm, part in (('Re', Qc.real), ('Im', Qc.imag)):
        ev = np.linalg.eigvalsh(Qb @ part @ Qb.T)
        print(" cc %s: eigenvalues on quotient (normalised) %s" % (nm, np.round(ev / np.abs(ev).max(), 3)))
