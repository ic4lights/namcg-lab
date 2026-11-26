# patch_r1_t5c.py - check-side repair R1 for verify_r120.py (T5c combinatorial stall).
# Idempotent: if verify_r120.py already carries the post-R1 pin 610a2c6c7a32, the script
# re-derives the patched bytes from verify_r120-preR1.py and re-checks (no rewrite).
# Replaces the 5-line T5c block (L1 = lift_full / Phi_q2 / L2 = lift_full / chk) by an
# exact-claim-equivalent unexpanded implementation plus a non-vacuity tooth.
# Guards: exactly one start line, exactly one end line, block length exactly 5;
# positive controls fire on wrong output.
import hashlib
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, "verify_r120.py")
OLD = os.path.join(HERE, "verify_r120-preR1.py")

PIN_OLD = "54ec6b20233b"
PIN_NEW = "610a2c6c7a32"

raw = io.open(P, "rb").read()
sha = hashlib.sha1(raw).hexdigest()[:12]
assert sha in (PIN_OLD, PIN_NEW), "pin mismatch %s, abort" % sha
if sha == PIN_NEW:
    src = io.open(OLD, "rb").read()
    assert hashlib.sha1(src).hexdigest()[:12] == PIN_OLD, "preR1 pin mismatch"
    rewrite = False
else:
    src = raw
    io.open(OLD, "wb").write(raw)
    rewrite = True

txt = src.decode("ascii")
lines = txt.splitlines(True)
start = [i for i, l in enumerate(lines) if l.strip() == "L1 = lift_full(Phi_q, Asym, ThN, n)"]
end = [i for i, l in enumerate(lines) if l.strip() == "sp.simplify(L2 - L1) == 0)"]
assert len(start) == 1 and len(end) == 1, "anchor counts %d/%d" % (len(start), len(end))
s, e = start[0], end[0]
assert e - s == 4, "block length %d not 5" % (e - s + 1)

NEW = """# Repair R1 (check-side, S2-final): the chunk-assembled T5c computed
# L1 = lift_full(...) and L2 = lift_full(...) and then sp.simplify(L2 - L1) on
# the fully EXPANDED difference: 16 truncated-star products of 2x2 matrices
# whose entries are quartic polynomials in 44 generic symbols; does not
# terminate in reasonable time (30+ min, 0-byte captures; blowup in
# sp.expand/Add). Rewrite verifies the IDENTICAL claim exactly: brackets
# compared exactly after simplify_sym, lift difference taken on the UNEXPANDED
# sums (identical unexpanded sums cancel in sympy Add without expand).
# Non-vacuity tooth added: a NON-scalar constant shift must change brackets.
# Claim string and inputs (generic quadratic Phi, linear A, numeric Theta) kept.
def brackets_full(Phi_list, Asym_, Th_, n_, Adeg=(1, 0, 0, 0)):
    Bs = []
    for mu in range(4):
        Xmu = xhat_sym(mu, Asym_, Th_, Adeg, n_)
        Bs.append(madd(star(Xmu, Phi_list, Th_), mmul_scalar(star(Phi_list, Xmu, Th_), -1)))
    return Bs


def lift_from_B(Bs, Th_, n_):
    tot = 0
    for mu in range(4):
        for nu in range(4):
            if g[mu, nu] == 0:
                continue
            Sb = star(Bs[mu], Bs[nu], Th_)
            tot = tot + (-sp.Rational(1, 2)) * g[mu, nu] * polymat(Sb, n_).trace()
    return tot


def mats_eq(Ba, Bb, n_):
    return sp.simplify(polymat(Ba, n_) - polymat(Bb, n_)) == sp.zeros(n_)


Bs1 = brackets_full(Phi_q, Asym, ThN, n)
Phi_q2 = madd(Phi_q, [((0, 0, 0, 0), sp.Symbol("ss", complex=True) * sp.eye(n))])
Bs2 = brackets_full(Phi_q2, Asym, ThN, n)
L1 = lift_from_B(Bs1, ThN, n)
L2 = lift_from_B(Bs2, ThN, n)
chk("T5c full star lift: L(Phi + s I) - L(Phi) = 0 exactly (quadratic Phi, linear A, numeric Theta)",
    all(mats_eq(Ba, Bb, n) for Ba, Bb in zip(Bs1, Bs2)) and (L2 == L1 or sp.simplify(L2 - L1) == 0))
Phi_q3 = madd(Phi_q, [((0, 0, 0, 0), sp.Symbol("snc", complex=True) * sp.diag(1, 0))])
Bs3 = brackets_full(Phi_q3, Asym, ThN, n)
chk("T5c-teeth: non-scalar constant shift changes the brackets (control: T5c non-vacuous)",
    not all(mats_eq(Ba, Bb, n) for Ba, Bb in zip(Bs1, Bs3)))
"""
newlines = [l + "\r\n" for l in NEW.split("\n") if l != ""]
out = "".join(lines[:s] + newlines + lines[e + 1:]).encode("ascii")
assert hashlib.sha1(out).hexdigest()[:12] == PIN_NEW, "output pin drifted: %s" % hashlib.sha1(out).hexdigest()[:12]
if rewrite:
    io.open(P, "wb").write(out)
print("PATCH R1 %s: old %d B -> new %d B" % ("VERIFIED (idempotent)" if not rewrite else "APPLIED", len(src), len(out)))
print("old sha1[:12]", PIN_OLD, " new sha1[:12]", PIN_NEW)
# positive controls on the post-patch text (fire if patch damaged the block)
assert out.decode("ascii").count("\nL1 = lift_full(Phi_q, Asym, ThN, n)\r\n") == 0, "control: old L1 line present"
assert out.decode("ascii").count("Bs1 = brackets_full(Phi_q, Asym, ThN, n)") == 1, "control: new Bs1 line wrong count"
assert out.decode("ascii").count("T5c-teeth") == 1, "control: tooth missing"
print("CONTROL OK 120R1")
