#!/usr/bin/env python3
"""Build appH_insert.tex (LF) for proposal 054 round 2 from appH_insert.r1.tex by two exact
byte replacements implementing gatekeeper findings F1-F4 (plus F6 wording) from review-r1.md
'Corrected snippet' (i) and (ii). Each old span must occur exactly once. Prints sizes and
sha256 of the LF and CRLF forms. Run:  python -I patch_insert_r2.py
One deviation from the gatekeeper snippet is recorded in proposal-r2.md: the pronoun "(it
vanishes ...)" of snippet (i) is written "(S_{\mathrm E} vanishes ...)" to remove a false
reading (the weight does not vanish on the ray; S_{\mathrm E} does). No math change.
"""
import pathlib, hashlib
HERE = pathlib.Path(__file__).resolve().parent
CR, LF = b"\r", b"\n"
def lf(b): return b.replace(CR+LF, LF)
def crlf(b): return lf(b).replace(LF, CR+LF)
def sha(b): return hashlib.sha256(b).hexdigest()

OLD_A = (
    r"Along rank-one rays \(\tilde A_\mu=\rho_\mu H\), \(\operatorname{Tr}H^2=1\), the Euclidean weight at \(u=1\) is not "
    r"exponentially damped and the Pfaffian vanishes on the ray and is polynomial in the coordinates nearby, so convergence is "
    r"governed by powers of the reduced variables and the radius: in reduced coordinates the weight is polynomial times "
    r"\(\mathrm e^{-\lambda e_2/2}\) with \(e_2\) bounded along the corner and no other damping along it (numerical, reduced "
    r"coordinates), while \(|O_k|\ge\mathrm e^{b_u(\hat\rho;k)\rho}/4\) with "
    r"\(b_u(\hat\rho;k)=|\operatorname{Im}(k^0\mathrm e^{-3\pi\mathrm iu/8}\hat\rho_0+k^i\mathrm e^{\pi\mathrm iu/8}\hat\rho_i)|\).")
NEW_A = (
    r"Along rank-one rays \(\tilde A_\mu=\rho_\mu H\), \(\operatorname{Tr}H^2=1\), the Euclidean weight \(\mathrm e^{-S_{\mathrm E}}\) is "
    r"not exponentially damped and tends to a bounded factor along the corner (\(S_{\mathrm E}\) vanishes on the exact rank-one rays), "
    r"the Pfaffian vanishes on the ray and is polynomial in the coordinates nearby, and the remaining factors are polynomial "
    r"(numerical, in a reduced chart), while \(|O_k|\ge 2\sinh\!\bigl(b_u(\hat\rho;k)\rho/2\bigr)\) with "
    r"\(b_u(\hat\rho;k)=|\operatorname{Im}(k^0\mathrm e^{-3\pi\mathrm iu/8}\hat\rho_0+k^i\mathrm e^{\pi\mathrm iu/8}\hat\rho_i)|\).")

OLD_B = (
    r"For \(\operatorname{Im}k\ne0\) a commuting ray with \((\operatorname{Re}k\cdot\rho)(\operatorname{Im}k\cdot\rho)>0\) has "
    r"\(S_{\mathrm b}=0\) and \(|O_k|\) of order \(\mathrm e^{b\rho}\) with \(b>0\), so the regulated Laplace integral at \(u=0\) grows "
    r"like \(\mathrm e^{c_2(k)/\epsilon}\) along a sequence \(\epsilon\to0^+\), and \(I_\epsilon[O_k]\) has no finite \(\epsilon\to0\) "
    r"limit for non-real \(k\). For real \(k\ne0\) the integrand at \(u=0\) carries \(|O_k|\le2\) pointwise, but no fixed-\(u\) "
    r"domination in \(\epsilon\) is available at any \(u\in(0,2/3)\): the fixed-\(\epsilon\) modulus on \(\mathcal R_u\) grows without "
    r"bound as \(\epsilon\to0\), numerically like \(\mathrm e^{c(k,u)/\sqrt\epsilon}\). Hence the displayed limit identity holds for "
    r"\(O_k\) exactly at \(k=0\): there is no analyticity strip and no non-polynomial extension of the limit statement at \(\gamma=0\), "
    r"within the hypothesis class \(N=2\), regulator (A), contours \(\mathcal R_u\), \(\epsilon\to0^+\) last.")
NEW_B = (
    r"For \(\operatorname{Im}k\ne0\) such that some commuting unit \(\hat\rho\) has \(|\operatorname{Im}(k\cdot\hat\rho)|>"
    r"|\operatorname{Re}(k\cdot\hat\rho)|\), the commuting-ray contribution to the \(u=0\) integral has \(S_{\mathrm b}=0\) and grows "
    r"along a sequence \(\epsilon\to0^+\) like \(\mathrm e^{c_2(k)/\epsilon}\) with \(c_2(k)>0\) (commuting-ray model; no transverse "
    r"stationary-phase bound is claimed), and for real \(k\ne0\) the integrand at \(u=0\) carries \(|O_k|\le2\) pointwise, but no "
    r"fixed-\(u\) domination in \(\epsilon\) is available at any \(u\in(0,2/3)\): the fixed-\(\epsilon\) modulus on \(\mathcal R_u\) "
    r"grows without bound as \(\epsilon\to0\), numerically like \(\mathrm e^{c(k,u)/\sqrt\epsilon}\) on the sampled range. Hence "
    r"within the class stated the displayed limit identity fails for every nonzero real \(k\) and for every non-real \(k\) outside "
    r"the slice on which \(k^0\mathrm e^{-3\pi\mathrm i/8}\) and all \(k^i\mathrm e^{\pi\mathrm i/8}\) are real, holds at \(k=0\), "
    r"and is unresolved on that slice at \(k\ne0\): there is no analyticity strip and no non-polynomial extension of the limit "
    r"statement at \(\gamma=0\) off that slice, within the hypothesis class \(N=2\), regulator (A), contours \(\mathcal R_u\), "
    r"\(\epsilon\to0^+\) last.")

def main():
    src = lf((HERE/"appH_insert.r1.tex").read_bytes())
    assert src.count(OLD_A.encode()) == 1, "OLD_A count != 1"
    assert src.count(OLD_B.encode()) == 1, "OLD_B count != 1"
    out = src.replace(OLD_A.encode(), NEW_A.encode()).replace(OLD_B.encode(), NEW_B.encode())
    for bad in (rb"e_2", rb"\lambda e_2", rb"exactly at \(k=0\)", rb"no finite \(\epsilon\to0\) limit for non-real"):
        assert out.count(bad) == 0, "residual " + repr(bad)
    for need in (rb"2\sinh\!\bigl(b_u(\hat\rho;k)\rho/2\bigr)", rb"\mathrm e^{-S_{\mathrm E}}",
                 rb"holds at \(k=0\), and is unresolved on that slice at \(k\ne0\)",
                 rb"on the sampled range",
                 b"|\\operatorname{Im}(k\\cdot\\hat\\rho)|>|\\operatorname{Re}(k\\cdot\\hat\\rho)|",
                 rb"commuting-ray model; no transverse stationary-phase bound is claimed"):
        assert out.count(need) == 1, "missing " + repr(need)
    (HERE/"appH_insert.tex").write_bytes(out)
    print("appH_insert.tex LF   size %d sha256 %s" % (len(out), sha(out)))
    c = crlf(out)
    print("appH_insert.tex CRLF size %d sha256 %s" % (len(c), sha(c)))
    print("r1 LF size %d sha256 %s" % (len(src), sha(src)))
    print("r1 CRLF size %d sha256 %s" % (len(crlf(src)), sha(crlf(src))))

main()
