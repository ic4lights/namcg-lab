#!/usr/bin/env python3
"""Proposal 053, round 3: apply gatekeeper replacement S7 from review-r2.md to the insert.

Reads the S7 Old/New strings from review-r2.md (the two code spans in the **S7.** block,
each on its own line: "- Old (sha256 `...`): `...`" and "- New (sha256 `...`): `...`"),
verifies their sha256 against the values printed there, verifies the r2 insert bytes,
applies S7 to appH_insert.r2.tex and writes appH_insert.tex in LF form.
Refuses if appH_insert.r2.tex is not the expected r2 bytes, if S7 is already applied,
and if any expected hash mismatches. Writes only appH_insert.tex in this folder.

r3 fix: the r3 first version of this script anchored the New capture with a trailing
backtick-plus-period (`` `\\. ``), but review-r2.md ends the New code span with a period
INSIDE the span and the closing backtick followed by a newline, so the non-greedy
capture over-ran the span; the sha assertion then failed and nothing was written.
The pattern now ends each code-span capture at the closing backtick followed by a
newline (read_text translates CRLF to LF).
"""
import pathlib, re, hashlib, sys
HERE = pathlib.Path(__file__).resolve().parent
CR, LF = b"\r", b"\n"
def lf(b): return b.replace(CR + LF, LF)
def crlf(b): return lf(b).replace(LF, CR + LF)
def sha(b): return hashlib.sha256(b).hexdigest()

R2_EXPECT = (10645, "5d0d4538b69b3a2e6d77659be5b2ae407a90b68cd68b9c0ed3b4d26ec4513aef")
S7_OLD_SHA = "5c217b675886d1ff5cd0a1f81b14d8308e61fde336bbea8c14c246ac49d6ec76"
S7_NEW_SHA = "4dd695f93cada41514bb4c086d142717da4d1f8e8061e62401370f9f7c6aef2c"
OUT_EXPECT = {
    "LF":   (10766, "e5562f7670046d486f9855703190b04d78a08994aee9f661b124f930f6d15009"),
    "CRLF": (10783, "bab65e9595a2b2c2f7dad231e1427cfeae0de0ff0ac4e262b33dd8d95b504285"),
}

def main():
    rev = (HERE / "review-r2.md").read_text(encoding="utf-8")
    mo = re.search(r"- Old \(sha256 `([0-9a-f]{64})`\): `(.*?)`\r?\n", rev)
    mn = re.search(r"- New \(sha256 `([0-9a-f]{64})`\): `(.*?)`\r?\n", rev)
    if not mo or not mn:
        sys.exit("S7 Old/New lines not found in review-r2.md")
    old_sha, old, new_sha, new = mo.group(1), mo.group(2), mn.group(1), mn.group(2)
    ob, nb = old.encode(), new.encode()
    assert sha(ob) == old_sha == S7_OLD_SHA, "S7 old sha mismatch: " + sha(ob)
    assert sha(nb) == new_sha == S7_NEW_SHA, "S7 new sha mismatch: " + sha(nb)
    assert len(ob) == 195 and len(nb) == 316, "S7 string sizes wrong: %d %d" % (len(ob), len(nb))
    print("S7 strings parsed from review-r2.md; shas and sizes match:", old_sha, new_sha)

    r2 = lf((HERE / "appH_insert.r2.tex").read_bytes())
    if (len(r2), sha(r2)) != R2_EXPECT:
        sys.exit("appH_insert.r2.tex is not the r2 bytes: %d %s" % (len(r2), sha(r2)))
    print("r2 insert bytes confirmed:", len(r2), sha(r2))

    cur = lf((HERE / "appH_insert.tex").read_bytes())
    if nb in cur:
        sys.exit("S7 already applied; refusing a second run")
    if cur != r2:
        sys.exit("appH_insert.tex differs from appH_insert.r2.tex before S7; refusing")
    assert r2.count(ob) == 1, "S7 old string not exactly once in r2 insert"
    out = r2.replace(ob, nb)
    assert all(c < 128 for c in out), "non-ASCII byte"
    if (len(out), sha(out)) != OUT_EXPECT["LF"]:
        sys.exit("output does not match the gatekeeper's expected LF insert: %d %s" % (len(out), sha(out)))
    if (len(crlf(out)), sha(crlf(out))) != OUT_EXPECT["CRLF"]:
        sys.exit("CRLF form does not match the gatekeeper's expectation")
    (HERE / "appH_insert.tex").write_bytes(out)
    print("applied S7; appH_insert.tex written LF:", len(out), sha(out))
    print("CRLF form:", len(crlf(out)), sha(crlf(out)))

main()
