"""050 s6: mechanics of appH_insert.tex. Prints only. Finds the manuscript through NAMCG_REPO or the nearest
ancestor holding it, otherwise prints SKIPPED for the checks against the manuscript."""
import hashlib
import os
import re

here = os.path.dirname(os.path.abspath(__file__))
raw = open(os.path.join(here, "appH_insert.tex"), "rb").read()
print("bytes", len(raw), "sha256", hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest(), "(LF form)")
print("ASCII", all(b < 128 for b in raw), "CR", raw.count(b"\r"), "BOM", raw[:3] == b"\xef\xbb\xbf")
s = raw.decode("ascii")
print("paragraph blocks", len([p for p in s.split("\n\n") if p.strip()]))
print("new labels", re.findall(r"\\label\{([^}]*)\}", s))
print("status sentence count", s.count("remain open and PROGRAMME-CONDITIONAL"))
words = ["we ", "proposal", "gatekeeper", "researcher", "as proposed", "this package", "round ", "avenue", "script"]
print("process-word scan", [w for w in words if w in s.lower()])
refs = sorted(set(re.findall(r"\\(?:ref|eqref)\{([^}]*)\}", s)))
cites = sorted(set(c.strip() for g in re.findall(r"\\cite\{([^}]*)\}", s) for c in g.split(",")))
print("refs", refs)
print("cites", cites)


def find():
    r = os.environ.get("NAMCG_REPO")
    if r and os.path.isfile(os.path.join(r, "namcg-book7.tex")):
        return r
    d = here
    while True:
        if os.path.isfile(os.path.join(d, "namcg-book7.tex")):
            return d
        n = os.path.dirname(d)
        if n == d:
            return None
        d = n


repo = find()
if repo is None:
    print("SKIPPED: manuscript not found for anchor, label and cite counts")
else:
    all_tex = ""
    for f in sorted(os.listdir(os.path.join(repo, "chapters"))):
        if f.endswith(".tex"):
            all_tex += open(os.path.join(repo, "chapters", f), encoding="utf-8").read()
    apph = open(os.path.join(repo, "chapters", "appH-microscopic-proofs.tex"), encoding="utf-8").read()
    print("anchor count", apph.count(r"\section{Problem E: signature}"))
    for r in refs:
        print("  label", r, all_tex.count(r"\label{" + r + "}"))
    bib = open(os.path.join(repo, "bib", "namcg.bib"), encoding="utf-8").read()
    for c in cites:
        print("  bib", c, bib.count("{" + c + ","))
    newbib = open(os.path.join(here, "new_bib_entries.bib")).read()
    print("keys in new_bib_entries.bib:", re.findall(r"@\w+\{([^,]*),", newbib))
