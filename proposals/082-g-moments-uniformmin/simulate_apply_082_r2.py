"""082 simulate_apply: READ-ONLY byte contract of insert-r2.tex (r2, F1 fix) against the
LIVE chapters/appH-microscopic-proofs.tex. No write performed.
Run from repo root: python -I proposals/082-g-moments-uniformmin/simulate_apply_082_r2.py"""
import glob
import hashlib

APPH = 'chapters/appH-microscopic-proofs.tex'
INS = 'proposals/082-g-moments-uniformmin/insert-r2.tex'
PRE = dict(size=729152,
           sha256='5d52b67252b152751709dd2f7d22ccdd29e77df131d60fd43432d7583463a303',
           crlf=3828, barelf=0)
INS_SIZE = 2029
INS_SHA = '9342a7be34ea588defdaf6efd465c6617f5e4d1bebe4f45e00c8f9218f37414e'

BANNED = ['status', 'priority', 'completion', 'open', 'critical', 'programme', 'derived']
CLOSING = 'they close nothing in Problem~G.'
HDR = r'\emph{Uniform minimiser of the obstruction factor over profiles.}'


def main():
    b = open(APPH, 'rb').read()
    sha = hashlib.sha256(b).hexdigest()
    assert len(b) == PRE['size'], ('PRE size', len(b))
    assert sha == PRE['sha256'], ('PRE sha', sha[:16])
    assert b.count(b'\r\n') == PRE['crlf'], 'PRE CRLF'
    assert b.replace(b'\r\n', b'').count(b'\n') == PRE['barelf'], 'PRE bareLF'
    allch = sum(open(f, encoding='utf-8').read().count(HDR)
                for f in glob.glob('chapters/**/*.tex', recursive=True))
    assert allch == 0, ('header collision all-chapters', allch)
    lines = b.decode('utf-8').split('\r\n')
    n081 = sum(1 for L in lines if L.startswith(r'\emph{Charge-to-edge moment identification'))
    nvac = sum(1 for L in lines if L.startswith(r'\emph{Vacuum term.}'))
    assert n081 == 1, ('081 header pin', n081)
    assert nvac == 2, ('Vacuum line-start count', nvac)
    ib = open(INS, 'rb').read()
    assert len(ib) == INS_SIZE, ('INS size', len(ib))
    isha = hashlib.sha256(ib).hexdigest()
    assert isha == INS_SHA, ('INS sha', isha[:16])
    assert not [i for i, v in enumerate(ib[:-2]) if v < 0x20], 'INS control byte'
    assert ib[-2:] == b'\r\n' and ib[:3] != b'\xef\xbb\xbf'
    il = ib.decode('utf-8').split('\r\n')
    assert il[-1] == '' and len(il) == 2, 'insert must be one CRLF-terminated line'
    line = il[0]
    low = line.lower()
    for w in BANNED:
        assert w not in low, ('banned word', w)
    assert line.count(CLOSING) == 1, 'closing idiom count'
    for tok in ['$', '[', ']', r'\cite', r'\ref', r'\label', r'\eqref']:
        assert tok not in line, ('banned token', tok)
    assert line.count(r'\emph{') == 1, 'emph header count'
    h081 = next(i for i, L in enumerate(lines)
                if L.startswith(r'\emph{Charge-to-edge moment identification'))
    cand = [i for i, L in enumerate(lines)
            if i > h081 and L.startswith(r'\emph{Vacuum term.}')]
    assert len(cand) == 1, ('G-side Vacuum anchor', cand)
    ia = cand[0]
    assert lines[ia - 1] == '' and lines[ia - 2] != '', 'blank-CRLF separation'
    out = lines[:ia] + [line, ''] + lines[ia:]
    nb = '\r\n'.join(out).encode('utf-8')
    assert nb.count(b'\r\n') == PRE['crlf'] + 2 and nb.replace(b'\r\n', b'').count(b'\n') == 0
    print('PRE OK size %d sha8 %s CRLF %d bareLF 0 header-collide 0 081-pin 1 vacuum 2'
          % (len(b), sha[:8], PRE['crlf']))
    print('POST computed size %d sha8 %s CRLF %d bareLF 0; insert lands line %d'
          % (len(nb), hashlib.sha256(nb).hexdigest()[:8], nb.count(b'\r\n'), ia + 1))
    print('no write performed')


if __name__ == '__main__':
    main()
