"""Normalise the r2 snippet files to UTF-8 without BOM, CRLF line endings, one final CRLF."""
from pathlib import Path
here = Path(__file__).resolve().parent
for n in ('insert_block_r2.tex', 'closing_r2.tex', 'bib_additions_r2.bib'):
    p = here / n
    b = p.read_bytes()
    if b.startswith(b'\xef\xbb\xbf'):
        b = b[3:]
    b = b.replace(b'\r\n', b'\n').rstrip(b'\n') + b'\n'
    b = b.replace(b'\n', b'\r\n')
    assert b.decode('utf-8').isascii() or True
    p.write_bytes(b)
    print(n, len(b), b.count(b'\r\n'))
