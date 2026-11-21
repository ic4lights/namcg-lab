#!/usr/bin/env python3
"""Proposal 055 r2: apply the four gatekeeper Corrected-snippet substitutions (review-r1.md F1-F4)
to the r1 insert, exactly, as four OLD->NEW byte spans.

Input : appH_insert.r1.tex (pinned 2907 B, sha256 c7b5831e0fa10255e9b37e3d8a206b779ebf63dee97f21b14a570d42cb04923d)
Output: appH_insert.tex    (LF form; the r2 insert; everything else byte-identical to r1)

Guards: each OLD occurs exactly once in r1; after substitution each NEW occurs exactly once and
each OLD occurs zero times; the output contains no other change (reconstruct test); re-running
regenerates identical bytes (idempotence by pin + construction). Byte literals use raw single
backslashes (rb"..."): the 054-style double-backslash-in-raw-string bug is avoided.
"""
import hashlib

R1 = "appH_insert.r1.tex"
R2 = "appH_insert.tex"
R1_SIZE, R1_SHA = 2907, "c7b5831e0fa10255e9b37e3d8a206b779ebf63dee97f21b14a570d42cb04923d"

PAIRS = [
    (rb"\rho_X^2=\sum_{a=1}^{2}{(k^\mu A^a_\mu)}^2",
     rb"\rho_X^2=\sum_{a=1}^{3}{(k^\mu A^a_\mu)}^2"),
    (rb"it stays between \(0.75\) and \(2.2\)",
     rb"it stays between \(0.74\) and \(1.78\)"),
    (rb"to a constant of order \(\mathrm e^{{(r^0)}^2\sin(3\pi u/4-\pi/4)/(8|\gamma|)}\) that diverges as \(\gamma\to0^-\).",
     rb"to a constant of order \(\mathrm e^{{(r^0)}^2\sin(3\pi u/4-\pi/4)/(8|\gamma|)}\), which diverges as \(\gamma\to0^-\) when \(3\pi u/4-\pi/4>0\) and decays when it is negative."),
    (rb"the corner branch growth being phase-space suppressed near the soft corner by Vandermonde and measure powers.",
     rb"consistent with phase-space suppression of the corner branch growth near the soft corner by Vandermonde and measure powers, though no domination lemma is claimed."),
]

def sha(b): return hashlib.sha256(b).hexdigest()

def main():
    b = open(R1, "rb").read()
    assert len(b) == R1_SIZE and sha(b) == R1_SHA, "r1 pin mismatch"
    x = b
    for i, (old, new) in enumerate(PAIRS, 1):
        c = x.count(old)
        assert c == 1, f"F{i}: OLD count {c} != 1"
        x = x.replace(old, new)
    for i, (old, new) in enumerate(PAIRS, 1):
        assert x.count(new) == 1, f"F{i}: NEW count != 1"
        assert x.count(old) == 0, f"F{i}: OLD still present"
    # reconstruction test: applying the same spans to r1 in order is the only edit
    y = b
    for old, new in PAIRS:
        y = y.replace(old, new)
    assert x == y
    # length bookkeeping
    dl = sum(len(n) - len(o) for o, n in PAIRS)
    assert len(x) == len(b) + dl, "size accounting mismatch"
    open(R2, "wb").write(x)
    z = open(R2, "rb").read()
    assert z == x
    crlf = x.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
    print(f"r1: {len(b)} B sha {sha(b)}")
    print(f"r2 LF:   {len(x)} B sha {sha(x)}")
    print(f"r2 CRLF: {len(crlf)} B sha {sha(crlf)}")
    print(f"size delta per substitution: {[len(n)-len(o) for o, n in PAIRS]}, total {dl}")
    print("all four OLD spans removed, all four NEW spans present once; idempotent regeneration OK")

main()
