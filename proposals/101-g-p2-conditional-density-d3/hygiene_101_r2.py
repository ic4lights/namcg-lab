# hygiene_101_r2.py -- item 101 round 2: contract checks on insert-r2.tex and the LIVE chapters/appH
# bytes (read-only). Run: python -I hygiene_101_r2.py   (expect ALL PASS)
import hashlib, sys
ok = True
def chk(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name); ok = ok and cond
ins = open("insert-r2.tex", "rb").read()
chk("ins is ASCII", all(c < 128 for c in ins))
chk("ins has no tabs", b"\t" not in ins)
chk("ins single terminal CRLF, no double CRLF", ins.count(b"\r\n") == 1 and ins.endswith(b"\r\n") and b"\r\n\r\n" not in ins)
chk("ins no bare LF", ins.count(b"\n") == ins.count(b"\r\n"))
chk("ins has no literal square brackets", b"[" not in ins and b"]" not in ins)
chk("ins one idiom tail", ins.count(b"close nothing in Problem~G.") == 1 and ins.endswith(b"and close nothing in Problem~G.\r\n"))
chk("ins header present", ins.startswith(b"\\emph{Exact conditional diagonal law at D=3.}"))
chk("ins no \\ref/\\cite", b"\\ref" not in ins and b"\\cite" not in ins)
chk("ins forbidden words absent", not any(w in ins for w in [b"closes", b"CRITICAL", b"OPEN", b"DERIVED", b"PROGRAMME", b"priority"]))
body = ins.rstrip(b"\r\n").decode("ascii")
chk("ins brace balance", body.count("{") == body.count("}"))
chk("ins bigl=bigr", body.count("\\bigl(") == body.count("\\bigr)"))
chk("ins dollar count even", body.count("$") % 2 == 0)
chk("ins r2 markers", ins.count(b"\\operatorname{diag}(\\lambda)") == 1 and ins.count(b"$G/\\tau$") == 1)
chk("ins r2 HCIZ numerator 2", ins.count(b"integral $2\\det\\bigl(e^{t_{i}\\lambda_{j}}\\bigr)_{1\\le i,j\\le3}/\\bigl(\\Delta(t)\\Delta(\\lambda)\\bigr)$ at $t=(t_{1},t_{2},0)$") == 1)
chk("ins Vandermonde defined", ins.count(b"where $\\Delta(x)=\\prod_{i<j}(x_{i}-x_{j})$ denotes the Vandermonde product") == 1)
chk("ins no r1 stale HCIZ", ins.count(b"\\bigl(2\\,\\Delta(a)") == 0 and ins.count(b"at $a=(s_{1},s_{2},0)$") == 0)
chk("ins length 2848", len(ins) == 2848)
b = open("../../chapters/appH-microscopic-proofs.tex", "rb").read()
chk("appH size 795607", len(b) == 795607)
chk("appH sha256 prefix 3f1b030c", hashlib.sha256(b).hexdigest().startswith("3f1b030c"))
chk("appH idiom 26", b.count(b"close nothing in Problem~G.") == 26)
chk("appH Vacuum term 2", b.count(b"\\emph{Vacuum term.}") == 2)
chk("appH CRLF 3864, bareLF 0", b.count(b"\r\n") == 3864 and b.count(b"\n") == b.count(b"\r\n"))
anch = b"close nothing in Problem~G.\r\n\r\n\\emph{Vacuum term.}"
chk("anchor unique", b.count(anch) == 1)
chk("header new in appH", b.count(b"\\emph{Exact conditional diagonal law at D=3.}") == 0)
print("ALL PASS" if ok else "HYGIENE FAILURES PRESENT"); sys.exit(0 if ok else 1)
