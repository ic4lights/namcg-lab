"""
074 r3: build appH_insert_r3.tex from appH_insert_r2.tex (kept) by
  F1 (scan-pass-2): cross-reference to the vacuum-term display of the scale-of-K paragraph;
  W  (review-r2 optional wording): scope-sentence list without the double 'and'.
Each old string must occur exactly once.  Run:  python -I make_insert_r3.py
"""
import hashlib
from pathlib import Path

here = Path(__file__).resolve().parent
r2 = (here / "appH_insert_r2.tex").read_text(encoding="utf-8")
assert "\r" not in r2

R = [
    ("F1 display reference",
     r"is not among the terms of the displays of the two preceding paragraphs.",
     r"is not among the terms of the vacuum-term display of that paragraph or of the displays of the two preceding paragraphs."),
    ("W scope wording",
     r"with the supplied bilinear term and the matter fields at their vanishing background and \(C_{\mu\nu\lambda}=0\) on \(M\)",
     r"with the supplied bilinear term, the matter fields at their vanishing background and \(C_{\mu\nu\lambda}=0\) on \(M\)"),
]
txt = r2
for name, old, new in R:
    n = txt.count(old)
    print(f"{name}: old occurs {n}x")
    assert n == 1, name
    txt = txt.replace(old, new)
    assert txt.count(new) == 1
assert txt.count("PROGRAMME-CONDITIONAL") == 1 and txt.rstrip().endswith("remain open and PROGRAMME-CONDITIONAL.")
assert all(ord(c) < 128 for c in txt) and txt.endswith(".\n\n")
(here / "appH_insert_r3.tex").write_bytes(txt.encode("utf-8"))
print("appH_insert_r3.tex bytes", len(txt.encode()), "sha256(LF)", hashlib.sha256(txt.encode()).hexdigest())
