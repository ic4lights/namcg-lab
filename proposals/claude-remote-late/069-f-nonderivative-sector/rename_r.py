"""one-off helper (already applied; idempotent): rename r -> r_c in appH_insert.tex to avoid the clash
with 'the presentation r=-2' of the merged text. Writes only inside this proposal folder."""
import os, re
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "appH_insert.tex")
s = open(p, encoding="ascii").read()
reps = [
    (r"Write \(r=c/2\chi\) and \(\kappa=2-c/\chi=2(1-r)\).", r"Write \(r_c=c/2\chi\) and \(\kappa=2-c/\chi=2(1-r_c)\)."),
    (r"\frac VT=(1-r)^2,\qquad W_R=V-T=-T\,r(2-r),", r"\frac VT=(1-r_c)^2,\qquad W_R=V-T=-T\,r_c(2-r_c),"),
    (r"exactly at \(r=1\). There,", r"exactly at \(r_c=1\). There,"),
    (r"holds only at \(r=0\) and at \(r=2\), where", r"holds only at \(r_c=0\) and at \(r_c=2\), where"),
    (r"The example has \(r=1.168\),", r"The example has \(r_c=1.168\),"),
    (r"1-r=-\frac{L'}{4\tilde U},\qquad \beta_K=\frac{2(r-1)}{4-3r+\delta},", r"1-r_c=-\frac{L'}{4\tilde U},\qquad \beta_K=\frac{2(r_c-1)}{4-3r_c+\delta},"),
    (r"requires \(r=(6+\delta)/5\), where \(V/T=(1+\delta)^2/25\); at \(r=2\),", r"requires \(r_c=(6+\delta)/5\), where \(V/T=(1+\delta)^2/25\); at \(r_c=2\),"),
    (r"the minimum is at \(r\to1\),", r"the minimum is at \(r_c\to1\),"),
]
n = 0
for a, b in reps:
    if s.count(a) == 1:
        s = s.replace(a, b); n += 1
open(p, "w", encoding="ascii", newline="\n").write(s)
print("replacements applied:", n)
print("remaining bare r tokens:", re.findall(r"[^_a-zA-Z\\]r[=)\-(\\]", s))
