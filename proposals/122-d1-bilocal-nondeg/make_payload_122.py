# -*- coding: ascii -*-
# Item 122 payload generator: emits payload-122.tex (pure ASCII, single CRLF
# line, ends CRLF, zero new \label/\cite, refs only to verified labels) and a
# spliced preview of the live appH file. Every hygiene check is exercised by
# an injected positive control proving the detector fires. Does not run
# pdflatex. Does not write outside the proposal folder.
import hashlib
import re
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = r"C:\Users\redgi\Projects\namcg-lab@gpu"
APPB = os.path.join(ROOT, "chapters", "appH-microscopic-proofs.tex")
CRLF = chr(13) + chr(10)
CRLF_B = CRLF.encode("ascii")
CR_B = chr(13).encode("ascii")
LF_B = chr(10).encode("ascii")
PAT_LONE_CR = (chr(92) + "r(?!" + chr(92) + "n)").encode("ascii")


P = []
P.append(chr(92) + "emph{Bilocal composite: exact reduction of the two-point-kernel gap and conditional non-degeneracy bounds.} This paragraph records derivations that discharge the two-point-kernel non-degeneracy step under explicit hypotheses and scope what the bilocal reading of Assumption~" + chr(92) + "ref{ass:nondeg} can supply. Let \\(M(x,y)=\\Phi(x)\\,W(x,y)\\,\\Phi(y)^\\dagger\\) be the bilocal composite with transport coefficients \\(W(x,y)\\in\\mathbb C^{4\\times4}\\) on a carrier measure \\(\\mathrm d\\mu_{\\rm c}\\) over the base, and let \\(T_M\\) be the operator \\((T_M f)(x)=\\int M(x,y)f(y)\\,\\mathrm d\\mu_{\\rm c}(y)\\) on \\(L^2(\\mathrm d\\mu_{\\rm c})\\otimes\\mathbb C^4\\), with \\(T_W\\) the operator of \\(W\\) alone and \\(\\kappa(T):=\\sigma_{\\max}(T)/\\sigma_{\\min}(T)\\). (i)~Reduction. The factorization \\(T_M=\\mathsf P\\,T_W\\,\\mathsf P^\\dagger\\), with \\(\\mathsf P\\) fibrewise multiplication by \\(\\Phi\\), applied to the identities \\(\\sigma_{\\min}(AB)\\ge\\sigma_{\\min}(A)\\,\\sigma_{\\min}(B)\\) and \\(\\sigma_{\\max}(AB)\\le\\sigma_{\\max}(A)\\,\\sigma_{\\max}(B)\\), gives: if \\(c\\le\\sigma_{\\min}(\\Phi)\\) and \\(\\sigma_{\\max}(\\Phi)\\le C\\) \\(\\mathrm d\\mu_{\\rm c}\\)-a.e., then \\(\\sigma_{\\min}(T_M)\\ge c^2\\sigma_{\\min}(T_W)\\) and \\(\\kappa(T_M)\\le(C/c)^2\\kappa(T_W)\\). The gap recorded above therefore reduces exactly to the transport-kernel lower bound \\(w:=\\sigma_{\\min}(T_W)\\), and no bound on \\(w\\) follows from pointwise \\(\\Phi\\)-data: with \\(\\Phi\\equiv v\\,\\mathbb I\\) and \\(W\\) fibrewise a rank-deficient projector, \\(w=0=\\sigma_{\\min}(T_M)\\) with \\(\\Phi\\) invertible, and a fibre of smallest singular value \\(c\\) drives the bound at rate \\(c^2\\). (ii)~Unitary-transporter carrier case. If the carrier is finite and the link-variable assembly makes the carrier transport operator unitary -- matrix link variables and exactly unitary fuzzy Wilson lines (transport as a unitary superoperator on the finite carrier), path-ordered exponentials of anti-Hermitian fibre connections, for which \\(\\sigma_{\\min}=1\\) exactly and uniformly in the carrier size -- then \\(w=1\\) and \\(\\sigma_{\\min}(T_M)\\ge c^2\\); on a region where \\(\\mathcal V\\le\\varepsilon\\) for \\(\\mathcal V\\) of Equation~" + chr(92) + "eqref{eq:V}, the recorded bound \\(\\sigma_i(\\Phi)^2\\ge v^2-2\\sqrt{\\varepsilon/\\lambda}\\) upgrades this to \\(\\sigma_{\\min}(T_M)\\ge v^2-2\\sqrt{\\varepsilon/\\lambda}>0\\) for \\(\\varepsilon<\\lambda v^4/4\\). The estimate is an inequality in general, with fibre-wise equality on radial fibres \\(\\Phi=\\rho\\,U\\) (and operator equality when \\(\\rho\\) is constant), so it transfers non-degeneracy and does not determine the spectrum of \\(T_M\\). (iii)~Coincidence fibre and positivity. At coincidence, \\(\\sigma_{\\min}(\\Phi\\Phi^\\dagger)=\\sigma_{\\min}(\\Phi)^2\\) and \\(\\det(\\Phi\\Psi^\\dagger)=\\det\\Phi\\,\\overline{\\det\\Psi}\\) hold exactly, so the diagonal composite inherits pointwise non-degeneracy; every orthogonal compression of a positive-semidefinite fibre bounded below by \\(c\\) retains lower bound \\(c\\), while compression of a non-positive factor can drop below \\(\\sigma_{\\min}\\) -- positivity of the composite is what transports. (iv)~Diagonal state bound. For any one-point state \\(\\omega\\) with potential moment \\(\\mu_{\\mathcal V}:=\\mathbb E_\\omega[\\mathcal V(x)]<\\lambda v^4/4\\), the Loewner estimate \\(\\lambda_{\\min}(\\mathbb E_\\omega[\\Phi\\Phi^\\dagger])\\ge\\mathbb E_\\omega[\\lambda_{\\min}(\\Phi\\Phi^\\dagger)]\\), the fibre identity of (iii), and Markov's inequality give \\(\\lambda_{\\min}(\\mathbb E_\\omega[\\Phi\\Phi^\\dagger])\\ge\\sup_{\\mu_{\\mathcal V}<\\varepsilon<\\lambda v^4/4}\\,(v^2-2\\sqrt{\\varepsilon/\\lambda})(1-\\mu_{\\mathcal V}/\\varepsilon)>0\\): under the single moment hypothesis \\(\\mu_{\\mathcal V}<\\lambda v^4/4\\) -- the one-point moment class made finite by the Gibbs paragraph above, whose smallness remains an input -- the coincidence composite \\(\\mathbb E_\\omega[\\Phi\\Phi^\\dagger]\\) is state-nondegenerate; this is a statement about the composite and not about the mean-field frame \\(e=\\langle\\Phi\\rangle/v\\) of Equation~" + chr(92) + "eqref{eq:vev-is-frame}, whose control is the mean-field gap recorded above. The hypothesis is sharp, the bound being non-positive at \\(\\mu_{\\mathcal V}=\\lambda v^4/4\\) on the threshold fibre \\((0,v,v,v)\\), and no analogous bound holds for the off-diagonal expectation composite, whose fibre-wise Haar average vanishes identically. (v)~Carrier topology. The lower bound \\(w\\) is a property of the carrier, not of the kernel alone: on a periodic grid of \\(n\\) points the Fourier-diagonalised heat kernel of diffusion parameter \\(s\\) has smallest eigenvalue \\(\\exp(-s^2 n^2/4)\\to0\\), while its compression to a fixed band \\(|k|\\le K\\) has grid-independent smallest eigenvalue \\(\\exp(-s^2K^2)\\); a continuum smooth-kernel reading of the composite therefore cannot carry a uniform \\(w>0\\), and the bilocal non-degeneracy of Assumption~" + chr(92) + "ref{ass:nondeg} must be stated on a finite carrier as in (ii), the finite-\\(N\\) matrix-theory regime, or through the coincidence fibre (iii). For a path-ordered transporter \\(W=P\\exp\\int\\omega\\) one has \\(\\sigma_{\\min}(W)\\ge\\exp(-\\int\\sigma_{\\max}(\\omega))\\), with equality on scalar-gauge paths and \\(\\sigma_{\\min}=1\\) for anti-Hermitian \\(\\omega\\). Scope: (i)-(iii) and (v) are identities and conditional estimates under the stated a.e.\\ bounds with explicit sharpness examples, and (iv) is a conditional estimate under the stated moment hypothesis; the carrier measure, the connection class of \\(W\\), and the state \\(\\omega\\) are inputs and are not derived from Equation~" + chr(92) + "eqref{eq:Smicro}, no measure or state is constructed here, the off-diagonal expectation composite is not bounded, the vacuum-manifold fibre measure of Equation~" + chr(92) + "eqref{eq:vacuum-manifold} is untouched, and the computation of \\(w\\) for the specific carrier of Problem~D1 remains open; Assumptions~" + chr(92) + "ref{ass:frame-lock} and~" + chr(92) + "ref{ass:nondeg} remain assumed and this paragraph closes none of Problem~D, Problem~D1, Problem~F or Problem~N, all of which remain OPEN and PROGRAMME-CONDITIONAL." + CRLF)

payload_src = "".join(P)
body = payload_src.rstrip("\r\n").replace(chr(10), CRLF)
payload = (body + CRLF).encode("ascii")

ANCHOR = (
    r"remains the upstream input that gates what any Presentation-B measure "
    r"can be cited as; Assumptions~\ref{ass:frame-lock} and~\ref{ass:nondeg} "
    r"remain assumed, so Problem~D remains OPEN and PROGRAMME-CONDITIONAL."
).encode("ascii")

fails = []

def chk(name, cond):
    print("%-42s %s" % (name, "OK" if cond else "FAIL"))
    if not cond:
        fails.append(name)

def det_ascii(b):
    return any(x > 127 for x in bytearray(b))

def det_eol(b):
    if not b.endswith(CRLF_B):
        return True
    if b"\n" in b.replace(CRLF_B, b""):
        return True
    return re.search(PAT_LONE_CR, b) is not None

def det_lc(b):
    return (b"\\label" in b) or (b"\\cite" in b) or (b"$" in b)

def det_refs(b, srcs):
    for m in re.findall(rb"\\(?:eq)?ref\{([^}]+)\}", b):
        if srcs.count(b"\\label{" + m + b"}") < 1:
            return False
    return True

def det_math(b):
    return b.count(b"\\(") == b.count(b"\\)") and b.count(b"\\[") == b.count(b"\\]")

# real checks
chk("ascii pure", not det_ascii(payload))
chk("CRLF-only EOL (no lone LF or CR)", not det_eol(payload))
chk("no label/cite/dollar", not det_lc(payload))
chk("math \\( \\) balanced", det_math(payload))
allsrc = b""
for f in os.listdir(os.path.join(ROOT, "chapters")):
    if f.endswith(".tex"):
        allsrc += open(os.path.join(ROOT, "chapters", f), "rb").read()
chk("all refs resolve in chapters/", det_refs(payload, allsrc))
chk("anchor unique in appH", open(APPB, "rb").read().count(ANCHOR) == 1)
chk("single paragraph (one line)", payload.count(b"\r\n") == 1)

# injected positive controls: each detector must fire; the CR-CR-LF control
# replaces the dead lone-CR control of r1 (review 122 r1 finding 1): the fixed
# det_eol sees CR-before-CRLF and the guard rejects such payloads.
controls = []
def ctrl(name, fired):
    controls.append((name, bool(fired)))
ctrl("nonascii-bytes", det_ascii(payload.replace(b"Assumption", b"Assum\xc3\xa9tion")))
ctrl("no-CRLF-terminator", det_eol(payload[:-2]))
ctrl("CR-CR-LF-terminator", det_eol(payload[:-2] + CR_B + CRLF_B))
ctrl("label-injection", det_lc(payload + b"\\label{x}" + CRLF_B))
ctrl("dollar-injection", det_lc(payload + b"$x$" + CRLF_B))
ctrl("unresolved-ref", not det_refs(payload.replace(b"ass:nondeg", b"ass:nope-122", 1), allsrc))
ctrl("unbalanced-math", not det_math(payload[:-4] + b"\\)" + CRLF_B))
fired = [n for n, f in controls if f]
print("controls fired: %d/%d" % (len(fired), len(controls)))
for n in fired:
    print("  FIRED %s" % n)
chk("all seven controls fired", len(controls) == 7 and len(fired) == 7)
chk("fixed payload passes det_eol", not det_eol(payload))
chk("CR-CR-LF defect rejected by det_eol", det_eol(payload[:-2] + CR_B + CRLF_B))
chk("payload not CR-CR-LF terminated", not payload.endswith(CR_B + CRLF_B))
chk("exactly one CR and one LF byte", payload.count(CR_B) == 1 and payload.count(LF_B) == 1)

if fails:
    print("GEN FAILURES:", fails)
    raise SystemExit(1)

with open(os.path.join(HERE, "payload-122.tex"), "wb") as fh:
    fh.write(payload)
pre = open(APPB, "rb").read()
assert pre.count(ANCHOR + b"\r\n\r\n") == 1
post = pre.replace(ANCHOR + b"\r\n\r\n", ANCHOR + b"\r\n\r\n" + payload + b"\r\n", 1)
with open(os.path.join(HERE, "preview-appH-spliced.tex"), "wb") as fh:
    fh.write(post)
chk("POST = PRE + payload + 2", len(post) == len(pre) + len(payload) + 2)
print("PRE %d PAY %d POST %d" % (len(pre), len(payload), len(post)))
print("POST-SHA1 %s" % hashlib.sha1(post).hexdigest())
print("PAYLOAD-SHA1 %s" % hashlib.sha1(payload).hexdigest())
print("GEN-FAILURES: %d %s" % (len(fails), fails if fails else "(none)"))
