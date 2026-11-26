"""s2: orbit-extremised (Stueckelberg) quadratic form of rho^2 X about constant Theta-bar, Poisson-class plane waves.

Setting: omega-bar = Theta-bar^{-1} constant antisymmetric, e-bar^A_mu = eta^{AB} omega-bar_{mu B}, G-bar = e-bar^T eta e-bar (constant).
Class perturbation: Theta = Theta-bar + eps T, T^{mn} = q^m u^n - q^n u^m (plane wave, q = Theta-bar p), i.e. delta omega = p ^ (u.omega-bar)
(a closed 2-form), first-order frame amplitude  ehat^A_n = eta^{AB} delta omega_{nB}.
Local rotation (Stueckelberg dressing):  ehat -> ehat + lambda e-bar,  lambda_{AB} antisymmetric, plane-wave amplitude (6 complex).
Phase-averaged second-order torsion invariants need only the first-order torsion amplitude (T-bar = 0).

Checks
 (1) ledger ratios on the delta-rho = 0 class modes:  S^2 : X = 1/3,  N = X/4  (N = TT/4 + TT'/2 - V^2).
 (2) algebraic identity  X = 2 N + (3/2) S^2 + 2 V^2  (exact, torsion irreps).
 (3) N^{(2)} is constant on the rotation orbit; stationary point of X over the orbit has S^2 = 0.
 (4) X_ext / X_class on the delta-rho = 0 modes (expected 1/2) and  X_ext = 2 N + 2 W^2  on all three modes.
 (5) p ^ S-hat = 0 for every class mode (so S can be rotated away); Hessian signature in the two signatures.
"""
import numpy as np


def sym_setup(eta_d, w0):
    eta = np.diag(np.array(eta_d, float)); etai = np.linalg.inv(eta)
    E = np.einsum('AB,mB->Am', etai, w0)
    G = E.T @ eta @ E
    return eta, etai, E, G, np.linalg.inv(G)


def torsion_amp(eta, E, p, Eh):
    TA = 1j*(np.einsum('m,An->Amn', p, Eh) - np.einsum('n,Am->Amn', p, Eh))
    return np.einsum('AB,Al,Bmn->lmn', eta, E, TA)


def invariants(Tl, Gi):
    Tu = np.einsum('la,mb,nc,abc->lmn', Gi, Gi, Gi, Tl)
    avg = lambda a: 0.5*np.real(a)
    TT = avg(np.einsum('lmn,lmn->', Tl, np.conj(Tu)))
    TTp = avg(np.einsum('lmn,mln->', Tl, np.conj(Tu)))
    V = np.einsum('ln,lmn->m', Gi, Tl)
    V2 = avg(np.einsum('m,n,mn->', V, np.conj(V), Gi))
    S = (Tl + np.einsum('lmn->mnl', Tl) + np.einsum('lmn->nlm', Tl))/3.0
    Su = np.einsum('la,mb,nc,abc->lmn', Gi, Gi, Gi, S)
    S2 = avg(np.einsum('lmn,lmn->', S, np.conj(Su)))
    return TT, TTp, V2, S2, V, S


def class_amp(etai, w0, p, u):
    ut = u @ w0
    dom = np.outer(p, ut) - np.outer(ut, p)
    return np.einsum('AB,nB->An', etai, dom).astype(complex)


def W_amp(E, Eh):
    """first-order d ln rho amplitude: W_mu = (1/2) i p_mu tr(E^{-1} Eh) (rho^2 = |det e|)."""
    return 0.5*np.trace(np.linalg.inv(E) @ Eh)


pairs = [(a, b) for a in range(4) for b in range(a+1, 4)]


def shifted(etai, E, Eh, v):
    lam = np.zeros((4, 4), complex)
    for k, (a, b) in enumerate(pairs):
        lam[a, b] = v[k] + 1j*v[6+k]; lam[b, a] = -lam[a, b]
    return Eh + (etai @ lam) @ E


def quad_ext(eta, etai, E, Gi, p, Eh):
    n = 12
    f = lambda v: invariants(torsion_amp(eta, E, p, shifted(etai, E, Eh, v)), Gi)[0]
    c0 = f(np.zeros(n)); g = np.zeros(n); H = np.zeros((n, n))
    for i in range(n):
        e = np.zeros(n); e[i] = 1.0
        g[i] = (f(e) - f(-e))/2; H[i, i] = f(e) + f(-e) - 2*c0
    for i in range(n):
        for j in range(i+1, n):
            ei = np.zeros(n); ej = np.zeros(n); ei[i] = 1; ej[j] = 1
            H[i, j] = H[j, i] = (f(ei+ej) + f(-ei-ej) - f(ei-ej) - f(-ei+ej))/4
    sol = np.linalg.lstsq(H, -g, rcond=1e-10)[0]
    return c0, sol, np.linalg.eigvalsh(H)


rng = np.random.default_rng(2026)


def rand_w0():
    while True:
        w = rng.uniform(-1, 1, (4, 4)); w = w - w.T
        if abs(np.linalg.det(w)) > 0.1:
            return w


dev_ratio=[]; dev_id=[]; dev_s=[]
print("signature  | mode      | S2/X    N/X     X=2N+1.5S2+2V2 (resid) | X_ext/X_cl  S2_ext   N_ext/X_cl  X_ext-(2N+2W2)  p^S")
for eta_d in [(1, 1, 1, 1), (-1, 1, 1, 1)]:
    for trial in range(3):
        w0 = rand_w0(); p = rng.normal(size=4)
        eta, etai, E, G, Gi = sym_setup(eta_d, w0)
        # delta-rho = 0 subspace: V = 0
        M = np.array([np.einsum('ln,lmn->m', Gi, torsion_amp(eta, E, p, class_amp(etai, w0, p, np.eye(4)[k]))) for k in range(4)]).T
        A = np.vstack([M.real, M.imag]); U, S_, Vt = np.linalg.svd(A)
        null = Vt[np.sum(S_ > 1e-10):]
        modes = [("drho=0", u) for u in null]
        # generic polarisation (includes drho != 0)
        modes.append(("generic", rng.normal(size=4)))
        for name, u in modes:
            Eh = class_amp(etai, w0, p, u)
            Tl = torsion_amp(eta, E, p, Eh)
            TT, TTp, V2, S2, V, S = invariants(Tl, Gi)
            if abs(TT) < 1e-9:
                continue
            N = TT/4 + TTp/2 - V2
            ident = TT - (2*N + 1.5*S2 + 2*V2)
            c0, sol, ev = quad_ext(eta, etai, E, Gi, p, Eh)
            Eh2 = shifted(etai, E, Eh, sol)
            T2 = torsion_amp(eta, E, p, Eh2)
            TTe, TTpe, V2e, S2e, Ve, Se = invariants(T2, Gi)
            Ne = TTe/4 + TTpe/2 - V2e
            Wv = 1j*p*W_amp(E, Eh)
            W2 = 0.5*np.real(np.einsum('m,n,mn->', Wv, np.conj(Wv), Gi))
            # p ^ S : antisymmetrised p_[a S_bcd]
            pS = np.abs(np.einsum('a,bcd->abcd', p, S) - np.einsum('b,acd->abcd', p, S)
                        + np.einsum('c,abd->abcd', p, S) - np.einsum('d,abc->abcd', p, S)).max()
            if name=="drho=0": dev_ratio.append(abs(TTe/TT-0.5))
            dev_id.append(abs(TTe-(2*N+2*W2))/abs(TT)); dev_s.append(abs(S2e)/abs(TT))
            print(f"{str(eta_d):14s}| {name:9s} | {S2/TT:.5f} {N/TT:.5f}  {ident: .1e}                  | {TTe/TT:.5f}   {S2e/TT: .1e}  {Ne/TT:.5f}    {TTe-(2*N+2*W2): .1e}     {pS:.1e}")
    print("   Hessian eigenvalue signs over the 12 real Goldstone parameters (+,-):", (int((ev > 1e-9).sum()), int((ev < -1e-9).sum())))

print("max |X_ext/X_class - 1/2| on drho=0 modes:", f"{max(dev_ratio):.1e}", "| max |X_ext-(2N+2W^2)|/|X_class| on all modes:", f"{max(dev_id):.1e}", "| max S2_ext/|X_class|:", f"{max(dev_s):.1e}")
