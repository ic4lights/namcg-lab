"""034 script 4: Fin/c on the leaf, central (corrected) versus interleaved (032) model, several centre directions, two orbit points.  Parallel (multiprocessing)."""
import numpy as np, mpmath as mp, time, sys, pickle
sys.dont_write_bytecode = True
from multiprocessing import Pool
from l3_fin import *
def job(args):
    seed, th, model, nq, nn, nint = args
    rng = np.random.default_rng(seed)
    M0 = rand_point(rng); q = rng.normal(size=4); alpha = rng.normal(size=4)
    d = leaf_data(M0, q)
    cd = canonical_data(d, np.array([np.cos(th), np.sin(th)]), alpha)
    A, c, fin, f = fin_case(cd, model=model, nquad=nq, nn=nn, nint=nint)
    a, b = mp.mpf(cd['a']), mp.mpf(cd['b'])
    rho = mp.mpf('1e-4') / max(a, b)
    s = rho * PH
    small = f(s) * s / c
    return dict(seed=seed, th=th, model=model, a=float(a), b=float(b), c0=cd['c0'], A=float(A), c=float(c), fin=complex(fin), fin_over_c=complex(fin / c), small_ratio=complex(small))
if __name__ == "__main__":
    nq = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    nn = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    nint = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    seeds = [12, 21]
    ths = [0.3, 0.8, 1.4, 2.0, 2.6, 3.0]
    jobs = [(sd, th, m, nq, nn, nint) for sd in seeds for th in ths for m in ('central', 'interleaved')]
    t = time.time()
    with Pool(16) as pool:
        res = pool.map(job, jobs, chunksize=1)
    pickle.dump(res, open('l4_res_nq%d_nn%d_ni%d.pkl' % (nq, nn, nint), 'wb'))
    for r in res:
        print("seed %d th=%.1f %-11s a=%.3f b=%.3f c0=%+.2f  A=%+.4e  c*(small-s ratio T2 s/c)=%.4f%+.4fj  Fin/c = %.4f %+.4fj" % (r['seed'], r['th'], r['model'], r['a'], r['b'], r['c0'], r['A'], r['small_ratio'].real, r['small_ratio'].imag, r['fin_over_c'].real, r['fin_over_c'].imag))
    print("time", time.time() - t)
