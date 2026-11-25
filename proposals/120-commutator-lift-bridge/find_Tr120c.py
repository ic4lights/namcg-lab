# find_Tr120c.py -- locate standalone backslash-Tr macro uses in chapters/
import glob
import io
import re

BS = chr(92)
pat = re.compile(BS + BS + "Tr(?![A-Za-z])")
for f in sorted(glob.glob("chapters/*.tex")):
    t = io.open(f, "r", encoding="utf-8", newline="").read()
    for m in pat.finditer(t):
        s = max(0, m.start() - 80)
        line = t.count("\n", 0, m.start()) + 1
        print(f, "line", line, repr(t[s:m.end() + 60]))
