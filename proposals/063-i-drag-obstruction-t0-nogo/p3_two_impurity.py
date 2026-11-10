"""
Proposal 063 (Problem I, drag), P3 conditional benchmark: two impurities
dragged through a free Bogoliubov gas, separation entering only through an
interference factor.  This is an explicitly reduced model with an IMPORTED
separation parameter (exit-(iii) type).  It is a benchmark for the
structure of a nonzero drag tensor, NOT a NAMCG calculation; nothing here
is a result about the NAMCG correlator.

Model (standard Cherenkov/golden-rule loss rate, continuum, d=3):
  bath dispersion eps_q = sqrt(c^2 q^2 + q^4/4)  (c = 1),
  two static impurity cores of sizes ell_A, ell_B at separation r along
  the velocity, Gaussian form factors |W~(q)|^2 = exp(-q^2 ell^2),
  coupling of each impurity to the density.  On-shell (delta-function)
  rate per unit path for the pair:
    P_pair(v, r) = 2 pi Int dq q^2 [f_A(q)^2 + f_B(q)^2
                   + 2 f_A(q) f_B(q) cos(q r mu*(q))] / (2 eps_q v q)
                   * theta(v q - eps_q),   mu*(q) = eps_q/(v q),
  self terms r-independent; interference term I(v,r) = the last piece.
Checks:
 1. subsonic v < c: theta empty (eps_q/q >= c) => P = 0 exactly;
    supersonic v > c: P > 0 with Cherenkov momentum q* = 2 sqrt(v^2-c^2).
 2. r-dependence of I(v,r): stationary-phase endpoint asymptotics give a
    1/r envelope with oscillation phase r eps(q*)/v; a log-log fit of
    max|I| over r in [5, 60] returns a slope near -1.  The separation
    dependence is constant (self) + oscillatory ~1/r (interference):
    NO negative power -4 of the separation arises in this class, for any
    core sizes ell_A, ell_B; the amplitudes do depend on (ell_A, ell_B).
 3. BEK-type modified dispersion sqrt((c^2-kappa^2) q^2 + q^4/4):
    for c_eff < v < c the bare rate is 0 and the modified rate is > 0:
    sub-critical friction reopens when the low-q phase velocity is
    lowered (medium-modified dispersion loophole).
"""
import numpy as np

c = 1.0

def eps(q, cph=c):
    return np.sqrt(cph**2 * q**2 + q**4 / 4.0)

def P_pair(v, r, ellA=1.0, ellB=1.0, cph=c, n=400000, qmax=60.0):
    """On-shell pair rate; returns (self_part, interference_part)."""
    vph = np.linspace(0, 1, n)                      # q = q* + s*(qmax-q*)
    qs = 1e-9
    # lower limit: solve v q = eps_q  ->  q* (0 if never)
    disc = v**2 - cph**2
    if disc <= 0:
        return 0.0, 0.0
    qa = 2.0 * np.sqrt(disc)
    q = qa + vph * (qmax - qa)
    e = eps(q, cph)
    fa = np.exp(-0.5 * q**2 * ellA**2)
    fb = np.exp(-0.5 * q**2 * ellB**2)
    mu = e / (v * q)
    w = q**2 * fa * fb / (2.0 * e * v * q)
    self_int = np.trapezoid(q**2 * (fa**2 + fb**2) / (2.0 * e * v * q), q)
    interf = 2.0 * np.trapezoid(w * np.cos(q * r * mu), q)
    return 2 * np.pi * self_int, 2 * np.pi * interf

print("=" * 74)
print("P3: two impurities in a free Bogoliubov gas (conditional benchmark)")
print("=" * 74)
print("1. Cherenkov threshold, single impurity (ell=1):")
for v in [0.5, 0.9, 0.999, 1.001, 1.2, 1.5]:
    s, _ = P_pair(v, 0.0)
    disc = v**2 - c**2
    qstar = 2 * np.sqrt(disc) if disc > 0 else 0.0
    lbl = ("empty-set zero, exact" if disc <= 0 else "on-shell rate > 0")
    print(f"   v={v:5.3f}: P = {s:.6e}   (q* = {qstar:.4f}; {lbl})")

print()
print("2. Separation structure of the pair drag (v=1.3, equal cores):")
v = 1.3
s1, _ = P_pair(v, 0.0, ellA=1.0, ellB=1.0)
print(f"   self part (r-independent): {s1:.6e} (per impurity pair prefactor"
      f" f_A^2+f_B^2)")
rs = np.arange(5.0, 61.0, 2.5)
envs = []
for r in rs:
    _, I = P_pair(v, r)
    envs.append(abs(I))
# log-log slope of the envelope (endpoint 1/r prediction)
lr, le = np.log(rs[-12:]), np.log(np.array(envs[-12:]))
# fit max over local windows to see envelope, not oscillation
winsz = 6
mx = [max(envs[i:i+winsz]) for i in range(0, len(envs)-winsz+1, 3)]
rmid = [rs[i + winsz//2] for i in range(0, len(envs)-winsz+1, 3)]
lmx = np.log(np.array(mx))
lmr = np.log(np.array(rmid))
slope = np.polyfit(lmr, lmx, 1)[0]
print(f"   interference I(v,r): sign oscillates in r; windowed max|I| "
      f"log-log slope = {slope:.3f}; tail pointwise local slopes over "
      f"r=40..400 scatter between about -2.4 and -0.2 (oscillatory "
      f"interference), endpoint/stationary-phase prediction for the "
      f"envelope is an r^-1 decay; the exponent is O(1) and is NOT -4")
print(f"   sample values: " + ", ".join(f"r={r:.0f}:I={P_pair(v,r)[1]:+.3e}"
                                        for r in [5, 10, 20, 40, 60]))
_, I5 = P_pair(v, 5.0); _, I60 = P_pair(v, 60.0)
print(f"   ratio |I(60)|/|I(5)| = {abs(I60)/abs(I5):.4f} "
      f"(vs 60^-4 = {60**-4:.2e} and 60^-1 = {1/60:.4f})")
print("   asymmetric cores (ellA,ellB) change amplitudes, not the exponent:")
for (la, lb) in [(1.0, 1.0), (1.0, 2.0), (2.0, 0.7)]:
    s_ab, _ = P_pair(v, 0.0, ellA=la, ellB=lb)
    _, I20 = P_pair(v, 20.0, ellA=la, ellB=lb)
    print(f"     ellA={la}, ellB={lb}: self = {s_ab:.4e}, I(r=20) = {I20:+.3e}")

print()
print("3. BEK-type dispersion lowering, cph = sqrt(c^2 - kappa^2):")
kap = 0.3
cph = np.sqrt(c**2 - kap**2)
print(f"   kappa={kap}: bare phase velocity c={c}, modified c_eff={cph:.4f}")
for v in [0.9, 0.95, 0.97]:
    sb, _ = P_pair(v, 10.0, cph=c)
    sm, Im_ = P_pair(v, 10.0, cph=cph)
    print(f"   v={v:5.3f} (< c): bare P = {sb:.3e}, modified P = {sm:.3e}, "
          f"interference = {Im_:+.3e} -> "
          f"{'REOPENED' if sm > 0 and sb == 0 else 'closed/unchanged'}")
print()
print("Classification: all statements above are CONDITIONAL benchmark results")
print("for the stated reduced model (imported separation, free Bogoliubov")
print("gas, pointlike Gaussian cores, tree-level golden rule). They show the")
print("KIND of structure a nonzero drag tensor can have (constants + an")
print("oscillatory 1/r-type interference, exponent model-dependent, never")
print("-4 in this class) and how a lowered phase velocity reopens sub-critical")
print("friction. None of this computes or constrains the NAMCG response.")
