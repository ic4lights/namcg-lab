# hygiene_098.py - byte hygiene battery for insert-r1.tex + PRE pins + relative-pointer checks. No writes.
# Run from repo root: python -I proposals/098-g-scalar-p2-nonbridge-d3/hygiene_098.py
import hashlib, re, glob
BS = chr(92)
ok = 0
def chk(tag, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + tag)
    if not cond:
        ok += 1

ins = open("proposals/098-g-scalar-p2-nonbridge-d3/insert-r1.tex", "rb").read()
chk("H0 terminal CRLF", ins.endswith(b"\r\n") and ins.count(b"\n") == 1)
body = ins[:-2].decode("ascii")
chk("H1 single line", chr(10) not in body and chr(13) not in body)
chk("H2 printable ASCII", all(32 <= ord(c) < 127 for c in body))
chk("H3 no $ or brackets", all(t not in body for t in ["$", "[", "]"]))
for t in ["\\cite", "\\ref{", "\\eqref", "\\label"]:
    chk("H4 " + t, t not in body)
chk("H5 single leading emph", body.count(BS + "emph{") == 1 and body.startswith(BS + "emph{"))
hdr = body.split("} ")[0]
chk("H6 header period", hdr.endswith("."))
chk("H7 header plain", BS not in hdr[5:])
chk("H8 banned words", re.search(r"(?i)\b(status|priority|completion|open|critical|programme|derived)\b", body) is None)
IDIOM = "they close nothing in Problem~G."
chk("H9 idiom once at end", body.count(IDIOM) == 1 and body.endswith(IDIOM))
chk("H10 no verb-form or Vacuum", "closes nothing" not in body and "Vacuum" not in body)
chk("H11 math balanced", body.count("\\(") == body.count("\\)"))
chk("H12 braces balanced", body.count("{") == body.count("}"))
app = open("chapters/appH-microscopic-proofs.tex", "rb").read()
chk("H13 appH PRE hash", hashlib.sha256(app).hexdigest() == "691af35303cf46fadcb38b9e0f4a455a54e14fa65adf5e553c0e8839fdfc6e41" and len(app) == 786170)
chk("H14 appH idiom 23", app.count(IDIOM.encode()) == 23)

hdrfull = hdr + "}"
hits = 0
for f in glob.glob("chapters" + chr(47) + "*" + chr(46) + "tex"):
    hits += open(f, "rb").read().count(hdrfull.encode())
chk("H15 header unique in chapters", hits == 0)
# relative-pointer sanity on the live tree at the cut point (before Vacuum-term):
# 1st preceding = 097, 2nd = 096, 3rd = 095, 6th = 092 (rho-family + recursion)
paras = [p for p in app.decode("ascii", "ignore").split(chr(13) + chr(10) + chr(13) + chr(10)) if p.strip()]
vi = None
for i, p in enumerate(paras):
    if p.startswith(BS + "emph{Vacuum term.}"):
        vi = i
chk("H16 relative pointers", vi is not None and vi >= 7
    and paras[vi - 1].startswith("\emph{Non-identifiability of the diagonal moment tuple under heterogeneous")
    and paras[vi - 2].startswith("\emph{Higher-dimensional non-identifiability")
    and paras[vi - 3].startswith("\emph{Non-identifiability of the moment-type")
    and ("recursion" in paras[vi - 6]) and ((BS + "rho") in paras[vi - 6]))
# PIN uniqueness probes (pathfinder warning: 097 tail head shares its first 110 bytes with the 096 tail head)
start = b"These statements are exact linear-algebraic and measure-theoretic identifiability statements on the support of"
chk("H17 shared head occurs twice", app.count(start) == 2)
head = start + b" the named column-profile law for every strictly positive non-constant profile at every"
idxh = app.find(head)
chk("H18 097-head unique at pinned offset", app.count(head) == 1 and idxh == 748701)
tail648 = app[idxh:idxh + 648]
chk("H18b tail648 unique + ends idiom", app.count(tail648) == 1 and tail648.endswith(IDIOM.encode()))
chk("H19 compound PIN unique", app.count(tail648 + b"\r\n\r\n" + BS.encode() + b"emph{Vacuum term.}") == 1)
print("SUMMARY " + ("ALL PASS" if ok == 0 else "FAILURES %d" % ok))
raise SystemExit(0 if ok == 0 else 1)
