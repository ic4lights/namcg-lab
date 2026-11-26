"""051 s5: mechanics of appH_insert.tex and new_bib_entries.bib against the working tree. Read-only.
ASCII, LF, no BOM; anchor once at byte level; labels and citation keys present; one closing status sentence; no process language;
no new labels; bib keys new and not duplicated.  Finds the repository by walking up, or from NAMCG_REPO."""
import os, re, sys
BS = chr(92)
here = os.path.dirname(os.path.abspath(__file__))


def find_repo():
    r = os.environ.get('NAMCG_REPO')
    if r and os.path.isfile(os.path.join(r, 'namcg-book7.tex')):
        return r
    d = here
    while True:
        if os.path.isfile(os.path.join(d, 'namcg-book7.tex')):
            return d
        n = os.path.dirname(d)
        if n == d:
            return None
        d = n


repo = find_repo()
if repo is None:
    print('SKIPPED: manuscript not found; set NAMCG_REPO')
    sys.exit(0)
raw = open(os.path.join(here, 'appH_insert.tex'), 'rb').read()
print('bytes', len(raw), 'ascii', all(b < 128 for b in raw), 'CR', raw.count(b'\r'), 'BOM', raw[:3] == b'\xef\xbb\xbf', 'ends blank line', raw.endswith(b'\n\n'))
assert all(b < 128 for b in raw) and raw.count(b'\r') == 0
txt = raw.decode()
appH = open(os.path.join(repo, 'chapters', 'appH-microscopic-proofs.tex'), 'rb').read()
anchor = (BS + 'section{Problem E: signature}').encode()
print('anchor+CRLF count', appH.count(anchor + b'\r\n'), '; anchor+LF', appH.count(anchor + b'\n'))
assert appH.count(anchor + b'\r\n') == 1
alltex = ''
for root, _, fs in os.walk(os.path.join(repo, 'chapters')):
    for f in fs:
        if f.endswith('.tex'):
            alltex += open(os.path.join(root, f), encoding='utf-8', errors='replace').read()
lab_re = re.escape(BS) + r'label\{([^}]+)\}'
labels = set(re.findall(lab_re, alltex))
refs = set(re.findall(re.escape(BS) + r'(?:eq)?ref\{([^}]+)\}', txt))
print('refs', sorted(refs), 'all defined:', refs <= labels)
assert refs <= labels
print('new labels in insert:', re.findall(lab_re, txt))
assert not re.findall(lab_re, txt)
cites = set(c.strip() for g in re.findall(re.escape(BS) + r'cite\{([^}]+)\}', txt) for c in g.split(','))
bib = open(os.path.join(repo, 'bib', 'namcg.bib'), encoding='utf-8').read()
newbib = open(os.path.join(here, 'new_bib_entries.bib'), encoding='utf-8').read()
key_re = r'@\w+\{([^,\s]+),'
oldkeys = set(re.findall(key_re, bib))
newkeys = set(re.findall(key_re, newbib))
print('cites', sorted(cites), 'in bib or new:', cites <= (oldkeys | newkeys), '; new keys', sorted(newkeys), 'already present:', sorted(newkeys & oldkeys))
assert cites <= (oldkeys | newkeys) and not (newkeys & oldkeys)
print('unused new keys:', sorted(newkeys - cites))
print('status sentences:', len(re.findall(r'remain open and PROGRAMME-CONDITIONAL', txt)), '; paragraph headings', txt.count(BS + 'paragraph{'))
assert len(re.findall(r'remain open and PROGRAMME-CONDITIONAL', txt)) == 1
for w in ('proposal', 'researcher', 'gatekeeper', 'as proposed', 'reviewer', 'this package', r'\bround\b'):
    print('  process word %r:' % w, len(re.findall(w, txt, re.I)))
print('newlines to convert', txt.count('\n'), '; bytes after CRLF', len(raw) + txt.count('\n'))
print('ALL CHECKS DONE')
