"""034: Lorentz transformation of the data (F, kappa, alpha, y) to the canonical frame F_01 = a, F_23 = b (a,b > 0), eta = diag(-1,1,1,1).
omega = C omega',  F' = B F B^T,  kappa' = B kappa,  alpha' = B alpha,  y' = C^T y,  B = C^{-1},  C^T eta C = eta."""
import numpy as np
eta = np.diag([-1., 1, 1, 1])
def canonical(F):
    N = F @ eta
    w, V = np.linalg.eig(N)
    re = [i for i in range(4) if abs(w[i].imag) < 1e-9 * max(1, abs(w).max())]
    im = [i for i in range(4) if w[i].imag > 1e-9 * max(1, abs(w).max())]
    assert len(re) == 2 and len(im) == 1, (w,)
    ip, im_ = (re[0], re[1]) if w[re[0]].real > 0 else (re[1], re[0])
    a = abs(w[ip].real)
    ep = V[:, ip].real; em = V[:, im_].real
    g = ep @ eta @ em
    if g < 0: em = -em; g = -g
    ep = ep / np.sqrt(g); em = em / np.sqrt(g)
    c1 = (ep + em) / np.sqrt(2); c0 = (ep - em) / np.sqrt(2)
    # check N c1 = a c0, N c0 = a c1
    if not (np.allclose(N @ c1, a * c0, atol=1e-8) and np.allclose(N @ c0, a * c1, atol=1e-8)):
        c0 = -c0
    assert np.allclose(N @ c1, a * c0, atol=1e-8) and np.allclose(N @ c0, a * c1, atol=1e-8)
    wv = V[:, im[0]]
    b = w[im[0]].imag
    u = wv.real; v = wv.imag
    sc = np.sqrt(abs(u @ eta @ u))
    u = u / sc; v = v / sc
    # N v = b u, N u = -b v  (N w = i b w, w = u + i v: N u = -b v, N v = b u); but scaling by complex phase may rotate u,v: re-orthonormalise
    c2, c3 = u, v
    if not (np.allclose(N @ c3, b * c2, atol=1e-7) and np.allclose(N @ c2, -b * c3, atol=1e-7)):
        raise RuntimeError("magnetic plane relations fail")
    C = np.column_stack([c0, c1, c2, c3])
    assert np.allclose(C.T @ eta @ C, eta, atol=1e-7), np.round(C.T @ eta @ C, 6)
    Bm = np.linalg.inv(C)
    Fc = Bm @ F @ Bm.T
    return a, b, C, Bm, Fc
if __name__ == "__main__":
    rng = np.random.default_rng(1)
    X = rng.normal(size=(4, 4)); F = X - X.T
    a, b, C, Bm, Fc = canonical(F)
    print(a, b); print(np.round(Fc, 8))
