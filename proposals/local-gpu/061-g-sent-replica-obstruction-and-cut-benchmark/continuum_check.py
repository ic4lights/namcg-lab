"""Proposal 061 script 2: continuum-consistency checks for the quasi-free
cut-entropy benchmark (sympy + mpmath).

(i) continuum x-x correlator of the massive 1D free field used in script 1:
      C(r) = int dp/(2pi) e^{ipr}/(2 sqrt(p^2+mu^2)) = K0(mu r)/(2 pi),
    since int_0^inf cos(pr)/sqrt(p^2+mu^2) dp = K0(mu r). The integral is
    only conditionally convergent, so it is evaluated numerically in the
    once-integrated-by-parts form
      int_0^inf cos(pr)/sqrt(p^2+mu^2) dp
        = (1/r) int_0^inf sin(pr) p/(p^2+mu^2)^{3/2} dp      (abs. conv.),
    and the short-distance logarithm C(r) ~ -(1/2pi)(ln(mu r/2) + gamma)
    (the source of the log divergence behind the two-cut
    interval slope 1/3 in script halfline_r2.py) is checked numerically.
(ii) p-p block: D(r) = int dp/(2pi) e^{ipr} sqrt(p^2+mu^2)/2 is, for r>0,
    -C''(r) + mu^2 C(r) (since omega/2 = p^2/(2 omega) + mu^2/(2 omega));
    with C = K0(mu r)/(2pi) and the K0 ODE this gives
    D(r) = -mu K1(mu r)/(2 pi r), negative for r>0: the off-diagonal p-p
    correlator. Checked symbolically.
(iii) decoupled two-mode check: a quadratic kernel diagonal in the site
    basis (no coupling across the cut) has restricted symplectic spectrum
    {(1/2),(1/2)}: the free product sector carries no cut entropy; the
    entanglement is carried by kernel modes crossing the cut.
(iv) dimensional bookkeeping: [sigma Lambda^2] = 2 (area law on an area);
    [alpha_0 Lambda^3] = 3 (boundary 3-density of ass:Sent-density); the
    tube relation sigma Lambda^2 / w = alpha_0 Lambda^3 gives
    alpha_0 = sigma / (w Lambda), i.e. alpha_0 = sigma exactly when the
    tube width is w = Lambda^{-1} = Theta^{1/2} (the eq:LUV-def scale).
Symbolic/numerical output is a check, not a proof. Run:
python -I continuum_check.py
"""
import sympy as sp
import mpmath as mp

mu, r, p, z = sp.symbols('mu r p z', positive=True)

# ---------- (i) C(r) = K0(mu r)/(2 pi) ----------
print("(i) C(r) = int dp/(2pi) e^{ipr}/(2 sqrt(p^2+mu^2)) = K0(mu r)/(2 pi)")
print("    numeric check via int_0^inf sin(pr) p/(p^2+mu^2)^{3/2} dp / r:")
for (m, rr) in [(0.7, 0.3), (1.3, 2.1), (0.2, 7.5), (0.5, 15.0)]:
    val = mp.quad(lambda pp: mp.sin(pp*rr)*pp/(pp**2+m**2)**sp.Integer(3)/2
                  if False else mp.sin(pp*rr)*pp/(pp**2+m*m)**mp.mpf(3)/2,
                  [0, mp.inf]) / rr
    # (p^2+mu^2)^{3/2}:
    val = mp.quad(lambda pp: mp.sin(pp*rr)*pp/mp.power(pp**2+m*m, mp.mpf(3)/2),
                  [0, mp.inf]) / rr
    k0 = mp.besselk(0, m*rr)
    print(f"  mu={m} r={rr}: IBP integral={float(val):.10f} K0={float(k0):.10f} "
          f"diff={float(abs(val-k0)):.2e}  => C(r)={float(val/(2*mp.pi)):.10f}")
print("    small-r: C(r) + (1/2pi)(ln(mu r/2)+gamma) -> 0   [gamma = Euler constant]")
gam = mp.euler
for rr in (1e-1, 1e-2, 1e-3):
    m = 0.7
    Crr = mp.besselk(0, m*rr)/(2*mp.pi)
    combo = Crr + (mp.log(m*rr/2)+gam)/(2*mp.pi)
    print(f"  mu={m} r={rr}: combo={float(combo):.3e}")

# ---------- (ii) D(r) = -C'' + mu^2 C = -mu K1(mu r)/(2 pi r) ----------
print("(ii) D(r) = -d^2C/dr^2 + mu^2 C  with C = K0(mu r)/(2 pi):")
C = sp.besselk(0, mu*r)/(2*sp.pi)
Dexpr = sp.simplify(-sp.diff(C, r, 2) + mu**2*C)
print("    -C'' + mu^2 C =", Dexpr, " (negative for r>0, since K1>0)")

# ---------- (iii) decoupled two-mode check ----------
print("(iii) decoupled two-mode check (no kernel coupling across the cut):")
w1, w2 = sp.symbols('w1 w2', positive=True)
Cm = sp.diag(1/(2*w1), 1/(2*w2))
Dm = sp.diag(w1/2, w2/2)
CD = sp.simplify(Cm*Dm)
print("    C D =", CD, "eigenvalues:", CD.eigenvals(), "-> nu = 1/2, 1/2 -> s = 0")

# ---------- (iv) dimensional bookkeeping ----------
print("(iv) dimensional bookkeeping (mass dimension, [Lambda]=1):")
print("    area law: S/A_cut = sigma Lambda^2: [S/A_cut] = 2, [Lambda^2] = 2, [sigma] = 0;")
print("    sigma = O(10^-2) dimensionless in lattice units Lambda = pi (script 1, check 4).")
print("    ass:Sent-density form: alpha_0 Lambda^3 is a boundary 3-density, [.] = 3.")
w, Lambda, alpha0, sigma = sp.symbols('w Lambda alpha0 sigma', positive=True)
sol = sp.solve(sp.Eq(sigma*Lambda**2/w, alpha0*Lambda**3), alpha0)[0]
print("    sigma Lambda^2 / w = alpha_0 Lambda^3  ->  alpha_0 =", sp.simplify(sol))
print("    at w = 1/Lambda: alpha_0 =", sp.simplify(sol.subs(w, 1/Lambda)), "(= sigma)")
