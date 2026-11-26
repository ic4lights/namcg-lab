"""MINOR-4 cleanup: replace the stale 4*tr(X^3) comment (and the
'every other reading is not a scalar' clause contradicted by stage3
T5c) in ecg_cas_lib.py's cubic_P docstring. Byte-level patch: only the
docstring bytes change; no code bytes change. Comment-only, so no
shipped .out can depend on it (verified by re-running stage1/stage3).

Run:  python -I proposals/068-j-spherical-reduction-consistency/patch_lib_docstring.py
"""
import hashlib
import os

p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ecg_cas_lib.py')
data = open(p, 'rb').read()
print('pre  bytes %d sha256 %s CRLF %d bareLF %d'
      % (len(data), hashlib.sha256(data).hexdigest(),
         data.count(b'\r\n'), data.count(b'\n') - data.count(b'\r\n')))
old = (b"contraction (the bivector-chain cube); every other reading "
       b"leaves\n    unpaired lower slots and is not a scalar.  Chain "
       b"is computed as\n    4*tr(X^3) on the antisymmetric-pair basis "
       b"(M2 is antisymmetric in\n    its first two slots for a "
       b"Levi-Civita connection).")
new = (b"contraction (the bivector-chain cube); a slot-shifted reading "
       b"that\n    still pairs all slots (g^{cp} R^a_{p b d}) is a "
       b"different scalar (stage3\n    T5c), while naive readings of "
       b"the printed slots leave unpaired lower\n    slots.  Chain is "
       b"computed as 8*tr(X^3) on the antisymmetric-pair basis\n    "
       b"(M2 is antisymmetric in its first two slots for a Levi-Civita\n"
       b"    connection; verified symbolically, c1 - 8*trX3 = 0).")
assert data.count(old) == 1, ('anchor count', data.count(old))
out = data.replace(old, new, 1)
open(p, 'wb').write(out)
print('post bytes %d sha256 %s CRLF %d bareLF %d'
      % (len(out), hashlib.sha256(out).hexdigest(),
         out.count(b'\r\n'), out.count(b'\n') - out.count(b'\r\n')))
