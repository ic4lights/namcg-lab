# assemble_r1.resume.py -- concatenates .p1..p4 into proposal-r1.md and splices the
# verbatim payload-126-v2.txt bytes at the @@PAYLOAD_V2@@ placeholder (no retyping).
import hashlib, io

parts = []
for name in (".p1.md", ".p2.md", ".p3.md", ".p4.md"):
    parts.append(open(name, encoding="utf-8").read())
doc = "".join(parts)
assert doc.count("@@PAYLOAD_V2@@") == 1, "placeholder"

pay = open("payload-126-v2.txt", "rb").read()
assert pay.endswith(b"\r\n"), "payload terminator"
pay_sha = hashlib.sha1(pay).hexdigest()
assert pay_sha == "b9ebeba71fe933b1048dbcd2a0ec4f46d89c54dd" and len(pay) == 4447, "v2 pin"
body = pay[:-2].decode("ascii")  # strip the single trailing CRLF for the fenced block

doc = doc.replace("@@PAYLOAD_V2@@", body)
assert "@@PAYLOAD" not in doc
out = doc.encode("utf-8")
open("proposal-r1.md", "wb").write(out)
print("R1-WRITTEN", len(out), hashlib.sha1(out).hexdigest())
print("PAYLOAD-EMBEDDED-SHA1", pay_sha)
# sanity: the embedded fenced block byte-matches the payload file
i = doc.index("````latex\n") + len("````latex\n")
j = doc.index("\n````", i)
emb = (doc[i:j] + "\r\n").encode("ascii")
print("EMBED-MATCHES-PAYLOAD", emb == pay)
