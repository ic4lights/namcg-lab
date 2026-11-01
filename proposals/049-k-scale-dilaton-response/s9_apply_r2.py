"""049 r2 s9: build appH_insert.tex from appH_insert.r1.tex. Old strings R1-R20 come from repl_old.r1.txt (line k = Rk,
the gatekeeper's file, copied unchanged); E1-E5 are additional replacements of this round. Every old string must occur
exactly once at its turn; on any mismatch the script stops without writing. Prints the outcome only."""
import hashlib
import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, "appH_insert.r1.tex"), "rb").read()
assert hashlib.sha256(src).hexdigest() == "13879e6c3546c135f8645b85b540a0a460a7f1003b0c36d0738a241ba7266a5a", "r1 bytes changed"
text = src.decode("ascii")
lines = open(os.path.join(here, "repl_old.r1.txt"), encoding="ascii", newline="").read().replace("\r\n", "\n").split("\n")
old = {k + 1: lines[k] for k in range(20)}

new = {}
new[1] = r"So, while the loop expansion is controlled, a value \(\beta_K\) of order one can come only from the response of \(\chi\); a loop correction of negative sign contributes a small positive part."
new[2] = r"the terms of the action density without derivatives of the wave that depend on \(\chi\), through first order in the background torsion, are"
new[3] = r"including the negative sign of the torsion term in the Lorentzian section. At the next order the first term \(s_0^K(v^M-2\sigma^M)\) of the factorisation enters: on fibre-constant modes at the frozen symbol \(v^M-2\sigma^M\) has the value \(\tfrac{15}{4}\vartheta^2F\sqrt{|g|}/16\pi^2\) at order \(s^0\) on the background, an order that has no term linear or quadratic in the curvature, as recorded in the preceding paragraphs. So the derivative of the density with respect to \(\ln\chi\) gains \(Y=\tfrac{15F}{64\pi^2}\vartheta^2\sqrt{|g|}N_K\ge0\), with \(N_K\) the number of modes of \(K\) with \(\chi^2\mu_A^2\gg\vartheta\). It is not suppressed by the flux of \(K\) or at large \(N\); on \(S^2_N\) at large \(N\), \(Y/2|U_2|=\tfrac54\vartheta/\chi^2\). The fibre flux in \(Y\) is treated below."
new[4] = r"Write \(U\) for this density with the first term and \(U_{\chi\chi}=\partial^2U/\partial(\ln\chi)^2\) at a stationary point. Since \(\bar T^{ab\mu}y_\mu=0\), a perturbation along \(y^\mu y^\nu\) leaves the Gaussian average over the loop momentum unchanged, so where \(\bar h^{11}\) is negligible \(U_4\), \(U_2\) and the fibre-constant part of \(Y\) carry \(\sqrt{|g|}\) alone."
new[5] = r"\beta_K=\frac{2(4U_4+2U_2+Y)}{U_{\chi\chi}}=-\frac{2\,\partial_{\ln\chi}(\rho_MV_{\mathrm t}/g^2)}{U_{\chi\chi}},"
new[6] = r"Hence at a local minimum, \(U_{\chi\chi}>0\), \(\beta_K\) has the sign opposite to the slope of the tree term; for \(U_4\le0\) and \(U_2<0\) one has \(\beta_K<0\) for every \(V_{\mathrm t}\) exactly where \(Y<4|U_4|+2|U_2|\), in particular for \(\chi^2\hat T\gg\vartheta N_K\)."
new[7] = r"\(\beta_K=-1/(1+\varepsilon-Y/4\tilde U)\); adding a tree cubic term, of the form of the cubic term of Equation~\eqref{eq:Smatrix} read on \(K\) and supplied there, gives \(\beta_K=2(4U_4+2U_2+Y)/(4\tilde U+4U_4-2U_2-3Y)\); adding a tree mass term gives \(\beta_K=(4U_4+2U_2+Y)/(4\tilde U+4U_4-Y)\), with \(\partial Y/\partial\ln\chi\) neglected in these three forms. Where the tree stabiliser dominates, \(\beta_K\to0\), from below where the slope of the tree term is positive and from above where it is negative. For \(Y\) negligible, \(\beta_K>0\) needs \(U_4>0\), so \(\hat U<0\); then \(\beta_K=1\) is attained in the cubic case at \(U_4=\tilde U-\tfrac32U_2\) and approached from below in the mass case as \(U_4\) comes to dominate \(\tilde U\) and \(U_2\), each with a tree term of negative slope."
new[8] = r"so \(U_4<0\), \(U_2<0\) and, at large \(N\) with \(x=\chi^2/\vartheta\) and \(N^2\chi^2\gg\vartheta\), \(4U_4+2U_2+Y\) is proportional to \(-4x^2-6x+\tfrac{15}2\), positive for \(x<(\sqrt{39}-3)/4\simeq0.81\). For \(V_{\mathrm t}=\bar a\chi^4\) a stationary point then exists only for \(|\varepsilon|\ge\tfrac{10}{13}\) and a local minimum only for \(\tfrac{10}{13}<|\varepsilon|<1\), with \(x>\tfrac52\) and \(\beta_K<-1\), so there is none at weak coupling. With a tree cubic term \(\beta_K=1\) is attained at a local minimum with \(\hat U>0\): in units \(F\sqrt{|g|}N^2\vartheta^2/32\pi^2\), at \(x=\tfrac3{10}\), a tree quartic \(7.935\) and a tree cubic \(-12.36\) give \(U_{\chi\chi}=10.68\) and \(|\varepsilon|\simeq0.011\). These tree values are supplied, and the tree quartic there is of the order of \(Y\), so the one-loop term is not small against the tree term, and higher loops are not computed."
new[9] = r"so for \(f_1<f_2+f_3\), the range without a negative mode, the integrands of \(\hat U\) and \(\hat V-\hat T\) are negative for every \(s\), and for \(f_1=f_2+f_3\), \(v\equiv\tau\). These integrals diverge at small \(s\) for such non-compact stacks, so \(\hat U<0\) and \(\hat V<\hat T\) are signs with a lower limit on \(s\); the scaling \(U_4\propto\chi^4\) then needs a limit that scales as \(\chi^{-2}\), such as a fixed truncation of the modes, for which the sign is not established. On this evidence the sign of \(\hat U\) depends on \(K\)."
new[10] = r"For \(V_{\mathrm t}=\bar a\chi^4\), \(m^2m_\chi^2=8(1+\varepsilon-Y/4\tilde U)\bar a\chi^2/\bar n\), which is \(4(1+\varepsilon-Y/4\tilde U)\chi^2\) on \(S^2_N\). So (S2) holds above \(m_\chi\) and approximately where a tree stabiliser dominates, and below \(m_\chi\) the value (S1) is a condition on the tree stabiliser and on \(\chi^2/\vartheta\), not an output of this class."
new[11] = r"in addition to the function \(g=g(\tau)\) of the preceding paragraph (in the next display \(g^2\) is its square, not the coupling),"
new[12] = r"the phase average of the density \((A/4\pi^2)\sqrt{|g|}g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi\) in this static channel, with the positive sign in \(S_E\); \(t\) is gauge invariant here, since \(q\cdot v=0\), and the matter charge is \(1-\tfrac12\beta_K\)."
new[13] = r"\(V_0=-F\hat U\chi^4/32\pi^2\), not the weight \(V_0\) of the preceding paragraphs."
new[14] = r"and for \(\hat U<0\) and \(\mathcal M\ge0\) it is a Yukawa pole."
new[15] = r"so for \(\hat U\ge0\) and \(Y\le4|U_4|+2|U_2|\), (S1) and \(V=T\) are incompatible at a local minimum: there the sign of the torsion term that supplies the minimum makes \(\beta_K\) non-positive. For \(\hat U\ge0\) and \(Y>4|U_4|+2|U_2|\), \(\beta_K>0\), and its value is set by the tree term of negative slope."
new[16] = ""
new[17] = r"and the computed exponent is negative for \(\hat U\ge0\) where \(Y<4|U_4|+2|U_2|\)."
new[18] = r"The value \(\beta_K=1\) needs a tree term of negative slope at the minimum and, for \(\hat U\ge0\), \(Y>4|U_4|+2|U_2|\), which at large \(N\) on \(S^2_N\) is \(\chi^2<0.81\vartheta\); for \(\hat U<0\), where \(q_b^2<0\), it is available at negligible \(Y\). In each case the relation among the tree data that sets it is not derived, and the vacuum term must be cancelled at the minimum without cancelling its derivative in \(\chi\)."
new[19] = r"the fibre-constant background for \(U_2\) and for the response of \(Y\), the fibre flux in \(Y\) at the background only and with the base-fibre cross term dropped, and higher orders in \(\vartheta/\chi^2\mu_A^2\) not treated;"
new[20] = r"The sign statement and the exponents are exact for these forms, the first-term identity and its non-negativity are exact on the background, the level form of \(Y\) is the leading form in \(s\) stated there, and the values on explicit \(K\) are exact spectra with numerical fits."

fibre_block = r"""\emph{Fibre flux in the first term.} On the background \(\mathbb F_{ab}\) is the action of the generators \(J_{ab}\) of \(\mathfrak{so}(3,1)\), which commute with \(\Box\). Write \(\mathfrak{so}(3,1)\) over \(\mathbb C\) as \(\mathfrak{su}(2)\oplus\mathfrak{su}(2)\), so that the vector is \((\tfrac12,\tfrac12)\) and the Dirac spinor is \((\tfrac12,0)\oplus(0,\tfrac12)\). On an irreducible orbital component with labels \(j_\pm\), \(\Xi_\pm=2j_\pm+1\), and per state, with \(P(\Xi)=e^{-s}[2\cosh s\Xi+2\Xi^{-1}\sinh s\Xi]\), exactly,
\[
\operatorname{tr}_De^{-sZ}=P(\Xi_+)+P(\Xi_-),\qquad
\operatorname{tr}_Ve^{-sZ}=P(\Xi_+)P(\Xi_-),\qquad
\operatorname{tr}_Ve^{-sZ}-2\operatorname{tr}_De^{-sZ}+4=\bigl(P(\Xi_+)-2\bigr)\bigl(P(\Xi_-)-2\bigr)
\]
(explicit vector and gamma matrices at finite-dimensional labels). On a unitary principal-series component \(\Xi_\pm=\pm m_L+\mathrm i\varsigma\), with \(m_L\) an integer and \(\varsigma\) real, so the two factors are complex conjugates and the integrand of the first term is \(|P(\Xi_+)-2|^2\ge0\) on each component, for every \(s\) and with every fibre flux included. At fibre order \(J\), at a frozen base point, the rotations about \(y\) act as spin \(J\), \(|m_L|\le J\), the density of \((m_L,\varsigma)\) is the Plancherel density \(\varsigma^2+m_L^2\), the squared boost is \(\varsigma^2+1-m_L^2+c_J\) with \(c_J=J(J+1)\), and \(H_0\) is the squared boost divided by \(\vartheta\) plus \(\mu_J\), with the cross term dropped and the direction along \(y\) a spectator. With \(M_A^2=\chi^2\mu_A^2\), the proper time is small where \(M_A^2+\mu_J\gg\vartheta\), and there the average of the integrand over these labels is \(s^2[\tfrac{15}4\vartheta^2-s\vartheta c_J+s^2c_J^2]\), positive, with corrections of relative order \(s\) and \(s\vartheta\) that do not depend on \(J\) at this order (the integral over \(m_L\) is exact in the limit of large \(J\) at fixed \(sJ^2\); the exact average agrees). Hence
\[
Y=\frac{\sqrt{|g|}}{32\pi^2}\sum_A\sum_{J\le n}(2J+1)\,2M_A^2\Bigl[\frac{15\vartheta^2}{4\mathcal D}-\frac{\vartheta c_J}{\mathcal D^2}+\frac{2c_J^2}{\mathcal D^3}\Bigr],\qquad\mathcal D=M_A^2+\mu_J,
\]
each term positive, which reduces to the value above for \(M_A^2\gg\mu_n\). On \(S^2_N\) its relative correction is of order \((n/\chi N)^2\) with a logarithm, the condition for equal weights below (the ratio to the value above is \(0.998\) at \(N=1024\), \(n=10\), \(\vartheta=1\), \(\chi^2=0.3\)), and the fibre-flux part of the mixed term contributes \(4c_J\) per level to \(\partial U/\partial\ln\chi\) in the same units, of relative order \((n/N)^2\). So at equal weights the fibre flux does not change \(Y\) or its sign on the background. The response of the fibre levels to \(\bar h\) and the part of the first term with two fibre fluxes and two base derivatives of the wave are not computed.

"""

extra = [
    ("E1", r"and the tree form is exactly", r"and, with \(g^2\) in \(\rho_M/g^2\) the coupling of the tree form of the preceding paragraph, the tree form is exactly"),
    ("E2", r"and for the homogeneous mode \(\beta_K=(8U_4+2U_2)/U_{\chi\chi}\), which is", r"and for the homogeneous mode, with \(\partial Y/\partial\ln\chi\) neglected, \(\beta_K=(8U_4+2U_2)/U_{\chi\chi}\), which is"),
    ("E3", r"\emph{Explicit \(K\).}", fibre_block + r"\emph{Explicit \(K\).}"),
    ("E4", r"and any term with the same fibre dependence are not computed, and a long-range form needs them or \(\hat U\to0\).", r"and any term with the same fibre dependence are not computed, and a long-range form needs them or \(\hat U\to0\); where \(\chi^2\lesssim\vartheta\) the second-order non-derivative terms of \(U_2\) and of the first term are of the size of this one and are among those not computed."),
    ("E5", r"The background Feynman gauge is used (Hessian checked by finite differences); its dependence at the stationary point is of higher order by the usual argument, not computed.", r"The background Feynman gauge is used (Hessian checked by finite differences); its dependence at the stationary point is of higher order by the usual argument, not computed. The value \(U_2\) above is the order \(\vartheta\) of the mixed term, and on \(S^2_N\) the mixed term with all orders of the frozen symbol agrees with it (ratio above \(0.9999\) at \(N\ge256\) for \(\chi^2\ge0.1\vartheta\))."),
]

def apply(t, tag, o, n):
    c = t.count(o)
    if c != 1:
        print("MISMATCH", tag, "count", c, "- nothing written")
        sys.exit(1)
    return t.replace(o, n)

for k in range(1, 21):
    text = apply(text, "R%d" % k, old[k], new[k])
    print("R%d applied" % k)
for tag, o, n in extra:
    text = apply(text, tag, o, n)
    print(tag, "applied")

for s_ in text:
    if ord(s_) > 127:
        print("non-ASCII character - nothing written")
        sys.exit(1)
data = text.encode("ascii")
open(os.path.join(here, "appH_insert.tex"), "wb").write(data)
print("written appH_insert.tex", len(data), "bytes, sha256", hashlib.sha256(data).hexdigest())
