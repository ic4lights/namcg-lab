#!/usr/bin/env python3
"""Apply review-r1 Findings 1-7 verbatim to appH_insert.tex (proposal 055).
Requires the r1 insert hash; keeps the r1 bytes as appH_insert.r1.tex; each old string must occur exactly once."""
import os, sys, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
INS = os.path.join(HERE, 'appH_insert.tex')
R1 = os.path.join(HERE, 'appH_insert.r1.tex')
R1_SHA = 'ca32f19296b2645a12936ce2732b1c9d092277badcfac16ca53c3710538de5b1'
if os.path.exists(R1):
    sys.exit("appH_insert.r1.tex already exists; nothing written")
b = open(INS, 'rb').read()
if hashlib.sha256(b).hexdigest() != R1_SHA:
    sys.exit("insert is not the r1 insert; stop")
s = b.decode('ascii')
EDITS = [
 ("F1", r"and let \(V(h,q)=W(h,q)/W(h,0)\).", r"and let \(V(h,q)=2W(h,q)/W(h,0)\)."),
 ("F2", r"the contour integrals with bounded Fourier modes are therefore at \(N=2\) values of",
        r"the contour integrals with \(h\in\mathfrak C_0\) and bounded Fourier modes are therefore at \(N=2\) values of"),
 ("F3", r"are exactly the nonzero causal ones, \(k^\mu k_\mu\le0\).",
        r"are exactly the nonzero causal ones, \(k^\mu k_\mu\le0\). Contours with \(h\in-\mathfrak C_0\) do make the mode bounded at real timelike \(k\), for example \(A_0=X_0\), \(A_i=\mathrm e^{2\pi\mathrm i/3}X_i\) at \(k^\mu=\kappa\delta^\mu_0\), with the value \(F_{\mathrm E}(\mathrm e^{\mathrm i\pi/4}\kappa^2)\) at \(N=2\), but by (ii) no path along which \(h\) stays in the closure of \(\mathfrak C\) joins them to the Hermitian contour."),
 ("F4", r"For \(h\in\mathfrak C_0\) the directions \(\mathrm e^{-\mathrm i\beta_\mu}\) lie in an open half-plane, so \(k^\mu k_\mu\) lies in the sector",
        r"For \(h\in\mathfrak C_0\) the pairwise conditions, applied with a third index, put the arguments \(-\beta_\mu\) of the directions \(\mathrm e^{-\mathrm i\beta_\mu}\) in an interval of length less than \(\pi\) inside \((-\pi,\pi/2)\), so \(k^\mu k_\mu\neq0\) lies in the sector"),
 ("F5", r"so no signature is derived, Assumption~\ref{ass:lorentzian} is not discharged, and Problem~E keeps its ledger label.",
        r"so no signature is derived and Assumption~\ref{ass:lorentzian} is not discharged."),
 ("F6", r"zero components of \(q\) follow by continuity", r"zero components of \(T^{-\mathrm T}q\) follow by continuity in \(q\)"),
 ("F7", r"Let \(\Lambda(\tau)\), \(0\le\tau\le1\), be continuous,", r"Let \(\Lambda(\tau)\), \(0\le\tau\le1\), be piecewise continuously differentiable,"),
]
for tag, old, new in EDITS:
    c = s.count(old)
    print(tag, "old count", c)
    if c != 1:
        sys.exit(tag + ": old string not unique; nothing written")
    s = s.replace(old, new)
for tag, old, new in EDITS:
    print(tag, "new count", s.count(new))
open(R1, 'wb').write(b)
open(INS, 'wb').write(s.encode('ascii'))
print("wrote", INS, len(s.encode('ascii')), "bytes sha256", hashlib.sha256(s.encode('ascii')).hexdigest())
