"""Build appH_insert_r3.tex from appH_insert_r2.tex by the exact replacements of round 3
(gatekeeper review-r2 snippets H and SC2, verbatim; each asserted to occur once).
Output CRLF, UTF-8 without BOM.  Run: python -I make_insert_r3.py"""
import hashlib
import re
from pathlib import Path
here = Path(__file__).resolve().parent
s = (here / 'appH_insert_r2.tex').read_bytes().decode('utf-8').replace('\r\n', '\n')
H_OLD = (r"On the algebra of (ii) the wider ansatz \(w_a{}^{cd}=k_a(aB^{cd}+\zeta N^{cd}+xN'^{cd})\) solves all three brackets for all real \(\kappa,a,\zeta,x\): \(\mathsf T_{ac}{}^c=a\,k_a\), the only nonzero pair of \(\mathsf F\) is \(\mathsf F_{13}=\tfrac12a\kappa\), the only nonzero pair of \(\mathsf R\) is \(\mathsf R_{13}{}^{cd}=\kappa(aB^{cd}+\zeta N^{cd}+xN'^{cd})\), and \(\mathsf R_{abcd}\mathsf R^{abcd}=-4a^2\kappa^2\), \(\mathsf R_{ab}{}^{ab}=0\), \(\mathsf T_{abc}\mathsf T^{abc}=2\kappa^2\) (exact for the section values; for the operators on the bundle at random Lorentz \(u\), including the order-zero part, residual below \(10^{-15}\)). For \(a\neq0\) it is an exact solution with \(\mathsf R_{abcd}\mathsf R^{abcd}\neq0\) on a unimodular algebra.")
H_NEW = (r"On the algebra of (ii) the wider ansatz \(w_a{}^{cd}=k_a(\chi B^{cd}+\zeta N^{cd}+xN'^{cd})\) solves all three brackets for all real \(\kappa,\chi,\zeta,x\): \(\mathsf T_{ac}{}^c=\chi\,k_a\), the only nonzero pair of \(\mathsf F\) is \(\mathsf F_{13}=\tfrac12\chi\kappa\), the only nonzero pair of \(\mathsf R\) is \(\mathsf R_{13}{}^{cd}=\kappa(\chi B^{cd}+\zeta N^{cd}+xN'^{cd})\), and \(\mathsf R_{abcd}\mathsf R^{abcd}=-4\chi^2\kappa^2\), \(\mathsf R_{ab}{}^{ab}=0\), \(\mathsf T_{abc}\mathsf T^{abc}=2\kappa^2\) (exact for the section values; for the operators on the bundle at random Lorentz \(u\), including the order-zero part, residual below \(10^{-15}\)). For \(\chi\kappa\neq0\) it is an exact solution with \(\mathsf R_{abcd}\mathsf R^{abcd}\neq0\) on a unimodular algebra.")
R = [
 ('H', H_OLD, H_NEW),
 ('SC2', r"its extension with \(a\neq0\)", r"its extension with \(\chi\neq0\)"),
]
for tag, old, new in R:
    assert s.count(old) == 1, (tag, s.count(old))
    s = s.replace(old, new)
    print('replacement', tag, 'applied once')
# checks: no parameter a left (the old parameter patterns), chi count
BS = chr(92)
for pat in ['(aB^', 'kappa,a,', '=a'+BS+',k_a', '12a'+BS+'kappa', '4a^2', '(a'+BS+'neq0', '('+'a'+BS+')']:
    assert pat not in s, pat
print('old parameter-a patterns remaining: 0')
print('\chi occurrences in insert:', s.count('\chi'))
b = s.replace('\n', '\r\n').encode('utf-8')
assert not b.startswith(b'\xef\xbb\xbf')
(here / 'appH_insert_r3.tex').write_bytes(b)
print('appH_insert_r3.tex bytes', len(b), 'sha256', hashlib.sha256(b).hexdigest(), 'bare LF', b.count(b'\n') - b.count(b'\r\n'))
