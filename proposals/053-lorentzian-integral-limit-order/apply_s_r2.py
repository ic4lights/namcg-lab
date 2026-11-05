#!/usr/bin/env python3
"""Applies the gatekeeper replacements S1-S6 of review-r1.md, read raw from that file, inside this proposal folder only.

S1-S5 go to appH_insert.tex.  S6 goes to the NEW bytes of apply_check.py.  Each old string must occur exactly once, in the order applied.
Nothing is written unless every check passes.  A second run is refused, since appH_insert.r1.tex then exists.
apply_check.py keeps its r1 bytes as apply_check.r1.py; the CRLF correction of its bib step is a separate edit of apply_check.py, recorded in the proposal.
"""
import hashlib, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
review = (HERE / "review-r1.md").read_bytes()
ins_path, ins_keep = HERE / "appH_insert.tex", HERE / "appH_insert.r1.tex"
chk_path, chk_keep = HERE / "apply_check.py", HERE / "apply_check.r1.py"
if ins_keep.exists() or chk_keep.exists():
    sys.exit("refusing a second run: a kept r1 copy already exists; nothing written")

pairs = {}
for k in range(1, 7):
    label = b"**S%d" % k
    if review.count(label) != 1:
        sys.exit(f"S{k}: label count {review.count(label)}; nothing written")
    rest = review[review.index(label):]
    m = re.search(rb"^- Old: `(.*)`\r?\n- New: `(.*)`\r?$", rest, re.M)
    if not m:
        sys.exit(f"S{k}: old/new lines not found; nothing written")
    pairs[k] = m.group(1), m.group(2)
    print(f"S{k}: old {len(m.group(1))} bytes sha256 {hashlib.sha256(m.group(1)).hexdigest()[:16]}, new {len(m.group(2))} bytes sha256 {hashlib.sha256(m.group(2)).hexdigest()[:16]}")

ins = ins_path.read_bytes()
out = ins
for k in range(1, 6):
    old, new = pairs[k]
    if ins.count(old) != 1 or out.count(old) != 1:
        sys.exit(f"S{k}: old string count {ins.count(old)} in r1, {out.count(old)} after earlier edits; nothing written")
    out = out.replace(old, new)
    print(f"S{k}: old string occurs once; net change {len(new) - len(old)} bytes")
if any(c > 127 for c in out) or b"\r" in out:
    sys.exit("insert is not ASCII with LF; nothing written")

src = chk_path.read_bytes()
def load_new(b):
    g = {}
    tree_end = b.index(b"def main():")
    exec(compile(b[:tree_end], "apply_check-head", "exec"), {"__file__": str(chk_path), "__name__": "x"}, g)
    return g["OLD"], g["NEW"]
old6, new6 = pairs[6]
OLD_r1, NEW_r1 = load_new(src)
if NEW_r1.count(old6) != 1:
    sys.exit(f"S6: count {NEW_r1.count(old6)} in the evaluated NEW; nothing written")
suffix = b"its polynomial moments"
if not (old6.endswith(b" " + suffix) and new6.endswith(b" " + suffix)):
    sys.exit("S6: common suffix not as expected; nothing written")
# In the source of apply_check.py the string is split into two literals just before the suffix.
p_old, p_new = old6[:-len(suffix)], new6[:-len(suffix)]
if src.count(p_old) != 1:
    sys.exit(f"S6: prefix count {src.count(p_old)} in apply_check.py source; nothing written")
src2 = src.replace(p_old, p_new)
OLD_2, NEW_2 = load_new(src2)
if OLD_2 != OLD_r1 or NEW_2 != NEW_r1.replace(old6, new6) or NEW_2.count(new6) != 1:
    sys.exit("S6: evaluated NEW is not the r1 NEW with S6 applied; nothing written")
print("S6: old string occurs once in the evaluated NEW; OLD unchanged; evaluated NEW equals r1 NEW with S6 applied")

ins_keep.write_bytes(ins)
ins_path.write_bytes(out)
chk_keep.write_bytes(src)
chk_path.write_bytes(src2)
print("r1 insert", len(ins), hashlib.sha256(ins).hexdigest())
print("r2 insert", len(out), hashlib.sha256(out).hexdigest())
print("OLD", len(OLD_2), hashlib.sha256(OLD_2).hexdigest())
print("NEW", len(NEW_2), hashlib.sha256(NEW_2).hexdigest())
