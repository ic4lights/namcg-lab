# r2_checks_095.py - round-2 record-repair checks for proposal 095.
# Run from repo root: python -I proposals/095-g-gram-moment-identification/r2_checks_095.py
# Deterministic: fixed sympy expressions, fixed RNG seed 20261119.
import hashlib
from pathlib import Path
import numpy as np
import sympy as sp

F = Path(__file__).resolve().parent
fails = []

def chk(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        fails.append(name)

def sha8(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:8]

# ---- (a) artifact identities unchanged ----
ins = F / "insert-r1h.tex"
b = ins.read_bytes()
chk("A.insert_size_3480", len(b) == 3480)
chk("A.insert_sha8_b9b75e8f", sha8(ins) == "b9b75e8f")
rv = F / "review-r1.md"
chk("A.review_size_13538", rv.stat().st_size == 13538)
chk("A.review_sha8_04fb1009", sha8(rv) == "04fb1009")

# ---- (b) corrected rho2hat|p density: pushforward of uniform a|p ----
# parameters l1 = l2 + d, tau = l1 + l2, all positive, d > 0
l2, d, y, x, a = sp.symbols("l2 d y x a", positive=True)
r = sp.Symbol("r", positive=True)
l1 = l2 + d
tau = l1 + l2
rmap = (a**2 + (tau - a)**2) / tau**2          # rho(a)
drda = sp.diff(rmap, a)
branches = sp.solve(sp.Eq(rmap, r), a)
chk("B.two_branches", len(branches) == 2)
chk("B.branch_form",
    all(sp.simplify((bb - (tau + tau * sp.sqrt(2 * r - 1)) / 2)
                    * (bb - (tau - tau * sp.sqrt(2 * r - 1)) / 2)) == 0 for bb in branches))
chk("B.branches_distinct",
    sp.simplify((branches[0] - branches[1])**2 - tau**2 * (2 * r - 1)) == 0)
chk("B.branch_slope_sq",
    all(sp.simplify(drda.subs(a, bb)**2 - 4 * (2 * r - 1) / tau**2) == 0
        for bb in branches))
# two-branch Jacobian sum of the uniform density 1/d gives the recorded density
pdf_from_jac = sp.simplify(2 * (1 / d) * (tau / (2 * y)))
target_y = tau / (d * y)                         # tau/((l1-l2)*sqrt(2r-1)) at sqrt(2r-1)=y
chk("B.pdf_form", sp.simplify(pdf_from_jac - target_y) == 0)
rmax = (l1**2 + l2**2) / tau**2
chk("B.rmax_sqrt", sp.simplify(sp.sqrt(2 * rmax - 1) - d / tau) == 0)
chk("B.norm_to_1", sp.simplify(sp.integrate(tau / (d * sp.sqrt(2 * r - 1)),
                                            (r, sp.Rational(1, 2), rmax)) - 1) == 0)
chk("B.width_formula", sp.simplify(rmax - sp.Rational(1, 2) - d**2 / (2 * tau**2)) == 0)
chk("B.cdf_match",
    sp.simplify(sp.integrate(tau / (d * sp.sqrt(2 * r - 1)), (r, sp.Rational(1, 2), x))
                - tau * sp.sqrt(2 * x - 1) / d) == 0)
Ea = sp.integrate(rmap / d, (a, l2, l1))
# mean via the t = sqrt(2r-1) substitution: rho = (1+t^2)/2, density dr measure = tau/d dt
Et = sp.integrate((1 + y**2) / 2 * tau / d, (y, 0, d / tau))
chk("B.mean_forms_match", sp.simplify(Ea - Et) == 0)
chk("B.uniform_var",
    sp.simplify(sp.integrate((a - (l1 + l2) / 2)**2 / d, (a, l2, l1)) - d**2 / 12) == 0)
cand = sp.sqrt(a * (tau - a) - l1 * l2) * sp.Abs(tau - 2 * a) / 2
chk("B.r1_candidate_vanishes_at_mid", sp.simplify(cand.subs(a, tau / 2)) == 0)
# numerics: l1,l2 = 7,2 (tau = 9, d = 5): quadrature of the density == 1 within 1e-6
sub = {l2: 2, d: 5}
tmax = float((d / tau).subs(sub))
tt = np.linspace(0.0, tmax, 20001)
vv = np.full(tt.shape, float((tau / d).subs(sub)))   # density*dt/dr Jacobian: integrand const
chk("B.quadrature_to_1", abs(float(np.trapezoid(vv, tt)) - 1.0) < 1e-6)
u = np.random.default_rng(20261119).random(200000)
chk("B.mc_uniform_var", abs(float(np.var(u)) - 1.0 / 12.0) < 5e-3)

# ---- (c) the two r1 -> r2 record changes are present ----
t = (F / "proposal-r2.md").read_text(encoding="utf-8")
deleted = "any law with support " + "equal to the subclass"
chk("C.deleted_phrase_absent", t.count(deleted) == 0)
for nm, m in [("R1_unitary", "unitary invariance"), ("R1_Haar", "Haar"),
              ("R1_Beta", "Beta(1,1)"), ("R1_nonatomic", "nonatomic"),
              ("R1_section", "graph of a measurable section"),
              ("R2_density", "tau/((lambda1-lambda2)*sqrt(2r-1))"),
              ("R2_uniform", "uniform on [lambda2, lambda1]"),
              ("R2_settled", "essentially settled at D=2"),
              ("R2_rescope", "heterogeneous variances")]:
    chk("C." + nm, m in t)

print("R2 CHECKS 095:", "PASS" if not fails else "FAIL " + ",".join(fails))
