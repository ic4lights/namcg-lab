import hashlib
import os

ROOT = r"C:\Users\redgi\Projects\namcg-lab@gpu"
APPH = os.path.join(ROOT, "chapters", "appH-microscopic-proofs.tex")
INSE = os.path.join(ROOT, "proposals", "064-f-fibre-level-response-q0-trace", "insert-r1.tex")

PRE_BYTES = 578723
PRE_SHA = "5b5fc2650f05d95dce7fb7a4ed96ca282b946dbf7a3b3d2e368331b65638a631"
PRE_CRLF = 3433
PRE_BARELF = 0
SEP = b"\r\n\r\n"  # paragraph separator: 4 bytes = 2 CRLFs

def sha(b):
    return hashlib.sha256(b).hexdigest()

orig = open(APPH, "rb").read()
print("== pre-state certification (read-only) ==")
print("bytes:", len(orig), "match:", len(orig) == PRE_BYTES)
print("sha256:", sha(orig), "match:", sha(orig) == PRE_SHA)
crlf = orig.count(b"\r\n")
lf = orig.count(b"\n")
bare = lf - crlf
print("CRLF:", crlf, "match:", crlf == PRE_CRLF, "; bare LF:", bare, "match:", bare == PRE_BARELF)
assert len(orig) == PRE_BYTES and sha(orig) == PRE_SHA and crlf == PRE_CRLF and bare == PRE_BARELF

anchor = (b"and give no Cassini or Newtonian comparison. "
          b"Problems~C, F and~N remain open and PROGRAMME-CONDITIONAL.")
cnt = orig.count(anchor)
print("anchor count:", cnt)
assert cnt == 1
apos = orig.find(anchor)
print("anchor byte offset:", apos)
print("bytes before anchor (80):", orig[max(0, apos - 80):apos])
after = orig[apos + len(anchor): apos + len(anchor) + 60]
print("bytes after anchor (60):", after)
assert after.startswith(SEP)

ins = open(INSE, "rb").read()
print("== insert-r1.tex ==")
print("bytes:", len(ins), "sha256:", sha(ins))
assert ins.count(b"\r") == 0, "insert must be LF-only"
ins_body = ins
while ins_body.endswith(b"\n"):
    ins_body = ins_body[:-1]
ins_crlf = ins_body.replace(b"\n", b"\r\n")
print("insert LF newlines:", ins.count(b"\n"), "; after strip:", ins_crlf.count(b"\r\n"))

ins_pos = apos + len(anchor)
new = orig[:ins_pos] + SEP + ins_crlf + orig[ins_pos:]

print("== predicted post-state (simulation only; chapters/ NOT written) ==")
post_crlf = new.count(b"\r\n")
post_bare = new.count(b"\n") - post_crlf
print("post bytes:", len(new), "= 578723 + 4 +", len(ins_crlf), ":",
      len(new) == PRE_BYTES + len(SEP) + len(ins_crlf))
print("post sha256:", sha(new))
print("post CRLF:", post_crlf, "= 3433 + 2 +", ins_crlf.count(b"\r\n"), ":",
      post_crlf == PRE_CRLF + 2 + ins_crlf.count(b"\r\n"))
print("post bare LF:", post_bare, ":", post_bare == 0)
assert len(new) == PRE_BYTES + len(SEP) + len(ins_crlf)
assert post_bare == 0

print("== integrity of untouched regions ==")
assert new[:ins_pos] == orig[:ins_pos]
assert new[ins_pos + len(SEP) + len(ins_crlf):] == orig[ins_pos:]
mk = b"\\label{sec:status-F}"
i0 = orig.find(mk)
i1 = new.find(mk)
assert orig.count(mk) == new.count(mk) == 1
blk0 = orig[i0:i0 + 900]
blk1 = new[i1:i1 + 900]
print("status-F block byte-identical:", blk0 == blk1, "; block sha256:", sha(blk0))
assert blk0 == blk1
sp0 = orig[i0:i0 + 900].decode("utf-8", "replace")
import re
m = re.search(r"Status.*?Priority.*?Completion", sp0, re.S)
print("Status/Priority/Completion passage present and unchanged:", bool(m))

tail = new[new.find(b"\\section{Problem G: HBEV}") - 40: new.find(b"\\section{Problem G: HBEV}") + 30]
print("junction before Problem G section (bytes):", tail)
print("SIMULATION OK: pre-state certified, anchor unique, splice predicted, status passage unchanged")
