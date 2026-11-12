#!/usr/bin/env python3
"""Wording edits applied to appH_insert.tex during drafting (each old string must occur once)."""
import os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'appH_insert.tex')
s = open(p, encoding='utf-8').read()
reps = [
    (r"Along a path as above all these planes for \(\operatorname{Re}h_\varphi\) therefore have one class at each \(\tau\)",
     r"Along a path as above \(\operatorname{Re}h_\varphi\) has at least eight positive eigenvalues by (i), so all planes on which it is positive definite have one class at each \(\tau\)"),
    (r"By (i), at least eight diagonal entries of \(\operatorname{Re}h_\varphi=-T^{\mathrm T}\operatorname{diag}(\operatorname{Re}\mathrm e^{\mathrm i\varphi}d_\mu)T\) are positive.",
     r"Since \(\operatorname{Re}h_\varphi=-T^{\mathrm T}\operatorname{diag}(\operatorname{Re}\mathrm e^{\mathrm i\varphi}d_\mu)T\), (i) and the law of inertia give \(-\operatorname{Re}\mathrm e^{\mathrm i\varphi}d_\mu>0\) for at least eight \(\mu\)."),
    (r"is not joined to the Hermitian contour, and no contour joined to it has a damped limit at \(N=2\).",
     r"is not joined to the Hermitian contour, and at \(N=2\) no contour joined to it, fixed or convergent as \(\epsilon\to0\), has a limit on which the integrand at \(\epsilon=0\) is absolutely integrable."),
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
