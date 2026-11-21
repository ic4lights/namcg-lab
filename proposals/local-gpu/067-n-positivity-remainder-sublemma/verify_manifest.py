# verify_manifest.py -- proposal 067, round 2. READ-ONLY.
# Confirms, against the working tree: (1) every cite key used by insert-r2.tex exists in
# bib/namcg.bib; (2) every \ref label used by insert-r2.tex is defined exactly once in
# chapters/*.tex; (3) the marker strings used by simulate_apply.py occur exactly once in
# appH, and the closer sentences stay intact; (4) the insert adds no new labels or refs
# beyond those checked. Run from repo root: python -I proposals/067-n-positivity-remainder-sublemma/verify_manifest.py
import glob
import hashlib
import re

APP = "chapters/appH-microscopic-proofs.tex"
INS = "proposals/067-n-positivity-remainder-sublemma/insert-r2.tex"
BIB = "bib/namcg.bib"

ins = open(INS, encoding="utf-8").read()
bib = open(BIB, encoding="utf-8").read()
app = open(APP, encoding="utf-8", newline="").read()

keys = set()
for m in re.finditer(r"\\cite\{([^}]*)\}", ins):
    keys.update(k.strip() for k in m.group(1).split(","))
refs = sorted(set(re.findall(r"\\ref\{([^}]*)\}", ins)))
labels_new = re.findall(r"\\label\{([^}]*)\}", ins)

# Finding 3 (review r1) fixed: the earlier crude boolean ("@"+k in bib) printed False
# for existing keys; the regex entry-count below is the authoritative check (count 1
# means exactly one bib entry @<type>{<key>,).
print("cite keys used by insert:", sorted(keys))
for k in sorted(keys):
    n = len(re.findall(r"@\w+\{" + re.escape(k) + r"[,\s]", bib))
    print(f"  bib entries for {k}: {n}")
print("\\ref keys used:", refs)
for r in refs:
    cnt = 0
    for f in glob.glob("chapters/*.tex"):
        cnt += open(f, encoding="utf-8", errors="replace").read().count("\\label{" + r + "}")
    print(f"  \\label{{{r}}} defined in chapters/*.tex: {cnt}")
print("new \\label added by insert:", labels_new)

marker_a = ("are a complex-conjugate pair with \\(|k^2|\\approx3.9\\LUV^2\\).\r\n\r\n"
            "These statements are conditional on the truncated identity, the\r\n")
old_c = ("These statements are conditional on the truncated identity, the\r\n"
         "continuation and common limits stated, massless sectors (massive\r\n"
         "sectors require the threshold functions of Problem~F), and the use of\r\n"
         "the leading-logarithmic form factor up to \\(|k^2|\\sim\\LUV^2\\), where\r\n"
         "the derivative expansion is not controlled.")
print()
print("marker_a count:", app.count(marker_a))
print("old_c count:", app.count(old_c))
print("closer 'is not implied by the metric being composite.' count:",
      app.count("is not implied by the metric being composite."))
print("closer 'Problems~F and~N remain open.' count:",
      app.count("Problems~F and~N remain open."))
i = app.find("Problems~F and~N remain open.")
print("context around block closer:", repr(app[i - 120:i + 40]))
print("count 'Remains Assumption~\\ref{ass:EFT-a2}':",
      app.count("Remains Assumption~\\ref{ass:EFT-a2}"))
print("count '\\paragraph{Missing step.}':", app.count("\\paragraph{Missing step.}"))
print("insert anchors used: none on 'Missing step' lines:",
      "Missing step" not in marker_a and "Missing step" not in old_c)
h = hashlib.sha256(open(APP, "rb").read()).hexdigest()
print("appH sha256:", h)
print("DONE")
