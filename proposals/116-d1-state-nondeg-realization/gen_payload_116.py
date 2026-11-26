# gen_payload_116.py -- byte-exact generator for insert-d1-state-nondeg.tex
# SINGLE-LINE LaTeX paragraph (matching the long-line style of the ordinal-43
# paragraph at appH L1711), CRLF-terminated, ASCII, no BOM, no tabs, no
# backslash immediately followed by a whitespace byte.
# ROUND 2 (review-r1 Findings 1 and 6): the false "for \mu-almost every point,
# with an explicit bound on the measure of the complement" clause is replaced
# by the gatekeeper's corrected measure-upper-bound clause (applied VERBATIM
# from review-r1.md "Corrected snippet"), and "an identity for a set of
# singular values" is replaced by the Finding 6 wording.
# Run: python -I gen_payload_116.py      (from the proposal folder)
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "insert-d1-state-nondeg.tex")

LINE = (
    r"\emph{State-route realization of the pointwise bound.} Write "
    r"\(r(\Phi):=\min_{U}\|\Phi-vU\|\) for the operator-norm distance from "
    r"\(\Phi\) to the vacuum manifold \(v\,\mathrm U(4)\) of "
    r"Equation~\eqref{eq:vacuum-manifold}, the minimum running over unitary "
    r"\(U\). By the polar decomposition and Weyl's singular-value inequality, "
    r"\(r=\max_i|\sigma_i-v|\) exactly, the minimum attained at the polar "
    r"factor, and on \(r\le v\) the function~\eqref{eq:V} obeys the sharp "
    r"two-sided estimate \((\lambda/4)\,r^2(2v-r)^2\le\mathcal V\le"
    r"\lambda\,r^2(2v+r)^2\), the upper bound attained at the uniform radial "
    r"deviation \(\Phi=(v+r)\,\Omega\) with \(\Omega\) unitary and the lower "
    r"bound at singular values \((v-r,v,v,v)\). Hence "
    r"\(\mathcal V\le\varepsilon\le\lambda v^4/4\) forces "
    r"\(r\le r_\varepsilon:=v-\sqrt{v^2-2\sqrt{\varepsilon/\lambda}}\), which "
    r"equals \(v\) at \(\varepsilon=\lambda v^4/4\) and re-derives the "
    r"threshold \(\inf\{\mathcal V:\det\Phi=0\}=\lambda v^4/4\) as the "
    r"statement that defect points lie at distance at least \(v\) from the "
    r"vacuum manifold, equality being attained at \((0,v,v,v)\), and it gives "
    r"\(|\det e|\ge(1-r/v)^4\ge(1-r_\varepsilon/v)^4\), the last factor equal "
    r"to the recorded \((1-\sqrt{4\varepsilon/\lambda}/v^2)^2\). Moreover "
    r"\(\sup\{\mathcal V:r\le\delta\}=\lambda\,\delta^2(2v+\delta)^2\), "
    r"attained at uniform radial deviation, and this is below the defect "
    r"threshold if and only if \(\delta<\delta_*:=(\sqrt{6}-2)\,v/2\), with "
    r"equality of the supremum and the threshold at \(\delta=\delta_*\); "
    r"consequently every configuration field with "
    r"\(\sup_x r(\Phi(x))<\delta_*\) realizes the pointwise bound "
    r"\(\mathcal V<\lambda v^4/4\) everywhere, with "
    r"\(|\det e|\ge(1-\delta/v)^4\). In measure form, for any field on any "
    r"measure space with \(E_{\mathcal V}:=\int\mathcal V\,d\mu<\infty\), "
    r"Markov's inequality and the threshold give "
    r"\(\mu\{x:\det e(x)=0\}\le\mu\{\mathcal V\ge\lambda v^4/4\}\le "
    r"4E_{\mathcal V}/(\lambda v^4)\), attained as an identity on any region "
    r"where the singular values are \((0,v,v,v)\), and "
    r"\(\mu\{|\det e|<(1-\sqrt{4\varepsilon/\lambda}/v^2)^2\}\le "
    r"E_{\mathcal V}/\varepsilon\) for every "
    r"\(0<\varepsilon<\lambda v^4/4\); consequently the sets "
    r"\(\{\mathcal V\ge\lambda v^4/4\}\) and \(\{x:\det e(x)=0\}\) have "
    r"\(\mu\)-measure at most \(4E_{\mathcal V}/(\lambda v^4)\), and every "
    r"configuration of finite potential energy, in particular every "
    r"finite-potential-energy classical solution of Equation~\eqref{eq:Phi-eom} "
    r"on a slice, realizes \(\mathcal V<\lambda v^4/4\) and the non-vanishing "
    r"determinant of Assumption~\ref{ass:nondeg} off a set of at most that "
    r"measure, which is null when \(E_{\mathcal V}=0\) and cannot in general "
    r"be improved, saturation being attained on a region where the singular "
    r"values are \((0,v,v,v)\). Scope: these are "
    r"geometric statements about configurations of the displayed "
    r"Presentation-B potential read through Equation~\eqref{eq:vev-is-frame}; "
    r"the radius \(\delta_*\) is a fluctuation certificate and not a spectral "
    r"gap, and it bounds neither the indefinite \(\eta\)-contracted quadratic "
    r"diagnostic recorded above for the locked block nor the quantum "
    r"stability of the minimum; no state of the matrix theory and no "
    r"integration measure is constructed; the bilocal composite reading above "
    r"is not covered, because pointwise singular-value bounds do not control "
    r"the smallest singular value of a two-point kernel; the small-measure "
    r"exception obtained when \(E_{\mathcal V}>0\) is a fortiori not the "
    r"pointwise statement of Assumption~\ref{ass:nondeg} and does not "
    r"discharge it; the selection of Equation~\eqref{eq:V} by "
    r"Presentation~A remains the missing input of "
    r"Section~\ref{sec:ch3-relate}; and Assumptions~\ref{ass:frame-lock} "
    r"and~\ref{ass:nondeg} remain assumed, so Problem~D remains OPEN and "
    r"PROGRAMME-CONDITIONAL."
)

data = LINE.encode("ascii") + b"\r\n"   # encode('ascii') rejects non-ASCII
assert b"\n" not in LINE.encode("ascii")
with open(OUT, "wb") as f:
    f.write(data)

# ---- control-byte scan of the written file ----
raw = open(OUT, "rb").read()
cr = raw.count(b"\r"); lf = raw.count(b"\n")
crlf = raw.count(b"\r\n")
bad_c0 = sum(1 for b in raw if b < 0x20 and b not in (0x0D, 0x0A))
lone_cr = len(re.findall(b"\r(?!\n)", raw))
lone_lf = len(re.findall(b"(?<!\r)\n", raw))
tab = raw.count(b"\t")
bs_ws = len(re.findall(b"\\[ \t\r\n]", raw))
ends = raw.endswith(b"\r\n")
nonascii = sum(1 for b in raw if b > 0x7E)
print("bytes %d CR %d LF %d CRLF %d loneCR %d loneLF %d badC0 %d tab %d "
      "backslash+ws %d nonascii %d endsCRLF %s" %
      (len(raw), cr, lf, crlf, lone_cr, lone_lf, bad_c0, tab, bs_ws,
       nonascii, ends))
assert cr == lf == crlf == 1 and lone_cr == 0 and lone_lf == 0 and bad_c0 == 0 \
    and tab == 0 and bs_ws == 0 and nonascii == 0 and ends
print("PAYLOAD SCAN OK")
