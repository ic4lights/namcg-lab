"""s6: the bundle connection of the Poisson-limit vector operator is the torsion 1-form, not a Lorentz connection.

O_v a^m = O_s a^m - 2 eta^{m a} {Theta_{a n}, a^n},  {Theta_{an}, a^n} = B^s_{an} d_s a^n,  B^s_{an} = Theta^{r s} d_r Theta_{an},  Theta_{an} = eta_{am} eta_{nb} Theta^{mb}.
Lower s with G.  Claim tested at random Theta-class 2-jets (omega = dA, e^A_mu = eta^{AB} omega_{mu B}), both signatures:
    B_{s|an} = - T_{s m n'} e_a^m e_n^{n'}      (T_{lmn} = eta_AB e^A_l (d_m e^B_n - d_n e^B_m)),
i.e. B_s^{AB} is the frame-component torsion with its form index s, a tensor-like object whose inhomogeneous rotation law
(delta T_{lmn} = ell_{m|ln} - ell_{n|lm}, s1) is not the connection law  delta B_s = d_s lambda.  Residual of the identity is printed.
"""
import sys
import numpy as np
sys.path.insert(0, '.')
from tj import Jets, random_class

J = Jets(4, 3); D = 4
for eta_d in [(1, 1, 1, 1), (-1, 1, 1, 1)]:
    for seed in (1, 2, 3):
        c = random_class(J, seed, eta_d)
        eta = c['eta']; om = c['om']; Th = c['Th']; etai = np.linalg.inv(eta)
        etaJ = np.zeros((D, D, J.M)); etaJ[:, :, 0] = eta
        E = np.einsum('AB,mBc->Amc', etai, om)
        Einv = -J.matmul(Th, etaJ)
        G = J.matmul(J.matmul(np.transpose(E, (1, 0, 2)), etaJ), E)
        Tlow = np.einsum('am,mbc,nb->anc', eta, Th, eta)                       # Theta_{a n}
        dT = np.stack([J.d(Tlow, k) for k in range(D)], axis=2)                # d_k Theta_{an}  [a,n,k,M]
        Bup = np.zeros((D, D, D))                                              # B^s_{an} at x=0
        for s in range(D):
            for a in range(D):
                for n in range(D):
                    Bup[s, a, n] = sum(J.mul(Th[r, s], dT[a, n, r])[0] for r in range(D))
        G0 = G[:, :, 0]
        Blow = np.einsum('st,tan->san', G0, Bup)
        TA = np.zeros((D, D, D, J.M))
        for A in range(D):
            for m in range(D):
                for n in range(D):
                    TA[A, m, n] = J.d(E[A, n], m) - J.d(E[A, m], n)
        T0 = np.einsum('A,Al,Amn->lmn', np.diag(eta), E[:, :, 0], TA[..., 0])
        Ei0 = Einv[..., 0]                                                      # e_A^lam  [lam, A]
        pred = -np.einsum('smn,ma,nb->sab', T0, Ei0, Ei0)
        print(f"eta={eta_d} seed={seed}: |B_s,an + T_s,mn e_a^m e_n^n|/|B| = {np.linalg.norm(Blow-pred)/np.linalg.norm(Blow):.2e};  tr B_s = {np.abs(np.einsum('san->s', np.einsum('san,an->san', Blow, np.ones((D, D))*0+np.eye(D)))).max():.1e}")
