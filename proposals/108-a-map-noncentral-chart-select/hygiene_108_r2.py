# hygiene_108_r2.py -- self-contained hygiene battery for insert-r2.tex.
# Reads only the file it checks (argument 1, default insert-r2.tex in cwd);
# writes nothing. Run:  python -I hygiene_108_r2.py insert-r2.tex
import io, sys, hashlib

fname = sys.argv[1] if len(sys.argv) > 1 else "insert-r2.tex"
data = io.open(fname, "rb").read()
res = []
def chk(n, name, ok, inv=""):
    res.append((n, name, bool(ok)))
    print("H%02d [%s]: %s%s" % (n, name, "PASS" if ok else "FAIL", (" | " + inv) if inv else ""))

crlf = data.count(b"\r\n")
lf = data.count(b"\n")
chk(1, "exactly-one-CRLF", crlf == 1, "CRLF=%d" % crlf)
chk(2, "no-bare-LF", lf == crlf, "LF=%d" % lf)
chk(3, "no-tabs", b"\t" not in data)
chk(4, "no-ampersand", b"&" not in data)
chk(5, "no-lt-gt", b"<" not in data and b">" not in data)
chk(6, "pure-ascii", all(b < 128 for b in data))
chk(7, "no-BOM", not data.startswith(b"\xef\xbb\xbf"))
txt = data.decode("utf-8")
chk(8, "balanced-braces", txt.count("{") == txt.count("}"), "open=%d close=%d" % (txt.count("{"), txt.count("}")))
chk(9, "balanced-inline-math", txt.count(r"\(") == txt.count(r"\)"), r"\(=%d \)=%d" % (txt.count(r"\("), txt.count(r"\)")))
chk(10, "no-display-math", r"\[" not in txt and r"\]" not in txt)
chk(11, "no-refs-or-cites-or-labels", all(t not in txt for t in (r"\ref", r"\eqref", r"\cite", r"\label")))
low = txt
forbidden_status = ["Status:", "OPEN", "CRITICAL", "PROGRAMME", "DERIVED", "PRIORITY", "Priority"]
chk(12, "no-status-words", all(t not in low for t in forbidden_status))
proc = ["researcher", "proposal", "gatekeeper", "integrator", "round 1", "TODO", "TBD",
        "as proposed", "we show", "we prove", "our earlier"]
chk(13, "no-process-language", all(t not in low for t in proc))
chk(14, "starts-with-paragraph", txt.startswith(r"\paragraph{"))
chk(15, "ends-with-closing-dot", txt.rstrip("\r\n").endswith("does not close Problem~A."))
chk(16, "single-negative-closing", txt.count("does not close Problem~A.") == 1)
chk(17, "problem-A-tilde-form", "Problem~A" in txt and "Problem A" not in txt)
chk(18, "no-HTML-entities", all(t not in txt for t in ("&amp;", "&gt;", "&lt;", "gt;", "lt;")))
chk(19, "paragraph-title-present", txt.startswith(r"\paragraph{Scalarity dichotomy"))
chk(20, "size-in-band", 1500 <= len(data) <= 4000, "bytes=%d" % len(data))
chk(21, "checked-file-recorded", True, "file=%s sha256/16=%s" % (fname, hashlib.sha256(data).hexdigest()[:16]))

np_ = sum(1 for r in res if r[2])
print("HYGIENE TOTALS: PASS %d/%d FAIL %d" % (np_, len(res), len(res) - np_))
raise SystemExit(0 if np_ == len(res) else 1)
