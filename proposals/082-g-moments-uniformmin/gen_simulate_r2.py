"""082 r2: derive simulate_apply_082_r2.py from the FROZEN simulate_apply_082.py
(reads only; writes the single new file). Exactly two content changes:
 (1) BANNED -> seven-word standard incl. 'derived' (F4);
 (2) INS pin -> insert-r2.tex size 2029 + sha256 9342a7be34ea... (F1 re-pin;
     docstring run-command updated to the new filename to match the new file).
Run from repo root: python -I proposals/082-g-moments-uniformmin/gen_simulate_r2.py"""
import hashlib
SRC = 'proposals/082-g-moments-uniformmin/simulate_apply_082.py'
DST = 'proposals/082-g-moments-uniformmin/simulate_apply_082_r2.py'
B_OLD = "BANNED = ['status', 'priority', 'completion', 'open', 'critical', 'programme']"
B_NEW = ("BANNED = ['status', 'priority', 'completion', 'open', 'critical', "
         "'programme', 'derived']")
I_OLD = "INS = 'proposals/082-g-moments-uniformmin/insert-r1.tex'"
I_NEW = "INS = 'proposals/082-g-moments-uniformmin/insert-r2.tex'"
S_OLD = ("INS_SHA = 'edec101f2695deadc965aa31d11496adaece6f58e37f12546317be7"
         "ff3d00690'")
S_NEW = ("INS_SHA = '9342a7be34ea588defdaf6efd465c6617f5e4d1bebe4f45e00c8f92"
         "18f37414e'")
D_OLD = "byte contract of insert-r1.tex against the"
D_NEW = "byte contract of insert-r2.tex (r2, F1 fix) against the"
C_OLD = "simulate_apply_082.py\"\"\""
C_NEW = "simulate_apply_082_r2.py\"\"\""


def main():
    src = open(SRC, 'r', encoding='utf-8', newline='').read()
    for o in (B_OLD, I_OLD, S_OLD, D_OLD, C_OLD):
        assert src.count(o) == 1, ('anchor not unique', o[:40])
    out = src.replace(B_OLD, B_NEW).replace(I_OLD, I_NEW).replace(S_OLD, S_NEW)
    out = out.replace(D_OLD, D_NEW).replace(C_OLD, C_NEW)
    open(DST, 'w', encoding='utf-8', newline='').write(out)
    ob = out.encode('utf-8')
    print('GEN OK bytes %d sha8 %s' % (len(ob), hashlib.sha256(ob).hexdigest()[:8]))


if __name__ == '__main__':
    main()
