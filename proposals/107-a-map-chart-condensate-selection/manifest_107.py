# manifest_107.py -- lists every file in the proposal folder (size, sha256/16;
# manifest.md itself excluded) plus the LIVE chapters/appH triple. Read-only.
import hashlib
import os

D = r"proposals\107-a-map-chart-condensate-selection"
A = r"chapters\appH-microscopic-proofs.tex"
for f in sorted(os.listdir(D)):
    if f == "manifest.md":
        continue
    b = open(os.path.join(D, f), "rb").read()
    print("%-38s %8d %s" % (f, len(b), hashlib.sha256(b).hexdigest()[:16]))
a = open(A, "rb").read()
print("LIVE appH: size %d sha256/16 %s CRLF %d"
      % (len(a), hashlib.sha256(a).hexdigest()[:16], a.count(b"\r\n")))
