# manifest_105.py -- list every file in the proposal folder with size and sha256/8.
# Run from repo root: python -I proposals/105-a-map-order2-associator-correction/manifest_105.py
import hashlib
import os
import sys

D = r"proposals\105-a-map-order2-associator-correction"
names = sorted(n for n in os.listdir(D) if os.path.isfile(os.path.join(D, n)) and n != "manifest.md")
for n in names:
    b = open(os.path.join(D, n), "rb").read()
    print("%-38s %8d  %s" % (n, len(b), hashlib.sha256(b).hexdigest()[:8]))
print("appH live: %8d  %s  CRLF %d" %
      (lambda b: (len(b), hashlib.sha256(b).hexdigest()[:8], b.count(b"\r\n")))(
          open(r"chapters\appH-microscopic-proofs.tex", "rb").read()))
sys.exit(0)
