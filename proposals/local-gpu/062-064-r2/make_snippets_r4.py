r"""Build block_C_r4.tex and block_F_r4.tex from the r3 blocks by three verbatim wording replacements
(review-r3 finding 1; scan-pass-4 findings 1 and 2). Run: python -I make_snippets_r4.py
Each old string must occur exactly once; outputs are CRLF, UTF-8 without BOM, no trailing newline."""
import hashlib, os
HERE = os.path.dirname(os.path.abspath(__file__))
def rd(n): return open(os.path.join(HERE, n), 'rb').read().decode('utf-8')
def sha(s): return hashlib.sha256(s.encode('utf-8')).hexdigest()
C_REPL = [
 ('S4-1', r'including the induced Einstein--Hilbert term,', r'including the induced Einstein--Hilbert contribution,'),
 ('S4-2', r'and its pole mass, or a ratio \(m_\psi/v\), as a derived output,',
          r'and its pole mass, or a ratio \(m_\psi/v\), as a derived output, together with the coupling that can be compared with Cassini bounds,'),
]
F_REPL = [
 ('R3-1', r'\(E_1(s_\Lambda\mathcal D)>2c_J/15\vartheta\mathcal D\)', r'\(E_1(s_\Lambda\mathcal D)>2c_J/(15\vartheta\mathcal D)\)'),
]
for src, dst, repl in (('block_C_r3.tex', 'block_C_r4.tex', C_REPL), ('block_F_r3.tex', 'block_F_r4.tex', F_REPL)):
    t0 = rd(src); t = t0
    assert t.count('\n') == t.count('\r\n') and not t.endswith('\n')
    for name, old, new in repl:
        n = t.count(old)
        print(f'{dst} {name}: old occurs {n}')
        assert n == 1, name
        t = t.replace(old, new)
        assert t.count(new) == 1
    assert t.count('\n') == t.count('\r\n') and not t.endswith('\n')
    assert len(t) - len(t0) == sum(len(b) - len(a) for _, a, b in repl)
    open(os.path.join(HERE, dst), 'wb').write(t.encode('utf-8'))
    print(dst, len(t.encode('utf-8')), 'bytes sha', sha(t))
