"""068-j-spherical-reduction-consistency: manifest of the proposal folder.

Prints size and sha256 of every file in the proposal folder (excluding
__pycache__ and this file's own output). Re-run after any edit; the
gatekeeper can compare against the manifest quoted in proposal-rK.md (the latest round present at run time).

Run:
  python -I proposals/068-j-spherical-reduction-consistency/verify_manifest.py
"""
import hashlib
import os
import sys

sys.stdout.reconfigure(encoding='ascii', errors='backslashreplace')
D = os.path.dirname(os.path.abspath(__file__))
names = []
for root, dirs, files in os.walk(D):
    dirs[:] = [x for x in dirs if x != '__pycache__']
    for f in files:
        p = os.path.join(root, f)
        names.append(os.path.relpath(p, D).replace('\\', '/'))
for name in sorted(names):
    b = open(os.path.join(D, name), 'rb').read()
    print('%8d %s %s' % (len(b), hashlib.sha256(b).hexdigest(), name))
