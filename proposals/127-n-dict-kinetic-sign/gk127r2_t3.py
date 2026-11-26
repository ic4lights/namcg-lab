# GK127 r2 task 3: independent POST recompute on external copies. python -I.
import hashlib, os, sys
ROOT = r"C:\Users\redgi\Projects\namcg-lab@gpu"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.environ["TEMP"], "gk127r2_post")
os.makedirs(OUT, exist_ok=True)
def h12(b): return hashlib.sha1(b).hexdigest()[:12]
def rd(p):
    with open(p, "rb") as f: return f.read()

ch03 = rd(os.path.join(ROOT, "chapters", "ch03-matrix-action.tex"))
appH = rd(os.path.join(ROOT, "chapters", "appH-microscopic-proofs.tex"))
assert h12(ch03) == "78afd166ccdc" and len(ch03) == 36967, "ch03 live rehash FAIL"
assert h12(appH) == "123108d4a947" and len(appH) == 880023, "appH live rehash FAIL"
print("live rehash: ch03 %s/%d OK, appH %s/%d OK" % (h12(ch03), len(ch03), h12(appH), len(appH)))

CRLF = b"\r\n"
A_CH03 = b"  \(\LUV\) remains the cutoff of the derivative expansion." + CRLF
A_APPH = b"\paragraph{The named completion class and the remainder bound.}"
A_SENT = b"this is a matching condition, not an established result."
for name, data, a, cnt in (("ch03-LUV-line", ch03, A_CH03, 1),
                           ("appH-head", appH, A_APPH, 1),
                           ("ch03-anchor-sentence", ch03, A_SENT, 1)):
    n = data.count(a)
    print("anchor %-24s count=%d %s" % (name, n, "OK" if n == cnt else "FAIL"))
    assert n == cnt

def splice(data, anchor, payload):
    pc = payload.replace(b"\n", CRLF)
    assert len(pc) == len(payload) + payload.count(b"\n")
    assert data.count(anchor) == 1
    return data.replace(anchor, pc + anchor, 1), pc

def report(tag, pre, post, pc, lines_pin, bytes_pin, oldsha):
    i = post.find(pc)
    assert i != -1 and post.count(pc) == 1, tag + ": payload CRLF block not unique/present"
    assert post[:i] + post[i+len(pc):] == pre, tag + ": not pure insertion"
    assert post.count(b"\n") == post.count(CRLF), tag + ": not pure CRLF"
    lines = len(post.splitlines())
    ok = (len(post) == bytes_pin and lines == lines_pin)
    print("%s POST %d B / %d lines (pin %d/%d) sha1_12=%s  %s" %
          (tag, len(post), lines, bytes_pin, lines_pin, h12(post), "OK" if ok else "FAIL"))
    assert ok
    if oldsha:
        assert h12(post) == oldsha, tag + ": recipe self-test sha mismatch %s" % h12(post)
        print("%s recipe self-test reproduces inherited r1 POST sha1_12 %s" % (tag, oldsha))
    return post

# self-test of recipe/layout on frozen r1 payloads (pins from repro pass R4/R5)
p1r1 = rd(os.path.join(HERE, "payload-P1.txt")); p2r1 = rd(os.path.join(HERE, "payload-P2.txt"))
assert h12(p1r1) == "8df7a7f42a97" and h12(p2r1) == "e30a1cd68ed6"
s3, _ = splice(ch03, A_CH03, p1r1); report("SELFTEST ch03", ch03, s3, p1r1.replace(b"\n", CRLF), 917, 37839, "9031f6cf469c")
sH, _ = splice(appH, A_APPH, p2r1); report("SELFTEST appH", appH, sH, p2r1.replace(b"\n", CRLF), 4146, 883068, "639e0fce81a2")

# r2 splices
p1 = rd(os.path.join(HERE, "payload-P1-r2.txt")); p2 = rd(os.path.join(HERE, "payload-P2-r2.txt"))
assert h12(p1) == "6dd693e2cf0b" and len(p1) == 1010
assert h12(p2) == "73aca8c862ec" and len(p2) == 3050
pc1, pc2 = p1.replace(b"\n", CRLF), p2.replace(b"\n", CRLF)
post3, _ = splice(ch03, A_CH03, p1); post3 = report("ch03", ch03, post3, pc1, 917, 37978, None)
postH, _ = splice(appH, A_APPH, p2); postH = report("appH", appH, postH, pc2, 4146, 883075, None)
# join sanity: payload between anchor sentence line and LUV line; before appH head
j = post3.find(pc1); k = post3.find(A_SENT)
assert k != -1 and post3.rfind(A_SENT, 0, j) == k, "ch03 join: payload not after anchor sentence"
assert post3[j+len(pc1):].startswith(A_CH03), "ch03 join: LUV line not directly after payload"
jH = postH.find(pc2)
assert postH[jH+len(pc2):].startswith(A_APPH), "appH join: head not directly after payload"
assert postH[:jH].endswith(CRLF*2), "appH join: blank line before payload lost"
print("joins: ch03 payload after anchor sentence, before LUV line; appH blank line kept, head follows payload -- OK")
with open(os.path.join(OUT, "ch03-spliced.tex"), "wb") as f: f.write(post3)
with open(os.path.join(OUT, "appH-spliced.tex"), "wb") as f: f.write(postH)
print("WROTE %s ch03 %s appH %s" % (OUT, h12(post3), h12(postH)))
print("TASK3: PASS  ch03 POST %d B / %d / %s   appH POST %d B / %d / %s"
      % (len(post3), len(post3.splitlines()), h12(post3), len(postH), len(postH.splitlines()), h12(postH)))
