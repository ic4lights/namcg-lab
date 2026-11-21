# check_f_zeros.py -- proposal 067, round 1.
# Re-derivation (independent of the appH scan) of the Lambert-W zero formula and of the
# zero-free-region claims of the Problem N block of chapters/appH-microscopic-proofs.tex:
#   F(x) = 1 - (x/U)*(log(1/x) + d), principal logarithm,
#   zeros on the principal sheet x = -U / W_j(-U e^{-d}), j in {0,-1} at (U,d)=(10,0),
#   U_*(0) = pi/2 (crossing x = +/- i), U_*(d) = d for d >= 1 (crossing x = 1),
#   U = 10: condition -9.58 < d < 10; at d = 0 the zeros are a complex-conjugate pair
#   with |x| ~ 3.9.
# Method: derive the zero formula symbolically (sympy), enumerate candidate zeros over
# Lambert-W branches (mpmath), keep those that actually satisfy F(x)=0 with the PRINCIPAL
# log (this is the principal-sheet condition, since t = log(1/x) must lie in the principal
# range), count zeros with |x| < 1, and compare with the crossing system
#   d*sin(theta) = theta*cos(theta),  U = d*cos(theta) + theta*sin(theta), theta in (0,pi),
# plus the x = 1 crossing U = d.  Output is a check, not a proof.
# Run: python -I check_f_zeros.py
import sympy as sp
import mpmath as mp

mp.mp.dps = 40

print("=" * 72)
print("1. Symbolic derivation of the zero formula")
print("=" * 72)
x, U, d, t, u = sp.symbols("x Upsilon delta t u", positive=False)
# F = 0  <=>  1 = (x/U)(log(1/x) + d).  Put t = log(1/x), x = exp(-t):
#   t + d = U exp(t)  <=>  (t+d) exp(-(t+d)) = U exp(-d)  <=>  -(t+d) = W(-U e^{-d})
expr = (t + d) * sp.exp(-(t + d)) - U * sp.exp(-d)
lhs = sp.expand(expr)
w = sp.symbols("w")
subs_check = sp.simplify(lhs.subs(t, -d - w) - (-u * sp.exp(-u)).subs(u, w))
print("residual of (t+d)exp(-(t+d)) = U e^{-d} at t = -d - W :", sp.simplify(lhs.subs(t, -d - w)))
print("   (equals -W e^{-W} - W(-U e^{-d})-form identity; vanishes when W = W_j(-U e^{-d}) via W e^W = a)")
# then x = exp(-t) = exp(d + W) = e^d * a / W  with a = -U e^{-d}  =>  x = -U / W.
xd = sp.exp(d + w)
print("x = exp(d+W) ; e^d * (-U e^{-d})/W = ", sp.simplify(sp.exp(d) * (-U * sp.exp(-d)) / w))
print("identity e^W = W/a used; sympy check e^W - W/a at a=-U e^{-d} :",
      sp.simplify(sp.exp(w) - w / (-U * sp.exp(-d))))

print()
print("=" * 72)
print("2. Branch enumeration with the PRINCIPAL log (principal sheet)")
print("=" * 72)

def F(xv, Uv, dv):
    return 1 - (xv / Uv) * (mp.log(1 / xv) + dv)

def principal_sheet_zeros(Uv, dv, jmax=6, tol=mp.mpf("1e-25")):
    a = -Uv * mp.e**(-dv)
    out = []
    for j in range(-jmax, jmax + 1):
        wv = mp.lambertw(a, j)
        if wv == 0:
            continue
        xv = -Uv / wv
        res = abs(F(xv, Uv, dv))
        if res < tol * (1 + abs(xv)):
            out.append((j, xv))
    return out

def in_disc(Uv, dv, jmax=6):
    return sum(1 for j, xv in principal_sheet_zeros(Uv, dv, jmax) if abs(xv) < 1)

print("Zeros at Upsilon=10, delta_W=0 (formula x_j = -U/W_j(-U e^{-d})):")
for j, xv in principal_sheet_zeros(10, 0):
    print(f"  j = {j:+d}   x = {mp.nstr(xv, 12)}   |x| = {mp.nstr(abs(xv), 8)}")
zs = principal_sheet_zeros(10, 0)
print("  branches surviving the principal-sheet condition: j in",
      sorted(j for j, _ in zs))
mods = sorted(abs(zv) for _, zv in zs)
print("  smallest |x| among zeros:", mp.nstr(mods[0], 6),
      "  (text: complex-conjugate pair |k^2| ~ 3.9 L_UV^2)")

print()
print("=" * 72)
print("3. Crossing system and U_*(delta)")
print("=" * 72)
# On |x| = 1, x = e^{i theta}, theta in (0,pi): principal log(1/x) = -i theta,
# F = 0 <=> U = delta cos(theta) + theta sin(theta) AND delta sin(theta) = theta cos(theta).
def Ustar(dv):
    # circle crossing for delta < 1: theta* solves delta = theta cot(theta), U* = theta/sin(theta)
    if dv >= 1:
        return dv  # crossing at x = 1, line U = delta
    th = mp.findroot(lambda th: th / mp.sin(th) * 0 + (th * (1 / mp.tan(th)) - dv),
                     mp.pi / 2 if dv <= 0 else mp.pi / 4)
    return th / mp.sin(th)

print("U_*(0) from the system: theta = pi/2, U = pi/2 =",
      mp.nstr(mp.pi / 2, 10), "; numeric branch value:", mp.nstr(Ustar(0), 10))
for dv in [0.0, 0.5, 0.99, 1.0, 2.0, 5.0, 20.0]:
    print(f"  delta_W = {dv:5.2f}   U_* = {mp.nstr(Ustar(dv), 10)}")

print("delta at the U=10 circle crossing (upper edge of the delta-window):")
th10 = mp.findroot(lambda th: th / mp.sin(th) - 10, mp.pi - 0.35)
dmin = th10 * (1 / mp.tan(th10))
print("  theta* =", mp.nstr(th10, 12), "  delta_min(10) =", mp.nstr(dmin, 10),
      "  (text: -9.58 < delta_W)")
print("  x=1 line gives delta_W < Upsilon = 10; window: -9.58 < delta_W < 10 (text)")

print()
print("=" * 72)
print("4. Zero counts in |x| < 1 vs the region Upsilon > U_*(delta_W)")
print("=" * 72)
cases = [(10.0, 0.0, 0), (1.2, 0.0, ">0"), (2.0, 0.0, 0), (1.56, 0.0, ">0"),
         (2.5, 2.0, 0), (1.8, 2.0, ">0"), (6.0, 5.0, 0), (4.5, 5.0, ">0"),
         (25.0, 20.0, 0), (10.0, -9.5, 0), (10.0, -9.7, ">0")]
allok = True
for Uv, dv, expect in cases:
    n = in_disc(Uv, dv)
    pred = Uv > Ustar(dv)
    ok = (n == 0) == pred and (n > 0) == (not pred)
    allok = allok and ok
    print(f"  U={Uv:5.2f} d={dv:5.2f}  zeros in disc: {n:2d}   "
          f"U > U*: {pred}   expect {expect}   ok: {ok}")
print("all region comparisons consistent:", allok)

print()
print("5. Pinch at x = 1 for delta_W >= 1 (minimum modulus of zeros near U = delta):")
for dv, Uv in [(2.0, 1.97), (2.0, 2.03), (5.0, 4.95), (5.0, 5.05)]:
    zs2 = principal_sheet_zeros(Uv, dv)
    if zs2:
        mn = min(abs(zv) for _, zv in zs2)
        print(f"  delta={dv} U={Uv}: min |zero| = {mp.nstr(mn, 8)} "
              f"({'inside' if mn < 1 else 'outside'} disc)")
print("DONE")
