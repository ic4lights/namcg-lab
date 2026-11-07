import pathlib
p = pathlib.Path('patch_insert_r2.py')
s = p.read_text()
BS = chr(92)
old = 'r"' + BS + '(' + '|' + BS + 'operatorname{Re}'
assert s.count(old) == 1, "old count=%d" % s.count(old)
new = 'r"|' + BS + 'operatorname{Re}'
s = s.replace(old, new)
p.write_text(s)
print("NEW_B merged to single math group per the gatekeeper snippet")
