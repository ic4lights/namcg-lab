#!/usr/bin/env python3
"""Applies the gatekeeper replacement S7 of review-r2.md, read raw from that file, to appH_insert.tex in this proposal folder only.

The old string must occur exactly once in review-r2.md's S7 block, its sha256 must equal the one printed there, and it must occur
exactly once in appH_insert.tex.  Nothing is written unless every check passes, including the expected result hash given in review-r2.md.
A second run is refused, since appH_insert.r2.tex then exists.
"""
import hashlib, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
review = (HERE / "review-r2.md").read_bytes()
ins_path, ins_keep = HERE / "appH_insert.tex", HERE / "appH_insert.r2.tex"
if ins_keep.exists():
    sys.exit("refusing a second run: appH_insert.r2.tex already exists; nothing written")
H = lambda b: hashlib.sha256(b).hexdigest()
if review.count(b"**S7.**") != 1:
    sys.exit("S7 label count is not 1; nothing written")
rest = review[review.index(b"**S7.**"):]
m = re.search(rb"^- Old \(sha256 `([0-9a-f]{64})`\): `(.*)`\r?\n- New \(sha256 `([0-9a-f]{64})`\): `(.*)`\r?$", rest, re.M)
if not m:
    sys.exit("S7 old/new lines not found; nothing written")
h_old, old, h_new, new = m.groups()
if H(old) != h_old.decode() or H(new) != h_new.decode():
    sys.exit(f"S7 printed hashes do not match the strings: old {H(old)}, new {H(new)}; nothing written")
print(f"S7 old {len(old)} bytes sha256 {H(old)} (matches review)")
print(f"S7 new {len(new)} bytes sha256 {H(new)} (matches review)")
ins = ins_path.read_bytes()
R2 = "5d0d4538b69b3a2e6d77659be5b2ae407a90b68cd68b9c0ed3b4d26ec4513aef"
if H(ins) != R2:
    sys.exit(f"insert is not the r2 bytes ({H(ins)}); nothing written")
if ins.count(old) != 1:
    sys.exit(f"S7 old string occurs {ins.count(old)} times in appH_insert.tex; nothing written")
out = ins.replace(old, new)
if any(c > 127 for c in out) or b"\r" in out:
    sys.exit("result is not ASCII with LF; nothing written")
EXP = (10766, "e5562f7670046d486f9855703190b04d78a08994aee9f661b124f930f6d15009")
if (len(out), H(out)) != EXP:
    sys.exit(f"result {len(out)} {H(out)} differs from review-r2 expected {EXP}; nothing written")
ins_keep.write_bytes(ins)
ins_path.write_bytes(out)
print("S7: old string occurred once; net change", len(new) - len(old), "bytes")
print("r2 insert kept as appH_insert.r2.tex:", len(ins), H(ins))
print("r3 insert appH_insert.tex:", len(out), H(out))
print("r3 insert CRLF form:", len(out.replace(b"\n", b"\r\n")), H(out.replace(b"\n", b"\r\n")))
