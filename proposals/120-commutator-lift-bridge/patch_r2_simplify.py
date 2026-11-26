# patch_r2_simplify.py - check-side repair R2 for verify_r120.py (idempotent).
# R1 alone did not suffice: the stall moved into simplify_sym's per-coefficient
# sp.simplify (was: "return [(e, sp.simplify(C)) for e, C in acc.items() if C != 0]").
# For the T5c class the coefficients are expanded polynomials in ~44 generic symbols with
# thousands of terms; sp.simplify runs heuristic cancellation/fraction analysis per
# coefficient and is the black hole (40+ min stall at the PASS T5b -> T5c gap after R1).
# Repair: drop that sp.simplify; coefficients enter already expanded (sp.expand(C) in the
# accumulation loop) and Add/Mul flattening plus the != 0 filters make the downstream
# equality tests canonical without heuristic simplification. No chk call, claim string,
# input class or comparison changes; the full run re-establishes all earlier PASSes.
# Combined audit re-derivation: re-verifies the R1 step from verify_r120-preR1.py
# (54ec6b20233b), so the gatekeeper needs this one script only.
import hashlib
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(HERE, "verify_r120.py")
PRE1 = os.path.join(HERE, "verify_r120-preR1.py")
PRE2 = os.path.join(HERE, "verify_r120-preR2.py")

PIN0 = "54ec6b20233b"
PIN1 = "610a2c6c7a32"

b1 = io.open(PRE1, "rb").read()
assert hashlib.sha1(b1).hexdigest()[:12] == PIN0, "preR1 pin mismatch"
cur = io.open(P, "rb").read()
shacur = hashlib.sha1(cur).hexdigest()[:12]

OLD_LINE = "    return [(e, sp.simplify(C)) for e, C in acc.items() if C != 0]\n"
NEW_LINE = ("    return [(e, C) for e, C in acc.items() if C != 0]  # Repair R2: "
            "coefficients are pre-expanded; heuristic simplify is the T5c black hole\n")


def to_r2(text):
    assert text.count(OLD_LINE) + text.count(OLD_LINE.replace("\n", "\r\n")) == 1, "target line not unique"
    return text.replace(OLD_LINE, NEW_LINE).replace(OLD_LINE.replace("\n", "\r\n"),
                                                    NEW_LINE.replace("\n", "\r\n"))


if shacur == PIN1:
    out = to_r2(cur.decode("ascii")).encode("ascii")
    io.open(PRE2, "wb").write(cur)
    io.open(P, "wb").write(out)
    mode = "APPLIED"
else:
    b2 = io.open(PRE2, "rb").read()
    assert hashlib.sha1(b2).hexdigest()[:12] == PIN1, "preR2 pin mismatch"
    out = to_r2(b2.decode("ascii")).encode("ascii")
    assert hashlib.sha1(out).hexdigest()[:12] == shacur, "current file does not re-derive from preR2"
    mode = "VERIFIED (idempotent)"
sha2 = hashlib.sha1(out).hexdigest()[:12]
print("PATCH R2 %s: base %d B -> %d B, new pin %s" % (mode, len(cur), len(out), sha2))
s = out.decode("ascii")
assert s.count("Repair R2: coefficients are pre-expanded") == 1, "control: R2 line wrong count"
assert "sp.simplify(C)) for e, C in acc.items()" not in s, "control: old simplify still present"
assert s.count("def simplify_sym") >= 1, "control: simplify_sym lost"
assert s.count("ALL CHECKS DONE 120") >= 1, "control: summary lost"
import py_compile
py_compile.compile(P, doraise=True)
print("CONTROL OK 120R2")
