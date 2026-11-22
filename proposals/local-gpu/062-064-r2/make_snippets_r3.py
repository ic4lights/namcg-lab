r"""Build block_C_r3.tex and block_F_r3.tex from the r2 blocks by the review-r2 replacements F1-F6, C1
(verbatim) and the optional item 6 sentence. Run: python -I make_snippets_r3.py
Each old string must occur exactly once; outputs are CRLF, UTF-8 without BOM, no trailing newline."""
import hashlib, os
HERE = os.path.dirname(os.path.abspath(__file__))
def rd(n): return open(os.path.join(HERE, n), 'rb').read().decode('utf-8')
def sha(s): return hashlib.sha256(s.encode('utf-8')).hexdigest()

C_REPL = [
 ('C1a', r'the gauge-fixed quadratic scalar operator', r'the full quadratic scalar operator'),
 ('C1b', r'and its pole mass as a derived output,', r'and its pole mass, or a ratio \(m_\psi/v\), as a derived output,'),
]
F_REPL = [
 ('F1', r'and the tree term carries \(\rho_M\), which does not respond at fixed \(\chi\).',
        r'and the tree potential \(\rho_MV_{\mathrm t}/g^2\) carries \(\rho_M\), which does not respond at fixed \(\chi\).'),
 ('F2', r'within the recorded content these are the second-order parts of \(U_2\) and of the fibre-constant part of the first term, and the part of the first term with the fibre flux, at first and at second order, none of which is computed.',
        r'within the recorded content these are the second-order parts of \(U_2\) and of the fibre-constant part of the first term, the part of the first term with the fibre flux, at first and at second order, and the tree non-derivative terms of the wave, which the leading symbol of the tree form drops, none of which is computed.'),
 ('F3', r', whose value and sign depend on \(s_\Lambda\), and that of \(U_2\) exceeds it by \(p\,U_2\);',
        r', whose value depends on \(s_\Lambda\) through \(E_1\), the bracket at each level being positive exactly when \(E_1(s_\Lambda\mathcal D)>2c_J/15\vartheta\mathcal D\), and that of \(U_2\) exceeds it by \(p\,U_2\sigma_1\);'),
 ('F4', r'The identity at a stationary background is exact for these forms, the density of the first term is exact for the level form at the stated limit, and the change of sign with \(s_\Lambda\) is numerical at sampled values.',
        r'The identity at a stationary background is exact for these forms, and the density of the first term is exact for the level form at the stated limit.'),
 ('F5a', r'exceeds the profile of \(\sqrt{|g|}\) by \(-p\,(', r'exceeds the profile of \(\sqrt{|g|}\) by \(\sigma_1\) times \(-p\,('),
 ('F5b', r'the response of \(Y\) is finite, with the summand', r'the coefficient of \(\sigma_1\) in the response of \(Y\) is finite, with the summand'),
 ('F6', r'With the exchange of \(\chi\) of the preceding paragraph, the denominator',
        r'With the exchange of \(\chi\) of the preceding paragraph, for \(q^2\) below \(m_\chi^2\), the denominator'),
 ('item6', r'With them set to zero the pole of this term has the tachyonic sign.',
        r'With them set to zero the pole of this term has the tachyonic sign for either sign of \(\hat U\), so at a stationary background the sign of \(\hat U\) does not decide it.'),
]
for src, dst, repl in (('block_C_r2.tex', 'block_C_r3.tex', C_REPL), ('block_F_r2.tex', 'block_F_r3.tex', F_REPL)):
    t = rd(src)
    assert '\r\n' not in t.replace('\r\n', '') and t.count('\n') == t.count('\r\n')
    for name, old, new in repl:
        n = t.count(old)
        print(f'{dst} {name}: old occurs {n}')
        assert n == 1, name
        t = t.replace(old, new)
        assert t.count(new) == 1
    assert t.count('\n') == t.count('\r\n') and not t.endswith('\n')
    open(os.path.join(HERE, dst), 'wb').write(t.encode('utf-8'))
    print(dst, len(t.encode('utf-8')), 'bytes sha', sha(t))
