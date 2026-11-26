# extract_sources_088_r2.py -- folder-local copy of scratch/r2fix/extract_r2.py (byte-identical logic):
# writes scratch/r2fix/block2_corrected.txt + clause_f2.txt consumed by build_insert_088_r2.py. byte-extract gatekeeper-supplied corrected texts from review-r1.md
import hashlib, re, sys
R = "proposals/088-g-moments-stationarity-functional/review-r1.md"
raw = open(R, "rb").read()
t = raw.decode("utf-8")
# --- block 2: fenced code block between "Corrected block-2 sentences:" and "**F2"
i = t.index("Corrected block-2 sentences:")
j = t.index("**F2", i)
seg = t[i:j]
f1 = seg.index("```")
f2 = seg.index("```", f1+3)
inner = seg[f1+3:f2]
inner = inner.lstrip("\r\n").rstrip(" \r\n")
assert inner.startswith("This stationarity is rigid"), "block2 start assert FAIL"
assert inner.endswith("profile selector."), "block2 end assert FAIL"
assert "\n" not in inner.replace("\r",""), "block2 must be one line"
b2 = inner.replace("\r\n","\n").encode("utf-8")
open("scratch/r2fix/block2_corrected.txt","wb").write(b2)
print("block2 bytes=%d sha8=%s start=OK end=OK one-line=OK" % (len(b2), hashlib.sha256(b2).hexdigest()[:8]))
# --- F2 clause: quoted in "replace the clause with \"...\""
m = re.findall(r'replace the clause with "(while a relabelling-symmetric[^"]*selection input)"', t)
assert len(m) == 1, "F2 clause extract count=%d" % len(m)
cl = m[0].encode("utf-8")
open("scratch/r2fix/clause_f2.txt","wb").write(cl)
print("clause_f2 bytes=%d sha8=%s count=1" % (len(cl), hashlib.sha256(cl).hexdigest()[:8]))
