SCAN-PASS 3/4: ISSUES (gatekeeper, 2026-11-19)
Read in full: ch01-ch09 (line 1 to last line).

Finding 1 (minor): ch01 L249-259 becomes stale. It says without qualification that stationarity "is a Ward identity of the microscopic theory". Insert (ii) contradicts this, and it was already in tension with ch06 L51-56 and ch07 L329-330.

Fix: replace L257-259 ("is not an extra thermodynamic slogan. ... forbids \(m_T^2\neq 0\) in the infrared.") with:
```
is not an extra thermodynamic slogan. It enters as the load-bearing
hypothesis of the framework, Assumption~\ref{ass:EE}, used in the form
of the conditional entanglement Ward identity of
Proposition~\ref{prop:ward}; under that hypothesis the identity forbids
\(m_T^2\neq 0\) in the infrared. Its derivation from the matrix theory
remains open (Problem~\ref{sec:status-B}).
```

Consistent, no change needed:
- ch06: ass:EE, prop:ward (conditional), fixed volume, replica
- ch07: L154-159 and L315-331; the L326 ref resolves
- ch05 L318-322 and L412-419
- ch02 L454-458
- ch03, ch04, ch08, ch09

No duplicate labels or titles.

Optional wording (not required): "the flat Lebesgue measure on the matrix entries, with the action of Equation~\eqref{eq:Smatrix}".
