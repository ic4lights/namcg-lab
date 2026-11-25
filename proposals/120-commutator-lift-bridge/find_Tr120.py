# find_Tr120.py -- locate standalone \Tr macro uses in chapters/ (context lines)
import glob
import io
import re

pat = re.compile(r"\\Tr(?![A-Za-z])")
for f in sorted(glob.glob("chapters/*.tex")):
    t = io.open(f, "r", encoding="utf-8", newline="").read()
    for m in pat.finditer(t):
        s = max(0, m.start() - 80)
        line = t.count("\n", 0, m.start()) + 1
        print(f, "line", line, repr(t[s:m.end() + 60]))
