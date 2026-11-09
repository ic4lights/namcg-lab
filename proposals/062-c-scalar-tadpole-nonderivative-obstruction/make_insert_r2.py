"""
Proposal 062 r2: build insert-r2.tex from insert-r1.tex by applying the
gatekeeper's Corrected snippet (review-r1.md) as a single byte-exact string
replacement in block 2 (the F block). Block 1 (the C block) must stay
byte-identical. Writes insert-r1-to-r2.diff recording the change.
insert-r1.tex is VOID for integration (retained for audit); insert-r2.tex is
the text to apply.
"""
import hashlib

def sha(b): return hashlib.sha256(b).hexdigest()

OLD = (r"Conversely the Yukawa threshold \(q_*^2=q_b^2\) at \(\hat U>0\) requires an uncancelled tadpole of size "
       r"\(|T|=\hat U\chi^2/(32\pi^2m^8)\) in the same convention. Second, taken alone and not cancelled, "
       r"\(U_4\) contributes \(\mathcal M=F\sqrt{|g|}\hat U\chi^4/256\pi^2\), of the sign that pulls \(q_*^2\) "
       r"positive for \(\hat U>0\), and \(q_*^2=6F\sqrt{|g|}\hat U\chi^4m^6/(\hat V+2\hat T)\); its ratio to "
       r"\(q_b^2\) is \(F\sqrt{|g|}\chi^2m^8/2\), and the comparison of magnitudes turns on the conventions for "
       r"\(m\), \(\vartheta\) and \(\sqrt{|g|}\) and is not settled here.")

NEW = (r"Conversely the Yukawa threshold \(q_*^2=q_b^2\) at \(\hat U>0\) requires an uncancelled tadpole of size "
       r"\(|T|=F\hat U\chi^4/(32\pi^2m^8)\) in the same convention. Second, taken alone and not cancelled, "
       r"\(U_4\) contributes \(\mathcal M=F\sqrt{|g|}\hat U\chi^4/256\pi^2\), of the sign that pulls \(q_*^2\) "
       r"positive for \(\hat U>0\), and \(q_*^2=6\sqrt{|g|}\hat U\chi^2m^6/(\hat V+2\hat T)\); its ratio to "
       r"\(q_b^2\) is \(\sqrt{|g|}m^8/2\), and the comparison of magnitudes turns on the conventions for "
       r"\(m\) and \(\sqrt{|g|}\) and is not settled here.")

raw1 = open("insert-r1.tex", "rb").read()
assert b"\r" not in raw1
parts = raw1.split(b"\n%---SPLIT---%\n")
assert len(parts) == 2
b1_old, b2_old = parts[0], parts[1]

assert raw1.count(OLD.encode("utf-8")) == 1, "OLD sentence occurrence count"
raw2 = raw1.replace(OLD.encode("utf-8"), NEW.encode("utf-8"))
parts2 = raw2.split(b"\n%---SPLIT---%\n")
assert len(parts2) == 2
b1_new, b2_new = parts2[0], parts2[1]

# block 1 must be byte-identical
assert b1_old == b1_new, "block 1 changed"
# block 2 diff is exactly the contiguous OLD->NEW replacement
assert b2_old == b2_new.replace(NEW.encode("utf-8"), OLD.encode("utf-8"))
pos = b2_old.find(OLD.encode("utf-8"))
assert pos != -1 and b2_old[pos:pos+len(OLD.encode("utf-8"))] == OLD.encode("utf-8")
# common prefix/suffix verification
common_pref = 0
while common_pref < len(b2_old) and common_pref < len(b2_new) and b2_old[common_pref] == b2_new[common_pref]:
    common_pref += 1
common_suf = 0
while (common_suf < len(b2_old) - pos and common_suf < len(b2_new) - pos
       and b2_old[-1-common_suf] == b2_new[-1-common_suf]):
    common_suf += 1
assert b2_old.count(OLD.encode("utf-8")) == 1 and b2_new.count(OLD.encode("utf-8")) == 0
assert b2_new.count(NEW.encode("utf-8")) == 1 and b2_old.count(NEW.encode("utf-8")) == 0
# common_pref/common_suf are informational (OLD and NEW share long prefix and suffix; the differing region of OLD is not contiguous)

open("insert-r2.tex", "wb").write(raw2)

lines = []
lines.append("insert-r1.tex -> insert-r2.tex  (proposal 062 r2; F1 correction)")
lines.append("insert-r1.tex is VOID for integration (retained for audit); insert-r2.tex is the text to apply.")
lines.append("")
lines.append("block 1 (C block): byte-identical, len %d -> %d, sha256 %s -> %s" % (
    len(b1_old), len(b1_new), sha(b1_old)[:16], sha(b1_new)[:16]))
lines.append("block 2 (F block): single contiguous replacement at offset %d (bytes %d..%d of block 2)," % (
    pos, pos, pos+len(OLD.encode("utf-8"))-1))
lines.append("  common prefix %d bytes, common suffix %d bytes, len %d -> %d, sha256 %s -> %s" % (
    common_pref, common_suf, len(b2_old), len(b2_new), sha(b2_old)[:16], sha(b2_new)[:16]))
lines.append("  split marker line unchanged; file LF-only in both.")
lines.append("")
lines.append("OLD (removed, %d bytes):" % len(OLD.encode("utf-8")))
lines.append(OLD)
lines.append("")
lines.append("NEW (inserted, %d bytes; gatekeeper Corrected snippet, review-r1.md):" % len(NEW.encode("utf-8")))
lines.append(NEW)
open("insert-r1-to-r2.diff", "wb").write(("\r\n".join(lines) + "\r\n").encode("utf-8"))

print("block 1 identical:", b1_old == b1_new, "| len", len(b1_old), "sha256", sha(b1_old))
print("block 2 old len", len(b2_old), "sha256", sha(b2_old))
print("block 2 new len", len(b2_new), "sha256", sha(b2_new))
print("block 2 new rstripped len", len(b2_new.rstrip(b"\n")), "sha256", sha(b2_new.rstrip(b"\n")))
print("replacement at offset", pos, "| only-region check passed; diff written to insert-r1-to-r2.diff")
print("insert-r2.tex written:", len(raw2), "bytes, sha256", sha(raw2))
