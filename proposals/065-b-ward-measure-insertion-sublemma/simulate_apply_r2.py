"""Proposal 065 (round 2): read-only simulation of the proposed appH splice (insert-r2.tex) and bib additions.

Asserts the certified pre-state of chapters/appH-microscopic-proofs.tex and
bib/namcg.bib, checks anchor uniqueness, applies the insert in memory only,
and reports the predicted post-states. Writes nothing outside this folder.
Run:  python -I simulate_apply_r2.py
"""
import hashlib
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
APPH = os.path.join(ROOT, "chapters", "appH-microscopic-proofs.tex")
BIB = os.path.join(ROOT, "bib", "namcg.bib")
INS = os.path.join(HERE, "insert-r2.tex")
BIBADD = os.path.join(HERE, "bib_additions.bib")

APPH_SIZE = 582706
APPH_SHA = "dd0bea7780757e51d9677d38130d0425dc38cd54538d85f14f26f23f97bdcf4a"
BIB_SIZE = 28038
BIB_SHA = "c71780a9d968f47076613cf9d2c9a3fc3370f2b24e015178d569b28fc28757aa"


def stats(b):
    crlf = b.count(b"\r\n")
    lf = b.count(b"\n") - crlf
    return len(b), crlf, lf, hashlib.sha256(b).hexdigest()


def show(tag, b):
    n, crlf, lf, sh = stats(b)
    print("%s: size=%d CRLF=%d bareLF=%d sha256=%s" % (tag, n, crlf, lf, sh))


print("== appH pre-state ==")
pre = io.open(APPH, "rb").read()
show("pre", pre)
assert len(pre) == APPH_SIZE, "appH size mismatch"
assert hashlib.sha256(pre).hexdigest() == APPH_SHA, "appH sha256 mismatch"
n, crlf, lf, _ = stats(pre)
assert crlf == 3435 and lf == 0, "appH line-ending profile mismatch"
print("pre-state matches certification (size, sha256, CRLF=3435, bareLF=0): OK")

anchor = b"\\section{Problem C: conformal mode and Cassini}"
cnt = pre.count(anchor)
print("anchor occurrences:", cnt)
assert cnt == 1, "anchor not unique"
start = pre.find(anchor)
assert pre[start - 2:start] == b"\r\n", "anchor not at line start"

ins_lf = io.open(INS, "rb").read()
assert b"\r" not in ins_lf, "insert contains CR"
assert b"\\label{" not in ins_lf, "insert contains \\label"
ins = ins_lf.replace(b"\n", b"\r\n")
assert ins.endswith(b"\r\n"), "insert must end with a line break"
print("insert bytes (LF form):", len(ins_lf))

post = pre[:start] + ins + pre[start:]
assert post[:start] == pre[:start] and post[start + len(ins):] == pre[start:]
print("only difference pre->post is the inserted block: OK")
print("== appH predicted post-state ==")
show("post", post)

# Status-B ledger window: bytes of the Problem B section head region unchanged.
head = b"\\section{Problem B"
assert pre.count(head) == 1, "Problem B header not unique"
i0 = pre.find(head)
win = pre[i0:i0 + 4000]
j0 = post.find(head)
assert pre[i0:i0 + 4000] == post[j0:j0 + 4000]
print("Status-B ledger window (4000 bytes from Problem B header) byte-unchanged: OK")

print()
print("== bib pre-state ==")
bib = io.open(BIB, "rb").read()
show("bib pre", bib)
assert len(bib) == BIB_SIZE, "bib size mismatch"
assert hashlib.sha256(bib).hexdigest() == BIB_SHA, "bib sha256 mismatch"
npre, _, _, _ = stats(bib)
nentries = bib.count(b"@")
print("bib entries (@ occurrences):", nentries)

adds = io.open(BIBADD, "rb").read()
assert b"\r" not in adds
addkeys = [line.split(b"{")[1].rstrip(b", ").decode() for line in adds.split(b"\n") if line.startswith(b"@")]
print("proposed keys:", addkeys)
for k in addkeys:
    assert b"{" + k.encode() + b"," not in bib, "key collision: " + k
assert len(set(addkeys)) == len(addkeys), "duplicate proposed keys"
print("no key collisions with current bib: OK")

bib_post = bib + b"\r\n" + adds.replace(b"\n", b"\r\n")
print("== bib predicted post-state (entries appended at EOF with CRLF) ==")
show("bib post", bib_post)
print("entries after append:", bib_post.count(b"@"))
