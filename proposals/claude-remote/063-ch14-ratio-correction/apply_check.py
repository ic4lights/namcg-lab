"""Apply the 063 OLD->NEW edits to chapters/ch14-dissipation.tex IN MEMORY (or to an output copy).
Backslashes are built from chr(92): the placeholder '@' stands for a backslash.
Usage: python apply_check.py <repo_root> [output_copy_path]"""
import sys, hashlib, pathlib
BS = chr(92)
CRLF_B = bytes([13, 10])
def L(*lines):
    s = "\r\n".join(lines)
    assert "@@" not in s
    return s.replace("@", BS)

OLD1 = L(
"For a circular Newtonian orbit, @(v^2=@Geff M/d@) and",
"@(@Omega^2=@Geff M/d^3@), so",
"@begin{equation}",
"  @label{eq:ratio}",
"  @frac{P_{@mathrm{ent}}}{P_{@mathrm{GW}}}",
"  @;@sim@;",
"  @frac{@eta}{@Geff^3 M^2@mu}@,",
"  @Bigl(@frac{d}{@Geff M}@Bigr)^{k}",
"@end{equation}",
"with a positive power of @(d@) that makes the ratio @emph{grow}",
"toward wide separations if @(@eta@) is held fixed. That conclusion",
"is an artefact of treating @(@eta@) as constant down to laboratory",
"distances. If @(@eta@) is instead suppressed at wide separations, the",
"growth need not occur; this book does not calculate that dependence,",
"and a sufficiently small @(@eta@) is required for consistency with",
"Solar-System tests.")
NEW1 = L(
"For a circular Newtonian orbit, @(v^2=@Geff M/d@) and",
"@(@Omega^2=@Geff M/d^3@), so both powers fall as @(d^{-5}@) and",
"@begin{equation}",
"  @label{eq:ratio}",
"  @frac{P_{@mathrm{ent}}}{P_{@mathrm{GW}}}",
"  @;@sim@;",
"  @frac{5}{32}@,",
"  @frac{@eta}{@Geff^3 M^2@mu},",
"@end{equation}",
"up to the inclination factors in~@eqref{eq:Peters}. With @(@eta@)",
"constant on a given inspiral, as in Assumption~@ref{ass:drag}, this",
"ratio does not depend on @(d@): the working law singles out no",
"separation at which the entropic channel overtakes the quadrupole",
"channel, and the comparison is fixed by @(@eta@) and the masses.",
"Because both losses have the same dependence on @(d@), and hence on",
"the orbital frequency, the extra loss multiplies the leading-order",
"quadrupole frequency evolution by the constant factor",
"@(1+P_{@mathrm{ent}}/P_{@mathrm{GW}}@). At that order it is",
"degenerate with a rescaling of the chirp mass",
"@(@mathcal M=@mu^{3/5}M^{2/5}@) to",
"@((1+P_{@mathrm{ent}}/P_{@mathrm{GW}})^{3/5}@mathcal M@).",
"For a drag falling as @(d^{-n}@) the same computation gives a ratio",
"proportional to @(d^{4-n}@); a ratio that grows toward wide",
"separations would require @(n<4@), which",
"Assumption~@ref{ass:drag} does not adopt. This book does not",
"calculate whether @(@eta@) differs between regimes, and a",
"sufficiently small @(@eta@) is required for consistency with",
"Solar-System tests.")
OLD2 = L(
"    inspiral and estimate a separation where the two powers",
"    could be comparable for a chosen @(@eta@).")
NEW2 = L(
"    inspiral, show that their ratio does not depend on @(d@), and",
"    find the value of @(@eta@), in terms of the masses, at which the",
"    two powers are comparable. For which drag exponents would the",
"    ratio depend on separation?")
EDITS = [("block1 sec:ch14-quad eq:ratio", OLD1, NEW1), ("block2 exercise Energy identity", OLD2, NEW2)]

def report(tag, b):
    crlf = b.count(b"\r\n"); lf = b.count(b"\n"); cr = b.count(b"\r")
    print(f"{tag}: bytes={len(b)} sha256={hashlib.sha256(b).hexdigest()}")
    bom = b.startswith(bytes([0xEF, 0xBB, 0xBF]))
    tw = sum(1 for x in b.split(CRLF_B) if x.rstrip(b" " + bytes([9])) != x)
    print(f"  CRLF={crlf} bare-LF={lf-crlf} bare-CR={cr-crlf} BOM={bom} trailing-ws-lines={tw}")

root = pathlib.Path(sys.argv[1])
p = root / "chapters" / "ch14-dissipation.tex"
raw = p.read_bytes()
report("baseline", raw)
txt = raw.decode("utf-8")
for name, old, new in EDITS:
    c = txt.count(old)
    print(f"{name}: OLD occurrences={c}; NEW occurrences before={txt.count(new)}")
    assert c == 1, name
    txt = txt.replace(old, new)
    print(f"  after: OLD={txt.count(old)} NEW={txt.count(new)}")
out = txt.encode("utf-8")
report("result", out)
for lab in ["label{eq:ratio}", "label{eq:Peters}", "label{ass:drag}"]:
    print(f"count {lab} in result: {txt.count(BS+lab)}")
assert "\n" not in out.replace(b"\r\n", b"").decode()
if len(sys.argv) > 2:
    pathlib.Path(sys.argv[2]).write_bytes(out)
    print("wrote", sys.argv[2])
