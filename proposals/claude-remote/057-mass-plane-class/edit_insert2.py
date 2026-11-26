#!/usr/bin/env python3
"""Second set of wording edits to appH_insert.tex (symbol clash c -> kappa in (iii); wording of the family)."""
import os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'appH_insert.tex')
s = open(p, encoding='utf-8').read()
reps = [
    (r"and let \(\Lambda_j\) be end points of paths as above for \((\epsilon_j,\gamma_j)\) that converge to an invertible \(\Lambda_\infty\), with \(h_\infty\) its \(h\).",
     r"and let \(\Lambda_j\) be the end points of paths as above for \((\epsilon_j,\gamma_j)\), converging to an invertible \(\Lambda_\infty\) with \(h=h_\infty\)."),
    (r"\(\operatorname{Re}M_{\gamma_j}/|\epsilon_j+\mathrm i\gamma_j'|\to-\operatorname{Im}h_\infty\), which is therefore positive semidefinite.",
     r"\(\operatorname{Re}M_{\gamma_j}/|\epsilon_j+\mathrm i\gamma_j'|\to-\operatorname{Im}h_\infty\), with \(\epsilon_jc\) in place of \(\epsilon_j\) for the regulator of (ii), which is therefore positive semidefinite."),
    (r"So \(\operatorname{Im}h_\infty=-c\,vv^{\mathrm T}\) with \(c\ge0\) and \(v\) real.",
     r"So \(\operatorname{Im}h_\infty=-\kappa\,vv^{\mathrm T}\) with \(\kappa\ge0\) and \(v\) real."),
]
for o, nw in reps:
    c = s.count(o)
    if c == 0 and s.count(nw) == 1:
        print('already applied:', o[:50])
        continue
    assert c == 1, o[:60]
    s = s.replace(o, nw)
    print('applied:', o[:50])
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('bytes', len(s.encode('utf-8')))
