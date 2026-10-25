"""Geometry helpers on 3-jets (tj.Jets): scalar curvature at 0, Gilkey data (omega, E) and a_1 of a second-order operator given by applying it to test fields."""
import numpy as np
from tj import Jets
J = Jets(4, 3); D = 4


def christoffel_jets(g):
    """g[m,n,M] lower metric jets -> Gam[l,m,n,M] (valid to jet order 2)"""
    gi = J.inv_series(g)
    dg = np.stack([J.d(g, k) for k in range(D)], axis=2)           # dg[m,n,k,M] = d_k g_mn
    Gam = np.zeros((D, D, D, J.M))
    for l in range(D):
        for m in range(D):
            for n in range(m, D):
                s = np.zeros(J.M)
                for k in range(D):
                    s += J.mul(gi[l, k], dg[k, n, m] + dg[k, m, n] - dg[m, n, k])
                Gam[l, m, n] = 0.5*s; Gam[l, n, m] = 0.5*s
    return Gam, gi


def ricci_scalar_at0(g):
    Gam, gi = christoffel_jets(g)
    # R^l_{m k n} = d_k Gam^l_{n m} - d_n Gam^l_{k m} + Gam^l_{k s} Gam^s_{n m} - Gam^l_{n s} Gam^s_{k m}
    Ric = np.zeros((D, D))
    G0 = Gam[..., 0]
    for m in range(D):
        for n in range(D):
            s = 0.0
            for l in range(D):
                s += J.d(Gam[l, n, m], l)[0] - J.d(Gam[l, l, m], n)[0]
                for sg in range(D):
                    s += G0[l, l, sg]*G0[sg, n, m] - G0[l, n, sg]*G0[sg, l, m]
            Ric[m, n] = s
    return np.einsum('mn,mn->', gi[..., 0], Ric)


def apply_to_jets(apply_op, n):
    """returns coefficient jets: a[s][:,k,M] (so out = -(g^{ij}d d + a^s d_s + b)A) and b[:,k,M]; operator acting on n-component fields"""
    b = np.zeros((n, n, J.M)); a = np.zeros((D, n, n, J.M))
    xs = []
    for s in range(D):
        mon = tuple(1 if j == s else 0 for j in range(D)); v = np.zeros(J.M); v[J.idx[mon]] = 1.0; xs.append(v)
    for k in range(n):
        A = np.zeros((n, J.M)); A[k, 0] = 1.0
        oc = apply_op(A)
        b[:, k] = -oc
        for s in range(D):
            A = np.zeros((n, J.M)); A[k] = xs[s]
            os_ = apply_op(A)
            for l in range(n):
                a[s, l, k] = -os_[l] + J.mul(xs[s], oc[l])
    return a, b


def gilkey_a1(a, b, g, n):
    """O = -(g^{ij} d_i d_j + a^s d_s + b);  returns (tr E_G + R/6) at 0 with E_G = B - g^{ij}(d_i w_j + w_i w_j - w_k Gam^k_ij), w_i = 1/2 g_ik (A^k + g^{pq} Gam^k_pq)"""
    Gam, gi = christoffel_jets(g)
    contr = np.zeros((D, J.M))                       # g^{pq} Gam^k_pq
    for k in range(D):
        for p in range(D):
            for q in range(D):
                contr[k] += J.mul(gi[p, q], Gam[k, p, q])
    w = np.zeros((D, n, n, J.M))
    for i in range(D):
        for kk in range(D):
            for l in range(n):
                for m in range(n):
                    val = a[kk, l, m] + (contr[kk] if l == m else 0.0)
                    w[i, l, m] += 0.5*J.mul(g[i, kk], val)
    E = b.copy()
    for i in range(D):
        for j in range(D):
            gij = gi[i, j]
            dw = np.stack([[J.d(w[j, l, m], i) for m in range(n)] for l in range(n)])      # [l,m,M]
            ww = np.einsum('lmA,mrB,ABC->lrC', w[i], w[j], J.P) if False else np.zeros((n, n, J.M))
            for l in range(n):
                for r in range(n):
                    for m in range(n):
                        ww[l, r] += J.mul(w[i, l, m], w[j, m, r])
            wk = np.zeros((n, n, J.M))
            for kk in range(D):
                wk += np.stack([[J.mul(w[kk, l, m], Gam[kk, i, j]) for m in range(n)] for l in range(n)])
            E = E - np.stack([[J.mul(gij, dw[l, m] + ww[l, m] - wk[l, m]) for m in range(n)] for l in range(n)])
    trE = sum(E[l, l, 0] for l in range(n))
    return trE + n*ricci_scalar_at0(g)/6.0, trE
