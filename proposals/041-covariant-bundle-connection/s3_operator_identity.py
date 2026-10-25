"""s3: operator-level comparison of the matrix vector operator O_v (a^mu variables, Feynman background gauge, alpha = 1) with the covariant
Maxwell (metric G, weight rho) + axion operator in the Moser variables A_nu = a^mu omega_{mu nu}.

Background: Poisson class omega = Theta^{-1} closed, random 3-jets (tj.py).  Operators are compared through the coefficients of
   O = -( G^{st} d_s d_t + a^s d_s + b )   (acting on the column vector of components, at x = 0)
extracted by applying the operator to test polynomials.  Two operators:
  (V) S O_v S^{-1},  (S a)_nu = a^mu omega_{mu nu},  O_v a^m = O_s a^m - 2 eta^{m a} Theta^{r s} d_r Theta_{a n} d_s a^n,  O_s f = -rho^{-1} d_m(rho K^{mn} d_n f)
  (M) (kappa rho)^{-1} G_{lam nu} P^nu with P^nu = -d_mu FF^{mu nu} - c rho G^{nu lam} d_lam Xi,  Xi = rho^{-1} d_nu(rho G^{nu lam} A_lam),
      FF = H F,  H = 2*Maxwell_G + b*Axion,  b = -sgn(Pf Theta) I1/8   (s2),  c fixed by Feynman symbol.
Reports |a_V - a_M|, |b_V - b_M| together with the size of J_nu = Theta^{rho mu} d_rho Theta_{mu nu} (D^mu Theta_{mu nu}) and of its derivative.
"""
import sys
import numpy as np
sys.path.insert(0, '.')
from tj import Jets, random_class
from s2_constitutive_tensor import pairs, omega_from6   # noqa  (prints nothing important)

J = Jets(4, 3); D = 4


def scal_inv(f):
    A = np.zeros((1, 1, J.M)); A[0, 0] = f
    return J.inv_series(A)[0, 0]


def setup(seed, etad, amp=0.4):
    c = random_class(J, seed, etad, amp=amp)
    eta = c['eta']; om = c['om']; Th = c['Th']
    etaJ = np.zeros((D, D, J.M)); etaJ[:, :, 0] = eta
    Pf = J.mul(om[0, 1], om[2, 3]) - J.mul(om[0, 2], om[1, 3]) + J.mul(om[0, 3], om[1, 2])
    sg = np.sign(Pf[0])
    rho = sg*Pf
    rhoi = scal_inv(rho)
    # K^{mu nu} = eta_ab Th^{a mu} Th^{b nu}
    K = J.matmul(J.matmul(np.transpose(Th, (1, 0, 2)), etaJ), Th)
    G = J.inv_series(K)                                   # G_{mu nu}
    return dict(eta=eta, etaJ=etaJ, om=om, Th=Th, rho=rho, rhoi=rhoi, K=K, G=G, sg=sg, Pf=Pf)


def Jvec(bg):
    """J_nu = Theta^{rho mu} d_rho Theta_{mu nu}, Theta_{mu nu} = eta_{ma} eta_{nb} Theta^{ab}  (jets)"""
    Th, eta = bg['Th'], bg['eta']
    Tlow = np.einsum('ma,nb,abM->mnM', eta, eta, Th)
    out = np.zeros((D, J.M))
    for nu in range(D):
        for rr in range(D):
            for mu in range(D):
                out[nu] += J.mul(Th[rr, mu], J.d(Tlow[mu, nu], rr))
    return out


def Ov_apply(bg, a):
    """a: [mu, M] jets -> (O_v a)^mu jets"""
    Th, eta, rho, rhoi, K = bg['Th'], bg['eta'], bg['rho'], bg['rhoi'], bg['K']
    out = np.zeros_like(a)
    for m in range(D):
        s = np.zeros(J.M)
        for mm in range(D):
            for n in range(D):
                s += J.d(J.mul(J.mul(rho, K[mm, n]), J.d(a[m], n)), mm)
        out[m] = -J.mul(rhoi, s)
    Tlow = np.einsum('ma,nb,abM->mnM', eta, eta, Th)
    for m in range(D):
        for al in range(D):
            for n in range(D):
                for r in range(D):
                    for s_ in range(D):
                        # -2 eta^{m al} Th^{r s} d_r Th_{al n} d_s a^n
                        out[m] += -2*eta[m, al]*J.mul(J.mul(Th[r, s_], J.d(Tlow[al, n], r)), J.d(a[n], s_))
    return out


def S_apply(bg, a):          # A_nu = a^mu omega_{mu nu}
    om = bg['om']
    A = np.zeros_like(a)
    for nu in range(D):
        for mu in range(D):
            A[nu] += J.mul(a[mu], om[mu, nu])
    return A


def Sinv_apply(bg, A):       # a^l = A_nu Theta^{nu l}
    Th = bg['Th']
    a = np.zeros_like(A)
    for l in range(D):
        for nu in range(D):
            a[l] += J.mul(A[nu], Th[nu, l])
    return a


def H_jets(bg):
    """H[I,J,M] = 2 Maxwell_G + b Axion  with jets (pairs basis)"""
    K, rho, Th, eta, sg = bg['K'], bg['rho'], bg['Th'], bg['eta'], bg['sg']
    # I1 = eta_ac eta_bd Th^{ab} Th^{cd}
    I1 = np.zeros(J.M)
    for a in range(D):
        for b in range(D):
            for c_ in range(D):
                for d in range(D):
                    co = eta[a, c_]*eta[b, d]
                    if co != 0:
                        I1 += co*J.mul(Th[a, b], Th[c_, d])
    PfTh = Th[0, 1]*0
    PfTh = J.mul(Th[0, 1], Th[2, 3]) - J.mul(Th[0, 2], Th[1, 3]) + J.mul(Th[0, 3], Th[1, 2])
    sgT = np.sign(PfTh[0])
    bjet = -sgT*I1/8.0
    H = np.zeros((6, 6, J.M))
    for I, (a, b) in enumerate(pairs):
        for Jx, (c_, d) in enumerate(pairs):
            # s2.maxwell_G = 2*rho*(K K - K K); H = 2*Mx -> 4*rho*(KK-KK)
            H[I, Jx] = 4*J.mul(rho, J.mul(K[a, c_], K[b, d]) - J.mul(K[a, d], K[b, c_]))
            if len({a, b, c_, d}) == 4:
                perm = [a, b, c_, d]
                sign = np.linalg.det(np.eye(4)[perm])
                H[I, Jx] += 8*sign*bjet
    return H, bjet


def P_apply(bg, H, c, A):
    """P^nu[A] jets, A: [lam, M] lower-index components"""
    G, K, rho, rhoi = bg['G'], bg['K'], bg['rho'], bg['rhoi']
    F = np.zeros((6, J.M))
    for I, (m, n) in enumerate(pairs):
        F[I] = J.d(A[n], m) - J.d(A[m], n)
    HF = np.einsum('IJa,Jb,abc->Ic', H, F, J.P, optimize=True)
    FF = np.zeros((D, D, J.M))
    for I, (m, n) in enumerate(pairs):
        FF[m, n] = HF[I]; FF[n, m] = -HF[I]
    P = np.zeros((D, J.M))
    for nu in range(D):
        for mu in range(D):
            P[nu] += -J.d(FF[mu, nu], mu)
    # gauge fixing
    Xi_in = np.zeros(J.M)
    for nu in range(D):
        for lam in range(D):
            Xi_in += J.d(J.mul(J.mul(rho, K[nu, lam]), A[lam]), nu)
    Xi = J.mul(rhoi, Xi_in)
    for nu in range(D):
        for lam in range(D):
            P[nu] += -c*J.mul(J.mul(rho, K[nu, lam]), J.d(Xi, lam))
    return P


def extract(apply_op):
    """returns C[s,t,l,k] (symmetric in s,t), a1[s,l,k], b[l,k] with  out = -(C^{st} d_s d_t + a^s d_s + b) A  at 0, A = e_k * monomial"""
    b = np.zeros((D, D)); a1 = np.zeros((D, D, D)); C = np.zeros((D, D, D, D))
    for k in range(D):
        A = np.zeros((D, J.M)); A[k, 0] = 1.0
        b[:, k] = -apply_op(A)[:, 0]
        for s in range(D):
            A = np.zeros((D, J.M)); mon = tuple(1 if j == s else 0 for j in range(D)); A[k, J.idx[mon]] = 1.0
            a1[s, :, k] = -apply_op(A)[:, 0]
        for s in range(D):
            for t in range(s, D):
                A = np.zeros((D, J.M)); mon = [0]*D; mon[s] += 1; mon[t] += 1
                A[k, J.idx[tuple(mon)]] = 1.0
                out = -apply_op(A)[:, 0]          # = 2 C^{st} (s != t) or 2 C^{ss}
                C[s, t, :, k] = out/2.0; C[t, s, :, k] = out/2.0
    return C, a1, b


def symbol(C, q):
    return np.einsum('s,t,stlk->lk', q, q, C)


if __name__ == '__main__':
    q = np.array([0.3, -0.5, 0.7, 0.2])
    for etad in [(1, 1, 1, 1), (-1, 1, 1, 1)]:
        for seed in (1, 2):
            bg = setup(seed, etad)
            H, bjet = H_jets(bg)
            Jv = Jvec(bg)
            dJ = np.array([[J.d(Jv[nu], k)[0] for k in range(D)] for nu in range(D)])
            print(f'eta={etad} seed={seed}:  |J(0)|={np.linalg.norm(Jv[:, 0]):.3f}  |dJ(0)|={np.linalg.norm(dJ):.3f}')
            Kz = bg['K'][..., 0]; Gz = bg['G'][..., 0]; rho0 = bg['rho'][0]
            qG2 = q @ Kz @ q
            opV = lambda A: S_apply(bg, Ov_apply(bg, Sinv_apply(bg, A)))
            CV, aV, bV = extract(opV)
            print(f'   (V) principal symbol - q_G^2 1 : {np.linalg.norm(symbol(CV, q) - qG2*np.eye(D)):.2e}')
            def make_opM(c, kappa):
                def op(A):
                    P = P_apply(bg, H, c, A)
                    out = np.zeros_like(P)
                    for lam in range(D):
                        for nu in range(D):
                            out[lam] += J.mul(J.mul(bg['G'][lam, nu], bg['rhoi']), P[nu])/kappa
                    return out
                return op
            C0, a0, b0 = extract(make_opM(0.0, 1.0))
            M0 = symbol(C0, q)
            kap = np.trace(M0)/(3*qG2)
            Gq = Gz @ q
            print(f'   (M) Maxwell symbol: kappa={kap:.6f}; transversality |M0 Gq| = {np.linalg.norm(M0@Gq):.1e}; '
                  f'|M0 - kap (q2 1 - Gq q^T)| = {np.linalg.norm(M0 - kap*(qG2*np.eye(D) - np.outer(Gq, q))):.2e}')
            best = None
            for cs in np.linspace(0.25, 4.0, 16):
                CM, aM, bM = extract(make_opM(kap*cs*rho0*0 + kap*cs, kap))
                err = np.linalg.norm(symbol(CM, q) - qG2*np.eye(D))
                if best is None or err < best[0]:
                    best = (err, cs, CM, aM, bM)
            err, cs, CM, aM, bM = best
            print(f'   (M) Feynman symbol at c = kappa*{cs:.3f}: |symbol - q_G^2 1| = {err:.2e}')
            print(f'   principal : |C_V - C_M| = {np.linalg.norm(CV-CM):.2e}')
            print(f'   first-order  : |a_V - a_M|/|a_V| = {np.linalg.norm(aV-aM)/np.linalg.norm(aV):.3e}   (|a_V|={np.linalg.norm(aV):.3f})')
            print(f'   zeroth-order : |b_V - b_M|/|b_V| = {np.linalg.norm(bV-bM)/np.linalg.norm(bV):.3e}   (|b_V|={np.linalg.norm(bV):.3f})')
