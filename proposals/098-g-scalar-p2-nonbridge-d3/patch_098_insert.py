# patch_098_insert.py - one-shot wording patch to gen_insert_098.py (block-local D>3 mechanism) + regen. Run from repo root.
D = "proposals/098-g-scalar-p2-nonbridge-d3/"
p = D + "gen_insert_098.py"
s = open(p).read()
old = ("because intersecting the two-angle rotation patch of the second preceding paragraph "
       "with any interior level set of \\\\(" + "P_{2}" + "\\\\) yields an uncountable family of distinct diagonals")
new = ("because, for every \\\\(D\\\\ge3\\\\), intersecting the two-angle rotation patch of the second preceding paragraph "
       "- at \\\\(D>3\\\\) the same two-angle construction taken inside a three-dimensional eigen-coordinate block with "
       "the remaining diagonal entries held fixed, the two-angle Jacobian computation being block-local - "
       "with any interior level set of \\\\(" + "P_{2}" + "\\\\) yields an uncountable family of distinct diagonals")
assert s.count(old) == 1, "old sentence not unique"
s = s.replace(old, new, 1)
open(p, "w", newline="").write(s)
print("SENTENCE-PATCHED")
