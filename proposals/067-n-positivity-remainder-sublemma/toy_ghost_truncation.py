# toy_ghost_truncation.py -- proposal 067, round 1.
# Two-oscillator quantum mechanics: a light observable x (frequency^2 mx2) linearly coupled
# to a heavy mode y (frequency^2 my2) with coupling g (g has dimension of frequency^2).
# The EXACT composite two-point function of x,
#   D_xx(s) = (s - my2)/det(s - M^2),  M^2 = [[mx2, g], [g, my2]],
# has positive Kallen-Lehmann residues at both normal-mode poles (proof: Delta^2 -
# (mx2-my2)^2 = 4g^2 > 0, and the residues are squared eigenvector components; they also
# satisfy the completeness sum rule r_+ + r_- = 1).  The EFFECTIVE kernel of x,
#   Gamma(s) = s - mx2 - g^2/(s - my2) = s - mx2 + g^2/(my2 - s),
# expanded in powers of s/my2 (valid for |s| < my2) and truncated at O(s^2),
#   Gamma_2(s) = s - mx2 + (g^2/my2)(1 + s/my2 + s^2/my2^2),
# develops a SECOND real pole at s* < 0 (tachyonic location) with NEGATIVE residue
# (proof: Gamma_2'(s*) = a (s* - s_p), a > 0, s* < 0 < s_p), at |s*| = (b+sqrt(D))/(2a)
# > b/a = my2 (1 + my2^2/g^2)... see printout, i.e. strictly above the expansion scale
# my2 of the truncated expansion.  This is the artifact the Problem N block records for
# the composite graviton: a negative-residue real pole of a truncated kernel of a theory
# whose exact correlator is positive.  Symbolic output checks the sign statements and
# locations whose proofs are displayed alongside.
# Run: python -I toy_ghost_truncation.py
import sympy as sp

s = sp.symbols("s", real=True)
mx2, my2, g = sp.symbols("omega_x2 omega_y2 g", positive=True)

print("=" * 72)
print("1. Exact model: M^2 = [[mx2, g], [g, my2]], D_xx(s) = (s - my2)/det(s - M^2)")
print("=" * 72)
Delta = sp.sqrt((mx2 - my2) ** 2 + 4 * g ** 2)
lam_p = (mx2 + my2 + Delta) / 2
lam_m = (mx2 + my2 - Delta) / 2
Dxx = (s - my2) / ((s - lam_p) * (s - lam_m))
r_p = sp.simplify(sp.residue(Dxx, s, lam_p))
r_m = sp.simplify(sp.residue(Dxx, s, lam_m))
print("residue at s = lam_+ :", sp.simplify(r_p))
print("residue at s = lam_- :", sp.simplify(r_m))
proof = sp.simplify(Delta ** 2 - (mx2 - my2) ** 2)
print("Delta^2 - (mx2-my2)^2 =", proof, "> 0 for g != 0  =>  both numerators positive")
print("sum rule r_+ + r_- =", sp.simplify(r_p + r_m),
      "(completeness: sum of squared eigenvector components = 1)")

print()
print("=" * 72)
print("2. Truncated kernel Gamma_2(s) = s - mx2 + (g^2/my2)(1 + s/my2 + s^2/my2^2)")
print("=" * 72)
Gam2 = s - mx2 + (g ** 2 / my2) * (1 + s / my2 + s ** 2 / my2 ** 2)
a2 = sp.expand(Gam2).coeff(s, 2)
b2 = sp.expand(Gam2).coeff(s, 1)
c2 = sp.expand(Gam2).coeff(s, 0)
print("coefficients: a =", a2, ", b =", b2, ", c =", c2)
disc = sp.sqrt(b2 ** 2 - 4 * a2 * c2)
s_spur = (-b2 - disc) / (2 * a2)
s_phys = (-b2 + disc) / (2 * a2)
print("regime mx2 > g^2/my2 (physical pole not removed): then c < 0,")
print("product of roots c/a < 0 => exactly one negative root s* and one positive s_p,")
print("and sum -b/a < 0 => |s*| > s_p.")
res_spur = sp.simplify(1 / sp.diff(Gam2, s).subs(s, s_spur))
chk = sp.simplify(sp.diff(Gam2, s).subs(s, s_spur) - a2 * (s_spur - s_phys))
_ = res_spur
print("identity Gamma_2'(s*) = a*(s* - s_p); residual:", chk,
      " => a>0, s*<0<s_p => Gamma_2'(s*)<0 => residue(s*) = 1/Gamma_2'(s*) < 0")
_ = s_spur
print("|s*| = (b + sqrt(D))/(2a) > b/a (since c<0 => D > b^2);")
print("b/a =", sp.simplify(b2 / a2), " ;  b/a - my2 =", sp.simplify(sp.together(b2 / a2 - my2)),
      " > 0  =>  |s*| > my2 (the expansion scale): the spurious pole is OUTSIDE the")
print("domain |s| < my2 of validity of the O(s^2) truncation.")

print()
print("=" * 72)
print("3. Numeric instance: my2 = 100 (expansion scale |s| < 100), mx2 = 1, g = 1")
print("=" * 72)
num = {my2: 100, mx2: 1, g: 1}
r_spur_n = sp.N(s_spur.subs(num), 12)
r_phys_n = sp.N(s_phys.subs(num), 12)
print("roots of Gamma_2: s* =", r_spur_n, " s_p =", r_phys_n)
dG = sp.diff(Gam2, s)
print("residue at s*:", sp.N((1 / dG).subs(num).subs(s, s_spur.subs(num)), 12),
      "   residue at s_p:", sp.N((1 / dG).subs(num).subs(s, s_phys.subs(num)), 12))
ex_p = float(r_p.subs(num))
ex_m = float(r_m.subs(num))
print("exact-model poles and residues: lam_+ =", sp.N(lam_p.subs(num), 12), "r_+ =", ex_p,
      "; lam_- =", sp.N(lam_m.subs(num), 12), "r_- =", ex_m)
print("exact residues positive:", ex_p > 0 and ex_m > 0)
print("|s*| =", sp.N(abs(r_spur_n), 12), "> my2 = 100 (above the expansion scale of")
print("Gamma_2, while the exact kernel has no pole there)")

print()
print("=" * 72)
print("4. Consistency: exact kernel zero-free where the truncation adds the spurious pole")
print("=" * 72)
Gam_exact = s - mx2 - g ** 2 / (s - my2)
ex_roots = sp.solve(sp.Eq(sp.together(Gam_exact), 0), s)
print("exact zeros of Gamma (real):", [sp.N(rt, 12) for rt in ex_roots])
print("=> the exact response has poles only at lam_-, lam_+ (inside the spectrum, positive")
print("   residues); the negative-residue tachyonic pole near s* ~ -my2^3/g^2 is a pure")
print("   artifact of the O(s^2) truncation of the kernel.")
print("DONE")
