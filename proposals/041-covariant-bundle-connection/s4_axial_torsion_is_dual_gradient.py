"""s4: is the axial torsion S = T_[lam mu nu] of the Theta-built coframe the Hodge dual of a gradient of a Lorentz-scalar function of Theta?
Candidate: pseudo-scalar theta~ = rho*b, b = -sgn(Pf Theta) I1/8 (axion coefficient of s2), I1 = eta eta Theta Theta.
Test at random Poisson-class 3-jets (both signatures): S_{lam mu nu} vs  eps_{lam mu nu sigma} G^{sigma kappa} d_kappa f(theta~) for f in {identity, ln, ...}:
report the best-fit proportionality constant and residual for S_{lam mu nu} = k(x) * sqrt|G| [lam mu nu sigma] G^{sigma kappa} d_kappa theta~.
"""
import sys, io, contextlib
import numpy as np
sys.path.insert(0, '.')
with contextlib.redirect_stdout(io.StringIO()):
    import s3_operator_identity as s3
J = s3.J; D = 4

def levi(l, m, n, s):
    perm = [l, m, n, s]
    if len(set(perm)) < 4: return 0.0
    return float(np.linalg.det(np.eye(4)[perm]))

def theta_tilde(bg):
    Th, eta, rho = bg['Th'], bg['eta'], bg['rho']
    I1 = np.zeros(J.M)
    for a in range(D):
        for b in range(D):
            for c in range(D):
                for d in range(D):
                    co = eta[a, c]*eta[b, d]
                    if co != 0: I1 += co*J.mul(Th[a, b], Th[c, d])
    PfTh = J.mul(Th[0, 1], Th[2, 3]) - J.mul(Th[0, 2], Th[1, 3]) + J.mul(Th[0, 3], Th[1, 2])
    b = -np.sign(PfTh[0])*I1/8.0
    return J.mul(rho, b), I1, b

for etad in [(1, 1, 1, 1), (-1, 1, 1, 1)]:
    print('eta', etad)
    for seed in range(1, 7):
        bg = s3.setup(seed, etad)
        eta = bg['eta']; om = bg['om']
        E = np.einsum('AB,mBc->Amc', np.linalg.inv(eta), om)
        # T_{lam mu nu} at 0
        T = np.zeros((D, D, D))
        for l in range(D):
            for m in range(D):
                for n in range(D):
                    T[l, m, n] = sum(eta[A, A]*E[A, l, 0]*(J.d(E[A, n], m)[0] - J.d(E[A, m], n)[0]) for A in range(D))
        S = np.zeros((D, D, D))
        import itertools
        for l, m, n in itertools.product(range(D), repeat=3):
            S[l, m, n] = sum(np.linalg.det(np.eye(3)[list(p)])*T[[l, m, n][p[0]], [l, m, n][p[1]], [l, m, n][p[2]]] for p in itertools.permutations(range(3)))/6.0
        tt, I1, b = theta_tilde(bg)
        dtt = np.array([J.d(tt, k)[0] for k in range(D)])
        Gz = bg['G'][..., 0]; Kz = bg['K'][..., 0]
        sqrtG = np.sqrt(abs(np.linalg.det(Gz)))
        dual = np.zeros((D, D, D))
        for l, m, n in itertools.product(range(D), repeat=3):
            dual[l, m, n] = sum(levi(l, m, n, s)*sqrtG*(Kz[s] @ dtt) for s in range(D))
        k = np.sum(S*dual)/np.sum(dual*dual)
        res = np.linalg.norm(S - k*dual)/np.linalg.norm(S)
        print(f'  seed {seed}: |S|={np.linalg.norm(S):.4f}  best k={k:+.5f}  residual |S - k *d theta~|/|S| = {res:.2e}   theta~={tt[0]:+.4f} rho={bg["rho"][0]:.4f}')
