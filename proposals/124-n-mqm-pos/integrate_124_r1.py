# Integrator splice for proposal 124 (n-mqm-pos), round 2 accepted text.
# Canonical splice: content.replace(anchor, payload + anchor, 1) on raw bytes.
# Refuses to write unless every pin and the expected-post byte-equality hold.
import hashlib
import sys

ROOT = r"C:\Users\redgi\Projects\namcg-lab@gpu"
TARGET = ROOT + r"\chapters\appH-microscopic-proofs.tex"
PAYLOAD = ROOT + r"\proposals\124-n-mqm-pos\payload-124.txt"
EXPECTED = ROOT + r"\proposals\124-n-mqm-pos\spliced_appH_124.bin"

ANCHOR = b"\\paragraph{The named completion class and the remainder bound.}"

PRE_SHA1 = "ba72024aba4d26aff3fd5ad5a1219cdd5a1bd1e1"
PRE_SIZE = 869275
PAYLOAD_SHA1 = "8a86b389f85999161f8c7488064e13e9d1b8340c"
PAYLOAD_SIZE = 5831
POST_SHA1 = "76d862968c31d78fffc665f72aaf60d40c90367a"
POST_SIZE = 875106


def sha1(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()


def fail(msg: str) -> None:
    print("ASSERTION FAILED: " + msg)
    sys.exit(1)


with open(TARGET, "rb") as f:
    content = f.read()
with open(PAYLOAD, "rb") as f:
    payload = f.read()
with open(EXPECTED, "rb") as f:
    expected = f.read()

# Pre-state pins
if sha1(content) != PRE_SHA1:
    fail("PRE sha1 %s != %s" % (sha1(content), PRE_SHA1))
if len(content) != PRE_SIZE:
    fail("PRE size %d != %d" % (len(content), PRE_SIZE))
if sha1(payload) != PAYLOAD_SHA1:
    fail("payload sha1 %s != %s" % (sha1(payload), PAYLOAD_SHA1))
if len(payload) != PAYLOAD_SIZE:
    fail("payload size %d != %d" % (len(payload), PAYLOAD_SIZE))

# Anchor exactly once; payload must end CRLF so the join is a clean insertion
n = content.count(ANCHOR)
if n != 1:
    fail("anchor count %d != 1" % n)
if not payload.endswith(b"\r\n"):
    fail("payload does not end CRLF")

result = content.replace(ANCHOR, payload + ANCHOR, 1)

# Post-state pins: hash, size, AND byte-equality against the certified bin
if sha1(result) != POST_SHA1:
    fail("POST sha1 %s != %s" % (sha1(result), POST_SHA1))
if len(result) != POST_SIZE:
    fail("POST size %d != %d" % (len(result), POST_SIZE))
if result != expected:
    fail("POST not byte-identical to spliced_appH_124.bin")

# Pure-insertion sanity: removing the payload reproduces PRE exactly
check = result.replace(payload + ANCHOR, ANCHOR, 1)
if check != content:
    fail("reverse splice does not reproduce PRE bytes")

with open(TARGET, "wb") as f:
    f.write(result)

print("SPLICE OK")
print("PRE   sha1 %s size %d" % (PRE_SHA1, PRE_SIZE))
print("POST  sha1 %s size %d" % (POST_SHA1, len(result)))
print("byte-identical to spliced_appH_124.bin: True")
