# ordinal_scan_104.py -- proposal 104 r1: anchor and ordinal-safety scan of live appH bytes.
# Verifies: (1) PRE identity; (2) the two line-initial occurrences of \emph{Vacuum term.}
# (hazard: NEVER pin on it alone); (3) the PIN built from the 103 closer clause
# "they derive no slot law from the core action" through CRLFCRLF to the line-initial
# Vacuum header is unique; (4) ORDINAL SAFETY: for the insertion slot immediately AFTER the
# 103 paragraph and BEFORE the Vacuum-term paragraph, every "Nth preceding paragraph"
# referent in every downstream paragraph (down to EOF) still counts to a paragraph
# DOWNSTREAM of the slot, so no backward ordinal crosses the insertion point.
# Also records, for the record, the upstream ordinals (unchanged by construction: all their
# targets lie strictly above the slot). Prints line numbers + short prefixes only (context
# discipline). Run from repo root:
#   python -I proposals/104-g-slot-frame-joint-law/ordinal_scan_104.py
import hashlib
import re
import sys

APP = "chapters/appH-microscopic-proofs.tex"
data = open(APP, "rb").read()
sha16 = hashlib.sha256(data).hexdigest()[:16]
print("PRE bytes", len(data), "sha256-16", sha16, "CRLF", data.count(b"\r\n"),
      "bareLF", data.count(b"\n") - data.count(b"\r\n"), "BOM", data[:3] == b"\xef\xbb\xbf")
if not (len(data) == 805839 and sha16 == "21163962e4f7f514" and data.count(b"\r\n") == 3870
        and data.count(b"\n") - data.count(b"\r\n") == 0):
    print("PRE MISMATCH"); sys.exit(1)

# (2) Vacuum-term header occurrences, with line-initiality
VAC = rb"\emph{Vacuum term.}"
occ = [m.start() for m in re.finditer(re.escape(VAC), data)]
print("Vacuum-term header occurrences:", len(occ))
for off in occ:
    ls = data.rfind(b"\r\n", 0, off) + 2
    ln = data.count(b"\r\n", 0, off) + 1
    print("  offset", off, "line", ln, "line-initial", ls == off)
if len(occ) != 2:
    print("HAZARD SCAN UNEXPECTED (expected the two recorded occurrences)"); sys.exit(1)

# (3) PIN: from the 103 closer clause through CRLFCRLF to the Vacuum header prefix
CLAUSE = b"they derive no slot law from the core action"
VACLINES = [off for off in occ if data.rfind(b"\r\n", 0, off) + 2 == off]
print("clause occurrences:", data.count(CLAUSE))
if data.count(CLAUSE) != 1:
    print("PIN SOURCE NOT UNIQUE"); sys.exit(1)
ci = data.find(CLAUSE)
vac_line_start = None
for off in VACLINES:
    if off > ci:
        vac_line_start = off
        break
PIN = data[ci:vac_line_start + len(VAC)]
print("PIN bytes", len(PIN), "count", data.count(PIN))
print("PIN head 60B", PIN[:60])
print("PIN tail 80B", PIN[-80:])
if data.count(PIN) != 1:
    print("PIN NOT UNIQUE"); sys.exit(1)
# structural: between clause and Vacuum line there must be exactly the clause-end CRLF,
# the end of the 103 line, and ONE blank line (regional separator idiom)
gap = data[ci + len(CLAUSE):vac_line_start]
print("gap bytes between clause end and Vacuum line start:", gap)
if gap != b" they supply no state and no selected profile, they leave the missing steps (i)-(iv) of the Missing step paragraph unchanged, and they close nothing in Problem~G.\r\n\r\n":
    print("UNEXPECTED gap structure; clause is not in the closer position assumed"); sys.exit(1)
print("cut offset (Vacuum line start):", vac_line_start)

# (4) ordinal safety. Split downstream region (from cut to EOF) into LaTeX paragraphs:
# runs of nonempty lines separated by blank lines. Walk paragraphs; for each ordinal
# phrase "Nth preceding paragraph" (and "preceding paragraph" with no ordinal = 1st),
# require the count to stay inside the downstream region (strictly-after-slot paragraphs).
ORD = re.compile(r"(first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|eleventh|twelfth|thirteenth|fourteenth|fifteenth|sixteenth|seventeenth|eighteenth|nineteenth|twentieth) preceding paragraph")
NTH = {"first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5, "sixth": 6, "seventh": 7,
       "eighth": 8, "ninth": 9, "tenth": 10, "eleventh": 11, "twelfth": 12, "thirteenth": 13,
       "fourteenth": 14, "fifteenth": 15, "sixteenth": 16, "seventeenth": 17, "eighteenth": 18,
       "nineteenth": 19, "twentieth": 20}

def paragraphs_from(off):
    # paragraphs of the region data[off:], paragraph = line (this block is one-line-paragraph style)
    tail = data[off:]
    lines = tail.split(b"\r\n")
    paras = []
    cur = []
    startline = data.count(b"\r\n", 0, off) + 1  # 1-based line number of region line 0
    for i, ln in enumerate(lines):
        if ln.strip() == b"":
            if cur:
                paras.append((startline + cur[0], b"\r\n".join([l for l in [cur[0] and ln and None or None] or []])))
                cur = []
        else:
            cur.append((i, ln))
    # simpler: this file uses one-line paragraphs in this region; verify that assumption
    return paras

# Region style check: every nonblank line in the downstream region is a complete paragraph
# (blank lines between). Verify no wrapped-paragraph continuation: in appH this block and
# all of ch17-adjacent sections use one logical paragraph per line; confirm by checking
# that every line after a blank one starts with \emph or \paragraph or \section or is a
# closer/citation-type single line. Instead, do the scan purely by LINES (== paragraphs):
region_lines = data[vac_line_start:].split(b"\r\n")
region_start_line = data.count(b"\r\n", 0, vac_line_start) + 1  # 1-based file line of Vacuum line
parapics = []  # (file_line, text) for nonblank lines == paragraphs (style verified below)
prev_blank = True
wrapped = []
for i, ln in enumerate(region_lines):
    if ln.strip() == b"":
        prev_blank = True
        continue
    if not prev_blank:
        wrapped.append((region_start_line + i, ln[:60]))
    parapics.append((region_start_line + i, ln))
    prev_blank = False
print("region nonblank paragraphs:", len(parapics), " lines NOT following a blank (possible wrapped continuations):", len(wrapped))
for t in wrapped[:10]:
    print("  wrapped?", t)

bad = []
for (fline, txt) in parapics:
    # count how many paragraphs strictly between this one and the slot (Vacuum line is index 0)
    k = parapics.index((fline, txt))  # paragraphs after slot before this one: k
    for m in ORD.finditer(txt.decode("utf-8", errors="replace")):
        n = NTH[m.group(1)]
        # this paragraph is parapics[k]; its Nth preceding paragraph counts back through
        # the file. In POST, one paragraph (the insert) is added at index 0 boundary, so a
        # target at file-rank r (paragraphs back) lands in the inserted region iff n > k.
        if n > k:
            bad.append((fline, m.group(0), "needs", n, "paragraphs back, only", k, "downstream"))
    # bare "preceding paragraph" (no ordinal) = 1st preceding: crosses iff k == 0
    for m in re.finditer(r"preceding paragraph", txt.decode("utf-8", errors="replace")):
        pre = txt[:m.start()].decode("utf-8", errors="replace")
        if not re.search(r"(first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|eleventh|twelfth|thirteenth|fourteenth|fifteenth|sixteenth|seventeenth|eighteenth|nineteenth|twentieth)$", pre.strip() + "\x00"[0:0] if False else (pre.strip() + "END")):
            pass
    for m in re.finditer(r"(first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|eleventh|twelfth|thirteenth|fourteenth|fifteenth|sixteenth|seventeenth|eighteenth|nineteenth|twentieth|preceding)", txt.decode("utf-8", errors="replace")):
        pass
print("downstream crossings of the proposed slot (Nth-preceding with N > paragraphs-since-slot):", len(bad))
for b in bad:
    print("  CROSSING:", b)

# bare "preceding paragraph" handling (1st preceding crosses iff the paragraph is the
# first downstream one, i.e. k == 0)
for (fline, txt) in parapics:
    k = [p[0] for p in parapics].index(fline)
    s = txt.decode("utf-8", errors="replace")
    for m in re.finditer(r"(?<![a-z])(?<!first )(?<!second )(?<!third )(?<!fourth )(?<!fifth )(?<!sixth )(?<!seventh )(?<!eighth )(?<!ninth )(?<!tenth )preceding paragraph", s):
        # was there an ordinal word right before? ORD regex already covered those; here catch bare ones
        pre = s[max(0, m.start() - 12):m.start()]
        if not any(w in pre for w in ["first", "second", "third", "fourth", "fifth", "sixth",
                                      "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]):
            print("bare 'preceding paragraph' at line", fline, "paragraph index k =", k)
            if k == 0:
                bad.append((fline, "bare preceding paragraph crosses slot", 1, "vs", k))
# also "second preceding" style multi-word already in ORD; check "Nth and Mth preceding" forms captured
# (a) paragraph-header styles that reset ordinals: record \section/\subsection boundaries in region
for (fline, txt) in parapics[:6]:
    print("region head para line", fline, txt[:60])
if bad:
    print("ORDINAL SCAN: SLOT NOT SAFE"); sys.exit(1)
print("ORDINAL SCAN: SLOT SAFE (no downstream backward ordinal crosses the slot)")
print("SCAN DONE")
