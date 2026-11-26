"""s1: local frame rotations e^A -> Lambda^A_B(x) e^B and first-order frame densities.

Family: sqrt|G| ( a1 T_{lmn}T^{lmn} + a2 T_{lmn}T^{mln} + a3 V.V + a4 V.W + a5 W.W ),
T_{lmn} = eta_AB e^A_l (d_m e^B_n - d_n e^B_m), V_m = G^{ln} T_{lmn}, W_m = d_m ln rho, rho^2 = |det e|.

Part A. delta e^A = lam^A_B e^B gives, with ell_{m|ln} := (d_m lam_AB) e^A_l e^B_n,
        delta T_{lmn} = ell_{m|ln} - ell_{n|lm},  delta V_m = - G^{ls} ell_{s|lm},  delta W = 0
        (the homogeneous part cancels in every scalar). Hence delta(sqrtG L) = sqrtG P^{m|ln} ell_{m|ln}, with
        P^{m|ln} = 2 a1 (T^{lmn} - T^{nml}) + a2 [ (T^{mln} - T^{nlm}) - (T^{mnl} - T^{lnm}) ]
                   - a3 (G^{ml} V^n - G^{mn} V^l) - (a4/2)(G^{ml} W^n - G^{mn} W^l)
        (antisymmetrised in l,n). The formula is checked against a finite variation of L.
Part B. Invariance mod total derivative <=> d_m( sqrtG P^{m|ln} e^A_l e^B_n ) = 0 identically in e.
        The linear map (a1..a5) -> divergence is evaluated at random 2-jets; its null space is computed.
"""
import sys
import numpy as np
sys.path.insert(0, '.')
from tj import Jets


def frame_jets(J, D, seed, amp=0.35):
    rng = np.random.default_rng(seed)
    E = np.zeros((D, D, J.M))
    E[:, :, 0] = np.eye(D) + 0.3*rng.normal(size=(D, D))
    for A in range(D):
        for m in range(D):
            for i, mon in enumerate(J.mons):
                if 1 <= sum(mon) <= J.ORD:
                    E[A, m, i] = amp*rng.normal()
    return E


def sqrtG_jets(J, E, D):
    E0 = E[:, :, 0]
    det0 = abs(np.linalg.det(E0))
    E0i = np.linalg.inv(E0)
    dE = E.copy(); dE[:, :, 0] = 0
    Em = np.zeros((D, D, J.M)); Em[:, :, 0] = E0i
    X = J.matmul(Em, dE)
    lg = np.zeros(J.M); Xp = X.copy()
    for k in range(1, J.ORD+1):
        lg += ((-1)**(k+1)/k)*sum(Xp[i, i] for i in range(D))
        Xp = J.matmul(Xp, X)
    res = J.const(1.0); term = J.const(1.0)
    for k in range(1, J.ORD+1):
        term = J.mul(term, lg)/k
        res = res + term
    return det0*res


def geometry(J, E, eta, D):
    etaJ = np.zeros((D, D, J.M)); etaJ[:, :, 0] = eta
    etaiJ = np.zeros((D, D, J.M)); etaiJ[:, :, 0] = np.linalg.inv(eta)
    Einv = J.inv_series(E)
    Gi = J.matmul(J.matmul(Einv, etaiJ), np.transpose(Einv, (1, 0, 2)))
    TA = np.zeros((D, D, D, J.M))
    for A in range(D):
        for m in range(D):
            for n in range(D):
                TA[A, m, n] = J.d(E[A, n], m) - J.d(E[A, m], n)
    Tl = np.zeros((D, D, D, J.M))
    for l in range(D):
        for m in range(D):
            for n in range(D):
                Tl[l, m, n] = sum(eta[A, A]*J.mul(E[A, l], TA[A, m, n]) for A in range(D))
    sg = sqrtG_jets(J, E, D)
    W = np.zeros((D, J.M))
    for k in range(D):
        dEk = np.stack([J.d(E[A], k) for A in range(D)], axis=0)
        W[k] = 0.5*sum(J.mul(Einv[l, A], dEk[A, l]) for A in range(D) for l in range(D))
    return dict(Gi=Gi, Tl=Tl, sg=sg, W=W, E=E)


def uptensors(J, g, D):
    Gi = g['Gi']; Tl = g['Tl']; W = g['W']

    def raise1(T, pos):
        out = np.zeros_like(T)
        for l in range(D):
            for m in range(D):
                for n in range(D):
                    if pos == 0:
                        out[l, m, n] = sum(J.mul(Gi[l, a], T[a, m, n]) for a in range(D))
                    elif pos == 1:
                        out[l, m, n] = sum(J.mul(Gi[m, a], T[l, a, n]) for a in range(D))
                    else:
                        out[l, m, n] = sum(J.mul(Gi[n, a], T[l, m, a]) for a in range(D))
        return out
    Tu = raise1(raise1(raise1(Tl, 0), 1), 2)
    V = np.zeros((D, J.M))
    for m in range(D):
        V[m] = sum(J.mul(Gi[l, n], Tl[l, m, n]) for l in range(D) for n in range(D))
    Vu = np.stack([sum(J.mul(Gi[m, a], V[a]) for a in range(D)) for m in range(D)])
    Wu = np.stack([sum(J.mul(Gi[m, a], W[a]) for a in range(D)) for m in range(D)])
    return Tu, V, Vu, Wu


def scalars(J, g, D):
    Tu, V, Vu, Wu = uptensors(J, g, D)
    Tl = g['Tl']
    TT = sum(J.mul(Tl[l, m, n], Tu[l, m, n]) for l in range(D) for m in range(D) for n in range(D))
    TTp = sum(J.mul(Tl[l, m, n], Tu[m, l, n]) for l in range(D) for m in range(D) for n in range(D))
    V2 = sum(J.mul(V[m], Vu[m]) for m in range(D))
    VW = sum(J.mul(V[m], Wu[m]) for m in range(D))
    W2 = sum(J.mul(g['W'][m], Wu[m]) for m in range(D))
    return np.array([TT, TTp, V2, VW, W2])


def superpotential(J, g, D, alpha):
    """sqrtG * P^{m|[ln]} e^A_l e^B_n as jets, indices [m, A, B]; P^{m|ln} is antisymmetrised in (l,n)."""
    Tu, V, Vu, Wu = uptensors(J, g, D)
    a1, a2, a3, a4, a5 = alpha
    Gi = g['Gi']
    P = np.zeros((D, D, D, J.M))
    for m in range(D):
        for l in range(D):
            for n in range(D):
                t1 = 2*a1*(Tu[l, m, n] - Tu[n, m, l])
                t2 = a2*((Tu[m, l, n] - Tu[n, l, m]) - (Tu[m, n, l] - Tu[l, n, m]))
                t3 = -a3*(J.mul(Gi[m, l], Vu[n]) - J.mul(Gi[m, n], Vu[l]))
                t4 = -0.5*a4*(J.mul(Gi[m, l], Wu[n]) - J.mul(Gi[m, n], Wu[l]))
                P[m, l, n] = t1 + t2 + t3 + t4
    E = g['E']
    Q = np.zeros((D, D, D, J.M))
    for m in range(D):
        for A in range(D):
            for B in range(D):
                acc = np.zeros(J.M)
                for l in range(D):
                    for n in range(D):
                        acc += J.mul(J.mul(P[m, l, n], E[A, l]), E[B, n])
                Q[m, A, B] = J.mul(g['sg'], acc)
    return Q


def divergence_at0(J, Q, D):
    out = np.zeros((D, D))
    for A in range(D):
        for B in range(D):
            out[A, B] = sum(J.d(Q[m, A, B], m)[0] for m in range(D))
    return out


def L_value(J, g, D, alpha):
    return g['sg'][0]*np.dot(alpha, scalars(J, g, D)[:, 0])


def check_variation(D, eta, seed, alpha):
    J = Jets(D, 2)
    E = frame_jets(J, D, seed)
    rng = np.random.default_rng(seed+100)
    lam0 = rng.normal(size=(D, D)); lam0 = lam0 - lam0.T
    lam1 = rng.normal(size=(D, D, D)); lam1 = lam1 - np.transpose(lam1, (1, 0, 2))
    etai = np.linalg.inv(eta)

    def rotated(eps):
        lamA = np.zeros((D, D, J.M))
        lamA[:, :, 0] = etai @ lam0
        for m in range(D):
            lamA[:, :, J.idx[tuple(1 if i == m else 0 for i in range(D))]] = etai @ lam1[:, :, m]
        return E + eps*J.matmul(lamA, E)
    h = 1e-5
    vals = []
    for s in (+1, -1):
        g = geometry(J, rotated(s*h), eta, D)
        vals.append(L_value(J, g, D, alpha))
    num = (vals[0]-vals[1])/(2*h)
    g = geometry(J, E, eta, D)
    Q = superpotential(J, g, D, alpha)
    pred = sum(Q[m, A, B, 0]*lam1[A, B, m] for m in range(D) for A in range(D) for B in range(D))
    return num, pred


if __name__ == "__main__":
    for D, eta_d in [(3, (1, 1, 1)), (3, (-1, 1, 1)), (4, (1, 1, 1, 1)), (4, (-1, 1, 1, 1))]:
        eta = np.diag(np.array(eta_d, float))
        alpha = np.array([0.7, -0.4, 0.9, 0.3, -0.5])
        num, pred = check_variation(D, eta, 7, alpha)
        print(f"d={D} eta={eta_d}: delta(sqrtG L)/eps numeric {num:.10f}  vs P.ell {pred:.10f}  diff {abs(num-pred):.2e}")
        J = Jets(D, 2)
        rows = []
        for seed in range(1, 4):
            E = frame_jets(J, D, seed)
            g = geometry(J, E, eta, D)
            cols = []
            for k in range(5):
                al = np.zeros(5); al[k] = 1.0
                Q = superpotential(J, g, D, al)
                dv = divergence_at0(J, Q, D)
                cols.append([dv[A, B] for A in range(D) for B in range(A+1, D)])
            rows.append(np.array(cols).T)
        M = np.vstack(rows)
        U, S, Vt = np.linalg.svd(M)
        print("  singular values:", np.round(S, 8))
        null = Vt[np.sum(S > 1e-9):]
        print("  null space dimension:", null.shape[0])
        Nvec = np.array([0.25, 0.5, -1, 0, 0]); W2vec = np.array([0, 0, 0, 0, 1.0])
        B = np.array([Nvec, W2vec]).T
        res = np.linalg.norm(null.T - B @ np.linalg.lstsq(B, null.T, rcond=None)[0])
        print("  residual of null space against span{N, W^2}:", f"{res:.2e}")
        print("  |violation| of X=T^2 alone:", f"{np.linalg.norm(M@np.array([1, 0, 0, 0, 0.])):.4f}",
              "| of N:", f"{np.linalg.norm(M@Nvec):.2e}", "| of W^2:", f"{np.linalg.norm(M@W2vec):.2e}")
