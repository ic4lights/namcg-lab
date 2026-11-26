"""Write appH_insert_r3.tex (CRLF, UTF-8 without BOM) from appH_insert_r2.tex by one replacement:
the closing sentence becomes the gatekeeper review-r2 F1 text, verbatim. The old string must occur once.
Run: python -I -B make_insert_r3.py"""
import hashlib
from pathlib import Path

here = Path(__file__).resolve().parent
R2 = (here / 'appH_insert_r2.tex').read_bytes()
assert hashlib.sha256(R2).hexdigest() == '01b5d27a25bb8c19904ed13f26f29aae6b33d813bd66e11d3d63bbad01a42513'
t = R2.decode('utf-8').replace('\r\n', '\n')

OLD = (r"Nothing here shows that the matrix integral selects this class or these backgrounds, so the assumptions "
       r"listed in the preceding paragraph are not discharged; Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL.")
NEW = (r"Nothing here shows that the matrix integral selects this class, these backgrounds or the algebra \(\mathcal A\), "
       r"so the assumptions listed in the preceding paragraph are not discharged, and the frame of these backgrounds is not "
       r"identified with the emergent metric of Chapter~\ref{ch:vierbein-emergence}; Problems~D, F and~N remain open and "
       r"PROGRAMME-CONDITIONAL.")
assert t.count(OLD) == 1, t.count(OLD)
assert t.rstrip('\n').endswith(OLD), "closer is not the last sentence of the block"
t = t.replace(OLD, NEW)
print('replaced once: closer (F1)')
b = t.replace('\n', '\r\n').encode('utf-8')
assert not b.startswith(b'\xef\xbb\xbf')
(here / 'appH_insert_r3.tex').write_bytes(b)
print('appH_insert_r3.tex bytes', len(b), 'sha256', hashlib.sha256(b).hexdigest(),
      'bare LF', b.count(b'\n') - b.count(b'\r\n'), 'lines', b.count(b'\r\n'))
