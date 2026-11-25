# assemble_pr1.py - builds proposal-r1.md = pr1_partA.md + pr1_partB.md with placeholders
# substituted from live artifacts in this folder. Guards: all placeholders consumed, every
# clause-line group non-empty, zero FAIL lines in the capture, ASCII, CRLF-normalized, no BOM.
import hashlib
import io
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))


def rd(name):
    return io.open(os.path.join(HERE, name), "rb").read()


def sha12(b):
    return hashlib.sha1(b).hexdigest()[:12]


CAPT = os.environ.get("CAP120") or ("out-r120-rerun3.txt" if os.path.exists(os.path.join(HERE, "out-r120-rerun3.txt")) else "out-r120-rerun2.txt")
cap = rd(CAPT)
capl = cap.decode("ascii").splitlines()
total = [l for l in capl if l.startswith("TOTAL ")]
done = [l for l in capl if l.startswith("ALL CHECKS DONE 120")]
fails = [l for l in capl if l.startswith("FAIL ")]
assert len(total) == 1 and len(done) == 1, "capture lacks TOTAL/ALL DONE"
assert not fails, "capture has %d FAIL lines; do not assemble" % len(fails)


def lrep(pat):
    idx = [str(i + 1) for i, l in enumerate(capl) if re.match(pat, l)]
    assert idx, "no capture line for /%s/" % pat
    return ",".join(idx) if len(idx) <= 12 else "%s..%s" % (idx[0], idx[-1])


vals = {
    "<<PAYPIN>>": "%s/%d" % (sha12(rd("insert-commutator-lift-r1.tex")),
                             len(rd("insert-commutator-lift-r1.tex"))),
    "<<VERPIN>>": "%s/%d" % (sha12(rd("verify_r120.py")), len(rd("verify_r120.py"))),
    "<<R120PIN>>": sha12(cap),
    "<<R120SIZE>>": str(len(cap)),
    "<<TOTAL>>": total[0].strip(),
    "<<LINES-P>>": lrep(r"PASS P\d"),
    "<<LINES-T2>>": lrep(r"PASS T2"),
    "<<LINES-T3>>": lrep(r"PASS T3"),
    "<<LINES-T4>>": lrep(r"PASS T4"),
    "<<LINES-T5>>": lrep(r"PASS T5"),
    "<<LINES-T6>>": lrep(r"PASS T6"),
    "<<LINES-T7>>": lrep(r"PASS T7"),
}
A = rd("pr1_partA.md").decode("ascii")
B = rd("pr1_partB.md").decode("ascii")
assert "<<PAYPIN>>" in B and "<<LINES-T7>>" in B, "partB placeholders missing"
for k, v in vals.items():
    assert v and (k not in A), k
    B = B.replace(k, v)
assert not re.search(r"<<[A-Z0-9-]+>>", B), "unsubstituted placeholder remains"
full = A.rstrip("\r\n") + "\r\n\r\n" + B
full = full.replace("\r\n", "\n").replace("\n", "\r\n")
out = full.encode("ascii")
assert out[:3] != b"\xef\xbb\xbf" and b"\t" not in out
io.open(os.path.join(HERE, "proposal-r1.md"), "wb").write(out)
print("ASSEMBLE OK 120: proposal-r1.md %d B sha1[:12] %s" % (len(out), sha12(out)))
print("TOTAL line:", total[0].strip())
print("placeholders substituted:", len(vals))
