# gen_insert_097_r2.py - byte surgery insert-r1.tex -> insert-r2.tex (F1 snippet B + F2 wording).
# Proof strategy: b must EQUAL a with exactly two disjoint authorized spans replaced; report diff spans.
# Run from repo root: python -I proposals/097-g-nonbridge-hetero-variance/gen_insert_097_r2.py
import hashlib
D = "proposals/097-g-nonbridge-hetero-variance/"
a = open(D + "insert-r1.tex", "rb").read()
assert len(a) == 5373, "r1 size moved"
assert hashlib.sha256(a).hexdigest().startswith("e3cc6a01"), "r1 hash moved"

F2_OLD = (", the profile " + chr(92) + "(g" + chr(92) + ") is a strictly positive non-constant ").encode("ascii")
F2_NEW = (", the variance profile " + chr(92) + "(g" + chr(92) + ") is a strictly positive non-constant ").encode("ascii")
F1_OLD = b", while every exact identity of the constant-variance conditional law is lost: at"
F1_NEW = b", while the uniform conditional law of the constant-variance case is in general replaced by a tilted one, exactly so at"

for tag, old in [("F2", F2_OLD), ("F1", F1_OLD)]:
    assert a.count(old) == 1, tag + " old not unique"
pos2 = a.find(F2_OLD)
pos1 = a.find(F1_OLD)
assert pos2 + len(F2_OLD) <= pos1, "edit spans overlap or wrong order"
b = a[:pos2] + F2_NEW + a[pos2 + len(F2_OLD):pos1] + F1_NEW + a[pos1 + len(F1_OLD):]
assert b == a.replace(F2_OLD, F2_NEW).replace(F1_OLD, F1_NEW), "two-span reconstruction != global replace"

i = 0
while a[i] == b[i]:
    i += 1
j = 0
while a[len(a) - 1 - j] == b[len(b) - 1 - j]:
    j += 1
assert i + j <= len(a) and b[:i] == a[:i] and b[len(b) - j:] == a[len(a) - j:], "prefix/suffix equality"
assert i >= pos2 and j >= len(a) - (pos1 + len(F1_OLD)), "differing bytes inside authorized spans only"
assert b.count(F1_NEW) == 1 and b.count(F2_NEW) == 1 and b.count(F1_OLD) == 0 and b.count(F2_OLD) == 0

open(D + "insert-r2.tex", "wb").write(b)
print("F2 edit: off %d old %dB new %dB delta %+d" % (pos2, len(F2_OLD), len(F2_NEW), len(F2_NEW) - len(F2_OLD)))
print("F1 edit: off %d old %dB new %dB delta %+d" % (pos1, len(F1_OLD), len(F1_NEW), len(F1_NEW) - len(F1_OLD)))
print("gap between edits %dB byte-equal; total delta %+d" % (pos1 - pos2 - len(F2_OLD), len(b) - len(a)))
print("common-prefix %dB common-suffix %dB" % (i, j))
print("insert-r2 bytes %d sha256 %s" % (len(b), hashlib.sha256(b).hexdigest()))
raise SystemExit(0)
