"""s8: does the Goldstone-extremised rotation of proposal 039 keep the coframe in the matrix-realisable class?
Class condition: eta_{AB} e^B_mu antisymmetric in (A,mu)  [e = eta^{-1} omega], omega closed.
Plane-wave first order about constant omega_bar:  delta omega = eps*(p_mu a_nu - p_nu a_mu) cos(p.x).  Rotations e -> (1 + eps*lam) e with lam_{AB}(x) = lamhat_{AB} sin(p.x)
(so d_k lam = lamhat p_k at x = 0).  S = totally antisymmetric part of the torsion T_{lam mu nu} of e.
Unknown lamhat (6).  Conditions:  (C1) S + delta S(lamhat) = 0   (Goldstone stationarity of 039: S -> 0),
                                    (C2) (eta e')_{A mu} antisymmetric  <=>  omega_bar eta^{-1} lamhat + lamhat eta^{-1} omega_bar = 0 .
Reports: dimension of the C2 solution space, dimension of the C1 solution space, and whether C1 & C2 are simultaneously solvable.
"""
import sys, io, contextlib, itertools
import numpy as np
sys.path.insert(0, '.')
from tj import Jets
J = Jets(4, 2); D = 4
pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

def S_of(E, eta):
    """axial part of T_{lam mu nu} = eta_AB e^A_lam (d_mu e^B_nu - d_nu e^B_mu) at x=0; E[A,mu,M]"""
    T = np.zeros((D, D, D))
    for l in range(D):
        for m in range(D):
            for n in range(D):
                T[l, m, n] = sum(eta[A, A]*E[A, l, 0]*(J.d(E[A, n], m)[0] - J.d(E[A, m], n)[0]) for A in range(D))
    S = np.zeros((D, D, D))
    for l, m, n in itertools.product(range(D), repeat=3):
        idx = [l, m, n]; s = 0.0
        for p in itertools.permutations(range(3)):
            sign = np.linalg.det(np.eye(3)[list(p)])
            s += sign*T[idx[p[0]], idx[p[1]], idx[p[2]]]
        S[l, m, n] = s/6.0
    return S

def build(etad, seed, eps):
    rng = np.random.default_rng(seed)
    eta = np.diag(np.array(etad, float))
    while True:
        w0 = rng.uniform(-1, 1, (D, D)); w0 = w0 - w0.T
        if abs(np.linalg.det(w0)) > 0.2: break
    p = rng.normal(size=D); a = rng.normal(size=D)
    # delta omega_{mu nu}(x) = eps (p_mu a_nu - p_nu a_mu) cos(p.x) ~ eps*(...)(1 - (p.x)^2/2): first jet zero?  use  sin(p.x) ~ p.x instead (nonzero gradient at 0)
    om = np.zeros((D, D, J.M)); om[:, :, 0] = w0
    for m in range(D):
        for n in range(D):
            for k in range(D):
                mon = tuple(1 if j == k else 0 for j in range(D))
                om[m, n, J.idx[mon]] += eps*(p[m]*a[n] - p[n]*a[m])*p[k]
    return eta, w0, p, a, om

for etad in [(1, 1, 1, 1), (-1, 1, 1, 1)]:
    print('eta', etad)
    for seed in range(1, 7):
        eps = 1e-6
        eta, w0, p, a, om = build(etad, seed, eps)
        E = np.einsum('AB,mBc->Amc', np.linalg.inv(eta), om)
        S0 = S_of(E, eta)/eps
        # delta S(lamhat) by finite difference: e' = (1 + eps2*lam) e with lam_{AB}(x) = lamhat_{AB} (p.x)  (jets)
        cols = []
        for (i, j) in pairs:
            lam = np.zeros((D, D, J.M))
            lamhat = np.zeros((D, D)); lamhat[i, j] = 1.0; lamhat[j, i] = -1.0
            for k in range(D):
                mon = tuple(1 if jj == k else 0 for jj in range(D))
                lam[:, :, J.idx[mon]] = np.linalg.inv(eta) @ lamhat * p[k]
            Lm = np.zeros((D, D, J.M)); Lm[:, :, 0] = np.eye(D); Lm = Lm + eps*lam
            Ep = J.matmul(Lm, E)
            dS = (S_of(Ep, eta) - S_of(E, eta))/eps/eps*1.0      # linear in lam; E itself is O(eps) amplitude: use base e_bar instead
            # use base constant frame to isolate the pure rotation response:
            Eb = np.zeros_like(E); Eb[:, :, 0] = (np.linalg.inv(eta) @ w0)
            Eb_p = J.matmul(Lm, Eb)
            dS = (S_of(Eb_p, eta) - S_of(Eb, eta))/eps
            cols.append(dS.ravel())
        Mmat = np.array(cols).T                      # [64, 6]
        # C1: Mmat x = -S0.ravel()
        x1, res1, rk1, sv1 = np.linalg.lstsq(Mmat, -S0.ravel(), rcond=None)
        r1 = np.linalg.norm(Mmat@x1 + S0.ravel())/np.linalg.norm(S0)
        # C2: omega_bar eta^{-1} lam + lam eta^{-1} omega_bar = 0  (linear in lamhat, 16 comps)
        c2 = []
        for (i, j) in pairs:
            lamhat = np.zeros((D, D)); lamhat[i, j] = 1.0; lamhat[j, i] = -1.0
            c2.append((w0 @ np.linalg.inv(eta) @ lamhat + lamhat @ np.linalg.inv(eta) @ w0).ravel())
        C2 = np.array(c2).T
        sv2 = np.linalg.svd(C2, compute_uv=False)
        null2 = int(np.sum(sv2 < 1e-9)) + (6 - len(sv2))
        # combined
        A = np.vstack([Mmat, 1e3*C2]); bvec = np.concatenate([-S0.ravel(), np.zeros(16)])
        xc, *_ = np.linalg.lstsq(A, bvec, rcond=None)
        rc = np.linalg.norm(Mmat@xc + S0.ravel())/np.linalg.norm(S0); c2res = np.linalg.norm(C2@xc)
        print(f'  seed {seed}: rank(dS map)={rk1}, C1 alone: residual {r1:.1e};  dim ker C2 (in-class rotations) = {null2};  C1 with C2 imposed: residual {rc:.3f} (|C2 x| = {c2res:.1e}), |S|={np.linalg.norm(S0):.3f}')
