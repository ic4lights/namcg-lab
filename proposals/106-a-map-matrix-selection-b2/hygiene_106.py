# hygiene_106.py -- checks insert-r1.tex against chapters/appH-microscopic-proofs.tex.
# Read-only; exits 0 iff all checks pass.
# Run from repo root: python -I proposals/106-a-map-matrix-selection-b2/hygiene_106.py
import hashlib
import re
import sys

F = r"proposals\106-a-map-matrix-selection-b2\insert-r2.tex"
A = r"chapters\appH-microscopic-proofs.tex"
ins = open(F, "rb").read()
print("checked insert:", F, len(ins), "bytes, sha256/16",
      hashlib.sha256(ins).hexdigest()[:16])
app = open(A, "rb").read()
appS = app.decode("utf-8")
fails = []

# 1. single CRLF-terminated line, ASCII only
if ins.count(b"\n") != 1 or not ins.endswith(b"\r\n"):
    fails.append("insert must be exactly one CRLF-terminated line")
if ins.count(b"\r") != 1 or b"\r" in ins.replace(b"\r\n", b""):
    fails.append("stray CR")
if any(c > 127 for c in ins):
    fails.append("non-ASCII byte")
line = ins.decode("ascii").rstrip("\r\n")

# 2. all macros already occur in appH
macros = sorted(set(re.findall(r"\\[A-Za-z]+", line)))
for m in macros:
    if m not in appS:
        fails.append("macro not present in appH: " + m)
print("macros used:", macros)

# 3. no new labels, no refs, no hard-coded chapter numbers
for bad in ("\\label", "\\ref", "\\eqref", "\\cite"):
    if bad in line:
        fails.append("forbidden command: " + bad)
if re.search(r"Chapter~?\s*\d", line):
    fails.append("hard-coded chapter number")

# 4. braces balanced (ignore escaped braces if any)
s = line.replace("\{", "").replace("\}", "")
depth = 0
for ch in s:
    if ch == "{":
        depth += 1
    elif ch == "}":
        depth -= 1
        if depth < 0:
            fails.append("unbalanced brace (extra })")
            break
if depth != 0 and not fails:
    fails.append("unbalanced braces (depth %d)" % depth)

# 5. exactly one scoped status sentence, one derive disclaimer, ends with period
n_close = line.count("does not close Problem~A")
if n_close != 1:
    fails.append("exactly one scoped status sentence required")
if line.count("do not derive") + line.count("does not derive") != 1:
    fails.append("status sentence count wrong")
if not line.rstrip().endswith("."):
    fails.append("line must end with a period")

# 6. anchor uniqueness in live appH (POST-integration-35 anchor: end of the integrated
#    order-Theta^2 dichotomy paragraph + blank line + Missing step)
pin = (b"does not close Problem~A."
       b"\r\n\r\n\paragraph{Missing step.}")
if app.count(pin) != 1:
    fails.append("PIN anchor count = %d (must be 1)" % app.count(pin))
print("appH size %d sha256/8 %s CRLF %d PIN count %d" %
      (len(app), hashlib.sha256(app).hexdigest()[:8], app.count(b"\r\n"),
       app.count(pin)))

print("HYGIENE:", "PASS" if not fails else "FAIL")
for f in fails:
    print(" -", f)
sys.exit(0 if not fails else 1)
