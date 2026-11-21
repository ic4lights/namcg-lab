# mk_r2_sentence_check.py -- one-shot (round 2): extract the gatekeeper replacement
# sentence from the ```latex fence under "## Corrected snippet" in review-r1.md, splice it
# into the live insert-r1.tex line by locating the span "In the five-structure" ...
# "remains open." (inclusive), and check the spliced line against the gatekeeper candidate
# scratch/gk105/insert_r2_candidate.tex. Prints everything; writes nothing except the
# diagnostic scratch copy of the new sentence.
# Run from repo root: python -I proposals/105-a-map-order2-associator-correction/mk_r2_sentence_check.py
import hashlib

P = r"proposals\105-a-map-order2-associator-correction"
CAND = r"scratch\gk105\insert_r2_candidate.tex"

rev = open(P + r"\review-r1.md", "rb").read().decode("utf-8")
i = rev.index("## Corrected snippet")
j = rev.index("```latex", i) + len("```latex")
k = rev.index("```", j)
sent = rev[j:k].strip("\r\n")
print("fence sentence content bytes:", len(sent.encode("utf-8")))
print("fence sentence ascii:", all(ord(c) < 128 for c in sent))
print("apostrophe codepoint in Kontsevich's:",
      ord(sent[sent.index("Kontsevich") + len("Kontsevich")]))

r1 = open(P + r"\insert-r1.tex", "rb").read()
assert r1.endswith(b"\r\n") and r1.count(b"\r\n") == 1
line = r1.decode("ascii").rstrip("\r\n")
a = line.index("In the five-structure")
b = line.index("remains open.") + len("remains open.")
old = line[a:b]
print("old sentence span [%d:%d] bytes:" % (a, b), len(old.encode("utf-8")))
print("OLD:", old)
print("NEW:", sent)

new_line = line[:a] + sent + line[b:]
print("new content len:", len(new_line), "braces %d/%d" %
      (new_line.count("{"), new_line.count("}")))

cand = open(CAND, "rb").read()
built = (new_line + "\r\n").encode("ascii")
print("CANDIDATE MATCH:", built == cand,
      "| cand size", len(cand), "sha256/16", hashlib.sha256(cand).hexdigest()[:16],
      "| built size", len(built), "sha256/16", hashlib.sha256(built).hexdigest()[:16])

for bad in ("Dolgushev", "0410417", "Cattaneo", "Felder", "Lecomte",
            r"\label", r"\ref", r"\eqref", r"\cite", "In the five-structure"):
    assert bad not in new_line, "forbidden string present: " + bad
print("forbidden-string check: OK")
print("counts: does-not-close=%d does/derive=%d" %
      (new_line.count("does not close Problem~A"),
       new_line.count("do not derive") + new_line.count("does not derive")))
