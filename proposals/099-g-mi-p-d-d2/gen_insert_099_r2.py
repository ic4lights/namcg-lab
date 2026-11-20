# gen_insert_099_r2.py -- SOLE byte authority for insert-r2.tex (item 099, round 2). Supersedes gen_insert_099.py.
# Round-2 change (gatekeeper review-r1, ACCEPT WITH REQUIRED REVISIONS): bare `u` eliminated per the review's
# Corrected snippet, adopted VERBATIM: (i) "\(f_{U}(u)=6(1-2u)^{2}\) and the affine fibre map" -> "the exact
# density \(6(1-2p_{2})^{2}\), \(0<p_{2}<1/2\), of the smaller entry \(p_{2}\) of the spectrum coordinate and the
# affine fibre map"; (ii) "\(\rho=\beta\tau(1-2u)\)" -> "\(\rho=\beta\tau(p_{1}-p_{2})\)". Ordering p1>=p2 is
# inherited from p=(lambda1,lambda2)/tau of the preceding block paragraphs. No numeric or claim change.
# Numerics unchanged from round 1 (review-r1 confirmed all values to <=4e-7 on an independent exact mpmath path).
# Run from repo root:  python -I proposals/099-g-mi-p-d-d2/gen_insert_099_r2.py
import hashlib, re, os
HEADER = r"\emph{Mutual information between the Gram spectrum and the diagonal fibre coordinate at \(D=2\).} "
BODY = (
 r"In the constant-variance \(D=2\) class the fibre coordinate \(x=(G_{11}-\lambda_{2})/(\lambda_{1}-\lambda_{2})\) "
 r"is exactly uniform on the unit interval and exactly independent of the spectrum for every \(M\), by right-unitary "
 r"invariance, so the mutual information between the spectrum and the fibre coordinate vanishes identically; at \(M=2\), "
 r"combining this independence with the exact density \(6(1-2p_{2})^{2}\), \(0<p_{2}<1/2\), of the smaller entry \(p_{2}\) "
 r"of the spectrum coordinate and the affine fibre map gives in closed form "
 r"\(I(p;d_{1})=I(p;t)=I(p;P_{2})=2-\ln 6=0.2082405308\) nats for the ordered-diagonal, pair and quadratic-statistic "
 r"channels, where \(t=|2d_{1}-1|\). In the column-profile class with \(g_{1}\neq g_{2}\) the conditional density of the "
 r"fibre coordinate given the spectrum is the truncated exponential \(e^{-\rho x}\) on the unit interval with "
 r"\(\rho=\beta\tau(p_{1}-p_{2})\) and \(\beta=1/(\sigma^{2}g_{1})-1/(\sigma^{2}g_{2})\), and nested quadrature on the exact "
 r"joint density of \((\tau,p_{2},x)\), cross-checked by direct Wishart sampling, gives \(I(p;x)=0.0108991\) at \(M=2\) and "
 r"\(0.0327074\) at \(M=4\) and \(I(p;P_{2})=0.267988\) at \(M=2\) and \(0.475266\) at \(M=4\) nats for \(g=(1,2)\); "
 r"these values are exactly independent of \(\sigma\), invariant under \(g_{1}\leftrightarrow g_{2}\), and tend to the "
 r"constant-variance values as \(\beta\to 0\). These are spectrum-side numbers about a fibre coordinate: they bound no "
 r"state-side profile weight, identify no simplex fibre, and they close nothing in Problem~G."
)
para = HEADER + BODY
# ---- contract assertions ----
assert para.isprintable(), "non-printable char"
assert all(ord(c) < 128 for c in para), "non-ASCII char"
assert "\n" not in para and "\r" not in para, "line break inside paragraph"
for tok in ["$", r"\cite", r"\ref", r"\eqref", r"\label", "[", "]", "closes nothing", "Vacuum"]:
    assert tok not in para, "forbidden token: " + tok
assert para.count(r"\emph{") == 1 and para.startswith(r"\emph{"), "exactly one header emph"
assert not re.search(r"(?i)\b(status|priority|completion|open|critical|programme|derived)\b", para), "banned word"
assert para.count(r"\(") == para.count(r"\)"), "unbalanced \( \)"
assert not re.search(r"(?<![A-Za-z])u(?![A-Za-z])", para), "bare u token present"
IDIOM = "they close nothing in Problem~G."
assert para.endswith(IDIOM) and para.count(IDIOM) == 1, "idiom must end the paragraph, exactly once"
data = (para + "\r\n").encode("ascii")
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "insert-r2.tex")
open(out, "wb").write(data)
print("bytes=%d sha256=%s" % (len(data), hashlib.sha256(data).hexdigest()))
print("chars=%d parens=%d emph=1 idiom=1 bare_u=0" % (len(para), para.count(r"\(")))
