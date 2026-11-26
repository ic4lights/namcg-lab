#!/usr/bin/env python3
"""Package 059, numerical probe (not a proof): first-order damping directions at N=2 for linear maps that
also mix the colour components, A = Lambda X with Lambda in GL(30, C) acting on vec(x), x the 10 x 3 matrix
of colour columns x^a, starting at the real contour Lambda = 1 with a real target contraction h0.

To first order in tau, along Lambda = 1 + tau (K_R + i K_I):  Im S_b(Lambda X) = tau g(x) + O(tau^2), with
g(x) = grad S_b(x) . K_I vec(x), and S_b = (1/8)[(tr G)^2 - tr G^2], G = x^T h0 x, grad S_b = (1/2) h0 x (tr G - G).
A path keeping Re i S_b <= 0 needs g >= 0 for all real x.  The LP below maximises the mean of g over a sample
of unit x subject to g >= 0 on the sample and |K_I| <= 1 entrywise.  An optimum ~0 means: on the sample, no
first-order direction other than those with g = 0.  Positive optima are validated on a fresh sample.
Runs: colour-blind (K_I = k (x) 1_3, 100 variables) and full colour mixing (900 variables), t = 1, 2, 5.
"""
import numpy as np
from scipy.optimize import linprog
rng = np.random.default_rng(5959)
n, c = 10, 3

def grad(x, h0):
    G = x.T @ h0 @ x
    return 0.5*h0 @ x @ (np.trace(G)*np.eye(c) - G)

def rows(xs, h0, blind):
    R = []
    for x in xs:
        gr = grad(x, h0)
        if blind:
            # K_I acts on the index only: g = sum_{mu,nu} k_{mu nu} sum_a gr[mu,a] x[nu,a]
            R.append((gr @ x.T).ravel())
        else:
            R.append(np.outer(gr.ravel(order='F'), x.ravel(order='F')).ravel())
    return np.array(R)

def sample(m, t):
    # columns x^a = cos(phi) u_+ + sin(phi) u_-, u_+ / u_- random unit vectors in the positive / negative
    # eigenspaces of h0 (h0 diagonal), phi uniform; half of the columns plain Gaussian.  This puts weight on
    # the definite and mixed 2-planes, where violations of g >= 0 sit when t or 10-t is small.
    xs = rng.normal(size=(m, n, c))
    if 0 < t < n:
        up = rng.normal(size=(m, n - t, c)); up /= np.linalg.norm(up, axis=1)[:, None, :]
        um = rng.normal(size=(m, t, c)); um /= np.linalg.norm(um, axis=1)[:, None, :]
        phi = rng.uniform(0, 2*np.pi, size=(m, 1, c))
        st = np.concatenate([np.cos(phi)*up, np.sin(phi)*um], axis=1)
        mask = rng.random((m, 1, c)) < 0.5
        xs = np.where(mask, st, xs)
    return xs/np.linalg.norm(xs.reshape(m, -1), axis=1)[:, None, None]

def run(t, blind, m_fit, m_pool, iters=8, add=1000):
    """Cutting-plane LP: fit on a working set, add the worst violators from a fresh pool, repeat."""
    h0 = np.diag([1.0]*(n - t) + [-1.0]*t)
    A = rows(sample(m_fit, t), h0, blind)
    nv = A.shape[1]
    hist = []
    for it in range(iters):
        res = linprog(-A.mean(axis=0), A_ub=-A, b_ub=np.zeros(len(A)), bounds=[(-1, 1)]*nv, method='highs')
        k = res.x
        P = rows(sample(m_pool, t), h0, blind)
        g = P @ k
        scale = np.abs(P).sum(axis=1).mean()
        hist.append((it, -res.fun, g.min(), g.max(), len(A)))
        bad = np.argsort(g)[:add]
        bad = bad[g[bad] < -1e-9*scale]
        if len(bad) == 0:
            break
        A = np.vstack([A, P[bad]])
    return hist, scale

for blind in (True, False):
    for t in (1, 2, 5):
        hist, sc = run(t, blind, 3000 if blind else 4000, 40000 if blind else 20000)
        lab = "colour-blind" if blind else "colour-mixing"
        for (it, opt, gmin, gmax, nA) in hist:
            print("%-13s t=%d it=%2d  constraints=%6d  LP optimum=%.3e  fresh pool: min g=%.3e max g=%.3e  [|g| scale %.2e]" % (lab, t, it, nA, opt, gmin, gmax, sc))
        print(flush=True)
