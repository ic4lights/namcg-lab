import sys, os
sys.path.insert(0, os.getcwd())
import numpy as np
np.set_printoptions(precision=3, suppress=True, linewidth=100)
import _common as cm

def probe(L, mu, N):
    sites = np.arange(6, 6 + N)
    C, Pim = cm.restrict(L, mu, sites)
    G = cm.G_block(C, Pim)
    nu = cm.symplectic_spectrum(G)
    nun = 0.5 * (nu[0::2] + nu[1::2])
    # reproduce internals of A_of_G
    n = G.shape[0] // 2
    O = cm.omega(n); Oi = -O
    w, U = np.linalg.eigh(G)
    sq = U @ np.diag(np.sqrt(w)) @ U.T
    T = sq @ Oi @ sq
    antisym = np.max(np.abs(T + T.T))
    B = (-0.5j) * np.linalg.inv(T)
    B = 0.5 * (B + B.conj().T)
    bw, BV = np.linalg.eigh(B)
    bw = np.clip(bw, -1.0 + 1e-12, 1.0 - 1e-12)
    fB = BV @ np.diag(np.arctanh(bw)) @ BV.conj().T
    isq = U @ np.diag(1.0 / np.sqrt(w)) @ U.T
    f = isq @ fB @ sq
    A = 2j * (f @ Oi)
    print("L=%d mu=%.2f N=%d" % (L, mu, N))
    print(" nu-0.5 min=%.3e max=%.3e  |G|=%.3e eigG[min,max]=%.3e,%.3e"
          % (np.min(nun - 0.5), np.max(nun - 0.5), np.max(np.abs(G)), w.min(), w.max()))
    print(" antisym(T)=%.2e  |B| max=%.15f  n(|B|>1-1e-9)=%d"
          % (antisym, np.max(np.abs(bw)), int(np.sum(np.abs(bw) > 1 - 1e-9))))
    print(" A.imag max=%.3e  A.real max=%.3e  (A-A^T)/2 max=%.3e"
          % (np.max(np.abs(A.imag)), np.max(np.abs(A.real)),
             np.max(np.abs(A.real - A.real.T))))
    # eig(B) expected = +/- 0.5/nu_j
    pred = 0.5 / nun
    got = np.sort(np.abs(bw))
    print(" max||bw|-0.5/nu|=%.3e" % np.max(np.abs(got - np.sort(pred))))

for (L, mu, N) in [(31, 0.05, 8), (41, 0.01, 12), (17, 0.7, 1), (23, 0.25, 3)]:
    probe(L, mu, N)
