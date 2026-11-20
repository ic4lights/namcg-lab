# hygiene_100.py -- item 100 r1 hygiene battery (099-r2 convention). Read-only.
# Run: python -I proposals/100-g-mi-tau-conditioning-d2/hygiene_100.py
import hashlib, re, io, glob
D = "C:/Users/redgi/Projects/namcg-lab@gpu/"
A = D + "chapters/appH-microscopic-proofs.tex"
INS = D + "proposals/100-g-mi-tau-conditioning-d2/insert-r1.tex"
res = []
def chk(name, ok, extra=""):
    res.append((name, bool(ok), extra))
d = open(A, "rb").read()
chk("pre.bytes", len(d) == 793616, str(len(d)))
chk("pre.sha", hashlib.sha256(d).hexdigest().startswith("7cd6e2084c065f69"))
chk("pre.crlf", d.count(b"\r\n") == 3862, str(d.count(b"\r\n")))
chk("pre.bareLF", d.replace(b"\r\n", b"").count(b"\n") == 0)
pin = (b"These are spectrum-side numbers about a fibre coordinate: they bound no state-side profile weight, "
       b"identify no simplex fibre, and they close" + b" nothing in Problem~G.")
i = d.find(pin)
chk("pin.len", len(pin) == 162, str(len(pin)))
chk("pin.pos", i == 756633, str(i))
chk("pin.count", d.count(pin) == 1, str(d.count(pin)))
comp = pin + b"\r\n\r\n" + b"\\emph{Vacuum term.}"
chk("compound.count", d.count(comp) == 1, str(d.count(comp)))
chk("cut.begin", d[756799:757000].startswith(b"\\emph{Vacuum term.}"))
ins = open(INS, "rb").read()
chk("ins.nonempty", len(ins) > 300, str(len(ins)))
chk("ins.termCRLF", ins.endswith(b"\r\n") and ins[:-2].count(b"\r\n") == 0)
chk("ins.ascii", all(c < 128 for c in ins))
txt = ins.decode()
chk("ins.nobareu", re.search(r"(?<![A-Za-z0-9])u(?![A-Za-z0-9])", txt) is None)
chk("ins.onehdr", txt.count("\\emph{") == 1 and txt.startswith("\\emph{"))
chk("ins.nomathchars", all(txt.count(c) == 0 for c in "$[]"))
chk("ins.norefcite", all(k not in txt for k in ("\\cite", "\\ref{", "\\eqref", "\\label")))
chk("ins.idiom", txt.count("close nothing in Problem~G.") == 1)
hdr = txt[: txt.index("}")] + "}"
files = sorted(glob.glob(D + "chapters/*.tex"))
cnt = sum(open(f, "rb").read().decode("latin-1").count(hdr) for f in files)
chk("hdr.unique_pre", cnt == 0, hdr[:60])
bal = txt.count("{") - txt.count("}")
chk("ins.braces", bal == 0, str(bal))
chk("ins.parens", txt.count("(") - txt.count(")") == 0)
bad = [w for w in ("TODO", "predecessor", "corrected", "round 1", "we ") if w in txt]
chk("ins.noproc", not bad, str(bad))
post = d[:756799] + ins + b"\r\n" + d[756799:]
chk("post.bytes", len(post) == 793616 + len(ins) + 2, str(len(post)))
chk("post.crlf", post.count(b"\r\n") == 3864)
chk("post.bareLF", post.replace(b"\r\n", b"").count(b"\n") == 0)
chk("post.idiom26", post.count(b"close nothing in Problem~G.") == 26)
chk("post.closes1", post.count(b"closes nothing") == 1)
chk("post.vac2", post.count(b"\\emph{Vacuum term.}") == 2)
chk("post.hdr1", post.decode("latin-1").count(hdr) == 1)
chk("post.adjacency", post.count(b"Problem~G.\r\n\r\n" + ins[:12]) == 1)
chk("post.oldseam", post.count(b"and they close nothing in Problem~G.\r\n\r\n\\emph{Vacuum term.}") == 0)
fails = [n for n, ok, _ in res if not ok]
for n, ok, e in res:
    print(("PASS " if ok else "FAIL ") + n + ((" | " + e) if e else ""))
print("SUMMARY " + ("ALL PASS" if not fails else "FAILURES: " + ",".join(fails)))
