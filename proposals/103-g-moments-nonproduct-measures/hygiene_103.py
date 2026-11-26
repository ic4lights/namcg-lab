# hygiene_103.py -- hygiene gate for insert-r1.tex (proposal 103, round 1).
# Adapted from proposals/102-g-profile-selection-output/hygiene_102.py: retargeted to
# insert-r1.tex; FIX H102/H102b logic kept (lenient appH decode; the open-math macro
# \( is checked exactly as written, with no trailing space). Section 7 is automated:
# EVERY backslash macro token used by the insert must occur at least once in the live
# appH bytes. Run from repo root:
#   python -I proposals/103-g-moments-nonproduct-measures/hygiene_103.py
# Exits nonzero on any failure.
import hashlib
import os
import re
import sys

FOLDER = os.path.dirname(os.path.abspath(__file__))
INSERT = os.path.join(FOLDER, "insert-r1.tex")
APPH = os.path.join(FOLDER, "..", "..", "chapters", "appH-microscopic-proofs.tex")
CHAPTERS = os.path.join(FOLDER, "..", "..", "chapters")

fails = []

def fail(msg):
    fails.append(msg)
    print("FAIL:", msg)

def sha8(b):
    return hashlib.sha256(b).hexdigest()[:8]

data = open(INSERT, "rb").read()
print("insert-r1.tex bytes =", len(data))
print("insert-r1.tex sha8  =", sha8(data))

# 1. BOM
if data.startswith(b"\xef\xbb\xbf"):
    fail("BOM present")
else:
    print("BOM: none")

# 2. CRLF-only / bare LF; single CRLF-terminated paragraph line
crlf = data.count(b"\r\n")
lf = data.count(b"\n")
bare_lf = lf - crlf
print("CRLF =", crlf, "bareLF =", bare_lf)
if bare_lf != 0:
    fail("bare LF bytes present")
if not data.endswith(b"\r\n"):
    fail("file does not end with CRLF")
if crlf != 1:
    fail("expected exactly one CRLF-terminated paragraph line")

# 3. control bytes outside TAB/LF/CR
ctl = sorted({b for b in data if b < 32 and b not in (9, 10, 13)})
print("control bytes outside TAB/LF/CR:", ctl if ctl else "none")
if ctl:
    fail("control bytes present")

# 4. ASCII-only
nonascii = sorted({b for b in data if b > 127})
print("non-ASCII bytes:", nonascii if nonascii else "none (ASCII-only)")
if nonascii:
    fail("non-ASCII bytes present (G-block neighbours around the anchor are ASCII-only)")

# 5. balanced braces/brackets (no verbatim environments in this file; none in appH either)
if re.search(rb"\\begin\{verbatim\}", data):
    fail("insert contains a verbatim environment; brace counter assumes none")
for op, cl, name in ((b"{", b"}", "braces"), (b"[", b"]", "brackets")):
    o, c = data.count(op), data.count(cl)
    print(name, "open =", o, "close =", c)
    if o != c:
        fail("unbalanced " + name)

# 6. \ref / \label inventory, grep-checked across chapters/
txt = data.decode("ascii")
labels = re.findall(r"\\label\{([^}]*)\}", txt)
refs = re.findall(r"\\ref\{([^}]*)\}", txt)
eqs = re.findall(r"\\eqref\{([^}]*)\}", txt)
print("\\label found:", labels if labels else "none")
print("\\ref found:", refs if refs else "none")
print("\\eqref found:", eqs if eqs else "none")
if labels or refs or eqs:
    alltex = []
    for root, _dirs, files in os.walk(CHAPTERS):
        for f in files:
            if f.endswith(".tex"):
                alltex.append(os.path.join(root, f))
    for want in sorted(set(refs) | set(eqs)):
        cnt = sum(len(re.findall(r"\\label\{" + re.escape(want) + r"\}", open(p, encoding="utf-8", errors="replace").read())) for p in alltex)
        print("grep \\label{%s} across chapters/: %d occurrence(s)" % (want, cnt))
        if cnt != 1:
            fail("\\ref{%s} resolves %d times (need exactly 1)" % (want, cnt))
    for lab in set(labels):
        cnt = sum(len(re.findall(r"\\label\{" + re.escape(lab) + r"\}", open(p, encoding="utf-8", errors="replace").read())) for p in alltex)
        print("grep \\label{%s} across chapters/ (incl. insert file itself): %d" % (lab, cnt))
        if cnt != 1:
            fail("duplicate or missing \\label{%s}" % lab)
else:
    print("no \\ref/\\label/\\eqref used: nothing to resolve (grep not required)")

# 7. every backslash macro used by the insert must appear elsewhere in appH.
# FIX H102b (carried from hygiene_102.py): appH contains non-ASCII UTF-8 bytes
# (0xe2 at offset 711159, an integrated character), so decoding appH as ascii
# crashes. Lenient decode; the ASCII check that matters is on the insert
# (section 4), which passes ASCII-only.
# FIX H102 (carried from hygiene_102.py): single-character macros must be
# checked exactly as written; the loop below iterates the tokens as extracted,
# so \( is checked as \( with no trailing space.
apph = open(APPH, "rb").read().decode("utf-8", errors="replace")
word = sorted(set(re.findall(r"\\[a-zA-Z]+", txt)))
sym = sorted(set(re.findall(r"\\[^a-zA-Z\s{}\\]", txt)))
missing = []
for key in word:
    n = apph.count(key)
    print("appH count of %r = %d" % (key, n))
    if n == 0:
        missing.append(key)
for key in sym:
    n = apph.count(key)
    print("appH count of %r = %d" % (key, n))
    if n == 0:
        missing.append(key)
if missing:
    fail("macro/convention not found elsewhere in appH: %s" % missing)

# 8. closing idiom present exactly once (single scoped status sentence)
idiom = "they close nothing in Problem~G."
n = txt.count(idiom)
print("closing idiom %r count = %d" % (idiom, n))
if n != 1:
    fail("expected exactly one closing scoped status sentence")

# 9. insertion-robustness: no ordinal paragraph references in the insert
ord_hits = re.findall(r"(first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth) preceding paragraph", txt)
print("ordinal 'Nth preceding paragraph' references in insert:", ord_hits if ord_hits else "none")
if ord_hits:
    fail("insert uses ordinal paragraph references; use title-fragment names")

print("HYGIENE PASS" if not fails else "HYGIENE FAIL (%d)" % len(fails))
sys.exit(1 if fails else 0)
