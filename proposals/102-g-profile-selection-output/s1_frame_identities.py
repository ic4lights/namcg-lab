# s1_frame_identities.py - exact/numerical checks for proposal 102.
# Spin-l factor matrices of the compact fuzzy factor: the adjoint su(2) harmonics
# T_{lm}, l = 0..N-1, m = -l..l, an orthonormal basis of N x N matrices, built here
# as the spectral projectors of the quadratic Casimir of the adjoint action
# (L2 = -sum_a ad(J_a) ad(J_a), J_a the spin-j = (N-1)/2 irreducible representation);
# [Pi_l]_{(v,i),(v,i)} = sum_m |T_{lm;vi}|^2 is basis-independent within the level.
# Checks:
#  (1) Parseval:  sum_l [Pi_l]_{(v,i),(v,i)} = 1 for every matrix unit (v,i).
#  (2) Row-uniformity per level: sum_i [Pi_l]_{(v,i),(v,i)} = (2l+1)/N for every v,l
#      (the row-sum identity of the Row length paragraph, in basis form).
#  (3) Label-blind FULL-band (f(l) = f0 for all l) induces iid slots:
#      sum_l [Pi_l]_{(v,i),(v,j)} = delta_ij (exact slot independence, uniform profile).
#  (4) Label-blind TRUNCATED at l_c: off-diagonal slot covariance and profile spread
#      are nonzero for l_c < N-1 (data: max offdiag/min diag, profile max/min).
#  (5) Laplacian weight-branch profile f(l) = l(l+1)/4, cap cut: induced slot
#      variances, effective dimension D_eff/D, rho_2 = 1 + s2/W^2 excess over the
#      sharp floor 1 + 1/D, off-diagonal covariance ratio; ground branch
#      f(l) = sqrt(l(l+1))/2 for comparison.
import numpy as np

def spin_ops(N):
    j = (N - 1) / 2.0
    m = np.arange(j, -j - 1, -1)          # m = j, j-1, ..., -j
    Jz = np.diag(m)
    Jp = np.zeros((N, N))
    for k in range(N - 1):                # ladder: m_k = j-k -> m_{k+1} = m_k - 1
        Jp[k, k + 1] = np.sqrt(j * (j + 1) - m[k + 1] * (m[k + 1] + 1))
    Jm = Jp.T
    Jx = (Jp + Jm) / 2.0
    Jy = (Jp - Jm) / 2j          # /2i
    return Jz, Jx, Jy

def casimir_projectors(N):
    Jz, Jx, Jy = spin_ops(N)
    def ad(A):                            # vec(AX - XA), row-major flatten (v,i)
        return np.kron(A, np.eye(N)) - np.kron(np.eye(N), A.T)
    L2 = ad(Jz) @ ad(Jz) + ad(Jx) @ ad(Jx) + ad(Jy) @ ad(Jy)  # ad self-adjoint: spec +l(l+1)
    L2 = (L2 + L2.conj().T) / 2.0
    w, V = np.linalg.eigh(L2)
    Pis = []
    idx = 0
    for l in range(N):
        target = l * (l + 1)
        sel = np.where(np.abs(w - target) < 1e-6 * max(1.0, target))[0]
        assert len(sel) == 2 * l + 1, (N, l, len(sel))
        W = V[:, sel]
        Pis.append(W @ W.conj().T)
        idx += len(sel)
    assert idx == N * N
    return Pis

def run(N, lc=None, report=True):
    if lc is None: lc = N - 1
    Pis = casimir_projectors(N)
    Dl = np.array([np.diag(P).real.reshape(N, N) for P in Pis])   # [l, v, i]
    errs = {}
    errs["parseval"] = np.max(np.abs(Dl.sum(axis=0) - 1.0))
    rs = Dl.sum(axis=2)                                   # [l, v]
    errs["rowlevel"] = np.max(np.abs(rs - np.array([2 * l + 1 for l in range(N)])[:, None] / N))
    ident_err = 0.0
    for v in range(N):
        S = sum(P.reshape(N, N, N, N)[v, :, v, :] for P in Pis)
        ident_err = max(ident_err, np.max(np.abs(S - np.eye(N))))
    errs["iid_full"] = ident_err
    M = N // 2
    v_edge = M - 1                                        # cap = M largest m: 0..M-1
    slots = np.arange(M, N)
    D = N - M
    Z = np.zeros((N * N, N * N), dtype=complex)
    Pt = sum(Pis[lc + 1:], Z)                             # complement projector: l > lc
    St = Pt.reshape(N, N, N, N)[v_edge, :, v_edge, :][np.ix_(slots, slots)]
    full = sum(P.reshape(N, N, N, N)[v_edge, :, v_edge, :] for P in Pis)[np.ix_(slots, slots)]
    St = full - St                                        # truncated sum l <= lc
    diagt = np.real(np.diag(St))
    offd = np.max(np.abs(St - np.diag(diagt)))
    errs["trunc_offdiag_ratio"] = offd / diagt.min()
    errs["trunc_profile_spread"] = diagt.max() / diagt.min() - 1.0
    res = {}
    for name, fv in (("lap4", lambda l: l * (l + 1) / 4.0),
                     ("sqrt2", lambda l: np.sqrt(l * (l + 1)) / 2.0)):
        C = sum(fv(l) * P.reshape(N, N, N, N)[v_edge, :, v_edge, :]
                for l, P in enumerate(Pis[:lc + 1]))
        Cs = C[np.ix_(slots, slots)]
        g = np.real(np.diag(Cs))
        W = g.sum()
        s2 = (g * g).sum()
        Deff = W * W / s2
        off = np.max(np.abs(Cs - np.diag(np.diag(Cs))))
        res[name] = dict(D_eff_over_D=Deff / D, rho2=1 + s2 / (W * W),
                         rho2_floor=1 + 1.0 / D,
                         offdiag_over_mindiag=off / g.min(),
                         gmax_over_gmin=g.max() / g.min())
    if report:
        print("N=%d M=%d D=%d lc=%d" % (N, M, D, lc))
        print("  parseval maxerr %.3e  rowlevel maxerr %.3e  iid_full maxerr %.3e"
              % (errs["parseval"], errs["rowlevel"], errs["iid_full"]))
        print("  label-blind truncated: offdiag/minDiag %.4f  profile spread %.4f"
              % (errs["trunc_offdiag_ratio"], errs["trunc_profile_spread"]))
        for name in ("lap4", "sqrt2"):
            r = res[name]
            print("  f=%s: D_eff/D %.5f  rho_2 %.6f (floor %.6f)  offdiag/minDiag %.4f  gmax/gmin %.4f"
                  % (name, r["D_eff_over_D"], r["rho2"], r["rho2_floor"],
                     r["offdiag_over_mindiag"], r["gmax_over_gmin"]))
    return errs, res

if __name__ == "__main__":
    print("== frame identities and induced slot laws (spin-l factor basis) ==")
    for N in (6, 8, 12, 16, 24, 32):
        run(N)
    print("== truncated label-blind and Laplacian branches at interior cutoffs ==")
    for N, lc in ((16, 4), (16, 8), (32, 8), (32, 16)):
        run(N, lc=lc)
