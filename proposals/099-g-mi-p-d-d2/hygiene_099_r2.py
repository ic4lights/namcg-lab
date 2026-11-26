# hygiene_099_r2.py -- live-file contract and anchor hygiene for item 099 round 2 (read-only).
# Adapted from hygiene_099b.py: insert pins updated to the round-2 bytes (1656 B, sha256 aa19ac66...), plus a
# new bare-`u` token check (round-1 blocking finding). Live-appH PIN probes (tail, offsets, counts) unchanged.
# SUPERSEDES hygiene_099b.py. Run from repo root:  python -I proposals/099-g-mi-p-d-d2/hygiene_099_r2.py
import hashlib, re, glob
FAIL = []
def chk(tag, cond, info=""):
    print(("PASS " if cond else "FAIL ") + tag + "  " + info, flush=True)
    if not cond: FAIL.append(tag)
APP = "chapters/appH-microscopic-proofs.tex"
d = open(APP, "rb").read()
chk("PRE.bytes", len(d) == 791958, "len=%d" % len(d))
chk("PRE.sha", hashlib.sha256(d).hexdigest() == "711ed76dd238a995ed77c597d0717b5045cff53b4a0837c9b03469d7c172a3fb",
    hashlib.sha256(d).hexdigest())
chk("PRE.eol", d.count(b"\n") == d.count(b"\r\n") and d.count(b"\r\n") == 3860,
    "CRLF=%d bareLF=%d" % (d.count(b"\r\n"), d.count(b"\n") - d.count(b"\r\n")))
s = d.decode("utf-8")
chk("idiom24", s.count("they close nothing in Problem~G.") == 24, "count=%d" % s.count("they close nothing in Problem~G."))
chk("verb1", s.count("closes nothing") == 1, "count=%d" % s.count("closes nothing"))
chk("vac2", s.count("\\emph{Vacuum term.}") == 2, "count=%d" % s.count("\\emph{Vacuum term.}"))
p098 = d.rfind(b"\\emph{Exact fibre interval")
le = d.find(b"\r\n", p098)
tail = d[le - 620:le]
tailwant = ("These statements are exact linear-algebraic and measure-theoretic identifiability statements on the "
            "support of the named constant-variance subclass and of the named column-profile law at every strictly "
            "positive non-constant profile and every \\(D\\ge3\\), they bound nonexistence between the named scalar "
            "and spectrum coordinates only, they evaluate no matrix integral of the core action, they supply no "
            "state and no selection mechanism, they do not fix the state that sets \\(W\\), \\(g\\), \\(s\\) or the "
            "frame, they leave the missing steps (i)-(iv) of the Missing step paragraph unchanged, and they close "
            "nothing in Problem~G.").encode("ascii")
chk("pin.tail", tail == tailwant and len(tailwant) == 620, "tail exact 620 B")
chk("pin.range", d[754517:755137] == tailwant, "tail == d[754517:755137]")
probe = tail + b"\r\n\r\n\\emph{Vacuum term.}"
chk("pin.count", d.count(probe) == 1, "compound probe count=%d" % d.count(probe))
cut = le + 4
chk("pin.offset", cut == 755141 and le == 755137, "byte cut=%d tail start=%d" % (cut, le - 620))
ins = open("proposals/099-g-mi-p-d-d2/insert-r2.tex", "rb").read()
chk("ins.bytes", len(ins) == 1656, "len=%d sha256=%s" % (len(ins), hashlib.sha256(ins).hexdigest()))
chk("ins.eol", ins.endswith(b"\r\n") and ins.count(b"\r\n") == 1, "single terminal CRLF")
chk("ins.ascii", all(b < 128 for b in ins), "pure ASCII")
chk("ins.idiom", ins.count(b"they close nothing in Problem~G.") == 1 and ins.rstrip(b"\r\n").endswith(b"they close nothing in Problem~G."), "ends with idiom, once")
chk("ins.banned", not re.search(rb"(?i)\b(status|priority|completion|open|critical|programme|derived)\b", ins), "no banned words")
chk("ins.tokens", not any(t in ins for t in (b"$", b"\\cite", b"\\ref", b"\\eqref", b"\\label", b"[", b"]")), "no forbidden tokens")
chk("ins.nobareu", re.search(rb"(?<![A-Za-z])u(?![A-Za-z])", ins) is None, "zero bare-u tokens (round-1 blocking fix)")
hdr = ins[:ins.index(b"}") + 1]
cnt = 0
for f in glob.glob("chapters/**/*.tex", recursive=True):
    cnt += open(f, "rb").read().count(hdr)
chk("ins.hdruniq", cnt == 0, "header appears %d times pre-insert (must be 0)" % cnt)
print("SUMMARY", "ALL PASS" if not FAIL else "FAILED: " + ",".join(FAIL))
assert not FAIL
