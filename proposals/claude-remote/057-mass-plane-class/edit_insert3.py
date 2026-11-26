#!/usr/bin/env python3
"""Third wording edit to appH_insert.tex (antecedent of 'which')."""
import os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'appH_insert.tex')
s = open(p, encoding='utf-8').read()
o = r"with \(\epsilon_jc\) in place of \(\epsilon_j\) for the regulator of (ii), which is therefore positive semidefinite."
nw = r"with \(\epsilon_jc\) in place of \(\epsilon_j\) for the regulator of (ii), so \(-\operatorname{Im}h_\infty\) is positive semidefinite."
if s.count(o) == 1:
    s = s.replace(o, nw)
    print('applied')
else:
    assert s.count(nw) == 1
    print('already applied')
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('bytes', len(s.encode('utf-8')))
