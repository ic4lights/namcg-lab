#!/usr/bin/env python3
"""Byte-level anchor check for proposal 055, and application to a COPY of the tree outside the repository.

usage: python -I apply_check.py <repo-root>                 report pins, anchors, EOLs, hashes; writes nothing
       python -I apply_check.py <repo-root> --copy [DIR]     copy namcg-book7.tex, chapters/, bib/ into a NEW
                                                            DIR (default C:/Users/redgi/tmp/055_apply_r1),
                                                            apply the single insertion there, print realized
                                                            size/sha256; refuses if DIR exists (no second run),
                                                            refuses any path inside the repository.

E1 inserts appH_insert.tex as its own paragraph between the merged 054 paragraph and the Status paragraph
of the Problem E ledger block. Anchor (exact bytes, count must be 1):
    CRLF CRLF CRLF \paragraph{Status.} CRLF Remains Assumption~\ref{ass:lorentzian}.
Replacement keeps one blank line between the 054 paragraph and the new paragraph and the original two blank
lines before \paragraph{Status.}:  CRLF CRLF + crlf(insert) + CRLF CRLF CRLF + Status-tail.
Pins of the current working tree (verified 2026-11-07): appH 537324 B sha256 943816e923a844521faf56fc88774cd0827eca501f69bb7b12dc9f4af18e8571,
bib 25976 B sha256 a651fe603183fbd91d18e4da30e0a29fd09843621ce86b3effb661dcd51dc42b, appH CRLF 3206 bare-LF 0.
No bib additions in this package (the insert contains no \cite and no \ref/\label).
"""
import sys, pathlib, hashlib, shutil
HERE = pathlib.Path(__file__).resolve().parent
CR, LF = b"\r", b"\n"
APPEND_TAIL = rb"\paragraph{Status.}" + CR + LF + rb"Remains Assumption~\ref{ass:lorentzian}."
ANCHOR = CR + LF + CR + LF + CR + LF + APPEND_TAIL
MARK54 = rb"Exponential observables \(\operatorname{Tr}\mathrm e^{\mathrm ik^\mu A_\mu}\) at \(N=2\)"
MARK55 = rb"The slice at \(k\ne0\): refinement of the window and model-level growth control."
APPH_SHA = "943816e923a844521faf56fc88774cd0827eca501f69bb7b12dc9f4af18e8571"
APPH_SIZE = 537324
BIB_SHA = "a651fe603183fbd91d18e4da30e0a29fd09843621ce86b3effb661dcd51dc42b"
BIB_SIZE = 25976
def lf(b): return b.replace(CR + LF, LF)
def crlf(b): return lf(b).replace(LF, CR + LF)
def eol(name, b):
    print(f"{name}: size {len(b)} CRLF {b.count(CR+LF)} bare-LF {b.count(LF)-b.count(CR+LF)} "
          f"sha256 {hashlib.sha256(b).hexdigest()}")
def main():
    root = pathlib.Path(sys.argv[1]).resolve()
    apph = (root / "chapters" / "appH-microscopic-proofs.tex").read_bytes()
    bib = (root / "bib" / "namcg.bib").read_bytes()
    ok_apph = len(apph) == APPH_SIZE and hashlib.sha256(apph).hexdigest() == APPH_SHA
    ok_bib = len(bib) == BIB_SIZE and hashlib.sha256(bib).hexdigest() == BIB_SHA
    print(f"PIN appH size {APPH_SIZE} sha256 {APPH_SHA[:16]}... matches: {ok_apph}")
    print(f"PIN bib  size {BIB_SIZE} sha256 {BIB_SHA[:16]}... matches: {ok_bib}")
    eol("appH working file", apph)
    eol("bib  working file", bib)
    print("054 paragraph present (prerequisite for this insert):", apph.count(MARK54))
    print("055 paragraph already present (must be 0):", apph.count(MARK55))
    print("anchor count (must be 1):", apph.count(ANCHOR))
    print("bare Status tail count (context):", apph.count(APPEND_TAIL))
    ins = lf((HERE / "appH_insert.tex").read_bytes())
    print("insert ASCII-only:", all(c < 128 for c in ins),
          "| bare-LF after LF-normalising:", ins.count(LF) - ins.count(CR + LF),
          "| trailing-LF count:", ins.count(LF))
    eol("insert, LF form", ins)
    eol("insert, CRLF form", crlf(ins))
    no_cite = b"\\cite" not in ins and b"\\ref{" not in ins and b"\\label{" not in ins
    print("insert contains no \\cite, no \\ref, no \\label:", no_cite)
    exp = len(apph) + len(crlf(ins)) + 2 * len(CR + LF)
    print("expected realized size after insertion:", exp)
    if "--copy" in sys.argv:
        i = sys.argv.index("--copy")
        d = pathlib.Path(sys.argv[i + 1]).resolve() if len(sys.argv) > i + 1 else pathlib.Path(r"C:/Users/redgi/tmp/055_apply_r1")
        if root in d.parents or d == root:
            sys.exit("refusing to write inside the repository")
        if d.exists():
            sys.exit(f"refusing second run: {d} already exists (delete it manually if you intend a fresh copy)")
        (d / "chapters").mkdir(parents=True)
        (d / "bib").mkdir(parents=True)
        shutil.copy2(root / "namcg-book7.tex", d / "namcg-book7.tex")
        for p in (root / "chapters").glob("*.tex"):
            shutil.copy2(p, d / "chapters" / p.name)
        shutil.copy2(root / "bib" / "namcg.bib", d / "bib" / "namcg.bib")
        if (root / "figs").is_dir():
            shutil.copytree(root / "figs", d / "figs")
        (d / "frontmatter").mkdir(exist_ok=True)
        for p in (root / "frontmatter").glob("*.tex"):
            shutil.copy2(p, d / "frontmatter" / p.name)
        if (root / "namcg-book7.bbl").is_file():
            shutil.copy2(root / "namcg-book7.bbl", d / "namcg-book7.bbl")
        f = d / "chapters" / "appH-microscopic-proofs.tex"
        x = f.read_bytes()
        assert x == apph, "copy differs from working tree"
        assert x.count(ANCHOR) == 1 and x.count(MARK54) == 1 and x.count(MARK55) == 0, "anchor counts wrong in copy"
        x = x.replace(ANCHOR, CR + LF + CR + LF + crlf(ins) + ANCHOR)
        f.write_bytes(x)
        print("applied to copy:", d)
        eol("appH after", x)
        print("bare LF after application (must be 0):", x.count(LF) - x.count(CR + LF))
        print("new anchor for the 055 paragraph now present once:", x.count(MARK55))
        print("Status tail still present once:", x.count(APPEND_TAIL))
        print("bib untouched in copy:", hashlib.sha256((d / "bib" / "namcg.bib").read_bytes()).hexdigest() == BIB_SHA)
        print("namcg-book7.tex untouched:", (d / "namcg-book7.tex").read_bytes() == (root / "namcg-book7.tex").read_bytes())
main()
