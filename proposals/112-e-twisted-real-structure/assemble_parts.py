# Byte-assemble p01..p08 into proposal-r1.md (proposal 112, round 1).
import io, os
here = os.path.dirname(os.path.abspath(__file__))
parts = [f"p{n:02d}.md" for n in range(1, 9)]
out = []
for p in parts:
    with io.open(os.path.join(here, p), "r", encoding="utf-8", newline="") as f:
        out.append(f.read().rstrip("\n"))
text = "\n".join(out) + "\n"
with io.open(os.path.join(here, "proposal-r1.md"), "w", encoding="utf-8", newline="\n") as f:
    f.write(text)
print(f"assembled {len(parts)} parts, {len(text.splitlines())} lines, {len(text.encode('utf-8'))} bytes")
