"""049 s12: check R1 of review-r3.md, then apply it to the r3 insert.

Part 1 checks the mathematical content of R1 by sympy. Part 2 reads the old and new strings as raw text from
review-r3.md; neither is typed here. The source is the r3 insert: the archive appH_insert.r3.tex if present, otherwise
appH_insert.tex, which is then archived. CRLF in the source would be reported and normalised to LF before hashing. The
old string must occur exactly once, and the result must have the byte count and sha256 stated in the review and in the
task. On any mismatch the script exits without writing. Re-running it on the finished folder reproduces the same bytes."""
import hashlib
import os
import re
import sys

import sympy as sp

here = os.path.dirname(os.path.abspath(__file__))
SRC_SHA = "b19b4c9890f65a15f33ec0fb21bc5af957ad2e56617335ec3e7f3ff7d47e43e3"
SRC_LEN = 22769
OUT_SHA = "eba2c8ed7f120413377176df1da08adf4cd5e4d57458b07561ee5fedbd6fa256"
OUT_LEN = 22821


def sha(b):
    return hashlib.sha256(b).hexdigest()


def refuse(msg):
    print("REFUSED, nothing written:", msg)
    sys.exit(1)


print("Part 1: content of R1")
a, c = sp.symbols("a c", real=True)
th, D, cJ, s = sp.symbols("vartheta D c_J s", positive=True)
q = sp.Rational(15, 4) * a**2 - a * c + 2 * c**2
Q = sp.Matrix([[sp.Rational(15, 4), -sp.Rational(1, 2)], [-sp.Rational(1, 2), 2]])
if sp.expand((sp.Matrix([[a, c]]) * Q * sp.Matrix([a, c]))[0] - q) != 0:
    refuse("matrix does not represent the form")
print("  form (15/4)a^2 - a c + 2c^2, matrix", Q.tolist())
print("  leading minor", Q[0, 0], "> 0; determinant", Q.det(), "> 0; eigenvalues", [sp.nsimplify(e) for e in Q.eigenvals()])
if not (Q[0, 0] > 0 and Q.det() > 0 and Q.det() == sp.Rational(29, 4)):
    refuse("form is not positive definite")
print("  completed square:", sp.factor(sp.Rational(15, 4) * (a - sp.Rational(2, 15) * c) ** 2 + sp.Rational(29, 15) * c**2), "difference from form",
      sp.expand(sp.Rational(15, 4) * (a - sp.Rational(2, 15) * c) ** 2 + sp.Rational(29, 15) * c**2 - q))
bracket = sp.Rational(15, 4) * th**2 / D - th * cJ / D**2 + 2 * cJ**2 / D**3
residual = sp.simplify(bracket * D**3 - q.subs({a: th * D, c: cJ}))
print("  bracket times D^3 minus the form at a = vartheta D, c = c_J:", residual)
if residual != 0:
    refuse("bracket times D^3 is not the form")
proper_time = sp.integrate((sp.Rational(15, 4) * th**2 - s * th * cJ + s**2 * cJ**2) * sp.exp(-s * D), (s, 0, sp.oo))
print("  bracket from the proper-time integral of the printed average, residual:", sp.simplify(proper_time - bracket))
at_zero = sp.simplify(bracket.subs(cJ, 0))
print("  at J = 0 (c_J = 0) the bracket is", at_zero, "; form", sp.simplify(q.subs({a: th * D, c: 0})), "> 0 since a = vartheta D > 0")
print("  discriminant of the form in a, at c_J = 0:", sp.discriminant(q, a).subs(c, 0), "(so the old reason fails at J = 0; the new one does not use it)")

print("Part 2: application")
review = open(os.path.join(here, "review-r3.md"), "rb").read().decode("utf-8").replace("\r\n", "\n")
pairs = re.findall(r"^- \*\*R(\d)\.\*\* old: `([^`\n]*)`\n  new: `([^`\n]*)`$", review, flags=re.M)
if [p[0] for p in pairs] != ["1"]:
    refuse("parsed items %s, expected R1 only" % [p[0] for p in pairs])
_, old, new = pairs[0]
m = re.search(r"\*\*(\d+) bytes, sha256 ([0-9a-f]{64})\*\*", review)
if m is None or int(m.group(1)) != OUT_LEN or m.group(2) != OUT_SHA:
    refuse("review's stated result does not match the expected values")
print("review states", m.group(1), "bytes, sha256", m.group(2))

arch = os.path.join(here, "appH_insert.r3.tex")
cur = os.path.join(here, "appH_insert.tex")
src_path = arch if os.path.exists(arch) else cur
raw = open(src_path, "rb").read()
print("source", os.path.basename(src_path), len(raw), "bytes on disk, CR", raw.count(b"\r"))
if b"\r" in raw:
    print("source holds CR; normalising CRLF to LF before hashing")
src = raw.replace(b"\r\n", b"\n")
if len(src) != SRC_LEN or sha(src) != SRC_SHA:
    refuse("source %s is %d bytes, sha %s" % (os.path.basename(src_path), len(src), sha(src)))
print("source sha256", sha(src), "matches r3")

s_txt = src.decode("ascii")
n = s_txt.count(old)
print("R1: old occurs %d; old %d chars, new %d chars" % (n, len(old), len(new)))
if n != 1:
    refuse("R1 old string occurs %d times" % n)
out = s_txt.replace(old, new).encode("ascii")
print("result", len(out), "bytes, sha256", sha(out))
if len(out) != OUT_LEN or sha(out) != OUT_SHA:
    refuse("result differs from the expected %d bytes, sha %s" % (OUT_LEN, OUT_SHA))
print("matches the review's byte count and sha256")

if not os.path.exists(arch):
    with open(arch, "wb") as f:
        f.write(src)
    print("archived r3 bytes as appH_insert.r3.tex")
with open(cur, "wb") as f:
    f.write(out)
print("wrote appH_insert.tex; ASCII", all(b < 128 for b in out), "CR", out.count(b"\r"), "BOM", out[:3] == b"\xef\xbb\xbf")
