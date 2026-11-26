# hygiene_091_r2.py - r2 hygiene: same 24 checks as hygiene_091.py, pointed at insert-r2.tex.
# Run: python -I proposals/091-g-core-induced-pair-correlation/hygiene_091_r2.py
import hashlib
P = "proposals/091-g-core-induced-pair-correlation/insert-r2.tex"
A = "chapters/appH-microscopic-proofs.tex"
raw = open(P, "rb").read()
bad = []
def chk(name, cond):
    print(("OK  " if cond else "FAIL") + " " + name)
    if not cond:
        bad.append(name)
chk("size 3749", len(raw) == 3749)
chk("sha8 ecc2b239", hashlib.sha256(raw).hexdigest()[:8] == "ecc2b239")
chk("CRLF-only single line", raw.count(b"\r\n") == 1 and raw.count(b"\n") == 1)
try:
    raw.decode("ascii"); ok = True
except UnicodeDecodeError:
    ok = False
chk("ascii-only", ok)
low = raw.decode().lower()
for w in ["status", "priority", "completion", "open", "critical", "programme", "derived"]:
    chk("no-banned '" + w + "'", w not in low)
chk("emph==1", raw.count(b"\\emph") == 1)
chk("no-$", raw.count(b"$") == 0)
chk("no-brackets", raw.count(b"[") == 0 and raw.count(b"]") == 0)
for c in [b"\\cite", b"\\ref", b"\\eqref", b"\\label", b"\\ "]:
    chk("no-" + c.decode(), raw.count(c) == 0)
chk("paren-math balanced", raw.count(b"\\(") == raw.count(b"\\)"))
chk("close-idiom once", raw.count(b"close nothing in Problem~G.") == 1)
chk("F1 phrase deleted", raw.count(b"identically distributed complex entries") == 0)
chk("A-block iid kept", raw.count(b"independent identically distributed complex gaussians") == 1)
app = open(A, "rb").read()
chk("appH verb-form count 1", app.count(b"closes nothing in Problem~G.") == 1)
chk("appH noun-form total 16", app.count(b"close nothing in Problem~G.") == 16)
chk("appH Vacuum-term 2", app.count(b"\\emph{Vacuum term.}") == 2)
chk("appH header absent", app.count(b"Eigenvalue reduction of the edge Gram") == 0)
print("HYGIENE 091 R2:", "PASS" if not bad else "FAIL " + str(bad))
