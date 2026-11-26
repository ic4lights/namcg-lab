# gen_insert_100.py -- SOLE byte authority for insert-r1.tex (item 100, round 1).
# Writes the single-line paragraph (ASCII, one terminal CRLF, one \\emph{header}, \\( \\) math,
# no bare u, no $ [ ] \\ref \\cite, idiom exactly once) and self-checks all hygiene invariants
# BEFORE writing. All numbers are script-verified outputs (pipeline mi_tau_100q.out, mpmath
# rederive_100.out, MC mc100s.out); none typed from head. Run: python -I gen_insert_100.py
import hashlib, pathlib, re
base = pathlib.Path(__file__).resolve().parent
LINE = (
    "\\emph{Full-spectrum conditioning of the fibre coordinate at \\(D=2\\).} Sharpening the "
    "preceding paragraph, decompose the spectrum coordinate into the trace \\(\\tau\\) and the "
    "ratio \\(p_{2}\\), so that conditioning on the spectrum is conditioning on the pair "
    "\\((p_{2},\\tau)\\) and the chain rule gives \\(I((p_{2},\\tau);x)=I(p_{2};x)+"
    "I(\\tau;x\\mid p_{2})\\) exactly. In the constant-variance class the two terms and the "
    "full mutual information vanish identically for every \\(M\\): equality, not merely a "
    "limit. In the column-profile class with \\(g_{1}\\neq g_{2}\\) the exact joint density of "
    "\\((\\tau,p_{2},x)\\) is proportional to \\(\\tau^{2M-1}(p_{2}(1-p_{2}))^{M-2}"
    "(1-2p_{2})^{2}e^{-\\tau\\Lambda}\\) with \\(\\Lambda=(g_{1}^{-1}+g_{2}^{-1})/(2\\sigma^{2})"
    "+(g_{1}^{-1}-g_{2}^{-1})(1-2p_{2})(x-\\tfrac{1}{2})/\\sigma^{2}\\), so that \\(\\tau\\mid "
    "x,p_{2}\\) is \\(\\mathrm{Gamma}(2M)\\) with rate \\(\\Lambda\\), while \\(f(\\tau\\mid "
    "p_{2})\\) is proportional to \\(\\tau^{2M-2}(e^{-\\Lambda_{0}\\tau}-e^{-\\Lambda_{1}\\tau})\\) "
    "with \\(\\Lambda_{0,1}\\) the endpoints of the \\(x\\)-range of \\(\\Lambda\\); the second "
    "term equals \\(E_{x\\mid p_{2}}\\mathrm{KL}(\\mathrm{Gamma}(2M,\\Lambda)\\,\\|\\,f(\\tau\\mid "
    "p_{2}))\\) and is strictly positive for almost every \\(p_{2}\\in(0,\\tfrac{1}{2})\\), since "
    "\\(\\Lambda\\) depends on \\(x\\) unless \\(g_{1}=g_{2}\\) or \\(p_{2}=\\tfrac{1}{2}\\). "
    "Nested quadrature and an independent high-precision path give \\(I(\\tau;x\\mid "
    "p_{2})=0.0390018\\) and \\(I((p_{2},\\tau);x)=0.0499009\\) at \\(M=2\\), and \\(0.0346061\\) "
    "and \\(0.0673135\\) at \\(M=4\\), for \\(g=(1,2)\\), on top of the preceding "
    "\\(I(p_{2};x)=0.0108991\\) and \\(0.0327074\\); these conditioning numbers are exactly "
    "independent of \\(\\sigma\\), invariant under \\(g_{1}\\leftrightarrow g_{2}\\), and vanish "
    "as \\(g_{1}-g_{2}\\to 0\\), with \\(I(\\tau;x\\mid p_{2})=0.157269\\) at \\(M=2\\) for "
    "\\(g=(1,100)\\). These are spectrum-side conditioning numbers about a fibre coordinate: "
    "they bound no state-side profile weight, identify no simplex fibre, and close nothing "
    "in Problem~G.")
ins = (LINE + "\r\n").encode("ascii")
def bail(msg):
    raise SystemExit("REFUSED: " + msg)
txt = ins.decode()
if len(ins) <= 300: bail("too short")
if not (ins.endswith(b"\r\n") and ins[:-2].count(b"\r\n") == 0): bail("termCRLF")
if re.search(r"(?<![A-Za-z0-9])u(?![A-Za-z0-9])", txt): bail("bare u")
if txt.count("\\emph{") != 1 or not txt.startswith("\\emph{"): bail("header")
if any(c in txt for c in "$[]"): bail("math delims")
if any(k in txt for k in ("\\cite", "\\ref{", "\\eqref", "\\label")): bail("ref/cite")
if txt.count("close nothing in Problem~G.") != 1 or "closes nothing" in txt: bail("idiom")
if txt.count("{") != txt.count("}") or txt.count("(") != txt.count(")"): bail("balance")
bad = [w for w in ("TODO", "predecessor", "corrected", "round 1", "we ") if w in txt]
if bad: bail("process words " + str(bad))
(base / "insert-r1.tex").write_bytes(ins)
print("insert-r1.tex bytes=%d sha256=%s idiom=1 parens=%d braces=%d"
      % (len(ins), hashlib.sha256(ins).hexdigest(), txt.count("("), txt.count("{")))
