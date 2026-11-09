"""
Proposal 062 r1: apply simulation for chapters/appH-microscopic-proofs.tex.

Pre-state asserted (must match before any integration):
  size 566953, sha256 21737625769589a64090c8b7f93842b1eaa5d12cff3e4877f70f2db8e5947999,
  CRLF count 3415, bare LF 0.
Inserts: insert-r1.tex (LF in file; two blocks split on a line "%---SPLIT---%"),
converted to CRLF on apply. Ascending single-pass splices:
  X_C: after the unique anchor "tensor operator or the remaining scalar couplings."
       (Problem C section end; the following bytes must be
        "\\r\\nProblems~B, C, D, F and~G remain open.\\r\\n\\r\\n\\section{Problem D")
  X_F: at the start of "\\r\\n\\r\\n\\section{Problem G: HBEV}" (unique), i.e. the
       Problem G section header; the preceding bytes must be the end of the
       second 048/049 ledger paragraph "PROGRAMME-CONDITIONAL."
bib/namcg.bib is NOT modified by this proposal; its pre-state is asserted and
echoed for the record: size 27350, sha256 40d6ea09915dd4b8220f30c466821118492ee5560f66930b7c5d9a2dd8b95b90.
"""
import hashlib

APP = r"C:\Users\redgi\Projects\namcg-lab@gpu\chapters\appH-microscopic-proofs.tex"
BIB = r"C:\Users\redgi\Projects\namcg-lab@gpu\bib\namcg.bib"
INS = r"C:\Users\redgi\Projects\namcg-lab@gpu\proposals\062-c-scalar-tadpole-nonderivative-obstruction\insert-r1.tex"

def sha(b): return hashlib.sha256(b).hexdigest()

app = open(APP, "rb").read()
bib = open(BIB, "rb").read()
print("appH pre  size:", len(app), "sha256:", sha(app))
assert len(app) == 566953
assert sha(app) == "21737625769589a64090c8b7f93842b1eaa5d12cff3e4877f70f2db8e5947999"
assert app.count(b"\r\n") == 3415
assert app.replace(b"\r\n", b"").count(b"\n") == 0
print("appH pre-state OK (CRLF 3415, bare LF 0)")
print("bib pre  size:", len(bib), "sha256:", sha(bib), "CRLF:", bib.count(b"\r\n"), "bare LF:", bib.replace(b"\r\n", b"").count(b"\n"))
assert len(bib) == 27350
assert sha(bib) == "40d6ea09915dd4b8220f30c466821118492ee5560f66930b7c5d9a2dd8b95b90"

raw = open(INS, "rb").read()
parts = raw.split(b"\n%---SPLIT---%\n")
assert len(parts) == 2, f"split marker found {len(parts)-1} times"
pc_LF, pf_LF = parts[0], parts[1]
assert b"\r" not in raw
pc = pc_LF.replace(b"\n", b"\r\n")
pf = pf_LF.rstrip(b"\n").replace(b"\n", b"\r\n")
print("insert C block: raw len", len(pc_LF), "sha", sha(pc_LF)[:16], "| CRLF-converted len", len(pc), "sha", sha(pc)[:16])
print("insert F block: raw len", len(pf_LF), "sha", sha(pf_LF)[:16], "| CRLF-converted len", len(pf), "sha", sha(pf)[:16])

anchorC = b"tensor operator or the remaining scalar couplings."
assert app.count(anchorC) == 1, "anchorC not unique"
XC = app.find(anchorC) + len(anchorC)
following = app[XC:XC + 100]
print("X_C =", XC, "following bytes:", following)
assert following.startswith(b"\r\nProblems~B, C, D, F and~G remain open.\r\n\r\n\\section{Problem D")

anchorF = b"\r\n\r\n\\section{Problem G: HBEV}"
assert app.count(anchorF) == 1, "anchorF not unique"
XF = app.find(anchorF)
print("X_F =", XF, "preceding bytes:", app[XF - 40:XF])
assert app[XF - 22:XF] == b"PROGRAMME-CONDITIONAL."

# ascending splices; insert content carries its own leading blank lines
contentC = b"\r\n\r\n" + pc
contentF = b"\r\n\r\n" + pf
out = app[:XC] + contentC + app[XC:XF] + contentF + app[XF:]
print("post  size:", len(out), "sha256:", sha(out))
print("post  CRLF:", out.count(b"\r\n"), "bare LF:", out.replace(b"\r\n", b"").count(b"\n"))
# spot-check contexts after the splices
i = out.find(anchorC)
print("C junction:", out[i + len(anchorC): i + len(anchorC) + 60])
print("C end:", out[out.find(b"recorded in the Problem~F entry."): out.find(b"recorded in the Problem~F entry.") + 90])
j = out.find(pf[:60])
print("F start:", out[j:j + 80])
k = out.find(b"Problems~C, F and~N remain open and PROGRAMME-CONDITIONAL.\r\n\r\n\\section{Problem G: HBEV}")
print("F end junction found:", k != -1, "at", k)
print("bib post (unchanged):", len(bib), sha(bib))
