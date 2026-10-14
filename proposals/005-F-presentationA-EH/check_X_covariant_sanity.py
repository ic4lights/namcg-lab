"""
Sanity checks of check_X_covariant_rewrite.py machinery.
(1) quadratic order: generalized eigenvalues of <rho R>^(2) relative to <rho^2 X>^(2) on the 3-dim quotient by
    u ~ q = Thbar p must be (-1/4,-1/4,-3/4) (X has eigenvalues 1,1,1 relative to M, proposal r1).
(2) fixed (alpha,beta)=(-4,-4) from the quadratic fit: relative cubic residual of X - alpha*h - beta*r.
"""
import numpy as np, importlib.util, sys
spec = importlib.util.spec_from_file_location('cr', 'check_X_covariant_rewrite.py')
cr = importlib.util.module_from_spec(spec); spec.loader.exec_module(cr)
rng = np.random.default_rng(7)
for sig in (1.0, -1.0):
    ab = np.array([1.0, 2.0]); p = np.array([1., 2., -1., 1.])
    Bh = np.zeros((4, 4), complex); Bx = np.zeros((4, 4), complex); Br = np.zeros((4, 4), complex)
    for i in range(4):
        for j in range(4):
            ui = np.eye(4)[i]; uj = np.eye(4)[j]
            o = cr.run(sig, ab, [p, -p], [ui, uj], [3])
            Bh[i, j] = o['h'][3]; Bx[i, j] = o['x'][3]; Br[i, j] = o['r'][3]
    Bh = (Bh + Bh.T)/2; Bx = (Bx + Bx.T)/2; Br = (Br + Br.T)/2
    omb = np.zeros((4, 4)); omb[0, 1] = ab[0]; omb[1, 0] = -ab[0]; omb[2, 3] = ab[1]; omb[3, 2] = -ab[1]
    q = np.linalg.inv(omb) @ p
    # quotient basis: complement of q
    Q, _ = np.linalg.qr(np.column_stack([q, rng.normal(size=(4, 3))]))
    V = Q[:, 1:]
    h = V.T @ Bh @ V; x = V.T @ Bx @ V; r = V.T @ Br @ V
    print('sig', sig, ' |Bh q|', np.linalg.norm(Bh @ q), ' |Bx q|', np.linalg.norm(Bx @ q))
    print('  eigvals of x^-1 h (expect -1/4,-1/4,-3/4):', np.sort(np.linalg.eigvals(np.linalg.solve(x, h)).real))
    print('  eigvals of x^-1 r :', np.sort(np.linalg.eigvals(np.linalg.solve(x, r)).real), ' (third eigenvalue 1/2: 1 = (-4)(-3/4) + beta/2 gives beta = -4)')
rows = []
for s in range(40):
    sig = rng.choice([1.0, -1.0]); ab = rng.uniform(0.5, 2.5, 2)
    p1 = rng.integers(-3, 4, 4).astype(float); p2 = rng.integers(-3, 4, 4).astype(float)
    us = [rng.normal(size=4) for _ in range(3)]
    o = cr.run(sig, ab, [p1, p2, -p1-p2], us, [7])
    rows.append(o['x'][7] - (-4)*o['h'][7] - (-4)*o['r'][7])
    rows.append(o['x'][7])
res = np.array(rows[0::2]); xs = np.array(rows[1::2])
print('fixed (-4,-4): cubic |X - alpha h - beta r| / |X| =', np.linalg.norm(res)/np.linalg.norm(xs))
