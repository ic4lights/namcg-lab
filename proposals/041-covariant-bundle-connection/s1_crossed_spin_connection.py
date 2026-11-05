"""s1: the Poisson composite connection is the Levi-Civita spin connection with the form index and one frame index crossed.

Definitions (as in proposal 039 s6, Presentation A): omega = Theta^{-1} closed, e^A_mu = eta^{AB} omega_{mu B},
T^A_{mu nu} = d_mu e^A_nu - d_nu e^A_mu,  B_{c|ab} := -T_{c|ab} (frame components of the torsion, first slot = form index).
Claim 1 (exact, any coframe): B_{c|ab} = w_{a|cb} - w_{b|ca}, with w_{a|cb} = e_a^mu eta_{cd} w_mu^d_b the Levi-Civita spin connection
(computed independently from the metric G = e^T eta e).  This is the torsion-free relation de^A = -w^A_B ^ e^B.
Claim 2 (rotation law): under e -> L(x) e, L = exp(eps*lam), lam(0)=0, to first order in eps the inhomogeneous part of B
is  d_B_{c|ab} = d_a lam_{cb} - d_b lam_{ca}  (frame derivatives), whereas a connection would shift by d_c lam_{ab}.
"""
import sys
import numpy as np
sys.path.insert(0, '.')
from tj import Jets, random_class

J = Jets(4, 3); D = 4


def inv_jet(A):
    return J.inv_series(A)


def frame_data(E, etad):
    """E[A,mu,M] coframe jets. Returns T_{c|ab}, w_{c|ab} (levi-civita, frame comps along e_c) at x=0, and G jets."""
    eta = np.diag(etad)
    etaJ = np.zeros((D, D, J.M)); etaJ[:, :, 0] = eta
    Gj = J.matmul(J.matmul(np.transpose(E, (1, 0, 2)), etaJ), E)         # G_{mu nu}
    Ginv0 = np.linalg.inv(Gj[:, :, 0])
    dG = np.stack([J.d(Gj, k)[..., 0] for k in range(D)], axis=2)         # dG[mu,nu,k] = d_k G_{mu nu}
    Gam = np.zeros((D, D, D))                                             # Gam[l,m,n]
    for l in range(D):
        for m in range(D):
            for n in range(D):
                Gam[l, m, n] = 0.5*sum(Ginv0[l, k]*(dG[k, n, m]+dG[k, m, n]-dG[m, n, k]) for k in range(D))
    # inverse coframe Einv[mu, A] = e_A^mu
    Ej = inv_jet(E.copy().transpose(0, 1, 2))      # inverse of matrix E[A,mu] -> [mu,A]
    E0 = E[..., 0]; Ei0 = Ej[..., 0]
    dEi = np.stack([J.d(Ej, k)[..., 0] for k in range(D)], axis=2)        # dEi[mu,A,k] = d_k e_A^mu
    # w_mu^A_B = e^A_nu (d_mu e_B^nu + Gam^nu_{mu l} e_B^l)
    w = np.zeros((D, D, D))                                               # w[mu,A,B]
    for mu in range(D):
        for A in range(D):
            for B in range(D):
                s = 0.0
                for nu in range(D):
                    s += E0[A, nu]*(dEi[nu, B, mu] + sum(Gam[nu, mu, l]*Ei0[l, B] for l in range(D)))
                w[mu, A, B] = s
    wlow = np.einsum('AC,mCB->mAB', eta, w)                               # w_{mu|AB}
    wfr = np.einsum('mAB,mc->cAB', wlow, Ei0)                             # w_{c|AB} = e_c^mu w_{mu|AB}
    # torsion T^A_{mu nu}
    T = np.zeros((D, D, D))
    for A in range(D):
        for m in range(D):
            for n in range(D):
                T[A, m, n] = J.d(E[A, n], m)[0] - J.d(E[A, m], n)[0]
    Tfr = np.einsum('Amn,ma,nb->Aab', T, Ei0, Ei0)                       # T^A_{ab} frame
    Tlow = np.einsum('cA,Aab->cab', eta, Tfr)                             # T_{c|ab}
    return Tlow, wfr, Ei0, E0


def crossed(w):
    return np.einsum('acb->cab', w) - np.einsum('bca->cab', w)           # w_{a|cb} - w_{b|ca}


if __name__ == '__main__':
    print('Claim 1: B_{c|ab} = w_{a|cb} - w_{b|ca}')
    for etad in [(1, 1, 1, 1), (-1, 1, 1, 1)]:
        for seed in (1, 2, 3, 4):
            c = random_class(J, seed, etad)
            etaM = c['eta']; om = c['om']
            E = np.einsum('AB,mBc->Amc', np.linalg.inv(etaM), om)
            Tlow, wfr, Ei0, E0 = frame_data(E, np.array(etad, float))
            B = -Tlow
            P = crossed(wfr)
            print(f"  eta={etad} seed={seed}: |B - cross(w)|/|B| = {np.linalg.norm(B-P)/np.linalg.norm(B):.2e}; "
                  f"|B - w|/|B| = {np.linalg.norm(B-wfr)/np.linalg.norm(B):.2e}")
    print('Claim 1 also for a non-class coframe (random 16-component e):')
    rng = np.random.default_rng(7)
    for etad in [(1, 1, 1, 1), (-1, 1, 1, 1)]:
        E = np.zeros((D, D, J.M))
        E[:, :, 0] = np.eye(D) + 0.3*rng.normal(size=(D, D))
        for i, m in enumerate(J.mons):
            if 1 <= sum(m) <= 3:
                E[:, :, i] = 0.3*rng.normal(size=(D, D))
        Tlow, wfr, Ei0, E0 = frame_data(E, np.array(etad, float))
        B = -Tlow; P = crossed(wfr)
        print(f"  eta={etad}: |B - cross(w)|/|B| = {np.linalg.norm(B-P)/np.linalg.norm(B):.2e}")

    print('Claim 2: inhomogeneous rotation law of B versus that of w (e -> L e, L = 1 + eps lam + eps^2 lam^2/2, lam_{AB}(x) = l_{AB,k} x^k)')
    for etad in [(1, 1, 1, 1), (-1, 1, 1, 1)]:
        eta = np.diag(np.array(etad, float))
        c = random_class(J, 5, etad)
        om = c['om']
        E = np.einsum('AB,mBc->Amc', np.linalg.inv(c['eta']), om)
        rng = np.random.default_rng(11)
        # lam^A_B(x) = eta^{AC} lam_{CB}, lam_{CB} antisymmetric
        l = rng.normal(size=(D, D, D)); l = l - np.transpose(l, (1, 0, 2))      # l[C,B,k]
        lam = np.zeros((D, D, J.M))
        for k in range(D):
            mon = tuple(1 if j == k else 0 for j in range(D))
            lam[:, :, J.idx[mon]] = np.einsum('AC,CB->AB', np.linalg.inv(eta), l[:, :, k])
        res = {}
        for eps in (1e-4, 2e-4):
            Lm = np.zeros((D, D, J.M)); Lm[:, :, 0] = np.eye(D)
            Lm = Lm + eps*lam + 0.5*eps**2*J.matmul(lam, lam)
            Ep = J.matmul(Lm, E)
            T0, w0, Ei, E0 = frame_data(E, np.array(etad, float))
            T1, w1, Ei1, E01 = frame_data(Ep, np.array(etad, float))
            # frame at x=0 is rotated by L(0)=1 so components are directly comparable
            dB = (-(T1) - (-(T0)))/eps
            dw = (w1 - w0)/eps
            Ei0 = Ei
            # frame derivative d_a lam_{cb}: e_a^mu l_{cb,mu}
            dl = np.einsum('cbk,ka->cba', l, Ei0)       # dl[c,b,a] = d_a lam_{cb}
            pred_B = np.zeros((D, D, D))
            for cc in range(D):
                for a in range(D):
                    for b in range(D):
                        pred_B[cc, a, b] = dl[cc, b, a] - dl[cc, a, b]
            # connection law (sign from numerics): dw_{c|ab} = s * d_c lam_{ab}
            pred_w = np.zeros((D, D, D))
            for cc in range(D):
                for a in range(D):
                    for b in range(D):
                        pred_w[cc, a, b] = dl[a, b, cc]
            res[eps] = (dB, dw, pred_B, pred_w)
        dB, dw, pB, pw = res[1e-4]
        for name, num, pr in (('dB vs  (d_a lam_cb - d_b lam_ca)', dB, pB), ('dw vs d_c lam_ab', dw, pw)):
            s = np.sum(num*pr)/np.sum(pr*pr)
            print(f"  eta={etad}: {name}: best sign/scale {s:+.4f}, residual {np.linalg.norm(num - s*pr)/np.linalg.norm(num):.2e}")
        print(f"  eta={etad}: dB vs d_c lam_ab residual (if B were a connection) = "
              f"{min(np.linalg.norm(dB - s*pw)/np.linalg.norm(dB) for s in (1.0, -1.0)):.3f}")
        # also check that dB = cross(dw)
        print(f"  eta={etad}: |dB - cross(dw)|/|dB| = {np.linalg.norm(dB-crossed(dw))/np.linalg.norm(dB):.2e}")
