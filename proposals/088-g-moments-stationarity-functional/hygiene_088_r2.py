# hygiene_088_r2.py -- independent re-check of insert-r2.tex bytes + live-anchor pins
# + byte-equality against gatekeeper-extracted correction sources. Read-only on chapters/.
# Run: python -I hygiene_088_r2.py
import glob, re, sys
sys.stdout.reconfigure(errors="replace")
P = "proposals/088-g-moments-stationarity-functional/insert-r2.tex"
d = open(P, "rb").read(); ok = True
def chk(name, cond, extra=""):
    global ok
    print("%-48s %s %s" % (name, "OK" if cond else "FAIL", extra)); ok = ok and cond
t = d.decode("utf-8")
chk("single content line + terminal CRLF",
    d.endswith(b"\r\n") and d.replace(b"\r\n", b"").count(b"\n") == 0 and d.count(b"\r\n") == 1)
chk("no control bytes < 0x20 except terminal", sum(1 for x in d[:-2] if x < 0x20) == 0)
chk("no BOM, valid UTF-8", d[:3] != b"\xef\xbb\xbf")
for m in [b"$", b"[", b"]", b"\cite", b"\ref", b"\eqref", b"\label"]:
    chk("absent " + m.decode(), d.count(m) == 0)
for f in ["status", "priority", "completion", "open", "critical", "programme", "derived"]:
    chk("word absent: " + f, t.lower().count(f) == 0)
chk("exactly one \emph{ header", d.count(b"\emph{") == 1)
h = "Variational rigidity of the frame-averaged decoupling locus"
hits = sum(open(f, encoding="utf-8", errors="replace").read().count(h)
           for f in glob.glob("chapters/**/*.tex", recursive=True))
chk("header unique across chapters (count 0 pre-splice)", hits == 0, "hits=%d" % hits)
chk("brace balance", d.count(b"{") == d.count(b"}"))
chk("paren balance", d.count(b"(") == d.count(b")"))
chk("ends with close idiom", d.endswith(b"they close nothing in Problem~G.\r\n"))
nums = sorted(set(re.findall(r"(?<![A-Za-z_])\d+", t)))
chk("numerals within allowlist {0,1,2}", all(x in {"0","1","2"} for x in nums), str(nums))
# --- r2 correction byte-equality vs gatekeeper-extracted sources ---
b2 = open("scratch/r2fix/block2_corrected.txt", "rb").read()
b2f3 = b2.replace(b"is the minimal case;", b"is the minimal recorded case;", 1)  # F3 fold
chk("F2 clause bytes present verbatim (review-sourced)",
    open("scratch/r2fix/clause_f2.txt","rb").read() in d)
chk("block2 bytes present (with F3 fold, count 1)", d.count(b2f3) == 1)
chk("F1 false claim absent", b"strictly monotone \(C^{1}\) reparametrisation the stationary locus is unchanged" not in d)
chk("old block-3 clause absent", b"while a symmetric non-convex term" not in d)
chk("'minimal recorded case' count 1", d.count(b"minimal recorded case") == 1)
# --- live-anchor pins (read-only) ---
D = open("chapters/appH-microscopic-proofs.tex", "rb").read()
pin = b"they classify the locus over frame laws rather than selecting the profile"
chk("forward pin count == 1", D.count(pin) == 1, "count=%d" % D.count(pin))
j = D.find(b"\r\n\r\n\emph{Vacuum term.}", D.find(pin))
chk("gap CRLFCRLF before Vacuum term", j != -1)
k = D.rfind(b"\r\n", 0, D.find(pin))
chk("pin lies inside the 087 paragraph line", D[k+2:k+20].startswith(b"\emph{Measure"))
print("insert-r2 bytes", len(d), "| numerals", nums, "| overall", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
