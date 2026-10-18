"""027 script 3: geometry of the fibre-bounded cone window at orbit points of CP^{1,2}.
Whitened coordinates xi = V_b N_b^{-1/2} u + V_f N_f^{-1/2} z with  |u|^2 = alpha q_b,  |z|^2 = beta q_f,  -sigma(C42) = |u|^2 - |z|^2  (pencil of 023: C41 v = lam C42 v, lam=1/2 base, 1 vertical).
S = T^T K_Box T  is the Lorentzian symbol sigma(Box) in these coordinates (rank 4).  Writes S = [[Suu,Suz],[Szu,Szz]];  Schur complement Szz - Szu Suu^{-1} Suz must vanish (rank 4) and
sigma = Q_L(u + w z),  Q_L = Suu,  w = Suu^{-1} Suz.   The shell/apex lemma needs  ||w||_op < 1."""
import numpy as np, scipy.linalg as sl
from symbol_tools import *
from sym_signatures import forms
rng = np.random.default_rng(11)
e5 = np.diag([-1., 1, 1, 1, 1])
def frame(M0):
    rk, F = forms(M0)
    lam, V = sl.eig(F['C41'], F['C42']); lam = np.real(lam); V = np.real(V)
    # orthonormalise inside eigenspaces w.r.t. |K42|
    Vb = V[:, np.abs(lam - 0.5) < 1e-6]; Vf = V[:, np.abs(lam - 1.0) < 1e-6]
    Nb = -Vb.T @ F['C42'] @ Vb; Nf = Vf.T @ F['C42'] @ Vf
    wb, Ub = np.linalg.eigh(Nb); wf, Uf = np.linalg.eigh(Nf)
    Tb = Vb @ Ub @ np.diag(wb**-0.5) @ Ub.T          # columns: u-directions with  u^T u = alpha q_b
    Tf = Vf @ Uf @ np.diag(wf**-0.5) @ Uf.T
    T = np.hstack([Tb, Tf])
    return F, T
def analyse(M0):
    F, T = frame(M0)
    S = T.T @ F['Box4'] @ T
    Suu, Suz, Szz = S[:4, :4], S[:4, 4:], S[4:, 4:]
    ev = np.linalg.eigvalsh(Suu)
    w = np.linalg.solve(Suu, Suz)
    schur = np.max(np.abs(Szz - Suz.T @ w))/np.max(np.abs(S))
    # check the C42 and C41 forms in whitened coords
    K42 = T.T @ F['C42'] @ T
    return dict(T=T, S=S, ev=ev, w=w, wn=np.linalg.norm(w, 2), schur=schur, K42=K42, F=F)
if __name__ == "__main__":
    print("   y4^2    ell^2 | eig(Suu) | ||w||_2 | Schur residual | K42 in whitened coords: diag(-1x4,+1x2)? | |det T|")
    for t in range(14):
        z = rand_z_pos(rng, rng.uniform(0.5, 4)); M0 = Mfun(z); y = M0[:5, 5]
        r = analyse(M0)
        K42 = r['K42']
        ok = np.allclose(K42, np.diag([-1., -1, -1, -1, 1, 1]), atol=1e-8)
        print("%8.4f %8.4f | %s | %7.4f | %.1e | %s | %.4f" % (y[4]**2, -(y @ e5 @ y), np.round(r['ev'], 4), r['wn'], r['schur'], ok, abs(np.linalg.det(r['T']))))
