"""s14: relation between the two forms of the tree-level equation at the point: Jlow_nu = Theta^{rho mu} d_rho Theta_{mu nu} (Theta_{mu nu} = eta eta Theta, as in s3b)
and Vup^nu = rho^{-1} d_mu (rho G^{mu nu}) (= box_G x^nu - G^{mu nu} d_mu ln rho).  Test  Vup = c * Theta^{nu lam} eta... : fit a 4x4 matrix N(0) from random jets? (N must be a fixed natural matrix)."""
import sys, io, contextlib
import numpy as np
sys.path.insert(0, '.')
with contextlib.redirect_stdout(io.StringIO()):
    import s3_operator_identity as s3
J = s3.J; D = 4
for etad in [(1, 1, 1, 1), (-1, 1, 1, 1)]:
    for seed in (1, 2, 3):
        bg = s3.setup(seed, etad)
        rho, K, rhoi, Th, eta = bg['rho'], bg['K'], bg['rhoi'], bg['Th'], bg['eta']
        V = np.zeros(D)
        for s in range(D):
            t = np.zeros(J.M)
            for m in range(D): t += J.d(J.mul(rho, K[m, s]), m)
            V[s] = J.mul(rhoi, t)[0]
        Jl = s3.Jvec(bg)[:, 0]
        T0 = Th[..., 0]
        cands = {'eta^-1 Jl': np.linalg.inv(eta) @ Jl, 'Theta eta Jl': T0 @ eta @ Jl, 'Theta Jl': T0 @ Jl, 'Jl': Jl, 'K Jl': K[..., 0] @ Jl,
                 'Theta eta Theta^T eta Jl': T0 @ eta @ T0.T @ eta @ Jl, 'omega-based': np.linalg.inv(T0) @ Jl}
        out = []
        for k, c in cands.items():
            s = (V @ c)/(c @ c)
            out.append(f'{k}: res {np.linalg.norm(V - s*c)/np.linalg.norm(V):.1e}')
        print(etad, seed, '; '.join(out))
