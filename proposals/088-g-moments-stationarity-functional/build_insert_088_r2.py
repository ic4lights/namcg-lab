# build_insert_088_r2.py -- emits insert-r2.tex from the FROZEN insert-r1.tex skeleton
# by splicing the gatekeeper-byte-extracted corrected block-2 sentences and the
# gatekeeper-byte-extracted F2 dichotomy clause. ONE content line + terminal CRLF.
# Byte sources: scratch/r2fix/block2_corrected.txt, scratch/r2fix/clause_f2.txt
# (extracted from review-r1.md by scratch/r2fix/extract_r2.py -- no retyping).
# Run: python -I build_insert_088_r2.py
import sys
SRC = "proposals/088-g-moments-stationarity-functional/insert-r1.tex"
OUT = "proposals/088-g-moments-stationarity-functional/insert-r2.tex"
B2F = "scratch/r2fix/block2_corrected.txt"
CLF = "scratch/r2fix/clause_f2.txt"
ok = True
def chk(name, cond, extra=""):
    global ok
    print("%-46s %s %s" % (name, "OK" if cond else "FAIL", extra)); ok = ok and cond

r1 = open(SRC, "rb").read().decode("utf-8")
assert r1.endswith("\r\n"); r1 = r1[:-2]
b2 = open(B2F, "rb").read().decode("utf-8")
# F3 fold-in: gatekeeper fenced snippet retains "the minimal case" (verified in review-r1.md;
# their F3 text requires "minimal recorded case"). Single-count byte substitution, asserted:
assert b2.count("is the minimal case;") == 1, "F3 fold anchor count != 1"
b2 = b2.replace("is the minimal case;", "is the minimal recorded case;", 1)
cl = open(CLF, "rb").read().decode("utf-8")

# --- locate old block 2 by boundary markers (never retyped) ---
s0 = r1.index("This stationarity is rigid across the decoupling cone:")
s1 = r1.index("profile selector.", s0) + len("profile selector.")
old_block2 = r1[s0:s1]
chk("old block2 starts with rigid sentence", old_block2.startswith("This stationarity is rigid"))
chk("old block2 contains r1 false claim", "strictly monotone \(C^{1}\) reparametrisation the stationary locus is unchanged" in old_block2)
chk("old block2 unique", r1.count(old_block2) == 1)
# --- locate old block-3 clause by boundary markers (never retyped) ---
c0 = r1.index("while a symmetric non-convex term")
c1 = r1.index("further selection input", c0) + len("further selection input")
old_clause = r1[c0:c1]
chk("old clause unique", r1.count(old_clause) == 1)
# --- source-byte asserts ---
chk("block2 src starts 'This stationarity is rigid'", b2.startswith("This stationarity is rigid"))
chk("block2 src ends 'profile selector.'", b2.endswith("profile selector."))
chk("F3 fold applied: block2 has 'minimal recorded case'", b2.count("minimal recorded case") == 1)
chk("F2 clause src starts 'while a relabelling-symmetric'", cl.startswith("while a relabelling-symmetric"))
chk("F2 clause src has dichotomy 'either has the uniform profile itself'", "either has the uniform profile itself among its minimisers" in cl)

content = r1.replace(old_block2, b2, 1).replace(old_clause, cl, 1)
# --- byte-equality of spliced sources in the built content ---
chk("built contains block2 bytes verbatim", b2 in content)
chk("built contains F2 clause bytes verbatim", cl in content)
chk("false claim removed", "strictly monotone \(C^{1}\) reparametrisation the stationary locus is unchanged" not in content)
chk("old clause removed", "while a symmetric non-convex term" not in content)
chk("'minimal case;' removed", "minimal case;" not in content)
# --- r1 hygiene guards recomputed on r2 content ---
chk("no banned tokens", all(x not in content for x in ["$", "[", "]", "\cite", "\ref", "\eqref", "\label"]))
for f in ["status", "priority", "completion", "open", "critical", "programme", "derived"]:
    chk("word absent: " + f, f not in content.lower())
chk("exactly one \emph{ header", content.count("\emph{") == 1)
chk("brace balance", content.count("{") == content.count("}"))
chk("paren balance", content.count("(") == content.count(")"))
chk("ends with close idiom", content.endswith("they close nothing in Problem~G."))
import re
nums = sorted(set(re.findall(r"(?<![A-Za-z_])\d+", content)))
chk("numerals within allowlist {0,1,2}", all(n in {"0", "1", "2"} for n in nums), str(nums))
chk("no control chars", all(ord(c) >= 32 for c in content))
chk("single line", "\n" not in content)
if not ok:
    print("BUILD FAIL"); sys.exit(1)
out = (content + "\r\n").encode("utf-8")
open(OUT, "wb").write(out)
print("delta bytes: r1 content=%d r2 content=%d (block2 %+d, clause %+d)"
      % (len(r1), len(content), len(b2)-len(old_block2), len(cl)-len(old_clause)))
print("insert-r2.tex bytes:", len(out), "| line chars:", len(content))
