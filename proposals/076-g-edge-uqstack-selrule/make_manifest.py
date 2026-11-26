"""076: manifest generator (read-only over the proposal folder).

Prints a markdown table row per file (bytes, sha256) for every file in the
proposal folder except make_manifest.py and manifest.md themselves.

Run: python -I proposals/076-g-edge-uqstack-selrule/make_manifest.py
"""
import hashlib
import os
import sys

sys.stdout.reconfigure(encoding='ascii', errors='backslashreplace')
HERE = os.path.dirname(os.path.abspath(__file__))
skip = {'make_manifest.py', 'manifest.md'}
for name in sorted(os.listdir(HERE)):
    p = os.path.join(HERE, name)
    if not os.path.isfile(p) or name in skip:
        continue
    d = open(p, 'rb').read()
    print('| %s | %d | %s |' % (name, len(d), hashlib.sha256(d).hexdigest()))
