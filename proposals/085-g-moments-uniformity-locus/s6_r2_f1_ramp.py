from fractions import Fraction

# S6 (round 2): F1 verification with exact rational arithmetic.
# E_u Gamma = (D*sum g^2 - W^2)/(D(D+1)) for the integrated f = nu*l/2 proxy
# profiles under the two slot-count conventions:
#   A (s5 convention):  D = (lc+1)^2, includes one l=0 zero-variance slot
#                       (adding a g=0 slot leaves W, sum g^2 and D_eff unchanged).
#   B (gatekeeper ramp): D = (lc+1)^2 - 1 = sum_{l=1..lc} (2l+1).
# Fixed nu=1: E_u Gamma GROWS ~ nu^2 L^2 / 72 (it does not vanish): the r1
#   insert clause is false in the repository's fixed-nu proxy convention (F1).
# Fixed W=1: E_u Gamma -> 0 like W^2/(8 D^2): the corrected fixed-W clause.
# Reproduces review-r1 ramp data 23.233 / 91.009 / 359.9 / 1431 (fixed nu) and
# 4.57e-8 -> 1.18e-11 (fixed W).

def proxy(lc):
    W = sum(Fraction(2*l+1)*Fraction(l, 2) for l in range(1, lc+1))
    S2 = sum(Fraction(2*l+1)*Fraction(l, 2)**2 for l in range(1, lc+1))
    return W, S2

for lc in (40, 80, 160, 320):
    W, S2 = proxy(lc)
    DB = (lc+1)**2 - 1
    for name, D in (("B no-zero-slot", DB), ("A with-zero-slot", DB+1)):
        Eg = (D*S2 - W*W)/(Fraction(D)*(D+1))
        print("lc=%4d %s: D=%7d  E_uGamma(nu=1) = %10.4f" % (lc, name, D, float(Eg)))

GK = {40: 23.233, 80: 91.009, 160: 359.9, 320: 1431.0}
for lc in (40, 80, 160, 320):
    W, S2 = proxy(lc)
    D = (lc+1)**2 - 1
    Eg = float((D*S2 - W*W)/(Fraction(D)*(D+1)))
    assert abs(Eg/GK[lc] - 1) < 2e-3, (lc, Eg, GK[lc])
    print("fixed-nu check lc=%3d: %.4f vs gatekeeper %.5g (rel dev %.1e) ; "
          "E_uGamma/L^2 = %.6f (1/72 = %.6f)"
          % (lc, Eg, GK[lc], abs(Eg/GK[lc]-1), Eg/lc**2, 1/72))

for lc in (40, 320):
    W, S2 = proxy(lc)
    D = (lc+1)**2 - 1
    EgW = float((D*S2/W**2 - 1)/(Fraction(D)*(D+1)))
    print("lc=%4d fixed-W=1: E_uGamma = %.4e ; W^2/(8D^2) = %.4e ; ratio %.5f"
          % (lc, EgW, 1.0/(8*D*D), EgW/(1.0/(8*D*D))))

# review-r1 quotes these fixed-W values to 3 significant figures, so the
# comparison tolerance is 5e-3 (rounding of the quoted reference, not of the
# exact computation, which is a Fraction throughout).
GKW = {40: 4.57e-8, 320: 1.18e-11}
for lc, ref in sorted(GKW.items()):
    W, S2 = proxy(lc)
    D = (lc+1)**2 - 1
    EgW = float((D*S2/W**2 - 1)/(Fraction(D)*(D+1)))
    assert abs(EgW/ref - 1) < 5e-3, (lc, EgW, ref)
print("S6 DONE")
