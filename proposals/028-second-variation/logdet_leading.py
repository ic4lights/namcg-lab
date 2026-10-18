"""028 script 7: the non-expanded leading-symbol supertrace logarithm at fixed xi (commuting symbols).
 Lfun(sigma;f_e,f_m) = sum_i w_i ln det(sigma + Zsym_i),  Zsym_i = species matrices contracted with i F(xi)  (symbol of {F,.} is i F).
Closed form: ln(s^2-4fm^2)+ln(s^2+4fe^2)+4 ln s -2 ln[(s+fm)^2+fe^2] -2 ln[(s-fm)^2+fe^2];  large-sigma series  -6 (fe^2+fm^2)^2/sigma^4 + O(sigma^-6).
Checks: (1) numeric eigenvalue sum equals closed form for random F, (2) series coefficient, (3) the closed form has branch points at sigma=+-2 fm (real), +-2 i fe, -+fm -+ i fe (complex)."""
import numpy as np
from tensors_lemma import SP, eta, fef_m
rng = np.random.default_rng(4)
def L_num(F, sig):
    tot = 0.0
    for w, Z, d, _ in SP:
        Zm = sum(Z[(a, b)]*(1j*F[a, b]) for a in range(4) for b in range(4) if a != b)
        ev = np.linalg.eigvals(Zm)
        tot += w*np.sum(np.log(sig + ev))
    return tot
def L_closed(sig, fe, fm):
    return (np.log(sig**2 - 4*fm**2) + np.log(sig**2 + 4*fe**2) + 4*np.log(sig)
            - 2*np.log((sig + fm)**2 + fe**2) - 2*np.log((sig - fm)**2 + fe**2))
for t in range(3):
    A = rng.normal(size=(4, 4)); F = A - A.T
    fe, fm = fef_m(F)
    sig = 40.0 + 0.0j
    ln, lc = L_num(F, sig), L_closed(sig, fe, fm)
    ser = -6*(fe**2 + fm**2)**2/sig**4
    print("f_e=%.3f f_m=%.3f sigma=40: numeric %.10e  closed %.10e  series %.10e  (ratio numeric/series %.5f)" % (fe, fm, ln.real, lc.real, ser.real, ln.real/ser.real))
for sig in (200.0, 1000.0):
    fe, fm = 1.3, 0.7
    print("sigma=%g: closed*sigma^4/(fe^2+fm^2)^2 = %.6f (-> -6)" % (sig, (L_closed(sig + 0j, fe, fm)*sig**4/(fe**2 + fm**2)**2).real))
