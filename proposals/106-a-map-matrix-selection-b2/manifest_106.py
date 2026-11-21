# manifest_106.py -- list every file in the proposal folder with size and sha256/16.
# Run from repo root: python -I proposals/106-a-map-matrix-selection-b2/manifest_106.py
import hashlib
import os
import sys

D = r"proposals\106-a-map-matrix-selection-b2"
names = sorted(n for n in os.listdir(D) if os.path.isfile(os.path.join(D, n)) and n != "manifest.md")
for n in names:
    b = open(os.path.join(D, n), "rb").read()
    print("%-38s %8d  %s" % (n, len(b), hashlib.sha256(b).hexdigest()[:16]))
print("appH live: %8d  %s  CRLF %d" %
      (lambda b: (len(b), hashlib.sha256(b).hexdigest()[:16], b.count(b"\r\n")))(
          open(r"chapters\appH-microscopic-proofs.tex", "rb").read()))
sys.exit(0)
