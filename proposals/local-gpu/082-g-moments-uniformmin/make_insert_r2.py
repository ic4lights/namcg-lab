"""082 round 2 F1 byte surgery: insert-r1.tex -> insert-r2.tex.
One-character display fix k=1 -> k=0 in the uniform-value product, never retyped.
Run from repo root: python -I proposals/082-g-moments-uniformmin/make_insert_r2.py"""
import hashlib
R1 = 'proposals/082-g-moments-uniformmin/insert-r1.tex'
R2 = 'proposals/082-g-moments-uniformmin/insert-r2.tex'
R1_SHA = 'edec101f2695deadc965aa31d11496adaece6f58e37f12546317be7ff3d00690'
OLD = rb'D^{-p}\prod_{k=1}^{p-1}(D+k)'
NEW = rb'D^{-p}\prod_{k=0}^{p-1}(D+k)'


def main():
    d = open(R1, 'rb').read()
    assert len(d) == 2029, ('r1 size', len(d))
    assert hashlib.sha256(d).hexdigest() == R1_SHA, 'r1 sha pin'
    assert d.count(OLD) == 1, ('old-form count', d.count(OLD))
    assert d.count(NEW) == 0, 'new form already present'
    n = d.replace(OLD, NEW, 1)
    assert len(n) == 2029, ('r2 size', len(n))
    diff = [i for i in range(2029) if n[i] != d[i]]
    assert len(diff) == 1 and d[diff[0]] == 0x31 and n[diff[0]] == 0x30, \
        ('not a single 1->0 byte', diff[:4])
    assert not [i for i, v in enumerate(n[:-2]) if v < 0x20], 'control byte in body'
    assert n[-2:] == b'\r\n' and n[:3] != b'\xef\xbb\xbf', 'terminal CRLF / no BOM'
    open(R2, 'wb').write(n)
    print('R1 PIN OK size 2029 sha8 edec101f; one-byte diff at %d (0x31->0x30)'
          % diff[0])
    print('INSERT2 size %d sha256 %s' % (len(n), hashlib.sha256(n).hexdigest()))


if __name__ == '__main__':
    main()
