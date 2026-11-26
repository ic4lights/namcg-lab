# hygiene_099.py -- live-file contract and anchor hygiene for item 099 (read-only).
# Run from repo root:  python -I proposals/099-g-mi-p-d-d2/hygiene_099.py
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
hdrs = [("089", "Pushforward weights on the profile simplex from the named slot and frame measures."),
        ("090", "Fixed-trace beta deformation of the exchangeable weight on the profile simplex."),
        ("091", "Eigenvalue reduction of the edge Gram and the Jacobian origin of the beta factor."),
        ("092", "Transport of the profile coordinate along the pushforward family and its moment coordinates."),
        ("093", "Quantitative orbit rigidity of the moment coordinate near coincidence walls."),
        ("094", "Unconditional stratum localization of the beta-family wall integrals."),
        ("095", "Non-identifiability of the moment-type diagonal coordinate from the Gram spectrum."),
        ("096", "Higher-dimensional non-identifiability of the diagonal moment tuple from the Gram spectrum."),
        ("097", "Non-identifiability of the diagonal moment tuple under heterogeneous slot variances."),
        ("098", "Exact fibre interval of the diagonal quadratic statistic and scalar non-recovery from the Gram spectrum.")]
pos = []
for tag, h in hdrs:
    i = s.find(h)
    chk("hdr." + tag, i >= 0 and s.count(h) == 1, "found=%d count=%d" % (i >= 0, s.count(h)))
    pos.append(i)
chk("order", all(pos[k] < pos[k + 1] for k in range(len(pos) - 1)), "089<090<...<098 order holds")
# PIN probe, byte-based (the file has 3 non-ASCII bytes near 711159 so char offsets differ):
p098 = d.rfind(b"\\emph{Exact fibre interval")
le = d.find(b"\r\n", p098)
tail = d[le - 620:le]
probe = tail + b"\r\n\r\n\\emph{Vacuum term.}"
chk("pin.count", d.count(probe) == 1, "compound probe count=%d" % d.count(probe))
cut = le + 4
chk("pin.offset", cut == 755141, "byte cut=%d tail start=%d" % (cut, le - 620))
tailwant = ("These statements are exactly as stated: the fibre interval, the uniform law of x and the independence "
            "are identities of the model; they carry no state-side weight. As with the preceding two paragraphs they "
            "close nothing in Problem~G.").encode("ascii")
chk("pin.tail", tail == tailwant and len(tail) == 620, "tail exact 620 B")
shared = 0
p097 = d.rfind(b"\\emph{Non-identifiability of the diagonal moment tuple under")
le97 = d.find(b"\r\n", p097)
tail097 = d[le97 - 620:le97]
while shared < 620 and tail[-1 - shared] == tail097[-1 - shared]:
    shared += 1
print("INFO shared-suffix: last %d bytes of the 620-B tail are shared with the 097 tail; the compound probe (tail + CRLFCRLF + line-initial Vacuum) still occurs exactly once" % shared)
ins = open("proposals/099-g-mi-p-d-d2/insert-r1.tex", "rb").read()
chk("ins.bytes", len(ins) == 1558, "len=%d sha256=%s" % (len(ins), hashlib.sha256(ins).hexdigest()))
chk("ins.eol", ins.endswith(b"\r\n") and ins.count(b"\r\n") == 1, "single terminal CRLF")
chk("ins.ascii", all(b < 128 for b in ins), "pure ASCII")
chk("ins.idiom", ins.count(b"they close nothing in Problem~G.") == 1 and ins.rstrip(b"\r\n").endswith(b"they close nothing in Problem~G."), "ends with idiom, once")
chk("ins.banned", not re.search(rb"(?i)\b(status|priority|completion|open|critical|programme|derived)\b", ins), "no banned words")
chk("ins.tokens", not any(t in ins for t in (b"$", b"\\cite", b"\\ref", b"\\eqref", b"\\label", b"[", b"]")), "no forbidden tokens")
hdr = ins[:ins.index(b"}") + 1]
cnt = 0
for f in glob.glob("chapters/**/*.tex", recursive=True):
    cnt += open(f, "rb").read().count(hdr)
chk("ins.hdruniq", cnt == 0, "header appears %d times pre-insert (must be 0)" % cnt)
print("SUMMARY", "ALL PASS" if not FAIL else "FAILED: " + ",".join(FAIL))
assert not FAIL
