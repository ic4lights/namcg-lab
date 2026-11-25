# gen_payload_117_r2.py -- round-2 payload generator for proposal 117.
# The r1 payload (insert-d1-state-measure.tex, sha1 b514e44a..., 4597 B) is
# KEPT UNTOUCHED as the substitution base. The r2 payload
# (insert-d1-state-measure-r2.tex) is produced by applying EXACTLY the
# (v)-sentence replacement (gatekeeper option (a): drop \mathrm{Vol}^{-1} on
# the left of the soft-event display and rename "volume-averaged" to
# "spacetime-integrated") to the r1 bytes. No other byte changes.
# Two independent reconstruction paths are asserted:
#   (1) byte replacement on the r1 bytes  ->  r2 bytes;
#   (2) the r1 FRAGS machinery with the two modified fragments (join-absorb
#       assertion kept) -> the same bytes.
# Reverse substitution on the r2 bytes must recover the r1 bytes byte-exactly.
# Run:  python -I -B gen_payload_117_r2.py
# Expected output tail: "bytes 4585 CR 2 LF 2 CRLF 2 ..." and "PAYLOAD SCAN OK"
import os, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
R1SHA = "b514e44a19ee627f0aab4ac3d4f69bc052506154"

OLD_SENT = (b"so the volume-averaged soft-event estimate "
            b"\\(\\mathrm{Vol}^{-1}\\int\\omega_x")
NEW_SENT = (b"so the spacetime-integrated soft-event estimate "
            b"\\(\\int\\omega_x")

# ---- path 1: byte replacement on the r1 bytes ----
r1 = open(os.path.join(HERE, "insert-d1-state-measure.tex"), "rb").read()
assert hashlib.sha1(r1).hexdigest() == R1SHA, "r1 payload moved off its pin"
assert len(r1) == 4597
assert r1.count(OLD_SENT) == 1, "OLD (v) sentence not unique in r1: %d" % r1.count(OLD_SENT)
data = r1.replace(OLD_SENT, NEW_SENT, 1)
assert data.count(NEW_SENT) == 1
assert data.count(OLD_SENT) == 0
# byte-reconstruction proof (reverse direction): r2 with the inverse
# replacement hashes to the r1 payload
back = data.replace(NEW_SENT, OLD_SENT, 1)
assert back == r1, "reverse replacement does not recover r1 bytes"
print("r1 bytes %d sha1 %s" % (len(r1), hashlib.sha1(r1).hexdigest()))
print("v-replacement applied count 1 (delta %+d)" % (len(data) - len(r1)))
print("reverse-substitution recovers r1 bytes OK")

# ---- path 2: FRAGS rebuild (join-absorb assertion kept), modified (v) frags ----
FRAGS = [
    "\\emph{A Euclidean Gibbs probe measure with automatic first moment.} ",
    "This paragraph records a conditional construction of a measure with finite ",
    "one-point potential moment, supplying the single consumable estimate left ",
    "open by the paragraph above, and its typed one-point consequences. Let ",
    "\\(\\mathrm{dvol}\\) be the volume element of the Presentation-B background, ",
    "assumed closed with finite volume \\(\\mathrm{Vol}\\), fix the background ",
    "gauge field of Equation~\\eqref{eq:Smicro}, and take as hypothesis its ",
    "Euclidean continuation \\(S_E[\\Phi]=\\int(\\lvert D\\Phi\\rvert_F^2+",
    "\\mathcal V(\\Phi))\\,\\mathrm{dvol}\\) with \\(\\mathcal V\\) the potential ",
    "of Equation~\\eqref{eq:V}. Restrict \\(\\Phi\\) to a finite-dimensional ",
    "real-linear space of matrix fields containing the constant fields, with ",
    "coordinates \\(\\phi\\in\\mathbb R^K\\) and \\(\\phi\\mapsto\\Phi(x)\\) linear ",
    "and non-zero at each \\(x\\) (the truncation), and define the Gibbs history ",
    "measure \\(\\mu=\\mathcal Z^{-1}e^{-S_E}\\prod_k\\mathrm d\\phi_k\\) with ",
    "normalizing integral \\(\\mathcal Z\\), keeping the history measure \\(\\mu\\) ",
    "notationally distinct from the volume element \\(\\mathrm{dvol}\\). Then: ",
    "(i) \\(0<\\mathcal Z<\\infty\\): \\(S_E(\\phi)\\to\\infty\\) as ",
    "\\(\\lVert\\phi\\rVert_2\\to\\infty\\) (since \\(\\int\\lvert\\Phi\\rvert_F^4",
    "\\,\\mathrm{dvol}=0\\) forces \\(\\Phi\\equiv0\\) and the pointwise coercivity ",
    "\\(\\mathcal V\\ge(\\lambda/32)\\lVert\\Phi\\rVert_F^4-2\\lambda v^4\\), verified ",
    "below, controls the quartic uniformly on the unit sphere of the truncation), ",
    "so \\(\\mathcal Z\\) is dominated by a super-Gaussian integral; and ",
    "\\(\\mathcal Z>0\\) because \\(S_E\\) is bounded on the tube of constant ",
    "fields \\(v(\\mathbb I+\\{\\lVert E\\rVert_F\\le\\rho\\})\\) about the vacuum ",
    "manifold Equation~\\eqref{eq:vacuum-manifold}. ",
    "(ii) The first moment is automatic: the pointwise interpolation ",
    "\\(\\sup_x\\lVert\\Phi(x)\\rVert_F\\le C\\lVert\\phi\\rVert_2\\) on the ",
    "truncation, Jensen's inequality, and the coercivity bounds give ",
    "\\(\\mathcal V(x)\\le(8C^4/\\mathrm{Vol})\\int\\mathcal V\\,\\mathrm{dvol}",
    "+\\lambda v^4(16C^4+1)\\le(8C^4/\\mathrm{Vol})\\,S_E+\\lambda v^4(16C^4+1)\\), ",
    "whence \\(\\mathbb E_\\mu[\\mathcal V(x)]\\le(8C^4/\\mathrm{Vol})\\,",
    "\\mathbb E_\\mu[S_E]+\\lambda v^4(16C^4+1)\\) and, since ",
    "\\(\\sup_{s\\ge0}s\\,e^{-s/2}=2/e\\), ",
    "\\(\\mathbb E_\\mu[S_E]\\le(2/e)\\,\\mathcal Z(1/2)/\\mathcal Z(1)\\), where ",
    "\\(\\mathcal Z(\\beta)\\) is the normalizing integral of \\(e^{-\\beta S_E}\\). ",
    "(iii) The estimate of the paragraph above, applied to the one-point ",
    "distribution \\(\\omega_x\\) of \\(\\Phi(x)\\), gives ",
    "\\(\\omega_x\\{\\det e(x)=0\\}\\le\\omega_x\\{\\mathcal V(x)\\ge\\lambda v^4/4\\}",
    "\\le\\min\\{1,4\\,\\mathbb E_{\\omega_x}[\\mathcal V(x)]/(\\lambda v^4)\\}\\) ",
    "under the same configuration-level reading of \\(e\\) through ",
    "Equation~\\eqref{eq:vev-is-frame}; and on this measure the event itself has ",
    "zero mass, \\(\\omega_x\\{\\det e(x)=0\\}=0\\) identically: the singular set ",
    "is a proper real-algebraic cone and the constant identity field lies in the ",
    "truncation, so its inverse image under \\(\\phi\\mapsto\\Phi(x)\\) is a ",
    "proper algebraic subset of \\(\\mathbb R^K\\), which the \\(e^{-S_E}\\)-density ",
    "cannot charge. ",
    "(iv) By Fubini's theorem, \\(\\mu\\)-almost every configuration has ",
    "spacetime-Lebesgue-null defect set \\(\\{x:\\det\\Phi(x)=0\\}\\) - null, not ",
    "empty, so this does not discharge the pointwise Assumption~\\ref{ass:nondeg}. ",
    "(v) For the inverse-temperature family \\(\\mu_\\beta\\propto ",
    "e^{-\\beta S_E}\\), convexity of \\(\\ln\\mathcal Z(\\beta)\\) makes ",
    "\\(\\mathbb E_{\\mu_\\beta}[S_E]\\) nonincreasing in \\(\\beta\\), so the ",
    "spacetime-integrated soft-event estimate ",
    "\\(\\int\\omega_x\\{\\mathcal V(x)\\ge\\lambda v^4/4\\}\\,",
    "\\mathrm{dvol}\\le4\\,\\mathbb E_{\\mu_\\beta}[S_E]/(\\lambda v^4)\\le",
    "4\\,\\mathbb E_{\\mu_{\\beta_0}}[S_E]/(\\lambda v^4)\\) holds for every ",
    "\\(\\beta\\ge\\beta_0\\). ",
    "Scope: the hypotheses are stated and the conclusions are conditional ",
    "derivations within them; \\(\\mu\\) is a Euclidean Gibbs probe measure on a ",
    "truncated Presentation-B field theory and not a state of the matrix theory, ",
    "its Wick rotation, the closedness of the background and the choice of ",
    "truncation are assumed rather than derived, the estimate lives at ",
    "configuration level so the vacuum-expectation reading ",
    "\\(e=\\langle\\Phi\\rangle/v\\) of Equation~\\eqref{eq:vev-is-frame} would ",
    "additionally require control of the mean field \\(\\mathbb E_\\mu[\\Phi(x)]\\) ",
    "that is not provided here, removal of the truncation is open, and the ",
    "selection of Equation~\\eqref{eq:V} by Presentation~A ",
    "(Section~\\ref{sec:ch3-relate}) remains the upstream input that gates what ",
    "any Presentation-B measure can be cited as; ",
    "Assumptions~\\ref{ass:frame-lock} and~\\ref{ass:nondeg} remain assumed, so ",
    "Problem~D remains OPEN and PROGRAMME-CONDITIONAL.",
]
line = "".join(FRAGS)
assert "\n" not in line and "\r" not in line, "fragments must not contain newlines"
import re as _re
for _i in range(len(FRAGS) - 1):
    assert not (_re.search(r'\\\\[A-Za-z]+$', FRAGS[_i]) and FRAGS[_i+1][:1].isalpha()), ("macro-absorb join at", _i)
data_frags = b"\r\n" + line.encode("ascii") + b"\r\n"
assert data_frags == data, "FRAGS rebuild differs from byte-replacement payload"
print("frags-rebuild matches byte-replacement payload OK")

out = os.path.join(HERE, "insert-d1-state-measure-r2.tex")
with open(out, "wb") as f:
    f.write(data)

# ---- byte scan (as r1) ----
cr = data.count(b"\r"); lf = data.count(b"\n"); crlf = data.count(b"\r\n")
loneCR = cr - crlf; loneLF = lf - crlf
tab = data.count(b"\t"); nonascii = sum(1 for b in data if b > 127)
ctrl = sum(1 for b in data if b < 32 and b not in (13, 10))
endsCRLF = data.endswith(b"\r\n")
bom = data.startswith(b"\xef\xbb\xbf")
backslashws = 0
for i in range(len(data) - 1):
    if data[i:i+1] == b"\\" and data[i+1:i+2] in (b" ", b"\t", b"\r", b"\n"):
        backslashws += 1
print("bytes %d CR %d LF %d CRLF %d loneCR %d loneLF %d tab %d nonASCII %d ctrl %d endsCRLF %s BOM %s backslash-ws %d"
      % (len(data), cr, lf, crlf, loneCR, loneLF, tab, nonascii, ctrl, endsCRLF, bom, backslashws))
assert cr == lf == crlf == 2 and loneCR == 0 and loneLF == 0
assert tab == 0 and nonascii == 0 and ctrl == 0 and endsCRLF and not bom
assert backslashws == 0
for forb in [b"\\label", b"\\cite"]:
    assert forb not in data, forb.decode()
for req in [b"eq:Smicro", b"eq:V", b"eq:vacuum-manifold", b"eq:vev-is-frame",
            b"ass:nondeg", b"ass:frame-lock", b"sec:ch3-relate",
            b"OPEN and PROGRAMME-CONDITIONAL"]:
    assert req in data, req.decode()

# ---- macro-token whitelist scan (as _scan_macro_join.py, whitelist identical) ----
known = {
    "emph", "eqref", "ref", "label", "cite", "mathrm", "mathcal", "mathbb",
    "mathbf", "operatorname", "propto", "le", "ge", "in", "to", "infty",
    "det", "min", "sup", "int", "prod", "sum", "lvert", "rvert", "lVert",
    "rVert", "phi", "Phi", "mu", "beta", "lambda", "sigma", "alpha", "eta",
    "omega", "Omega", "epsilon", "varepsilon", "rho", "nu", "xi", "pi",
    "hat", "bar", "tilde", "vec", "mathit", "boldsymbol", "bigl", "bigr",
    "Bigl", "Bigr", "left", "right", "frac", "tfrac", "text", "textrm",
    "substack", "displaystyle", "ldots", "cdots", "dots", "colon", "mid",
    "coloncolon", "setminus", "subset", "subseteq", "supset", "cup", "cap",
    "vee", "wedge", "lnot", "partial", "nabla", "times", "cdot", "circ",
    "langle", "rangle", "lbrack", "rbrack", "lbrace", "rbrace",
    "Re", "Im", "arg", "ker", "tr", "rank", "supp", "Vol",
}
tokens = sorted(set(_re.findall(r"\\([A-Za-z]+)", line)))
bad = [t for t in tokens if t not in known]
print("distinct macro tokens: %d  UNKNOWN: %s" % (len(tokens), bad))
assert bad == ["equiv", "ln", "mapsto"] or bad == [], "unexpected macro tokens: %s" % bad

print("r2 sha1 %s size %d" % (hashlib.sha1(data).hexdigest(), len(data)))
print("PAYLOAD SCAN OK")
