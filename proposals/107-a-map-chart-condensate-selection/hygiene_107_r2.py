# hygiene_107_r2.py -- checks insert-r2.tex of proposal 107 against the LIVE
# chapters/appH-microscopic-proofs.tex (106 hygiene conventions). Read-only.
import hashlib
import sys

F = r"proposals\107-a-map-chart-condensate-selection\insert-r2.tex"
A = r"chapters\appH-microscopic-proofs.tex"
ins = open(F, "rb").read()
app = open(A, "rb").read()
print("checked insert: %s %d bytes, sha256/16 %s"
      % (F, len(ins), hashlib.sha256(ins).hexdigest()[:16]))
ok = True

def chk(name, cond, extra=""):
    global ok
    print("%s: %s %s" % (name, "PASS" if cond else "FAIL", extra))
    ok = ok and cond

chk("single CRLF-terminated line", ins.endswith(b"\r\n") and ins.count(b"\r\n") == 1)
try:
    line = ins.decode("ascii").rstrip("\r\n")
    chk("ASCII", True)
except UnicodeDecodeError:
    line = ""
    chk("ASCII", False)
chk("line length 1500-2500 B", 1500 <= len(ins) <= 2500, "actual %d" % len(ins))
chk("ends with period", line.endswith("."))
for pat in [b"\\label", b"\\ref{", b"\\eqref", b"\\cite"]:
    chk("no " + pat.decode(), pat not in ins)
import re
chk("no hard-coded Chapter/Section numbers",
    not re.search(r"(Chapter|Section)~?\s*\d", line))
for word in ["CRITICAL", "PRIORITY", "Priority", "Priority:", "Completion",
             "MILESTONE", "OPEN"]:
    chk("no status word " + word, word not in line)
depth = 0
bal = True
for ch in line:
    if ch == "{":
        depth += 1
    elif ch == "}":
        depth -= 1
        if depth < 0:
            bal = False
            break
chk("braces balanced", bal and depth == 0, "final depth %d" % depth)
chk("count('does not close Problem~A') == 1",
    line.count("does not close Problem~A") == 1)
chk("derive-disclaimer count == 1",
    line.count("do not derive") + line.count("does not derive") == 1,
    "got %d" % (line.count("do not derive") + line.count("does not derive")))
appstr = app.decode("utf-8")
macros = ["\\Theta", "\\theta", "\\sigma", "\\sin", "\\le", "\\paragraph"]
present = [m for m in macros if m in appstr]
chk("all macros present in appH", len(present) == len(macros), str(present))
sent = b"does not close Problem~A."
tail = b"\paragraph{Missing step.}"
PIN = sent + b"\r\n\r\n" + tail
occ = [i for i in range(len(app)) if app.startswith(PIN, i)]
print("appH size %d sha256/16 %s CRLF %d ; PIN count %d"
      % (len(app), hashlib.sha256(app).hexdigest()[:16], app.count(b"\r\n"), len(occ)))
chk("PIN unique", len(occ) == 1)
print("HYGIENE:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
