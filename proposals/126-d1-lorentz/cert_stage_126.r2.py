# cert_stage_126.r2.py -- stage the round-2 item-108 certificate tree OUTSIDE the repo
# (new dir name; never deleted). Copy of the v3 cert recipe (out-cert-126-v3.txt lineage):
# namcg-book7.tex + frontmatter/ + bib/ + figs/ + chapters/ (stale *.aux excluded), with
# chapters/appH-microscopic-proofs.tex replaced by appH-spliced-126-v3.tex (hash-asserted).
import hashlib
import os
import shutil
import sys

REPO = "C:/Users/redgi/Projects/namcg-lab@gpu"
DEST = "C:/Users/redgi/AppData/Local/Temp/build126_cert_v4_12620"
SPL = "appH-spliced-126-v3.tex"
SPL_SHA1 = "123108d4a94723be1dbad752883125baac940fe4"
SPL_LEN = 880023

assert not os.path.exists(DEST), "cert dir must be new"
os.makedirs(DEST)
shutil.copy2(REPO + "/namcg-book7.tex", DEST + "/namcg-book7.tex")
for d in ("frontmatter", "bib", "figs", "chapters"):
    shutil.copytree(REPO + "/" + d, DEST + "/" + d,
                    ignore=shutil.ignore_patterns("*.aux", "__pycache__"))
data = open(SPL, "rb").read()
assert hashlib.sha1(data).hexdigest() == SPL_SHA1 and len(data) == SPL_LEN, "v3 splice pin"
open(DEST + "/chapters/appH-microscopic-proofs.tex", "wb").write(data)
staged = open(DEST + "/chapters/appH-microscopic-proofs.tex", "rb").read()
assert hashlib.sha1(staged).hexdigest() == SPL_SHA1, "staged appH hash mismatch"
assert not any(f.endswith(".aux") for _, _, fs in os.walk(DEST) for f in fs), "stale aux staged"
print("STAGE-OK", DEST)
print("STAGED-APPH-SHA1", hashlib.sha1(staged).hexdigest(), len(staged))
