# verify_anchors_127.py -- anchor uniqueness for proposal 127 payload bytes.
# Run: python -I verify_anchors_127.py   (from the proposal folder; repo root
# is two levels up). Counts exact substring occurrences in the live bytes.
# Backslashes are built with chr(92): no backslash escape appears in a needle.
import io, sys
B = chr(92)
ROOT = "../../chapters/"
def count(rel, needle):
    data = io.open(ROOT + rel, "rb").read().decode("utf-8")
    return data.count(needle)
results = []
def check(name, cond):
    ok = bool(cond); results.append((name, ok))
    print(("PASS " if ok else "FAIL ") + name)
check("A1 ch03 matching-condition sentence unique",
      count("ch03-matrix-action.tex",
            "this is a matching condition, not an established result") == 1)
check("A2 ch03 sign-clause sentence unique",
      count("ch03-matrix-action.tex",
            "including its sign in the signature") == 1)
check("A3 appH completion-class paragraph head unique",
      count("appH-microscopic-proofs.tex",
            B + "paragraph{The named completion class and the remainder bound.}") == 1)
check("A4 appH kinetic-sign input sentence unique",
      count("appH-microscopic-proofs.tex",
            "the kinetic-sign content of Assumption~" + B + "ref{ass:dictionary}") == 1)
check("A5 POS-CONTROL counter fires on absent string",
      count("ch03-matrix-action.tex", "ZZZ-absent-anchor-ZZZ") == 0)
n = count("appH-microscopic-proofs.tex", "Problem~N")
check("A6 POS-CONTROL counter reports multiplicity when present (Problem~N > 1)",
      n > 1)
CRLF = bytes([13, 10])
check("A7 CRLF preserved in both target files",
      CRLF in io.open(ROOT + "ch03-matrix-action.tex", "rb").read()
      and CRLF in io.open(ROOT + "appH-microscopic-proofs.tex", "rb").read())
print("ALL PASS" if all(ok for _, ok in results) else "FAILURES")
sys.exit(0 if all(ok for _, ok in results) else 1)
