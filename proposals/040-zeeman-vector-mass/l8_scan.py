"""040 l8: scan of the order-eps^2 kappa^2-coefficient responses T2(s) (scalar, Zeeman-dressed vector, single 4x4 Dirac block) on the ray s = rho e^{-i theta*},
theta* = arctan(a/b), for the 10 alpha-directions needed to reconstruct the quadratic form Q(alpha).  Output pickle: rho nodes/weights and values.
usage: python l8_scan.py seed theta0 r mode nq   (mode yy: c0=0 ; full: c0 as on the leaf)"""
import sys, pickle, time, numpy as np, mpmath as mp
sys.dont_write_bytecode = True
from multiprocessing import Pool
from l3_fin import *
from engine_z import *
mp.mp.dps = 50
def make_nodes():
    x8, w8 = np.polynomial.legendre.leggauss(8)
    x6, w6 = np.polynomial.legendre.leggauss(6)
    nodes = []; rho1 = 0.05
    for xx, ww in zip(x6, w6):
        nodes.append((rho1 * (xx + 1) / 2, rho1 * ww / 2, 0))                      # panel 0: (0, rho1), subtraction region
    edges = [rho1 * (1.5 / rho1) ** (k / 4) for k in range(5)]
    edges += [1.5 + 1.5 * k for k in range(1, 31)]
    for lo, hi in zip(edges[:-1], edges[1:]):
        for xx, ww in zip(x8, w8):
            nodes.append((lo + (hi - lo) * (xx + 1) / 2, (hi - lo) * ww / 2, 1))
    return nodes
def setup(seed, th0, r, mode):
    rng = np.random.default_rng(seed)
    M0 = rand_point(rng); q = rng.normal(size=4); _ = rng.normal(size=4)
    d = leaf_data(M0, q)
    E = np.eye(4)
    alphas = [E[i] for i in range(4)] + [E[i] + E[j] for i in range(4) for j in range(i + 1, 4)]
    cds = [canonical_data(d, r * np.array([np.cos(th0), np.sin(th0)]), al) for al in alphas]
    if mode == 'yy':
        for cd in cds: cd['c0'] = 0.0
    return cds
def task(args):
    seed, th0, r, mode, nq, ia, rho = args
    nq = 14 if rho < 2 else (22 if rho < 15 else nq)
    cd = setup(seed, th0, r, mode)[ia]
    a, b = mp.mpf(cd['a']), mp.mpf(cd['b'])
    ths = mp.atan(a / b)
    s = mp.mpf(rho) * mp.expj(-ths)
    lam = mp.mpf('1e-14')
    ka = np.array([mp.mpf(x) for x in cd['kappa']], dtype=object)
    al = np.array([mp.mpf(x) for x in cd['alpha']], dtype=object)
    yy = np.array([mp.mpf(x) for x in cd['y']], dtype=object)
    c0 = mp.mpf(cd['c0'])
    vals = []
    for f in (lam, -lam, 0):
        kk = scale_kappa(ka, f)
        TC, nodes = orbital_nodes(a, b, kk, al, yy, c0, s, nq)
        v = T2_total([vector_species(a, b, kk, al)], TC, nodes, s)
        dsp = dirac_species(a, b, kk, al); dsp.w = mp.mpf(1)
        dd = T2_total([dsp], TC, nodes, s)
        sc = T2_total([scalar_species()], TC, nodes, s)
        vals.append((sc, v, dd))
    res = [(vals[0][i] + vals[1][i] - 2 * vals[2][i]) / (2 * lam ** 2) * Theta(s, a, b) for i in range(3)]
    return [complex(x) for x in res]
if __name__ == "__main__":
    seed = int(sys.argv[1]); th0 = float(sys.argv[2]); r = float(sys.argv[3]); mode = sys.argv[4]; nq = int(sys.argv[5])
    nodes = make_nodes()
    jobs = [(seed, th0, r, mode, nq, ia, nd[0]) for ia in range(10) for nd in nodes]
    t0 = time.time()
    with Pool(16) as p:
        res = p.map(task, jobs, chunksize=1)
    arr = np.array(res).reshape(10, len(nodes), 3)
    pickle.dump(dict(nodes=nodes, vals=arr, seed=seed, th0=th0, r=r, mode=mode, nq=nq), open('l8_scan_%d_%.1f_%s.pkl' % (seed, th0, mode), 'wb'))
    print('done', time.time() - t0, 's, nodes', len(nodes))
