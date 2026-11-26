import hashlib, shutil
def pin(f):
    b = open(f, 'rb').read(); return hashlib.sha1(b).hexdigest()[:12], len(b)
shutil.copyfile('verify_r120.py', 'verify_r120-preR5.py')
shutil.copyfile('cert-r120p.py', 'cert-r120p-preR5.py')
print('preR5 copies (share old hashes)', pin('verify_r120-preR5.py'), pin('cert-r120p-preR5.py'))
v = open('verify_r120.py', 'rb').read()
vr = [
    (b'"P1 payload bytes=5138 sha1[:12]=343226e27ebf"',
     b'"P1 payload bytes=5287 sha1[:12]=a5aa77dc90a3"'),
    (b'len(pay) == 5138 and hashlib.sha1(pay).hexdigest()[:12] == "343226e27ebf"',
     b'len(pay) == 5287 and hashlib.sha1(pay).hexdigest()[:12] == "a5aa77dc90a3"'),
    (b'"P8 payload size 5138 <= 5191 (chain-119 payload size ceiling)"',
     b'"P8 payload size 5287 <= 5340 (chain-119 ceiling re-pinned R5, +53 margin kept)"'),
    (b'len(pay) <= 5191', b'len(pay) <= 5340'),
]
for old, new in vr:
    assert v.count(old) == 1, ('verify', old[:40], v.count(old))
    v = v.replace(old, new)
open('verify_r120.py', 'wb').write(v)
c = open('cert-r120p.py', 'rb').read()
cr = [
    (b'PAY_SHA1_12 = "343226e27ebf"', b'PAY_SHA1_12 = "a5aa77dc90a3"'),
    (b'PAY_SIZE = 5138', b'PAY_SIZE = 5287'),
    (b'POST = 853982', b'POST = 854131'),
    (b'POST_SHA1 = "d5e2e67c0a63ad3b0bce6034f2985ea94b9f3274"',
     b'POST_SHA1 = "f5a761c55396faf78bb5f6d74693c5193bafbea0"'),
]
for old, new in cr:
    assert c.count(old) == 1, ('cert', old[:40], c.count(old))
    c = c.replace(old, new)
open('cert-r120p.py', 'wb').write(c)
print('postR5', pin('verify_r120.py'), pin('cert-r120p.py'))
log = open('verify_repair_log.txt', 'ab')
log.write((
"## R5 (supersession re-pin, 2026-11-23): payload r2 (paragraph-5 scope fix per R4 findings A/B/C)\r\n"
"regenerates to a5aa77dc90a3/5287 (was 343226e27ebf/5138). Constant-only re-pins, no logic edits:\r\n"
"verify_r120.py P1 payload pin + P8 ceiling (5191 -> 5340, chain-119 +53 margin kept; preR5 copy\r\n"
"verify_r120-preR5.py 4d751ac4afb8/39745); cert-r120p.py PAY_SHA1_12/PAY_SIZE/POST/POST_SHA1\r\n"
"(POST 853982 -> 854131 = 848842+5287+2, POST_SHA1 f5a761c55396faf78bb5f6d74693c5193bafbea0 from\r\n"
"gen; preR5 copy cert-r120p-preR5.py 1bf4a61b1597/4781). Deviation from dispatch spec noted: R5\r\n"
"covered P1 and cert pins in addition to the P8 ceiling, since both pinned the superseded bytes.\r\n"
).encode('ascii'))
log.close()
print('R5 log appended')
