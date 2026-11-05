"""s15: the matrix background gauge function D_mu a^mu = eta_{mu nu} Theta^{nu rho} d_rho a^mu equals minus the rho-weighted Lorenz gauge function of the Moser one-form A_nu = a^mu omega_{mu nu},
Xi = rho^{-1} d_nu(rho G^{nu lam} A_lam), at random Poisson-class jets and random fields a (jets), both signatures."""
import sys, io, contextlib
import numpy as np
sys.path.insert(0, '.')
with contextlib.redirect_stdout(io.StringIO()):
    import s3_operator_identity as s3
J = s3.J; D = 4
for etad in [(1, 1, 1, 1), (-1, 1, 1, 1)]:
    for seed in (1, 2, 3):
        bg = s3.setup(seed, etad)
        rng = np.random.default_rng(seed)
        a = rng.normal(size=(D, J.M))
        Th, eta, rho, rhoi, K = bg['Th'], bg['eta'], bg['rho'], bg['rhoi'], bg['K']
        Da = np.zeros(J.M)
        for mu in range(D):
            for nu in range(D):
                for r in range(D):
                    Da += eta[mu, nu]*J.mul(Th[nu, r], J.d(a[mu], r))
        A = s3.S_apply(bg, a)
        Xi_in = np.zeros(J.M)
        for nu in range(D):
            for lam in range(D):
                Xi_in += J.d(J.mul(J.mul(rho, K[nu, lam]), A[lam]), nu)
        Xi = J.mul(rhoi, Xi_in)
        n = 10
        print(f'eta={etad} seed={seed}: |Xi + D.a|/|D.a| = {np.linalg.norm(Xi[:n] + Da[:n])/np.linalg.norm(Da[:n]):.1e}   (|Xi - D.a|/|D.a| = {np.linalg.norm(Xi[:n] - Da[:n])/np.linalg.norm(Da[:n]):.2f})')
