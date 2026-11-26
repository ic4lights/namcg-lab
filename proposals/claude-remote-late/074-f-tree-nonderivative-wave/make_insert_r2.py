"""
074 r2: build appH_insert_r2.tex from appH_insert.tex (r1, kept) by the replacements of review-r1
(channel paragraph, added passage, Consequence paragraph, scope sentence) and m1, m3, m5.
Each old string must occur exactly once.  Run:  python -I make_insert_r2.py
"""
import hashlib
from pathlib import Path

here = Path(__file__).resolve().parent
r1 = (here / "appH_insert.tex").read_text(encoding="utf-8")
assert "\r" not in r1

R = []
# m1: field equation E_a -> \mathsf E_a (the frame E is kept)
R.append(("m1 field equation", r"the field equation \(E_a=0\)", r"the field equation \(\mathsf E_a=0\)"))
R.append(("m1 first-order term", r"\(\int\rho_M\langle E\cdot A\rangle\)", r"\(\int\rho_M\langle\mathsf E\cdot A\rangle\)"))
# m3: supplied bilinear term; matter fields at their vanishing background
R.append(("m3 setting", r"whose bilinear term is that of the class", r"whose supplied bilinear term is that of the class"))
R.append(("m3 degree argument",
          r"every term of the quartic term with \(C_{\mu\nu\lambda}=0\), of the bilinear term and of the terms with the matrices of \(K\) is of degree two or zero in one component,",
          r"with the matter fields at their vanishing background every term of the quartic term with \(C_{\mu\nu\lambda}=0\), of the supplied bilinear term and of the terms with the matrices of \(K\) is of degree two or zero in one component,"))
# M1/m2: channel paragraph (review replacement text, verbatim)
R.append(("M1 channel",
          r"Hence \(T_{\mathrm{tree}}=C_{\mathrm{tree}}=0\) in this realisation: the tree non-derivative terms add nothing to \(\sum_i(C_i-T_i)\) in the identity of the preceding paragraph, so they do not supply the Yukawa condition there and do not cancel the tadpole of \(U_4\) in this channel.",
          r"Hence \(T_{\mathrm{tree}}=C_{\mathrm{tree}}=0\) in this realisation. That \(T_{\mathrm{tree}}=0\) holds in every realisation, since the background is stationary, so the tree terms do not cancel the tadpole of \(U_4\) in any channel; that \(C_{\mathrm{tree}}=0\) is a property of this realisation, on which the other entries of the identity of the preceding paragraph, obtained with the background torsion held, are not computed."))
# m1: the constant L of the identity
R.append(("m1 constant L", r"In the normalisation of the identity the leading symbol adds",
          r"In the normalisation of the identity, that is after multiplication by its constant \(L/2m^4\), which is not the operator \(L\), the leading symbol adds"))
# M1/M3: added passage (verbatim)
R.append(("M1/M3 added passage", r"the two realisations do not have the same tree form.",
          r"the two realisations do not have the same tree form. These values are for the level-one profile \(\hat q\cdot T\). The identity of the preceding paragraph is stated at equal weights with all fibre harmonics eliminated at each fibre point; on that profile \(\langle\mathsf w\cdot L(\mathsf w)\rangle\) contains the fibre derivatives of \(L\) and is not computed. The reduced form of the paragraph on the response of the scale of \(K\) is the phase average of the induced density alone, so the term \(-3\varpi/m^2\) of the leading symbol of the tree form is not among the terms of the displays of the two preceding paragraphs."))
# m5: origin of the positive singlet value
R.append(("m5 singlet",
          r"adds \(\vartheta\varpi/2m^2>0\) to its denominator, the Yukawa sign at tree strength.",
          r"adds \(\vartheta\varpi/2m^2>0\) to its denominator, the Yukawa sign at tree strength. This positive value is obtained by extremising over the \(\sigma_1\)-neutral direction \((\mathsf P_\perp-3\mathsf P)T\), whose own non-derivative term is negative, with the eigenvalue \(-2\) of \(L\) and the curvature \(-4\) of the form at fixed \(\sigma_1\)."))
# M2: Consequence paragraph (verbatim)
old_cons = r"""\emph{Consequence.} In the channel along \(y^\mu y^\nu\) the tree terms supply no positive constant at \(q=0\): they vanish on the rescaling, and on the level-one amplitude the non-derivative term is positive but of order \(k^{-2}\) and the leading symbol is negative. A tree contribution of the Yukawa sign is available only if the static channel at \(q=0\) includes the \(\sigma_1\)-neutral singlet, which the identity of the preceding paragraph, written for the channel along \(y^\mu y^\nu\), does not contain."""
new_cons = r"""\emph{Consequence.} On the two realisations of the channel along \(y^\mu y^\nu\) computed here the tree terms supply no positive constant at \(q=0\): they vanish on the rescaling, and on the level-one amplitude the leading symbol adds a negative constant and the non-derivative term is positive but of order \(k^{-2}\), whose effect on the static response at small \(k\), where the frozen base point is not controlled, is not determined. The tree non-derivative term therefore depends on the fibre profile of the wave, and its value on the profile of the identity of the preceding paragraph is not computed. A positive constant at \(q=0\) of tree strength is obtained here only on the singlet sector, at the stationary value over the \(\sigma_1\)-neutral singlet, whose own non-derivative term is negative; the identity of the preceding paragraph, written for the channel along \(y^\mu y^\nu\), does not contain it."""
R.append(("M2 consequence", old_cons, new_cons))
# scope sentence
R.append(("scope (i)", r"They do not compute the loop profiles", r"They do not compute the tree non-derivative terms on the profile of the equal-weight elimination, the loop profiles"))
R.append(("scope (ii)", r"the conjugate-coordinate class with the bilinear term and",
          r"the conjugate-coordinate class with the supplied bilinear term and the matter fields at their vanishing background and"))

txt = r1
for name, old, new in R:
    n = txt.count(old)
    print(f"{name}: old occurs {n}x")
    assert n == 1, name
    txt = txt.replace(old, new)
assert "E_a" not in txt.replace(r"\mathsf E_a", "")
assert txt.count("PROGRAMME-CONDITIONAL") == 1 and txt.rstrip().endswith("remain open and PROGRAMME-CONDITIONAL.")
assert all(ord(c) < 128 for c in txt) and txt.endswith(".\n\n")
(here / "appH_insert_r2.tex").write_bytes(txt.encode("utf-8"))
print("appH_insert_r2.tex bytes", len(txt.encode()), "sha256(LF)", hashlib.sha256(txt.encode()).hexdigest())
