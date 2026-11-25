# GK127 r2 task 1: byte-diff verification, run python -I from this folder.
import hashlib, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
def rd(name):
    with open(os.path.join(HERE, name), "rb") as f:
        return f.read()
def h12(b): return hashlib.sha1(b).hexdigest()[:12]

rev = rd("review-r1.md").decode("ascii")
# extract the four pinned strings from the review itself (2-space-indented payload lines)
pats = re.findall(r"(?m)^(?:old string \(must occur\nexactly once\)|old string \(must occur exactly once\)):\r?\n  (.+)\r?$", rev)
m_old = re.findall(r"(?m)exactly once\):\r?\n  ([^\r\n]+)\r?\nnew string:\r?\n  ([^\r\n]+)\r?$", rev)
assert len(m_old) == 2, "expected 2 old/new pairs in review, got %d" % len(m_old)
R1_OLD, R1_NEW = (s.encode("ascii") for pair in m_old[:1] for s in pair)
R2_OLD, R2_NEW = (s.encode("ascii") for pair in m_old[1:2] for s in pair)
print("EXTRACTED R1_OLD %dB, R1_NEW %dB, R2_OLD %dB, R2_NEW %dB (from review-r1.md bytes)"
      % (len(R1_OLD), len(R1_NEW), len(R2_OLD), len(R2_NEW)))

def check(tag, r1name, r2name, old, new, r1h, r1s, r2h, r2s, nlines):
    r1 = rd(r1name); r2 = rd(r2name)
    assert h12(r1) == r1h and len(r1) == r1s, "%s r1 file changed: %s/%d" % (tag, h12(r1), len(r1))
    n = r1.count(old)
    assert n == 1, "%s old-string count %d != 1" % (tag, n)
    built = r1.replace(old, new, 1)
    assert built == r2, "%s mechanical build != r2 file (first diff at %d)" % (
        tag, next(i for i in range(len(built)) if i >= len(r2) or built[i] != r2[i]))
    assert h12(r2) == r2h and len(r2) == r2s, "%s r2 pin: %s/%d" % (tag, h12(r2), len(r2))
    # reverse: r2 with new->old reproduces r1 bytes exactly -> single diff region proven
    assert r2.count(new) == 1, "%s new-string count in r2 != 1" % tag
    assert r2.replace(new, old, 1) == r1, "%s reverse replace != r1 bytes" % tag
    # single contiguous differing region (independent diff view)
    pre = os.path.commonprefix([r1, r2]) if False else None
    i = 0
    while i < min(len(r1), len(r2)) and r1[i] == r2[i]: i += 1
    j = 0
    while j < min(len(r1), len(r2)) - i and r1[len(r1)-1-j] == r2[len(r2)-1-j]: j += 1
    print("%s: diff region r1[%d:%d] (%dB) -> r2[%d:%d] (%dB); delta %+d B"
          % (tag, i, len(r1)-j, len(r1)-j-i, i, len(r2)-j, len(r2)-j-i, len(r2)-len(r1)))
    # the trimmed diff region must be exactly the pinned span minus its own
    # shared prefix/suffix (old and new share the lead-in "to " / tail-in text)
    x = 0
    while x < min(len(old), len(new)) and old[x] == new[x]: x += 1
    y = 0
    while y < min(len(old), len(new)) - x and old[len(old)-1-y] == new[len(new)-1-y]: y += 1
    assert r1[i:len(r1)-j] == old[x:len(old)-y] and r2[i:len(r2)-j] == new[x:len(new)-y], \
        "%s diff region not the pinned span" % tag
    # hygiene
    assert all(b < 128 for b in r2), "%s non-ASCII" % tag
    assert b"\r" not in r2, "%s CR byte" % tag
    assert r2.endswith(b"\n"), "%s no trailing LF" % tag
    assert r2.count(b"\n") == nlines, "%s line count %d != %d" % (tag, r2.count(b"\n"), nlines)
    print("%s: FORWARD build==r2 FILE byte-identical; REVERSE==r1; ONLY span is pinned replacement; "
          "ASCII yes, CR 0, trailing LF yes, lines %d; r1 unchanged (%s/%d)"
          % (tag, nlines, h12(r1), len(r1)))

check("R1/P1", "payload-P1.txt", "payload-P1-r2.txt", R1_OLD, R1_NEW,
      "8df7a7f42a97", 871, "6dd693e2cf0b", 1010, 1)
check("R2/P2", "payload-P2.txt", "payload-P2-r2.txt", R2_OLD, R2_NEW,
      "e30a1cd68ed6", 3043, "73aca8c862ec", 3050, 2)
print("TASK1: PASS")
