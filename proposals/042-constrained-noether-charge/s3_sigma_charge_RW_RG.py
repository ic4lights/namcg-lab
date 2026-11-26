"""s3: Sigma charge densities of sqrt(G) R_G and sqrt(G) R_W.

For L = sqrt(G) l(R^a_{b mu nu}[Gamma]) with Gamma a torsion-free connection, the Noether charge on
Sigma (where xi = 0) is Q^{mu nu} = 2 P_a^{b mu nu} B^a_b with P = dL/dR^a_{b mu nu} (antisymmetrised
in mu nu) and B^a_b = d_b xi^a, the same for every connection because xi = 0 there.
  R_G : P_a^{b mu nu} = sqrt(G) (delta^mu_a G^{b nu} - delta^nu_a G^{b mu}) / 2
  R_W = G^{s nu} (e^-1)^mu_a R(gamma)^a_{b mu nu} e^b_s :  P_a^{b mu nu} = sqrt(G) (M - M^T_{mu nu}) / 2,
        M_a^{b mu nu} = G^{s nu} (e^-1)^mu_a e^b_s.
Contracted with B: q_G = sqrt(G) antisym(B G^-1), q_W = sqrt(G) antisym(e^-1 B e G^-1).
Equal pointwise iff [e, B] = 0, which is the stationarity of e at Sigma (s2).
Random numerical data, both signatures; with and without [e,B] = 0.
"""
import numpy as np

rng = np.random.default_rng(7)


def antisym(A):
    return 0.5 * (A - A.T)


def charges(eta, B, e):
    G = e.T @ eta @ e
    Gi = np.linalg.inv(G)
    sq = np.sqrt(abs(np.linalg.det(G)))
    qG = sq * antisym(B @ Gi)
    qW = sq * antisym(np.linalg.inv(e) @ B @ e @ Gi)
    return qG, qW


out = []
for label, eta, B in [
    ('Euclid', np.eye(4), np.array([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], float)),
    ('Lorentz', np.diag([-1., 1, 1, 1]), np.array([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], float)),
]:
    for trial in range(4):
        # e commuting with B: e = (p I + q B) on the normal block, arbitrary on the tangent block
        e = np.zeros((4, 4))
        p, q = rng.normal(size=2)
        e[:2, :2] = p * np.eye(2) + q * B[:2, :2]
        e[2:, 2:] = rng.normal(size=(2, 2))
        qG, qW = charges(eta, B, e)
        comm = np.abs(e @ B - B @ e).max()
        out.append(f"{label} commuting trial {trial}: |[e,B]| = {comm:.1e}, max|q_G - q_W| = {np.abs(qG - qW).max():.2e}, max|q_G| = {np.abs(qG).max():.3f}")
    for trial in range(2):
        e = rng.normal(size=(4, 4))
        qG, qW = charges(eta, B, e)
        out.append(f"{label} generic e trial {trial}: |[e,B]| = {np.abs(e @ B - B @ e).max():.2f}, max|q_G - q_W| = {np.abs(qG - qW).max():.3f}")
print("\n".join(out))
