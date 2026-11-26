"""Verbatim check: the S1/S2 OLD/NEW strings used in apply_check_066_r5.py must equal the four
fenced latex snippets in review-r4.md section "## Corrected snippet", in order
(S1 OLD, S1 NEW, S2 OLD, S2 NEW), with CRLF as line separator.
Usage: python -I verbatim_check_066_r5.py <repo_root>
The expected strings are reconstructed here with the same string-building helpers as
apply_check_066_r5.py, and additionally compared against the junction of F1 NEW lines and the
last line of F10 NEW plus the two baseline lines, exactly as asserted inside the apply script."""
import re, sys
B = chr(92); NL = "\r\n"
def L(*a): return NL.join(a)
def c(s): return B + "(" + s + B + ")"
def c2(s): return c(s)

repo = sys.argv[1]
TH = c(B + "Theta")
MAP = c("(" + B + "hat X," + B + "Phi)" + B + "mapsto H_D")

# S1/S2 exactly as encoded in apply_check_066_r5.py:
S1_OLD = L("mass " + c("m_" + B + "sigma") + " of Section~" + B + "ref{sec:ch3-scales}. Hence the charge",
           "is a vacuum modular Hamiltonian only where it coincides with one of")
S1_NEW = L("mass " + c("m_" + B + "sigma") + " of Section~" + B + "ref{sec:ch3-scales}. Hence the charge",
           "is known to be a vacuum modular Hamiltonian only where it coincides",
           "with one of")
S2_OLD = L("elsewhere that recovery is not known to suffice. That matching has",
           "not been performed for higher-order, interacting, or fluctuating-" + TH,
           "terms and is not a routine specialisation of the free-field result. The")
S2_NEW = L("elsewhere that recovery is not known to suffice. That matching has",
           "not been performed, even in the quadratic sector, where the Weyl-symbol",
           "identification above is not derived; for higher-order, interacting, or",
           "fluctuating-" + TH + " terms it would not be a routine specialisation of",
           "the free-field case. The")

t = open(repo + "/proposals/claude-remote/066-bw-diamond-scope-correction/review-r4.md",
         encoding="utf-8").read().replace("\r\n", "\n")
sec = t.split("## Corrected snippet")[1]
blocks = [b.replace("\n", NL) for b in re.findall(r"```latex\n(.*?)\n```", sec, re.S)]
names = ["S1_OLD", "S1_NEW", "S2_OLD", "S2_NEW"]
exp = [S1_OLD, S1_NEW, S2_OLD, S2_NEW]
ok = len(blocks) == 4
for n, b, e in zip(names, blocks, exp):
    same = b == e
    print(f"{n}: verbatim match to review-r4 snippet = {same}")
    if not same:
        print("  snippet:", repr(b))
        print("  encoded:", repr(e))
    ok &= same
# Cross-consistency with the F1/F10 NEW strings (same construction as in the r4/r5 scripts):
E1_HEAD_last = ("mass " + c("m_" + B + "sigma") + " of Section~" + B + "ref{sec:ch3-scales}. Hence the charge")
R2_TAIL_first = "is a vacuum modular Hamiltonian only where it coincides with one of"
F10_NEW_last = "elsewhere that recovery is not known to suffice. That matching has"
j1 = S1_OLD == NL.join([E1_HEAD_last, R2_TAIL_first])
j2 = S2_OLD == NL.join([F10_NEW_last,
                        "not been performed for higher-order, interacting, or fluctuating-" + TH,
                        "terms and is not a routine specialisation of the free-field result. The"])
print("S1_OLD == junction of F1 NEW lines:", j1)
print("S2_OLD == F10 NEW last line + baseline lines:", j2)
ok &= j1 and j2
print("VERBATIM CHECK PASS" if ok else "VERBATIM CHECK FAIL")
