"""Proposal 066: read-only simulation of the integration of insert-r1.tex into
chapters/appH-microscopic-proofs.tex and of bib_additions.bib into
bib/namcg.bib.  Nothing is written; the script only predicts the post-state
byte size, sha256 and line-ending counts, and asserts the pre-states and the
uniqueness of every anchor it relies on.  Run with:  python -I simulate_apply.py
"""
import hashlib
import re

APP = "../../chapters/appH-microscopic-proofs.tex"   # relative to this folder
BIB = "../../bib/namcg.bib"
INS = "insert-r1.tex"
BIBADD = "bib_additions.bib"

# ---- pre-state certification ------------------------------------------------
raw = open(APP, "rb").read()
assert len(raw) == 589388, len(raw)
assert hashlib.sha256(raw).hexdigest() == \
    "d94b79458c3e3613992ed66b8ac12024db84f6f44910ebc0d1e0081e14dafe3d"
crlf = raw.count(b"\r\n")
bare = raw.count(b"\n") - crlf
assert crlf == 3450 and bare == 0, (crlf, bare)
print("appH pre : size", len(raw), "sha256", hashlib.sha256(raw).hexdigest())
print("appH pre : CRLF", crlf, "bare LF", bare)

s = raw.decode("utf-8")

anchors = [
    "\\paragraph{Conditional lemma: occupation of one modular ladder.}",
    "where \\(d\\mu_{g_{\\mathrm N}}\\) includes the mode weights coupling",
    "its source dependence must also be calculated.",
    "In particular, reconcile the convention",
    "uniquely select \\(\\nu_{\\sqrt{}}\\). Problem~H remains open.",
]
for a in anchors:
    assert s.count(a) == 1, (a, s.count(a))
assert s.count("\\paragraph{Missing step.}") == 9
print("appH anchors: each count 1; '\\paragraph{Missing step.}' count 9")

# ---- insert ------------------------------------------------------------------
ins = open(INS, "rb").read()
assert ins.count(b"\r\n") == 0 and ins.endswith(b"\n")
block = ins[:-1].replace(b"\n", b"\r\n")          # drop trailing LF, CRLF body
title = ("\\paragraph{Bounded obstruction: analytic source dependence "
         "reproduces the exponential-linear class.}")
assert block.count(title.encode()) == 1
assert b"\\label{" not in ins
for k in [b"Longo2022Weyl", b"Kato1966", b"Jacobson2016", b"JacobsonVisser2019"]:
    assert ins.count(k) == 1, k

marker = "its source dependence must also be calculated.".encode()
pat = marker + b"\r\n\r\n"
assert s.encode().count(pat) == 1
new = raw.replace(pat, pat + block + b"\r\n\r\n", 1)

assert new.count("\\paragraph{Missing step.}".encode()) == 9
assert new.count(title.encode()) == 1
ncrlf = new.count(b"\r\n")
nbare = new.count(b"\n") - ncrlf
print("appH post: size", len(new), "sha256", hashlib.sha256(new).hexdigest())
print("appH post: CRLF", ncrlf, "bare LF", nbare,
      "(insert bytes", len(block), "+ separator 4)")
assert len(new) == 589388 + len(block) + 4
assert nbare == 0

# ---- bib ---------------------------------------------------------------------
bib = open(BIB, "rb").read()
assert len(bib) == 31789
assert hashlib.sha256(bib).hexdigest() == \
    "9e9dfa0617f90b9dae1dd3c94eabd584a22db3cd18c138719e91d7b46b9b6429"
bcrlf = bib.count(b"\r\n")
assert bcrlf == 1050 and bib.count(b"\n") - bcrlf == 0 and bib.endswith(b"\r\n")
keys = re.findall(rb"@[\w]+\{([^,]+),", bib)
assert len(keys) == 99 and len(set(keys)) == 99
print("bib pre  : size", len(bib), "entries", len(keys), "CRLF", bcrlf)

add = open(BIBADD, "rb").read()
assert add.count(b"\r\n") == 0 and add.endswith(b"\n")
blk = add[:-1].replace(b"\n", b"\r\n")
newkeys = re.findall(rb"@[\w]+\{([^,]+),", blk)
assert len(newkeys) == 2 and not (set(newkeys) & set(keys))
newbib = bib + b"\r\n" + blk + (b"" if blk.endswith(b"\r\n") else b"\r\n")
nbc = newbib.count(b"\r\n")
print("bib post : size", len(newbib), "entries",
      len(re.findall(rb"@[\w]+\{([^,]+),", newbib)), "CRLF", nbc,
      "bare LF", newbib.count(b"\n") - nbc)
print("new keys :", [k.decode() for k in newkeys])
