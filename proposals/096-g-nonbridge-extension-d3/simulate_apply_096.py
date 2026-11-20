import hashlib
from pathlib import Path
APPH = Path("chapters/appH-microscopic-proofs.tex")
INS = Path("proposals/096-g-nonbridge-extension-d3/insert-r1.tex")
PRE_SIZE, PRE_SHA, PRE_CRLF = 776019, "600588c1d1087232ace2cea1cdecf13fb38885cf7a2126a72eedfdc1234bfa0d", 3854
VAC = b"\emph{Vacuum term.}"
IDIOM = b"close nothing in Problem~G."
HEAD = b"These statements are exact linear-algebraic identifiability statements"
ok = 0
def chk(tag, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + tag)
    ok += 0 if cond else 1
data = APPH.read_bytes()
chk("PRE_SIZE", len(data) == PRE_SIZE)
chk("PRE_SHA", hashlib.sha256(data).hexdigest() == PRE_SHA)
chk("PRE_CRLF", data.count(b"\r\n") == PRE_CRLF)
chk("PRE_bareLF", data.count(b"\n") - data.count(b"\r\n") == 0)
if ok == 0:
    line = data.split(b"\r\n")[3202]
    j = line.index(HEAD)
    tail = line[j:]
    assert tail.endswith(IDIOM)
    print("PIN_TAIL %d bytes, head ok, end ok" % len(tail))
    PIN = tail + b"\r\n\r\n" + VAC
    chk("PIN_count_1", data.count(PIN) == 1)
    cut = data.index(PIN) + len(tail) + 4
    chk("CUT_lineinitial", data[cut:cut+len(VAC)] == VAC and data[cut-2:cut] == b"\r\n")
    ins = INS.read_bytes()
    chk("INS_terminal_crlf", ins.endswith(b"\r\n"))
    POST = data[:cut] + ins + b"\r\n" + data[cut:]
    chk("POST_SIZE", len(POST) == PRE_SIZE + len(ins) + 2)
    chk("POST_counts", POST.count(IDIOM) == 22 and POST.count(b"closes nothing") == 1 and POST.count(VAC) == 2)
    chk("POST_bareLF", POST.count(b"\n") - POST.count(b"\r\n") == 0)
    chk("POST_CRLF", POST.count(b"\r\n") == PRE_CRLF + 2)
    chk("PREFIX_SUFFIX", POST.startswith(data[:cut]) and POST.endswith(data[cut:]))
    print("INSERT_SIZE %d INSERT_SHA8 %s" % (len(ins), hashlib.sha256(ins).hexdigest()[:8]))
    print("POST_SIZE %d" % len(POST))
    print("POST_SHA256 %s" % hashlib.sha256(POST).hexdigest())
    print("POST_CRLF %d POST_bareLF %d" % (POST.count(b"\r\n"), POST.count(b"\n") - POST.count(b"\r\n")))
print("SUMMARY " + ("ALL PASS" if ok == 0 else "FAILURES %d" % ok))
raise SystemExit(0 if ok == 0 else 1)
