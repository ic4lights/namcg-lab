"""082 r2 POST-pin recorder: in-memory splice of insert-r2.tex (anchor contract
identical to simulate_apply_082_r2.py), prints the FULL sha256 for the manifest.
No write performed. Run: python -I proposals/082-g-moments-uniformmin/post_pin_full_r2.py"""
import hashlib
APPH = 'chapters/appH-microscopic-proofs.tex'
INS = 'proposals/082-g-moments-uniformmin/insert-r2.tex'
H081 = r'\emph{Charge-to-edge moment identification'


def main():
    lines = open(APPH, 'rb').read().decode('utf-8').split('\r\n')
    ib = open(INS, 'rb').read()
    assert len(ib) == 2029 and ib[-2:] == b'\r\n' and ib.count(b'\n') == 1
    h = next(i for i, L in enumerate(lines) if L.startswith(H081))
    cand = [i for i, L in enumerate(lines)
            if i > h and L.startswith(r'\emph{Vacuum term.}')]
    assert len(cand) == 1, cand
    ia = cand[0]
    assert lines[ia - 1] == '' and lines[ia - 2] != ''
    nb = '\r\n'.join(lines[:ia] + [ib.decode('utf-8')[:-2], ''] + lines[ia:])
    nb = nb.encode('utf-8')
    full = hashlib.sha256(nb).hexdigest()
    assert len(nb) == 731183 and nb.count(b'\r\n') == 3830
    assert nb.replace(b'\r\n', b'').count(b'\n') == 0
    print('POST FULL size %d sha256 %s sha8 %s; insert lands line %d'
          % (len(nb), full, full[:8], ia + 1))
    print('no write performed')


if __name__ == '__main__':
    main()
