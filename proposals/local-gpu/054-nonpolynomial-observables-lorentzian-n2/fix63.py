import pathlib
p = pathlib.Path('patch_insert_r2.py')
s = p.read_text()
BS = chr(92)
core = ('operatorname{Im}(k' + BS*2 + 'cdot' + BS*2 + 'hat' + BS*2 +
        'rho)|>|' + BS*2 + 'operatorname{Re}(k' + BS*2 + 'cdot' + BS*2 +
        'hat' + BS*2 + 'rho)|",')
cur = ' ' * 17 + 'rb"|' + BS*2 + core
new = ' ' * 17 + 'b"|' + BS*2 + core
assert s.count(cur) == 1, "cur count=%d" % s.count(cur)
s = s.replace(cur, new)
p.write_text(s)
print("line 63 rewritten: non-raw b\" literal, two backslashes in source = one in value")
