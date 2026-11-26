# assemble_r2.py -- programmatic assembly of proposal-r2.md from three part files plus
# verbatim disk-byte embeds (no retyping): payload-126-v3.txt (with PAYLOAD-EMBEDDED-SHA1
# guard, assemble_r1.resume.py precedent) and out-diff-v2v3.txt. Output CRLF, ASCII.
import hashlib

def rd(f): return open(f, "rb").read().decode("ascii")

pay = open("payload-126-v3.txt", "rb").read()
assert pay.endswith(b"\r\n") and not pay.endswith(b"\r\n\r\n")
sha = hashlib.sha1(pay).hexdigest()
body = pay[:-2].decode("ascii")
assert (body + "\r\n").encode("ascii") == pay, "embed byte-fidelity"
payblock = ("PAYLOAD-EMBEDDED-SHA1 " + sha + " BYTES " + str(len(pay)) +
            " EMBED-MATCHES-PAYLOAD True\n"
            "(the disk file is exactly the single line below plus one CRLF terminator)\r\n"
            "```\r\n" + body + "\r\n```")

dif = rd("out-diff-v2v3.txt").rstrip("\r\n")
difblock = "```\r\n" + dif + "\r\n```"

doc = rd("r2part1.md") + "\r\n" + rd("r2part2.md") + "\r\n" + rd("r2part3.md")
assert doc.count("@ @PAYLOAD@ @") == 1, "payload marker"
assert doc.count("@ @DIFF@ @") == 1, "diff marker"
doc = doc.replace("@ @DIFF@ @", difblock)
doc = doc.replace("@ @PAYLOAD@ @", payblock)
doc = doc.replace("\r\n", "\n").replace("\n", "\r\n")
assert doc.count("@ @") == 0, "marker residue"
b = doc.encode("ascii")
open("proposal-r2.md", "wb").write(b)
print("ASSEMBLED-BYTES", len(b))
print("ASSEMBLED-SHA1", hashlib.sha1(b).hexdigest())
print("PAYLOAD-EMBEDDED-SHA1", sha)
print("ASSEMBLE-OK")
