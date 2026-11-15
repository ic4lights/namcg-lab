"""s3: the merged cubic-branch point of appH (x = 3/10, tree quartic 7.935, tree cubic -12.36,
units F sqrt|g| N^2 vartheta^2 / 32 pi^2), loop/tree ratios, the implied c/chi, V/T, and the
size of the loop term omitted when the cubic Hessian is left out of the vector operator."""
import numpy as np, sympy as sp, importlib.util, os
spec = importlib.util.spec_from_file_location("s2", os.path.join(os.path.dirname(os.path.abspath(__file__)), "s2_traces.py"))
import io, contextlib
s2 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(s2)

print("A. merged point (operators without the cubic Hessian, as merged)")
x = sp.Rational(3, 10); Q = sp.Rational(7935, 1000); C = sp.Rational(-1236, 100)
U4 = -x**2; U2 = -3 * x; Y = sp.Rational(15, 2)
Lp = 4 * U4 + 2 * U2 + Y
print("  loop slope L' = 4U4+2U2+Y =", Lp, "=", float(Lp), "; -4x^2-6x+15/2 =", float(-4*x**2-6*x+sp.Rational(15,2)))
tree_slope = 4 * Q + 3 * C
print("  tree slope 4Q+3C =", float(tree_slope), "; sum =", float(tree_slope + Lp))
tree_cc = 16 * Q + 9 * C; loop_cc = 16 * U4 + 4 * U2
Ucc = tree_cc + loop_cc
print("  U_chichi: tree", float(tree_cc), "loop", float(loop_cc), "total", float(Ucc), " loop/tree =", float(loop_cc / tree_cc))
beta = 2 * Lp / Ucc
print("  beta_K = 2L'/U_chichi =", float(beta))
print("  slope: loop/tree = ", float(Lp / tree_slope), "; |loop slope| / (quartic slope 4Q) =", float(Lp / (4 * Q)))
r = -sp.Rational(3, 4) * C / Q          # C/Q = -(2c/3)/chi = -(4/3) r,  r = c/(2 chi)
kap = 2 - 2 * r
print("  r = c/2chi =", float(r), " c/chi =", float(2 * r), " kappa = 2-c/chi =", float(kap))
VT = (1 - r) ** 2
print("  V/T -> (1-r)^2 =", float(VT), "; varrho=(V+2T)/3V =", float((VT + 2) / (3 * VT)),
      "; (V+2T)/(2V+T) =", float((VT + 2) / (2 * VT + 1)))
print("  chi-exchange part of q_*^2 over q_b^2: beta_K L'/(4 U4) =", float(beta * Lp / (4 * U4)))

print("\nB. identities (sympy)")
ab, chi, c, d = sp.symbols("abar chi c delta", positive=True)
Vt = ab * (chi**4 - sp.Rational(2, 3) * c * chi**3)
D = lambda f: sp.simplify(chi * sp.diff(f, chi))
rr = sp.symbols("r", positive=True)
V1 = sp.simplify(D(Vt).subs(c, 2 * rr * chi) / (4 * ab * chi**4)); V2 = sp.simplify(D(D(Vt)).subs(c, 2 * rr * chi) / (4 * ab * chi**4))
print("  V_t'/(4 abar chi^4) =", V1, ";  V_t''/(4 abar chi^4) =", V2)
b = sp.simplify(-2 * V1 / (V2 + d))
print("  beta_K = -2V_t'/(V_t''+U_loop'') = ", b, "  [delta = U_loop''/(4 abar chi^4 rho_M/g^2)]")
print("  beta_K = 1  <=>  r =", sp.solve(sp.Eq(b, 1), rr), " ; V/T = (1-r)^2 =", sp.simplify((1 - sp.solve(sp.Eq(b, 1), rr)[0])**2))
print("  r for the merged point from this formula, delta = loop''/(4Q):", float((6 + loop_cc / (4 * Q)) / 5))
print("  V=T needs r=0 or r=2; at r=2 beta_K =", sp.simplify(b.subs(rr, 2)), "and the l=1, j=0 vector mode is", "chi^2*(1*2+kappa*2) with kappa=-2 ->", 2 + (-2) * 2)
# elimination of chi in the (ln chi, sigma_1) form
A_, B_, E_, l_, s_ = sp.symbols("Ucc Lp U4 l s")
form = sp.Rational(1, 2) * A_ * l_**2 + B_ * l_ * s_ + E_ * s_**2
red = sp.simplify(form.subs(l_, sp.solve(sp.diff(form, l_), l_)[0]))
print("  1/2 Ucc l^2 + L' l s + U4 s^2, l eliminated:", sp.factor(red), " -> with beta=2L'/Ucc: (U4 - beta L'/4) s^2 ; check:",
      sp.simplify(red - (E_ - (2 * B_ / A_) * B_ / 4) * s_**2))

print("\nC. loop term with the cubic Hessian at the merged point (vartheta=1, chi^2=0.3, c=2 r chi), same units")
chis = np.sqrt(0.3); cc = 2 * float(r) * chis
def P(chi_, N, eps_phys):          # -chi^4 Uhat_reg(kappa(chi); eps*chi^2) / N^2
    k = 2 - cc / chi_
    return -chi_**4 * s2.Ureg(N, k, eps_phys * chi_**2) / N**2
print("     N    eps*chi^2*N^2   P (replaces U4=-0.09)   dP/dlnchi (replaces 4U4=-0.36)   P/(tree quartic 7.935)   slope/L'(5.34)")
for N in (16, 64, 512):
    for e in (0.5, 1e-2, 1e-4):
        ep = e / (chis**2 * N**2); h = 1e-4
        p0 = P(chis, N, ep); dp = (P(chis * np.exp(h), N, ep) - P(chis * np.exp(-h), N, ep)) / (2 * h)
        print(f"  {N:4d}    {e:7.0e}       {p0:14.3f}          {dp:14.3f}               {p0/7.935:10.2f}           {dp/5.34:10.2f}")
print("   check, c=0 in the same routine reproduces U4 = -x^2 = -0.09 (N=512):", end=" ")
cc_save = cc; cc = 0.0; print(f"{P(chis, 512, 1e-9):.5f}"); cc = cc_save
print("   W_R term of U_2 at leading order: -(2-3/4)(kappa^2-4) x N^2-units ->", -(2 - 0.75) * (float(kap)**2 - 4) * 0.3, " against the merged U_2 = -0.9")

print("\nD. tree mass term (mu^2/2) Tr X_i X_i on K: Hessian mu^2 on the three vector components only (chi=1, kappa=2)")
for N in (5, 40):
    for mu2 in (0.3, 1.7):
        sc, ve, sp_ = s2.towers(N, 2.0)
        w = np.array([a for a, _ in ve] + [-3 * a for a, _ in sc] + [-4 * a for a, _ in sp_] + [8 * a for a, _ in sc], float)
        lam = np.array([b + mu2 for _, b in ve] + [b for _, b in sc] + [b for _, b in sp_] + [b for _, b in sc], float)
        print(f"  N={N:3d} mu^2={mu2}: m0={np.sum(w):.1e}  m1={np.sum(w*lam):.4f} (3 mu^2 N^2 = {3*mu2*N*N:.4f})  "
              f"m2={np.sum(w*lam**2):.4f} (3mu^4N^2+3mu^2N^2(N^2-1) = {3*mu2**2*N*N+3*mu2*N*N*(N*N-1):.4f})")
print("  m1 != 0: int ds s^-2 (v - tau) (the weight W_R) is logarithmically divergent at small s; m2 != 0: so is the s^-3 integral beyond its power term.")
print("\nE. identity V/T = (L'/4Utilde)^2 on the quartic+cubic branch: (1-r)^2 with 1-r = V_t'/(4 abar chi^4) = -L'/(4 Utilde)")
print("  merged point: (L'/4Q)^2 with the merged L' and Q:", (5.34 / (4 * 7.935))**2, " vs (1-r)^2 =", float(VT))
