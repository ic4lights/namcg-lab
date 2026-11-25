# patch_r3_liftcongruence.py - check-side repair R3 for verify_r120.py (idempotent).
# probe_t5c.py (capture out-probe-t5c.txt) localized the residual T5c stall: each
# lift_from_B call on the generic symbolic brackets costs ~50 min (simplify_sym/polymat
# on 21100-entry star lists); the two lifts cost ~100 min while mats_eq costs 1 s.
# The lift is a deterministic program in the four bracket polynomials, so the exact
# statement L(Phi + s I) - L(Phi) = 0 follows from exact bracket equality (mats_eq,
# polynomial identity of the simplified 2x2 matrices) plus substitutivity of equality;
# additionally the two lifts are evaluated on 6 deterministic integer draws of the 44
# generic coefficient symbols (integer arithmetic: fast; a guard against a representation
# bug in the primary route, never able to mask a genuine failure because it uses the
# same substitutions on both lifts and the primary route is exact).
# Claim string and input class (generic quadratic Phi, linear A, numeric Theta) kept
# verbatim; T5c-teeth kept. Preserves superseded bytes as verify_r120-preR3.py.
import hashlib
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, "verify_r120.py")
PRE3 = os.path.join(HERE, "verify_r120-preR3.py")
PIN2 = "b71430a6ebf3"

NEW = """Bs1 = brackets_full(Phi_q, Asym, ThN, n)
Phi_q2 = madd(Phi_q, [((0, 0, 0, 0), sp.Symbol("ss", complex=True) * sp.eye(n))])
Bs2 = brackets_full(Phi_q2, Asym, ThN, n)
# Repair R3 (check-side, S2-final; verify_repair_log.txt): full generic-symbolic lift
# evaluation is intractable in this representation (probe_t5c.py, out-probe-t5c.txt:
# ~50 min per lift_from_B call on 21100-entry star lists). Since lift_from_B is a
# deterministic program in the four bracket polynomials, L(Phi + s I) = L(Phi) exactly
# follows from exact equality of the bracket polynomials (mats_eq: simplify of the
# difference of the 2x2 polynomial matrices == 0), plus substitutivity of equality.
# Six deterministic integer draws of the generic coefficient symbols additionally
# evaluate both lifts numerically with identical substitutions per draw. Claim string
# and input class (generic quadratic Phi, linear A, numeric Theta) unchanged.
eq_br = all(mats_eq(Ba, Bb, n) for Ba, Bb in zip(Bs1, Bs2))
DR = [-7, -3, 2, 5, 11, -13]
GENS = sorted({s for M in Pc + Asym for s in M.atoms(sp.Symbol)}, key=str)


def draw_reps(k):
    return {s: sp.Integer(DR[(i + k) % len(DR)]) for i, s in enumerate(GENS)}


def lift_at(Bs_raw, reps):
    Bs_sub = [[(e, C.xreplace(reps)) for e, C in B] for B in Bs_raw]
    return lift_from_B(Bs_sub, ThN, n)


ok_draws = True
for k in range(6):
    rp = draw_reps(k)
    ok_draws = ok_draws and (lift_at(Bs1, rp) == lift_at(Bs2, rp))
chk("T5c full star lift: L(Phi + s I) - L(Phi) = 0 exactly (quadratic Phi, linear A, numeric Theta)",
    eq_br and ok_draws)
Phi_q3 = madd(Phi_q, [((0, 0, 0, 0), sp.Symbol("snc", complex=True) * sp.diag(1, 0))])
Bs3 = brackets_full(Phi_q3, Asym, ThN, n)
chk("T5c-teeth: non-scalar constant shift changes the brackets (control: T5c non-vacuous)",
    not all(mats_eq(Ba, Bb, n) for Ba, Bb in zip(Bs1, Bs3)))
"""

cur = io.open(P, "rb").read()
sha = hashlib.sha1(cur).hexdigest()[:12]
if sha == PIN2:
    src = cur.decode("ascii")
    io.open(PRE3, "wb").write(cur)
    mode = "APPLIED"
else:
    src = io.open(PRE3, "rb").read().decode("ascii")
    mode = "VERIFY"
lines = src.splitlines(True)
ks = [i for i, l in enumerate(lines) if l.strip() == "Bs1 = brackets_full(Phi_q, Asym, ThN, n)"]
ke = [i for i, l in enumerate(lines)
      if l.strip() == "not all(mats_eq(Ba, Bb, n) for Ba, Bb in zip(Bs1, Bs3)))"]
assert len(ks) == 1 and len(ke) == 1 and ke[0] > ks[0], "anchors %d/%d" % (len(ks), len(ke))
newlines = [l + "\r\n" for l in NEW.split("\n") if l != ""]
out = "".join(lines[:ks[0]] + newlines + lines[ke[0] + 1:]).encode("ascii")
sha2 = hashlib.sha1(out).hexdigest()[:12]
if mode == "APPLIED":
    io.open(P, "wb").write(out)
else:
    assert sha2 == sha, "R3 re-derivation mismatch %s vs %s" % (sha2, sha)
s = out.decode("ascii")
assert s.count("Repair R3 (check-side, S2-final") == 1, "control: R3 block count"
assert s.count('chk("T5c full star lift: L(Phi + s I) - L(Phi) = 0 exactly (quadratic Phi, linear A, numeric Theta)"') == 1, "control: T5c claim string"
assert s.count("T5c-teeth") == 1, "control: tooth"
assert s.count("ok_draws") >= 4, "control: draws"
assert "lift_from_B(Bs1, ThN, n)" not in s and "lift_from_B(Bs2, ThN, n)" not in s, "control: old lifts"
import py_compile
py_compile.compile(P, doraise=True)
print("PATCH R3 %s: %d B -> %d B, new pin %s" % (mode, len(cur), len(out), sha2))
print("CONTROL OK 120R3")
