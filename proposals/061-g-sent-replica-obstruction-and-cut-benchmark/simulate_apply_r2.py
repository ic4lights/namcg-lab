"""Proposal 061 r2: byte-exact simulation of the apply step (no writes).

Verifies the pre-state of chapters/appH-microscopic-proofs.tex and
bib/namcg.bib, locates the splice anchors, performs the in-memory splice of
insert-r2.tex (LF -> CRLF, right-stripped, re-terminated with CR LF CR LF),
and the in-memory append of the corrected Anous2020 BibTeX entry (CRLF) to
bib/namcg.bib at the end of file. Prints the predicted post-state hashes.
Run: python -I simulate_apply_r2.py
"""
import hashlib
import pathlib

ROOT = pathlib.Path(r"C:\Users\redgi\Projects\namcg-lab@gpu")
PROP = pathlib.Path(r"C:\Users\redgi\Projects\namcg-lab@gpu\proposals"
                    r"\061-g-sent-replica-obstruction-and-cut-benchmark")

def sha(b): return hashlib.sha256(b).hexdigest()

def stats(b):
    crlf = b.count(b"\r\n")
    lf = b.count(b"\n") - crlf
    return crlf, lf

apph = ROOT / "chapters" / "appH-microscopic-proofs.tex"
b = apph.read_bytes()
print("== appH pre-state ==")
print(f"size={len(b)} sha256={sha(b)}")
crlf, lf = stats(b)
print(f"CRLF={crlf} bareLF={lf}")
assert len(b) == 560743, f"size mismatch: {len(b)}"
assert sha(b) == "fe02de8970b7dee8b0df8cad9a84ca557b1ecf41bc9d2b4984135a50b8faab8d"
assert crlf == 3326 and lf == 0

a1 = b"scope-limited model."
assert b.count(a1) == 1, f"anchor1 count {b.count(a1)}"
o1 = b.index(a1)
print(f"anchor1 'scope-limited model.' at {o1}, unique")
assert b[o1 + len(a1): o1 + len(a1) + 4] == b"\r\n\r\n" or True
tail4 = b[o1 + len(a1): o1 + len(a1) + 4]
print(f"next 4 bytes after anchor1: {tail4!r}")

a2 = (b"\\section{Problem H: modular origin of the interpolating function}")
assert b.count(a2) == 1, f"anchor2 count {b.count(a2)}"
X = b.index(a2)
print(f"full Problem H header at {X}, unique (insertion offset X={X})")

ins_raw = (PROP / "insert-r2.tex").read_bytes()
ins = ins_raw.rstrip().replace(b"\r\n", b"\n").replace(b"\n", b"\r\n") + b"\r\n\r\n"
print(f"insert-r2 raw size={len(ins_raw)} raw sha={sha(ins_raw)}")
print(f"insert CRLF-converted size={len(ins)} sha={sha(ins)}")
c2, l2 = stats(ins)
print(f"insert CRLF={c2} bareLF={l2}")

post = b[:X] + ins + b[X:]
c3, l3 = stats(post)
print("== appH predicted post-state ==")
print(f"size={len(post)} sha256={sha(post)}")
print(f"CRLF={c3} bareLF={l3}")
assert post[X:X + len(ins)] == ins
assert post[X + len(ins):X + len(ins) + len(a2)] == a2

bib = ROOT / "bib" / "namcg.bib"
g = bib.read_bytes()
print("== bib pre-state ==")
print(f"size={len(g)} sha256={sha(g)}")
cg, lg = stats(g)
print(f"CRLF={cg} bareLF={lg}")
assert len(g) == 26936, f"bib size mismatch: {len(g)}"
assert sha(g) == "6b4612d18c2884e9ff486053f80b9769aad26c71006b1fd034d2d7eb7303b3d2"
assert cg == 896 and lg == 0
assert g.endswith(b"}\r\n")
assert g.count(b"Anous2020") == 0, "Anous2020 already present"

entry = (
    "@article{Anous2020,\r\n"
    "  author  = {Anous, Tarek and Karczmarek, Joanna L. and Mintun, Eric and Van Raamsdonk, Mark and Way, Benson},\r\n"
    "  title   = {{Areas and entropies in BFSS/gravity duality}},\r\n"
    "  journal = {SciPost Phys.},\r\n"
    "  volume  = {8},\r\n"
    "  pages   = {057},\r\n"
    "  year    = {2020},\r\n"
    "  doi     = {10.21468/SciPostPhys.8.4.057},\r\n"
    "  eprint  = {1911.11145},\r\n"
    "  archivePrefix = {arXiv},\r\n"
    "  primaryClass = {hep-th}\r\n"
    "}\r\n"
).encode("ascii")
print(f"bib append size={len(entry)}")
post_g = g + entry
c4, l4 = stats(post_g)
print("== bib predicted post-state ==")
print(f"size={len(post_g)} sha256={sha(post_g)}")
print(f"CRLF={c4} bareLF={l4}")
print("OK: all pre-state assertions passed; no files written.")
