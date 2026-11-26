# -*- coding: ascii -*-
# Item 123 generator: builds the payload paragraph, splices it against the
# LIVE appH bytes, writes payload + preview + spliced file (arg 1 = output
# path for the spliced file). Prints PRE/PAY/POST sha1[:12]+sizes.
# Every hygiene assert below has an INJECTED POSITIVE CONTROL proven to fire.
import sys, hashlib, re

APPH = r"C:\Users\redgi\Projects\namcg-lab@gpu\chapters\appH-microscopic-proofs.tex"
FOLDER = r"C:\Users\redgi\Projects\namcg-lab@gpu\proposals\123-f-coeff-locked-block"

PIN_SHA1 = "d2af19df0f998ce150c12ea11af9ea8c0387435f"
PIN_SIZE = 863831

# CONTEXT anchor per review-r1: the bare closing clause recurs in other
# section closers, so uniqueness is counted on the full context string
# (anchor sentence + CRLFCRLF + section line).
ANCHOR = ("These statements are for the hypotheses and the channel convention "
          "stated here; they retire the recorded item on the response of the "
          "fibre levels to \\(\\bar h\\) only for this channel component, they "
          "change no status label, and Problems~C, F and~N remain open and "
          "PROGRAMME-CONDITIONAL.")
SECTION = "\section{Problem G: HBEV}"
CTX = (ANCHOR + "\r\n\r\n" + SECTION).encode("ascii")

PAYLOAD = (
 r"\paragraph{Alternate-scope weighted sector data for the locked inventory in harmonic gauge (conditional; Alternate-scope; not closure).} "
 r"Pursued under the Alternate-scope paragraph of Chapter~\ref{ch:agenda}, this paragraph evaluates the weighted sector sum of Theorem~\ref{thm:Geff} "
 r"for a stated truncation of Problem~F. Truncation and named premises: the Presentation~B field content with imposed local Lorentz symmetry, the "
 r"locked frame, and a fixed background metric as in Assumption~\ref{ass:aux-metric}; sectors with kinetic operators are the Hermitian block \(H\) of "
 r"sixteen real components with \(\mathcal O_H=-\nabla^2+E\), \(E=\lambda v^2+Q R_E\) with \(m^2=\lambda v^2\) of Equation~\eqref{eq:V}, a retained "
 r"input set of \(n_K\) real scalar components indexed by the \(K\) labels of this section with \(E_K=Q_K R_E\), the tensor block as an input "
 r"Laplace-type block of ten symmetric-tensor components with fibre-traced endomorphism \(\mathrm{tr}\,E_{\mathrm{ten}}="
 r"e_h R_E\), and the diffeomorphism ghost, supplied as an infrared "
 r"input as recorded in the paragraph on Faddeev--Popov determinants of the pointwise gauge sectors of Section~\ref{sec:status-D}; the internal and "
 r"local-Lorentz Faddeev--Popov determinants of that paragraph are pointwise endomorphism factors in a zeroth-order gauge and are excluded from the "
 r"kinetic sector sum. Scheme (named, not derived): harmonic (de Donder) gauge \(F^\mu=g^{ab}\Gamma^\mu_{ab}\) for the diffeomorphism sector, weights "
 r"relative to a real bosonic determinant as in Equation~\eqref{eq:appA-sector-sum}, per-sector proper-time limits \(s_{\min}=\LUV^{-2}\) and "
 r"\(s_{\max}=\mu^{-2}\) of Equation~\eqref{eq:appA-Wexp}, the massive block carrying the recorded threshold window \(J(\lambda v^2;\LUV^{-2},"
 r"\mu^{-2})\) of the mass-resummed paragraph of this section and each massless sector carrying \(\LUV^2-\mu^2\), and no further local finite "
 r"counterterm at this order. Results (identities within the stated scheme, verified symbolically): (i)~the ghost operator is specified as "
 r"the Laplace-type operator \(M\xi^\mu:=g^{ab}\nabla_a\nabla_b\xi^\mu+R^\mu{}_\nu\xi^\nu\) in the curvature conventions of "
 r"Equations~\eqref{eq:christoffel}--\eqref{eq:riemann}, with principal symbol \(g^{ab}\delta^\mu_\nu\) and overall sign calibrated by the unit "
 r"sphere at \(R=+2\); the positive Euclidean operator \(-M\) has endomorphism "
 r"\(E_{\mathrm{gh}}{}^\mu{}_\nu=-R^\mu{}_\nu\) and, by \(a_1=\mathrm{tr}(R/6-E)\) of Equation~\eqref{eq:appA-a1}, the ghost fibre "
 r"carries \(a_1=(\tfrac46+1)R=\tfrac53R\); (ii)~Grassmann Gaussian integration gives \(\int\mathrm d\bar c\,\mathrm dc\,e^{-\bar c M c}=\det M\) "
 r"exactly (checked at sizes \(2\times2\) and \(3\times3\)), so against Equation~\eqref{eq:appA-sector-sum} the ghost weight is \(-2\); (iii)~the "
 r"truncated counts and curvature-linear coefficient are \(\mathcal N_0=18+n_K\) (ghost shift \(-8\)) and \(\mathcal A_{1,R}=16(\tfrac16-Q)+"
 r"n_K(\tfrac16-Q_K)-\tfrac53-e_h\), the tensor block contributing \(\tfrac{10}{6}-e_h\) and the ghost \(-\tfrac{10}{3}\), and the windowed "
 r"coefficient of \(R_E\) in the sign convention of the block bookkeeping paragraph is "
 r"\(-\frac{1}{32\pi^2}\bigl[16(\tfrac16-Q)J(\lambda v^2;\LUV^{-2},\mu^{-2})+(n_K(\tfrac16-Q_K)-\tfrac53-e_h)(\LUV^2-\mu^2)\bigr]\), where the "
 r"massless window is the recorded threshold at zero mass, \(J(0;\LUV^{-2},\mu^{-2})=\LUV^2-\mu^2\), and at small mass \(J=(\LUV^2-\mu^2)-"
 r"m^2\ln(\LUV^2/\mu^2)+O(m^4\ln m^2)\), which reproduces the recorded fixed-window block expression; (iv)~at \(Q=\tfrac16\) and \(n_K=0\) the "
 r"truncated \(\mathcal A_{1,R}=-\tfrac53-e_h\) persists and vanishes only for \(e_h=-\tfrac53\): the recorded \(Q=\tfrac16\) vanishing of the block "
 r"bookkeeping paragraph is a statement about the \(H\)-block coefficient and does not extend to the ghost-completed truncation, where the ghost "
 r"endomorphism leaves \(-\tfrac{10}{3}\); (v)~consuming, and not rederiving, the recorded mass-resummed window data, for the \(Q=0\) block with "
 r"\(\mu\ll m\) the windowed ratio \(10\,J/\LUV^2\) of the recorded \(\Upsilon=\mathcal A_1/(2\mathcal W_C)\) tends to \(10(e^{-y}-yE_1(y))\) with "
 r"\(y=\lambda v^2/\LUV^2\), whose derivative \(-10E_1(y)\) is negative and whose \(y\to0\) limit is the recorded universal \(10\). Status of items: "
 r"the ghost weight, endomorphism and \(a_1\) contribution, the counts and the windowed \(a_1\)-coefficient are derivations within the "
 r"named scheme; the field content, \(Q\), \(Q_K\), \(e_h\), \(n_K\), the Laplace-type tensor-block form and the ghost as an infrared input are "
 r"supplied premises of the Alternate-scope truncation named above; the curvature-squared coefficients of the vector ghost (the connection-curvature "
 r"terms of Equation~\eqref{eq:appA-a2} on the tangent bundle) are not evaluated, so \(\mathcal W_C\) and \(\delta_W\) are not fixed for the "
 r"truncation, \(\mathcal A_2\) is not evaluated beyond the recorded block data, the continuation and the Lorentzian sign are not fixed, no "
 r"comparison with \(A,B,C\) of Equation~\eqref{eq:Geff-structure} is made, and no value of \(G_{\mathrm{eff}}\) is obtained; the truncation does not "
 r"discharge the frame, selection or non-degeneracy inputs of Problem~D1 and supplies only part of the per-sector items of the missing-step "
 r"paragraph of this section. This paragraph closes none of Problem~D, Problem~D1, Problem~F or Problem~N, all of which remain OPEN and "
 r"PROGRAMME-CONDITIONAL, and it changes no status label.")

WHITELIST = ["thm:Geff", "ass:aux-metric", "sec:status-D", "eq:Geff-structure",
             "eq:V", "eq:appA-a1", "eq:appA-a2", "eq:appA-sector-sum",
             "eq:appA-Wexp", "eq:christoffel", "eq:riemann", "ch:agenda"]

CRLF = b"\r\n"

def sha(b): return hashlib.sha1(b).hexdigest()

def ascii_ok(b): return all(c < 128 for c in b)
def eol_ok(b):
    return (b.endswith(CRLF) and not re.search(rb"\r(?!\n)", b)
            and not re.search(rb"(?<!\r)\n", b) and rb"\r\r" not in b
            and CRLF not in b[:-2])
def forbidden_ok(b):
    return not any(tok in b for tok in (b"$", br"\label", br"\cite", br"\begin",
                                        br"\end", rb"\[", rb"\]"))
def braces_ok(b): return b.count(b"{") == b.count(b"}")
def refs_ok(b, wl):
    used = re.findall(rb"\\(?:ref|eqref)\{([^}]*)\}", b)
    return all(u.decode() in wl for u in used), set(u.decode() for u in used)

def die(msg):
    print("GEN FAIL:", msg); raise SystemExit(1)

# ---- injected positive controls (each detector must fire) ------------------
ctrl = b"x\r\ry\r\n"
if not eol_ok(ctrl): print("CTRL eol-crclr: fires OK")
else: die("eol detector dead (CR-CR-LF control)")
ctrl2 = b"x\ny"
if not eol_ok(ctrl2): print("CTRL eol-bareLF: fires OK")
else: die("eol detector dead (bare LF control)")
ctrl3 = b"x\ry" + CRLF
if not eol_ok(ctrl3): print("CTRL eol-bareCR: fires OK")
else: die("eol detector dead (bare CR control)")
if forbidden_ok(b"$x$" + PAYLOAD.encode()): die("forbidden detector dead ($ control)")
print("CTRL forbidden-dollar: fires OK")
if forbidden_ok(PAYLOAD.encode() + br"\label{a}"): die("forbidden detector dead (label control)")
print("CTRL forbidden-label: fires OK")
if ascii_ok(b"caf\xc3\xa9"): die("ascii detector dead (utf8 control)")
print("CTRL ascii: fires OK")
if braces_ok(b"{a"): die("braces detector dead (control)")
print("CTRL braces: fires OK")
if refs_ok(b"\\ref{nope}", WHITELIST)[0]: die("refs detector dead (control)")
print("CTRL refs: fires OK")
FTOK = rb"fibre-traced endomorphism \(\mathrm{tr}\,E_{\mathrm{ten}}=e_h R_E\)"
NOTOK = rb"\frac{\mathrm d}{\mathrm d\varepsilon}"
def r2tok_ok(b): return (FTOK in b) and (NOTOK not in b)
if r2tok_ok(FTOK + b" tail"): print("CTRL r2-fibretrace: fires OK")
else: die("r2 fibre-trace detector dead (missing-token control)")
if r2tok_ok(b"x" + NOTOK + b"y"): die("r2 first-variation detector dead (present-token control)")
print("CTRL r2-nofirstvar: fires OK")

# ---- live pin ---------------------------------------------------------------
pre = open(APPH, "rb").read()
if sha(pre) != PIN_SHA1 or len(pre) != PIN_SIZE:
    die("live appH pin mismatch sha1=%s size=%d" % (sha(pre)[:12], len(pre)))
print("PIN OK", sha(pre)[:12], len(pre))

pay = PAYLOAD.encode("ascii") + CRLF
if not ascii_ok(pay): die("payload ascii")
if not eol_ok(pay): die("payload eol")
if not forbidden_ok(pay): die("payload forbidden token")
if not braces_ok(pay): die("payload braces unbalanced")
if not r2tok_ok(pay): die("payload missing fibre-traced clause or still has first-variation formula")
print("R2 TOKENS OK")
ok, used = refs_ok(pay, WHITELIST)
if not ok: die("payload ref outside whitelist: %s" % used)
print("REFS OK used=%d labels" % len(used))
import os
XFILES = [os.path.join(r"C:\Users\redgi\Projects\namcg-lab@gpu\chapters", f) for f in
          ("ch02-preliminaries.tex", "ch03-matrix-action.tex",
           "ch08-heat-kernel.tex", "ch17-agenda.tex",
           "appA-seeley-dewitt.tex")]
xtxt = b"".join(open(f, "rb").read() for f in XFILES)
for lab in used:
    tok = b"\label{" + lab.encode() + b"}"
    if tok not in pre and tok not in xtxt:
        die("label %s not found in appH or whitelisted source files" % lab)
print("LABELS OK (each used label defined in appH or a whitelisted file)")

anchor = ANCHOR.encode("ascii")
if pay.rstrip(CRLF) in pre: die("payload already present")
n = pre.count(CTX)
if n != 1: die("context anchor count = %d (need 1)" % n)
print("ANCHOR unique on CONTEXT string (count 1)")

post = pre.replace(CTX,
                   anchor + CRLF + CRLF + pay + CRLF + SECTION.encode("ascii"), 1)
if len(post) != len(pre) + len(pay) + 2:
    die("POST arithmetic: %d != %d + %d + 2" % (len(post), len(pre), len(pay)))

open(FOLDER + r"\payload-123.txt", "wb").write(pay)
i = post.find(pay)
open(FOLDER + r"\preview-splice-123.txt", "wb").write(
    post[max(0, i - 400):i] + b"\n===== PAYLOAD =====\n" + pay +
    b"\n===== FOLLOWING =====\n" + post[i + len(pay):i + len(pay) + 200])
if len(sys.argv) > 1:
    open(sys.argv[1], "wb").write(post)
    print("SPLACED WRITTEN", sys.argv[1])

print("PRE  %s %d" % (sha(pre)[:12], len(pre)))
print("PAY  %s %d" % (sha(pay)[:12], len(pay)))
print("POST %s %d" % (sha(post)[:12], len(post)))
print("POST sha1 full:", sha(post))
print("GEN VERDICT: PASS")
