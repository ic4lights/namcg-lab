from fractions import Fraction
import math

# S5: the integrated fuzzy variance proxies (appH L3147 profile convention:
# boundary-row slots (l,m), 1 <= l <= l_c, (2l+1) copies with variance f(l)=nu*l/2;
# nu drops out of D_eff = (sum g)^2 / sum g^2) are nonuniform profiles whose
# effective dimension grows with the cutoff while D_eff/D stays strictly below 1:
# the proxies realize recovery through D_eff -> infinity with a strictly
# increasing (ramp) profile, NOT through the uniform profile.

def proxy(lc):
    D = (lc+1)**2
    W = sum(Fraction(2*l+1)*Fraction(l, 2) for l in range(1, lc+1))
    S2 = sum(Fraction(2*l+1)*Fraction(l, 2)**2 for l in range(1, lc+1))
    Deff = W*W/S2
    return D, W, S2, Deff

for lc in (20, 40, 80, 160, 320):
    D, W, S2, Deff = proxy(lc)
    f = float(Deff)
    print("l_c=%d: D=%d, D_eff=%.2f (quoted 1488 at 40, 23017 at 160), "
          "rho2-1=1/D_eff=%.4g, 6/D_eff=%.4g (quoted excesses 4.0e-3, 2.6e-4), "
          "D_eff/D=%.6f" % (lc, D, f, 1/f, 6/f, f/D))

# limit of D_eff/D for the ramp profile: asymptotics sum(2l+1)l ~ (2/3)L^3,
# sum(2l+1)l^2 ~ (1/2)L^4 -> D_eff ~ (4/9)L^6/((1/2)L^4) = (8/9)L^2, D ~ L^2.
for lc in (160, 320, 640, 1280):
    D, W, S2, Deff = proxy(lc)
    print("l_c=%d: D_eff/D = %.6f (8/9 = %.6f)" % (lc, float(Deff)/D, 8/9))

# frame-averaged coupling prediction for the proxies (nu=1): E_u Gamma =
# W^2 (D/D_eff - 1)/(D(D+1)) -> 0 as D -> inf at fixed W: decoupling in the
# frame average WITHOUT uniformity at fixed D.
for lc in (40, 160):
    D, W, S2, Deff = proxy(lc)
    Gam_avg = W*W*(D/Deff - 1)/(D*(D+1))
    Gam_unif_frame = (S2/D - W*W/D**2)  # Gamma at uniform frame |u_i|^2=1/D
    print("l_c=%d: E_u[Gamma] = %.6g ; Gamma(uniform frame) = %.6g ; both > 0 (nonuniform)"
          % (lc, float(Gam_avg), float(Gam_unif_frame)))

# witness: the uniform profile at the same D has D_eff = D exactly.
lc = 40
D, W, S2, Deff = proxy(lc)
Du = D
Wu = Fraction(1)
S2u = Fraction(1)*D*(Wu/D)**2*D
Deffu = (Wu/D)**2*D**2/((Wu/D)**2*D)
print("uniform profile check: D_eff = %s (equals D: %s)" % (Deffu, Deffu == D))
print("S5 DONE")
