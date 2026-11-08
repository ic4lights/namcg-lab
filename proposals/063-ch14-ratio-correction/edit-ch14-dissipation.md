# Edit file for chapters/ch14-dissipation.tex (proposal 063, round 1)

Authoritative strings: `apply_check.py` (backslashes built from `chr(92)`; lines joined with CRLF).
The text below is the same content for reading. Each OLD occurs exactly once in the baseline;
each NEW occurs zero times before and once after (see `apply_check_output.txt`).

- Baseline (working tree = HEAD for this file): 16520 bytes, sha256 `d6883ca33d0cebd7e78162cdc0b49e0faffac9ac07bd986119ca4a09a3872d36`, CRLF=397, bare LF=0, bare CR=0, no BOM, no trailing whitespace.
- Result: 17336 bytes, sha256 `b1fefa684669f0315e705061a9efd84c732eca741e687b9f3a88977f2f976dd2`, CRLF=411, bare LF=0, bare CR=0, no BOM, no trailing whitespace.

## Block 1 (sec:ch14-quad, baseline lines 243-258)

OLD (lines 243-258, from "For a circular Newtonian orbit" through "Solar-System tests."):

```latex
For a circular Newtonian orbit, \(v^2=\Geff M/d\) and
\(\Omega^2=\Geff M/d^3\), so
\begin{equation}
  \label{eq:ratio}
  \frac{P_{\mathrm{ent}}}{P_{\mathrm{GW}}}
  \;\sim\;
  \frac{\eta}{\Geff^3 M^2\mu}\,
  \Bigl(\frac{d}{\Geff M}\Bigr)^{k}
\end{equation}
with a positive power of \(d\) that makes the ratio \emph{grow}
toward wide separations if \(\eta\) is held fixed. That conclusion
is an artefact of treating \(\eta\) as constant down to laboratory
distances. If \(\eta\) is instead suppressed at wide separations, the
growth need not occur; this book does not calculate that dependence,
and a sufficiently small \(\eta\) is required for consistency with
Solar-System tests.
```

NEW:

```latex
For a circular Newtonian orbit, \(v^2=\Geff M/d\) and
\(\Omega^2=\Geff M/d^3\), so both powers fall as \(d^{-5}\) and
\begin{equation}
  \label{eq:ratio}
  \frac{P_{\mathrm{ent}}}{P_{\mathrm{GW}}}
  \;\sim\;
  \frac{5}{32}\,
  \frac{\eta}{\Geff^3 M^2\mu},
\end{equation}
up to the inclination factors in~\eqref{eq:Peters}. With \(\eta\)
constant on a given inspiral, as in Assumption~\ref{ass:drag}, this
ratio does not depend on \(d\): the working law singles out no
separation at which the entropic channel overtakes the quadrupole
channel, and the comparison is fixed by \(\eta\) and the masses.
Because both losses have the same dependence on \(d\), and hence on
the orbital frequency, the extra loss multiplies the leading-order
quadrupole frequency evolution by the constant factor
\(1+P_{\mathrm{ent}}/P_{\mathrm{GW}}\). At that order it is
degenerate with a rescaling of the chirp mass
\(\mathcal M=\mu^{3/5}M^{2/5}\) to
\((1+P_{\mathrm{ent}}/P_{\mathrm{GW}})^{3/5}\mathcal M\).
For a drag falling as \(d^{-n}\) the same computation gives a ratio
proportional to \(d^{4-n}\); a ratio that grows toward wide
separations would require \(n<4\), which
Assumption~\ref{ass:drag} does not adopt. This book does not
calculate whether \(\eta\) differs between regimes, and a
sufficiently small \(\eta\) is required for consistency with
Solar-System tests.
```

Kept: everything before line 243 (eq:Peters, eq:Pent) and from line 259 ("The intended domain of~\eqref{eq:Fdiss} is:") onward. The label `eq:ratio` is kept (one occurrence; no `\ref`/`\eqref` to it anywhere in `chapters/`). The prefactor \(\eta/(\Geff^3M^2\mu)\) of the old display is kept and given its computed factor \(5/32\); the undetermined factor \((d/\Geff M)^k\) is removed because \(k=0\).

## Block 2 (sec:ch14-exercises, exercise "Energy identity", baseline lines 367-368)

OLD:

```latex
    inspiral and estimate a separation where the two powers
    could be comparable for a chosen \(\eta\).
```

NEW:

```latex
    inspiral, show that their ratio does not depend on \(d\), and
    find the value of \(\eta\), in terms of the masses, at which the
    two powers are comparable. For which drag exponents would the
    ratio depend on separation?
```

Kept: lines 363-366 of the exercise ("\item \textbf{Energy identity.} ... Compare with \(\mathrm{d}U_{\mathrm{N}}/\mathrm{d}t\) along a Peters").
