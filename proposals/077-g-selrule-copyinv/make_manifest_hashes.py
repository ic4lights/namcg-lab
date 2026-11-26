"""077: print sha8 + size for every file in the folder (manifest support).

Run: python -I proposals/077-g-selrule-copyinv/make_manifest_hashes.py
"""
import hashlib
import os

D = os.path.dirname(os.path.abspath(__file__))
for f in sorted(os.listdir(D)):
    p = os.path.join(D, f)
    if not os.path.isfile(p):
        continue
    b = open(p, "rb").read()
    print("%s | %d | %s" % (f, len(b), hashlib.sha256(b).hexdigest()[:8]))
print("HASHES DONE")
