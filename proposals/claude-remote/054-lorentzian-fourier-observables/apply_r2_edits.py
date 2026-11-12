#!/usr/bin/env python3
"""Applies review-r1 findings F1-F4 verbatim to appH_insert.tex.  Keeps the r1 bytes as appH_insert.r1.tex and
refuses a second run (if appH_insert.r1.tex exists).  Each old string must occur exactly once."""
import os, sys, hashlib
H = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(H, 'appH_insert.tex'); R1 = os.path.join(H, 'appH_insert.r1.tex')
R1_SHA = '4f5c1301f41864be3a7f89fc0c742aad7a03b4ad4007a22b1fd5f44d02be5bd1'
if os.path.exists(R1):
    sys.exit("appH_insert.r1.tex already exists; nothing written")
b = open(P, 'rb').read()
if hashlib.sha256(b).hexdigest() != R1_SHA:
    sys.exit("appH_insert.tex is not the r1 insert; nothing written")
s = b.decode('ascii')
E = [
 (r"so the integral of (i) on \(\mathcal R_u\) defines \(\mathcal J(\kappa)\) for \(0<\arg\kappa<3\pi/4\),",
  r"so the integral of (i) on \(\mathcal R_u\), divided by \(I^{(u)}[1]\), defines \(\mathcal J(\kappa)\) for \(0<\arg\kappa<3\pi/4\), where \(I^{(u)}[1]\) is independent of \(u\in(0,2)\) by the Stokes argument of the preceding paragraph with the phase of the auxiliary factor on \(\operatorname{Tr}A_0^2\) chosen for each interval of \(u\),"),
 (r"It does not derive a signature, a background, a frame or the fermion content, and Assumption~\ref{ass:lorentzian} is not discharged. Problem~E remains open and PROGRAMME-CONDITIONAL.",
  r"Assumption~\ref{ass:lorentzian} is not discharged by this either, and Problem~E keeps its ledger label."),
 (r"The same construction at \(u=1\) gives the Euclidean expectation value of \(O\) with every factor replaced by \(\mathrm e^{\mathrm iK\tilde A_\mu}\).",
  r"At \(u=1\) the same choice of \(\kappa\) makes the integral on \(\mathcal R_1\) at \(\epsilon=0\) the Euclidean expectation value of \(O\) with every factor replaced by \(\mathrm e^{\mathrm iK\tilde A_\mu}\); this is an identity of integrands, not a limit of \(I_\epsilon\)."),
 (r"With \(k^\mu k_\mu=\mp\kappa^2\) for the two cases,",
  r"With \(k^\mu=\kappa\delta^\mu_0\) and \(k^\mu=\kappa\delta^\mu_j\), so that \(k^\mu k_\mu=\mp\kappa^2\),"),
]
for old, new in E:
    if s.count(old) != 1:
        sys.exit("old string not unique: "+old[:60])
for old, new in E:
    s = s.replace(old, new)
out = s.encode('ascii')
open(R1, 'wb').write(b)
open(P, 'wb').write(out)
print("r1 kept:", len(b), hashlib.sha256(b).hexdigest())
print("r2 written:", len(out), hashlib.sha256(out).hexdigest())
