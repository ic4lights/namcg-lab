"""027 script 8: Zeeman/flux structure over the fibre-bounded cone window.  F_ab(xi) = xi(J_ab) (J_ab = Hamiltonian field of M_ab, a,b<=3), linear in the cotangent vector xi.
Eigenvalues of eta F: real pair +-A ('electric': Zeeman of H_V imaginary, factor exp(+-2 s A)) and imaginary pair +-iB ('magnetic': phases exp(-+2 i s B)).
(a) vertical directions (xi = T_f z, |z|=1),  (b) base directions (xi = T_b u, |u|=1) = invariant-sector momenta,  (c) generic unit directions of the whitened 6-space.
Reports A_max, B_max, and the sign of  I1 = B^2 - A^2 = F_ab F^ab / 2."""
import numpy as np
from cone_window_geometry import *
from symbol_tools import *
eta = np.diag([-1., 1, 1, 1])
rng = np.random.default_rng(7)
def Fpack(M0):
    r = analyse(M0)
    F = r['F']
    # tangent-space coordinates: same basis as forms(): rebuild
    V = {p: vec(M0, *p) for p in pairs}
    T15 = np.array([V[p] for p in pairs]); u, sv, vh = np.linalg.svd(T15); rk = int(np.sum(sv > 1e-9*sv[0])); E = vh[:rk]
    c = {p: E @ V[p] for p in pairs}
    C = np.zeros((4, 4, 6))
    for a in range(4):
        for b in range(a + 1, 4):
            C[a, b] = c[(a, b)]; C[b, a] = -c[(a, b)]
    return r['T'], C
def classify(Fm):
    ev = np.linalg.eigvals(eta @ Fm)
    re = np.sort(np.abs(ev.real))[::-1]; im = np.sort(np.abs(ev.imag))[::-1]
    A = re[0]; B = im[0]
    return A, B, ev
if __name__ == "__main__":
    print("   y4^2   ell^2 | vertical: A_max  B_max  (A^2-B^2) range | base: A_max  B_max | generic 6D unit xi: A_max, B_max, frac(A>0), frac(B>0), frac(F^2>0) | A/|xi| coth, 1/sinh")
    for t in range(8):
        z = rand_z_pos(rng, rng.uniform(0.5, 4)); M0 = Mfun(z); y = M0[:5, 5]
        ell2 = -(y @ np.diag([-1., 1, 1, 1, 1]) @ y)
        T, C = Fpack(M0)
        out = []
        for lab, cols in (('v', slice(4, 6)), ('b', slice(0, 4))):
            Am = Bm = 0.0; lo = 1e9; hi = -1e9
            n = cols.stop - cols.start
            for k in range(400):
                v = rng.normal(size=n); v /= np.linalg.norm(v)
                xi = T[:, cols] @ v
                Fm = np.einsum('abk,k->ab', C, xi)
                A, B, ev = classify(Fm)
                Am = max(Am, A); Bm = max(Bm, B); lo = min(lo, A*A - B*B); hi = max(hi, A*A - B*B)
            out.append((Am, Bm, lo, hi))
        Ag = Bg = 0.0; fa = fb = fp = 0; N = 600
        for k in range(N):
            v = rng.normal(size=6); v /= np.linalg.norm(v)
            xi = T @ v; Fm = np.einsum('abk,k->ab', C, xi)
            A, B, ev = classify(Fm)
            Ag = max(Ag, A); Bg = max(Bg, B); fa += A > 1e-9; fb += B > 1e-9; fp += (B*B - A*A) > 0
        print("%8.3f %7.3f | v: %7.4f %7.4f (%8.4f,%8.4f) | b: %7.4f %7.4f (%8.4f,%8.4f) | g: %7.4f %7.4f %.2f %.2f %.2f | %.3f %.3f" % (y[4]**2, ell2, out[0][0], out[0][1], out[0][2], out[0][3], out[1][0], out[1][1], out[1][2], out[1][3], Ag, Bg, fa/N, fb/N, fp/N, np.sqrt(1 + ell2/y[4]**2), np.sqrt(ell2/y[4]**2)))
