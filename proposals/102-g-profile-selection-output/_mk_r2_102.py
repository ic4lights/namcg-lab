# _mk_r2_102.py -- transient: build insert-r2.tex as byte-copy of insert-r1.tex with the
# single gatekeeper-mandated clause replacement (review-r1 "Corrected snippet"). Deleted after use.
import hashlib
import os

FOLDER = os.path.dirname(os.path.abspath(__file__))
OLD = os.path.join(FOLDER, "insert-r1.tex")
NEW = os.path.join(FOLDER, "insert-r2.tex")

b = open(OLD, "rb").read()
assert len(b) == 3155 and hashlib.sha256(b).hexdigest()[:8] == "654284b4", "insert-r1 identity"

CLAUSE_OLD = b"so \\(s_{2}\\to0\\) in \\(L^{2}\\) at rate \\(D^{-3/2}\\)"
CLAUSE_NEW = b"so \\(s_{2}-\\mathbb{E}\\,s_{2}\\to0\\) in \\(L^{2}\\) at rate \\(D^{-3/2}\\)"
assert b.count(CLAUSE_OLD) == 1, "old clause count != 1"
c = b.replace(CLAUSE_OLD, CLAUSE_NEW)
# r2 note: review-r1 states the added clause is 13 bytes / expected insert 3168 B; the
# mandated clause pair actually differs by 18 bytes (`-\mathbb{E}\,s_{2}` = 18 ASCII bytes),
# so the verbatim replacement gives 3173 B. The verbatim clause governs; byte counts are measured.
assert len(c) == len(b) + (len(CLAUSE_NEW) - len(CLAUSE_OLD)) == 3173, "byte arithmetic: got %d" % len(c)
assert c.count(CLAUSE_NEW) == 1
assert c.endswith(b"\r\n") and c.count(b"\r\n") == 1 and c.count(b"\n") == 1, "one CRLF-terminated line"
assert b"\xef\xbb\xbf" not in c[:3]
assert all(x < 128 for x in c), "ASCII-only"

open(NEW, "wb").write(c)
print("insert-r2.tex bytes =", len(c))
print("insert-r2.tex sha8  =", hashlib.sha256(c).hexdigest()[:8])
print("MK R2 PASS")
