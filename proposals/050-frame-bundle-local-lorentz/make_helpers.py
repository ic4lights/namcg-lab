"""One-shot helper of round 1: applied four text edits to appH_insert.tex and derived compile_check.py and
s6_insert_mechanics.py from the 049 versions. Refuses to run twice (the edits assert the old text once)."""
import os
here = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(here, 'appH_insert.tex')
s = open(p, encoding='ascii', newline='').read()
reps = [
 (r"Keep Equation~\eqref{eq:Smatrix} with \(C_{\mu\nu\lambda}=0\) and change only the Hermitian operators.",
  r"Keep Equation~\eqref{eq:Smatrix} with \(C_{\mu\nu\lambda}=0\) and, except where a fermion is named, without the matter term, and change only the Hermitian operators."),
 (r"A base on which all of \(\mathfrak{so}(3,1)\) acts vertically would be an \(\mathrm{SO}(4,1)\)-equivariant map onto \(\mathrm{SO}(4,1)/\mathrm{SO}(3,1)\); none exists,",
  r"An \(\mathrm{SO}(4,1)\)-equivariant base on which a copy of \(\mathfrak{so}(3,1)\) acts vertically would be a map of the sheet onto \(\mathrm{SO}(4,1)/\mathrm{SO}(3,1)\); none exists,"),
 (r"so Assumptions~\ref{ass:frame-lock}, \ref{ass:nondeg} and~\ref{ass:lorentzian} are not discharged and Assumption~\ref{ass:local-lorentz} is replaced only within this class.",
  r"so Assumptions~\ref{ass:frame-lock}, \ref{ass:nondeg} and~\ref{ass:lorentzian} are not discharged; Assumption~\ref{ass:local-lorentz}, a statement about the action~\eqref{eq:Smicro}, is not derived, since this class is not shown to reproduce Presentation~B."),
 (r"\(y^\mu,M^{\mu\nu},T^\mu\) with \(y^4\) separate the points of the leaf.",
  r"\(y^\mu,M^{\mu\nu},T^\mu\) with \(y^4\), a function of \(y^\mu\) on the sheet, separate the points of the sheet."),
]
for a, b in reps:
    assert s.count(a) == 1, 'already applied or anchor missing: ' + a[:50]
    s = s.replace(a, b)
open(p, 'w', encoding='ascii', newline='\n').write(s)
d49 = os.path.join(here, '..', '049-k-scale-dilaton-response')
c = open(os.path.join(d49, 'compile_check.py'), encoding='utf-8').read()
c = c.replace('compile_check (049)', 'compile_check (050)').replace('new_bib_entry.bib', 'new_bib_entries.bib').replace(r'\section{Problem G: HBEV}', r'\section{Problem E: signature}')
open(os.path.join(here, 'compile_check.py'), 'w', encoding='utf-8', newline='\n').write(c)
m = open(os.path.join(d49, 's6_insert_mechanics.py'), encoding='utf-8').read()
m = m.replace('049 s6', '050 s6').replace('new_bib_entry.bib', 'new_bib_entries.bib').replace('Problem G: HBEV', 'Problem E: signature')
old = 'print("key in new_bib_entries.bib:", newbib.split("{")[1].split(",")[0])'
assert m.count(old) == 1
m = m.replace(old, r'print("keys in new_bib_entries.bib:", re.findall(r"@\w+\{([^,]*),", newbib))')
open(os.path.join(here, 's6_insert_mechanics.py'), 'w', encoding='utf-8', newline='\n').write(m)
print('applied')
