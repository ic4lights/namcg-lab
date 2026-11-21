# mk_insert_107_r2.py -- proposal 107 round 2: adopt the gatekeeper-corrected paragraph
# as insert-r2.tex WITHOUT retyping: reads scratch/gk107/insert-corrected-gk.tex as bytes
# and writes those EXACT bytes. Asserts the certified triple (2249 B / sha256-16
# d5eef9bbed7785d0 / exactly 1 CRLF-terminated line). Writes only inside the proposal folder.
import hashlib

SRC = r"scratch\gk107\insert-corrected-gk.tex"
DST = r"proposals\107-a-map-chart-condensate-selection\insert-r2.tex"
b = open(SRC, "rb").read()
print("source: %s %d bytes sha256/16 %s CRLF %d"
      % (SRC, len(b), hashlib.sha256(b).hexdigest()[:16], b.count(b"\r\n")))
assert len(b) == 2249, "source size changed: %d" % len(b)
assert hashlib.sha256(b).hexdigest()[:16] == "d5eef9bbed7785d0", "source sha changed"
assert b.count(b"\r\n") == 1 and b.endswith(b"\r\n"), "not exactly one CRLF-terminated line"
open(DST, "wb").write(b)
c = open(DST, "rb").read()
assert c == b, "byte-identity failed"
print("written: %s %d bytes sha256/16 %s CRLF %d"
      % (DST, len(c), hashlib.sha256(c).hexdigest()[:16], c.count(b"\r\n")))
print("CANDIDATE MATCH")
