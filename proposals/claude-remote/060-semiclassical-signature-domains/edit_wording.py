"""060: wording edit ('do not reach' -> 'do not apply to'), written with raw strings."""
p = 'appH_insert.tex'
s = open(p, encoding='utf-8').read()
a = r"with \(\epsilon\to0\) first, therefore do not reach these backgrounds,"
b = r"with \(\epsilon\to0\) first, therefore do not apply to these backgrounds,"
assert s.count(a) == 1
s = s.replace(a, b)
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print(len(s.encode('utf-8')))
