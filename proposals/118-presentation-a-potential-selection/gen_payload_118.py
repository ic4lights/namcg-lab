# gen_payload_118.py -- payload generator for proposal 118 (insert-potential-selection-r1.tex).
# Rebuilds the manuscript-bound paragraph byte-exactly from FRAGS (one line,
# leading CRLF separator, trailing CRLF, no internal line breaks), with the
# macro-absorption assertion at every fragment join (a fragment ending in
# \macro must not be followed by a letter) and the full byte-hygiene scan of
# the 117 r2 generator (CR/LF/CRLF counts, lone breaks, tabs, ASCII, control
# bytes, backslash-whitespace, delimiter pairing, endsCRLF, BOM, forbidden
# \label/\cite, required ref labels, macro-token whitelist).
# Idempotence: if the payload file already exists, its bytes must equal the
# rebuilt bytes before anything is written (regeneration reproduces byte-identically).
# NOTE: the join regex is r'\\[A-Za-z]+$' (ONE literal backslash then a word);
# the 117 r2 generator used r'\\\\[A-Za-z]+$', which matches a doubled
# backslash and was therefore vacuous on single-backslash LaTeX sources -
# corrected here so the check actually bites.
# Run:  python -I -B gen_payload_118.py     (from the proposal folder)
# Expected output tail: "bytes ... CR 2 LF 2 CRLF 2 ..." and "PAYLOAD SCAN OK"
import os, hashlib, re as _re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "insert-potential-selection-r1.tex")

FRAGS = [
    "\\emph{Constraint results on the Presentation-A selection of Equation~\\eqref{eq:V}.} ",
    "This paragraph records constraint results bearing on the selection of the Higgs ",
    "potential by Presentation~A, the missing input of Section~\\ref{sec:ch3-relate}; no ",
    "derivation of that selection from Equation~\\eqref{eq:Smatrix} is obtained, and ",
    "Assumption~\\ref{ass:dictionary} remains the assumed matching condition throughout. ",
    "Write \\(X=\\Phi^\\dagger\\Phi\\). (i) Forced form and exact slice: under the stated ",
    "bifundamental field content and the quartic degree-\\((2,2)\\) truncation, invariance ",
    "under independent left and right unitary transformations of \\(\\Phi\\) leaves exactly ",
    "two real quartic invariants, \\(\\mathrm{Tr}\\,X^2\\) and \\((\\mathrm{Tr}\\,X)^2\\), with ",
    "\\(\\mathrm{Tr}\\,X^2=\\sum_{i=1}^4\\sigma_i(\\Phi)^4\\) in the singular values ",
    "\\(\\sigma_i(\\Phi)\\) (hence non-negative), so the ",
    "general quartic matter potential is the two-parameter family \\(\\mathcal V=c_3\\,",
    "\\mathrm{Tr}\\,X^2+c_2(\\mathrm{Tr}\\,X)^2+c_1\\,\\mathrm{Tr}\\,X+c_0\\); Equation~\\eqref{eq:V} ",
    "is exactly the slice \\((c_3,c_2,c_1,c_0)=(\\lambda/4,\\,0,\\,-\\lambda v^2/2,\\,\\lambda v^4)\\) ",
    "at internal dimension four, its constant \\(c_0=\\lambda v^4\\) being the sum of the four ",
    "squared terms; the selection question reduces to the ratio \\(c_2/c_3\\), which ",
    "Equation~\\eqref{eq:V} sets to zero, and to the signs. Every point of ",
    "Equation~\\eqref{eq:vacuum-manifold} is stationary for this potential, whose gradient ",
    "\\((\\lambda/2)\\,\\Phi(X-v^2\\mathbb I)\\) is the potential term of Equation~\\eqref{eq:Phi-eom}. ",
    "(ii) Family theorem and slice threshold: throughout the strictly bounded-below region ",
    "\\(c_3>0\\), \\(c_3+4c_2>0\\) - where the Hessian in \\(x_i=\\sigma_i(\\Phi)^2\\) has ",
    "eigenvalues \\(2c_3\\) (three times) and \\(2c_3+8c_2\\), so the region is also strict ",
    "convexity - the family has a unique vacuum \\(X=s\\,\\mathbb I\\) with ",
    "\\(s=-c_1/(2(c_3+4c_2))\\); the infimum over \\(\\{\\det\\Phi=0\\}\\) is attained at singular ",
    "values \\((0,w,w,w)\\) with \\(w^2=-c_1/(2(c_3+3c_2))\\); and the defect gap \\(\\Delta=",
    "(c_1^2/4)\\,(c_3/12)/[(c_3/4+c_2)(c_3/3+c_2)]\\) is strictly positive through the whole ",
    "region. On the slice of Equation~\\eqref{eq:V} one has \\(s=v^2\\), the vacuum is the ",
    "manifold of Equation~\\eqref{eq:vacuum-manifold}, and \\(\\Delta=\\lambda v^4/4\\): the ",
    "defect threshold recorded above is re-derived as a slice of a family theorem, its ",
    "positivity is region-wide while its value is slice-dependent, and off the slice the ",
    "face minimizer moves, \\(w\\ne s\\). (iii) Pinned truncation order: for the ",
    "constant-\\(\\Theta\\) Moyal product of Section~\\ref{sec:ch3-relate} the two-point phase ",
    "vanishes exactly and the four-point phase is cyclic on the momentum-conservation shell, ",
    "while the quartic vertex carries the three channel factors \\(\\cos(\\Theta p/2)\\), ",
    "\\(\\cos(\\Theta q/2)\\), \\(\\cos(\\Theta(p+q)/2)\\), pairwise distinct and coinciding flatly ",
    "at \\(\\Theta=0\\) with \\(1-\\cos(\\Theta p/2)=\\Theta^2p^2/8+O(\\Theta^4)\\); no choice of ",
    "\\(c_0,c_1,c_2,c_3\\) absorbs these phases, so a channel-blind local ",
    "\\(\\mathrm{Tr}\\)-polynomial vertex such as Equation~\\eqref{eq:V} can match the ",
    "Presentation-A quartic vertex only through order \\(\\Theta^2\\) - a truncation output, ",
    "not an exact finite-\\(\\Theta\\) output, of the assumed dictionary. (iv) Quartic-order ",
    "boundary: beyond quartic order the gap property fails, since ",
    "\\(\\varepsilon(\\mathrm{Tr}\\,X)^4-\\mathrm{Tr}\\,X^2\\) with \\(\\varepsilon>0\\) is bounded ",
    "below with its global minimum on \\(\\{\\det\\Phi=0\\}\\) at rank one, of value ",
    "\\(-1/(4\\varepsilon)\\); the gap statements of (ii) are theorems of the quartic class, ",
    "not of bounded matrix potentials. Scope: (i)-(iv) are identities and exact reductions, ",
    "a family theorem conditional on the stated field content and truncation, and an ",
    "explicit counterexample; the field content, the quartic truncation, constant ",
    "\\(\\Theta\\), and Assumption~\\ref{ass:dictionary} are assumed and not derived, the ",
    "selection of Equation~\\eqref{eq:V} is constrained but not derived-closed, and nothing ",
    "in this paragraph closes Problem~D, Problem~D1, or Problem~A.",
]
line = "".join(FRAGS)
assert "\n" not in line and "\r" not in line, "fragments must not contain newlines"

# macro-absorption assertion at every join: a fragment ending in \macro must
# not be followed by a letter (LaTeX would swallow it into the macro name)
for _i in range(len(FRAGS) - 1):
    assert not (_re.search(r'\\[A-Za-z]+$', FRAGS[_i]) and FRAGS[_i+1][:1].isalpha()), ("macro-absorb join at", _i)
print("joins checked %d, macro-absorb none" % (len(FRAGS) - 1))

data = b"\r\n" + line.encode("ascii") + b"\r\n"
if os.path.exists(OUT):
    prev = open(OUT, "rb").read()
    assert prev == data, "regeneration differs from existing payload bytes"
    print("regeneration byte-identical to existing payload OK")
with open(OUT, "wb") as f:
    f.write(data)

# ---- byte hygiene scan ----
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
lb = data.count(b"\\("); rb = data.count(b"\\)")
ob = line.count("{"); cb = line.count("}")
print("bytes %d CR %d LF %d CRLF %d loneCR %d loneLF %d tab %d nonASCII %d ctrl %d endsCRLF %s BOM %s backslash-ws %d \\( %d \\) %d braces %d/%d"
      % (len(data), cr, lf, crlf, loneCR, loneLF, tab, nonascii, ctrl, endsCRLF, bom, backslashws, lb, rb, ob, cb))
assert cr == lf == crlf == 2 and loneCR == 0 and loneLF == 0
assert tab == 0 and nonascii == 0 and ctrl == 0 and endsCRLF and not bom
assert backslashws == 0
assert lb == rb
assert ob == cb
assert data.startswith(b"\r\n\\emph{"), "payload must start CRLF + \\emph{"
for forb in [b"\\label", b"\\cite"]:
    assert forb not in data, forb.decode()
for req in [b"eq:V", b"eq:Smatrix", b"ass:dictionary", b"eq:vacuum-manifold",
            b"sec:ch3-relate", b"eq:Phi-eom"]:
    assert req in data, req.decode()
print("forbidden \\label/\\cite absent; required labels present")

# ---- macro-token whitelist scan ----
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
    "dagger", "cos", "Theta", "ne", "Delta",
}
tokens = sorted(set(_re.findall(r"\\([A-Za-z]+)", line)))
bad = [t for t in tokens if t not in known]
print("distinct macro tokens: %d  %s  UNKNOWN: %s" % (len(tokens), tokens, bad))
assert bad == [], "unexpected macro tokens: %s" % bad

print("sha1 %s size %d" % (hashlib.sha1(data).hexdigest(), len(data)))
print("PAYLOAD SCAN OK")
