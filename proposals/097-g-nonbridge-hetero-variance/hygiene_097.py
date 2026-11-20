# hygiene_097.py - byte hygiene battery for insert-r1.tex + PRE pins for appH. No writes.
# Run: python -I proposals/097-g-nonbridge-hetero-variance/hygiene_097.py   (repo root)
import hashlib, re, glob
BS = chr(92)
ok = 0
def chk(tag, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + tag)
    if not cond:
        ok += 1

ins = open("proposals/097-g-nonbridge-hetero-variance/insert-r1.tex", "rb").read()
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
chk("H13 appH PRE hash", hashlib.sha256(app).hexdigest() == "0e4c097b078e020bcf8165bf6b78680ea8b0d40ca0369361ddb3b9efec3aed5b" and len(app) == 780748)
chk("H14 appH idiom 22", app.count(IDIOM.encode()) == 22)
hdrfull = hdr + "}"
hits = 0
for f in glob.glob("chapters" + chr(47) + "*" + chr(46) + "tex"):
    hits += open(f, "rb").read().count(hdrfull.encode())
chk("H15 header unique in chapters", hits == 0)
# relative-pointer sanity: 6th preceding para (from insert point) = 091 subclass para mentioning Vandermonde exponent 2
paras = [p for p in app.decode("ascii", "ignore").split(chr(13) + chr(10) + chr(13) + chr(10)) if p.strip()]
tailidx = None
for i, p in enumerate(paras):
    if p.startswith(BS + "emph{Higher-dimensional non-identifiability"):
        tailidx = i
chk("H16 relative pointers", tailidx is not None
    and paras[tailidx - 1].startswith("\emph{Non-identifiability of the moment-type")
    and ("Vandermonde" in paras[tailidx - 5])
    and ("recursion" in paras[tailidx - 4] and (BS + "rho") in paras[tailidx - 4]))
print("SUMMARY " + ("ALL PASS" if ok == 0 else "FAILURES %d" % ok))
raise SystemExit(0 if ok == 0 else 1)
