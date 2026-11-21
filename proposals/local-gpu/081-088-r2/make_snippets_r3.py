"""081-088 r3: write insert_r3.tex (insert_r2.tex with the review-r2 replacements (a)-(c) applied
verbatim) and rowlen_r3.txt (old and new text of replacement (d) in the Row length paragraph), CRLF,
UTF-8 without BOM. clause_r2.txt and closing_r2.tex are unchanged and reused.
Run: python -I proposals/local-gpu/081-088-r2/make_snippets_r3.py
"""
import hashlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
CRLF = b'\r\n'

REPL = [
    (r"\(D_{\mathrm{eff}}=29.5\) at \(N=400\), \(M=N/2\), \(l_c=40\) and \(f=\nu l/2\) (numerical)",
     r"\(D_{\mathrm{eff}}=38.0\) at \(N=400\), \(M=N/2\), \(l_c=40\) and \(f=\nu l/2\) (numerical)"),
    (r"since distinct entries carry distinct charges under that rotation;",
     r"since the entries carry distinct nonzero charges of one sign under that rotation;"),
    (r"The reading of the rows from the edge data in the transplanted selection rule therefore matches the averaged charge moments exactly at the second moment,",
     r"The reading of the rows from the edge data in the transplanted selection rule therefore matches the averaged charge moments at \(a=0\) exactly at the second moment,"),
]
D_OLD = r"with \(W\) the sum over the boundary row inside the block."
D_NEW = (r"with \(W\) the sum over the boundary row inside the block without its entry at \(u\), while "
         r"\(\tfrac12\langle\operatorname{Tr}Q^{2}\rangle\) is \(4s^{2}\) times the full sum (exact).")


def main():
    ins = (HERE / 'insert_r2.tex').read_bytes()
    for old, new in REPL:
        o, n = old.encode('utf-8'), new.encode('utf-8')
        assert ins.count(o) == 1, old
        ins = ins.replace(o, n)
    assert ins.count(b'\n') == ins.count(CRLF) and not ins.startswith(b'\xef\xbb\xbf')
    (HERE / 'insert_r3.tex').write_bytes(ins)
    (HERE / 'rowlen_r3.txt').write_bytes((D_OLD + '\r\n' + D_NEW + '\r\n').encode('utf-8'))
    for n in ('insert_r3.tex', 'rowlen_r3.txt'):
        b = (HERE / n).read_bytes()
        print(n, len(b), 'B sha256', hashlib.sha256(b).hexdigest())


if __name__ == '__main__':
    main()
