#!/usr/bin/env python3
"""Apply review-r1 replacements R1-R7 (R5 in two parts) verbatim to appH_insert.tex (proposal 056).
Requires the r1 hash, checks each old string occurs once before and each new string once after, keeps the r1
bytes as appH_insert.r1.tex, and refuses a second run."""
import os, sys, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
INS = os.path.join(HERE, 'appH_insert.tex'); R1F = os.path.join(HERE, 'appH_insert.r1.tex')
R1_SHA = 'b58cda7e76d7fbb8cb395789e7edf9c94238305a7b1965f888366af6fa58056c'
E = [
 ("R1", r"With \(M\) now the matrix of this form on the contour, \((\epsilon+\mathrm i\gamma')h=M-2\epsilon\ell\ell^{\mathrm T}\).",
        r"Write \(M_\gamma=\epsilon\Lambda^{\mathrm T}\Lambda+\mathrm i\gamma'h\) for the matrix of this form on the contour; then \((\epsilon+\mathrm i\gamma')h=M_\gamma-2\epsilon\ell\ell^{\mathrm T}\)."),
 ("R2", r"while by the identity above it has at most one when \(\operatorname{Re}M\) is positive semidefinite.",
        r"while by the identity above it has at most one when \(\operatorname{Re}M_\gamma\) is positive semidefinite."),
 ("R3", r"every linear contour on which \(I_\epsilon[1]\) converges absolutely has \(\operatorname{Re}M\) positive semidefinite.",
        r"every linear contour on which \(I_\epsilon[1]\) converges absolutely has \(\operatorname{Re}M\) positive semidefinite, and the same argument applies to \(\Lambda^{\mathrm T}P\Lambda\) and to \(M_\gamma\)."),
 ("R4", r"In particular, paths along which \(\operatorname{Re}\mathrm iS_{\mathrm b}\le0\) while \(h\) leaves the closure of \(\mathfrak C\) do not reach \(-\mathfrak C_0\).",
        r"In particular, no path along which \(\operatorname{Re}\mathrm iS_{\mathrm b}\le0\) while \(h\) leaves the closure of \(\mathfrak C\) ends on a contour with \(h\in-\mathfrak C_0\) on which the regulated integrand is absolutely integrable."),
 ("R5a", r"which is the limit of the first paragraph.", r"which is the limit of the paragraph on the regulated Lorentzian integral."),
 ("R5b", r"The first paragraph gives this limit", r"That paragraph gives this limit"),
 ("R6", r"Definition~(A) or a regulator as in (i), \(\gamma\le0\),", r"Definition~(A) with \(\gamma\le0\) or a regulator as in (i) with \(\gamma=0\),"),
 ("R7", r"The inertia found in (i) is that of the \(\eta\) put into \(S_{\mathrm b}\), so no signature is derived and Assumption~\ref{ass:lorentzian} is not discharged.",
        r"The inertia found in (i) is that of the \(\eta\) put into \(S_{\mathrm b}\), which the regulator carries over to every admissible contour but does not select, so Assumption~\ref{ass:lorentzian} is still required."),
]
if os.path.exists(R1F):
    sys.exit("appH_insert.r1.tex already exists; nothing written")
b = open(INS, 'rb').read()
if hashlib.sha256(b).hexdigest() != R1_SHA:
    sys.exit("insert is not the r1 bytes; nothing written")
s = b.decode('ascii')
for k, o, n in E:
    c = s.count(o); print(k, "old count", c)
    assert c == 1, k
    s = s.replace(o, n)
for k, o, n in E:
    c = s.count(n); print(k, "new count", c)
    assert c == 1, k
open(R1F, 'wb').write(b)
nb = s.encode('ascii'); open(INS, 'wb').write(nb)
print("r1 kept:", len(b), hashlib.sha256(b).hexdigest())
print("r2 insert:", len(nb), hashlib.sha256(nb).hexdigest())
