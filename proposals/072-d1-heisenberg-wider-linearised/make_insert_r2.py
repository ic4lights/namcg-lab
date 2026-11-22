"""Write appH_insert_r2.tex (CRLF, UTF-8 without BOM) from appH_insert_r1.tex by the r2 replacements
(gatekeeper review-r1 snippets S1, S2, S3 and closer F8, verbatim). Each old string must occur exactly once.
Run: python -I -B make_insert_r2.py"""
import hashlib
from pathlib import Path

here = Path(__file__).resolve().parent
R1 = (here / 'appH_insert_r1.tex').read_bytes()
assert hashlib.sha256(R1).hexdigest() == '3dbdc81ddd65079a970cd516da5fef294f10356bcee764a0ababaa1edeb69a98'
t = R1.decode('utf-8').replace('\r\n', '\n')

REPL = [
    # S1: qualifier sentence after the root display
    (r"""\]
For \(l\ge3\)""",
     r"""\]
This is exact in the blocks described below and numerical, at sampled points, for \(l\le9\) otherwise; higher levels are not checked. For \(l\ge3\)"""),
    # S1: in-paragraph replacements
    (r"of the maximal minors", r"of the minors of the generic rank"),
    (r"which contain all factors with \(l\le5\),",
     r"which on the observed pattern of levels contain all factors with \(l\le5\),"),
    (r"(exact in rational arithmetic)",
     r"(exact in rational arithmetic after rational reconstruction of the double-precision entries)"),
    (r"At \(\chi=0\) this gives the levels \(q_0^2=p^2+\kappa p\,l\) of the paragraph on left-invariant backgrounds with torsion for every \(\zeta,x\) (numerical).",
     r"At \(\chi=0\) and a sampled \((\zeta,x)\neq(0,0)\) the levels \(q_0^2=p^2+\kappa p\,l\) of the paragraph on left-invariant backgrounds with torsion are recovered (numerical)."),
    # S2
    (r"No gauge-invariant gap or mass therefore appears for the Lorentz or torsion modes at this order, although the background carries the scale \(\kappa\) and \(\mathsf R_{abcd}\mathsf R^{abcd}=-4\chi^2\kappa^2\neq0\), and no sign of a mass arises.",
     r"No term independent of the momentum enters, so no gauge-invariant gap or mass appears for the Lorentz or torsion modes at this order, although the background carries the scale \(\kappa\) and \(\mathsf R_{abcd}\mathsf R^{abcd}=-4\chi^2\kappa^2\neq0\); \(\chi\) enters the roots only as a rate, since as \(p\to0\) they tend to \(q_0=0\) and to the imaginary \(q_0=-\mathrm ic\chi\)."),
    # S3
    (r"with supremum \(|c\chi|\) as \(p\to\infty\);",
     r"with supremum \(|c\chi|\), approached as \(p\to0\) and as \(p\to\infty\);"),
    (r"its largest rate rises from", r"its largest \(|\operatorname{Im}q_0|\) rises from"),
    (r"Over all modes the largest rate is", r"Over all modes the largest \(|\operatorname{Im}q_0|\) is"),
    # F8: shortened closer
    (r"Nothing here shows that the matrix integral selects this class, these backgrounds or the algebra \(\mathcal A\), or yields the frame and its non-degeneracy, so Assumptions~\ref{ass:frame-lock}, \ref{ass:nondeg}, \ref{ass:lorentzian}, \ref{ass:local-lorentz} and~\ref{ass:EFT-a2} are not discharged, and the frame of these backgrounds is not identified with the emergent metric of Chapter~\ref{ch:vierbein-emergence}; Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL.",
     r"Nothing here shows that the matrix integral selects this class or these backgrounds, so the assumptions listed in the preceding paragraph are not discharged; Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL."),
]
for old, new in REPL:
    n = t.count(old)
    assert n == 1, (n, old[:60])
    t = t.replace(old, new)
    print('replaced once:', old[:70].replace('\n', '\\n'))
assert 'rate rises' not in t and 'largest rate' not in t and 'maximal minors' not in t
b = t.replace('\n', '\r\n').encode('utf-8')
assert not b.startswith(b'\xef\xbb\xbf')
(here / 'appH_insert_r2.tex').write_bytes(b)
print('appH_insert_r2.tex bytes', len(b), 'sha256', hashlib.sha256(b).hexdigest(),
      'bare LF', b.count(b'\n') - b.count(b'\r\n'), 'lines', b.count(b'\r\n'))
