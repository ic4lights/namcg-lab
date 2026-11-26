"""apply check for 069: anchor uniqueness, bytes, labels, citations, one status sentence.
Read-only on the repository; nothing is written."""
import re, os, hashlib
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.abspath(os.path.join(here, "..", ".."))
ins = open(os.path.join(here, "appH_insert.tex"), "rb").read()
app = open(os.path.join(root, "chapters", "appH-microscopic-proofs.tex"), "rb").read()
BS = chr(92)
anchor = (BS + "section{Problem G: HBEV}").encode()
ok = True
def chk(name, cond):
    global ok
    ok = ok and bool(cond); print(("PASS " if cond else "FAIL ") + name)
chk("anchor occurs once in appH: %d" % app.count(anchor), app.count(anchor) == 1)
pre = app[:app.index(anchor)]
chk("anchor preceded by the closing sentence of the L2793 paragraph", pre.rstrip().endswith(b"Problems~C, F and~N remain open and PROGRAMME-CONDITIONAL."))
chk("anchor after label sec:status-F and before label sec:status-G", pre.rfind((BS + "label{sec:status-F}").encode()) > 0 and (BS + "label{sec:status-G}").encode() not in pre)
chk("insert ASCII, LF only, no BOM", all(b < 128 for b in ins) and b"\r" not in ins)
chk("insert ends with blank line", ins.endswith(b".\n\n"))
txt = ins.decode()
allch = b""
for f in sorted(os.listdir(os.path.join(root, "chapters"))):
    if f.endswith(".tex"):
        allch += open(os.path.join(root, "chapters", f), "rb").read()
labs = sorted(set(re.findall("[" + BS + BS + "](?:eq)?ref[{]([^}]*)[}]", txt)))
for lab in labs:
    chk("label exists once: " + lab, allch.count((BS + "label{%s}" % lab).encode()) == 1)
chk("no new label in insert", (BS + "label{") not in txt)
bib = open(os.path.join(root, "bib", "namcg.bib"), encoding="utf-8").read()
new = open(os.path.join(here, "new_bib_entry.bib")).read()
keys = sorted(set(k.strip() for c in re.findall("[" + BS + BS + "]cite[{]([^}]*)[}]", txt) for k in c.split(",")))
for key in keys:
    inb = ("{%s," % key) in bib; inn = ("{%s," % key) in new
    chk("cite key %s: in bib=%s, in new_bib_entry=%s (exactly one)" % (key, inb, inn), inb != inn)
chk("one status sentence, at the end", txt.count("PROGRAMME-CONDITIONAL") == 1 and txt.rstrip().endswith("remain open and PROGRAMME-CONDITIONAL."))
chk("no label words (Status:, CRITICAL PATH, DERIVED, CLOSED)", not re.search("Status:|CRITICAL PATH|DERIVED|CLOSED", txt))
chk("balanced braces and math delimiters", txt.count("{") == txt.count("}") and txt.count(BS + "(") == txt.count(BS + ")") and txt.count(BS + "[") == txt.count(BS + "]"))
chk("no process language", not re.search("proposal|gatekeeper|researcher|adversary|review|[^g]round ", txt))
chk("no bare r variable left (r_c only)", not re.search("[^_a-zA-Z" + BS + BS + "]r[=)(-]", txt.replace("r=-2", "")))
out = pre + ins.replace(b"\n", b"\r\n") + app[app.index(anchor):]
print("labels:", labs); print("cite keys:", keys)
print("insert bytes (LF) %d, sha256 %s" % (len(ins), hashlib.sha256(ins).hexdigest()))
print("appH bytes %d -> %d (in memory only)" % (len(app), len(out)))
print("paragraph blocks:", txt.count("\n\n"))
print("ALL PASS" if ok else "SOME FAIL")
