# simulate_apply_097.py - splices insert-r2.tex into appH in memory only; asserts; no writes.
# Run: python -I proposals/097-g-nonbridge-hetero-variance/simulate_apply_097.py   (repo root)
import hashlib

BS = chr(92)
APP = "chapters/appH-microscopic-proofs.tex"
INS = "proposals/097-g-nonbridge-hetero-variance/insert-r2.tex"
app = open(APP, "rb").read()
ins = open(INS, "rb").read()

PRE_SHA = "0e4c097b078e020bcf8165bf6b78680ea8b0d40ca0369361ddb3b9efec3aed5b"
assert len(app) == 780748, "PRE size moved"
assert hashlib.sha256(app).hexdigest() == PRE_SHA, "PRE sha moved"
assert app.count(b"\r\n") == 3856 and app.count(b"\n") == 3856, "PRE EOL moved"
IDIOM = b"they close nothing in Problem~G."
pre_idiom = app.count(IDIOM)
assert pre_idiom == 22, "PRE idiom count moved: %d" % pre_idiom

# PIN: 096-paragraph tail (538 B) + CRLFCRLF + line-initial Vacuum header
start = b"These statements are exact linear-algebraic and measure-theoretic identifiability statements on the support of"
assert app.count(start) == 1, "PIN start not unique"
idx = app.find(start)
tail = app[idx:idx + 538]
assert tail.startswith(start) and tail.endswith(IDIOM), "PIN tail wrong"
vac = b"\\emph{Vacuum term.}"
pattern = tail + b"\r\n\r\n" + vac
assert app.count(pattern) == 1, "PIN+CRLF+CRLF+Vacuum not unique"
cut = idx + 538 + 4

post = app[:cut] + ins + b"\r\n" + app[cut:]
h = hashlib.sha256(post).hexdigest()
print("POST bytes %d sha256 %s" % (len(post), h))
print("POST CRLF %d bareLF %d" % (post.count(b"\r\n"), post.count(b"\n") - post.count(b"\r\n")))
assert len(post) == 780748 + len(ins) + 2, "POST arithmetic"
assert len(post) == 786170 and len(ins) == 5420, "insert/POST sizes"
assert post.count(b"\r\n") == 3858 and post.count(b"\n") - post.count(b"\r\n") == 0, "POST EOL"
assert post.count(IDIOM) == 23, "POST idiom 22->23"
assert post.count(b"closes nothing") == 1, "verb form still 1"
assert post.count(vac) == 2, "Vacuum header twice"
header = ins.split(b" ")[0] + b" " + ins.split(b" ")[1]  # \emph{Non-identifiability of...
hdr_full = ins[: ins.find(b".} ") + 2]
assert post.count(hdr_full) == 1, "insert header once in POST"
# insert lands between the 096 tail and the Vacuum paragraph
j = post.find(hdr_full)
assert j > idx and post[j:].find(vac) < j + len(ins) + 600 - (j - idx), "insert placed before Vacuum"
seg = post[idx: j]
assert seg == tail + b"\r\n\r\n", "seam before insert exact"
seg2 = post[j + len(ins) - 2: j + len(ins) + 2]
assert seg2 == b"\r\n\r\n", "seam after insert exact (blank line to Vacuum)"
print("SUMMARY ALL PASS")
raise SystemExit(0)
