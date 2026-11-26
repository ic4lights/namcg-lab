# simulate_apply_098.py - splices insert-r1.tex into appH in memory only; asserts; no writes.
# Run from repo root: python -I proposals/098-g-scalar-p2-nonbridge-d3/simulate_apply_098.py
import hashlib
APP = "chapters/appH-microscopic-proofs.tex"
INS = "proposals/098-g-scalar-p2-nonbridge-d3/insert-r1.tex"
app = open(APP, "rb").read()
ins = open(INS, "rb").read()

PRE_SHA = "691af35303cf46fadcb38b9e0f4a455a54e14fa65adf5e553c0e8839fdfc6e41"
assert len(app) == 786170, "PRE size moved"
assert hashlib.sha256(app).hexdigest() == PRE_SHA, "PRE sha moved"
assert app.count(b"\r\n") == 3858 and app.count(b"\n") == 3858, "PRE EOL moved"
IDIOM = b"they close nothing in Problem~G."
assert app.count(IDIOM) == 23, "PRE idiom moved"

# PIN: 097-paragraph tail (648 B) + CRLFCRLF + line-initial Vacuum header.
# The tail head shares its first 114 bytes with the 096 tail head: uniqueness is asserted on the
# FULL 648-B tail and the compound, never on the head alone.
head = (b"These statements are exact linear-algebraic and measure-theoretic identifiability statements"
        b" on the support of the named column-profile law for every strictly positive non-constant profile at every")
assert app.count(head) == 1, "097-tail head not unique"
idx = app.find(head)
assert idx == 748701, "PIN offset moved"
tail = app[idx:idx + 648]
assert tail.endswith(IDIOM), "tail does not end at idiom"
vac = b"\\emph{Vacuum term.}"
assert app.count(tail + b"\r\n\r\n" + vac) == 1, "compound PIN not unique"
cut = idx + 648 + 4
assert cut == 749353, "cut moved"

post = app[:cut] + ins + b"\r\n" + app[cut:]
h = hashlib.sha256(post).hexdigest()
print("POST bytes %d sha256 %s" % (len(post), h))
print("POST CRLF %d bareLF %d" % (post.count(b"\r\n"), post.count(b"\n") - post.count(b"\r\n")))
assert len(post) == 786170 + len(ins) + 2, "POST arithmetic"
assert post.count(b"\r\n") == 3860 and post.count(b"\n") - post.count(b"\r\n") == 0, "POST EOL"
assert post.count(IDIOM) == 24, "POST idiom 23->24"
assert post.count(b"closes nothing") == 1, "verb form still 1"
assert post.count(vac) == 2, "Vacuum header twice"
hdr_full = ins[: ins.find(b".} ") + 2]
assert post.count(hdr_full) == 1, "insert header once in POST"
j = post.find(hdr_full)
seg = post[idx: j]

assert seg == tail + b"\r\n\r\n", "seam before insert exact"
seg2 = post[j + len(ins) - 2: j + len(ins) + 2]
assert seg2 == b"\r\n\r\n", "seam after insert exact (blank line to Vacuum)"
# insert lands strictly between the 097 tail and the Vacuum paragraph
assert idx < j < post.find(vac, cut), "insert placed before Vacuum"
print("SUMMARY ALL PASS")
raise SystemExit(0)
