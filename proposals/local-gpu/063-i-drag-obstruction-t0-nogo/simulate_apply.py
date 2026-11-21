"""
Proposal 063 r1: apply simulation for chapters/appH-microscopic-proofs.tex
using insert-r1.tex (single block, no "%---SPLIT---%" marker).

Pre-state asserted (must match before any integration):
  appH: size 573239, sha256 08a61b890e33dedf9c3122912c8e4ea6c113fe95396fa4220136d3417b49b9eb,
        CRLF count 3419, bare LF 0.
  bib:  size 27350, sha256 40d6ea09915dd4b8220f30c466821118492ee5560f66930b7c5d9a2dd8b95b90
        (NOT modified by this proposal; asserted and echoed).

Insert: insert-r1.tex (LF in file), converted to CRLF on apply; trailing LF
stripped. Splice point X: immediately after the unique string
  "response, its tensor structure, or its coefficient."
(last sentence of the "Static tail, distinct from the response" paragraph),
which is followed in the file by "\r\n\r\n\paragraph{Missing step.}"
(the bare "\paragraph{Missing step.}" occurs 9 times in the appendix, so
the uniqueness comes from the prefixed sentence; both are asserted).
The block is inserted with one blank line before and after, immediately
before that \paragraph{Missing step.}. Nothing in the Ledger-label or
Status paragraphs is touched; no status, priority or completion label
changes.
"""
import hashlib

APP = r"C:\Users\redgi\Projects\namcg-lab@gpu\chapters\appH-microscopic-proofs.tex"
BIB = r"C:\Users\redgi\Projects\namcg-lab@gpu\bib\namcg.bib"
INS = r"C:\Users\redgi\Projects\namcg-lab@gpu\proposals\063-i-drag-obstruction-t0-nogo\insert-r1.tex"

def sha(b): return hashlib.sha256(b).hexdigest()

app = open(APP, "rb").read()
bib = open(BIB, "rb").read()
print("appH pre  size:", len(app), "sha256:", sha(app))
assert len(app) == 573239
assert sha(app) == "08a61b890e33dedf9c3122912c8e4ea6c113fe95396fa4220136d3417b49b9eb"
assert app.count(b"\r\n") == 3419
assert app.replace(b"\r\n", b"").count(b"\n") == 0
print("appH pre-state OK (CRLF 3419, bare LF 0)")
print("bib pre  size:", len(bib), "sha256:", sha(bib), "CRLF:", bib.count(b"\r\n"),
      "bare LF:", bib.replace(b"\r\n", b"").count(b"\n"))
assert len(bib) == 27350
assert sha(bib) == "40d6ea09915dd4b8220f30c466821118492ee5560f66930b7c5d9a2dd8b95b90"

raw = open(INS, "rb").read()
assert b"\r" not in raw, "insert file must be LF-only"
assert b"%---SPLIT---%" not in raw, "single-block insert: no split marker expected"
blk = raw.rstrip(b"\n").replace(b"\n", b"\r\n")
print("insert block: raw len", len(raw), "sha", sha(raw)[:16],
      "| rstripped", len(raw.rstrip(b"\n")), "| CRLF-converted len", len(blk),
      "sha", sha(blk)[:16])

sent = "response, its tensor structure, or its coefficient.".encode("ascii")
anchor_full = sent + b"\r\n\r\n" + "\\paragraph{Missing step.}".encode("ascii")
assert app.count(sent) == 1, f"anchor sentence not unique: {app.count(sent)}"
assert app.count(anchor_full) == 1, "anchor_full not unique"
X = app.find(sent) + len(sent)
following = app[X:X + 90]
print("X =", X, "preceding bytes:", app[X - 60:X])
print("following bytes:", following)
tail = (chr(13) + chr(10)).encode("ascii") * 2 + (chr(92) + "paragraph{Missing step.}").encode("ascii")
assert following.startswith(tail)

out = app[:X] + b"\r\n\r\n" + blk + app[X:]
print("post  size:", len(out), "sha256:", sha(out))
print("post  CRLF:", out.count(b"\r\n"), "bare LF:", out.replace(b"\r\n", b"").count(b"\n"))
i = out.find("\\paragraph{Definitional status of the prescription.}".encode("ascii"))
print("block 1 present:", i != -1, "at", i)
j = out.find("\\paragraph{Low-frequency support and sub-critical vanishing".encode("ascii"))
print("block 2 present:", j != -1, "at", j)
k = out.find("coefficient; Problem~I remains open.".encode("ascii"))
print("block 2 closer present:", k != -1, "at", k)
crlf2 = tail[:4]
m1 = out.find(sent + crlf2 + blk[:40])
m2 = out.find(blk[-40:] + tail)
print("junction before block OK:", m1 != -1, "at", m1, "| junction after block OK:", m2 != -1, "at", m2)
print("Ledger-label paragraph untouched:",
      app.count(b"Status: OPEN. Priority: OPTIONAL falsifiable") == 1)
print("bib post (unchanged):", len(bib), sha(bib))
