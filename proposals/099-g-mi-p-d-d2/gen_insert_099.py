# gen_insert_099.py -- sole byte authority for insert-r1.tex (item 099).
# CORRECTION 2026-11-19: the hetero I(p;P_2) values are the rederive_099.py panel-quadrature numbers
# 0.267988 (M=2) and 0.475266 (M=4), replacing the predecessor nested-quadrature values 0.2863661/0.4958970;
# the predecessor t-channel overestimates by ~1.8e-2 (see proposal-r1.md), its beta=0 self-test already
# showed +4.4e-3 bias, and KSG nearest-neighbour MC (bias-calibrated on the exact constant-variance case)
# gives 0.2679/0.4738+-0.002, ruling out 0.286/0.496. The I(p;x) values are unchanged (independently
# reproduced to 8 digits by rederive_099.py).
# Run from repo root:  python -I proposals/099-g-mi-p-d-d2/gen_insert_099.py
import hashlib, re, os
HEADER = r"\emph{Mutual information between the Gram spectrum and the diagonal fibre coordinate at \(D=2\).} "
BODY = (
 r"In the constant-variance \(D=2\) class the fibre coordinate \(x=(G_{11}-\lambda_{2})/(\lambda_{1}-\lambda_{2})\) "
 r"is exactly uniform on the unit interval and exactly independent of the spectrum for every \(M\), by right-unitary "
 r"invariance, so the mutual information between the spectrum and the fibre coordinate vanishes identically; at \(M=2\), "
 r"combining this independence with \(f_{U}(u)=6(1-2u)^{2}\) and the affine fibre map gives in closed form "
 r"\(I(p;d_{1})=I(p;t)=I(p;P_{2})=2-\ln 6=0.2082405308\) nats for the ordered-diagonal, pair and quadratic-statistic "
 r"channels, where \(t=|2d_{1}-1|\). In the column-profile class with \(g_{1}\neq g_{2}\) the conditional density of the "
 r"fibre coordinate given the spectrum is the truncated exponential \(e^{-\rho x}\) on the unit interval with "
 r"\(\rho=\beta\tau(1-2u)\) and \(\beta=1/(\sigma^{2}g_{1})-1/(\sigma^{2}g_{2})\), and nested quadrature on the exact "
 r"joint density of \((\tau,u,x)\), cross-checked by direct Wishart sampling, gives \(I(p;x)=0.0108991\) at \(M=2\) and "
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
IDIOM = "they close nothing in Problem~G."
assert para.endswith(IDIOM) and para.count(IDIOM) == 1, "idiom must end the paragraph, exactly once"
data = (para + "\r\n").encode("ascii")
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "insert-r1.tex")
open(out, "wb").write(data)
print("bytes=%d sha256=%s" % (len(data), hashlib.sha256(data).hexdigest()))
print("chars=%d parens=%d emph=1 idiom=1" % (len(para), para.count(r"\(")))
