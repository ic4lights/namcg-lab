"""060: two precision edits, raw strings."""
p = 'appH_insert.tex'
s = open(p, encoding='utf-8').read()
reps = [
    (r"the solutions at finite \(N\) are therefore those of the compact form, with",
     r"the non-zero solutions at finite \(N\) are therefore those of compact forms, with"),
    (r"which in the coordinates \(y^\mu\) is a constant times \(\mathrm d^4y/|m|\).",
     r"which in the coordinates \(y^\mu\) is a constant times \(\mathrm d^4y/|m|\) on each of the parts \(m>0\) and \(m<0\)."),
    (r"for the Euclidean contraction \(t'=t\) gives the maximum, and for",
     r"for the Euclidean contraction the maximum is at \(t'=t\), and for"),
]
for a, b in reps:
    assert s.count(a) == 1, a
    s = s.replace(a, b)
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print(len(s.encode('utf-8')))
