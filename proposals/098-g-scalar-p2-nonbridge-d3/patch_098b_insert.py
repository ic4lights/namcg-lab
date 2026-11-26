# patch_098b_insert.py - precision fixes to gen_insert_098.py wording. Run from repo root.
# (a) level-set scope: "any interior level set" -> a level set in the interior of the patch image;
# (b) Vandermonde attribution: "those paragraphs" -> the first preceding paragraph (097 records it);
# (c) D=2 profile-class attribution for the "settles at every D>=2" sentence (095 + 097-D=2).
D = "proposals/098-g-scalar-p2-nonbridge-d3/"
p = D + "gen_insert_098.py"
s = open(p).read()

o1 = "with any interior level set of \\\\(" + "P_{2}" + "\\\\) yields an uncountable family of distinct diagonals"
n1 = "with a level set of \\\\(" + "P_{2}" + "\\\\) in the interior of its image range under the patch yields an uncountable family of distinct diagonals"
assert s.count(o1) == 1, "o1"
s = s.replace(o1, n1, 1)

o2 = "the scalar-spectrum collision set still carries no mass, the joint eigenvalue density being absolutely continuous on the ordered chamber with the Vandermonde weight recorded in those paragraphs"
n2 = "the eigenvalue-collision set still carries no mass, the joint eigenvalue density being absolutely continuous on the ordered chamber with the Vandermonde weight recorded in the first preceding paragraph"
assert s.count(o2) == 1, "o2"
s = s.replace(o2, n2, 1)

o3 = "combined with the \\\\(D=2\\\\) nonexistence of the third preceding paragraph this settles the single quadratic statistic at every dimension \\\\(D\\\\ge2\\\\) in both named classes"
n3 = "combined with the \\\\(D=2\\\\) nonexistence of the third preceding paragraph and the \\\\(D=2\\\\) instance of the tuple nonexistence of the first preceding paragraph, this settles the single quadratic statistic at every dimension \\\\(D\\\\ge2\\\\) in both named classes"
assert s.count(o3) == 1, "o3"
s = s.replace(o3, n3, 1)

open(p, "w", newline="").write(s)
print("PRECISION-PATCHED")
raise SystemExit(0)
