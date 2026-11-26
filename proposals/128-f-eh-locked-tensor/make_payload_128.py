# make_payload_128.py  (item 128 generator, final text matching the v4.1
# verified outputs: e_h matter vertex = 29/6 exact; sigma_gf (harmonic
# gauge-fixing zero-order remainder) and sigma_pt (pure-trace pairing-vanishing
# completions) left as named undetermined parts; condition (iv) becomes
# sigma = -13/2.)
#
# Builds payload-P1.txt (paragraph text, CRLF-terminated), verifies the live
# anchor, splices into a copy of appH INSIDE this proposal folder only, and
# prints pins (sha1_12 + byte sizes) + hygiene reports with injected positive
# controls (per project memory: every hygiene assert must be shown to fire on
# an adversarial payload).
#
# Tab-trap note (found in r1): EHS/SIG MUST be written "\\tfrac" - a single
# backslash makes Python emit a literal TAB before "rac". The TAB guard in
# hygiene() and the raw-TAB assert in main() are the positive controls.
#
# Usage: python -I make_payload_128.py <EH_value_rational>   (29/6)
import hashlib
import sys
from fractions import Fraction

EHV = sys.argv[1] if len(sys.argv) > 1 else "29/6"
ehf = Fraction(EHV)
sig = -Fraction(5, 3) - ehf            # condition-(iv) requirement on sigma
SIG = "\\tfrac{%d}{%d}" % (abs(sig.numerator), sig.denominator)   # \tfrac{13}{2}
EHS = "\\tfrac{%d}{%d}" % (abs(ehf.numerator), ehf.denominator)   # \tfrac{29}{6}

ANCHOR = b"\\paragraph{Alternate-scope weighted sector data"

PAYLOAD = (
    "\\paragraph{Tensor-block endomorphism trace in the Einstein--Hilbert completion "
    "of the locked tensor block (conditional; not closure).} Hypothesis H1 (stated, "
    "not derived): the ten-component tensor block of the locked action is the quadratic "
    "Einstein--Hilbert action of the metric sector about the fixed background of "
    "Assumption~\\ref{ass:aux-metric}, gauge-fixed by the harmonic functional "
    "\\(F^\\mu=g^{ab}\\Gamma^\\mu_{ab}\\) named in the Alternate-scope truncation paragraph "
    "of this section, in the curvature conventions of Equations~\\eqref{eq:christoffel}"
    "--\\eqref{eq:riemann} with the unit-sphere calibration \\(R=+2\\). Write \\(e_h\\) "
    "for the total-fibre-trace reading \\(\\mathrm{tr}\\,E_{\\mathrm{ten}}=e_h R_E\\) of "
    "the Laplace-type endomorphism of the block used in that paragraph. Two statements "
    "hold under H1. First, the curvature vertex \\(K\\) extracted from the "
    "Einstein--Hilbert density at a point where the background \\(\\Gamma\\) vanishes "
    "(the coefficient of the quadratic term in a constant fibre direction, which is the "
    "part of the block independent of the gauge fixing) obeys \\(\\mathrm{tr}\\,K="
    "%(EH)s\\,R_E\\) exactly: this is obtained by exact symbolic expansion on the "
    "conformal family \\(\\bar{g}=e^{2\\omega}\\delta\\), \\(\\omega=\\tfrac{1}{2}"
    "C_{\\mu\\nu}x^\\mu x^\\nu\\) at \\(x=0\\), where \\(\\Gamma=0\\) and the symmetric "
    "matrix \\(C\\) supplies ten independent background-curvature data; the trace is "
    "independent of \\(C\\) (a natural scalar linear in curvature), the fibre endomorphism "
    "decomposes exactly on the curvature-linear natural structures "
    "\\(\\mathrm{Rm}\\cdot\\), \\(\\mathrm{Ric}\\cdot\\), \\(\\cdot\\,\\mathrm{Ric}\\), "
    "\\(g(\\mathrm{Ric}:\\cdot)\\), \\((\\mathrm{Ric})\\,\\mathrm{tr}(\\cdot)\\,g\\), "
    "\\(R\\,g\\,\\mathrm{tr}(\\cdot)\\) with fibre traces \\(-R_E/2\\), \\(5R_E/2\\), "
    "\\(5R_E/2\\), \\(R_E\\), \\(R_E\\), \\(4R_E\\), and the full fibre trace is "
    "reproduced basis-independently on an orthonormal fibre basis. Second, "
    "\\(e_h=%(EH)s+\\sigma_{\\mathrm{gf}}+\\sigma_{\\mathrm{pt}}\\): "
    "\\(\\sigma_{\\mathrm{gf}}=\\mathrm{tr}\\,E_{\\mathrm{gf}}/R_E\\) is the zero-order "
    "trace of the named harmonic gauge fixing, whose constant-fibre density vanishes at "
    "such a point identically (\\(F=0\\) there to all orders in the fluctuation) and whose "
    "contribution arises only through the zero-order remainder left after the block is "
    "reduced to Laplace form, a term not evaluated here; and \\(\\sigma_{\\mathrm{pt}}\\) "
    "runs over curvature-linear endomorphism additions whose fibre bilinear form vanishes "
    "on the nine-dimensional traceless fibre, which among self-adjoint curvature-linear "
    "natural additions are exactly \\(H\\mapsto g(\\mathrm{Ric}:H)\\), "
    "\\(H\\mapsto(\\mathrm{Ric})\\,\\mathrm{tr}\\,H\\,g\\) and \\(H\\mapsto R\\,g\\,"
    "\\mathrm{tr}\\,H\\) (fibre traces \\(R_E\\), \\(R_E\\), \\(4R_E\\), the middle one "
    "vanishing on the traceless fibre trivially), leaving the traceless-fibre propagation "
    "of the block untouched. Hence \\(e_h\\) is determined by the tensor-block data of H1 "
    "if and only if both the pure-trace zero-order completion and the gauge-fixing "
    "zero-order remainder are fixed; no flat-background datum can fix them, since they "
    "vanish with the curvature and share the flat limit, the massless Fierz--Pauli block "
    "of Equation~\\eqref{eq:FP} whose curved-background counterpart "
    "Section~\\ref{sec:ch1-checklist} item 3 requires of \\(T_{\\mu\\nu}\\), consistently "
    "with the recorded statement that tensor-block terms beyond the displayed action are "
    "an additional input. Consumption: in the Alternate-scope truncation below the "
    "supplied parameter becomes \\(e_h=%(EH)s+\\sigma\\) with \\(\\sigma=\\sigma_{\\mathrm{gf}}"
    "+\\sigma_{\\mathrm{pt}}\\), the tensor-plus-ghost trunk at \\(Q=\\tfrac16\\), "
    "\\(n_K=0\\) becomes \\(-\\sigma-%(SIG)s\\), and condition (iv) of that paragraph "
    "becomes the explicit requirement \\(\\sigma=-%(SIG)s\\). The ghost coefficient "
    "\\(5R_E/3\\) of that paragraph is reproduced from the paragraph's own stated ghost "
    "endomorphism and is not re-derived here. Not claimed: that H1 follows from the "
    "displayed action; the separate values of \\(\\sigma_{\\mathrm{gf}}\\) or "
    "\\(\\sigma_{\\mathrm{pt}}\\); that condition (iv) holds; any \\(a_1\\) or \\(a_2\\) "
    "evaluation beyond the Alternate-scope paragraph; any closure. This paragraph closes "
    "no problem and changes no label.\r\n\r\n"
) % {"EH": EHS, "SIG": SIG}


def sha12(b):
    return hashlib.sha1(b).hexdigest()[:12]


def main():
    pay = PAYLOAD.encode("ascii")  # raises on non-ASCII
    if b"PLACEHOLDER" in pay:
        raise SystemExit("placeholder left in payload")
    if b"\t" in pay:
        raise SystemExit("raw TAB in payload (\\t escape trap)")

    def hygiene(buf, name, out):
        ok = True
        if b"\r" in buf.replace(b"\r\n", b""):
            out.append("FAIL bare CR in %s" % name); ok = False
        if b"\n" in buf.replace(b"\r\n", b""):
            out.append("FAIL bare LF in %s" % name); ok = False
        if b"\t" in buf:
            out.append("FAIL raw TAB in %s" % name); ok = False
        for tok in (b"\\label", b"\\cite", b"$", b"Status:", b"Priority:", b"CRITICAL", b"PROGRAMME-CONDITIONAL"):
            if tok in buf:
                out.append("FAIL token %s in %s" % (tok, name)); ok = False
        if buf.count(b"{") != buf.count(b"}"):
            out.append("FAIL braces in %s" % name); ok = False
        return ok

    out = []
    h_ok = hygiene(pay, "payload", out)
    # positive controls: injected violations must fire (TAB control included)
    ctrl = pay.replace(b"\\ref", b"\\label", 1)
    c_ok = not hygiene(ctrl, "control-label", out)
    ctrl2 = pay + b"\n"
    c2_ok = not hygiene(ctrl2, "control-lf", out)
    ctrl3 = pay.replace(b"}", b"}}", 1)
    c3_ok = not hygiene(ctrl3, "control-brace", out)
    ctrl4 = pay.replace(b"\\tfrac", b"\tfrac", 1)
    c4_ok = (b"\t" in ctrl4) and not hygiene(ctrl4, "control-tab", out)
    out.append("CTRL_FIRES = (%s, %s, %s, %s)" % (c_ok, c2_ok, c3_ok, c4_ok))
    assert h_ok, out
    assert c_ok and c2_ok and c3_ok and c4_ok, ("hygiene guard vacuous", out)
    assert pay.count(b"\\tfrac{29}{6}") == 3 and pay.count(b"\\tfrac{13}{2}") == 2, (
        "tfrac occurrences wrong: %d/%d" % (pay.count(b"\\tfrac{29}{6}"),
                                            pay.count(b"\\tfrac{13}{2}")))

    open("proposals/128-f-eh-locked-tensor/payload-P1.txt", "wb").write(pay)
    live = open("chapters/appH-microscopic-proofs.tex", "rb").read()
    n = live.count(ANCHOR)
    out.append("ANCHOR_COUNT = %d" % n)
    assert n == 1, out
    pre_hash, pre_len = sha12(live), len(live)
    post = live.replace(ANCHOR, pay + ANCHOR, 1)
    assert len(post) == pre_len + len(pay), "POST accounting"
    open("proposals/128-f-eh-locked-tensor/appH-spliced-P1.tex", "wb").write(post)
    out.append("PAY_PIN  = %s / %d" % (sha12(pay), len(pay)))
    out.append("PRE_PIN  = %s / %d" % (pre_hash, pre_len))
    out.append("POST_PIN = %s / %d (= PRE + PAY)" % (sha12(post), len(post)))
    out.append("GEN PASS")
    txt = "\r\n".join(out) + "\r\n"
    open("proposals/128-f-eh-locked-tensor/out-make-payload-128.txt", "wb").write(txt.encode())
    print(txt)


if __name__ == "__main__":
    main()
